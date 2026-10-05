# TypeFullName

Caminho: Customização > Modelo de objetos > Utilitários > CustomClass > TypeFullName

Nome completo da Classe .NET incluindo Nome da Classe, Assembly, Culture e Public Token

**Exemplo 1: modificação da propriedade TypeFullName**

```
# carrega objeto CustomClass de identificador 1
customClass = CustomClass.Carrega(1)
# modifica a propriedade TypeFullName
customClass.TypeFullName = "Nome Tipo";
# salva modificação da propriedade TypeFullName
CustomClass.Salva(customClass)
```
