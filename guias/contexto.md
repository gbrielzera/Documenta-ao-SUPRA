# Contexto do ambiente e do usuário
Caminho: Guias > Contexto

Leia este arquivo antes de atender uma demanda: ele diz como é o ambiente do cliente e o que o
usuário espera. Tudo aqui foi observado nos 76 fluxos exportados, salvo quando indicado.

## Quem pergunta e para quê
- O usuário é estagiário e desenvolve/mantém fluxos no Supravizio da empresa (BBTS, antiga Cobra
  Tecnologia): cria fluxos, campos, papéis, scripts IronPython, consultas SQL e integrações.
- Costuma consultar pelo celular, sem o Supravizio aberto. As respostas precisam estar prontas
  para colar e testar depois; quando algo não foi testado, dizer.
- Ele valida as respostas na prática. Se ele corrigir algo, atualizar `guias/receitas.md`.

## Ambiente
- Supravizio 19.1.1 (versão dos XMLs). DLLs do Client analisadas: 18.1.1.
- Banco Oracle: usar `TO_CHAR`, `NVL`, `SYSDATE`, `||`, `ROWNUM`. `PESSOA.ATIVO` vale `'Sim'`/`'Nao'`.
- Scripts em IronPython 2.7: `except Exception as e:` funciona; sem f-string; `print` não se usa.
- Existem ambientes de Produção e Qualidade; fluxos sobem por exportação/importação de XML.

## Siglas e termos do cliente
- **OS**: Ordem de Serviço (a ocorrência de um fluxo). **UOR**: unidade organizacional (descrição do órgão da pessoa).
- **Cesec / CSC**: Centro de Serviços Compartilhados; as filas "Fila CSC - ..." são pessoas-fila que recebem as tarefas.
- **ANS/ANO**: acordo de nível de serviço / operacional. **AA**: autoatendimento (Portal).
- **DGCO**: identificador de contrato usado nos fluxos de Contratos. **IDF**: Índice de Desempenho de Fornecedores.
- **Favorecido**: a pessoa para quem a OS é aberta; **Cliente**: quem abriu.
- **Fluxo "LOTE"/"Em Lote"**: fluxo que lê planilha e abre uma OS por linha (receita 16).

## Campos customizados recorrentes (nome → onde grava)
Os nomes são genéricos e reaproveitados entre fluxos; o significado vem do rótulo dado em cada tarefa.
- `FAVORECIDO_COBRA` (25 fluxos) e `FAVORECIDO_TODOS` (24): combo de pessoa; o valor é o **ID_PESSOA** em texto → `CP_ORDEM_SERVICO`.
  Carregar com `Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))`.
- `TE_MATRICULA`, `TE_UOR`, `TE_CARGO`, `TE_FUNCAO`: dados da pessoa preenchidos por script → `CPE_CSC`.
- `SIM_NAO`, `SIM_NAO2`, `COMBOBOX`, `COMBOBOX1`...: combos genéricos; `LABEL1`, `LABEL10`: textos informativos.
- `CHECKBOX1`: usado como botão ("clique para ler a planilha"). `OBS1`, `DESCRICAO_DETALHADA`, `TEXT`: textos.
- `CNPJ`, `NOME_FORNECEDOR`, `FORNECEDOR1`, `VALOR`, `DGCO_BB`: fluxos financeiros e de contratos.
- Grids gravam em tabelas `Z_00143_<NOME_DO_GRID>` (ex.: `Z_00143_GRID_IDF`).
- Lista completa (4.317 campos, com tipo, controle, tabela e coluna): `catalogo/campos.tsv`.

## Papéis recorrentes
`Cliente` (54 fluxos), `Responsável atual` (43), `Favorecido Cobra` (19), `Fila CSC - Contratos`,
`Fila CSC - Benefícios`, `Fila CSC - Pagamentos`, `Fila CSC - Pendente de Aprovação`,
`Gerente Favorecido Cobra`, `Gerente de Centro do favorecido`, `Gestor do Cliente`, `Gestor do Responsável`.
Os papéis de gestor são "customizados por script" e partem de `FAVORECIDO_COBRA` ou do Cliente;
o gestor é achado por `CP_PESSOA.GESTOR_POSICAO` (matrícula do gestor). Ver o script de cada papel
na seção "Papéis usados" de um fluxo que o utilize.

## Tabelas e views do cliente (fora do modelo oficial)
- `CP_PESSOA`: campos customizados de Pessoa (`MATRICULA`, `CPF`, `CARGO_FUNCIONAL`, `FUNCAO_GRATIFICADA`,
  `GESTOR_POSICAO`, `DATA_DE_ADMISSAO`, `PERSON_ID`...), chave `ID_PESSOA`.
- `CAD_FUNCIONARIO_V`: view de funcionários (`NOME`, `MATRICULA`, `STATUS_MATRICULA`, `DATA_DE_DEMISSAO`).
- `CP_ORDEM_SERVICO`, `CPE_CSC`, `CPE_CONTRATOS`, `CPE_FINANCEIRO`...: campos customizados da OS. `CP_ORDEM_SERVICO` junta por `ID_OCORRENCIA` (visto em fluxos); nas `CPE_*` a chave não foi conferida.
- `SERVICES_PARAM` (`FILES_PATH` = pasta dos anexos) e `SV_PARAM`: parâmetros do sistema.
- `DEPENDENTES_BENEFICIOS_V`, `CIDADE_V`, `ESTADO_V`, `PS_*` (PeopleSoft), `MTL_*`/`ORG_*` (ERP Oracle EBS).
- Uso real de cada uma: `catalogo/tabelas_usadas_em_sql.md`. Colunas das tabelas oficiais: `catalogo/schema.txt`.

## Padrões que os fluxos do cliente seguem
- Pessoa por matrícula: `PESSOA P INNER JOIN CP_PESSOA CP ON CP.ID_PESSOA = P.ID_PESSOA WHERE CP.MATRICULA = '...'`.
- Combo de pessoa: LookupScript devolvendo `to_char(p.id_pessoa)` e o nome.
- Aprovação: tarefa com Código + Desvio Exclusivo com `OrdemServico.PossuiAprovacao("CODIGO")` e alternativas `True`/`False`.
- Integrações REST com `HttpClient` + `Newtonsoft.Json`, em módulos da Biblioteca de Scripts (`catalogo/biblioteca/api*.py`).
- Anexos: classe "Arquivo" (sigla `ARQUIVO`) na maioria; `OrdemServico.PossuiItem("ARQUIVO")` / `ObtemItem("ARQUIVO")`.
- Log: `Utils.LogError(mensagem, categoria)` e `OrdemServico.AdicionaComentario(texto, False)`.

## Dados sensíveis
Credenciais aparecem como `***MASCARADO***`. Nunca reconstituir, pedir ou sugerir valores reais.
Nomes e e-mails de pessoas que aparecem nos fluxos são dados internos: não citar sem necessidade.
