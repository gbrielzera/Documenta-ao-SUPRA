# Questoes

Caminho: Customização > Modelo de objetos > Processo > ClassePesquisaSatisfacao > Questoes

Questões que farão parte da Pesquisa de Satisfação

**Exemplo 1: percorrer objetos da propriedade Questoes**

```
# carrega objeto ClassePesquisaSatisfacao de identificador 78
classePesquisaSatisfacao = ClassePesquisaSatisfacao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if classePesquisaSatisfacao != None:
    # percorre objetos da propriedade Questoes e para cada uma escreve conteúdo no log de mensagens
    for questaoClassePesquisa in classePesquisaSatisfacao.Questoes:
        Utils.LogInformation(questaoClassePesquisa.ToString())
```
