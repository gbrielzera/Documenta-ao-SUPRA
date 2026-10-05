# ACAO_GAP

Caminho: Customização > Modelo de dados > Processo > ACAO_GAP

Item do Plano de Ação relacionado com um Gap.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OCORRENCIA** | Número sequencial gerado automaticamente pelo sistema para Identificar um Ocorrência | int | number(6,0) | Não |
| **SEQUENCIAL** | Sequencial | int | number(6,0) | Não |
| **ID_OCOR_PLANO** | Identificador da Ocorrencia associada | int | number(6,0) | Não |

Tabelas referenciadas por ACAO_GAP

| **Tabela** | **Colunas de ligação** |
|---|---|
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **ACAO_GAP** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCOR_PLANO \| |
| [GAP](dados_gap) | \| **GAP** \| **ACAO_GAP** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| \| SEQUENCIAL \| SEQUENCIAL \| |
