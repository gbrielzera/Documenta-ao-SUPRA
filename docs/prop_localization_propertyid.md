# PropertyId

Caminho: Customização > Modelo de objetos > Utilitários > Localization > PropertyId

Identificador do(a) Property associado(a)

**Exemplo 1: modificação da propriedade PropertyId**

```
# carrega objeto Localization de identificador 1
localization = Localization.Carrega(1)
# modifica a propriedade PropertyId
localization.PropertyId = 1;
# salva modificação da propriedade PropertyId
Localization.Salva(localization)
```
