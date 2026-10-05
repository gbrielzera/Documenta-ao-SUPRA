# LogonDateTime

Caminho: Customização > Modelo de objetos > Utilitários > UserSession > LogonDateTime

Data/hora do início de conexão.

**Exemplo 1: modificação da propriedade LogonDateTime**

```
# carrega objeto UserSession de identificador 1
userSession = UserSession.Carrega(1)
# modifica a propriedade LogonDateTime
userSession.LogonDateTime = DateTime;
# salva modificação da propriedade LogonDateTime
UserSession.Salva(userSession)
```
