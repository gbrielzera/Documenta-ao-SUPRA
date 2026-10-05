# Name

Caminho: Customização > Modelo de objetos > Utilitários > CommandClass > Name

Nome da Classe incluindo namespace

**Exemplo 1: modificação da propriedade Name**

```
# carrega objeto CommandClass de identificador 1
commandClass = CommandClass.Carrega(1)
# modifica a propriedade Name
commandClass.Name = "Nome completo";
# salva modificação da propriedade Name
CommandClass.Salva(commandClass)
```
