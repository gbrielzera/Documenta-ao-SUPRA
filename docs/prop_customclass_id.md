# Id

Caminho: Customização > Modelo de objetos > Utilitários > CustomClass > Id

Identificador do Assinante

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto CustomClass de identificador 1
customClass = CustomClass.Carrega(1)
# modifica a propriedade Id
customClass.Id = 1;
# salva modificação da propriedade Id
CustomClass.Salva(customClass)
```
