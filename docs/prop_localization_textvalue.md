# TextValue

Caminho: Customização > Modelo de objetos > Utilitários > Localization > TextValue

Texto localizado

**Exemplo 1: modificação da propriedade TextValue**

```
# carrega objeto Localization de identificador 1
localization = Localization.Carrega(1)
# modifica a propriedade TextValue
localization.TextValue = "Texto localizado";
# salva modificação da propriedade TextValue
Localization.Salva(localization)
```
