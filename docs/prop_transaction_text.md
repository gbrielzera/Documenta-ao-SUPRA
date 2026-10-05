# Text

Caminho: Customização > Modelo de objetos > Utilitários > Transaction > Text

Descrição resumida da Transação.

**Exemplo 1: modificação da propriedade Text**

```
# carrega objeto Transaction de identificador 1
transaction = Transaction.Carrega(1)
# modifica a propriedade Text
transaction.Text = "Descrição resumida";
# salva modificação da propriedade Text
Transaction.Salva(transaction)
```
