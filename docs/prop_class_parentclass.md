# ParentClass

Caminho: Customização > Modelo de objetos > Utilitários > Class > ParentClass

Classe Pai

**Exemplo 1: modificação da propriedade ParentClass**

```
# carrega objeto Class de identificador 94
class = Class.Carrega(94)
# modifica a propriedade ParentClass
class.ParentClass = Class.Carrega(57);
# salva modificação da propriedade ParentClass
Class.Salva(class)
```
