# SV_CHANGE_ITEM

Caminho: Customização > Modelo de dados > Utilitários > SV_CHANGE_ITEM

Modificação de Propriedades

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CHANGE_LOG** | Identificador da Modificação | decimal(15,2) | number(15,2) | Não |
| **PROPERTY_NAME** | Nome da Propriedade modificada | varchar(500) | varchar(500) | Não |
| **OLD_VALUE** | Valor anterior da Propriedade | varchar(500) | varchar(500) | Sim |
| **NEW_VALUE** | Novo valor da Propriedade | varchar(500) | varchar(500) | Sim |
| **IS_CUSTOM** | Indica que corresponde a uma propriedade customizada pelo Usuário. | char(3) | char(3) | Não |
| **OLD_LARGE_TEXT** | Valor antigo em formato longo | text | clob | Sim |
| **NEW_LARGE_TEXT** | Novo valor em formato longo | text | clob | Sim |

Tabelas referenciadas por SV_CHANGE_ITEM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CHANGE_LOG](dados_sv_change_log) | \| **SV_CHANGE_LOG** \| **SV_CHANGE_ITEM** \| \|---\|---\| \| ID_CHANGE_LOG \| ID_CHANGE_LOG \| |

**Exemplo 1: join com a tabela SV_CHANGE_LOG**

```
select SV_CHANGE_ITEM.*
from SV_CHANGE_ITEM, SV_CHANGE_LOG
where SV_CHANGE_ITEM.ID_CHANGE_LOG = SV_CHANGE_LOG.ID_CHANGE_LOG
```
