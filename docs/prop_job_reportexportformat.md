# ReportExportFormat

Caminho: Customização > Modelo de objetos > Utilitários > Job > ReportExportFormat

Formato de saída do arquivo gerado pelo relatório

**Exemplo 1: modificação da propriedade ReportExportFormat**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade ReportExportFormat
job.ReportExportFormat = "PDF";
# salva modificação da propriedade ReportExportFormat
Job.Salva(job)
```
