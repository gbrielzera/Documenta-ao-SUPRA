# SV_CLASS

Caminho: Customização > Modelo de dados > Utilitários > SV_CLASS

Implementa um cadastro de todas as Classes de Negócio existentes no sistema. Este cadastro torna possível a customização do software permitindo: alteração de documentação, definição de novos campos e regras de negócio.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASS** | Idenficador da Classe | int | number(6,0) | Não |
| **ID_MODULE** | Identificador do Módulo Associado | int | number(6,0) | Não |
| **NAME** | Nome da Classe incluindo namespace | varchar(500) | varchar(500) | Não |
| **CHANGE_LOG_ENABLED** | Indica que o Log de modificações está ativado. Quando ativado o sistema gera registro (log) de todas as modificações em objetos deste tipo. | char(3) | char(3) | Não |
| **ORIGINAL_TEXT** | Descrição resumida originalmente definida pelo fabricante do software. Este valor pode ser utilizado para reverter modificações realizadas pelo usuário. | varchar(500) | varchar(500) | Não |
| **DESCRIPTION** | Documentação sobre a Classe de Negócio utilizada como ajuda para usuário em telas de cadastro e outras funções do sistema. | text | clob | Não |
| **LOCALIZATION_ENABLED** | Indica que a Classe possui o recurso de localização de objetos ativado. Quando ativado é possível a tradução de propriedades do tipo texto para diversas culturas. | char(3) | char(3) | Não |
| **TEXT** | Descrição resumida da Classe. Este texto é muito usado para identificar objetos deste tipo. | varchar(500) | varchar(500) | Não |
| **ORIGINAL_DESCRIPTION** | Descrição completa definida originalmente pelo fabricante do software. Este valor pode ser utilizado para reverter modificações realizadas pelo usuário. | text | clob | Não |
| **CHANGE_LOG_MODE** | Configuração gerada durante fase de projeto para configuração da propriedade LogChangeEnabled | varchar(250) | varchar(250) | Não |
| **LOCALIZATION_MODE** | Configuração gerada durante fase de projeto para configuração da propriedade LocalizeEnabled | varchar(250) | varchar(250) | Não |
| **ID_PARENT_CLASS** | Identificador da Classe Pai | int | number(6,0) | Sim |
| **ORIG_LOCAL_ENABLED** | Opção de ativação do recurso de Localização definido pelo fabricante do software. Este valor pode ser utilizado para reverter modificações realizadas pelo usuário. | char(3) | char(3) | Não |
| **ORIG_CHNG_LOG_ENABLED** | Opção de ativação do log de modificações definida pelo fabricante do software. Este valor pode ser utilizado para reverter modificações realizadas pelo usuário. | char(3) | char(3) | Não |
| **TABLE_NAME** | Nome da tabela que mantém objetos da Classe. Válido apenas para Classes de Entidades. | varchar(100) | varchar(100) | Sim |

Tabelas referenciadas por SV_CLASS

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_MODULE](dados_sv_module) | \| **SV_MODULE** \| **SV_CLASS** \| \|---\|---\| \| ID_MODULE \| ID_MODULE \| |
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_PARENT_CLASS \| |

Tabelas que dependem de SV_CLASS

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_COMMAND_CLASS](dados_sv_command_class) | \| **SV_COMMAND_CLASS** \| **SV_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |
| [SV_EXCEPTION_CLASS](dados_sv_exception_class) | \| **SV_EXCEPTION_CLASS** \| **SV_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |
| [SV_CUSTOM_CLASS](dados_sv_custom_class) | \| **SV_CUSTOM_CLASS** \| **SV_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |
| [SV_CHANGE_LOG](dados_sv_change_log) | \| **SV_CHANGE_LOG** \| **SV_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |
| [SV_JOB](dados_sv_job) | \| **SV_JOB** \| **SV_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_CLASS** \| \|---\|---\| \| ID_PARENT_CLASS \| ID_CLASS \| |
| [SV_CUSTOM_PROPERTY](dados_sv_custom_property) | \| **SV_CUSTOM_PROPERTY** \| **SV_CLASS** \| \|---\|---\| \| ID_CLASS_REF \| ID_CLASS \| |
| [SV_LOCALIZATION](dados_sv_localization) | \| **SV_LOCALIZATION** \| **SV_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |
| [SV_MESSAGE](dados_sv_message) | \| **SV_MESSAGE** \| **SV_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |
| [SV_MESSAGE](dados_sv_message) | \| **SV_MESSAGE** \| **SV_CLASS** \| \|---\|---\| \| ID_TEMPORALITY_CLASS \| ID_CLASS \| |
| [SV_ATTACHMENT_FILE](dados_sv_attachment_file) | \| **SV_ATTACHMENT_FILE** \| **SV_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |
| [SV_PICTURE](dados_sv_picture) | \| **SV_PICTURE** \| **SV_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |
| [SV_PROPERTY](dados_sv_property) | \| **SV_PROPERTY** \| **SV_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |
| [SV_CUSTOM_PROPERTY](dados_sv_custom_property) | \| **SV_CUSTOM_PROPERTY** \| **SV_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |
| [SV_CUSTOM_EVENT](dados_sv_custom_event) | \| **SV_CUSTOM_EVENT** \| **SV_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |

**Exemplo 1: join com a tabela SV_MODULE**

```
select SV_CLASS.*, SV_MODULE.NAME
from SV_CLASS, SV_MODULE
where SV_CLASS.ID_MODULE = SV_MODULE.ID_MODULE
```

**Exemplo 2: join com a tabela SV_CLASS**

```
select SV_CLASS.*, SV_CLASS2.NAME
from SV_CLASS left outer join SV_CLASS SV_CLASS2 on SV_CLASS.ID_PARENT_CLASS = SV_CLASS2.ID_CLASS
```
