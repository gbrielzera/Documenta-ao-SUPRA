# SQL no Supravizio do cliente — o que se sabe do banco real
Caminho: Guias > SQL

Fontes: exports de **produção** feitos pelo usuário em 2026-10-08 (`catalogo/schema_real.tsv`,
`catalogo/campos_banco.tsv`, tamanhos, índices, contagens, valores de domínio) + documentação de 2018
(`catalogo/schema.txt`, `docs/dados_*.md`) + SQL dos fluxos reais. O usuário tem só `SELECT` em
homologação e produção (sem insert/update/delete). Banco **Oracle**. Onde o repositório e o banco
divergirem, vale o banco.

## Regras de ouro
1. **Parta da OCORRENCIA filtrada.** Ela tem 1,6 milhão de linhas; filtre por `ID_CLASSE_SUB_PROC`
   (fluxo), `SITUACAO`, `ID_CLIENTE`, `ID_RESPONSAVEL`, `DATA_HORA_CRIACAO` ou `(ID_DOMAIN, NUMERO)`,
   todos indexados, e só depois faça os joins.
2. **Nunca filtre só por um campo customizado.** `CPE_*` e `CP_ORDEM_SERVICO` têm **apenas a PK
   `ID_OCORRENCIA`**: `WHERE C.TE_MATRICULA = '...'` sozinho varre 1 milhão de linhas. Reduza antes pela
   OCORRENCIA (fluxo, situação, cliente) e junte pela PK.
3. **Tabelas CPE_* com LEFT JOIN** quando precisar das OS sem o campo: elas só têm linha para as OS que
   usaram algum de seus campos (docs/armazenando_dados_de_campos_cu.md). INNER JOIN só quando a ausência
   do campo deve excluir a OS (ex.: trava de duplicidade).
4. **Nunca consultar sem filtro de OS** as tabelas de log gigantes: `SV_CHANGE_ITEM` (110 mi de linhas),
   `SV_CHANGE_LOG` (31 mi), `EXECUCAO_ATIVIDADE` (22 mi), `EVENTO_OCORR` (13 mi), `SV_CATEGORYLOG`,
   `SV_CHANGE_INC`, `SV_RECIPIENT`, `SV_MESSAGE`, `APONT_RESPONSAVEL`. Sempre `WHERE ID_OCORRENCIA = ...`.
5. **Sem `SELECT *`.** Liste colunas; ainda mais em `CAD_FUNCIONARIO_V` (ver "Dados sensíveis").
6. **Dentro de script**: dobrar aspas simples (`valor.replace("'", "''")`), `TO_CHAR(ID)` em listas de combo,
   `ROWNUM` em vez de `FETCH FIRST` (versão do Oracle não confirmada), nada de `;` no fim.
   O `DB` aceita parâmetros (`DB.ExecuteScalar(sql, nomes, valores)`, assinatura confirmada); a sintaxe do
   marcador (`:nome`?) não foi testada.

## Descobrir tabela e coluna física de um campo
O nome do campo no script (`OrdemServico["TE_MATRICULA"]`) não diz onde ele é gravado.
`grep -P "\tTE_MATRICULA\t" catalogo/campos_banco.tsv` → classe, nome, rótulo, tipo, controle, **tabela**, coluna,
tamanho em caracteres. Esse arquivo é o mapa oficial da produção (3.451 campos, 404 tabelas); o `campos.tsv`
(vindo dos XMLs) tem 868 campos que a produção não tem e 6 que apontam para outra tabela:
`catalogo/campos_vs_banco.md`. Exemplo real: `COMBOBOX3` está em **`CPE_BOOTCAMP`** na produção, não em
`CPE_CONTRATOS` como no XML do fluxo Atualizar Perfil/Especialidade. Os XMLs analisados parecem vir de
Qualidade, que tem mais campos que a produção (inferência).

## Valores de domínio confirmados (produção)
- `OCORRENCIA.SITUACAO`: `Aberto`, `Rascunho`, `FinalizadaSucesso`, `FinalizadaNaoRealizada`,
  `FinalizadaFalha`, `Cancelada`. "Em andamento" = `'Aberto'`; "terminada" = as três `Finalizada*`.
- `OCORRENCIA.CLASSE_NEGOCIO`: só `OrdemServico` (1.606.782 linhas).
- `APROVACAO.SITUACAO`: `Pendente` (154 mil), `Aprovado` (740 mil), `Reprovado` (29 mil), `Elaboracao` (1,8 mil).
- `CAD_FUNCIONARIO_V.STATUS_MATRICULA`: `ATIVO` (3.638) e `DEMITIDO` (10.235). Para quem está na empresa usar
  `STATUS_MATRICULA = 'ATIVO'`.
- `CAD_FUNCIONARIO_V.TIPO_COLABORADOR` (letra + `DESC_COLABORADOR`): A funcionário CLT (5.652), H concursado
  (4.702), E estagiário (1.354), P prestador de serviço (656), G menor aprendiz (488), T temporário (337),
  B cedido Banco do Brasil (256), L funcionários CCLP (214), R terceiro (136), O conselheiro (53),
  D diretor não empregado (20), F diretor empregado (1), e 4 linhas em branco.
- `PESSOA.ATIVO`: `'Sim'` / `'Nao'` por documentação e uso nos fluxos (15 scripts); três scripts usam `'S'`,
  que não casa. Os valores reais de `PESSOA.ATIVO`, `PESSOA.TIPO_COLABORADOR` e `PESSOA.TIPO` **ainda não
  foram levantados** (a consulta rodou sem resultado colado): `guias/consultas_banco.md`.

## Quantidade de linhas
`PESSOA` 9.646; `CP_PESSOA` 5.648; `ORGAO` 788; `CAD_FUNCIONARIO_V` 13.873 (inclui desligados).
Só parte dos funcionários tem cadastro no Supravizio (5.648 em `CP_PESSOA` contra 13.873 no RH): **uma
matrícula que existe no RH pode não existir no Supravizio**. Para achar a pessoa de uma OS valide em
`CP_PESSOA` + `PESSOA.ATIVO`, não só na view do RH.

## Índices conhecidos
- `OCORRENCIA`: PK `ID_OCORRENCIA`; único `(ID_DOMAIN, NUMERO)`; simples em `SITUACAO`,
  `DATA_HORA_CRIACAO`, `ID_ATIVIDADE`, `ID_CLIENTE`, `ID_CLASSE_SUB_PROC`, `ID_CLASSE_SUB_PROC_INI`,
  `ID_DESENHO_PROCESSO`, `ID_FINALIZADOR`, `ID_GRUPO_TRABALHO`, `ID_CORRENCIA_PRIN`, `ID_OCORR_PAI`,
  `ID_ORGAO_CLIENTE`, `ID_RESPONSAVEL`, `ID_RESP_INICIAL`, `ID_SUB_PROCESSO`, `ID_USU_AUT`, `ID_GATEWAY`.
- `ORDEM_SERVICO`: PK `ID_OCORRENCIA`; simples em `ID_FAVORECIDO`, `ID_SERVICO`, `ID_CONTRATO`, `ID_CATEGORIA`.
- `CLASSE_SUB_PROCESSO`: único `(ID_DOMAIN, SIGLA)`; `ATIVO`, `ID_ORGAO_DONO`, `ID_RESPONSAVEL`.
- `SERVICO`: único `(ID_DOMAIN, SIGLA)`; `ID_TECNICO_RESPONSAVEL`, `ID_CLASSE_SERVICO`.
- `ORGAO`: PK `ID_ORGAO`; único `(ID_DOMAIN, SIGLA)`; `ID_ORGAO_PAI`, `ID_GESTOR`, `ID_EMPRESA`.
- `PESSOA`: PK `ID_PESSOA`; único `(ID_DOMAIN, USUARIO_REDE)`; `ID_ORGAO`, `ID_LOCAL`, `ID_USER` e outros.
  **Sem índice em `NOME`.** `ID_DOMAIN` nos XMLs vale 1: inclua-o para aproveitar os índices únicos.
- `CP_PESSOA`: só a PK `ID_PESSOA` (5.648 linhas: a busca por `MATRICULA` varre tudo, barato, mas não repita
  em laço para centenas de linhas; use `IN (...)`).
- `APROVACAO`: PK `(ID_PESSOA, VERSAO, ID_ASSUNTO_APROVACAO)`; `(SITUACAO, PASSO)`; `(ID_ASSUNTO_APROVACAO, VERSAO)`;
  `ID_APROVADOR_REAL`; `ID_PESSOA`. `ASSUNTO_APROVACAO`: PK; `ID_OCORRENCIA`; `OPERACAO_ATIVIDADE`.
- `CPE_CSC`, `CP_ORDEM_SERVICO`: **só a PK `ID_OCORRENCIA`**.

## Tamanho das tabelas (linhas, produção)
- Core: `OCORRENCIA`/`ORDEM_SERVICO` 1,60 mi; `CP_ORDEM_SERVICO` 1,54 mi; `CPE_ORDEM_SERVICO` 1,19 mi;
  `ITEM_OCORRENCIA` 2,1 mi; `APROVACAO` 922 mil; `VERSAO_APROVACAO` 808 mil; `ASSUNTO_APROVACAO` 785 mil;
  `SLA_OS` 1,4 mi; `TEMPO_ANO` 2,4 mi; `ATIVIDADE` 290 mil; `FLUXO_SEQUENCIA` 210 mil.
- Campos customizados da OS: cada `CPE_*` tem de 0,4 a 1,2 mi de linhas (`CPE_CSC` 1,17 mi, `CPE_CONTRATOS`
  1,04 mi, `CPE_FINANCEIRO` 895 mil, `CPE_PESSOAS` 986 mil, `CPE_NEGOCIOS` 1,05 mi, `CPE_BOOTCAMP` 640 mil).
- Grids `Z_00143_*`: de 130 mil a 407 mil linhas (`..._LISTA_MEDICAMENTOS` 407 mil, `..._LISTA_NF` 181 mil).

## Objetos do cliente no schema (fora do modelo oficial)
Só se conhece o **número de colunas** de cada um; as colunas só foram exportadas para as 4 tabelas de `catalogo/schema_real.tsv`. Para outra tabela, pedir ao usuário a consulta 3 de `guias/consultas_banco.md`.
- **Campos customizados**: ~38 tabelas `CPE_*` (as maiores: `CPE_CSC` 637 colunas, `CPE_CONTRATOS` 304,
  `CPE_PESSOAS` 172, `CPE_PRJ_BB` 160, `CPE_CONTRATOS02` 136, `CPE_PDCI2019` 99, `CPE_DESLOCAMENTO` 68,
  `CPE_ORDEM_SERVICO` 62, `CPE_BOOTCAMP` 54, `CPE_NEGOCIOS` 50); `CP_ORDEM_SERVICO` (1000), `CP_PESSOA` (12), `CP_SERVICO` (4).
- **Grids**: ~370 tabelas `Z_00143_<NOME_DO_GRID>` (uma por campo DataGrid; 360 no mapa) e 13 `Z_00186_*`.
  O grid grava na tabela com o nome dele: `OrdemServico.GetCustom("GRID_IDF")` ↔ `Z_00143_GRID_IDF`.
- **RH / cadastro**: `SV_CAD_PESSOAS_V`, `SV_CAD_PESSOAS_NOVA`, `SV_CAD_FUNC_HIERARQ_V`, `SV_CAD_FUNC_HIERARQ_NOVA`,
  `SV_ATUALIZA_CADASTRO_PESSOAS`, `T_RH_V`, `T_SV_RH_AREAS`, `DE_PARA_CARGOS`, `VW_TEMP_PESSOAS`, `VW_TEMP_AREAS`,
  `SV_RUBRICA`, `SV_PBI_CONCURSO`, `NOTA_GDP`.
- **Views de negócio** (`VW_*`): `VW_BBTS_SV_LOCOMOCOES`, `VW_BBTS_CHAMADOS_LOCOMOCAO`, `VW_BBTS_SV_CLIENTES_EMISAO_NF`,
  `VW_BBTS_SV_LISTA_NF_COBAN`, `VW_SV_CAD_FORNECEDOR`, `VW_SV_ORCAMENTO`, `VW_TEMPO_ATENDIMENTO_ATIVIDADE` e outras.
- **Integrações**: `SV_API_COD_ETICA`, `SV_API_COJUR_DESEMPENHO_CHAMADOS`, `SV_API_NNMENSAGENS`, `SV_API_POL900`,
  `SV_CHAMADOS_GT_ESTRUTURACAO`, `SV_APONTAMENTO_SW`, `SV_DIFERIMENTO_SW`, `KEYUSER_ERP`, `LGPD_CONS_REVO_TB`.
- **Cópias e lixo (ignorar)**: `*_BKP`, `CPE_CSC_BKP20240712`, `CP_ORDEM_SERVICO_BKP`, `*_GOLIVER12*`, `*_PRD`
  (`CAD_FUNCIONARIO_V_PRD`, `PESSOA_PRD`, `ORGAO_PRD`), `ORGAO_11`, `TESTE_*`, `TMP_*`, `PLAN_TABLE`, `SNP_PLAN_TABLE`.
- **Fora do schema do Supravizio**: os fluxos consultam objetos que **não aparecem** na lista do schema
  (`owner = USER`): `CAD_FUNCIONARIO_V`, `SV_PARAM`, `CIDADE_V`, `ESTADO_V`, `DEPENDENTES_BENEFICIOS_V`, `CRONOGRAMA_DOD`,
  `TB_CUSTOM_*`, `TB_PRIORIZACAO*`, `PS_*` (PeopleSoft), `MTL_*`/`ORG_*` (ERP), `COB_GL_CENTRO`. São de outros schemas,
  acessados por sinônimo ou permissão; por isso a definição de `CAD_FUNCIONARIO_V` não saiu de `all_views`
  (consulta vazia). Confirmar dono e tipo: consulta 2 de `guias/consultas_banco.md`.

## Tamanhos: bytes no banco, caracteres no Supravizio
Em `all_tab_columns`, `data_length` de `NVARCHAR2` é em **bytes** (2 por caractere). O campo do Supravizio mostra
**caracteres**: `COMBOBOX` tem 900 caracteres no mapa e `NVARCHAR2(1800)` no banco; `COMBOBOX1` 200 → 400;
`DESCRICAO_DETALHADA` 2000 → 4000. **Texto sem tamanho definido = 250 caracteres** (500 bytes; 1.966 dos 2.460
campos de texto estão assim). O máximo prático é 2000 caracteres (4000 bytes). Valor maior que o campo falha ao gravar.
Tipos: texto = `NVARCHAR2`, inteiro/decimal = `NUMBER`, data = `DATE`.

## Limite de colunas: CP_ORDEM_SERVICO está cheia
`CP_ORDEM_SERVICO` tem exatamente **1000 colunas**, o máximo do Oracle por tabela (e há uma cópia `CP_ORDEM_SERVICO_BKP`, também com 1000).
Por isso os campos novos de OS vão para tabelas `CPE_*` (docs/armazenando_dados_de_campos_cu.md). Inferência minha:
ao criar um campo, escolher "Nome Tabela" `CPE_...` (existente com folga, ou `<Novo>`), nunca `CP_ORDEM_SERVICO`.

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
WHERE CS.ID_DOMAIN = 1 AND CS.SIGLA = 'ATTPERFILESPEC' AND O.SITUACAO = 'Aberto'
```
6. Já existe OS aberta deste fluxo para a matrícula (trava de duplicidade; `CPE_CSC.TE_MATRICULA` existe em produção):
```sql
SELECT COUNT(*) FROM OCORRENCIA O
INNER JOIN CLASSE_SUB_PROCESSO CS ON CS.ID_CLASSE_SUB_PROCESSO = O.ID_CLASSE_SUB_PROC
INNER JOIN CPE_CSC C ON C.ID_OCORRENCIA = O.ID_OCORRENCIA
WHERE CS.ID_DOMAIN = 1 AND CS.SIGLA = 'ATTPERFILESPEC' AND O.SITUACAO = 'Aberto' AND C.TE_MATRICULA = '123456'
```
INNER JOIN é correto aqui. Parte da OCORRENCIA filtrada por fluxo e situação (regra 2). O fluxo precisa gravar
`TE_MATRICULA`; confirmar antes de confiar na contagem. Para um laço de centenas de linhas, uma consulta só:
`... AND C.TE_MATRICULA IN ('111','222',...)` com `GROUP BY C.TE_MATRICULA`.
7. Valor de campo customizado de uma OS (LEFT JOIN, regra 3):
```sql
SELECT O.NUMERO, CP.FAVORECIDO_COBRA, C.TE_MATRICULA FROM OCORRENCIA O
LEFT JOIN CP_ORDEM_SERVICO CP ON CP.ID_OCORRENCIA = O.ID_OCORRENCIA
LEFT JOIN CPE_CSC C ON C.ID_OCORRENCIA = O.ID_OCORRENCIA
WHERE O.ID_DOMAIN = 1 AND O.NUMERO = '12345'
```
8. Aprovações pendentes de uma OS:
```sql
SELECT A.SITUACAO, A.PASSO, A.ID_PESSOA FROM ASSUNTO_APROVACAO AA
INNER JOIN APROVACAO A ON A.ID_ASSUNTO_APROVACAO = AA.ID_ASSUNTO_APROVACAO
WHERE AA.ID_OCORRENCIA = 123 AND A.SITUACAO = 'Pendente'
```
9. Tabela e coluna de um campo (mapa oficial, direto no banco):
```sql
SELECT P.NAME, P.TEXT, P.TABLE_NAME, P.TABLE_COLUMN, P.LENGTH, C.NAME AS CLASSE
FROM SV_CUSTOM_PROPERTY P INNER JOIN SV_CLASS C ON C.ID_CLASS = P.ID_CLASS
WHERE P.NAME = 'COMBOBOX'
```

## CAD_FUNCIONARIO_V (view do RH, 95 colunas, 13.873 linhas)
Colunas úteis: `MATRICULA`, `NOME`, `STATUS_MATRICULA`, `TIPO_COLABORADOR`, `DESC_COLABORADOR`, `POSICAO`,
`GESTOR_POSICAO`, `CARGO`, `CARGO_FUNCIONAL`, `FUNCAO_GRATIFICADA`, `SUPERVISOR`/`SUPERVISOR_ID`, `ORGANIZACAO`,
`SIGLA`, `UNIDADE_NEGOCIO`, `LOCAL`, `DATA_DE_ADMISSAO`, `DATA_DE_DEMISSAO`; hierarquia de UORs em
`NIVEL1..5`, `NUMERO_SUBCR_NIVELn`, `DESCRICAO_SUBCR_NIVELn`, `MATRICULA_SUP_NIVELn`.
Todas as colunas são anuláveis. Pode haver mais de uma linha por matrícula (13.873 linhas): confirmar antes de usar
como chave. `MATRICULA` é `VARCHAR2(11)`; em `CP_PESSOA` é `NVARCHAR2` (60 bytes).

## Dados sensíveis (LGPD)
`CAD_FUNCIONARIO_V` tem CPF, identidade, PIS/PASEP, CTPS, salário e gratificação, tipo sanguíneo, endereço,
telefone e data de nascimento. Em scripts, SELECT só o que o campo precisa; nunca gravar esses valores em
comentário da OS, log ou campo visível; nunca colar resultados com pessoas reais em chat ou no repositório.
