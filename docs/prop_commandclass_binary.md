# Binary

Caminho: Customização > Modelo de objetos > Utilitários > CommandClass > Binary

Código binário

**Exemplo 1: modificação da propriedade Binary**

```
# carrega objeto CommandClass de identificador 1
commandClass = CommandClass.Carrega(1)
# modifica a propriedade Binary
commandClass.Binary = "Código binário";
# salva modificação da propriedade Binary
CommandClass.Salva(commandClass)
```
