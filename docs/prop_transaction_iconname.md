# IconName

Caminho: Customização > Modelo de objetos > Utilitários > Transaction > IconName

Nome do ícone utilizado na Transação. Este nome corresponde ao objeto adicionado como recurso na aplicação cliente.

**Exemplo 1: modificação da propriedade IconName**

```
# carrega objeto Transaction de identificador 1
transaction = Transaction.Carrega(1)
# modifica a propriedade IconName
transaction.IconName = "Nome ícone";
# salva modificação da propriedade IconName
Transaction.Salva(transaction)
```
