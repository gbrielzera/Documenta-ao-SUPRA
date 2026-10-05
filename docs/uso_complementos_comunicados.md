# Uso de Complementos em Comunicados

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 11: Envio de Comunicados > Uso de Complementos em Comunicados

Quando um modelo de comunicado é configurado, é possível que se use 5 campos ‘Complemento’ na mensagem, afim de tornar o modelo mais flexível para que possa ser usado em diferentes tipos de mensagens, por exemplo:

Novo modelo de comunicado usando um campo de complemento

Logo após o modelo de comunicado ser criado, é possível customizar o conteúdo do complemento a partir da propriedade Script Evento em cada subprocesso no editor de processos, ou em eventos por mensagem:

Configuração do evento intermediário por mensagem

No editor de scripts, você poderá selecionar o complemento através da árvore do lado direito da tela, na opção Mensagem. Em seguida, poderá incluir um texto que substituirá o complemento no modelo de comunicado:

Script usando o complemento

Mensagem gerada a partir do modelo de comunicado com o complemento configurado no evento de mensagem

Configuração de mensagem em evento de abertura de Ordem de Serviço usando o mesmo modelo de comunicado

Mensagem gerada a partir do evento de abertura de Ordem de Serviço

Obs.: O texto atribuído nos campos de complemento a partir de um evento intermediário por mensagem só valerão para o mesmo. Caso outro evento de mensagem utilize o mesmo modelo de comunicado, os campos de complemento presentes neste deverão ser alterados, tornando assim, possível usar textos diferentes em um mesmo modelo de comunicado.
