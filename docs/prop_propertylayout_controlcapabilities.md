# ControlCapabilities

Caminho: Customização > Modelo de objetos > Utilitários > PropertyLayout > ControlCapabilities

Recursos disponíveis para o Controle. Exemplos: UpperCase para controles TextBox. O recurso é variável de acordo com o Controle.

**Exemplo 1: modificação da propriedade ControlCapabilities**

```
# carrega objeto PropertyLayout de identificador 1
propertyLayout = PropertyLayout.Carrega(1)
# modifica a propriedade ControlCapabilities
propertyLayout.ControlCapabilities = "Recursos grupo";
# salva modificação da propriedade ControlCapabilities
PropertyLayout.Salva(propertyLayout)
```
