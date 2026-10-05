# SV_LOG_EXEC_SQL

Caminho: Customização > Modelo de dados > Utilitários > SV_LOG_EXEC_SQL

Log de execução de comandos SQL

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **EXEC_DATE_TIME** | Data e hora em que o comando SQL foi executado | datetime | date | Não |
| **ID_USER** | Identificador do usuário que executou o comando SQL. | int | number(6,0) | Não |
| **SQL** | Comando SQL executado pelo usuário | text | clob | Não |
| **ENVIROMENT** | Ambiente configurado no sistema no instante em que o comando SQL foi executado. Para ambiente de produção não é possível executar comando SQL de modificação ou comandos que contenham a palavra 'commit' | varchar(100) | varchar(100) | Não |
| **EXEC_ROLLBACK** | Indica que foi necessário executar a rotina de rollback | char(3) | char(3) | Não |
| **ERROR_MESSAGE** | Mensagem de erro gerada pela execução do comando SQL. Se o comando for executado com sucesso então este campo será nulo. | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por SV_LOG_EXEC_SQL

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_USER](dados_sv_user) | \| **SV_USER** \| **SV_LOG_EXEC_SQL** \| \|---\|---\| \| ID_USER \| ID_USER \| |

**Exemplo 1: join com a tabela SV_USER**

```
select SV_LOG_EXEC_SQL.*, SV_USER.USERNAME
from SV_LOG_EXEC_SQL, SV_USER
where SV_LOG_EXEC_SQL.ID_USER = SV_USER.ID_USER
```
