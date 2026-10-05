# Enabled

Caminho: Customização > Modelo de objetos > Utilitários > Job > Enabled

Indica que o Job está ativo

**Exemplo 1: modificação da propriedade Enabled**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade Enabled
job.Enabled = true;
# salva modificação da propriedade Enabled
Job.Salva(job)
```
