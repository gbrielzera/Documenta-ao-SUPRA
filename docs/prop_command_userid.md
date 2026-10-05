# UserId

Caminho: Customização > Modelo de objetos > Utilitários > Command > UserId

Identificador do Usuário proprietário do Comando

**Exemplo 1: modificação da propriedade UserId**

```
# carrega objeto Command de identificador 1
command = Command.Carrega(1)
# modifica a propriedade UserId
command.UserId = 1;
# salva modificação da propriedade UserId
Command.Salva(command)
```
