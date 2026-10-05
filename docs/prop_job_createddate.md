# CreatedDate

Caminho: Customização > Modelo de objetos > Utilitários > Job > CreatedDate

Data e hora em que o Job foi criado.

**Exemplo 1: modificação da propriedade CreatedDate**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade CreatedDate
job.CreatedDate = DateTime;
# salva modificação da propriedade CreatedDate
Job.Salva(job)
```
