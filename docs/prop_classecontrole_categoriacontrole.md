# CategoriaControle

Caminho: Customização > Modelo de objetos > Processo > ClasseControle > CategoriaControle

Categoria de Riscos e Controles

**Exemplo 1: modificação da propriedade CategoriaControle**

```
# carrega objeto ClasseControle de identificador 78
classeControle = ClasseControle.Carrega(78)
# modifica a propriedade CategoriaControle
classeControle.CategoriaControle = CategoriaRisco.Carrega(23);
# salva modificação da propriedade CategoriaControle
ClasseControle.Salva(classeControle)
```
