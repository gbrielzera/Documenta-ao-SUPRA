# CriterioChargeBack

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > CriterioChargeBack

Critério para destino de custo no cálculo de Charge-back.

**Exemplo 1: modificação da propriedade CriterioChargeBack**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade CriterioChargeBack
classeConfiguracao.CriterioChargeBack = "Usuario";
# salva modificação da propriedade CriterioChargeBack
ClasseConfiguracao.Salva(classeConfiguracao)
```
