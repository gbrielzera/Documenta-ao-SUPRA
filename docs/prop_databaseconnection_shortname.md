# Shortname

Caminho: Customização > Modelo de objetos > Utilitários > DatabaseConnection > Shortname

Nome resumido do DatabaseConnection

**Exemplo 1: modificação da propriedade Shortname**

```
# carrega objeto DatabaseConnection de identificador 1
databaseConnection = DatabaseConnection.Carrega(1)
# modifica a propriedade Shortname
databaseConnection.Shortname = "Sigla";
# salva modificação da propriedade Shortname
DatabaseConnection.Salva(databaseConnection)
```
