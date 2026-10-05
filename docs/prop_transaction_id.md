# Id

Caminho: Customização > Modelo de objetos > Utilitários > Transaction > Id

Identificador da Transação

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Transaction de identificador 1
transaction = Transaction.Carrega(1)
# modifica a propriedade Id
transaction.Id = 1;
# salva modificação da propriedade Id
Transaction.Salva(transaction)
```
