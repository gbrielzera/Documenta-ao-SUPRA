# RECEPTOR

Caminho: Customização > Modelo de dados > Processo > RECEPTOR

Atividade de entrada em um Gateway

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_RECEPTOR** | Número sequencial gerado automaticamente pelo sistema para Identificar um Receptor | int | number(6,0) | Não |
| **ID_ATIVIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Atividade | int | number(6,0) | Sim |
| **ID_GATEWAY** | Número sequencial gerado automaticamente pelo sistema para Identificar um Gateway | int | number(6,0) | Não |
| **ID_GATEWAY_ENT** | Gateway de entrada. | int | number(6,0) | Sim |

Tabelas referenciadas por RECEPTOR

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **RECEPTOR** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [GATEWAY](dados_gateway) | \| **GATEWAY** \| **RECEPTOR** \| \|---\|---\| \| ID_GATEWAY \| ID_GATEWAY_ENT \| |
| [GATEWAY](dados_gateway) | \| **GATEWAY** \| **RECEPTOR** \| \|---\|---\| \| ID_GATEWAY \| ID_GATEWAY \| |

**Exemplo 1: join com a tabela GATEWAY**

```
select RECEPTOR.*, GATEWAY.DESCRICAO
from RECEPTOR left outer join GATEWAY on RECEPTOR.ID_GATEWAY_ENT = GATEWAY.ID_GATEWAY
```

**Exemplo 2: join com a tabela GATEWAY**

```
select RECEPTOR.*
from RECEPTOR, GATEWAY
where RECEPTOR.ID_GATEWAY = GATEWAY.ID_GATEWAY
```
