# Action

Caminho: Customização > Modelo de objetos > Utilitários > ExceptionClass > Action

Orientação para o Usuário para resolução do problema. O descritivo da ação pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes)

**Exemplo 1: modificação da propriedade Action**

```
# carrega objeto ExceptionClass de identificador 1
exceptionClass = ExceptionClass.Carrega(1)
# modifica a propriedade Action
exceptionClass.Action = "Ação";
# salva modificação da propriedade Action
ExceptionClass.Salva(exceptionClass)
```
