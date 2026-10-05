# FromAddress

Caminho: Customização > Modelo de objetos > Utilitários > Message > FromAddress

Endereço de email remetente da mensagem.

**Exemplo 1: modificação da propriedade FromAddress**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade FromAddress
message.FromAddress = "Remetente";
# salva modificação da propriedade FromAddress
Message.Salva(message)
```
