# CATEGORIA_RISCO

Caminho: Customização > Modelo de dados > Processo > CATEGORIA_RISCO

Categoria de Riscos e Controles

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CATEGORIA_RISCO** | Número sequencial gerado automaticamente pelo sistema para Identificar um CategoriaRisco | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do CategoriaRisco | varchar(500) | varchar(500) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas que dependem de CATEGORIA_RISCO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [RISCO](dados_risco) | \| **RISCO** \| **CATEGORIA_RISCO** \| \|---\|---\| \| ID_CATEGORIA_RISCO \| ID_CATEGORIA_RISCO \| |
| [CLASSE_CONTROLE](dados_classe_controle) | \| **CLASSE_CONTROLE** \| **CATEGORIA_RISCO** \| \|---\|---\| \| ID_CATEGORIA_CONTROLE \| ID_CATEGORIA_RISCO \| |
