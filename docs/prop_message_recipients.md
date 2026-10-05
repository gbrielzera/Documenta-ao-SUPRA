# Recipients

Caminho: Customização > Modelo de objetos > Utilitários > Message > Recipients

Destinatários da Mensagem

**Exemplo 1: percorrer objetos da propriedade Recipients**

```
# carrega objeto Message de identificador 94
message = Message.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if message != None:
    # percorre objetos da propriedade Recipients e para cada uma escreve conteúdo no log de mensagens
    for recipient in message.Recipients:
        Utils.LogInformation(recipient.ToString())
```
