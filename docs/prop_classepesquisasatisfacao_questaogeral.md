# QuestaoGeral

Caminho: Customização > Modelo de objetos > Processo > ClassePesquisaSatisfacao > QuestaoGeral

Questão que é exibida no fim da Pesquisa de Satisfação para obter a satisfação geral do Cliente

**Exemplo 1: modificação da propriedade QuestaoGeral**

```
# carrega objeto ClassePesquisaSatisfacao de identificador 78
classePesquisaSatisfacao = ClassePesquisaSatisfacao.Carrega(78)
# modifica a propriedade QuestaoGeral
classePesquisaSatisfacao.QuestaoGeral = QuestaoPesquisa.Carrega(23);
# salva modificação da propriedade QuestaoGeral
ClassePesquisaSatisfacao.Salva(classePesquisaSatisfacao)
```
