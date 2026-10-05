# Effect

Caminho: Customização > Modelo de objetos > Utilitários > ExceptionClass > Effect

Efeito que o Erro possa ter provocado no sistema. O descritivo do efeito pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes)

**Exemplo 1: modificação da propriedade Effect**

```
# carrega objeto ExceptionClass de identificador 1
exceptionClass = ExceptionClass.Carrega(1)
# modifica a propriedade Effect
exceptionClass.Effect = "Efeito";
# salva modificação da propriedade Effect
ExceptionClass.Salva(exceptionClass)
```
