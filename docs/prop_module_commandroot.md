# CommandRoot

Caminho: Customização > Modelo de objetos > Utilitários > Module > CommandRoot

Item de menu utilizado como comando pai de todas as opções do módulo. Um Módulo possui obrigatoriamente um único comando raiz. Todos os demais comandos estão abaixo deste item (direto ou indiretamente).

**Exemplo 1: modificação da propriedade CommandRoot**

```
# carrega objeto Module de identificador 94
module = Module.Carrega(94)
# modifica a propriedade CommandRoot
module.CommandRoot = Command.Carrega(57);
# salva modificação da propriedade CommandRoot
Module.Salva(module)
```
