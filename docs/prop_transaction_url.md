# Url

Caminho: Customização > Modelo de objetos > Utilitários > Transaction > Url

Caminho para objeto inicial da Transação

**Exemplo 1: modificação da propriedade Url**

```
# carrega objeto Transaction de identificador 1
transaction = Transaction.Carrega(1)
# modifica a propriedade Url
transaction.Url = "Url";
# salva modificação da propriedade Url
Transaction.Salva(transaction)
```
