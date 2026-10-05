# INTER_SLA

Caminho: Customização > Modelo de dados > Processo > INTER_SLA

Apontamento de interrupção de contagem de tempo estabelecido em Acordo de Nível de Serviço

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **DATA_HORA_INICIO** | Data/hora de início da interrupção | datetime | date | Não |
| **ID_MOTIVO_INTER** | Identificador da AcordoInterrupcaoSLA associada | int | number(6,0) | Não |
| **ID_SLA** | Identificador do Acordo de Nível de Serviço | int | number(6,0) | Não |
| **ID_OCORRENCIA** | Identificador da Ordem de Serviço | int | number(6,0) | Não |
| **DATA_HORA_FIM** | Data/hora de fim da interrupção | datetime | date | Sim |
| **SITUACAO** | Situação | varchar(250) | varchar(250) | Não |
| **TEMPO_INTER** | Tempo de interrução (em minutos) resultado da interrupção. Neste tempo já é considerada a disponibilidade de serviço definida no Acordo de Nível de Serviço firmado com o Cliente. Este valor é calculado pela rotina de finalização de interrupção de ANS. | int | number(6,0) | Sim |
| **ID_ATIVIDADE_GERADORA** | Identificador da Atividade de Processo que gerou a interrupção de ANS | int | number(6,0) | Sim |
| **DATA_HORA_FIM_PREV** | Data e hora previsto para finalização da interrupção. Após este momento é reiniciada a contagem de tempo do acordo. | datetime | date | Sim |
| **QTD_HORAS_AVISO_FIM** | Quantidade de horas anterior ao fim previsto utilizado para envio de aviso. O comunicado é configurado como um Tipo de Evento e visualizado na aba de comunicados da Ordem de Serviço. | int | number(6,0) | Sim |
| **COMENTARIO** | Comentário ou justificativa sobre a interrupção. Este comentário é replicado como evento da Ordem de Serviço e em caso de motivo que exija aprovação esta informação é exibida na página de aprovçavação do Autoatendimento. | varchar(500) | varchar(500) | Sim |
| **ENVIOU_AVISO** | Indica que foi enviado o aviso prévio sobre fim da interrupção programada. | char(3) | char(3) | Não |

Tabelas referenciadas por INTER_SLA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ACORDO_INTER_SLA](dados_acordo_inter_sla) | \| **ACORDO_INTER_SLA** \| **INTER_SLA** \| \|---\|---\| \| ID_SLA \| ID_SLA \| \| ID_MOTIVO_INTER \| ID_MOTIVO_INTER \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **INTER_SLA** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE_GERADORA \| |
| [ORDEM_SERVICO](dados_ordem_servico) | \| **ORDEM_SERVICO** \| **INTER_SLA** \| \|---\|---\| \|  \| ID_OCORRENCIA \| |

Tabelas que dependem de INTER_SLA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [VERSAO_APROVACAO](dados_versao_aprovacao) | \| **VERSAO_APROVACAO** \| **INTER_SLA** \| \|---\|---\| \| DATA_HORA_INICIO_INT \| DATA_HORA_INICIO \| \| ID_MOTIVO_INTER \| ID_MOTIVO_INTER \| \| ID_SLA \| ID_SLA \| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |

**Exemplo 1: join com a tabela ORDEM_SERVICO**

```
select INTER_SLA.*
from INTER_SLA, ORDEM_SERVICO
where INTER_SLA.ID_OCORRENCIA = ORDEM_SERVICO.
```
