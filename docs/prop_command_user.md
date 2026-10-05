# User

Caminho: Customização > Modelo de objetos > Utilitários > Command > User

Usuário proprietário do Comando. Esta propriedade é utilizada para customização da barra de ferramentas do sistema.

**Exemplo 1: modificação da propriedade User**

```
# carrega objeto Command de identificador 94
command = Command.Carrega(94)
# modifica a propriedade User
command.User = User.Carrega(57);
# salva modificação da propriedade User
Command.Salva(command)
```
