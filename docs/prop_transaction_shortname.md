# ShortName

Caminho: Customização > Modelo de objetos > Utilitários > Transaction > ShortName

Código da transação utilizado para acesso via barra de ferramentas.

**Exemplo 1: modificação da propriedade ShortName**

```
# carrega objeto Transaction de identificador 1
transaction = Transaction.Carrega(1)
# modifica a propriedade ShortName
transaction.ShortName = "Código";
# salva modificação da propriedade ShortName
Transaction.Salva(transaction)
```
