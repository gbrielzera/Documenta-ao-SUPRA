# Análise de Acordo de Nível Operacional

Caminho: Relatórios > Análise de Acordo de Nível Operacional

O relatório de Análise de Acordo de Nível Operacional tem por objetivo apresentar detalhadamente informações sobre o cumprimento de Acordos de Nível Operacional (ANO) configurados nas atividades (ou em grupos de atividades) executadas pelos solucionadores responsáveis ou envolvidos no processo. Com este relatório é possível analisar o desempenho de sua equipe e analisar o impacto de falhas de ANO em eventuais Acordos de Nível de Serviço (ANS).

## Parâmetros

Na figura abaixo podemos observar a tela de parâmetros para este relatório:

Parâmetros do relatório

| **Data Início** | Data de início da execução de atividades para recuperação. Recupera os registros cuja data de execução da atividade seja maior ou igual ao valor informado. |
|---|---|
| **Data Fim** | Data final da execução de atividades para recuperação. Recupera os registros cuja data de execução da atividade seja menor ou igual ao valor informado. |
| **Processo** | Filtra registros pelo processo associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Subprocesso** | Filtra registros de acordo com o Subprocesso associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Serviço** | Filtra registros pelo valor informado no campo Serviço da ocorrência. Se não for informado então este critério é desconsiderado na recuperação. |
| **Área Cliente** | Filtra os registros de acordo com o Área Cliente com o valor informado no campo Cliente da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui Sub-áreas** | Este parâmetro é utilizado em conjunto com o de Área Cliente. Se este parâmetro estiver marcado incluirá o Sub-Área do Orgão Cliente selecionado no campo anterior. |
| **Grupo Trabalho** | Filtra registros cujo responsável ou envolvido na execução da atividade (ou do grupo de atividades) seja do grupo informado. Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui sub-grupos** | Este parâmetro é utilizado em conjunto com o de Grupo de Trabalho. Se estiver marcado incluirá os sub-grupos do grupo selecionado no campo anterior. |
| **Solucionador** | Solucionador responsável ou envolvido na execução da atividade com ANO configurado. |
| **ANS comprometido** | Exibe apenas informações cujo ANO envolvido impactou no cumprimento de eventual ANS envolvido nas Ordens de Serviço em questão. |
| **Item Configuração** | Recupera Ordens de Serviço que tenha o item associado informado neste campo. Se não for informado então este critério é desconsiderado. |
| **Tipo Item ** | Recupera Ordens de Serviço que tenha um item associado do mesmo tipo informado neste campo. Se não for informado então este critério é desconsiderado. |
| **Exibir evolução diária** | Caso esteja marcado este campo, exibe informações detalhadas sobre a evolução diária de cada solucionador. |

Este relatório também está disponível na transação Workspace e é executado a partir da seleção de Ordens de Serviço:

## Saídas

Após informar os parâmetros de recuperação clique no botão Consultar para visualizar o conteúdo do relatório. Este relatório está dividido nos seguintes sub-relatórios:

### Totais por Grupos e por Solucionadores

Exibe de forma resumida o cumprimento de ANO agrupando as informações por Grupos de Trabalho, Solucionadores dos Grupos de Trabalhos e pelas Atividades (ou também os grupos de atividades) executadas por cada solucionador contabilizando seus respectivos totais.

### Resumo por Solucionador

Exibe de forma detalhada o cumprimento de ANO de cada solucionador, como responsável pela execução da atividade/grupo ou como envolvido. No grupo de colunas “Atendeu ANO” são exibidas as atividades que solucionador atendeu ao ANO definido indicando as atividades em que ele executou um ator definido no papel da atividade ou se executou sem ser um ator previsto para o papel. No grupo de colunas "Não atendeu ANO" são exibidas as atividades em que o ANO não foi atendido e se o solucionador era o responsável pela atividade/grupo ou apenas um envolvido.

### Relação de Ordens de Serviço

Exibe detalhadamente as Ordens de Serviço com ANO não cumpridos exibindo seus respectivos responsáveis. Exibe também informações sobre o impacto da falha no ANO no ANS.

Marcando a opção “ANS comprometido” da listagem de Parâmetros do relatório são listadas apenas as Ordens de Serviço cuja falha de ANO, tenham impactado na falha do ANS. Marcando esta opção, repare que a Ordem de Serviço 144 da listagem anterior, que não possui ANS comprometido, não é exibida na listagem, listando apenas as Ordens de Serviço com ANS comprometido:

### Relação de Ordens de Serviço por Envolvimento com Falha no ANO

Exibe de forma detalhada o envolvimento de solucionadores nos ANO com falha no cumprimento. Indica a participação do solucionador indicando o percentual de tempo de envolvimento com a atividade ou grupo de atividades.

### Evolução (diária) de solucionadores

Exibe detalhadamente a quantidade de atividades (ou grupo de atividades) executadas pelo solucionador indicando se este atendeu ou não os ANO envolvidos. Exibe, além disso, média de cumprimento de ANO da equipe para as datas exibidas.

Para dias que não fazem parte do período útil do solucionador (configurados no Calendário do Grupo de Trabalho que o solucionador faz parte), não são comparadas médias, a não ser que o solucionador execute atividades em dias que não fazem parte de seu período útil. Veja por exemplo na figura acima que os dias de 02/04 a 04/04 não são períodos úteis ou são feriados, porém o solucionador executou atividades nos dias 02/04 e 03/04 e nestas datas foi exibida a comparação com a média da equipe. Porém, como não executou atividades em 04/04, não são comparadas as médias deste este dia, embora possam haver atividades executadas por outros solucionadores.
