# ClassId

Caminho: Customização > Modelo de objetos > Utilitários > CommandClass > ClassId

Identificador da Classe associada

**Exemplo 1: modificação da propriedade ClassId**

```
# carrega objeto CommandClass de identificador 1
commandClass = CommandClass.Carrega(1)
# modifica a propriedade ClassId
commandClass.ClassId = 1;
# salva modificação da propriedade ClassId
CommandClass.Salva(commandClass)
```
