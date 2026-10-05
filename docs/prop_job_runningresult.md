# RunningResult

Caminho: Customização > Modelo de objetos > Utilitários > Job > RunningResult

Último resultado em processamento

**Exemplo 1: modificação da propriedade RunningResult**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade RunningResult
job.RunningResult = "Último resultado apurado";
# salva modificação da propriedade RunningResult
Job.Salva(job)
```
