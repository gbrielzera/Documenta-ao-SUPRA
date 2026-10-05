# FromName

Caminho: Customização > Modelo de objetos > Utilitários > Message > FromName

Nome do remetente da mensagem

**Exemplo 1: modificação da propriedade FromName**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade FromName
message.FromName = "Nome remetente";
# salva modificação da propriedade FromName
Message.Salva(message)
```
