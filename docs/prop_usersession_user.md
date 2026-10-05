# User

Caminho: Customização > Modelo de objetos > Utilitários > UserSession > User

Usuário autorizado a acessar o sistema.

**Exemplo 1: modificação da propriedade User**

```
# carrega objeto UserSession de identificador 94
userSession = UserSession.Carrega(94)
# modifica a propriedade User
userSession.User = User.Carrega(57);
# salva modificação da propriedade User
UserSession.Salva(userSession)
```
