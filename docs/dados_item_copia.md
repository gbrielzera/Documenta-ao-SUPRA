# ITEM_COPIA

Caminho: Customização > Modelo de dados > Ativos > ITEM_COPIA

Itens que são cópias

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ITEM** | Número sequencial gerado automaticamente para Identificar um Item de Configuração | int | number(6,0) | Não |
| **ID_ITEM_COPIA** | Identificador do Item considerado Cópia | int | number(6,0) | Não |
| **COMENTARIO** | Comentário sobre a relação de Cópia. Para conhecimento do autor do Comentário utilize a ferramenta de Consulta de Trilha de Modificações do Item. | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por ITEM_COPIA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM](dados_item) | \| **ITEM** \| **ITEM_COPIA** \| \|---\|---\| \| ID_ITEM \| ID_ITEM_COPIA \| |
| [ITEM](dados_item) | \| **ITEM** \| **ITEM_COPIA** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |

**Exemplo 1: join com a tabela ITEM**

```
select ITEM_COPIA.*, ITEM.DESCRICAO
from ITEM_COPIA, ITEM
where ITEM_COPIA.ID_ITEM_COPIA = ITEM.ID_ITEM
```

**Exemplo 2: join com a tabela ITEM**

```
select ITEM_COPIA.*
from ITEM_COPIA, ITEM
where ITEM_COPIA.ID_ITEM = ITEM.ID_ITEM
```
