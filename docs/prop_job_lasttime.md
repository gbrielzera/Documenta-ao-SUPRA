# LastTime

Caminho: Customização > Modelo de objetos > Utilitários > Job > LastTime

Data/hora da última execução

**Exemplo 1: modificação da propriedade LastTime**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade LastTime
job.LastTime = DateTime;
# salva modificação da propriedade LastTime
Job.Salva(job)
```
