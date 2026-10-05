# Description

Caminho: Customização > Modelo de objetos > Utilitários > Transaction > Description

Descrição detalhada sobre a transação.

**Exemplo 1: modificação da propriedade Description**

```
# carrega objeto Transaction de identificador 1
transaction = Transaction.Carrega(1)
# modifica a propriedade Description
transaction.Description = "Descrição";
# salva modificação da propriedade Description
Transaction.Salva(transaction)
```
