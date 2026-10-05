# Description

Caminho: Customização > Modelo de objetos > Utilitários > Job > Description

Descrição detalhada do Job

**Exemplo 1: modificação da propriedade Description**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade Description
job.Description = "Descrição";
# salva modificação da propriedade Description
Job.Salva(job)
```
