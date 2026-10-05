# OriginalText

Caminho: Customização > Modelo de objetos > Utilitários > Transaction > OriginalText

Descrição resumida original

**Exemplo 1: modificação da propriedade OriginalText**

```
# carrega objeto Transaction de identificador 1
transaction = Transaction.Carrega(1)
# modifica a propriedade OriginalText
transaction.OriginalText = "Descrição resumida original";
# salva modificação da propriedade OriginalText
Transaction.Salva(transaction)
```
