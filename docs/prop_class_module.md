# Module

Caminho: Customização > Modelo de objetos > Utilitários > Class > Module

Um Módulo define um conjunto de funcionalidades pertencentes a uma aplicação. Para cada Módulo existe um item de menu raiz denominado 'Comando raiz' e a partir deste item são associados todos as opções de comandos do módulo.

**Exemplo 1: modificação da propriedade Module**

```
# carrega objeto Class de identificador 94
class = Class.Carrega(94)
# modifica a propriedade Module
class.Module = Module.Carrega(57);
# salva modificação da propriedade Module
Class.Salva(class)
```
