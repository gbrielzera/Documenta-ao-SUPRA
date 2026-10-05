# SV_REPORT_QUERY

Caminho: Customização > Modelo de dados > Utilitários > SV_REPORT_QUERY

Consulta criada pelo usuário para recuperação dos dados que serão apresentados pelo relatório. No caso de consultas do banco de dados do produto o usuário contará com o recurso Query Builder.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_REPORT** | Número sequencial gerado automaticamente pelo sistema para Identificar um Report | int | number(6,0) | Não |
| **NAME** | Corresponde ao nome da banda do relatório associada com a consulta. | varchar(500) | varchar(500) | Não |
| **SQL** | Comand SQL Select utilizado para recuperar os dados do relatório. | text | clob | Não |
| **ID_DB_CONNECTION** | Identificador da conexão de base de dados externa utilizada para executar o comando SQL Select. No caso de consultas no banco do produto este campo estará sempre nulo. | int | number(6,0) | Sim |

Tabelas referenciadas por SV_REPORT_QUERY

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_DB_CONNECTION](dados_sv_db_connection) | \| **SV_DB_CONNECTION** \| **SV_REPORT_QUERY** \| \|---\|---\| \| ID_DB_CONNECTION \| ID_DB_CONNECTION \| |
| [SV_REPORT](dados_sv_report) | \| **SV_REPORT** \| **SV_REPORT_QUERY** \| \|---\|---\| \| ID_REPORT \| ID_REPORT \| |

**Exemplo 1: join com a tabela SV_DB_CONNECTION**

```
select SV_REPORT_QUERY.*, SV_DB_CONNECTION.SHORT_NAME
from SV_REPORT_QUERY left outer join SV_DB_CONNECTION on SV_REPORT_QUERY.ID_DB_CONNECTION = SV_DB_CONNECTION.ID_DB_CONNECTION
```

**Exemplo 2: join com a tabela SV_REPORT**

```
select SV_REPORT_QUERY.*
from SV_REPORT_QUERY, SV_REPORT
where SV_REPORT_QUERY.ID_REPORT = SV_REPORT.ID_REPORT
```
