# Status

Caminho: Customização > Modelo de objetos > Utilitários > Message > Status

Situação da Mensagem

**Exemplo 1: modificação da propriedade Status**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade Status
message.Status = "Pending";
# salva modificação da propriedade Status
Message.Salva(message)
```
