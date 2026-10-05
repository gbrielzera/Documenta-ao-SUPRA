# SV_TRANSACTION

Caminho: Customização > Modelo de dados > Utilitários > SV_TRANSACTION

Uma Transação representa o ponto de entrada para uma funcionalidade do sistema (Tela de sistema, Web Services, etc). Para cada Transação é possível a configuração de autorização por Perfil de acesso.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_TRANSACTION** | Identificador da Transação | int | number(6,0) | Não |
| **ID_MODULE** | Identificador do Módulo associado | int | number(6,0) | Não |
| **SHORT_NAME** | Código da transação utilizado para acesso via barra de ferramentas. | varchar(50) | varchar(50) | Não |
| **ENABLED** | Indica que a Transação está ativa. Quando desativada a Transação não é mais visível para o usuário. | char(3) | char(3) | Não |
| **URL** | Caminho para objeto inicial da Transação | varchar(500) | varchar(500) | Não |
| **CAPABILITIES** | Funcionalidades disponibilizadas na Transação. Exemplos de funções disponíveis: AllowEdit, AllowRemove, AllowNew etc. | varchar(500) | varchar(500) | Sim |
| **TEXT** | Descrição resumida da Transação. | varchar(500) | varchar(500) | Não |
| **DESCRIPTION** | Descrição detalhada sobre a transação. | varchar(500) | varchar(500) | Não |
| **ORIGINAL_TEXT** | Descrição resumida original | varchar(500) | varchar(500) | Não |
| **ORIGINAL_DESCRIPTION** | Descrição detalhada original. | varchar(500) | varchar(500) | Não |
| **SOURCE** | Fonte do registro que pode ser Usuário ou Sistema | varchar(250) | varchar(250) | Não |
| **ICON_NAME** | Nome do ícone utilizado na Transação. Este nome corresponde ao objeto adicionado como recurso na aplicação cliente. | varchar(500) | varchar(500) | Sim |
| **ADAPTER_CRUD** | Classe que customiza o comportamento de telas CRUD | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por SV_TRANSACTION

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_MODULE](dados_sv_module) | \| **SV_MODULE** \| **SV_TRANSACTION** \| \|---\|---\| \| ID_MODULE \| ID_MODULE \| |

Tabelas que dependem de SV_TRANSACTION

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_COMMAND](dados_sv_command) | \| **SV_COMMAND** \| **SV_TRANSACTION** \| \|---\|---\| \| ID_TRANSACTION \| ID_TRANSACTION \| |
| [SV_AUTHORIZATION](dados_sv_authorization) | \| **SV_AUTHORIZATION** \| **SV_TRANSACTION** \| \|---\|---\| \| ID_TRANSACTION \| ID_TRANSACTION \| |
| [SV_TRANS_ACCESS](dados_sv_trans_access) | \| **SV_TRANS_ACCESS** \| **SV_TRANSACTION** \| \|---\|---\| \| ID_TRANSACTION \| ID_TRANSACTION \| |

**Exemplo 1: join com a tabela SV_MODULE**

```
select SV_TRANSACTION.*, SV_MODULE.NAME
from SV_TRANSACTION, SV_MODULE
where SV_TRANSACTION.ID_MODULE = SV_MODULE.ID_MODULE
```
