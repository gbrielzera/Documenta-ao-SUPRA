# PropertyId

Caminho: Customização > Modelo de objetos > Utilitários > PropertyLayout > PropertyId

Identificador da Propriedade

**Exemplo 1: modificação da propriedade PropertyId**

```
# carrega objeto PropertyLayout de identificador 1
propertyLayout = PropertyLayout.Carrega(1)
# modifica a propriedade PropertyId
propertyLayout.PropertyId = 1;
# salva modificação da propriedade PropertyId
PropertyLayout.Salva(propertyLayout)
```
