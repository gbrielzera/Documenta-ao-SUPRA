# FatorPrioridadeId

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > FatorPrioridadeId

Identificador do(a) FatorPrioridade associado(a)

**Exemplo 1: modificação da propriedade FatorPrioridadeId**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade FatorPrioridadeId
itemConfiguracao.FatorPrioridadeId = 1;
# salva modificação da propriedade FatorPrioridadeId
ItemConfiguracao.Salva(itemConfiguracao)
```
