# Eventos Finalizadores

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Eventos Finalizadores

Um evento **finalizador** indica o fim de um fluxo de processo. Os tipos de eventos finalizadores são:

## Finalizador

Indica o fim de um fluxo com sucesso. Em um **Finalizador com Sucesso** podemos, por exemplo, enviar uma [Pesquisa de Satisfação](pesquisa_sub) ao Cliente da ocorrência daquele fluxo de processo, através da propriedade Pesquisa Satisfação:

Assim como as demais atividades, o **Finalizador com Sucesso** permite também a inclusão de operações, como por exemplo algum tipo de entrada de dados.

## Finalizador por Cancelamento

Utilizado para finalização em situações que exigem cancelamento da ocorrência como, por exemplo, após a reprovação de uma aprovação.

Neste caso, é obrigatório o preenchimento do campo Motivo de Cancelamento:

## Link Final

O Link Final permite que uma Ordem de Serviço seja finalizada e em seguida possa ser gerada uma nova Ordem de Serviço associada.

Link Final

A principal propriedade de um Link Final é a Associação. Uma Associação permite o relacionamento entre tipos de subprocessos diferentes (ou ao mesmo tipo de subprocesso):

Associação em um Link Final

Para mais informações sobre Associações leia o tópico [Associações](associacao_sub).

Utilizaremos a seguinte Associação no exemplo à seguir:

Associação Liberação da Mudança - Mudanças da Liberação

Em um fluxo de processo do tipo Mudança, vamos inserir um Link Final e na propriedade Associação vamos selecionar a associação "Liberação da Mudança":

Associação em um Link Final

Agora, em um desenho de fluxo do tipo Liberação, vamos incluir um Link Inicial (mais informações leia Link Inicial) com uma associação "Mudança da Liberação" (frase inversa da Associação):

Associação em um Link Inicial

Ao finalizarmos uma Ordem de Serviço do tipo "Mudança", será exibido um comando para a criação de uma nova Ordem de Serviço associada ou simplesmente associar uma Ordem de Serviço existente:

Ordem de Serviço de Mudança

Ao clicar no botão "Novo(a) Liberação", é exibida uma janela para indicarmos como iremos realizar a associação:

Janela de Associação

Em nosso exemplo, vamos clicar em "Iniciar uma nova Ordem de Serviço.

Veja que a nova Ordem de Serviço já é aberta referenciando o seu subprocesso chamador:

Ordem de Serviço de Liberação gerada por Mudança

### Passagem de Parâmetros

É possível também efetuar a passagem de parâmetros, tanto dados de campos da Ordem de Serviço, quanto seus Itens de Configuração, procedendo da mesma forma como no elemento Subprocesso. Para mais informações sobre passagens de parâmetros entre Ordens de Serviço leia [Subprocessos](subprocessos).

Associação Manual

Se houver necessidade, pode-se realizar a associação de uma Ordem de Serviço manualmente. Para mais informações veja o tópico: [Associação Manual](workspace_os_associada).
