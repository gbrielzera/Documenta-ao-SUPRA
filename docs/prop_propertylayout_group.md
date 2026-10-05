# Group

Caminho: Customização > Modelo de objetos > Utilitários > PropertyLayout > Group

Nome do Agrupamento. Se não for preenchido considerar como Grupo Principal

**Exemplo 1: modificação da propriedade Group**

```
# carrega objeto PropertyLayout de identificador 1
propertyLayout = PropertyLayout.Carrega(1)
# modifica a propriedade Group
propertyLayout.Group = "Grupo";
# salva modificação da propriedade Group
PropertyLayout.Salva(propertyLayout)
```
