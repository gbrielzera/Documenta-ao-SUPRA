# ITEM_DEPENDENCIA

Caminho: Customização > Modelo de dados > Ativos > ITEM_DEPENDENCIA

Itens de Configuração que possuem relação de Dependência.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ITEM** | Número sequencial gerado automaticamente para Identificar um Item de Configuração | int | number(6,0) | Não |
| **ID_DEPENDENCIA** | Identificador do Item de Configuração que do qual é dependente | int | number(6,0) | Não |
| **COMENTARIO** | Comentário sobre a relação de Dependência. Para conhecimento do autor do Comentário utilize a ferramenta de Consulta de Trilha de Modificações do Item. | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por ITEM_DEPENDENCIA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM](dados_item) | \| **ITEM** \| **ITEM_DEPENDENCIA** \| \|---\|---\| \| ID_ITEM \| ID_DEPENDENCIA \| |
| [ITEM](dados_item) | \| **ITEM** \| **ITEM_DEPENDENCIA** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |

**Exemplo 1: join com a tabela ITEM**

```
select ITEM_DEPENDENCIA.*, ITEM.DESCRICAO
from ITEM_DEPENDENCIA, ITEM
where ITEM_DEPENDENCIA.ID_DEPENDENCIA = ITEM.ID_ITEM
```

**Exemplo 2: join com a tabela ITEM**

```
select ITEM_DEPENDENCIA.*
from ITEM_DEPENDENCIA, ITEM
where ITEM_DEPENDENCIA.ID_ITEM = ITEM.ID_ITEM
```
