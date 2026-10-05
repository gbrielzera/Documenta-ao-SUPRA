# SV_PROFILE_ITEM

Caminho: Customização > Modelo de dados > Utilitários > SV_PROFILE_ITEM

Profile de Usuário

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ITEM_NAME** | Nome de identificação para o item de Profile | varchar(500) | varchar(500) | Não |
| **ID_USER** | Identificador do Usuário | int | number(6,0) | Não |
| **DATA** | Dados do Profile | varbinary(4000) | blob | Não |
| **LAST_MODIFIED_DATE** | Data de última modificação | datetime | date | Não |

Tabelas referenciadas por SV_PROFILE_ITEM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_USER](dados_sv_user) | \| **SV_USER** \| **SV_PROFILE_ITEM** \| \|---\|---\| \| ID_USER \| ID_USER \| |

**Exemplo 1: join com a tabela SV_USER**

```
select SV_PROFILE_ITEM.*, SV_USER.USERNAME
from SV_PROFILE_ITEM, SV_USER
where SV_PROFILE_ITEM.ID_USER = SV_USER.ID_USER
```
