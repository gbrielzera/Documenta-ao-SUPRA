# ModuleId

Caminho: Customização > Modelo de objetos > Utilitários > Transaction > ModuleId

Identificador do Módulo associado

**Exemplo 1: modificação da propriedade ModuleId**

```
# carrega objeto Transaction de identificador 1
transaction = Transaction.Carrega(1)
# modifica a propriedade ModuleId
transaction.ModuleId = 1;
# salva modificação da propriedade ModuleId
Transaction.Salva(transaction)
```
