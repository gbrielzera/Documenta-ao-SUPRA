# Pendências acumuladas

Caminho: Relatórios > Pendências acumuladas

O relatório de Pendências de Acumuladas tem por objetivo apresentar um resumo quantitativo das Ordens de Serviços acumuladas sem finalização até o período consultado. Com este relatório é possível analisar o desempenho de grupos de trabalho e de solucionadores de acordo com a quantidade de Ordens de Serviço que estão permanecendo com pendências acumuladas.

## Parâmetros

Na figura abaixo podemos observar a tela de parâmetros para este relatório:

Parâmetros do relatório

| **Data Início** | Data de início para recuperação das Ordens de Serviço. Este parâmetro recupera as Ordens de serviço abertas e finalizadas cuja data seja maior ou igual ao valor informado. |
|---|---|
| **Data Fim** | Data limite fim para recuperação das Ordens de Serviço. Este parâmetro recupera as Ordens de serviço abertas e finalizadas cuja data seja menor ou igual ao valor informado. |
| **Área Cliente** | Filtra os registros de acordo com o Área Cliente com o valor informado no campo Cliente da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui sub-áreas** | Este parâmetro é utilizado em conjunto com o de Área Cliente. Se este parâmetro estiver marcado incluirá o Sub-orgão do Orgão Cliente selecionado no campo anterior. |
| **Serviço** | Filtra registros pelo valor informado no campo Serviço da ocorrência. Se não for informado então este critério é desconsiderado na recuperação. |
| **Processo** | Filtra registros pelo Processo associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Subprocesso** | Filtra registros de acordo com o Subprocesso associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Grupo de Trabalho** | Filtra registros cujo responsável corrente ou último responsável seja do grupo informado. Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui sub-grupos** | Este parâmetro é utilizado em conjunto com o de Grupo de Trabalho. Se estiver marcado incluirá os sub-grupos do grupo selecionado no campo anterior. |
| **Tipo Item** | Recupera Ordens de Serviço que tenha um item associado do mesmo tipo informado neste campo. Se não for informado então este critério é desconsiderado. |
| **Solucionador** | Este parâmetro filtra os registros de acordo com Solucionador Responsável pela Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |

Além do filtro de recuperação informado pelo usuário existe também outro implícito por macroprocessos, que é aplicado em consultas por usuários que não possuem o perfil Administrador. Na figura abaixo podemos observar a mensagem exibida no rodapé da tela de relatórios quando o usuário não possui o perfil Administrador:

Alerta sobre filtro por macroprocessos

## Saídas

Após informar os parâmetros de recuperação clique no botão **Consultar** para visualizar o conteúdo do relatório.

Na saída deste relatório é apresentado um gráfico que quantifica as Ordens de Serviço que foram abertas, finalizadas e as ocorrências que estão com pendências acumuladas em um determinado período.

Podemos observar no gráfico duas colunas e uma linha: a coluna amarela representa as Ordens de Serviço que estão Abertas, a coluna verde representa as Ordens de Serviço que estão Finalizadas e a linha em vermelho representa o acumulado que são aquelas Ordens de serviço que permanecem abertas nas filas dos solucionadores com pendências e sem finalização:

Pendências Acumuladas

Abaixo do gráfico é apresentada uma listagem quantitativa com a relação das Ordens de Serviço abertas, finalizadas e as que permanecem com pendências acumuladas de acordo com o período consultado. No cabeçalho desta listagem podemos observar que é quantificado também o número de Ordens de Serviço com Pendências anteriores ao período consultado:

Relação de Ordens de Serviço com pendência acumuladas
