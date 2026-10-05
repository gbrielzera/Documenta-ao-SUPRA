# ControlUrl

Caminho: Customização > Modelo de objetos > Utilitários > PropertyLayout > ControlUrl

Caminho para carga do Controle em caso de Controles do tipo CustomControl

**Exemplo 1: modificação da propriedade ControlUrl**

```
# carrega objeto PropertyLayout de identificador 1
propertyLayout = PropertyLayout.Carrega(1)
# modifica a propriedade ControlUrl
propertyLayout.ControlUrl = "Caminho Controle";
# salva modificação da propriedade ControlUrl
PropertyLayout.Salva(propertyLayout)
```
