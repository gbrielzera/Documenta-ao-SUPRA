# SV_CUSTOM_EVENT

Caminho: Customização > Modelo de dados > Utilitários > SV_CUSTOM_EVENT

Evento para disponível para Customização em uma determinada Classe de Negócio. Todos os eventos são implementados pela linguagem de scripts Python e podem acessar propriedades da Classe de Negócio customizada.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CUSTOM_EVENT** | Identificador do Evento | int | number(6,0) | Não |
| **ID_CLASS** | Idenficador da Classe | int | number(6,0) | Não |
| **NAME** | Nome do Evento | varchar(100) | varchar(100) | Não |
| **DESCRIPTION** | Descrição detalhada sobre quando o Evento é disparado pelo sistema. | varchar(500) | varchar(500) | Não |

Tabelas referenciadas por SV_CUSTOM_EVENT

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_CUSTOM_EVENT** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |

Tabelas que dependem de SV_CUSTOM_EVENT

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CUSTOM_EVENT_IMPL](dados_sv_custom_event_impl) | \| **SV_CUSTOM_EVENT_IMPL** \| **SV_CUSTOM_EVENT** \| \|---\|---\| \| ID_CUSTOM_EVENT \| ID_CUSTOM_EVENT \| |
| [SV_CUSTOM_EVENT_ARGS](dados_sv_custom_event_args) | \| **SV_CUSTOM_EVENT_ARGS** \| **SV_CUSTOM_EVENT** \| \|---\|---\| \| ID_CUSTOM_EVENT \| ID_CUSTOM_EVENT \| |

**Exemplo 1: join com a tabela SV_CLASS**

```
select SV_CUSTOM_EVENT.*
from SV_CUSTOM_EVENT, SV_CLASS
where SV_CUSTOM_EVENT.ID_CLASS = SV_CLASS.ID_CLASS
```
