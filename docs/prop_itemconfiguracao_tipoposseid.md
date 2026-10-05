# TipoPosseId

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > TipoPosseId

Identificador do Tipo de Posse

**Exemplo 1: modificação da propriedade TipoPosseId**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade TipoPosseId
itemConfiguracao.TipoPosseId = 1;
# salva modificação da propriedade TipoPosseId
ItemConfiguracao.Salva(itemConfiguracao)
```
