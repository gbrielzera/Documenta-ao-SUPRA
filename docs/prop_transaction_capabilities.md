# Capabilities

Caminho: Customização > Modelo de objetos > Utilitários > Transaction > Capabilities

Funcionalidades disponibilizadas na Transação. Exemplos de funções disponíveis: AllowEdit, AllowRemove, AllowNew etc.

**Exemplo 1: modificação da propriedade Capabilities**

```
# carrega objeto Transaction de identificador 1
transaction = Transaction.Carrega(1)
# modifica a propriedade Capabilities
transaction.Capabilities = "Funções disponíveis";
# salva modificação da propriedade Capabilities
Transaction.Salva(transaction)
```
