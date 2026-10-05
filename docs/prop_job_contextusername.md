# ContextUsername

Caminho: Customização > Modelo de objetos > Utilitários > Job > ContextUsername

Nome do usuário proprietário do Job

**Exemplo 1: modificação da propriedade ContextUsername**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade ContextUsername
job.ContextUsername = "Nome usuário";
# salva modificação da propriedade ContextUsername
Job.Salva(job)
```
