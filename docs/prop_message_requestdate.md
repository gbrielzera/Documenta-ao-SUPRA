# RequestDate

Caminho: Customização > Modelo de objetos > Utilitários > Message > RequestDate

Data e hora em que a Mensagem foi registrada

**Exemplo 1: modificação da propriedade RequestDate**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade RequestDate
message.RequestDate = DateTime;
# salva modificação da propriedade RequestDate
Message.Salva(message)
```
