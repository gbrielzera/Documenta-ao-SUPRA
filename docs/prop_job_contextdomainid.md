# ContextDomainId

Caminho: Customização > Modelo de objetos > Utilitários > Job > ContextDomainId

Identificador do Domínio onde será executado o Job

**Exemplo 1: modificação da propriedade ContextDomainId**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade ContextDomainId
job.ContextDomainId = 1;
# salva modificação da propriedade ContextDomainId
Job.Salva(job)
```
