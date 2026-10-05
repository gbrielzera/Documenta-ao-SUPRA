# LastRunningDate

Caminho: Customização > Modelo de objetos > Utilitários > Job > LastRunningDate

Última informação de execução enquanto o Job estiver em execução.

**Exemplo 1: modificação da propriedade LastRunningDate**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade LastRunningDate
job.LastRunningDate = DateTime;
# salva modificação da propriedade LastRunningDate
Job.Salva(job)
```
