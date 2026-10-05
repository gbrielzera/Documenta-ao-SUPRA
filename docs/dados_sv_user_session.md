# SV_USER_SESSION

Caminho: Customização > Modelo de dados > Utilitários > SV_USER_SESSION

Mantém informações da sessão de conexão de usuário.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **SESSION_ID** | Identificador gerado automaticamente pelo sistema para Identificação da Sessão. | varchar(100) | varchar(100) | Não |
| **ID_USER** | Identificador do(a) User associado(a) | int | number(6,0) | Não |
| **LOGON** | Data/hora do início de conexão. | datetime | date | Não |
| **LOGOUT** | Data/hora do fim de conexão. | datetime | date | Sim |
| **APP_ID** | Nome da aplicação onde foi realizado o Logon | varchar(500) | varchar(500) | Não |
| **LOGON_TYPE** | Tipo de Logon que gerou a sessão de usuário | varchar(250) | varchar(250) | Não |
| **CONNECT_USERS** | Registro da quantidade de usuários conectados no instante do Logon. São desconsideradas sessões iniciadas por rotinas de manutenção de dados e processamento de Jobs (Logon de sistema). | int | number(6,0) | Não |
| **LOGOUT_REASON** | Motivo do logout do usuário | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por SV_USER_SESSION

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_USER](dados_sv_user) | \| **SV_USER** \| **SV_USER_SESSION** \| \|---\|---\| \| ID_USER \| ID_USER \| |

Tabelas que dependem de SV_USER_SESSION

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_TRANS_ACCESS](dados_sv_trans_access) | \| **SV_TRANS_ACCESS** \| **SV_USER_SESSION** \| \|---\|---\| \| SESSION_ID \| SESSION_ID \| |

**Exemplo 1: join com a tabela SV_USER**

```
select SV_USER_SESSION.*, SV_USER.USERNAME
from SV_USER_SESSION, SV_USER
where SV_USER_SESSION.ID_USER = SV_USER.ID_USER
```
