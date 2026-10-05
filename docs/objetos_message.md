# Message

Caminho: Customização > Modelo de objetos > Utilitários > Message

Mensagens enviadas em resposta a Eventos ou ferramentas de comunicação do sistema.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AssociatedObjectClass** | Classe de Negócio do objeto associado com a Mensagem | [Class](objetos_class) |
| **AssociatedObjectClassId** | Identificador da Classe de Negócio do objeto associado com a mensagem | Inteiro |
| **Attachments** | Arquivos anexados na Mensagem | [Lista de Attachment](objetos_attachment) |
| **Body** | Corpo da mensagem para envio. O formato pode ser configurado pela propriedade Mime-Format. | String |
| **ErrorDetails** | Relatório contendo detalhes sobre erros ocorridos durante o envio da mensagem. | String |
| **FromAddress** | Endereço de email remetente da mensagem. | String |
| **FromName** | Nome do remetente da mensagem | String |
| **Id** | Identificador da Mensagem. Este valor é acrescentados no Subject da mensagem. | Inteiro |
| **InitialMessage** | Mensagem inicial da comunicação. | [Message](objetos_message) |
| **InitialMessageId** | Identificador da Mensagem inicial. Esta chave é utilizada para identificar respostas de mensagens iniciais. | Inteiro |
| **KeyValue** | Chave de recuperação do objeto associado com a Mensagem. | String |
| **MimeFormat** | Formato MIME da Mensagem | String |
| **Parameters** | Parâmetros de envio | String |
| **ParamInfo** | Descritivo dos parâmetros de envio em formato legível pelo usuário. | String |
| **Priority** | Prioridade que é atribuida para a Mensagem. Esta é a prioridade da mensagem enviada. | [MessagePriority](enum_messagepriority) |
| **Recipients** | Destinatários da Mensagem | [Lista de Recipient](objetos_recipient) |
| **RecoveryCode** | Código de recuperação para a Mensagem. Possui uso e preenchimento conforme critérios definidos pelo sistema usuário. | String |
| **ReplyAddress** | Conta utilizada para reply quando o destinatário responder o comunicado. Quando não informada é utilizada a conta configurada no job de envio de emails. | String |
| **RequestDate** | Data e hora em que a Mensagem foi registrada | Data/hora |
| **RequestReadReceipt** | Configura a Mensagem para solicitar confirmação de leitura pelo usuário destinatário. | Booleano |
| **Status** | Situação da Mensagem | [MessageStatus](enum_messagestatus) |
| **Subject** | Campo Assunto da Mensagem. Em mensagens de respostas o assunto é acrescido do ID da Mensagem. | String |
| **TemporalityClass** | Implementa um cadastro de todas as Classes de Negócio existentes no sistema. Este cadastro torna possível a customização do software permitindo: alteração de documentação, definição de novos campos e regras de negócio. | [Class](objetos_class) |
| **TemporalityClassId** | Identificador da classe que possui temporalidade. | Inteiro |
| **TemporalityExpirationDate** | Após a data de expiração o registro de mensagem é excluído do sistema. | Data/hora |
| **TemporalityId** | Identificador da classe de temporalidade referenciada em TemporalityClass. | Inteiro |
| **TextualRepresention** | Representação textual do objeto de negócio associado com a Mensagem. | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Message Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Message | Message Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Message Carrega(string nomePropriedade, object valorPropriedade); |
