# Enabled

Caminho: Customização > Modelo de objetos > Utilitários > DatabaseConnection > Enabled

Indica que o DatabaseConnection está ativo no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema.

**Exemplo 1: modificação da propriedade Enabled**

```
# carrega objeto DatabaseConnection de identificador 1
databaseConnection = DatabaseConnection.Carrega(1)
# modifica a propriedade Enabled
databaseConnection.Enabled = true;
# salva modificação da propriedade Enabled
DatabaseConnection.Salva(databaseConnection)
```
