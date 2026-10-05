# UserId

Caminho: Customização > Modelo de objetos > Utilitários > Job > UserId

Identificador do Usuário criador do Job

**Exemplo 1: modificação da propriedade UserId**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade UserId
job.UserId = 1;
# salva modificação da propriedade UserId
Job.Salva(job)
```
