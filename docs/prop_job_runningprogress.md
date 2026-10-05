# RunningProgress

Caminho: Customização > Modelo de objetos > Utilitários > Job > RunningProgress

Progresso do job em execução.

**Exemplo 1: modificação da propriedade RunningProgress**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade RunningProgress
job.RunningProgress = 1;
# salva modificação da propriedade RunningProgress
Job.Salva(job)
```
