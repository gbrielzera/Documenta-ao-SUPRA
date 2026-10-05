# Culture

Caminho: Customização > Modelo de objetos > Utilitários > Localization > Culture

Cultura associada com a localização.

**Exemplo 1: modificação da propriedade Culture**

```
# carrega objeto Localization de identificador 94
localization = Localization.Carrega(94)
# modifica a propriedade Culture
localization.Culture = Culture.Carrega(57);
# salva modificação da propriedade Culture
Localization.Salva(localization)
```
