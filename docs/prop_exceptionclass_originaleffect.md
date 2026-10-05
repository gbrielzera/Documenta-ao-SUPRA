# OriginalEffect

Caminho: Customização > Modelo de objetos > Utilitários > ExceptionClass > OriginalEffect

Conteúdo do campo Efeito gerado pelo fabricante deste software e disponível para reversão de texto customizado.

**Exemplo 1: modificação da propriedade OriginalEffect**

```
# carrega objeto ExceptionClass de identificador 1
exceptionClass = ExceptionClass.Carrega(1)
# modifica a propriedade OriginalEffect
exceptionClass.OriginalEffect = "Efeito original";
# salva modificação da propriedade OriginalEffect
ExceptionClass.Salva(exceptionClass)
```
