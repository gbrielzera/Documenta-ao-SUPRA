# JobHistory

Caminho: Customização > Modelo de objetos > Utilitários > Job > JobHistory

Histórico de execuções

**Exemplo 1: percorrer objetos da propriedade JobHistory**

```
# carrega objeto Job de identificador 94
job = Job.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if job != None:
    # percorre objetos da propriedade JobHistory e para cada uma escreve conteúdo no log de mensagens
    for jobHistory in job.JobHistory:
        Utils.LogInformation(jobHistory.ToString())
```
