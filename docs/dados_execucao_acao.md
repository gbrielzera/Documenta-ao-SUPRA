# EXECUCAO_ACAO

Caminho: Customização > Modelo de dados > Processo > EXECUCAO_ACAO

Execução de Ação prevista em Acordo

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ACAO_ACORDO** | Identificador da Ação executada | int | number(6,0) | Não |
| **ID_OCORRENCIA** | Número sequencial gerado automaticamente pelo sistema para Identificar um Ocorrência | int | number(6,0) | Não |
| **DATA_HORA_EXEC** | Data e hora em que foi executada a ação. | datetime | date | Não |

Tabelas referenciadas por EXECUCAO_ACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ACAO_ACORDO](dados_acao_acordo) | \| **ACAO_ACORDO** \| **EXECUCAO_ACAO** \| \|---\|---\| \| ID_ACAO_ACORDO \| ID_ACAO_ACORDO \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **EXECUCAO_ACAO** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |

**Exemplo 1: join com a tabela OCORRENCIA**

```
select EXECUCAO_ACAO.*
from EXECUCAO_ACAO, OCORRENCIA
where EXECUCAO_ACAO.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA
```
