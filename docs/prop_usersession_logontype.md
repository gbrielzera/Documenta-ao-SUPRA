# LogonType

Caminho: Customização > Modelo de objetos > Utilitários > UserSession > LogonType

Tipo de Logon que gerou a sessão de usuário

**Exemplo 1: modificação da propriedade LogonType**

```
# carrega objeto UserSession de identificador 1
userSession = UserSession.Carrega(1)
# modifica a propriedade LogonType
userSession.LogonType = "System";
# salva modificação da propriedade LogonType
UserSession.Salva(userSession)
```
