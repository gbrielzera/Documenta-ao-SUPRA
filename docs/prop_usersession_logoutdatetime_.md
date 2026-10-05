# LogoutDateTime

Caminho: Customização > Modelo de objetos > Utilitários > UserSession > LogoutDateTime

Data/hora do fim de conexão.

**Exemplo 1: modificação da propriedade LogoutDateTime**

```
# carrega objeto UserSession de identificador 1
userSession = UserSession.Carrega(1)
# modifica a propriedade LogoutDateTime
userSession.LogoutDateTime = DateTime;
# salva modificação da propriedade LogoutDateTime
UserSession.Salva(userSession)
```
