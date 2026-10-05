# Atores

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > Atores

Atores

**Exemplo 1: percorrer objetos da propriedade Atores**

```
# carrega objeto ItemConfiguracao de identificador 73
itemConfiguracao = ItemConfiguracao.Carrega(73)
# verifica se o objeto foi recuperado com sucesso
if itemConfiguracao != None:
    # percorre objetos da propriedade Atores e para cada uma escreve conteúdo no log de mensagens
    for atoresItem in itemConfiguracao.Atores:
        Utils.LogInformation(atoresItem.ToString())
```
