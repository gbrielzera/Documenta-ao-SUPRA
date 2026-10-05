# Id

Caminho: Customização > Modelo de objetos > Utilitários > DatabaseConnection > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um DatabaseConnection

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto DatabaseConnection de identificador 1
databaseConnection = DatabaseConnection.Carrega(1)
# modifica a propriedade Id
databaseConnection.Id = 1;
# salva modificação da propriedade Id
DatabaseConnection.Salva(databaseConnection)
```
