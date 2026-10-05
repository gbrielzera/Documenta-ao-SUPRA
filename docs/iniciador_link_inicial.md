# Link Inicial

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Eventos Iniciadores > Link Inicial

Um Link Inicial permite a interface entre um subprocesso chamador (fonte) e um subprocesso invocado (alvo).

Início de um fluxo a partir de outro

Para que isso seja possível, um Link Inicial conta com uma ou mais Associações:

Associações em um Link Inicial

Uma Associação permite estabelecer um relacionamento entre duas Ordens de Serviço sendo uma chamadora (fonte) e uma invocada (alvo). Além de indicar uma associação entre Ordens de Serviço, é possível também indicar a cardinalidade do relacionamento:

Associação entre Mudança e Especificação

Para mais informações sobre o cadastro de uma nova Associação leia [Associações](associacao_sub).

Um Link Inicial permite o relacionamento com mais de um tipo de Associação. Em um fluxo de processo, uma Associação só poderá pertencer a um único Link Inicial:

Múltiplas associações em um Link Inicial

Existem basicamente duas formas de invocarmos um iniciador do tipo Link Inicial: Através de elementos do tipo [Link Final](bpmn_eventos_finalizadores) ou [Subprocesso](subprocessos), ou pelo Workspace abrindo diretamente pela tela de Edição de Ordem de Serviço na aba Ordens de Serviço associadas. Inicialmente, devemos determinar no Link Inicial o Tipo de Abertura. Esta propriedade permite determinar a forma de abertura desejada:

Tipos de Abertura em um Link Inicial

### Abertura por Subprocesso ou Link Final

Para que uma Ordem de Serviço seja aberta através de um Link Inicial a partir de um elemento Link Final ou Subprocesso, é necessário nesses dois últimos existir a uma Associação cadastrada que esteja contida no Link Inicial.

Observe o exemplo abaixo. Temos um subprocesso de Mudança que possui um elemento Subprocesso que ira criar nova uma Ordem de Serviço do tipo de subprocesso Especificação (ou simplesmente associará uma do mesmo tipo existente). Veja que o elemento Subprocesso do fluxo de Mudança possui a mesma Associação (usando a frase da Associação) contida no Link Inicial (que utiliza a frase inversa da Associação):

Associação entre um elemento Subprocesso e um Link Inicial

Da mesma forma que relacionamos a associação entre um elemento Subprocesso e um Link Inicial, podemos realizar a associação entre um elemento Link Final e um Link Inicial:

Associação entre um elemento Link Final e um Link Inicial

### Abertura por Workspace

Uma outra forma de configurar a abertura de uma Ordem de Serviço através de Links Iniciais é a invocação diretamente através da Ordem de Serviço. Para isso, é necessário configurarmos no Link Inicial o Tipo de Abertura Workspace:

Link Inicial com Tipo de Abertura por Workspace

Repare que ao alterar o valor da propriedade para "Workspace" o elemento recebe um novo ícone de Ordem de Serviço:

Elemento Link Inicial com abertura por Workspace

Links Iniciais não necessitam de elementos chamadores Link Final e Subprocesso, como no subtítulo anterior. A qualquer momento podemos abrir uma nova Ordem de Serviço invocada através da tela de Edição de Ordem de Serviço de uma Ordem de Serviço que seja do tipo do chamador da Associação do LInk Inicial:

Repare na Ordem de Serviço abaixo, do tipo "Projeto":

Ordem de Serviço de Projeto

Selecionando a aba [Ordens de Serviço associadas](workspace_os_associada), será exibida a listagem de Ordens de Serviço relacionadas com a Ordem de Serviço em Edição. Além disso, o solucionador contará com um comando de "Nova" para que possa criar a qualquer momento Ordens de Serviço que possuam associações com o subprocesso da Ordem de Serviço em edição:

Ordens de Serviço associadas

Em nosso exemplo, utilizamos uma Associação do tipo um para vários, ou seja, uma Ordem de Serviço do tipo Projeto poderá criar várias Ordens de Serviço do tipo Tarefa de Projeto. Porém, caso a associação seja do tipo um para um, então é exibida uma mensagem caso o solucionador tente criar uma nova Ordem de Serviço associada baseada em uma associação que já possua relacionamento:

Mensagem exibida sobre cardinalidade
