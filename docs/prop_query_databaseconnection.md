# DatabaseConnection

Caminho: Customização > Modelo de objetos > Utilitários > Query > DatabaseConnection

Conexão de banco de dados externo

**Exemplo 1: modificação da propriedade DatabaseConnection**

```
# carrega objeto Query de identificador 94
query = Query.Carrega(94)
# modifica a propriedade DatabaseConnection
query.DatabaseConnection = DatabaseConnection.Carrega(57);
# salva modificação da propriedade DatabaseConnection
Query.Salva(query)
```
