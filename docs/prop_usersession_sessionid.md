# SessionId

Caminho: Customização > Modelo de objetos > Utilitários > UserSession > SessionId

Identificador gerado automaticamente pelo sistema para Identificação da Sessão.

**Exemplo 1: modificação da propriedade SessionId**

```
# carrega objeto UserSession de identificador 1
userSession = UserSession.Carrega(1)
# modifica a propriedade SessionId
userSession.SessionId = "Identificador Sessão";
# salva modificação da propriedade SessionId
UserSession.Salva(userSession)
```
