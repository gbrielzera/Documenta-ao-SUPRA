# ErrorMessage

Caminho: Customização > Modelo de objetos > Utilitários > LogExecSQL > ErrorMessage

Mensagem de erro gerada pela execução do comando SQL. Se o comando for executado com sucesso então este campo será nulo.

**Exemplo 1: modificação da propriedade ErrorMessage**

```
# carrega objeto LogExecSQL de identificador 1
logExecSQL = LogExecSQL.Carrega(1)
# modifica a propriedade ErrorMessage
logExecSQL.ErrorMessage = "Mensagem de erro";
# salva modificação da propriedade ErrorMessage
LogExecSQL.Salva(logExecSQL)
```
