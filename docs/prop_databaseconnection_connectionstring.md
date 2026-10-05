# ConnectionString

Caminho: Customização > Modelo de objetos > Utilitários > DatabaseConnection > ConnectionString

String de conexão do banco de dados

**Exemplo 1: modificação da propriedade ConnectionString**

```
# carrega objeto DatabaseConnection de identificador 1
databaseConnection = DatabaseConnection.Carrega(1)
# modifica a propriedade ConnectionString
databaseConnection.ConnectionString = "String de conexão";
# salva modificação da propriedade ConnectionString
DatabaseConnection.Salva(databaseConnection)
```
