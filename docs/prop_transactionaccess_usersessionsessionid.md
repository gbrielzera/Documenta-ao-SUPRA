# UserSessionSessionId

Caminho: Customização > Modelo de objetos > Utilitários > TransactionAccess > UserSessionSessionId

Identificador do(a) UserSession associado(a)

**Exemplo 1: modificação da propriedade UserSessionSessionId**

```
# carrega objeto TransactionAccess de identificador 1
transactionAccess = TransactionAccess.Carrega(1)
# modifica a propriedade UserSessionSessionId
transactionAccess.UserSessionSessionId = "Identificador Sessão";
# salva modificação da propriedade UserSessionSessionId
TransactionAccess.Salva(transactionAccess)
```
