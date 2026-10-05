# ExecDateTime

Caminho: Customização > Modelo de objetos > Utilitários > LogExecSQL > ExecDateTime

Data e hora em que o comando SQL foi executado

**Exemplo 1: modificação da propriedade ExecDateTime**

```
# carrega objeto LogExecSQL de identificador 1
logExecSQL = LogExecSQL.Carrega(1)
# modifica a propriedade ExecDateTime
logExecSQL.ExecDateTime = DateTime;
# salva modificação da propriedade ExecDateTime
LogExecSQL.Salva(logExecSQL)
```
