# Id

Caminho: Customização > Modelo de objetos > Recurso > Ausencia > Id

Identificador da Ausência

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Ausencia de identificador 1
ausencia = Ausencia.Carrega(1)
# modifica a propriedade Id
ausencia.Id = 1;
# salva modificação da propriedade Id
Ausencia.Salva(ausencia)
```
