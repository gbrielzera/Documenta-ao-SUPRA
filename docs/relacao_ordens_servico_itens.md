# Relação de Ordens de Serviço X Itens de Configuração

Caminho: Relatórios > Relação de Ordens de Serviço X Itens de Configuração

O relatório de Relação de Ordens de Serviço X Itens de Configuração tem por objetivo apresentar uma listagem com dados das Ordens de Serviço de acordo com o Item de Configuração associado à estas ocorrências.

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
| **Tipo de Item** | Recupera Ordens de Serviço que tenha um item associado do mesmo tipo informado neste campo. Se não for informado então este critério é desconsiderado. |
| **Subprocessos** | Filtra registros de acordo com o Subprocesso associado com a classificação da Ordem de Serviço. Se não for informado então este critério é desconsiderado na recuperação. |
| **Agrupamento** | Filtra registro de acordo com os agrupamentos: Área\Cliente, Área\favorecido, Empresa\Cliente, Empresa\Favorecido. |
| **Exibir Aprovações** | Se esta opção for marcada será apresentada na saído do relatório a Aprovação do Gerente do Favorecido e a situação atual desta aprovação. |
| **Grupo de Trabalho** | Filtra registros cujo responsável corrente ou último responsável seja do grupo informado. Se não for informado então este critério é desconsiderado na recuperação. |
| **Inclui sub-grupos** | Este parâmetro é utilizado em conjunto com o de Grupo de Trabalho. Se estiver marcado incluirá os sub-grupos do grupo selecionado no campo anterior. |

## Saídas

Após informar os parâmetros de recuperação clique no botão **Consultar** para visualizar o conteúdo do relatório.

Na saída deste relatório é apresentada uma listagem agrupada de acordo com o valor selecionado no parâmetro de Agrupamento: Área\Cliente, Área\Favorecido, Empresa\Cliente, Empresa\Favorecido. Podemos observar que são exibidos dados de Ordens de Serviço que possuem itens de configuração associados.

Caso existam Ordens de Serviço com Aprovações são exibidas na listagem informações da última versão desta aprovação, é apresentado o responsável por estas aprovações e a atual situação da aprovação: Aprovada, Reprovada e Pendente. Caso deseje obter mais informações sobre Ordens de Serviço com pendências de Aprovação clique no link relatório de Pendência de Aprovações.

No exemplo abaixo foi selecionado Área\Cliente no valor do parâmetro Agrupamento. Na listagem será apresentado os dados das Ordens de Serviço agrupado por Orgão do Cliente e o Cliente da ocorrência:

Saída apresentada no relatório agrupado por Área\Cliente

Neste outro exemplo apresentamos a saída do relatório agrupada por Empresa\Favorecido:

Saída apresentada no relatório agrupado por Empresa\Favorecido
