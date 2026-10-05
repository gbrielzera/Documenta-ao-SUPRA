# ApplicationId

Caminho: Customização > Modelo de objetos > Utilitários > UserSession > ApplicationId

Nome da aplicação onde foi realizado o Logon

**Exemplo 1: modificação da propriedade ApplicationId**

```
# carrega objeto UserSession de identificador 1
userSession = UserSession.Carrega(1)
# modifica a propriedade ApplicationId
userSession.ApplicationId = "Supravizio";
# salva modificação da propriedade ApplicationId
UserSession.Salva(userSession)
```
