# SV_DB_CONNECTION

Caminho: Customização > Modelo de dados > Utilitários > SV_DB_CONNECTION

Conexão de banco de dados externo

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_DB_CONNECTION** | Número sequencial gerado automaticamente pelo sistema para Identificar um DatabaseConnection | int | number(6,0) | Não |
| **ENABLED** | Indica que o DatabaseConnection está ativo no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. | char(3) | char(3) | Não |
| **SHORT_NAME** | Nome resumido do DatabaseConnection | varchar(500) | varchar(500) | Não |
| **CONNECTION_STRING** | String de conexão do banco de dados | varchar(500) | varchar(500) | Sim |
| **TYPE** | Tipo de conexão para o banco externo. | varchar(250) | varchar(250) | Não |

Tabelas que dependem de SV_DB_CONNECTION

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_QUERY](dados_sv_query) | \| **SV_QUERY** \| **SV_DB_CONNECTION** \| \|---\|---\| \| ID_DB_CONNECTION \| ID_DB_CONNECTION \| |
| [SV_REPORT_QUERY](dados_sv_report_query) | \| **SV_REPORT_QUERY** \| **SV_DB_CONNECTION** \| \|---\|---\| \| ID_DB_CONNECTION \| ID_DB_CONNECTION \| |
| [SV_REPORT_PARAM](dados_sv_report_param) | \| **SV_REPORT_PARAM** \| **SV_DB_CONNECTION** \| \|---\|---\| \| ID_DB_CONNECTION \| ID_DB_CONNECTION \| |
