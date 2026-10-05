# Comunicados em Ordens de Serviço

Caminho: Guia para Solucionadores > Workspace  > Workspace Ordens de Serviço > Comunicados em Ordens de Serviço

O recurso de comunicados do Supravizio permite o fácil acesso as mensagens enviadas e relacionadas com uma Ordem de Serviço, sejam elas mensagens automáticas configuradas no processo ou mesmo aquelas editadas e enviadas manualmente por solucionadores envolvidos no atendimento.

Na figura abaixo podemos visualizar a aba Comunicados que contém todas as funcionalidades que descreveremos neste tópico.

Repare que além do acesso as mensagens do processo podemos editar e enviar um comunicado por esta tela. O destinatário receberá um e-mail na sua ferramenta de correio eletrônico e respondendo a mensagem uma cópia será arquivada no banco de dados do Supravizio. Desta forma toda comunicação realizada entre solucionadores, clientes e demais envolvidos fica arquivada e acessível na tela de Ordem de Serviço.

Armazenamento de comunicados

Na figura abaixo podemos observar que quando um destinatário recebe uma mensagem e decide responde-la o endereço é preenchido com uma conta de e-mail de sistema. Esta conta e o assunto não podem ser modificadas pois serão utilizadas pelo Supravizio para identificar a Ordem de Serviço que originou a mensagem.

Recebimento e respostas de mensagens

## Enviando um comunicado

Para enviar um novo comunicado siga os seguinte passos:

| 1. | Edite o corpo do e-mail conforme a figura abaixo. Repare que este editor pode ser inicializado com uma assinatura padrão. Veja [Configurando uma assinatura padrão](configurando_assinaturas). |
|---|---|

Edição do corpo do e-mail

| 2. | Informe um ou mais destinatários para a mensagem. Os destinatários devem ser separados por ponto e vírgula e a edição é livre. O link **Incluir Cliente** adiciona o e-mail do cliente da Ordem de Serviço. |
|---|---|

Destinatário da mensagem

| 3. | Verifique a configuração de seleção de destinatários (Caso seja marcada será enviada uma mensagem para cada destinatário, senão apenas uma mensagem para todos destinatários): |
|---|---|

Configuração envio de mensagem

| 4. | Confirme o preenchimento do Assunto: |
|---|---|

Campo assunto da mensagem

| 5. | Utilize arquivos anexados na Ordem de Serviço como anexos do comunicado. |
|---|---|

Anexos da mensagem

| 6. | Clique no botão Enviar |
|---|---|

Botão de envio

## Envio de cópia em comunicado manual

Os subprocessos podem ter cadastrado um campo chamado "Emails para cópia em comunicado manual".

No menu **Processo | Processos | Tipos de Subprocessos**:

Tipos de Subprocessos

Editando um subprocesso (ou adicionando um novo), por exemplo o de Incidente, é possível visualizar o campo "Emails para cópia em comunicado manual":

Edição de tipo de serviço

Se por exemplo for adicionado para E-mail para cópia "incidentes@empresa.com.br" ao abrir a aba de comunicados de uma OS ocorre o seguinte:

Comunicados com e-mail de cópia definido

Repare que automaticamente o e-mail é adicionado em um campo de destinatários e que esta parte do campo não pode ser modificada.

## Redefinição de remetente

Caso haja uma redefinição configurada no cadastro do [Tipo de Subprocesso](classesubprocesso_sub), ao enviar um comunicado, o nome e/ou e-mail do remetente será exibido conforme configurado. Veja no exemplo abaixo, onde inserimos parâmetro de nome e e-mail do remetente dos comunicados:

### Redefinição de remetentes de comunicados

Após, enviamos um comunicado com o usuário João Silva em uma Ordem de Serviço deste Tipo de Subprocesso:

Aba de comunicados

Assim quando recebemos este comunicado, o remetente será definido conforme inserido no parâmetro do cadastro.

Remetente da mensagem
