# TransactionId

Caminho: Customização > Modelo de objetos > Utilitários > Command > TransactionId

Identificador da Transação associada

**Exemplo 1: modificação da propriedade TransactionId**

```
# carrega objeto Command de identificador 1
command = Command.Carrega(1)
# modifica a propriedade TransactionId
command.TransactionId = 1;
# salva modificação da propriedade TransactionId
Command.Salva(command)
```
