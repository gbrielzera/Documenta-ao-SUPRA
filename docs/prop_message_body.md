# Body

Caminho: Customização > Modelo de objetos > Utilitários > Message > Body

Corpo da mensagem para envio. O formato pode ser configurado pela propriedade Mime-Format.

**Exemplo 1: modificação da propriedade Body**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade Body
message.Body = "Corpo";
# salva modificação da propriedade Body
Message.Salva(message)
```
