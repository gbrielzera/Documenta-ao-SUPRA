# Usuarios

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > Usuarios

Usuários do Item de Configuração

**Exemplo 1: percorrer objetos da propriedade Usuarios**

```
# carrega objeto ItemConfiguracao de identificador 73
itemConfiguracao = ItemConfiguracao.Carrega(73)
# verifica se o objeto foi recuperado com sucesso
if itemConfiguracao != None:
    # percorre objetos da propriedade Usuarios e para cada uma escreve conteúdo no log de mensagens
    for usuarioItem in itemConfiguracao.Usuarios:
        Utils.LogInformation(usuarioItem.ToString())
```
