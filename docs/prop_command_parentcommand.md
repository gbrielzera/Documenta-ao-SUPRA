# ParentCommand

Caminho: Customização > Modelo de objetos > Utilitários > Command > ParentCommand

Comando utilizado como container deste item. Para um comando raiz de módulo ou botões customizados na barra de ferramentas este valor será nulo.

**Exemplo 1: modificação da propriedade ParentCommand**

```
# carrega objeto Command de identificador 94
command = Command.Carrega(94)
# modifica a propriedade ParentCommand
command.ParentCommand = Command.Carrega(57);
# salva modificação da propriedade ParentCommand
Command.Salva(command)
```
