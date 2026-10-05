# SV_AUTHORIZATION

Caminho: Customização > Modelo de dados > Utilitários > SV_AUTHORIZATION

Autorização para um Perfil de acesso

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ROLE** | Identificador do Perfil de acesso associado | int | number(6,0) | Não |
| **ID_TRANSACTION** | Identificador da Transação associada | int | number(6,0) | Não |
| **TYPE** | Tipo de autorização que pode ser uma Permissão (Permit) ou Restrição (Deny) | varchar(250) | varchar(250) | Não |

Tabelas referenciadas por SV_AUTHORIZATION

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_TRANSACTION](dados_sv_transaction) | \| **SV_TRANSACTION** \| **SV_AUTHORIZATION** \| \|---\|---\| \| ID_TRANSACTION \| ID_TRANSACTION \| |
| [SV_ROLE](dados_sv_role) | \| **SV_ROLE** \| **SV_AUTHORIZATION** \| \|---\|---\| \| ID_ROLE \| ID_ROLE \| |

Tabelas que dependem de SV_AUTHORIZATION

| **Tabela** | **Colunas de ligação** |
|---|---|
| [DATA_REST](dados_data_rest) | \| **DATA_REST** \| **SV_AUTHORIZATION** \| \|---\|---\| \| ID_ROLE \| ID_ROLE \| \| ID_TRANSACTION \| ID_TRANSACTION \| |
| [FIELD_REST](dados_field_rest) | \| **FIELD_REST** \| **SV_AUTHORIZATION** \| \|---\|---\| \| ID_ROLE \| ID_ROLE \| \| ID_TRANSACTION \| ID_TRANSACTION \| |

**Exemplo 1: join com a tabela SV_TRANSACTION**

```
select SV_AUTHORIZATION.*, SV_TRANSACTION.TEXT
from SV_AUTHORIZATION, SV_TRANSACTION
where SV_AUTHORIZATION.ID_TRANSACTION = SV_TRANSACTION.ID_TRANSACTION
```

**Exemplo 2: join com a tabela SV_ROLE**

```
select SV_AUTHORIZATION.*
from SV_AUTHORIZATION, SV_ROLE
where SV_AUTHORIZATION.ID_ROLE = SV_ROLE.ID_ROLE
```
