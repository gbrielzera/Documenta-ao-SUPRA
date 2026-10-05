# TEMPO_ANO

Caminho: Customização > Modelo de dados > Processo > TEMPO_ANO

Tempos registrados para cada solucionador em decorrência de configuração do Acordo de Nível Operacional.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OCORRENCIA** | Identificador da Ocorrência que está sendo executada. Utilizado como chave composta para o registro de execução de atividade. | int | number(6,0) | Não |
| **SEQUENCIAL** | Sequencial da atividade executada em uma ocorrência. | int | number(6,0) | Não |
| **ID_SOLUCIONADOR** | Identificador do solucionador envolvido na execução da atividade | int | number(6,0) | Não |
| **TEMPO** | Tempo atribuído a um Solucionador na execução de uma atividade com acordo de nível operacional. Este valor é preenchido quando ocorre um encaminhamento (troca de responsabilidade), finalização da atividade ou cancelamento da atividade. | int | number(6,0) | Não |
| **DATA_HORA_REGISTRO** | Data e hora em que foi gerado do registro de tempo/responsabilidade. | datetime | date | Não |
| **TEMPO_SEG** | Complemento em segundos do tempo atribuído a um Solucionador na execução de uma atividade com acordo de nível operacional. Este valor é preenchido quando ocorre um encaminhamento (troca de responsabilidade), finalização da atividade ou cancelamento da atividade. | int | number(6,0) | Não |

Tabelas referenciadas por TEMPO_ANO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **TEMPO_ANO** \| \|---\|---\| \| ID_PESSOA \| ID_SOLUCIONADOR \| |
| [EXECUCAO_ATIVIDADE](dados_execucao_atividade) | \| **EXECUCAO_ATIVIDADE** \| **TEMPO_ANO** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| \| SEQUENCIAL \| SEQUENCIAL \| |
