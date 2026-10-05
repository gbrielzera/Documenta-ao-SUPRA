# Componentes

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > Componentes

Componentes de um Item de Configuração

**Exemplo 1: percorrer objetos da propriedade Componentes**

```
# carrega objeto ItemConfiguracao de identificador 73
itemConfiguracao = ItemConfiguracao.Carrega(73)
# verifica se o objeto foi recuperado com sucesso
if itemConfiguracao != None:
    # percorre objetos da propriedade Componentes e para cada uma escreve conteúdo no log de mensagens
    for itemComponente in itemConfiguracao.Componentes:
        Utils.LogInformation(itemComponente.ToString())
```
