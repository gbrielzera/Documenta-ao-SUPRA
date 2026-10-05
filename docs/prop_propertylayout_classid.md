# ClassId

Caminho: Customização > Modelo de objetos > Utilitários > PropertyLayout > ClassId

Identificador da Classe de uso apenas para otimização de carga

**Exemplo 1: modificação da propriedade ClassId**

```
# carrega objeto PropertyLayout de identificador 1
propertyLayout = PropertyLayout.Carrega(1)
# modifica a propriedade ClassId
propertyLayout.ClassId = 1;
# salva modificação da propriedade ClassId
PropertyLayout.Salva(propertyLayout)
```
