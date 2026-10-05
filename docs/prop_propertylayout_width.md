# Width

Caminho: Customização > Modelo de objetos > Utilitários > PropertyLayout > Width

Largura em pixels do Controle

**Exemplo 1: modificação da propriedade Width**

```
# carrega objeto PropertyLayout de identificador 1
propertyLayout = PropertyLayout.Carrega(1)
# modifica a propriedade Width
propertyLayout.Width = 1;
# salva modificação da propriedade Width
PropertyLayout.Salva(propertyLayout)
```
