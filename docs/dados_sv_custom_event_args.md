# SV_CUSTOM_EVENT_ARGS

Caminho: Customização > Modelo de dados > Utilitários > SV_CUSTOM_EVENT_ARGS

Argumentos disponibilizados pelo mecanismo invocador de Eventos Customizados. Estes argumentos, somente leitura, podem ser utilizados na implementação de regras de negócio contida no evento.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CUSTOM_EVENT** | Identificador do Evento proprietário do argumento. | int | number(6,0) | Não |
| **NAME** | Na implementação do script este argumento pode ser acessado por uma variável declarada com este Nome. | varchar(100) | varchar(100) | Não |
| **DESCRIPTION** | Descrição detalhada sobre o conteúdo e utilização do argumento. | varchar(500) | varchar(500) | Não |
| **TYPE** | Tipo de dados do argumento. No caso de classes de negócio o tipo se refere aquele disponível para o mecanismo de customização (proxies de customização). | varchar(500) | varchar(500) | Não |

Tabelas referenciadas por SV_CUSTOM_EVENT_ARGS

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CUSTOM_EVENT](dados_sv_custom_event) | \| **SV_CUSTOM_EVENT** \| **SV_CUSTOM_EVENT_ARGS** \| \|---\|---\| \| ID_CUSTOM_EVENT \| ID_CUSTOM_EVENT \| |

**Exemplo 1: join com a tabela SV_CUSTOM_EVENT**

```
select SV_CUSTOM_EVENT_ARGS.*
from SV_CUSTOM_EVENT_ARGS, SV_CUSTOM_EVENT
where SV_CUSTOM_EVENT_ARGS.ID_CUSTOM_EVENT = SV_CUSTOM_EVENT.ID_CUSTOM_EVENT
```
