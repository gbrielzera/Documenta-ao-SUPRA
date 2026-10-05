# GroupParent

Caminho: Customização > Modelo de objetos > Utilitários > PropertyLayout > GroupParent

Nome do agrupamento Pai

**Exemplo 1: modificação da propriedade GroupParent**

```
# carrega objeto PropertyLayout de identificador 1
propertyLayout = PropertyLayout.Carrega(1)
# modifica a propriedade GroupParent
propertyLayout.GroupParent = "Grupo pai";
# salva modificação da propriedade GroupParent
PropertyLayout.Salva(propertyLayout)
```
