# Creator

Caminho: Customização > Modelo de objetos > Utilitários > UserReport > Creator

Usuário que criou o relatório

**Exemplo 1: modificação da propriedade Creator**

```
# carrega objeto UserReport de identificador 94
userReport = UserReport.Carrega(94)
# modifica a propriedade Creator
userReport.Creator = User.Carrega(57);
# salva modificação da propriedade Creator
UserReport.Salva(userReport)
```
