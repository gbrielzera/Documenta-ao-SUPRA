# NextTime

Caminho: Customização > Modelo de objetos > Utilitários > Job > NextTime

Data/hora da próxima execução.

**Exemplo 1: modificação da propriedade NextTime**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade NextTime
job.NextTime = DateTime;
# salva modificação da propriedade NextTime
Job.Salva(job)
```
