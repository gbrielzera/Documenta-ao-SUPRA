# ClassId

Caminho: Customização > Modelo de objetos > Utilitários > Job > ClassId

Identificador do(a) Class associado(a)

**Exemplo 1: modificação da propriedade ClassId**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade ClassId
job.ClassId = 1;
# salva modificação da propriedade ClassId
Job.Salva(job)
```
