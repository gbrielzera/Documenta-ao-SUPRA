# SV_DOMAIN

Caminho: Customização > Modelo de dados > Utilitários > SV_DOMAIN

Um Domínio define um namespace de banco de dados. Quando um Usuário realiza uma conexão ele seleciona o Domínio no qual deseja acessar e a partir deste momento os dados apresentados são automaticamente filtrados para o "mundo" definido pelo Domínio. Também dentro de um Domínio é possível a existência de customizações (campos e regras em eventos) próprias

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_DOMAIN** | Identificador do Domínio | int | number(6,0) | Não |
| **NAME** | Nome do Domínio | varchar(100) | varchar(100) | Não |
| **SHORT_NAME** | Nome abreviado (código) que identifica um Domínio. | varchar(50) | varchar(50) | Não |
| **ENABLED** | Indica que o Domínio está ativo. Quando desabilitado não é possível ao usuário a operação de Login. | char(3) | char(3) | Não |
| **LOGO** | Logomarca associado ao Domínio | varbinary(4000) | blob | Sim |

Tabelas que dependem de SV_DOMAIN

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CUSTOM_PROPERTY](dados_sv_custom_property) | \| **SV_CUSTOM_PROPERTY** \| **SV_DOMAIN** \| \|---\|---\| \| ID_DOMAIN \| ID_DOMAIN \| |
| [SV_CUSTOM_CLASS](dados_sv_custom_class) | \| **SV_CUSTOM_CLASS** \| **SV_DOMAIN** \| \|---\|---\| \| ID_DOMAIN \| ID_DOMAIN \| |
| [SV_USER](dados_sv_user) | \| **SV_USER** \| **SV_DOMAIN** \| \|---\|---\| \| ID_DOMAIN \| ID_DOMAIN \| |
| [SV_ROLE](dados_sv_role) | \| **SV_ROLE** \| **SV_DOMAIN** \| \|---\|---\| \| ID_DOMAIN \| ID_DOMAIN \| |
| [SV_CUSTOM_EVENT_IMPL](dados_sv_custom_event_impl) | \| **SV_CUSTOM_EVENT_IMPL** \| **SV_DOMAIN** \| \|---\|---\| \| ID_DOMAIN \| ID_DOMAIN \| |
