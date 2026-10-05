# Source

Caminho: Customização > Modelo de objetos > Utilitários > CommandClass > Source

Código fonte da Classe

**Exemplo 1: modificação da propriedade Source**

```
# carrega objeto CommandClass de identificador 1
commandClass = CommandClass.Carrega(1)
# modifica a propriedade Source
commandClass.Source = "Código fonte";
# salva modificação da propriedade Source
CommandClass.Salva(commandClass)
```
