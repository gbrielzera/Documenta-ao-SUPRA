# Cause

Caminho: Customização > Modelo de objetos > Utilitários > ExceptionClass > Cause

Descritivo da Causa do Erro. Este descritivo pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes)

**Exemplo 1: modificação da propriedade Cause**

```
# carrega objeto ExceptionClass de identificador 1
exceptionClass = ExceptionClass.Carrega(1)
# modifica a propriedade Cause
exceptionClass.Cause = "Causa";
# salva modificação da propriedade Cause
ExceptionClass.Salva(exceptionClass)
```
