# CategoriaControleId

Caminho: Customização > Modelo de objetos > Processo > ClasseControle > CategoriaControleId

Identificador da Categoria

**Exemplo 1: modificação da propriedade CategoriaControleId**

```
# carrega objeto ClasseControle de identificador 1
classeControle = ClasseControle.Carrega(1)
# modifica a propriedade CategoriaControleId
classeControle.CategoriaControleId = 1;
# salva modificação da propriedade CategoriaControleId
ClasseControle.Salva(classeControle)
```
