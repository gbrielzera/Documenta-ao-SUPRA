# Enabled

Caminho: Customização > Modelo de objetos > Utilitários > Transaction > Enabled

Indica que a Transação está ativa. Quando desativada a Transação não é mais visível para o usuário.

**Exemplo 1: modificação da propriedade Enabled**

```
# carrega objeto Transaction de identificador 1
transaction = Transaction.Carrega(1)
# modifica a propriedade Enabled
transaction.Enabled = true;
# salva modificação da propriedade Enabled
Transaction.Salva(transaction)
```
