# SV_TRANS_ACCESS

Caminho: Customização > Modelo de dados > Utilitários > SV_TRANS_ACCESS

Acesso a Transação realizado por um Usuário do sistema.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **SESSION_ID** | Identificador do(a) UserSession associado(a) | varchar(100) | varchar(100) | Não |
| **ID_TRANSACTION** | Identificador do(a) Transaction associado(a) | int | number(6,0) | Não |
| **ACCESS_DATE_TIME** | Data/hora de acesso da transação pelo Usuário. | datetime | date | Não |

Tabelas referenciadas por SV_TRANS_ACCESS

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_USER_SESSION](dados_sv_user_session) | \| **SV_USER_SESSION** \| **SV_TRANS_ACCESS** \| \|---\|---\| \| SESSION_ID \| SESSION_ID \| |
| [SV_TRANSACTION](dados_sv_transaction) | \| **SV_TRANSACTION** \| **SV_TRANS_ACCESS** \| \|---\|---\| \| ID_TRANSACTION \| ID_TRANSACTION \| |

**Exemplo 1: join com a tabela SV_TRANSACTION**

```
select SV_TRANS_ACCESS.*, SV_TRANSACTION.TEXT
from SV_TRANS_ACCESS, SV_TRANSACTION
where SV_TRANS_ACCESS.ID_TRANSACTION = SV_TRANSACTION.ID_TRANSACTION
```
