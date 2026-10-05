# Id

Caminho: Customização > Modelo de objetos > Utilitários > Job > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Job

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade Id
job.Id = 1;
# salva modificação da propriedade Id
Job.Salva(job)
```
