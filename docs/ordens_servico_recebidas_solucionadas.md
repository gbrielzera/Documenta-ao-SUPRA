# Ordens de Serviço Recebidas X Solucionadas

Caminho: Relatórios > Ordens de Serviço Recebidas X Solucionadas

O relatório de Ordens de Serviço Recebidas X Solucionadas tem por objetivo apresentar um resumo quantitativo de Ordens de Serviço recebidas por solucionador e a situação destas Ordens de Serviço. Através deste relatório é possível analisar o desempenho de solucionadores de acordo com a quantidade de Ordem de Serviço solucionadas dentro ou fora do prazo acordado e através da quantidade de ocorrências sem solução ou canceladas.

## Parâmetros

Na figura abaixo podemos observar a tela de parâmetros para este relatório:

Parâmetros do relatório

| **Data Início** | Data de início para recuperação das Ordens de Serviço. Este parâmetro recupera as Ordens de serviço cuja data de referência seja maior ou igual ao valor informado. |
|---|---|
| **Data Fim** | Data limite fim para recuperação das Ordens de Serviço. Este parâmetro recupera as Ordens de serviço cuja data de referência seja menor ou igual ao valor informado. |
| **Área Cliente** | Filtra os registros de acordo com o Área Cliente com o valor informado no campo Cliente da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui sub-áreas** | Este parâmetro é utilizado em conjunto com o de Área Cliente. Se este parâmetro estiver marcado incluirá o Sub-orgão do Orgão Cliente selecionado no campo anterior. |
| **Grupo de Trabalho** | Filtra registros cujo responsável corrente ou último responsável seja do grupo informado. Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui sub-Grupos** | Este parâmetro é utilizado em conjunto com o de Grupo de Trabalho. Se estiver marcado incluirá os sub-grupos do grupo selecionado no campo anterior. |
| **Serviço** | Filtra registros pelo valor informado no campo Serviço da ocorrência. Se não for informado então este critério é desconsiderado na recuperação. |
| **Tipo de Subprocessos** | Filtra registros de acordo com o Subprocesso associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Processo** | Filtra registros pelo Processo associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Tipo de Item** | Recupera Ordens de Serviço que tenha um item associado do mesmo tipo informado neste campo. Se não for informado então este critério é desconsiderado. |
| **Solucionador** | Este parâmetro filtra os registros de acordo com Solucionador Responsável pela Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |

## Saídas

Após informar os parâmetros de recuperação clique no botão **Consultar** para visualizar o conteúdo do relatório.

Na saída deste relatório é apresentado um gráfico que quantifica as Ordens de Serviço que foram recebidas por um determinado solucionador de acordo a situação destas Ordens de Serviço: Finalizadas, Canceladas e Não solucionadas.

As Ordens de Serviço Finalizadas são aquelas que o solucionador recebeu em sua fila e finalizou seu atendimento, as Ordens de Serviço Canceladas são aquelas recebidas pelo solucionador e canceladas e as Não solucionadas são aquelas que ainda estão abertas na fila do solucionador ou que foram encaminhadas para outra pessoa sem solução.

Gráfico apresentado na saída do relatório de Ordens de Serviço Recebidas X Solucionadas

É apresentada também uma listagem quantitativa de Ordens de serviço relacionando o solucionador com a situação das Ordens de Serviço recebidas por ele. Cada situação apresentada na listagem, é explicada logo abaixo:

Listagem apresentado o responsável e a situação das Ordens de Serviço
