# ReplyAddress

Caminho: Customização > Modelo de objetos > Utilitários > Message > ReplyAddress

Conta utilizada para reply quando o destinatário responder o comunicado. Quando não informada é utilizada a conta configurada no job de envio de emails.

**Exemplo 1: modificação da propriedade ReplyAddress**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade ReplyAddress
message.ReplyAddress = "Endereço de reply";
# salva modificação da propriedade ReplyAddress
Message.Salva(message)
```
