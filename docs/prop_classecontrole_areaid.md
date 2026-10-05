# AreaId

Caminho: Customização > Modelo de objetos > Processo > ClasseControle > AreaId

Identificador da Área

**Exemplo 1: modificação da propriedade AreaId**

```
# carrega objeto ClasseControle de identificador 1
classeControle = ClasseControle.Carrega(1)
# modifica a propriedade AreaId
classeControle.AreaId = 1;
# salva modificação da propriedade AreaId
ClasseControle.Salva(classeControle)
```
