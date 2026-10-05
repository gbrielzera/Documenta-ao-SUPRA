# SV_QUERY

Caminho: Customização > Modelo de dados > Utilitários > SV_QUERY

Consultas SQL elaboradas pelo usuário do sistema.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_QUERY** | Número sequencial gerado automaticamente pelo sistema para Identificar um Query | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do Query | varchar(500) | varchar(500) | Não |
| **ID_USER** | Identificador do usuário criador da consulta | int | number(6,0) | Não |
| **SQL** | Texto da consulta SQL editada pelo usuário | text | clob | Sim |
| **ID_DB_CONNECTION** | Identificador da conexão de banco de dados externo | int | number(6,0) | Sim |

Tabelas referenciadas por SV_QUERY

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_USER](dados_sv_user) | \| **SV_USER** \| **SV_QUERY** \| \|---\|---\| \| ID_USER \| ID_USER \| |
| [SV_DB_CONNECTION](dados_sv_db_connection) | \| **SV_DB_CONNECTION** \| **SV_QUERY** \| \|---\|---\| \| ID_DB_CONNECTION \| ID_DB_CONNECTION \| |

**Exemplo 1: join com a tabela SV_USER**

```
select SV_QUERY.*, SV_USER.USERNAME
from SV_QUERY, SV_USER
where SV_QUERY.ID_USER = SV_USER.ID_USER
```

**Exemplo 2: join com a tabela SV_DB_CONNECTION**

```
select SV_QUERY.*, SV_DB_CONNECTION.SHORT_NAME
from SV_QUERY left outer join SV_DB_CONNECTION on SV_QUERY.ID_DB_CONNECTION = SV_DB_CONNECTION.ID_DB_CONNECTION
```
