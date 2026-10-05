# ContextUserId

Caminho: Customização > Modelo de objetos > Utilitários > Job > ContextUserId

Identificador do Usuário proprietário do Job

**Exemplo 1: modificação da propriedade ContextUserId**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade ContextUserId
job.ContextUserId = 1;
# salva modificação da propriedade ContextUserId
Job.Salva(job)
```
