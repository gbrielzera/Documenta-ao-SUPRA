# FormId

Caminho: Customização > Modelo de objetos > Utilitários > PropertyLayout > FormId

Identificador do tipo de Formulário

**Exemplo 1: modificação da propriedade FormId**

```
# carrega objeto PropertyLayout de identificador 1
propertyLayout = PropertyLayout.Carrega(1)
# modifica a propriedade FormId
propertyLayout.FormId = 1;
# salva modificação da propriedade FormId
PropertyLayout.Salva(propertyLayout)
```
