# TIPO_POSSE

Caminho: Customização > Modelo de dados > Ativos > TIPO_POSSE

Tipo de Posse

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_TIPO_POSSE** | Número sequencial gerado automaticamente pelo sistema para Identificar um Tipo de Posse | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada para o Tipo de Posse | varchar(500) | varchar(500) | Não |
| **ATIVO** | Indica que o Tipo de Posse está ativo no sistema | char(3) | char(3) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas que dependem de TIPO_POSSE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM](dados_item) | \| **ITEM** \| **TIPO_POSSE** \| \|---\|---\| \| ID_TIPO_POSSE \| ID_TIPO_POSSE \| |
