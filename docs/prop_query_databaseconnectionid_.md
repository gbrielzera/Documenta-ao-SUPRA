# DatabaseConnectionId

Caminho: Customização > Modelo de objetos > Utilitários > Query > DatabaseConnectionId

Identificador da conexão de banco de dados externo

**Exemplo 1: modificação da propriedade DatabaseConnectionId**

```
# carrega objeto Query de identificador 1
query = Query.Carrega(1)
# modifica a propriedade DatabaseConnectionId
query.DatabaseConnectionId = 1;
# salva modificação da propriedade DatabaseConnectionId
Query.Salva(query)
```
