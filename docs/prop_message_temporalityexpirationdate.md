# TemporalityExpirationDate

Caminho: Customização > Modelo de objetos > Utilitários > Message > TemporalityExpirationDate

Após a data de expiração o registro de mensagem é excluído do sistema.

**Exemplo 1: modificação da propriedade TemporalityExpirationDate**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade TemporalityExpirationDate
message.TemporalityExpirationDate = DateTime;
# salva modificação da propriedade TemporalityExpirationDate
Message.Salva(message)
```
