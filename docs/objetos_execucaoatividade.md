# ExecucaoAtividade

Caminho: Customização > Modelo de objetos > Processo > ExecucaoAtividade

Atividade executada por uma Ordem de Serviço

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Atividade** | Uma Atividade de Processo corresponde a Tarefas, Subprocessos e Eventos de Processos. | [Atividade](objetos_atividade) |
| **AtividadeId** | Atividade que foi executada na Ordem de Serviço | Inteiro |
| **AvancouAutomatico** | Indica que durante a execução do script de Inicialização a variável AvancaProximaAtividade foi preenchida com o valor verdadeiro caracterizando uma atividade executada automaticamente pelo processo. | Booleano |
| **Aviso** | Aviso gerado por alguma execução automática da atividade. Exemplos: erro ao acessar o Active Directory, rodar um comando SQL etc. Estes avisos são exibidos como alertas para o usuário da interface gráfica. | String |
| **Cancelado** | Indica que a execução da atividade foi cancelada pelo usuário utilizando o comando Voltar do assistente de processos. | Booleano |
| **DataHoraFim** | Data/hora de fim da atividade. | Data/hora |
| **DataHoraIndicacaoResponsavel** | Data e hora de indicação do responsável pelo Acordo de Nível Operacional. Este campo é preenchido pela operação de indicação de responsável com a data/hora corrente do sistema e não pode ser editada pelo usuário. | Data/hora |
| **DataHoraInicio** | Data/hora de início da Atividade | Data/hora |
| **FinalizadorAtendePapel** | Indica que o usuário finalizador da atividade atendeu aos requisitos de papeis definidos em processo. | Booleano |
| **IndicadorResponsavel** | Coordenador de Grupo de Trabalho que indicou o responsável pelo Acordo de Nível Operacional. Um coordenador só pode indicar um solucionador de um dos seus grupos coordenados. | [Pessoa](objetos_pessoa) |
| **IndicadorResponsavelId** | Indentificador do coordenador de Grupo de Trabalho que indicou o Solucionador responsável pelo resultado do Acordo de Nível Operacional. | Inteiro |
| **JustificativaIndicacaoANO** | Justificativa fornecida por um coordenador de Grupo de Trabalho para indicação de um Solucionador como responsável pelo resultado do Acordo de Nível Operacional. | String |
| **NomeTecnicoFinal** | Nome do solucionador que finalizou a tarefa. Esta finalização pode ter ocorrido de forma manual ou automática por intervenção da máquina de processos. | String |
| **NomeTecnicoInicial** | Nome do solucionador que iniciou a tarefa de processo | String |
| **OcorrenciaId** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Ocorrência | Inteiro |
| **OrigemAviso** | Script que introduziu o erro/aviso detectado. | String |
| **Relatorio** | Relatório feito pelo responsável pela ocorrência ao término ou durante a execução. | String |
| **ResponsavelANO** | Pessoa responsável pelo resultado do Acordo de Nível Operacional. Esta pessoa pode ser definida automaticamente pelo sistema que selecionará aquela que teve a maior parcela de tempo sob sua responsabilidade ou pode ser indicado manualmente por um de seus coordenadores. Neste último caso o coordenador deve indicar uma justificativa. | [Pessoa](objetos_pessoa) |
| **ResponsavelANOId** | Identificador do solucionador que será responsável pelo resultado do Acordo de Nível Operacional. Este solucionador pode ser indicado pelo coordenador do seu Grupo de Trabalho ou nível superior. | Inteiro |
| **Sequencial** | Sequencial de execução da Atividade em uma Ordem de Serviço | Inteiro |
| **TecnicoFinal** | Solucionador que finalizou a Atividade | [Pessoa](objetos_pessoa) |
| **TecnicoFinalId** | Solucionador que finalizou a Atividade | Inteiro |
| **TecnicoInicial** | Solucionador que iniciou a Atividade | [Pessoa](objetos_pessoa) |
| **TecnicoInicialId** | Solucionador que inicou a Atividade | Inteiro |
| **TempoANOPrevisto** | Tempo (em minutos) acordado e previsto para realização da tarefa. Este tempo é gravado pelo sistema no instante em que a atividade é finalizada. | Inteiro |
| **TempoANORealizado** | Tempo realizado (em minutos) do Acordo de Nível de Serviço considerando disponibilidade de recursos configurada no calendário. Este tempo é gravado pelo sistema no instante em que a atividade é finalizada. | Inteiro |
| **TempoANORealizadoSegundos** | Tempo realizado complementar do ANO. Deve ser adicionado ao tempo realizado em minutos. | Inteiro |
| **TempoExecucaoDias** | Total de dias considerando os períodos úteis do calendário dos recursos envolvidos. Esta informação deve ser complementada com o tempo em segundos. | Inteiro |
| **TempoExecucaoLiquidosDias** | Total de dias considerando os períodos úteis do calendário dos recursos envolvidos disponibilidade e paradas de ANS. Esta informação deve ser complementada com o tempo em segundos. | Inteiro |
| **TempoExecucaoLiquidoSegundos** | Tempo de execução da atividade considerando o início, fim, calendário de períodos úteis de todos os solucionadores e por último períodos e interrupções de ANS. Esta informação deve ser complementada pelo tempo total em dias. | Inteiro |
| **TempoExecucaoSegundos** | Tempo de execução da atividade considerando o início, fim e calendário de períodos úteis de todos os solucionadores que participaram da atividade. Esta informação deve ser complementada pelo tempo total em dias. | Inteiro |
| **TemposANO** | Log de tempos realizados pelos vários solucionadores envolvidos na execução da atividade. | [Lista de TemposANO](objetos_temposano) |
