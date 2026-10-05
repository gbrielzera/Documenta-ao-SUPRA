# EXECUCAO_ATIVIDADE

Caminho: Customização > Modelo de dados > Processo > EXECUCAO_ATIVIDADE

Atividade executada por uma Ordem de Serviço

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OCORRENCIA** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Ocorrência | int | number(6,0) | Não |
| **SEQUENCIAL** | Sequencial de execução da Atividade em uma Ordem de Serviço | int | number(6,0) | Não |
| **ID_ATIVIDADE** | Atividade que foi executada na Ordem de Serviço | int | number(6,0) | Não |
| **DATA_HORA_INICIO** | Data/hora de início da Atividade | datetime | date | Não |
| **DATA_HORA_FIM** | Data/hora de fim da atividade. | datetime | date | Sim |
| **ID_PESSOA_FIM** | Solucionador que finalizou a Atividade | int | number(6,0) | Sim |
| **ID_PESSOA_INICIO** | Solucionador que inicou a Atividade | int | number(6,0) | Não |
| **RELATORIO** | Relatório feito pelo responsável pela ocorrência ao término ou durante a execução. | text | clob | Sim |
| **AVANC_AUTOMATICO** | Indica que durante a execução do script de Inicialização a variável AvancaProximaAtividade foi preenchida com o valor verdadeiro caracterizando uma atividade executada automaticamente pelo processo. | char(3) | char(3) | Não |
| **AVISO** | Aviso gerado por alguma execução automática da atividade. Exemplos: erro ao acessar o Active Directory, rodar um comando SQL etc. Estes avisos são exibidos como alertas para o usuário da interface gráfica. | varchar(500) | varchar(500) | Sim |
| **ORIGEM_AVISO** | Script que introduziu o erro/aviso detectado. | varchar(100) | varchar(100) | Sim |
| **FIN_ATENDE_PAPEL** | Indica que o usuário finalizador da atividade atendeu aos requisitos de papeis definidos em processo. | char(3) | char(3) | Sim |
| **CANCELADO** | Indica que a execução da atividade foi cancelada pelo usuário utilizando o comando Voltar do assistente de processos. | char(3) | char(3) | Não |
| **JUSTIFICA_ANO** | Justificativa fornecida por um coordenador de Grupo de Trabalho para indicação de um Solucionador como responsável pelo resultado do Acordo de Nível Operacional. | varchar(500) | varchar(500) | Sim |
| **ID_RESP_ANO** | Identificador do solucionador que será responsável pelo resultado do Acordo de Nível Operacional. Este solucionador pode ser indicado pelo coordenador do seu Grupo de Trabalho ou nível superior. | int | number(6,0) | Sim |
| **ID_IND_RESP** | Indentificador do coordenador de Grupo de Trabalho que indicou o Solucionador responsável pelo resultado do Acordo de Nível Operacional. | int | number(6,0) | Sim |
| **TEMPO_ANO_REAL** | Tempo realizado (em minutos) do Acordo de Nível de Serviço considerando disponibilidade de recursos configurada no calendário. Este tempo é gravado pelo sistema no instante em que a atividade é finalizada. | int | number(6,0) | Sim |
| **TEMPO_ANO_PREV** | Tempo (em minutos) acordado e previsto para realização da tarefa. Este tempo é gravado pelo sistema no instante em que a atividade é finalizada. | int | number(6,0) | Sim |
| **DATA_HORA_IND_RESP** | Data e hora de indicação do responsável pelo Acordo de Nível Operacional. Este campo é preenchido pela operação de indicação de responsável com a data/hora corrente do sistema e não pode ser editada pelo usuário. | datetime | date | Sim |
| **TEMPO_EXEC** | Tempo de execução da atividade considerando o início, fim e calendário de períodos úteis de todos os solucionadores que participaram da atividade. Esta informação deve ser complementada pelo tempo total em dias. | int | number(6,0) | Sim |
| **TEMPO_EXEC_DIAS** | Total de dias considerando os períodos úteis do calendário dos recursos envolvidos. Esta informação deve ser complementada com o tempo em segundos. | int | number(6,0) | Sim |
| **NOME_TEC_FINAL** | Nome do solucionador que finalizou a tarefa. Esta finalização pode ter ocorrido de forma manual ou automática por intervenção da máquina de processos. | varchar(500) | varchar(500) | Sim |
| **NOME_TEC_INICIAL** | Nome do solucionador que iniciou a tarefa de processo | varchar(500) | varchar(500) | Não |
| **TEMPO_EXEC_LIQ** | Tempo de execução da atividade considerando o início, fim, calendário de períodos úteis de todos os solucionadores e por último períodos e interrupções de ANS. Esta informação deve ser complementada pelo tempo total em dias. | int | number(6,0) | Sim |
| **TEMPO_EXEC_DIAS_LIQ** | Total de dias considerando os períodos úteis do calendário dos recursos envolvidos disponibilidade e paradas de ANS. Esta informação deve ser complementada com o tempo em segundos. | int | number(6,0) | Sim |
| **TEMPO_ANO_REAL_SEG** | Tempo realizado complementar do ANO. Deve ser adicionado ao tempo realizado em minutos. | int | number(6,0) | Sim |

Tabelas referenciadas por EXECUCAO_ATIVIDADE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **EXECUCAO_ATIVIDADE** \| \|---\|---\| \| ID_PESSOA \| ID_RESP_ANO \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **EXECUCAO_ATIVIDADE** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA_FIM \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **EXECUCAO_ATIVIDADE** \| \|---\|---\| \| ID_PESSOA \| ID_IND_RESP \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **EXECUCAO_ATIVIDADE** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA_INICIO \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **EXECUCAO_ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **EXECUCAO_ATIVIDADE** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |

Tabelas que dependem de EXECUCAO_ATIVIDADE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [TEMPO_ANO](dados_tempo_ano) | \| **TEMPO_ANO** \| **EXECUCAO_ATIVIDADE** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| \| SEQUENCIAL \| SEQUENCIAL \| |

**Exemplo 1: join com a tabela OCORRENCIA**

```
select EXECUCAO_ATIVIDADE.*
from EXECUCAO_ATIVIDADE, OCORRENCIA
where EXECUCAO_ATIVIDADE.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA
```
