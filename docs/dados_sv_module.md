# SV_MODULE

Caminho: Customização > Modelo de dados > Utilitários > SV_MODULE

Um Módulo define um conjunto de funcionalidades pertencentes a uma aplicação. Para cada Módulo existe um item de menu raiz denominado 'Comando raiz' e a partir deste item são associados todos as opções de comandos do módulo.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_MODULE** | Identificador do Módulo | int | number(6,0) | Não |
| **ID_COMMAND_ROOT** | Identificador do item de menu denominado 'Comando raiz' | int | number(6,0) | Sim |
| **NAME** | Nome sucinto para o Módulo. | varchar(100) | varchar(100) | Não |
| **SHORT_NAME** | Nome resumido (código) que identifica um Módulo. | varchar(50) | varchar(50) | Não |
| **ENABLED** | Indica que o Módulo está ativo no sistema. Uma vez inativo o Módulo não pode ser acessado por Usuários. | char(3) | char(3) | Não |
| **TEXT** | Descrição resumida para utilização na interface com usuário. | varchar(500) | varchar(500) | Não |
| **DESCRIPTION** | Descrição detalhada do Módulo para documentação do Módulo. | varchar(500) | varchar(500) | Não |
| **ORIGINAL_TEXT** | Descrição resumida original | varchar(500) | varchar(500) | Não |
| **ORIGINAL_DESCRIPTION** | Descrição original do Módulo | varchar(500) | varchar(500) | Não |
| **PARAM_CLASS_NAME** | Nome da Classe responsável por manter os parâmetros do Módulo. | varchar(500) | varchar(500) | Não |

Tabelas referenciadas por SV_MODULE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_COMMAND](dados_sv_command) | \| **SV_COMMAND** \| **SV_MODULE** \| \|---\|---\| \| ID_COMMAND \| ID_COMMAND_ROOT \| |

Tabelas que dependem de SV_MODULE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_TRANSACTION](dados_sv_transaction) | \| **SV_TRANSACTION** \| **SV_MODULE** \| \|---\|---\| \| ID_MODULE \| ID_MODULE \| |
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_MODULE** \| \|---\|---\| \| ID_MODULE \| ID_MODULE \| |

**Exemplo 1: join com a tabela SV_COMMAND**

```
select SV_MODULE.*, SV_COMMAND.TEXT
from SV_MODULE left outer join SV_COMMAND on SV_MODULE.ID_COMMAND_ROOT = SV_COMMAND.ID_COMMAND
```
