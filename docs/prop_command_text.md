# Text

Caminho: Customização > Modelo de objetos > Utilitários > Command > Text

Texto exibido em itens de menu ou botões para seleção de comando pelo usuário.

**Exemplo 1: modificação da propriedade Text**

```
# carrega objeto Command de identificador 1
command = Command.Carrega(1)
# modifica a propriedade Text
command.Text = "Descrição";
# salva modificação da propriedade Text
Command.Salva(command)
```
