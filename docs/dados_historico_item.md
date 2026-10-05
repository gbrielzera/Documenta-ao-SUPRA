# HISTORICO_ITEM

Caminho: Customização > Modelo de dados > Ativos > HISTORICO_ITEM

Histórico de alterações no arquivo anexo

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_HISTORICO_ITEM** | Número sequencial gerado automaticamente para Identificar um Item de Configuração | int | number(6,0) | Não |
| **COMENTARIO** | Comentário feito pelo usuário responsável pela alteração | varchar(500) | varchar(500) | Sim |
| **DATA_ALTERACAO** | Data e hora de atualização do arquivo | datetime | date | Não |
| **ID_PESSOA** | Identificador do autor da mudança no documento | int | number(6,0) | Não |
| **ID_ITEM** | Número sequencial gerado automaticamente para Identificar um Item de Configuração | int | number(6,0) | Não |

Tabelas referenciadas por HISTORICO_ITEM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **HISTORICO_ITEM** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |
| [ITEM](dados_item) | \| **ITEM** \| **HISTORICO_ITEM** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |

**Exemplo 1: join com a tabela ITEM**

```
select HISTORICO_ITEM.*
from HISTORICO_ITEM, ITEM
where HISTORICO_ITEM.ID_ITEM = ITEM.ID_ITEM
```
