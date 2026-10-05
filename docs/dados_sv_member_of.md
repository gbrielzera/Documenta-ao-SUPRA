# SV_MEMBER_OF

Caminho: Customização > Modelo de dados > Utilitários > SV_MEMBER_OF

Define a associação entre um Usuário e Perfis de Acesso

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_USER** | Identificador do Usuário associado | int | number(6,0) | Não |
| **ID_ROLE** | Identificador do Perfil de acesso associado | int | number(6,0) | Não |

Tabelas referenciadas por SV_MEMBER_OF

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_ROLE](dados_sv_role) | \| **SV_ROLE** \| **SV_MEMBER_OF** \| \|---\|---\| \| ID_ROLE \| ID_ROLE \| |
| [SV_USER](dados_sv_user) | \| **SV_USER** \| **SV_MEMBER_OF** \| \|---\|---\| \| ID_USER \| ID_USER \| |

**Exemplo 1: join com a tabela SV_ROLE**

```
select SV_MEMBER_OF.*, SV_ROLE.NAME
from SV_MEMBER_OF, SV_ROLE
where SV_MEMBER_OF.ID_ROLE = SV_ROLE.ID_ROLE
```

**Exemplo 2: join com a tabela SV_USER**

```
select SV_MEMBER_OF.*
from SV_MEMBER_OF, SV_USER
where SV_MEMBER_OF.ID_USER = SV_USER.ID_USER
```
