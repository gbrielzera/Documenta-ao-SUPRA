# LogoutReason

Caminho: Customização > Modelo de objetos > Utilitários > UserSession > LogoutReason

Motivo do logout do usuário

**Exemplo 1: modificação da propriedade LogoutReason**

```
# carrega objeto UserSession de identificador 1
userSession = UserSession.Carrega(1)
# modifica a propriedade LogoutReason
userSession.LogoutReason = "Motivo";
# salva modificação da propriedade LogoutReason
UserSession.Salva(userSession)
```
