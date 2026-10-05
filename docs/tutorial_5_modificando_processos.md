# Modificar o Subprocesso

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 5: Sincronização de Cancelamentos > Modificar o Subprocesso

## Cancelar a Ordem de Serviço automaticamente após reprovação

Na versão anterior do subprocesso **Adquirir suprimentos** era necessário o preenchimento manual do campo de motivo de cancelamento. Veja na figura abaixo como era feito este preenchimento:

Fluxo para o estudo de caso

Preenchimento do motivo de cancelamento após reprovação

Nos próximos tópicos apresentaremos como configurar um fluxo de Processo para cancelar a Ordem de Serviço automaticamente após a reprovação:

### 1. Selecione o subprocesso Adquirir suprimentos utilizando um duplo clique no Process Explorer. Veja a figura abaixo:

Seleção do Subprocesso que será editado

### 2. Selecione o evento de cancelamento e atribua o valor True para a propriedade Preencher com motivos de reprovação:

Configuração do preenchimento automático do motivo de reprovação

## Sincronização de Cancelamentos entre Ordens de Serviços associadas

Outro problema clássico relativo a cancelamento é a sincronização entre Ordens de Serviço chamadoras e invocadas.

No nosso exemplo o que aconteceria com a Ordem de Serviço de Cadastrar Fornecedor se decidíssemos cancelar a aquisição do suprimento?

Neste tutorial vamos conhecer o recurso que permite sincronizar o cancelamento e a reabertura destas Ordens de Serviço.

### 1. Selecione o subprocesso Adquirir suprimentos utilizando um duplo clique no Process Explorer. Veja a figura abaixo:

Seleção do Subprocesso que será editado

### 2. Selecione o elemento Cadastrar Fornecedor e atribua o valor True para a propriedade Sincronizar cancelamento

Configuração do sincronismo de cancelamentos

Com a configuração acima durante a execução do subprocesso se o usuário cancelar uma Aquisição de suprimentos que já tenha gerado um Cadastramento de Fornecedor então esta segunda também será cancelada automaticamente. Se qualquer uma das duas for reaberta então a outra associada também será reaberta de forma automática.
