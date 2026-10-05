# Itens

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > Itens

Item a ser avaliado em uma Pesquisa

**Exemplo 1: percorrer objetos da propriedade Itens**

```
# carrega objeto Pesquisa de identificador 78
pesquisa = Pesquisa.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if pesquisa != None:
    # percorre objetos da propriedade Itens e para cada uma escreve conteúdo no log de mensagens
    for itemPesquisa in pesquisa.Itens:
        Utils.LogInformation(itemPesquisa.ToString())
```
