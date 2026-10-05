# ItemConfiguracao

Caminho: Customização > Modelo de objetos > Recurso > HistoricoItem > ItemConfiguracao

Item de Configuração

**Exemplo 1: modificação da propriedade ItemConfiguracao**

```
# carrega objeto HistoricoItem de identificador 51
historicoItem = HistoricoItem.Carrega(51)
# modifica a propriedade ItemConfiguracao
historicoItem.ItemConfiguracao = ItemConfiguracao.Carrega(94);
# salva modificação da propriedade ItemConfiguracao
HistoricoItem.Salva(historicoItem)
```
