# Enabled

Caminho: Customização > Modelo de objetos > Utilitários > UserReport > Enabled

Indica que o Report está ativo no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema.

**Exemplo 1: modificação da propriedade Enabled**

```
# carrega objeto UserReport de identificador 1
userReport = UserReport.Carrega(1)
# modifica a propriedade Enabled
userReport.Enabled = true;
# salva modificação da propriedade Enabled
UserReport.Salva(userReport)
```
