# Sequence

Caminho: Customização > Modelo de objetos > Utilitários > Command > Sequence

Define a sequência de exibição de comandos em lista (menu por exemplo).

**Exemplo 1: modificação da propriedade Sequence**

```
# carrega objeto Command de identificador 1
command = Command.Carrega(1)
# modifica a propriedade Sequence
command.Sequence = 1;
# salva modificação da propriedade Sequence
Command.Salva(command)
```
