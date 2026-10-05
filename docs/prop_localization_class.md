# Class

Caminho: Customização > Modelo de objetos > Utilitários > Localization > Class

Classe do objeto de negócio localizado.

**Exemplo 1: modificação da propriedade Class**

```
# carrega objeto Localization de identificador 94
localization = Localization.Carrega(94)
# modifica a propriedade Class
localization.Class = Class.Carrega(57);
# salva modificação da propriedade Class
Localization.Salva(localization)
```
