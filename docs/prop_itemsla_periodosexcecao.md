# PeriodosExcecao

Caminho: Customização > Modelo de objetos > Recurso > ItemSLA > PeriodosExcecao

Redefinição do tempo de atendimento para períodos de exceção em um mês ou ano.

**Exemplo 1: percorrer objetos da propriedade PeriodosExcecao**

```
# carrega objeto ItemSLA de identificador 51
itemSLA = ItemSLA.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if itemSLA != None:
    # percorre objetos da propriedade PeriodosExcecao e para cada uma escreve conteúdo no log de mensagens
    for excecaoSLA in itemSLA.PeriodosExcecao:
        Utils.LogInformation(excecaoSLA.ToString())
```
