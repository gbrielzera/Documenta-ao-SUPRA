# Configuração de Email

Caminho: Guia para Administradores > Configurações do Sistema > Configuração de Email

Este tópico tem como objetivo explicar como configurar a caixa de e-mail para envio e recebimento de comunicados.

**Importante**: Para utilização do recurso é necessário uma caixa de e-mail para o Supravizio com acesso SMTP, e preferencialmente também com acesso POP3 ou IMAP4.

Para configurar a caixa de e-mail acesse o menu **Utilitários | Gerenciamento de ambiente**:

Abrir Gerenciamento de Ambiente

Utilize duplo clique em **Envio e redirecionamento de Comunicados** ou clique em **Propriedades**:

Gerenciamento de Ambiente

Nas propriedades verifique as configurações:

Propriedades

Divididas em dois blocos, SMTP e POP3/IMAP4, as configurações de SMTP são essenciais para o funcionamento do envio de comunicados, já o de POP3/IMAP4 é opcional porém se desabilitado desativa funcionalidade de [recebimento de resposta e associação com OS](comunicados).

Também há a possibilidade de usar o protocolo Exchange Web Server (EWS), tanto para envio como recebimento. Para isso, basta alterar a opção selecionada em Protocolo.

**Importante**: Outra utilização do acesso POP3/IMAP4/EWS é para manutenção da caixa de e-mail do Supravizio. Com este acesso será possível manter esta caixa sempre vazia. Toda mensagem que chegar é processada e removida da caixa.

A caixa de seleção deve conter o protocolo para a recuperação das mensagens (POP3, IMAP4 ou EWS). Os campos de Usuário e senha devem ser preenchidas com o respectivo usuário e senha da conta criada para o Supravizio, o campo de Porta deve ser preenchido com a porta do serviço (deixe em branco caso seja a porta padrão) e os campos de servidores devem ser preenchidos com os nomes dos servidores dos protocolos utilizados.

**Importante: **Caso a conta de envio de mensagens não seja exatamente a mesma que a de recebimento, será necessário definir o Endereço de reply para respostas de comunicados para que sejam associadas as respostas de comunicados e as respectivas Ordens de serviço.

Neste campo, deve ser inserido o endereço da conta de e-mail a ser verificada e logo abaixo, em Texto do endereço de Reply, deve ser preenchido o nome com a qual esta conta irá aparecer para o usuário ao enviar a resposta.

Configuração de endereço de reply

Na aba Opções pode ser configurado o intervalo das execuções e o horário da primeira execução além de notificações após execução:

Aba Opções

## Casos Especiais

Existem dois casos em que o e-mail recebido pelo servidor deve ser ignorado, caso ele seja um e-mail automático enviado pelo Postmaster ou enviado pelo MAILER-DAEMON pois esses emails geralmente se referem a erros como caixa de mensagem cheia ou indisponibilidade do destinatário.

Para estas situações, é possível configurar a rotina para que ignore estas mensagens, a fim de evitar possíveis problemas, como por exemplo, loop de mensagens.

Configuração para ignorar mensagens

No campo Emails para redirecionamento de mensagens automáticas, é possível configurar um ou mais destinatários para redirecionar as mensagens indevidas e este possa analisar a causa do envio.

Abaixo, é possível inserir um script na linguagem Iron Python para que configurada uma regra, por exemplo, de acordo com seu Remetente, Assunto ou Corpo. Feita a condição, basta definir o valor da variável Cancelar como True, para que estas mensagens sejam ignoradas.

Exemplo de script

Realizadas as alterações, confirme-as e clique em Iniciar (caso a job esteja suspensa) e depois em Repetir:

**Executar rotina**

Verifique o Relatório de Execução:

**Relatório de Execução**

No menu **Utilitários | Mensagens** ficam armazenadas todas mensagens que devem ser enviadas (antes da job executar) ou que foram enviadas:

Caminho para acesso à tela

- Note que todos os comunicados que foram enviados (que apareceram no relatório de execução acima) tem como campo situação Enviado, já o comunicado que ainda não foi enviado é Pendente:

Tela de Mensagens
