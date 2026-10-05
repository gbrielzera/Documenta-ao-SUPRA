# APLIC_PROCESSO

Caminho: Customização > Modelo de dados > Recurso > APLIC_PROCESSO

Relação de subprocessos onde o Acordo de Nível de Serviço pode ser aplicado.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_SLA** | Identificador do ANS que contém a regra de aplicação em Processos. | int | number(6,0) | Não |
| **ID_CLASSE_SUB_PROCESSO** | Identificador do Tipo de Subprocesso associado | int | number(6,0) | Não |

Tabelas referenciadas por APLIC_PROCESSO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_SUB_PROCESSO](dados_classe_sub_processo) | \| **CLASSE_SUB_PROCESSO** \| **APLIC_PROCESSO** \| \|---\|---\| \| ID_CLASSE_SUB_PROCESSO \| ID_CLASSE_SUB_PROCESSO \| |
| [SLA](dados_sla) | \| **SLA** \| **APLIC_PROCESSO** \| \|---\|---\| \| ID_SLA \| ID_SLA \| |

**Exemplo 1: join com a tabela SLA**

```
select APLIC_PROCESSO.*
from APLIC_PROCESSO, SLA
where APLIC_PROCESSO.ID_SLA = SLA.ID_SLA
```
