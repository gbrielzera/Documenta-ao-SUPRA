# Description

Caminho: Customização > Modelo de objetos > Utilitários > CommandClass > Description

Descrição completa da Classe de Comando

**Exemplo 1: modificação da propriedade Description**

```
# carrega objeto CommandClass de identificador 1
commandClass = CommandClass.Carrega(1)
# modifica a propriedade Description
commandClass.Description = "Descrição";
# salva modificação da propriedade Description
CommandClass.Salva(commandClass)
```
