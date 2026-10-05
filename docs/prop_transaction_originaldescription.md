# OriginalDescription

Caminho: Customização > Modelo de objetos > Utilitários > Transaction > OriginalDescription

Descrição detalhada original.

**Exemplo 1: modificação da propriedade OriginalDescription**

```
# carrega objeto Transaction de identificador 1
transaction = Transaction.Carrega(1)
# modifica a propriedade OriginalDescription
transaction.OriginalDescription = "Descrição original";
# salva modificação da propriedade OriginalDescription
Transaction.Salva(transaction)
```
