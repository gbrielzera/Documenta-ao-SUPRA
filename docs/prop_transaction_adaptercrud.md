# AdapterCRUD

Caminho: Customização > Modelo de objetos > Utilitários > Transaction > AdapterCRUD

Classe que customiza o comportamento de telas CRUD

**Exemplo 1: modificação da propriedade AdapterCRUD**

```
# carrega objeto Transaction de identificador 1
transaction = Transaction.Carrega(1)
# modifica a propriedade AdapterCRUD
transaction.AdapterCRUD = "Adapter CRUD";
# salva modificação da propriedade AdapterCRUD
Transaction.Salva(transaction)
```
