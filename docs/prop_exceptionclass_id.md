# Id

Caminho: Customização > Modelo de objetos > Utilitários > ExceptionClass > Id

Identificador da Exceção

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto ExceptionClass de identificador 1
exceptionClass = ExceptionClass.Carrega(1)
# modifica a propriedade Id
exceptionClass.Id = 1;
# salva modificação da propriedade Id
ExceptionClass.Salva(exceptionClass)
```
