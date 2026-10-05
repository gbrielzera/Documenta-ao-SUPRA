# SV_USER

Caminho: Customização > Modelo de dados > Utilitários > SV_USER

Usuário autorizado a acessar o sistema.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_USER** | Identificador do Usuário gerado automaticamente. | int | number(6,0) | Não |
| **USERNAME** | Nome de identificação do Usuário utilizado na tela de logon ou em chamadas webservices. Para autenticação via serviço de diretório este username deve corresponder exatamente ao nome de usuário no serviço de diretório. | varchar(100) | varchar(100) | Não |
| **CREATED_DATE** | Data de criação do Usuário. | datetime | date | Não |
| **ID_USER_CREATED** | Usuário administrador de segurança responsável pela criação do Usuário | int | number(6,0) | Não |
| **SOURCE** | Fonte do dado que pode ser Usuário ou Sistema | varchar(250) | varchar(250) | Não |
| **PASSWORD** | Senha de acesso do Usuário. Se for configurada uma URL do domínio na tela de configurações então a validação do usuário é feita no Serviço de Diretório e o conteúdo deste campo passa a ser ignorado. | varchar(50) | varchar(50) | Sim |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas referenciadas por SV_USER

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_DOMAIN](dados_sv_domain) | \| **SV_DOMAIN** \| **SV_USER** \| \|---\|---\| \| ID_DOMAIN \| ID_DOMAIN \| |

Tabelas que dependem de SV_USER

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_PROFILE_ITEM](dados_sv_profile_item) | \| **SV_PROFILE_ITEM** \| **SV_USER** \| \|---\|---\| \| ID_USER \| ID_USER \| |
| [SV_COMMAND](dados_sv_command) | \| **SV_COMMAND** \| **SV_USER** \| \|---\|---\| \| ID_USER \| ID_USER \| |
| [SV_JOB](dados_sv_job) | \| **SV_JOB** \| **SV_USER** \| \|---\|---\| \| ID_USER_CREATOR \| ID_USER \| |
| [SV_USER_SESSION](dados_sv_user_session) | \| **SV_USER_SESSION** \| **SV_USER** \| \|---\|---\| \| ID_USER \| ID_USER \| |
| [SV_ATTACHMENT_FILE](dados_sv_attachment_file) | \| **SV_ATTACHMENT_FILE** \| **SV_USER** \| \|---\|---\| \| ID_USER \| ID_USER \| |
| [SV_REPORT](dados_sv_report) | \| **SV_REPORT** \| **SV_USER** \| \|---\|---\| \| ID_USER \| ID_USER \| |
| [SV_REPORT](dados_sv_report) | \| **SV_REPORT** \| **SV_USER** \| \|---\|---\| \| LOCKED_BY_ID \| ID_USER \| |
| [SV_REPORT](dados_sv_report) | \| **SV_REPORT** \| **SV_USER** \| \|---\|---\| \| ID_USER_UNLOCKER \| ID_USER \| |
| [SV_QUERY](dados_sv_query) | \| **SV_QUERY** \| **SV_USER** \| \|---\|---\| \| ID_USER \| ID_USER \| |
| [SV_LOG_EXEC_SQL](dados_sv_log_exec_sql) | \| **SV_LOG_EXEC_SQL** \| **SV_USER** \| \|---\|---\| \| ID_USER \| ID_USER \| |
| [SV_MEMBER_OF](dados_sv_member_of) | \| **SV_MEMBER_OF** \| **SV_USER** \| \|---\|---\| \| ID_USER \| ID_USER \| |

**Exemplo 1: join com a tabela SV_DOMAIN**

```
select SV_USER.*, SV_DOMAIN.NAME
from SV_USER, SV_DOMAIN
where SV_USER.ID_DOMAIN = SV_DOMAIN.ID_DOMAIN
```
