# Creator

Caminho: Customização > Modelo de objetos > Utilitários > Job > Creator

Usuário criador do Job

**Exemplo 1: modificação da propriedade Creator**

```
# carrega objeto Job de identificador 94
job = Job.Carrega(94)
# modifica a propriedade Creator
job.Creator = User.Carrega(57);
# salva modificação da propriedade Creator
Job.Salva(job)
```
