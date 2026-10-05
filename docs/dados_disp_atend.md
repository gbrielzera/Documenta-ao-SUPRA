# DISP_ATEND

Caminho: Customização > Modelo de dados > Recurso > DISP_ATEND

Relação de períodos na semana de disponibilidade do serviço, ou seja, os períodos onde será contabilizado o tempo de atendimento.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_DISP_ATEND** | Número sequencial gerado automaticamente pelo sistema para Identificar um DisponibilidadeAtendimento | int | number(6,0) | Não |
| **ID_SLA** | Identificador do Acordo de Nível de Serviço proprietário da disponibilidade de atendimento. | int | number(6,0) | Não |
| **DIA_SEMANA** | Dia da semana | varchar(250) | varchar(250) | Não |
| **HORA_INICIO** | Hora de início do período de disponibilidade (0 a 23) | int | number(6,0) | Não |
| **MIN_INICIO** | Minuto de início (0 a 59) | int | number(6,0) | Não |
| **HORA_FIM** | Hora de fim do período de disponibilidade (0 a 23) | int | number(6,0) | Não |
| **MIN_FIM** | Minuto de fim da disponibilidade (0 a 59) | int | number(6,0) | Não |

Tabelas referenciadas por DISP_ATEND

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SLA](dados_sla) | \| **SLA** \| **DISP_ATEND** \| \|---\|---\| \| ID_SLA \| ID_SLA \| |

**Exemplo 1: join com a tabela SLA**

```
select DISP_ATEND.*
from DISP_ATEND, SLA
where DISP_ATEND.ID_SLA = SLA.ID_SLA
```
