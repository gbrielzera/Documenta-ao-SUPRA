# FERIADO

Caminho: Customização > Modelo de dados > Recurso > FERIADO

Um Feriado constitui uma data especial onde considerada, a princípio, dia não-útil.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CALENDARIO** | Identificador do Calendário | int | number(6,0) | Não |
| **DATA** | Dia, mês e ano do feriado | datetime | date | Não |
| **DESCRICAO** | Descrição detalhada do Feriado | varchar(500) | varchar(500) | Não |

Tabelas referenciadas por FERIADO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CALENDARIO](dados_calendario) | \| **CALENDARIO** \| **FERIADO** \| \|---\|---\| \| ID_CALENDARIO \| ID_CALENDARIO \| |

**Exemplo 1: join com a tabela CALENDARIO**

```
select FERIADO.*
from FERIADO, CALENDARIO
where FERIADO.ID_CALENDARIO = CALENDARIO.ID_CALENDARIO
```
