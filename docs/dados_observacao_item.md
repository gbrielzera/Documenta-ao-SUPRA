# OBSERVACAO_ITEM

Caminho: Customização > Modelo de dados > Ativos > OBSERVACAO_ITEM

Observações a respeito do Item de Configuração

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ITEM** | Número sequencial gerado automaticamente para Identificar um Item de Configuração | int | number(6,0) | Não |
| **DATA_HORA_COMENTARIO** | Data/hora comentário | datetime | date | Não |
| **COMENTARIO** | Comentário fornecido por Solucionador ou Gestor | varchar(500) | varchar(500) | Não |
| **ID_PESSOA** | Identificador do Solucionador autor do comentário. | int | number(6,0) | Não |

Tabelas referenciadas por OBSERVACAO_ITEM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **OBSERVACAO_ITEM** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |
| [ITEM](dados_item) | \| **ITEM** \| **OBSERVACAO_ITEM** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |

**Exemplo 1: join com a tabela ITEM**

```
select OBSERVACAO_ITEM.*
from OBSERVACAO_ITEM, ITEM
where OBSERVACAO_ITEM.ID_ITEM = ITEM.ID_ITEM
```
