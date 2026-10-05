# CreationDate

Caminho: Customização > Modelo de objetos > Utilitários > UserReport > CreationDate

Data/hora de criação do relatório

**Exemplo 1: modificação da propriedade CreationDate**

```
# carrega objeto UserReport de identificador 1
userReport = UserReport.Carrega(1)
# modifica a propriedade CreationDate
userReport.CreationDate = DateTime;
# salva modificação da propriedade CreationDate
UserReport.Salva(userReport)
```
