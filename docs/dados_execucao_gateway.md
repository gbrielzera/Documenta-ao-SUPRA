# EXECUCAO_GATEWAY

Caminho: Customização > Modelo de dados > Processo > EXECUCAO_GATEWAY

Execução Gateway

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OCORRENCIA** | Identificador da Ocorrência | int | number(6,0) | Não |
| **SEQUENCIAL** | Sequencial de execução do Gateway em uma Ordem de Serviço | int | number(6,0) | Não |
| **DATA_HORA_EXEC** | Data e hora em que foi executado o Gateway | datetime | date | Não |
| **ID_EMISSOR** | Identificador do(a) Emissor associado(a) | int | number(6,0) | Não |
| **ID_RESPONSAVEL** | Identificador do Responsável pela tomada de Decisão | int | number(6,0) | Não |
| **MOTIVO** | Motivo informado pelo usuário para tomada de decisão. | text | clob | Sim |
| **CANCELADO** | Indica que a execução do gateway foi cancelada pelo usuário utilizando o comando Voltar do assistente de processos. | char(3) | char(3) | Não |

Tabelas referenciadas por EXECUCAO_GATEWAY

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **EXECUCAO_GATEWAY** \| \|---\|---\| \| ID_PESSOA \| ID_RESPONSAVEL \| |
| [EMISSOR](dados_emissor) | \| **EMISSOR** \| **EXECUCAO_GATEWAY** \| \|---\|---\| \| ID_EMISSOR \| ID_EMISSOR \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **EXECUCAO_GATEWAY** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |

**Exemplo 1: join com a tabela OCORRENCIA**

```
select EXECUCAO_GATEWAY.*
from EXECUCAO_GATEWAY, OCORRENCIA
where EXECUCAO_GATEWAY.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA
```
