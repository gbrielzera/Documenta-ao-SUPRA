# SQL

Caminho: Customização > Modelo de objetos > Utilitários > LogExecSQL > SQL

Comando SQL executado pelo usuário

**Exemplo 1: modificação da propriedade SQL**

```
# carrega objeto LogExecSQL de identificador 1
logExecSQL = LogExecSQL.Carrega(1)
# modifica a propriedade SQL
logExecSQL.SQL = "Comando SQL";
# salva modificação da propriedade SQL
LogExecSQL.Salva(logExecSQL)
```
