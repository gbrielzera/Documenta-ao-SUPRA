# SV_COMMAND

Caminho: Customização > Modelo de dados > Utilitários > SV_COMMAND

Um Comando pode ser um item de menu, botão ou qualquer outro recurso de interface para acesso a uma transação (janela windows, página Internet ou WebService).

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_COMMAND** | Identificador do Comando | int | number(6,0) | Não |
| **TEXT** | Texto exibido em itens de menu ou botões para seleção de comando pelo usuário. | varchar(500) | varchar(500) | Não |
| **ID_COMMAND_PARENT** | Identificador do Comando Pai | int | number(6,0) | Sim |
| **ID_TRANSACTION** | Identificador da Transação associada | int | number(6,0) | Sim |
| **TYPE** | Tipo de Comando: item menu, botão, etc | varchar(250) | varchar(250) | Não |
| **SEQUENCE** | Define a sequência de exibição de comandos em lista (menu por exemplo). | int | number(6,0) | Não |
| **ID_USER** | Identificador do Usuário proprietário do Comando | int | number(6,0) | Sim |

Tabelas referenciadas por SV_COMMAND

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_TRANSACTION](dados_sv_transaction) | \| **SV_TRANSACTION** \| **SV_COMMAND** \| \|---\|---\| \| ID_TRANSACTION \| ID_TRANSACTION \| |
| [SV_COMMAND](dados_sv_command) | \| **SV_COMMAND** \| **SV_COMMAND** \| \|---\|---\| \| ID_COMMAND \| ID_COMMAND_PARENT \| |
| [SV_USER](dados_sv_user) | \| **SV_USER** \| **SV_COMMAND** \| \|---\|---\| \| ID_USER \| ID_USER \| |

Tabelas que dependem de SV_COMMAND

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_MODULE](dados_sv_module) | \| **SV_MODULE** \| **SV_COMMAND** \| \|---\|---\| \| ID_COMMAND_ROOT \| ID_COMMAND \| |
| [SV_COMMAND](dados_sv_command) | \| **SV_COMMAND** \| **SV_COMMAND** \| \|---\|---\| \| ID_COMMAND_PARENT \| ID_COMMAND \| |

**Exemplo 1: join com a tabela SV_TRANSACTION**

```
select SV_COMMAND.*, SV_TRANSACTION.TEXT
from SV_COMMAND left outer join SV_TRANSACTION on SV_COMMAND.ID_TRANSACTION = SV_TRANSACTION.ID_TRANSACTION
```

**Exemplo 2: join com a tabela SV_COMMAND**

```
select SV_COMMAND.*, SV_COMMAND2.TEXT
from SV_COMMAND left outer join SV_COMMAND SV_COMMAND2 on SV_COMMAND.ID_COMMAND_PARENT = SV_COMMAND2.ID_COMMAND
```

**Exemplo 3: join com a tabela SV_USER**

```
select SV_COMMAND.*, SV_USER.USERNAME
from SV_COMMAND left outer join SV_USER on SV_COMMAND.ID_USER = SV_USER.ID_USER
```
