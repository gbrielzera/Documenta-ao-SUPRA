# Area

Caminho: Customização > Modelo de objetos > Processo > ClasseControle > Area

Área

**Exemplo 1: modificação da propriedade Area**

```
# carrega objeto ClasseControle de identificador 78
classeControle = ClasseControle.Carrega(78)
# modifica a propriedade Area
classeControle.Area = AreaRisco.Carrega(23);
# salva modificação da propriedade Area
ClasseControle.Salva(classeControle)
```
