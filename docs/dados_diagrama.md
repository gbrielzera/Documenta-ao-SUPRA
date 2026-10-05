# DIAGRAMA

Caminho: Customização > Modelo de dados > Processo > DIAGRAMA

Diagrama

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_DIAGRAMA** | Número sequencial gerado automaticamente pelo sistema para Identificar um Diagrama | int | number(6,0) | Não |
| **ID_SUB_PROCESSO** | Identificador do SubProcesso associado | int | number(6,0) | Não |

Tabelas referenciadas por DIAGRAMA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SUB_PROCESSO](dados_sub_processo) | \| **SUB_PROCESSO** \| **DIAGRAMA** \| \|---\|---\| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |

Tabelas que dependem de DIAGRAMA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [FIGURA](dados_figura) | \| **FIGURA** \| **DIAGRAMA** \| \|---\|---\| \| ID_DIAGRAMA \| ID_DIAGRAMA \| |
