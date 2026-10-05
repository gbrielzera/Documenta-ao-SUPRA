# Transaction

Caminho: Customização > Modelo de objetos > Utilitários > TransactionAccess > Transaction

Transação acessada por um Usuário

**Exemplo 1: modificação da propriedade Transaction**

```
# carrega objeto TransactionAccess de identificador 94
transactionAccess = TransactionAccess.Carrega(94)
# modifica a propriedade Transaction
transactionAccess.Transaction = Transaction.Carrega(57);
# salva modificação da propriedade Transaction
TransactionAccess.Salva(transactionAccess)
```
