# Cancelamento de Ordem de Serviço

Caminho: Guia para Solucionadores > Workspace  > Workspace Ordens de Serviço > Cancelamento de Ordem de Serviço

Em diversos casos pode ser necessário o cancelamento de certa Ordem de Serviço, tal ação pode ser realizada de três formas diferentes.

## Cancelamento por tela de Edição de Ordem de Serviço

Pela própria tela de edição de Ordem de Serviço é possível realizar o cancelamento pois nela há um botão "Cancelar":

Cancelar Ordem de Serviço pela tela de Edição

Caso deseje cancelar a Ordem de serviço o seguinte diálogo será exibido para preenchimento do motivo do cancelamento:

Motivo do cancelamento

IMPORTANTE: O usuário poderá cancelar somente se possuir permissão para alterar os dados da Ordem de Serviço, caso contrário o botão de cancelamento aparecerá desabilitado.

## Cancelamento pelo Workspace

O cancelamento pelo Workspace é uma importante ferramenta, principalmente se for necessário o cancelamento de múltiplas Ordens de Serviço. Selecione no grid do Workspace as Ordens de Serviço desejadas e clique com o botão direito para visualizar a opção de cancelamento :

Workspace

Após é exibida uma mensagem de confirmação para o cancelamento:

Cancelamento de Múltiplas Ordens de Serviço

## Cancelamento pelo Portal de Processos

É possível também o cancelamento de uma Ordem de Serviço pelo Portal, porém é necessário que o evento esteja configurado no processo para permitir o cancelamento pelo cliente no Portal. No editor de processos, utilizando o exemplo de Solicitação de viagens:

Edição do Processo

Salve as alterações do processo para que seja possível o cancelamento pelo cliente no Portal de Processos.

IMPORTANTE: No exemplo acima foi permitido o cancelamento pelo Portal apenas no evento de Solicitar aprovação do gerente do solicitante. No exemplo, na atividade "Reservar voo e hotel" já não é mais possível o cancelamento pelo Portal:

Tarefa seguinte não permite cancelamento

Com essas configurações é possível visualizar o botão de cancelamento no Portal:

Cancelamento pelo Portal

## Configurar envio de mensagem ao ocorrer cancelamento

É possível configurar envio de mensagem ao ocorrer o cancelamento de uma Ordem de Serviço. Em Tipos de Eventos (Processo | Processos | Tipos de Eventos) filtre pelo evento de cancelamento:

Tipos de Eventos - Cancelamento

Com duplo clique ou clicando em Modificar, uma nova tela é exibida. Nessa tela é possível visualizar a aba "Mensagens":

Dados Principais

Na aba Mensagens clique em "Novo" e então defina o campo Descrição, escolha um Modelo de comunicado, defina os Destinatários, e determine o Processo alvo (a temporalidade também pode ser definida, porém é opcional):

Nova Mensagem em Evento

Salve as modificações e então ao cancelar uma Ordem de Serviço (No modelo apenas para Viagens) automaticamente é enviada uma mensagem (No exemplo com modelo de Aviso sobre cancelamento e para o Gerente do Favorecido).

## Reabertura de Ordens de Serviço Canceladas

É possível reabrir uma Ordem de Serviço cancelada pelo Workspace (Edição de Ordem de Serviço):

Reabertura pela Edição de Ordem de Serviço

E também pelo Portal:

Reabertura pela edição de Ordem de Serviço

Há certas condições para que a Ordem de Serviço possa ser reaberta:

- Estar dentro do prazo parametrizado na tela de configurações (prazo em dias corridos);
- O Subprocesso deve permitir a reabertura via Portal (Para o caso do Portal de Processos)
- A Ordem de Serviço não pode ter sido por um link inicial (chamada por outro processo)
- O usuário logado no Portal deve ser o próprio Cliente da Ordem de Serviço

Para configurar as condições entre em Tipos de Subprocessos (Processo | Processos | Tipos de Subprocessos), selecione o processo desejado e verifique a existência da aba "Autoatendimento":

Tipos de Subprocessos

Na aba "Autoatendimento" é possível configurar a Permissão de Reabertura":

Configurações do Autoatendimento

E verifique em Utilitários | Configurações, na aba de Autoatendimento (dentro de Processo). Nessa tela é possível definir o máximo de dias para reabertura:

Configurações do Autoatendimento

## Consultar Ordens de Serviço Canceladas

Para consultar Ordens de serviço canceladas modifique o filtro de Ordens de Serviço de "Abertas" para "Canceladas", será necessário definir o período da consulta:

Filtro por Cancelamento

A partir das configurações do filtro, as Ordens de Serviço Canceladas estarão disponíveis para consulta:

Ordens de Serviço Canceladas

## Sincronizar Cancelamentos

A sincronia de Cancelamentos é utilizada em processos que possuem o Elemento de BPMN de Subprocesso, pois a sincronia define se quando uma Ordem de Serviço for cancelada, as associadas também são canceladas. No editor de processos, no chamador do Subprocesso deve ser configurada a propriedade de "Sincronizar Cancelamento" como "True":

Configuração do Subprocesso

É necessário também preencher o campo "Associação". Nesse campo Defina o "Subprocesso invocado", uma "Frase de Associação" e uma "Frase Inversa". É possível definir também uma cardinalidade entre o fonte e o alvo:

Criação de Associação

Sincronizando o cancelamento, ocorre o seguinte: Abrindo uma nova Ordem de Serviço de Subprocesso A, ela chama uma de Subprocesso B. Se uma das duas Ordens de Serviço for cancelada, ambas são canceladas.

Verifique que ao cancelar na Ordem de Serviço do Subprocesso B, o Subprocesso A recebe um aviso:

Aviso de Cancelamento de B na Ordem de Serviço A
