# Ordens de Serviço Associadas

Caminho: Guia para Solucionadores > Workspace  > Workspace Ordens de Serviço > Ordens de Serviço Associadas

Uma Ordem de Serviço pode estabelecer um relacionamento com outras Ordens de Serviço através de [Associações](associacao_sub). Estas Associações permitem estabelecer um relacionamento entre dois [Tipos de Subprocessos](classesubprocesso_sub) ativos. Todas as Ordens de Serviço que estão associadas à Ordem de Serviço em edição estão listadas nesta aba:

Edição de Ordem de Serviço - Ordens de Serviço Associadas

A listagem de Ordens de Serviço exibida nesta aba possui basicamente as mesmas funcionalidades e relatórios disponíveis na listagem de Ordens de Serviço do [Workspace](workspace_ordemservico). É possível realizar ações ([Encaminhar](enviar_os_solucionador), [Clonar](clonar_ordem_servico), [Classificar](classificacao_os), [Cancelar](cancelamento_de_ordem_de_servi), [Categorizar](workspace_categorizar), [exibir relatórios](impressao_da_ordem_de_servico), entre outras) levando em consideração Ordens de Serviço selecionadas na listagem é possível também [utilizar filtros](acessar_ordemservico) na listagem de Ordens de Serviço.

Observe na figura acima que a Ordem de Serviço em edição possui 4 Ordens de Serviço associadas. Vejamos detalhadamente a origem destas associações.

### Abertura de Ordens de Serviço associadas

Esta aba é possível também realizar a abertura de novas Ordens de Serviço que possuam um [Link Inicial](iniciador_link_inicial) com uma Associação que possua o mesmo Tipo de Subprocesso fonte da Ordem de Serviço em edição.

Observe o fluxo de processo abaixo, do tipo de subprocesso "Tarefa de projeto":

Subprocesso Tarefa de projeto

Repare que o fluxo possui um iniciador do tipo Link Inicial. Este iniciador possui uma associação com o fluxo de processo do tipo "Gerenciamento de Projeto":

Link Inicial em Tarefa de projeto

A associação em questão possui o seguinte cadastro:

Associação Tarefas do projeto - Projeto que gerou a tarefa

Repare que no fluxo de processo de Gerenciamento de Projetos não existem elemento chamadores ([Link Final](bpmn_eventos_finalizadores) e [Subprocesso](subprocessos)):

Subprocesso Gerenciamento de Projetos

Repare que na barra de ferramentas da aba de Ordens de Serviço associadas, visualizando uma Ordem de Serviço do tipo Gerenciamento de Projetos, encontramos um comando para criação de nova Ordem de Serviço de Tarefa de Projeto:

Ordens de Serviço associadas

Isso se dá ao fato de o iniciador Link Inicial do subprocesso de Tarefa de projeto possibilitar a abertura através do Workspace, ao invés de abertura por chamadores de processo (Links Finais e Subprocessos):

Link Inicial com Tipo de Abertura Workspace

Isso permite que a qualquer momento possamos abrir novas Ordens de Serviço do tipo Tarefa de projeto em uma Ordem de Serviço do tipo Gerenciamento de Projetos. Deve ser levada em consideração também o critério de Cardinalidade Alvo da Associação. Repare no cadastro da Associação que ela possui a Cardinalidade Alvo configurada para Vários:

Cardinalidade Alvo da Associação

Aviso sobre remoção de Associação

Também é possível a remoção da Ordem de Serviço que já possua a associação, selecionando-a na listagem de Ordens de Serviço associadas e clicando no botão "Remover Associação":

Remoção de Associações entre Ordens de Serviço

Logo, a associação entre a Ordem de Serviço de Gerenciamento de Projetos e a de Tarefa de projeto perderão vínculo, porém a Ordem de Serviço com associação Removida não é cancelada nem removida:

Lista de Ordens de Serviço abertas com Ordem de Serviço Tarefa de projeto sem associação

Associação Manual

Há a possibilidade também de realizar uma associação de um Ordem de Serviço manualmente, caso haja necessidade.

Por exemplo, um processo que possui uma associação com outro processo, mas para ser associada a uma Ordem de Serviço desse processo, o fluxo deve seguir um caminho que é desviado por um gateway. Evidentemente, em alguns o fluxo não seguirão para a abertura do processo, e também haver a necessidade de abrirmos uma OS daquele processo.

Para isso, basta acessar na tela de Ordem de Serviço a aba "Ordens de Serviço Associadas" e encontraremos um botão na barra superior chamado "Associar Existente", que listará todas as associações possíveis daquele tipo de subprocesso:

Associar existentes

Clicando numa opção, será apresentada uma tela para realizar a busca da Ordem de Serviço que possui a associação:

Procura Ordem de Serviço

Basta então, selecionar com um duplo clique a Ordem de Serviço desejada.
