# OriginalMessage

Caminho: Customização > Modelo de objetos > Utilitários > ExceptionClass > OriginalMessage

Conteúdo do campo Mensagem gerado pelo fabricante deste software e disponível para reversão de texto customizado.

**Exemplo 1: modificação da propriedade OriginalMessage**

```
# carrega objeto ExceptionClass de identificador 1
exceptionClass = ExceptionClass.Carrega(1)
# modifica a propriedade OriginalMessage
exceptionClass.OriginalMessage = "Mensagem Original";
# salva modificação da propriedade OriginalMessage
ExceptionClass.Salva(exceptionClass)
```
