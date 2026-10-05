# NextTimePeriodCount

Caminho: Customização > Modelo de objetos > Utilitários > Job > NextTimePeriodCount

Quantidade de Períodos a serem acrescentados em NextTime para próxima execução

**Exemplo 1: modificação da propriedade NextTimePeriodCount**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade NextTimePeriodCount
job.NextTimePeriodCount = 1;
# salva modificação da propriedade NextTimePeriodCount
Job.Salva(job)
```
