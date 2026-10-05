# ItensAprovacao

Caminho: Customização > Modelo de objetos > Processo > VersaoAprovacao > ItensAprovacao

Itens para Aprovação

**Exemplo 1: percorrer objetos da propriedade ItensAprovacao**

```
# carrega objeto VersaoAprovacao de identificador 78
versaoAprovacao = VersaoAprovacao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if versaoAprovacao != None:
    # percorre objetos da propriedade ItensAprovacao e para cada uma escreve conteúdo no log de mensagens
    for itemAprovacao in versaoAprovacao.ItensAprovacao:
        Utils.LogInformation(itemAprovacao.ToString())
```
