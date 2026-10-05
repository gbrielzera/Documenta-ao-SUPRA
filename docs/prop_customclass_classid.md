# ClassId

Caminho: Customização > Modelo de objetos > Utilitários > CustomClass > ClassId

Identificador da Classe

**Exemplo 1: modificação da propriedade ClassId**

```
# carrega objeto CustomClass de identificador 1
customClass = CustomClass.Carrega(1)
# modifica a propriedade ClassId
customClass.ClassId = 1;
# salva modificação da propriedade ClassId
CustomClass.Salva(customClass)
```
