# Ordens de Serviço por Processo

Caminho: Relatórios > Ordens de Serviço por Processo

O relatório de Ordens de Serviço por Processo tem por objetivo apresentar um resumo quantitativo das Ordens de Serviços de acordo com o Processo associado com a classificação das ocorrências. Com este relatório é possível identificar quais os Processos possuem mais ocorrência

## Parâmetros

Na figura abaixo podemos observar a tela de parâmetros para este relatório:

Parâmetros do relatório

| **Tipo Filtro** | Este parâmetro está relacionado com a **Data início** e **Data fim** de recuperação e possui as seguintes opções: - **Abertas em**: recupera Ordens de Serviços abertas entre a data início e data fim, não importando a situação corrente do registro. - **Abertas e não solucionadas em**: recupera Ordens de Serviço abertas entra a data de início e data fim e que não foram finalizadas até o momento. Importante: a situação Cancelada é considerada uma finalização e portanto registros nesta situação não serão recuperados. - **Finalizadas em**: recupera Ordens de Serviço finalizadas entre a data início e data fim. Ordens de Serviço canceladas são desconsideradas nesta opção. - **Canceladas em**: recupera Ordens de Serviço canceladas entre a data início e data fim, considerando para isto a data/hora do último cancelamento para o registro. Também são consideradas canceladas as ocorrências com finalização do tipo "Não- realizada". - **Reabertas em**: recupera Ordens de Serviço reabertas entre a data início e data fim. São consideradas todos os eventos de reabertura, ou seja, uma Ordem de Serviço pode constar em diversos períodos consultados. |
|---|---|
| **Data Início** | Data de início para recuperação. Este parâmetro é utilizado em conjunto com o tipo de filtro e recupera os registros cuja data de referência seja maior ou igual ao valor informado. |
| **Data Fim** | Data limite fim para recuperação. Este parâmetro é utilizado em conjunto com o tipo de filtro e recupera os registros cuja data de referência seja menor ou igual ao valor informado. |
| **Área Cliente** | Filtra os registros de acordo com o Área Cliente com o valor informado no campo Cliente da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui sub-áreas** | Este parâmetro é utilizado em conjunto com o de Área Cliente. Se este parâmetro estiver marcado incluirá o Sub-orgão do Orgão Cliente selecionado no campo anterior. |
| **Serviço** | Filtra registros pelo valor informado no campo Serviço da ocorrência. Se não for informado então este critério é desconsiderado na recuperação. |
| **Grupo de Trabalho** | Filtra registros cujo responsável corrente ou último responsável seja do grupo informado. Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui sub-grupos ** | Este parâmetro é utilizado em conjunto com o de Grupo de Trabalho. Se estiver marcado incluirá os sub-grupos do grupo selecionado no campo anterior. |
| **Tipo Item** | Recupera Ordens de Serviço que tenha um item associado do mesmo tipo informado neste campo. Se não for informado então este critério é desconsiderado. |
| **Solucionador** | Este parâmetro filtra os registros de acordo com Solucionador Responsável pela Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Periodicidade** | Este parâmetro determina a periodicidade que o gráfico de Evolução no Período deve apresentar o valor acumulado de Ordens de Serviço por Processo. |

Este relatório também está disponível na transação Workspace e é executado a partir da seleção de Ordens de Serviço.

No exemplo abaixo foi selecionado um conjunto reduzido de Ordens de Serviço para gerar o relatório:

Execução de relatórios a partir do Workspace

Além do filtro de recuperação informado pelo usuário existe também outro implícito por macroprocessos, que é aplicado em consultas por usuários que não possuem o perfil Administrador. Na figura abaixo podemos observar a mensagem exibida no rodapé da tela de relatórios quando o usuário não possui o perfil Administrador:

Alerta sobre filtro por macroprocessos

## Saídas

Após informar os parâmetros de recuperação clique no botão **Consultar** para visualizar o conteúdo do relatório. Serão apresentados dois relatórios.

O primeiro relatório exibe um gráfico que apresenta o percentual de Ordens de Serviço por Processo. Em seguida são apresentados gráficos e tabelas que detalham a quantidade de Ordens de Serviço para cada Processo.

Veja abaixo um exemplo de saída do primeiro relatório apresentado:

Ordens de Serviço por Processo

Detalhamento de Ordens de Serviço por Processo

O segundo relatório apresenta um gráfico para cada Processo com a evolução destas Ordens de Serviço no período marcado no parâmetro Periodicidade.

Veja abaixo um exemplo de saída do segundo relatório apresentado:

Evolução no Período
