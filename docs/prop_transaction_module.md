# Module

Caminho: Customização > Modelo de objetos > Utilitários > Transaction > Module

System Module

**Exemplo 1: modificação da propriedade Module**

```
# carrega objeto Transaction de identificador 94
transaction = Transaction.Carrega(94)
# modifica a propriedade Module
transaction.Module = Module.Carrega(57);
# salva modificação da propriedade Module
Transaction.Salva(transaction)
```
