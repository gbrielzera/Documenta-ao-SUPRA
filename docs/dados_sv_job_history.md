# SV_JOB_HISTORY

Caminho: Customização > Modelo de dados > Utilitários > SV_JOB_HISTORY

Histórico de execuções de um Job

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_JOB** | Número sequencial gerado automaticamente pelo sistema para Identificar um Job | int | number(6,0) | Não |
| **DATE_TIME** | Data e hora da execução do Job | datetime | date | Não |
| **REQUEST** | Parâmetros do Processo utilizado no instante da execução | varbinary(4000) | blob | Não |
| **STATUS** | Status final da execução do Job | varchar(250) | varchar(250) | Não |
| **START_TIME** | Início da execução do Job | datetime | date | Não |
| **END_TIME** | Fim da execução do Job | datetime | date | Não |
| **REPORT_DATA** | Log de modificações | varbinary(4000) | blob | Não |

Tabelas referenciadas por SV_JOB_HISTORY

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_JOB](dados_sv_job) | \| **SV_JOB** \| **SV_JOB_HISTORY** \| \|---\|---\| \| ID_JOB \| ID_JOB \| |

**Exemplo 1: join com a tabela SV_JOB**

```
select SV_JOB_HISTORY.*
from SV_JOB_HISTORY, SV_JOB
where SV_JOB_HISTORY.ID_JOB = SV_JOB.ID_JOB
```
