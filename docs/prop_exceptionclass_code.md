# Code

Caminho: Customização > Modelo de objetos > Utilitários > ExceptionClass > Code

Código identificador do erro.

**Exemplo 1: modificação da propriedade Code**

```
# carrega objeto ExceptionClass de identificador 1
exceptionClass = ExceptionClass.Carrega(1)
# modifica a propriedade Code
exceptionClass.Code = "Código de Erro";
# salva modificação da propriedade Code
ExceptionClass.Salva(exceptionClass)
```
