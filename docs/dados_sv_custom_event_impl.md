# SV_CUSTOM_EVENT_IMPL

Caminho: Customização > Modelo de dados > Utilitários > SV_CUSTOM_EVENT_IMPL

Implementação de Eventos

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CUSTOM_EVENT** | Identificador do Evento | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do(a) Domain associado(a) | int | number(6,0) | Não |
| **SOURCE** | Código fonte do script Python. Neste código é possível acessar propriedades da Classe de Negócio customizada. Também é possível interromper modificações utilizando o comando raise (este comando emite uma Exception). | text | clob | Não |

Tabelas referenciadas por SV_CUSTOM_EVENT_IMPL

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_DOMAIN](dados_sv_domain) | \| **SV_DOMAIN** \| **SV_CUSTOM_EVENT_IMPL** \| \|---\|---\| \| ID_DOMAIN \| ID_DOMAIN \| |
| [SV_CUSTOM_EVENT](dados_sv_custom_event) | \| **SV_CUSTOM_EVENT** \| **SV_CUSTOM_EVENT_IMPL** \| \|---\|---\| \| ID_CUSTOM_EVENT \| ID_CUSTOM_EVENT \| |

**Exemplo 1: join com a tabela SV_DOMAIN**

```
select SV_CUSTOM_EVENT_IMPL.*, SV_DOMAIN.NAME
from SV_CUSTOM_EVENT_IMPL, SV_DOMAIN
where SV_CUSTOM_EVENT_IMPL.ID_DOMAIN = SV_DOMAIN.ID_DOMAIN
```

**Exemplo 2: join com a tabela SV_CUSTOM_EVENT**

```
select SV_CUSTOM_EVENT_IMPL.*
from SV_CUSTOM_EVENT_IMPL, SV_CUSTOM_EVENT
where SV_CUSTOM_EVENT_IMPL.ID_CUSTOM_EVENT = SV_CUSTOM_EVENT.ID_CUSTOM_EVENT
```
