# UserId

Caminho: Customização > Modelo de objetos > Utilitários > UserSession > UserId

Identificador do(a) User associado(a)

**Exemplo 1: modificação da propriedade UserId**

```
# carrega objeto UserSession de identificador 1
userSession = UserSession.Carrega(1)
# modifica a propriedade UserId
userSession.UserId = 1;
# salva modificação da propriedade UserId
UserSession.Salva(userSession)
```
