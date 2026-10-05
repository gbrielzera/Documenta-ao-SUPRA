# OriginalCause

Caminho: Customização > Modelo de objetos > Utilitários > ExceptionClass > OriginalCause

Conteúdo do campo Causa gerado pelo fabricante deste software e disponível para reversão de texto customizado.

**Exemplo 1: modificação da propriedade OriginalCause**

```
# carrega objeto ExceptionClass de identificador 1
exceptionClass = ExceptionClass.Carrega(1)
# modifica a propriedade OriginalCause
exceptionClass.OriginalCause = "Causa original";
# salva modificação da propriedade OriginalCause
ExceptionClass.Salva(exceptionClass)
```
