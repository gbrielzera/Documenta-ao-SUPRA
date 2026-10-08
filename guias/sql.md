# SQL no Supravizio do cliente — o que se sabe do banco real
Caminho: Guias > SQL

Fontes: export de produção em 2026-10-08 feito pelo usuário (`catalogo/schema_real.tsv`, tamanhos de
tabela, índices, valores de domínio) + documentação (`catalogo/schema.txt`, `docs/dados_*.md`, de 2018)
+ SQL dos fluxos reais. O usuário tem só `SELECT` em homologação e produção (sem insert/update/delete):
consultas que ele roda para verificar são sempre de leitura. Banco **Oracle**.

## Regras de ouro
1. **Parta da OCORRENCIA filtrada.** Ela tem 1,6 milhão de linhas; filtre por `ID_CLASSE_SUB_PROC`
   (fluxo), `SITUACAO`, `ID_CLIENTE`, `ID_RESPONSAVEL`, `DATA_HORA_CRIACAO` ou `(ID_DOMAIN, NUMERO)`,
   todos indexados, e só depois faça os joins.
2. **Tabelas CPE_* com LEFT JOIN.** Elas só têm linha para as OS que usaram algum de seus campos
   (docs/armazenando_dados_de_campos_cu.md). Com `JOIN` comum, OS sem aquele campo somem do resultado.
   Junte sempre por `ID_OCORRENCIA`.
3. **Nunca consultar sem filtro de OS** as tabelas de log gigantes: `SV_CHANGE_ITEM` (110 mi de linhas),
   `SV_CHANGE_LOG` (31 mi), `EXECUCAO_ATIVIDADE` (22 mi), `EVENTO_OCORR` (13 mi), `SV_CATEGORYLOG`,
   `SV_CHANGE_INC`, `SV_RECIPIENT`, `SV_MESSAGE`, `APONT_RESPONSAVEL`. Sempre `WHERE ID_OCORRENCIA = ...`.
4. **Sem `SELECT *`.** Liste colunas; ainda mais em `CAD_FUNCIONARIO_V` (ver "Dados sensíveis").
5. **Dentro de script**: dobrar aspas simples (`valor.replace("'", "''")`), `TO_CHAR(ID)` em listas de combo,
   `ROWNUM` em vez de `FETCH FIRST` (versão do Oracle não confirmada), nada de `;` no fim.
   O `DB` aceita parâmetros (`DB.ExecuteScalar(sql, nomes, valores)`, assinatura confirmada); a sintaxe do
   marcador (`:nome`?) não foi testada.

## Valores de domínio confirmados
- `OCORRENCIA.SITUACAO` (produção): `Aberto`, `Rascunho`, `FinalizadaSucesso`, `FinalizadaNaoRealizada`,
  `FinalizadaFalha`, `Cancelada`. "Em andamento" = `'Aberto'`; "terminada" = as três `Finalizada*`.
- `PESSOA.ATIVO`: `'Sim'` / `'Nao'` (char(3)). Três scripts do cliente usam `'S'`, que não casa com isso.
- `CP_PESSOA.MATRICULA` e `CAD_FUNCIONARIO_V.MATRICULA` são texto. Outros códigos (STATUS_MATRICULA,
  TIPO_COLABORADOR, CLASSE_NEGOCIO...) ainda não foram levantados: `guias/consultas_banco.md`.

## Índices conhecidos (o resto não foi levantado)
- `OCORRENCIA`: PK `ID_OCORRENCIA`; únicos `(ID_DOMAIN, NUMERO)`; simples em `SITUACAO`,
  `DATA_HORA_CRIACAO`, `ID_ATIVIDADE`, `ID_CLIENTE`, `ID_CLASSE_SUB_PROC`, `ID_CLASSE_SUB_PROC_INI`,
  `ID_DESENHO_PROCESSO`, `ID_FINALIZADOR`, `ID_GRUPO_TRABALHO`, `ID_CORRENCIA_PRIN`, `ID_OCORR_PAI`,
  `ID_ORGAO_CLIENTE`, `ID_RESPONSAVEL`, `ID_RESP_INICIAL`, `ID_SUB_PROCESSO`, `ID_USU_AUT`, `ID_GATEWAY`.
- `PESSOA`: PK `ID_PESSOA`; único `(ID_DOMAIN, USUARIO_REDE)` (filtre também por `ID_DOMAIN`, que nos
  XMLs vale 1, para aproveitar o índice); simples em `ID_ORGAO`, `ID_LOCAL`, `ID_USER`, entre outras.
  **Não há índice em `NOME`.**
- `CP_PESSOA`: **só a PK `ID_PESSOA`**. Buscar por `MATRICULA` varre a tabela inteira; funciona porque ela
  tem menos de 100 mil linhas (não aparece entre as maiores), mas não repita essa busca dentro de laço
  para centenas de linhas: carregue as matrículas de uma vez com `IN (...)`.

## Tamanho das tabelas (linhas, produção, 2026-10-08)
- Core: `OCORRENCIA`/`ORDEM_SERVICO` 1,60 mi; `CP_ORDEM_SERVICO` 1,54 mi; `CPE_ORDEM_SERVICO` 1,19 mi;
  `ITEM_OCORRENCIA` 2,1 mi; `APROVACAO` 922 mil; `VERSAO_APROVACAO` 808 mil; `ASSUNTO_APROVACAO` 785 mil;
  `SLA_OS` 1,4 mi; `TEMPO_ANO` 2,4 mi; `ATIVIDADE` 290 mil; `FLUXO_SEQUENCIA` 210 mil.
- Campos customizados da OS (cada `CPE_*` tem ~0,5 a 1,2 mi de linhas): `CPE_CSC` 1,17 mi, `CPE_CONTRATOS`
  1,04 mi, `CPE_FINANCEIRO` 895 mil, `CPE_PESSOAS` 986 mil, `CPE_NEGOCIOS` 1,05 mi, `CPE_BOOTCAMP` 640 mil...
- Grids `Z_00143_*`: de 130 mil a 407 mil linhas (`Z_00143_LISTA_MEDICAMENTOS` 407 mil, `..._LISTA_NF` 181 mil).
- Existem cópias de backup (`EXECUCAO_ATIVIDADE_BKP`, `CPE_PRJ_BB_BKP`, `CP_ORDEM_SERVICO_GOLIVER12*`):
  ignorar, não são as tabelas vivas.

## Limite de colunas: CP_ORDEM_SERVICO está cheia
`CP_ORDEM_SERVICO` tem exatamente **1000 colunas**, o máximo que o Oracle permite por tabela. Por isso os
campos novos de OS vão para tabelas `CPE_*`. Inferência minha, a partir do limite do Oracle e da doc:
ao criar um campo, escolher "Nome Tabela" `CPE_...` (existente ou `<Novo>`), nunca `CP_ORDEM_SERVICO`.
`CPE_CSC` tem 637 colunas, ainda com folga (não há limite de nomes para o campo, só de tabela).
Campos que os XMLs declaram e não existem no banco de produção: `catalogo/campos_vs_banco.md`.

## Tipos reais das colunas customizadas
Texto = `NVARCHAR2(500)` por padrão (há de 100, 400, 1000, 1800 e 4000), números = `NUMBER`, datas = `DATE`.
Exemplos: `CP_ORDEM_SERVICO.FAVORECIDO_COBRA` NVARCHAR2(500) (guarda o ID_PESSOA como texto),
`COMBOBOX` NVARCHAR2(1800), `COMBOBOX1` NVARCHAR2(400), `CPE_CSC.TE_MATRICULA`/`TE_UOR` NVARCHAR2(500),
`CPE_CSC.DESCRICAO_DETALHADA` NVARCHAR2(4000). Cuidado com o tamanho: valor maior que a coluna falha ao gravar.

## Consultas prontas
Estrutura conferida contra o schema real; só a 1 foi executada pelo usuário. Teste em homologação.

1. Pessoa pela matrícula (testada pelo usuário):
```sql
SELECT P.ID_PESSOA, P.NOME FROM PESSOA P
INNER JOIN CP_PESSOA CP ON CP.ID_PESSOA = P.ID_PESSOA
WHERE CP.MATRICULA = '123456'
```
2. Matrícula e UOR de uma pessoa (padrão dos fluxos de Benefícios):
```sql
SELECT CP.MATRICULA, O.DESCRICAO FROM PESSOA P
INNER JOIN CP_PESSOA CP ON CP.ID_PESSOA = P.ID_PESSOA
INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO
WHERE P.ID_PESSOA = 123
```
3. Gestor de uma pessoa: `CP_PESSOA.GESTOR_POSICAO` guarda a **matrícula do gestor** (papéis de gestor dos fluxos):
```sql
SELECT G.ID_PESSOA FROM CP_PESSOA CP
INNER JOIN CP_PESSOA G ON G.MATRICULA = CP.GESTOR_POSICAO
WHERE CP.ID_PESSOA = 123
```
Um fluxo corta `SUBSTR(GESTOR_POSICAO, 1, 6)`: o formato das duas matrículas pode diferir (ex.: sufixo).
Se não casar, comparar os valores reais de uma pessoa antes de assumir.
4. OS pelo número:
```sql
SELECT O.ID_OCORRENCIA, O.SITUACAO, O.ASSUNTO FROM OCORRENCIA O
WHERE O.ID_DOMAIN = 1 AND O.NUMERO = '12345'
```
5. OS abertas de um fluxo (pela sigla do tipo de subprocesso):
```sql
SELECT O.NUMERO, O.ASSUNTO, O.DATA_HORA_CRIACAO FROM OCORRENCIA O
INNER JOIN CLASSE_SUB_PROCESSO CS ON CS.ID_CLASSE_SUB_PROCESSO = O.ID_CLASSE_SUB_PROC
WHERE CS.SIGLA = 'ATTPERFILESPEC' AND O.SITUACAO = 'Aberto'
```
6. Já existe OS aberta deste fluxo para a matrícula (trava de duplicidade; `TE_MATRICULA` existe em `CPE_CSC`):
```sql
SELECT COUNT(*) FROM OCORRENCIA O
INNER JOIN CLASSE_SUB_PROCESSO CS ON CS.ID_CLASSE_SUB_PROCESSO = O.ID_CLASSE_SUB_PROC
INNER JOIN CPE_CSC C ON C.ID_OCORRENCIA = O.ID_OCORRENCIA
WHERE CS.SIGLA = 'ATTPERFILESPEC' AND O.SITUACAO = 'Aberto' AND C.TE_MATRICULA = '123456'
```
(INNER JOIN é correto aqui: só interessa quem tem o campo preenchido. O campo `TE_MATRICULA` só tem valor se o
fluxo o gravou; confirmar que o fluxo preenche antes de confiar na contagem.)
7. Valor de campo customizado de uma OS (LEFT JOIN, regra 2):
```sql
SELECT O.NUMERO, CP.FAVORECIDO_COBRA, C.TE_MATRICULA FROM OCORRENCIA O
LEFT JOIN CP_ORDEM_SERVICO CP ON CP.ID_OCORRENCIA = O.ID_OCORRENCIA
LEFT JOIN CPE_CSC C ON C.ID_OCORRENCIA = O.ID_OCORRENCIA
WHERE O.ID_DOMAIN = 1 AND O.NUMERO = '12345'
```
8. Mapa oficial de campos customizados no banco (nome, rótulo, tabela e coluna física):
```sql
SELECT P.NAME, P.TEXT, P.TYPE, P.CONTROL, P.TABLE_NAME, P.TABLE_COLUMN, P.LENGTH, C.NAME AS CLASSE
FROM SV_CUSTOM_PROPERTY P INNER JOIN SV_CLASS C ON C.ID_CLASS = P.ID_CLASS
WHERE P.NAME = 'COMBOBOX'
```

## CAD_FUNCIONARIO_V (view do RH, 95 colunas)
Colunas úteis: `MATRICULA`, `NOME`, `STATUS_MATRICULA`, `TIPO_COLABORADOR`, `DESC_COLABORADOR`, `POSICAO`,
`GESTOR_POSICAO`, `CARGO`, `CARGO_FUNCIONAL`, `FUNCAO_GRATIFICADA`, `SUPERVISOR`/`SUPERVISOR_ID`, `ORGANIZACAO`,
`SIGLA`, `UNIDADE_NEGOCIO`, `LOCAL`, `DATA_DE_ADMISSAO`, `DATA_DE_DEMISSAO`; hierarquia de UORs em
`NIVEL1..5`, `NUMERO_SUBCR_NIVELn`, `DESCRICAO_SUBCR_NIVELn`, `MATRICULA_SUP_NIVELn`.
Todas as colunas são anuláveis. `DATA_DE_DEMISSAO IS NULL` é como os fluxos filtram quem está ativo.

## Dados sensíveis (LGPD)
`CAD_FUNCIONARIO_V` tem CPF, identidade, PIS/PASEP, CTPS, salário e gratificação, tipo sanguíneo, endereço,
telefone e data de nascimento. Em scripts, SELECT só o que o campo precisa; nunca gravar esses valores em
comentário da OS, log ou campo visível; nunca colar resultados com pessoas reais em chat ou no repositório.
