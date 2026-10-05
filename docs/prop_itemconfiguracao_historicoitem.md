# HistoricoItem

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > HistoricoItem

Histórico de modificações em arquivos. Válido apenas para artefatos do tipo arquivo mantido por transferência.

**Exemplo 1: percorrer objetos da propriedade HistoricoItem**

```
# carrega objeto ItemConfiguracao de identificador 73
itemConfiguracao = ItemConfiguracao.Carrega(73)
# verifica se o objeto foi recuperado com sucesso
if itemConfiguracao != None:
    # percorre objetos da propriedade HistoricoItem e para cada uma escreve conteúdo no log de mensagens
    for historicoItem in itemConfiguracao.HistoricoItem:
        Utils.LogInformation(historicoItem.ToString())
```
