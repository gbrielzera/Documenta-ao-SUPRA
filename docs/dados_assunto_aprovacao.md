# ASSUNTO_APROVACAO

Caminho: Customização > Modelo de dados > Processo > ASSUNTO_APROVACAO

Assunto para Aprovação

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ASSUNTO_APROVACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um AssuntoAprovacao | int | number(6,0) | Não |
| **ID_OCORRENCIA** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Ocorrência | int | number(6,0) | Não |
| **DESCRICAO** | Descricao detalhada | varchar(500) | varchar(500) | Não |
| **OPERACAO_ATIVIDADE** | Identificador da Operação Atividade que gerou o Assunto para Aprovação | int | number(6,0) | Sim |
| **ID_SLA** | Identificador da AcordoInterrupcaoSLA associada | int | number(6,0) | Sim |
| **ID_MOTIVO_INTER** | Identificador da AcordoInterrupcaoSLA associada | int | number(6,0) | Sim |

Tabelas referenciadas por ASSUNTO_APROVACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [OPERACAO_ATIVIDADE](dados_operacao_atividade) | \| **OPERACAO_ATIVIDADE** \| **ASSUNTO_APROVACAO** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| OPERACAO_ATIVIDADE \| |
| [ACORDO_INTER_SLA](dados_acordo_inter_sla) | \| **ACORDO_INTER_SLA** \| **ASSUNTO_APROVACAO** \| \|---\|---\| \| ID_SLA \| ID_SLA \| \| ID_MOTIVO_INTER \| ID_MOTIVO_INTER \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **ASSUNTO_APROVACAO** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |

Tabelas que dependem de ASSUNTO_APROVACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [VERSAO_APROVACAO](dados_versao_aprovacao) | \| **VERSAO_APROVACAO** \| **ASSUNTO_APROVACAO** \| \|---\|---\| \| ID_ASSUNTO_APROVACAO \| ID_ASSUNTO_APROVACAO \| |

**Exemplo 1: join com a tabela OCORRENCIA**

```
select ASSUNTO_APROVACAO.*
from ASSUNTO_APROVACAO, OCORRENCIA
where ASSUNTO_APROVACAO.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA
```
