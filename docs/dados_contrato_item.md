# CONTRATO_ITEM

Caminho: Customização > Modelo de dados > Recurso > CONTRATO_ITEM

Relaciona Itens de Configuração com o Contrato e define valor mensal para manutenção.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CONTRATO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Contrato | int | number(6,0) | Não |
| **ID_ITEM** | Identificador do Item de Configuração mantido pelo Contrato | int | number(6,0) | Não |
| **VALOR_MENSAL** | Valor mensal para manutenção do Item de Configuração | decimal(15,2) | number(15,2) | Não |

Tabelas referenciadas por CONTRATO_ITEM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM](dados_item) | \| **ITEM** \| **CONTRATO_ITEM** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |
| [CONTRATO](dados_contrato) | \| **CONTRATO** \| **CONTRATO_ITEM** \| \|---\|---\| \| ID_CONTRATO \| ID_CONTRATO \| |

**Exemplo 1: join com a tabela CONTRATO**

```
select CONTRATO_ITEM.*
from CONTRATO_ITEM, CONTRATO
where CONTRATO_ITEM.ID_CONTRATO = CONTRATO.ID_CONTRATO
```
