# ClassId

Caminho: Customização > Modelo de objetos > Utilitários > ExceptionClass > ClassId

Identificador da Classe associada

**Exemplo 1: modificação da propriedade ClassId**

```
# carrega objeto ExceptionClass de identificador 1
exceptionClass = ExceptionClass.Carrega(1)
# modifica a propriedade ClassId
exceptionClass.ClassId = 1;
# salva modificação da propriedade ClassId
ExceptionClass.Salva(exceptionClass)
```
