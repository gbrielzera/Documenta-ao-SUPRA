# Enviroment

Caminho: Customização > Modelo de objetos > Utilitários > LogExecSQL > Enviroment

Ambiente configurado no sistema no instante em que o comando SQL foi executado. Para ambiente de produção não é possível executar comando SQL de modificação ou comandos que contenham a palavra 'commit'

**Exemplo 1: modificação da propriedade Enviroment**

```
# carrega objeto LogExecSQL de identificador 1
logExecSQL = LogExecSQL.Carrega(1)
# modifica a propriedade Enviroment
logExecSQL.Enviroment = "Ambiente";
# salva modificação da propriedade Enviroment
LogExecSQL.Salva(logExecSQL)
```
