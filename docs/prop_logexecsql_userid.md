# UserId

Caminho: Customização > Modelo de objetos > Utilitários > LogExecSQL > UserId

Identificador do usuário que executou o comando SQL.

**Exemplo 1: modificação da propriedade UserId**

```
# carrega objeto LogExecSQL de identificador 1
logExecSQL = LogExecSQL.Carrega(1)
# modifica a propriedade UserId
logExecSQL.UserId = 1;
# salva modificação da propriedade UserId
LogExecSQL.Salva(logExecSQL)
```
