# Enabled

Caminho: Customização > Modelo de objetos > Utilitários > PropertyLayout > Enabled

Indica que o Controle está ativo

**Exemplo 1: modificação da propriedade Enabled**

```
# carrega objeto PropertyLayout de identificador 1
propertyLayout = PropertyLayout.Carrega(1)
# modifica a propriedade Enabled
propertyLayout.Enabled = true;
# salva modificação da propriedade Enabled
PropertyLayout.Salva(propertyLayout)
```
