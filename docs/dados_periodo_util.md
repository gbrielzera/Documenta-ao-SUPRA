# PERIODO_UTIL

Caminho: Customização > Modelo de dados > Recurso > PERIODO_UTIL

Regra que define a disponibilidade de recursos em função dos dias da semana.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PERIODO_UTIL** | Número sequencial gerado automaticamente pelo sistema para Identificar um PeriodoUtil | int | number(6,0) | Não |
| **DIA_SEMANA** | Dia da semana | varchar(250) | varchar(250) | Não |
| **HORA_INICIO** | Hora de início do período de disponibilidade (0 a 23) | int | number(6,0) | Não |
| **MINUTO_INICIO** | Minuto de início (0 a 59) | int | number(6,0) | Não |
| **HORA_FIM** | Hora de fim do período de disponibilidade (0 a 23) | int | number(6,0) | Não |
| **MINUTO_FIM** | Minuto fim (0 a 59) | int | number(6,0) | Não |
| **DISPONIBILIDADE** | Validade da regra em função da semana | varchar(250) | varchar(250) | Não |
| **ID_CALENDARIO** | Identificador do Calendário proprietário da regra de disponibilidade | int | number(6,0) | Não |

Tabelas referenciadas por PERIODO_UTIL

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CALENDARIO](dados_calendario) | \| **CALENDARIO** \| **PERIODO_UTIL** \| \|---\|---\| \| ID_CALENDARIO \| ID_CALENDARIO \| |

**Exemplo 1: join com a tabela CALENDARIO**

```
select PERIODO_UTIL.*
from PERIODO_UTIL, CALENDARIO
where PERIODO_UTIL.ID_CALENDARIO = CALENDARIO.ID_CALENDARIO
```
