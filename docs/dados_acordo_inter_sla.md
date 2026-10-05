# ACORDO_INTER_SLA

Caminho: Customização > Modelo de dados > Recurso > ACORDO_INTER_SLA

Motivos de interrupção habilitados para o Acordo de Nível de Serviço. Um motivo pode estar condicionado a uma aprovação.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_SLA** | Identificador do Acordo de Nível de Serviço proprietário da regra de interrupção de cronometragem de tempo. | int | number(6,0) | Não |
| **ID_MOTIVO_INTER** | Identificador do Motivo de interrução para cronometragem de tempo de atendimento. | int | number(6,0) | Não |

Tabelas referenciadas por ACORDO_INTER_SLA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [MOTIVO_INTER_SLA](dados_motivo_inter_sla) | \| **MOTIVO_INTER_SLA** \| **ACORDO_INTER_SLA** \| \|---\|---\| \| ID_MOTIVO_INTER_SLA \| ID_MOTIVO_INTER \| |
| [SLA](dados_sla) | \| **SLA** \| **ACORDO_INTER_SLA** \| \|---\|---\| \| ID_SLA \| ID_SLA \| |

Tabelas que dependem de ACORDO_INTER_SLA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [APROV_INTER_SLA](dados_aprov_inter_sla) | \| **APROV_INTER_SLA** \| **ACORDO_INTER_SLA** \| \|---\|---\| \| ID_SLA \| ID_SLA \| \| ID_MOTIVO_INTER \| ID_MOTIVO_INTER \| |

**Exemplo 1: join com a tabela MOTIVO_INTER_SLA**

```
select ACORDO_INTER_SLA.*, MOTIVO_INTER_SLA.DESCRICAO
from ACORDO_INTER_SLA, MOTIVO_INTER_SLA
where ACORDO_INTER_SLA.ID_MOTIVO_INTER = MOTIVO_INTER_SLA.ID_MOTIVO_INTER_SLA
```

**Exemplo 2: join com a tabela SLA**

```
select ACORDO_INTER_SLA.*
from ACORDO_INTER_SLA, SLA
where ACORDO_INTER_SLA.ID_SLA = SLA.ID_SLA
```
