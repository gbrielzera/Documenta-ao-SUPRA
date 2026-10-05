# CultureId

Caminho: Customização > Modelo de objetos > Utilitários > Localization > CultureId

Identificador da Cultura associada com a localização.

**Exemplo 1: modificação da propriedade CultureId**

```
# carrega objeto Localization de identificador 1
localization = Localization.Carrega(1)
# modifica a propriedade CultureId
localization.CultureId = 1;
# salva modificação da propriedade CultureId
Localization.Salva(localization)
```
