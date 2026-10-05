# User

Caminho: Customização > Modelo de objetos > Utilitários > LogExecSQL > User

Usuário que executou o comando SQL

**Exemplo 1: modificação da propriedade User**

```
# carrega objeto LogExecSQL de identificador 94
logExecSQL = LogExecSQL.Carrega(94)
# modifica a propriedade User
logExecSQL.User = User.Carrega(57);
# salva modificação da propriedade User
LogExecSQL.Salva(logExecSQL)
```
