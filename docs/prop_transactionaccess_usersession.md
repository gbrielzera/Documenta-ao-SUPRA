# UserSession

Caminho: Customização > Modelo de objetos > Utilitários > TransactionAccess > UserSession

Sessão de Usuário que realizou o acesso

**Exemplo 1: modificação da propriedade UserSession**

```
# carrega objeto TransactionAccess de identificador 94
transactionAccess = TransactionAccess.Carrega(94)
# modifica a propriedade UserSession
transactionAccess.UserSession = UserSession.Carrega(57);
# salva modificação da propriedade UserSession
TransactionAccess.Salva(transactionAccess)
```
