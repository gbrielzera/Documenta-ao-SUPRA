# FatorPrioridade

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > FatorPrioridade

Fator utilizado para cálculo de Prioridade em Ocorrências.

**Exemplo 1: modificação da propriedade FatorPrioridade**

```
# carrega objeto ItemConfiguracao de identificador 73
itemConfiguracao = ItemConfiguracao.Carrega(73)
# modifica a propriedade FatorPrioridade
itemConfiguracao.FatorPrioridade = FatorPrioridade.Carrega(91);
# salva modificação da propriedade FatorPrioridade
ItemConfiguracao.Salva(itemConfiguracao)
```
