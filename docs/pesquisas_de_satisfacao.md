# Pesquisas de Satisfação

Caminho: Guia para Administradores > Roteiro de implantação > Realizando cadastros > Cadastros Adicionais > Pesquisas de Satisfação

Uma Pesquisa de Satisfação é composta por um formulário enviado para Clientes após finalização de uma Ordem de Serviço. As respostas coletadas destas pesquisas podem ser utilizadas para construção de Indicadores de Desempenho - KPI's.

Para utilizarmos Pesquisas de Satisfação no Supravizio, devemos seguir basicamente os seguintes passos:

1. [Cadastrar Grupos de Questão](pesquisas_de_satisfacao)

2. [Cadastrar Questões de Pesquisa](pesquisas_de_satisfacao)

3. [Cadastrar Classes de Pesquisa de Satisfação](pesquisas_de_satisfacao)

## Cadastrar Grupos de Questão

O cadastro de Grupos de Questão é possível através do seguinte caminho **Processo | Processos | Pesquisa de Satisfação | Grupos de Questões**:

Caminho para acesso a tela

Para inserir um novo grupo, basta clicar em **Novo **na tela de listagem.

**Cadastro de Pesquisa**

Após preencher a Descrição do Grupo de Questões, clique na aba Escore Questão e preencha as opções de respostas disponíveis neste grupo.

**Dados de Pesquisa (Escores)**

## Cadastrar Questões de Pesquisa

O cadastro de Grupos de Questão está disponível do seguinte caminho **Processo | Processos | Pesquisa de Satisfação | Questões de Pesquisa.**

Para realizar um novo cadastro, basta clicar em **Novo** na tela de listagem:

Cadastro de Questões

Ao cadastrarmos uma Questão de Pesquisa, associamos com um Grupo de Questões:

Associação de Questão ao Grupo

## Cadastrar Classes de Pesquisa de Satisfação

O cadastro de Grupos de Questão está disponível do seguinte caminho **Processo | Processos | Pesquisa de Satisfação | Classes de Pesquisa de Satisfação.**

Para realizar um novo cadastro, basta clicar em **Novo** na tela de listagem:

Cadastro de Classe de Pesquisa de Satisfação

O campo **Ativo** da tela acima habilita o envio da pesquisa na finalização da Ordem de Serviço.

Associamos no cadastro da Classe de Pesquisa de Satisfação as Questões de Pesquisa necessárias:

Associação de Classe de Pesquisa de Satisfação com perguntas

## Associando Pesquisas de Satisfação em processos

Após criarmos nossas Classes de Pesquisa de Satisfação, é necessário modificarmos os processos através do [Editor de Processos](bpmn_eventos_finalizadores), indicando qual das classes desejamos gerar novas pesquisas. Isso é feito através da propriedade Pesquisa de Satisfação nos eventos finalizadores:

Finalizador com pesquisa de satisfação

Ao finalizar uma Ordem de Serviço será gerada (de acordo com o critério de percentual de envio) uma Pesquisa de Satisfação e enviado um comunicado ao favorecido (que por padrão é definido o cliente) para que responda no Portal de Processos:

Exemplo de Pesquisa de Satisfação no Portal

Após finalização, pode existir a necessidade de alteração do solicitante. Nesse caso a Ordem de Serviço deve ser reaberta e o Cliente deve ser alterado. Após isso uma nova pesquisa de satisfação será gerada e enviada ao novo avaliador enquanto a antiga será preservada.

Caso exista campo para preenchimento de Favorecido, pode ser seguido o mesmo processo acima porém ao invés de modificar o campo Cliente alteramos o campo Favorecido (A modificação do campo Cliente não acarretara no reenvio da pesquisa caso exista o campo Favorecido para preenchimento).

## Recebendo notificações de respostas de Pesquisas de Satisfação

É possível receber mensagens de notificação pelo Supravizio informando sobre respostas a Pesquisas de Satisfação.

Por padrão, o Supravizio possui dois **Tipos de Evento** relacionados a Pesquisa de Satisfação:

Tipos de eventos relacionados a Pesquisa de Satisfação

Para configurar o envio de notificações, é necessário cadastrar uma mensagem a ser enviada no respectivo Evento.

Caso tenha dúvidas de como configurá-la, visite o tópico [Envio de Mensagens em Eventos](envio_de_mensagens_em_eventos).

## Gestão da Pesquisa de Satisfação

A gestão da pesquisa de satisfação pode ser feita pelo uso dos relatórios [Analise de Pesquisa de Satisfação por Clientes](analise_pesquisa_satisfacao) e [Satisfação de Clientes por Solucionadores](satisfacao_de_clientes_por_sol).

Análise de respostas por Áreas clientes
