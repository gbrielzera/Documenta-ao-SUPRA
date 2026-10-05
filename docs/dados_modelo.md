# MODELO

Caminho: Customização > Modelo de dados > Ativos > MODELO

Modelo de Item de Configuração segundo especificação de um Fabricante.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_MODELO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Modelo | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada sobre o Modelo | varchar(500) | varchar(500) | Não |
| **ATIVO** | Indica que o Modelo está ativo no sistema | char(3) | char(3) | Não |
| **ID_FABRICANTE** | Identificador do Fabricante associado ao Modelo | int | number(6,0) | Sim |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas referenciadas por MODELO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [FABRICANTE](dados_fabricante) | \| **FABRICANTE** \| **MODELO** \| \|---\|---\| \| ID_FABRICANTE \| ID_FABRICANTE \| |

Tabelas que dependem de MODELO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM](dados_item) | \| **ITEM** \| **MODELO** \| \|---\|---\| \| ID_MODELO \| ID_MODELO \| |
| [ITEM_COMPONENTE](dados_item_componente) | \| **ITEM_COMPONENTE** \| **MODELO** \| \|---\|---\| \| ID_MODELO \| ID_MODELO \| |

**Exemplo 1: join com a tabela FABRICANTE**

```
select MODELO.*, FABRICANTE.DESCRICAO
from MODELO left outer join FABRICANTE on MODELO.ID_FABRICANTE = FABRICANTE.ID_FABRICANTE
```
