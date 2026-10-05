# Type

Caminho: Customização > Modelo de objetos > Utilitários > DatabaseConnection > Type

Tipo de conexão para o banco externo.

**Exemplo 1: modificação da propriedade Type**

```
# carrega objeto DatabaseConnection de identificador 1
databaseConnection = DatabaseConnection.Carrega(1)
# modifica a propriedade Type
databaseConnection.Type = "SystemDataSqlClient";
# salva modificação da propriedade Type
DatabaseConnection.Salva(databaseConnection)
```
