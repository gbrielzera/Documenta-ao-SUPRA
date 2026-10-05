# AREA_RISCO

Caminho: Customização > Modelo de dados > Processo > AREA_RISCO

Área de negócio atingida pelo Risco

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_AREA_RISCO** | Número sequencial gerado automaticamente pelo sistema para Identificar um AreaRisco | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do AreaRisco | varchar(500) | varchar(500) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas que dependem de AREA_RISCO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [RISCO](dados_risco) | \| **RISCO** \| **AREA_RISCO** \| \|---\|---\| \| ID_AREA_RISCO \| ID_AREA_RISCO \| |
| [CLASSE_CONTROLE](dados_classe_controle) | \| **CLASSE_CONTROLE** \| **AREA_RISCO** \| \|---\|---\| \| ID_AREA \| ID_AREA_RISCO \| |
