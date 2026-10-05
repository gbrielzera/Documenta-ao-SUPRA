# RISCO_GAP

Caminho: Customização > Modelo de dados > Processo > RISCO_GAP

Riscos adicionais do Gap

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OCORRENCIA** | Número sequencial gerado automaticamente pelo sistema para Identificar um Ocorrência | int | number(6,0) | Não |
| **SEQUENCIAL** | Número sequencia utilizado para identificar um Gap dentro de uma Ordem de Serviço de teste de Controle. | int | number(6,0) | Não |
| **ID_RISCO** | Identificador do RiscoProcesso associado | int | number(6,0) | Não |
| **ID_SUB_PROCESSO** | Identificador do RiscoProcesso associado | int | number(6,0) | Não |

Tabelas referenciadas por RISCO_GAP

| **Tabela** | **Colunas de ligação** |
|---|---|
| [RISCO_PROCESSO](dados_risco_processo) | \| **RISCO_PROCESSO** \| **RISCO_GAP** \| \|---\|---\| \| ID_RISCO \| ID_RISCO \| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |
| [GAP](dados_gap) | \| **GAP** \| **RISCO_GAP** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| \| SEQUENCIAL \| SEQUENCIAL \| |
