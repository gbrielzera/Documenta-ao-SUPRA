# Copias

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > Copias

Redundâncias existentes do Ativo.

**Exemplo 1: percorrer objetos da propriedade Copias**

```
# carrega objeto ItemConfiguracao de identificador 73
itemConfiguracao = ItemConfiguracao.Carrega(73)
# verifica se o objeto foi recuperado com sucesso
if itemConfiguracao != None:
    # percorre objetos da propriedade Copias e para cada uma escreve conteúdo no log de mensagens
    for itemCopia in itemConfiguracao.Copias:
        Utils.LogInformation(itemCopia.ToString())
```
