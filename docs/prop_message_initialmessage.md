# InitialMessage

Caminho: Customização > Modelo de objetos > Utilitários > Message > InitialMessage

Mensagem inicial da comunicação.

**Exemplo 1: modificação da propriedade InitialMessage**

```
# carrega objeto Message de identificador 94
message = Message.Carrega(94)
# modifica a propriedade InitialMessage
message.InitialMessage = Message.Carrega(57);
# salva modificação da propriedade InitialMessage
Message.Salva(message)
```
