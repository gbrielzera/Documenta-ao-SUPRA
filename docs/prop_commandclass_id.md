# Id

Caminho: Customização > Modelo de objetos > Utilitários > CommandClass > Id

Identificador da Classe de Comando

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto CommandClass de identificador 1
commandClass = CommandClass.Carrega(1)
# modifica a propriedade Id
commandClass.Id = 1;
# salva modificação da propriedade Id
CommandClass.Salva(commandClass)
```
