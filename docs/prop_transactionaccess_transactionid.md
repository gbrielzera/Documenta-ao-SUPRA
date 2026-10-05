# TransactionId

Caminho: Customização > Modelo de objetos > Utilitários > TransactionAccess > TransactionId

Identificador do(a) Transaction associado(a)

**Exemplo 1: modificação da propriedade TransactionId**

```
# carrega objeto TransactionAccess de identificador 1
transactionAccess = TransactionAccess.Carrega(1)
# modifica a propriedade TransactionId
transactionAccess.TransactionId = 1;
# salva modificação da propriedade TransactionId
TransactionAccess.Salva(transactionAccess)
```
