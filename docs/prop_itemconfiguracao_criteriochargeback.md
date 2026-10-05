# CriterioChargeBack

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > CriterioChargeBack

Critério para destino de custo no cálculo de Charge-back.

**Exemplo 1: modificação da propriedade CriterioChargeBack**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade CriterioChargeBack
itemConfiguracao.CriterioChargeBack = "Responsavel";
# salva modificação da propriedade CriterioChargeBack
ItemConfiguracao.Salva(itemConfiguracao)
```
