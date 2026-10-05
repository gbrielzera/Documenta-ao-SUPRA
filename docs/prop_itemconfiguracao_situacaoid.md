# SituacaoId

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > SituacaoId

Identificador da Situação corrente do Item

**Exemplo 1: modificação da propriedade SituacaoId**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade SituacaoId
itemConfiguracao.SituacaoId = 1;
# salva modificação da propriedade SituacaoId
ItemConfiguracao.Salva(itemConfiguracao)
```
