# Description

Caminho: Customização > Modelo de objetos > Utilitários > UserReport > Description

Descrição detalhada do Report

**Exemplo 1: modificação da propriedade Description**

```
# carrega objeto UserReport de identificador 1
userReport = UserReport.Carrega(1)
# modifica a propriedade Description
userReport.Description = "Descrição";
# salva modificação da propriedade Description
UserReport.Salva(userReport)
```
