# VERSAO_APROVACAO

Caminho: Customização > Modelo de dados > Processo > VERSAO_APROVACAO

Versão para Aprovação

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ASSUNTO_APROVACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um AssuntoAprovacao | int | number(6,0) | Não |
| **VERSAO** | Sequencial gerado automaticamente pelo sistema para cada Assunto de uma determinada Ordem de Serviço | int | number(6,0) | Não |
| **DATA_HORA_CRIACAO** | Data e hora de Criação da Versão | datetime | date | Não |
| **DATA_HORA_INICIO** | Data e hora de início do processo de Aprovação | datetime | date | Sim |
| **SITUACAO** | Situação para a Versão a ser Aprovada. | varchar(250) | varchar(250) | Não |
| **DATA_HORA_FIM** | Data e hora de fim do processo de Aprovação. | datetime | date | Sim |
| **ESCOPO** | Texto contendo o Escopo para Aprovação. Quando preenchido é apresentado para o usuário na aplicação de aprovação de Ocorrências. | text | clob | Sim |
| **DATA_HORA_INICIO_INT** | Identificador da InterrupcaoSLA associada | datetime | date | Sim |
| **ID_MOTIVO_INTER** | Identificador da InterrupcaoSLA associada | int | number(6,0) | Sim |
| **ID_SLA** | Identificador da InterrupcaoSLA associada | int | number(6,0) | Sim |
| **ID_OCORRENCIA** | Identificador da InterrupcaoSLA associada | int | number(6,0) | Sim |
| **PASSO_CORRENTE** | Indica nível hierarquico de aprovação | int | number(6,0) | Não |
| **DATA_HORA_ULT_COMUNICADO** | Data e hora do último email de aprovação enviado. Dependendo da configuração do processo é possível repetir o envio e sempre que isto ocorrer esta propriedade será atualizada. | datetime | date | Não |

Tabelas referenciadas por VERSAO_APROVACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [INTER_SLA](dados_inter_sla) | \| **INTER_SLA** \| **VERSAO_APROVACAO** \| \|---\|---\| \| DATA_HORA_INICIO \| DATA_HORA_INICIO_INT \| \| ID_MOTIVO_INTER \| ID_MOTIVO_INTER \| \| ID_SLA \| ID_SLA \| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [ASSUNTO_APROVACAO](dados_assunto_aprovacao) | \| **ASSUNTO_APROVACAO** \| **VERSAO_APROVACAO** \| \|---\|---\| \| ID_ASSUNTO_APROVACAO \| ID_ASSUNTO_APROVACAO \| |

Tabelas que dependem de VERSAO_APROVACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [APROVACAO](dados_aprovacao) | \| **APROVACAO** \| **VERSAO_APROVACAO** \| \|---\|---\| \| ID_ASSUNTO_APROVACAO \| ID_ASSUNTO_APROVACAO \| \| VERSAO \| VERSAO \| |
| [ITEM_APROVACAO](dados_item_aprovacao) | \| **ITEM_APROVACAO** \| **VERSAO_APROVACAO** \| \|---\|---\| \| ID_ASSUNTO_APROVACAO \| ID_ASSUNTO_APROVACAO \| \| VERSAO \| VERSAO \| |
| [APROPRIACAO_APROVACAO](dados_apropriacao_aprovacao) | \| **APROPRIACAO_APROVACAO** \| **VERSAO_APROVACAO** \| \|---\|---\| \| ID_ASSUNTO_APROVACAO \| ID_ASSUNTO_APROVACAO \| \| VERSAO \| VERSAO \| |

**Exemplo 1: join com a tabela ASSUNTO_APROVACAO**

```
select VERSAO_APROVACAO.*
from VERSAO_APROVACAO, ASSUNTO_APROVACAO
where VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO = ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO
```
