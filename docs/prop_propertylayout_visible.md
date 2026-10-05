# Visible

Caminho: Customização > Modelo de objetos > Utilitários > PropertyLayout > Visible

Indica que o Controle está visível

**Exemplo 1: modificação da propriedade Visible**

```
# carrega objeto PropertyLayout de identificador 1
propertyLayout = PropertyLayout.Carrega(1)
# modifica a propriedade Visible
propertyLayout.Visible = true;
# salva modificação da propriedade Visible
PropertyLayout.Salva(propertyLayout)
```
