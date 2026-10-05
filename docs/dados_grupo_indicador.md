# GRUPO_INDICADOR

Caminho: Customização > Modelo de dados > Processo > GRUPO_INDICADOR

Um Grupo de Indicadores é utilizado para classificar um Indicador de Desempenho. Também permite que Indicadores relacionados sejam agrupados na exibição feita pelo Executive Dashboard.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_GRUPO_INDICADOR** | Número sequencial gerado automaticamente pelo sistema para Identificar um Grupo Indicador. Este Identificador não pode ser modificado pelo usuário. | int | number(6,0) | Não |
| **DESCRICAO** | Texto que descreve com clareza a classificação de Indicadores. | varchar(500) | varchar(500) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas que dependem de GRUPO_INDICADOR

| **Tabela** | **Colunas de ligação** |
|---|---|
| [INDICADOR](dados_indicador) | \| **INDICADOR** \| **GRUPO_INDICADOR** \| \|---\|---\| \| ID_GRUPO_INDICADOR \| ID_GRUPO_INDICADOR \| |
