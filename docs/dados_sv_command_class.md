# SV_COMMAND_CLASS

Caminho: Customização > Modelo de dados > Utilitários > SV_COMMAND_CLASS

Classe de Comandos para customização do aplicativo

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_COMMAND_CLASS** | Identificador da Classe de Comando | int | number(6,0) | Não |
| **ID_CLASS** | Identificador da Classe associada | int | number(6,0) | Não |
| **NAME** | Nome da Classe incluindo namespace | varchar(100) | varchar(100) | Não |
| **DESCRIPTION** | Descrição completa da Classe de Comando | varchar(500) | varchar(500) | Não |
| **SOURCE** | Código fonte da Classe | varchar(500) | varchar(500) | Não |
| **BINARY** | Código binário | varchar(500) | varchar(500) | Não |

Tabelas referenciadas por SV_COMMAND_CLASS

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_COMMAND_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |

**Exemplo 1: join com a tabela SV_CLASS**

```
select SV_COMMAND_CLASS.*, SV_CLASS.NAME
from SV_COMMAND_CLASS, SV_CLASS
where SV_COMMAND_CLASS.ID_CLASS = SV_CLASS.ID_CLASS
```
