# MimeFormat

Caminho: Customização > Modelo de objetos > Utilitários > Message > MimeFormat

Formato MIME da Mensagem

**Exemplo 1: modificação da propriedade MimeFormat**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade MimeFormat
message.MimeFormat = "Formato MIME";
# salva modificação da propriedade MimeFormat
Message.Salva(message)
```
