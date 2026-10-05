# OriginalAction

Caminho: Customização > Modelo de objetos > Utilitários > ExceptionClass > OriginalAction

Conteúdo do campo Ação gerado pelo fabricante deste software e disponível para reversão de texto customizado.

**Exemplo 1: modificação da propriedade OriginalAction**

```
# carrega objeto ExceptionClass de identificador 1
exceptionClass = ExceptionClass.Carrega(1)
# modifica a propriedade OriginalAction
exceptionClass.OriginalAction = "Ação original";
# salva modificação da propriedade OriginalAction
ExceptionClass.Salva(exceptionClass)
```
