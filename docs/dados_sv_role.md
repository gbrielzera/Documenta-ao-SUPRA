# SV_ROLE

Caminho: Customização > Modelo de dados > Utilitários > SV_ROLE

Conjunto de telas autorizadas para um determinado usuário. Importante: um usuário pode acumular diversos perfis e o menu final é formado pela soma de todos os acessos.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ROLE** | Identificador do Perfil de acesso | int | number(6,0) | Não |
| **NAME** | Nome do Perfil de acesso | varchar(100) | varchar(100) | Não |
| **REFERENCE** | Texto explicativo para utilização do Perfil de acesso. Pode ser utilizado para esclarecer sobre funções ou transações que podem ser acessadas pelo usuário que detém o perfil. | text | clob | Não |
| **SOURCE** | Fonte do registro que pode ser Usuário ou Sistema | varchar(250) | varchar(250) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas referenciadas por SV_ROLE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_DOMAIN](dados_sv_domain) | \| **SV_DOMAIN** \| **SV_ROLE** \| \|---\|---\| \| ID_DOMAIN \| ID_DOMAIN \| |

Tabelas que dependem de SV_ROLE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_MEMBER_OF](dados_sv_member_of) | \| **SV_MEMBER_OF** \| **SV_ROLE** \| \|---\|---\| \| ID_ROLE \| ID_ROLE \| |
| [SV_AUTHORIZATION](dados_sv_authorization) | \| **SV_AUTHORIZATION** \| **SV_ROLE** \| \|---\|---\| \| ID_ROLE \| ID_ROLE \| |

**Exemplo 1: join com a tabela SV_DOMAIN**

```
select SV_ROLE.*, SV_DOMAIN.NAME
from SV_ROLE, SV_DOMAIN
where SV_ROLE.ID_DOMAIN = SV_DOMAIN.ID_DOMAIN
```
