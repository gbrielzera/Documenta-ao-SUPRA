# CommandRootId

Caminho: Customização > Modelo de objetos > Utilitários > Module > CommandRootId

Identificador do item de menu denominado 'Comando raiz'

**Exemplo 1: modificação da propriedade CommandRootId**

```
# carrega objeto Module de identificador 1
module = Module.Carrega(1)
# modifica a propriedade CommandRootId
module.CommandRootId = 1;
# salva modificação da propriedade CommandRootId
Module.Salva(module)
```
