# LocalizeEnabled

Caminho: Customização > Modelo de objetos > Utilitários > Class > LocalizeEnabled

Indica que a Classe possui o recurso de localização de objetos ativado. Quando ativado é possível a tradução de propriedades do tipo texto para diversas culturas.

**Exemplo 1: modificação da propriedade LocalizeEnabled**

```
# carrega objeto Class de identificador 1
class = Class.Carrega(1)
# modifica a propriedade LocalizeEnabled
class.LocalizeEnabled = true;
# salva modificação da propriedade LocalizeEnabled
Class.Salva(class)
```
