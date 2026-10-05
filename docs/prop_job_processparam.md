# ProcessParam

Caminho: Customização > Modelo de objetos > Utilitários > Job > ProcessParam

Parâmetro para Classe de Processo

**Exemplo 1: modificação da propriedade ProcessParam**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade ProcessParam
job.ProcessParam = "Param";
# salva modificação da propriedade ProcessParam
Job.Salva(job)
```
