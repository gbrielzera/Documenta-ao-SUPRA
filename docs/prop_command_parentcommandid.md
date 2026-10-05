# ParentCommandId

Caminho: Customização > Modelo de objetos > Utilitários > Command > ParentCommandId

Identificador do Comando Pai

**Exemplo 1: modificação da propriedade ParentCommandId**

```
# carrega objeto Command de identificador 1
command = Command.Carrega(1)
# modifica a propriedade ParentCommandId
command.ParentCommandId = 1;
# salva modificação da propriedade ParentCommandId
Command.Salva(command)
```
