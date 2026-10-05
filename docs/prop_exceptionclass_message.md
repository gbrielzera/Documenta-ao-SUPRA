# Message

Caminho: Customização > Modelo de objetos > Utilitários > ExceptionClass > Message

Mensagem que é exibida para o usuário na ocorrência do erro. Esta mensagem pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes)

**Exemplo 1: modificação da propriedade Message**

```
# carrega objeto ExceptionClass de identificador 1
exceptionClass = ExceptionClass.Carrega(1)
# modifica a propriedade Message
exceptionClass.Message = "Mensagem";
# salva modificação da propriedade Message
ExceptionClass.Salva(exceptionClass)
```
