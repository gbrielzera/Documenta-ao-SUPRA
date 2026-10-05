# Reclassificação de Ordens de Serviço

Caminho: Relatórios > Reclassificação de Ordens de Serviço

O relatório de Reclassificação de Ordens de Serviço tem por objetivo apresentar um resumo quantitativo das Ordens de Serviços que tiveram seu processo associado reclassificado. Com este relatório é possível identificar o número de Ordens de Serviço que foram reclassificadas.

## Parâmetros

Na figura abaixo podemos observar a tela de parâmetros para este relatório:

Parâmetros do relatório

| Tipo Filtro | Este parâmetro está relacionado com a **Data início** e **Data fim** de recuperação e possui as seguintes opções: - **Abertas em**: recupera Ordens de Serviços abertas entre a data início e data fim, não importando a situação corrente do registro. - **Abertas e não solucionadas em**: recupera Ordens de Serviço abertas entra a data de início e data fim e que não foram finalizadas até o momento. Importante: a situação Cancelada é considerada uma finalização e portanto registros nesta situação não serão recuperados. - **Finalizadas em**: recupera Ordens de Serviço finalizadas entre a data início e data fim. Ordens de Serviço canceladas são desconsideradas nesta opção. - **Canceladas em**: recupera Ordens de Serviço canceladas entre a data início e data fim, considerando para isto a data/hora do último cancelamento para o registro. Também são consideradas canceladas as ocorrências com finalização do tipo "Não- realizada". - **Reabertas em**: recupera Ordens de Serviço reabertas entre a data início e data fim. São consideradas todos os eventos de reabertura, ou seja, uma Ordem de Serviço pode constar em diversos períodos consultados. |
|---|---|
| **Data Início** | Data de início para recuperação. Este parâmetro é utilizado em conjunto com o tipo de filtro e recupera os registros cuja data de referência seja maior ou igual ao valor informado. |
| **Data Fim** | Data limite fim para recuperação. Este parâmetro é utilizado em conjunto com o tipo de filtro e recupera os registros cuja data de referência seja menor ou igual ao valor informado. |
| **Área Cliente** | Filtra os registros de acordo com o Área cujo valor é informado no campo Cliente da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui sub-áreas** | Este parâmetro é utilizado em conjunto com o de Área. Se este parâmetro estiver marcado incluirá o Sub-orgão do Orgão selecionado no campo anterior. |
| **Serviço** | Filtra registros pelo valor informado no campo Serviço da ocorrência. Se não for informado então este critério é desconsiderado na recuperação. |
| **Subprocesso** | Filtra registros de acordo com o Subprocesso associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Somente Violação ANS** | Se este parâmetro estiver marcado filtra somente Ordens de Serviço reclassificadas que tiveram o ANS violado. |
| **Somente aval. negativas** | Se este parâmetro estiver marcado filtra somente Ordens de Serviço reclassificadas que tiveram avaliações negativas. |
| **Tipo Item Configuração** | Recupera Ordens de Serviço que tenha um item associado do mesmo tipo informado neste campo. Se não for informado então este critério é desconsiderado. |
| **Item Configuração** | Recupera Ordens de Serviço que tenha o item associado informado neste campo. Se não for informado então este critério é desconsiderado. |
| **Solucionador Responsável** | Este parâmetro filtra os registros de acordo com Solucionador Responsável pela Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |

Este relatório também está disponível na transação Workspace e é executado a partir da seleção de Ordens de Serviço.

No exemplo abaixo foi selecionado um conjunto reduzido de Ordens de Serviço para gerar o relatório:

Execução de relatórios a partir do Workspace

## Saídas

Após informar os parâmetros de recuperação, clique no botão **Consultar** para visualizar o conteúdo do relatório. O relatório de Reclassificação de Ordens de Serviço exibe vários gráficos.

Veja abaixo um exemplo de saída para este relatório:

Gráficos apresentados na saída do relatório de Reclassificação de Ordens de Serviço

Podemos visualizar no exemplo acima os seguintes gráficos:

| TOP 10 Órgãos Clientes | Este gráfico apresenta o percentual Ordens de Serviço reclassificadas de acordo com o Orgão Cliente. O gráfico refere-se a classificação final da Ordem de Serviço. |
|---|---|
| **TOP 10 Subprocessos** | Este gráfico apresenta o percentual de Ordens de Serviço de acordo com o Subprocesso. O gráfico refere-se a classificação final da Ordem de Serviço. |
| **TOP 10 Re classificações** | Este gráfico apresenta o percentual Ordens de Serviço reclassificadas de acordo com suas novas classificações. |

Em seguida são é apresentado a relação de Ordens de Serviço reclassificadas e alguns dados destas Ordens de Serviço:

Relação de Ordens de Serviço reclassificadas

É possível abrir através deste segundo relatório a tela de Edição de Ordens de Serviço, para isso realize um duplo clique no Número da Ordem de Serviço apresentado no relatório:

Visualizando a tela de Edição de Ordem de Serviço através do relatório
