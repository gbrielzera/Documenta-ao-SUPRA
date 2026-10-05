# Observacoes

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > Observacoes

Observações a respeito do Item de Configuração

**Exemplo 1: percorrer objetos da propriedade Observacoes**

```
# carrega objeto ItemConfiguracao de identificador 73
itemConfiguracao = ItemConfiguracao.Carrega(73)
# verifica se o objeto foi recuperado com sucesso
if itemConfiguracao != None:
    # percorre objetos da propriedade Observacoes e para cada uma escreve conteúdo no log de mensagens
    for observacaoItem in itemConfiguracao.Observacoes:
        Utils.LogInformation(observacaoItem.ToString())
```
