# Rollback

Caminho: Customização > Modelo de objetos > Utilitários > LogExecSQL > Rollback

Indica que foi necessário executar a rotina de rollback

**Exemplo 1: modificação da propriedade Rollback**

```
# carrega objeto LogExecSQL de identificador 1
logExecSQL = LogExecSQL.Carrega(1)
# modifica a propriedade Rollback
logExecSQL.Rollback = true;
# salva modificação da propriedade Rollback
LogExecSQL.Salva(logExecSQL)
```
