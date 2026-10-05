# RunningServer

Caminho: Customização > Modelo de objetos > Utilitários > Job > RunningServer

Servidor onde está sendo executado o Job. Este valor é preenchido somente enquanto um Job está sendo executado.

**Exemplo 1: modificação da propriedade RunningServer**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade RunningServer
job.RunningServer = "Servidor execução";
# salva modificação da propriedade RunningServer
Job.Salva(job)
```
