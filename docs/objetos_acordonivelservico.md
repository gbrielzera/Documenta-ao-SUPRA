# AcordoNivelServico

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico

Um Calendário é um cadastro que contém feriados e períodos úteis de trabalho. O Calendário pode ser utilizado no cálculo de Acordos de Nível de Serviço quando este habilita o uso de feriados. O calendário é utilizado também no cálculo do Acordo de Nível Operacional servindo de referência para determinar tempos aplicados na execução de atividades. É importante que o solucionador tenha um calendário associado caso contrário o recurso terá sua disponibilidade equivalente a 24x7 (24 dias da semana x 7 dias da semana). Outra aplicação de um calendário está na apuração de indicadores de desempenho. Neste caso os calendários são utilizados para determinar a quantidade de dias úteis no mês apurado e influenciar no cálculo de ritmo.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AplicacoesProcesso** | Processos em que o Acordo de Nível de Serviço será aplicado. | [Lista de AplicacaoProcesso](objetos_aplicacaoprocesso) |
| **ConsideraFeriados** | Indica que todos os feriados do calendário associado com o Cliente são desconsiderados no cálculo de tempo (o intervalo referente ao feriado é excluído da contagem de tempo). Para consultar o calendário do cliente acesse o cadastro da Unidade onde está localizado o cliente (campo Local no cadastro da Pessoa). | Booleano |
| **CriterioChargeBack** | Forma de cálculo de Charge-back para o Acordo de Nivel de Serviço. | [CriterioChargeBackAcordo](enum_criteriochargebackacordo) |
| **DataFimValidade** | Data de fim de validade do Acordo de Nível de Serviço. Uma Ordem de Serviço só pode ser associada a um acordo cuja data de fim de validade seja menor que a data de abertura da ocorrência. | Data/hora |
| **DataInicioValidade** | Data de início de validade do Acordo de Nível de Serviço. Uma Ordem de Serviço só pode ser associada a um acordo cuja data de validade seja maior ou igual a data de abertura da ocorrência. | Data/hora |
| **Descricao** | Texto que descreve claramente a aplicação do Acordo de Nível de Serviço. Recomenda-se incluir o período de vigência e, quando possível, área atendida pelo Acordo. | String |
| **DisponibilidadeAtendimento** | Disponibilidade de atendimento (horário de início e horário de fim) nos dias da semana. A disponibilidae é levada em consideração no cálculo do tempo restante de atendimento. | [Lista de DisponibilidadeAtendimento](objetos_disponibilidadeatendimento) |
| **FormulaChargeBack** | Fórmula para cálculo de Charge-back em um determinado mês. Se o critério de Charge-back for 'Fórmula' ou 'ValorFixo' então esta fórmula é executada uma única vez e deve retornar o valor para Charge-back no período, caso contrário é executada para todo item calculado e permite a modificação do valor calculado inicialmente pelo sistema. | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um AcordoNivelServico | Inteiro |
| **InterrupcoesAcordadas** | Interrupções acordadas na cronometragem do tempo total de atendimento. | [Lista de AcordoInterrupcaoSLA](objetos_acordointerrupcaosla) |
| **Itens** | Itens do Acordo do Nível de Serviço que define o tempo de atendimento de uma Ordem de Serviço. Para determinar o Acordo de Nível de Serviço o sistema compara a Ordem de Serviço e os vários Critérios de Acordos cujo Cliente possui lotação relacionada (levando-se em conta hierarquia entre Órgãos e parâmetro de incluir sub-áreas de Acordos) são comparados levando-se em consideração aquele que apresenta o menor tempo de atendimento. | [Lista de ItemSLA](objetos_itemsla) |
| **OrgaosAtendidos** | Relação de Órgãos atendidos pelo ANS | [Lista de OrgaoAtendidoANS](objetos_orgaoatendidoans) |
| **Penalizacao** | Penalização aplicada no valor de Charge-back caso existam Ordens de Serviço em que não foi cumprido o Acordo de Nível de Serviço. Esta regra é válida somente para as opções de Charge-back 'Ocorrencia' e 'Hora'. | Inteiro |
| **PlanoGestao** | Conjunto de Indicadores de Desempenho (meta e realizado) para gerenciar o cumprimento do Acordo de Nível de Serviço. | [PlanoGestao](objetos_planogestao) |
| **PlanoGestaoId** | Identificador do Plano de Gestao associado | Inteiro |
| **PublicaInformacoesAA** | Permite publicar ou não informações sobre ANS no site de Autoatendimento. As informações são exibidas no Autoatendimento na página de consulta e na finalização de abertura de uma Ordem de Serviço. | Booleano |
| **ValorChargeBack** | Valor para cobrança pela rotina de Charge-back. Se o critério de charge-back for 'Hora' então o valor total é obtido pela multiplicação do 'Valor' pela quantidade de horas apontadas no período de apuração. Se o critério de charge-back for 'Ocorrência' então o total é obtido pela multiplicação do 'Valor' pela quantidade total de ocorrências finalizadas no período de apuração. Para o critério 'ValorFixo' o campo 'Valor' já indica o total de charge-back enquanto nos critérios 'Nenhum' ou 'Formula' não fazem uso desta informação. | Decimal |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **ObtemSLA** | Resolve identificação do critério de ANS para a Ordem de Serviço fornecida como parâmetro. | Venki.Supravizio.Recurso.ItemSLA ObtemSLA(Venki.Supravizio.Recurso.Pessoa cliente, Venki.Supravizio.Processo.ClasseServico classeServico, Venki.Supravizio.Processo.Servico servico, Venki.Supravizio.Processo.GrauPrioridade grauPrioridade, DateTime dataReferencia, Venki.Supravizio.Processo.ClasseSubProcesso classeSubProcesso,Venki.Supravizio.Recurso.Pessoa responsavel); |
| **ObtemOrdensServico** | Recupera Ordens de Serviço atendidas pelo Acordo em um período. | Venki.Supravizio.Processo.OrdemServicoList ObtemOrdensServico(DateTime dataInicio, DateTime dataFim); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | AcordoNivelServico Carrega(int i); |
| **Novo** | Cria um novo registro do tipo AcordoNivelServico | AcordoNivelServico Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | AcordoNivelServico Carrega(string nomePropriedade, object valorPropriedade); |
