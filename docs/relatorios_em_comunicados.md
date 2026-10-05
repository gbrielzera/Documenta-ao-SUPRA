# Relatórios em Comunicados

Caminho: Guia para Administradores > Editor de Relatórios > Publicando Relatórios > Relatórios em Comunicados

Este tópico tem por finalidade instruir sobre a configuração de publicação de relatórios em envios de comunicados em um fluxo de processo.

Em alguns casos necessitamos do uso de comunicados em um fluxo de processo para notificação de pessoas envolvidas em um processo levando em consideração o seu papel no processo. Para permitirmos que essas notificações sejam enviadas, utilizamos um [Evento Intermediário por Mensagem](bpmn_eventos_intermediarios).

Para que esta configurações seja possível, na propriedade "Relatórios que serão anexados" devemos indicar qual relatório será extraído e quais os valores de eventuais parâmetros que serão utilizados na consulta.

Clicando no símbolo (...) selecione o relatório necessário, indicando a lista de parâmetros exigidos.

Podemos indicar ainda quais valores poderão ser passados como parâmetros para o relatório. No exemplo acima, selecionamos um relatório que enviará uma lista de softwares para licenciamento. Vamos fornecer como parâmetro do relatório o número identificador da Ordem de Serviço. Para isso, expandindo a propriedade parâmetros, observe que após selecionarmos o relatório, a lista de parâmetros é preenchida automaticamente:

Observe que o parâmetro pertence à lista de parâmetros no cadastro do relatório:

Neste caso, é necessário fornecermos o valor que será repassado. Para isso, na aba de propriedades, expanda o parâmetro desejado e na propriedade Valor clique no símbolo (...).

Ao exibir o diálogo de edição de script, indique o valor desejado:

Todas as vezes em que o evento é iniciado, o relatório é processado e enviado para os destinatários como anexo do e-mail:

**Observação:** Em alguns casos, pode ser necessário enviar mensagens independentes para cada destinatário, incluindo relatórios com informações individuais para cada um. Para isso, podemos utilizar o parâmetro **DestinatarioMensagem**.

Ao incluir o relatório em um [Evento Intermediário de Mensagens](bpmn_eventos_intermediarios) e utilizarmos este parâmetro, será retornado o e-mail do destinatário da mensagem a ser enviada.
