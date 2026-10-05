# NextTimePeriod

Caminho: Customização > Modelo de objetos > Utilitários > Job > NextTimePeriod

Período a ser acrescido em NextTime para agendamento da próxima execução.

**Exemplo 1: modificação da propriedade NextTimePeriod**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade NextTimePeriod
job.NextTimePeriod = 1;
# salva modificação da propriedade NextTimePeriod
Job.Salva(job)
```
