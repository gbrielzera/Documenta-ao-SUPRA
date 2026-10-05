# Dependencias

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > Dependencias

Itens de configuração que possuem relação de Dependência.

**Exemplo 1: percorrer objetos da propriedade Dependencias**

```
# carrega objeto ItemConfiguracao de identificador 73
itemConfiguracao = ItemConfiguracao.Carrega(73)
# verifica se o objeto foi recuperado com sucesso
if itemConfiguracao != None:
    # percorre objetos da propriedade Dependencias e para cada uma escreve conteúdo no log de mensagens
    for itemDependencia in itemConfiguracao.Dependencias:
        Utils.LogInformation(itemDependencia.ToString())
```
