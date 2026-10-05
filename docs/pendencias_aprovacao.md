# Pendências de aprovação

Caminho: Relatórios > Pendências de aprovação

O relatório de Pendências de Aprovação tem por objetivo apresentar um resumo quantitativo das Ordens de Serviços que foram submetidas à aprovação e estão pendentes. Com este relatório é possível analisar o desempenho dos aprovadores de Ordens de Serviço com base nas pendências apresentadas.

## Parâmetros

Na figura abaixo podemos observar a tela de parâmetros para este relatório:

Parâmetros do relatório

| **Serviço** | Filtra registros pelo valor informado no campo Serviço da Ordem de Serviço que foi submetida à aprovação. Se não for informado então este critério é desconsiderado na recuperação. |
|---|---|
| **Subprocesso** | Filtra registros de acordo com o Subprocesso associado com a classificação da Ordem de Serviço que foi submetida à aprovação. Se não for informado então este critério é desconsiderado na recuperação. |
| **Área Cliente** | Filtra os registros de acordo com o Área Cliente cujo valor é informado no campo Cliente da Ordem de Serviço . Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui Sub-áreas** | Este parâmetro é utilizado em conjunto com o de Área Cliente. Se este parâmetro estiver marcado incluirá o Sub-orgão do Orgão Cliente selecionado no campo anterior. |
| **Processo** | Filtra registros pelo Processo associado com a classificação da Ordem de Serviço que foi submetida à aprovação. Se não for informado então este critério é desconsiderado na recuperação. |
| **Tipo Item** | Recupera Ordens de Serviço submetidas à aprovação, que tenham um item associado do mesmo tipo informado neste campo. Se não for informado então este critério é desconsiderado. |
| **Solucionador** | Este parâmetro filtra os registros de acordo com Solucionador Responsável pela Ordem de Serviço que foi encaminhada para aprovação. Se não for informado então este critério é desconsiderado na recuperação. |

Este relatório também está disponível na transação Workspace e é executado a partir da seleção de Ordens de Serviço.

No exemplo abaixo foi selecionado um conjunto reduzido de Ordens de Serviço para gerar o relatório:

Execução de relatórios a partir do Workspace

## Saídas

Após informar os parâmetros de recuperação clique no botão **Consultar** para visualizar o conteúdo do relatório. Serão apresentados dois relatórios.

O primeiro relatório exibe um gráfico com a quantidade de pendências por aprovadores. Em seguida são apresentados os dados relativos a cada aprovador com pendência.

Veja abaixo um exemplo de saída do primeiro relatório apresentado:

Pendências de Aprovação

Utilizando duplo clique no Aprovador ou no substituto é possível visualizar detalhes sobre o Histórico de Aprovações do Aprovador ou Substituto:

Histórico de Aprovações

O segundo relatório apresenta a relação de Ordens de Serviço com pendências de aprovação. São apresentados alguns dados das Ordens de Serviço como o número, o assunto, o subprocesso no qual foi classificada, a referência, o serviço e o cliente.

Veja abaixo um exemplo de saída do segundo relatório apresentado:

Relação de Ordens de Serviço com pendência de aprovação

É possível abrir através deste segundo relatório a tela de Edição de Ordens de Serviço, para isso realize um duplo clique no Número da Ordem de Serviço apresentado no relatório:

Visualizando a tela de Edição de Ordem de Serviço através do relatório de Pendência de Aprovação
