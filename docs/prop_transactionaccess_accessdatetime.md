# AccessDateTime

Caminho: Customização > Modelo de objetos > Utilitários > TransactionAccess > AccessDateTime

Data/hora de acesso da transação pelo Usuário.

**Exemplo 1: modificação da propriedade AccessDateTime**

```
# carrega objeto TransactionAccess de identificador 1
transactionAccess = TransactionAccess.Carrega(1)
# modifica a propriedade AccessDateTime
transactionAccess.AccessDateTime = DateTime;
# salva modificação da propriedade AccessDateTime
TransactionAccess.Salva(transactionAccess)
```
