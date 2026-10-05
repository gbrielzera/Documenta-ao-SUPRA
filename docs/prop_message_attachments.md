# Attachments

Caminho: Customização > Modelo de objetos > Utilitários > Message > Attachments

Arquivos anexados na Mensagem

**Exemplo 1: percorrer objetos da propriedade Attachments**

```
# carrega objeto Message de identificador 94
message = Message.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if message != None:
    # percorre objetos da propriedade Attachments e para cada uma escreve conteúdo no log de mensagens
    for attachment in message.Attachments:
        Utils.LogInformation(attachment.ToString())
```
