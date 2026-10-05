# Id

Caminho: Customização > Modelo de objetos > Utilitários > Command > Id

Identificador do Comando

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Command de identificador 1
command = Command.Carrega(1)
# modifica a propriedade Id
command.Id = 1;
# salva modificação da propriedade Id
Command.Salva(command)
```
