# SV_JOB

Caminho: Customização > Modelo de dados > Utilitários > SV_JOB

Rotinas para execução em background via mecanismo Schedule

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_JOB** | Número sequencial gerado automaticamente pelo sistema para Identificar um Job | int | number(6,0) | Não |
| **DESCRIPTION** | Descrição detalhada do Job | varchar(500) | varchar(500) | Não |
| **REQUEST** | Objeto de Requisição contendo parâmetros de execução do Processo. | varbinary(4000) | blob | Não |
| **ID_CLASS** | Identificador do(a) Class associado(a) | int | number(6,0) | Não |
| **NEXT_TIME** | Data/hora da próxima execução. | datetime | date | Sim |
| **LAST_TIME** | Data/hora da última execução | datetime | date | Sim |
| **ENABLED** | Indica que o Job está ativo | char(3) | char(3) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **ID_USER_CREATOR** | Identificador do Usuário criador do Job | int | number(6,0) | Sim |
| **TYPE** | Tipo do Job que pode ser Público ou Privado. | varchar(250) | varchar(250) | Não |
| **PROCESS_PARAM** | Parâmetro para Classe de Processo | varchar(500) | varchar(500) | Sim |
| **CREATED_DATE** | Data e hora em que o Job foi criado. | datetime | date | Não |
| **STATUS** | Status do Job que pode ser Pendente, Executando, FinalizadoSucesso, FinalizadoFalha | varchar(250) | varchar(250) | Não |
| **CONTEXT_APP_ID** | Identificador da Aplicação | varchar(100) | varchar(100) | Não |
| **CONTEXT_ID_DOMAIN** | Identificador do Domínio onde será executado o Job | int | number(6,0) | Não |
| **CONTEXT_USERNAME** | Nome do usuário proprietário do Job | varchar(100) | varchar(100) | Não |
| **CONTEXT_ID_USER** | Identificador do Usuário proprietário do Job | int | number(6,0) | Não |
| **NEXT_TIME_PERIOD** | Período a ser acrescido em NextTime para agendamento da próxima execução. | int | number(6,0) | Não |
| **NEXT_TIME_PER_CNT** | Quantidade de Períodos a serem acrescentados em NextTime para próxima execução | int | number(6,0) | Não |
| **EMAIL_SUCCESS** | Email enviado para usuário em caso de sucesso | varchar(500) | varchar(500) | Sim |
| **EMAIL_FAILURE** | Email enviado a usuários em caso de falha na execução | varchar(500) | varchar(500) | Sim |
| **LAST_RUNNING_DATE** | Última informação de execução enquanto o Job estiver em execução. | datetime | date | Sim |
| **RUNNING_PROGRESS** | Progresso do job em execução. | int | number(6,0) | Sim |
| **RUNNING_RESULT** | Último resultado em processamento | varchar(500) | varchar(500) | Sim |
| **RUNNING_SERVER** | Servidor onde está sendo executado o Job. Este valor é preenchido somente enquanto um Job está sendo executado. | varchar(100) | varchar(100) | Sim |
| **ERROR_COUNT** | Número de execuções seguindas com ocorrência de Erros. Se for excedido um número máximo de erros seguidos então o Job não é mais processado. Sempre que ocorrer execução com sucesso então este contador é zerado. | int | number(6,0) | Não |
| **REPORT_EXPORT** | Formato de saída do arquivo gerado pelo relatório | varchar(250) | varchar(250) | Não |
| **NAME** | Nome do job que é exibido na transação Gerenciamento de Ambiente | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por SV_JOB

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_JOB** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |
| [SV_USER](dados_sv_user) | \| **SV_USER** \| **SV_JOB** \| \|---\|---\| \| ID_USER \| ID_USER_CREATOR \| |

Tabelas que dependem de SV_JOB

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_JOB_HISTORY](dados_sv_job_history) | \| **SV_JOB_HISTORY** \| **SV_JOB** \| \|---\|---\| \| ID_JOB \| ID_JOB \| |

**Exemplo 1: join com a tabela SV_CLASS**

```
select SV_JOB.*, SV_CLASS.NAME
from SV_JOB, SV_CLASS
where SV_JOB.ID_CLASS = SV_CLASS.ID_CLASS
```

**Exemplo 2: join com a tabela SV_USER**

```
select SV_JOB.*, SV_USER.USERNAME
from SV_JOB left outer join SV_USER on SV_JOB.ID_USER_CREATOR = SV_USER.ID_USER
```
