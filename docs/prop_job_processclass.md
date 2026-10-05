# ProcessClass

Caminho: Customização > Modelo de objetos > Utilitários > Job > ProcessClass

Classe de Processo responsável pela execução do Job

**Exemplo 1: modificação da propriedade ProcessClass**

```
# carrega objeto Job de identificador 94
job = Job.Carrega(94)
# modifica a propriedade ProcessClass
job.ProcessClass = Class.Carrega(57);
# salva modificação da propriedade ProcessClass
Job.Salva(job)
```
