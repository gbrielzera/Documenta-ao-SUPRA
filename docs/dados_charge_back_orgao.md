# CHARGE_BACK_ORGAO

Caminho: Customização > Modelo de dados > Recurso > CHARGE_BACK_ORGAO

Conta de charge-back destinada a uma área.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CHARGE_BACK** | Número sequencial gerado automaticamente pelo sistema para Identificar um ChargeBack | int | number(6,0) | Não |
| **ID_ORGAO** | Identificador do Orgao associado | int | number(6,0) | Não |
| **VALOR_TOTAL** | Valor total apurado para uma área de negócio. | decimal(15,2) | number(15,2) | Não |

Tabelas referenciadas por CHARGE_BACK_ORGAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ORGAO](dados_orgao) | \| **ORGAO** \| **CHARGE_BACK_ORGAO** \| \|---\|---\| \| ID_ORGAO \| ID_ORGAO \| |
| [CHARGE_BACK](dados_charge_back) | \| **CHARGE_BACK** \| **CHARGE_BACK_ORGAO** \| \|---\|---\| \| ID_CHARGE_BACK \| ID_CHARGE_BACK \| |

Tabelas que dependem de CHARGE_BACK_ORGAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM_CHARGE_BACK](dados_item_charge_back) | \| **ITEM_CHARGE_BACK** \| **CHARGE_BACK_ORGAO** \| \|---\|---\| \| ID_CHARGE_BACK \| ID_CHARGE_BACK \| \| ID_ORGAO \| ID_ORGAO \| |

**Exemplo 1: join com a tabela ORGAO**

```
select CHARGE_BACK_ORGAO.*, ORGAO.DESCRICAO
from CHARGE_BACK_ORGAO, ORGAO
where CHARGE_BACK_ORGAO.ID_ORGAO = ORGAO.ID_ORGAO
```

**Exemplo 2: join com a tabela CHARGE_BACK**

```
select CHARGE_BACK_ORGAO.*
from CHARGE_BACK_ORGAO, CHARGE_BACK
where CHARGE_BACK_ORGAO.ID_CHARGE_BACK = CHARGE_BACK.ID_CHARGE_BACK
```
