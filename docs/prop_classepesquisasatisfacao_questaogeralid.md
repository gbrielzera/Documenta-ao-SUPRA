# QuestaoGeralId

Caminho: Customização > Modelo de objetos > Processo > ClassePesquisaSatisfacao > QuestaoGeralId

Identificador da QuestaoPesquisa associada

**Exemplo 1: modificação da propriedade QuestaoGeralId**

```
# carrega objeto ClassePesquisaSatisfacao de identificador 1
classePesquisaSatisfacao = ClassePesquisaSatisfacao.Carrega(1)
# modifica a propriedade QuestaoGeralId
classePesquisaSatisfacao.QuestaoGeralId = 1;
# salva modificação da propriedade QuestaoGeralId
ClassePesquisaSatisfacao.Salva(classePesquisaSatisfacao)
```
