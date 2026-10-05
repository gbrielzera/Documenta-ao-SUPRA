# InitialMessageId

Caminho: Customização > Modelo de objetos > Utilitários > Message > InitialMessageId

Identificador da Mensagem inicial. Esta chave é utilizada para identificar respostas de mensagens iniciais.

**Exemplo 1: modificação da propriedade InitialMessageId**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade InitialMessageId
message.InitialMessageId = 1;
# salva modificação da propriedade InitialMessageId
Message.Salva(message)
```
