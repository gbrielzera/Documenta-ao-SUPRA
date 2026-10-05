# ConnectedUsers

Caminho: Customização > Modelo de objetos > Utilitários > UserSession > ConnectedUsers

Registro da quantidade de usuários conectados no instante do Logon. São desconsideradas sessões iniciadas por rotinas de manutenção de dados e processamento de Jobs (Logon de sistema).

**Exemplo 1: modificação da propriedade ConnectedUsers**

```
# carrega objeto UserSession de identificador 1
userSession = UserSession.Carrega(1)
# modifica a propriedade ConnectedUsers
userSession.ConnectedUsers = 1;
# salva modificação da propriedade ConnectedUsers
UserSession.Salva(userSession)
```
