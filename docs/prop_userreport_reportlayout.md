# ReportLayout

Caminho: Customização > Modelo de objetos > Utilitários > UserReport > ReportLayout

Layout do relatório mantidos em um controle Report serializado

**Exemplo 1: modificação da propriedade ReportLayout**

```
# carrega objeto UserReport de identificador 1
userReport = UserReport.Carrega(1)
# modifica a propriedade ReportLayout
# salva modificação da propriedade ReportLayout
UserReport.Salva(userReport)
```
