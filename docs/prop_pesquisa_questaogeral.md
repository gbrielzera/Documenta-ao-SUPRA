# QuestaoGeral

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > QuestaoGeral

Questão que é exibida no fim da Pesquisa de Satisfação para obter a satisfação geral do Cliente

**Exemplo 1: modificação da propriedade QuestaoGeral**

```
# carrega objeto Pesquisa de identificador 78
pesquisa = Pesquisa.Carrega(78)
# modifica a propriedade QuestaoGeral
pesquisa.QuestaoGeral = QuestaoPesquisa.Carrega(23);
# salva modificação da propriedade QuestaoGeral
Pesquisa.Salva(pesquisa)
```
