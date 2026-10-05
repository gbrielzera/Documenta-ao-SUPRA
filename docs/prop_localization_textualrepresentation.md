# TextualRepresentation

Caminho: Customização > Modelo de objetos > Utilitários > Localization > TextualRepresentation

Representação textual do registro localizado

**Exemplo 1: modificação da propriedade TextualRepresentation**

```
# carrega objeto Localization de identificador 1
localization = Localization.Carrega(1)
# modifica a propriedade TextualRepresentation
localization.TextualRepresentation = "Representação textual";
# salva modificação da propriedade TextualRepresentation
Localization.Salva(localization)
```
