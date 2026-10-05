# SubstitutoId

Caminho: Customização > Modelo de objetos > Recurso > Ausencia > SubstitutoId

Identificador da Pessoa associada

**Exemplo 1: modificação da propriedade SubstitutoId**

```
# carrega objeto Ausencia de identificador 1
ausencia = Ausencia.Carrega(1)
# modifica a propriedade SubstitutoId
ausencia.SubstitutoId = 1;
# salva modificação da propriedade SubstitutoId
Ausencia.Salva(ausencia)
```
