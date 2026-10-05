# CriterioChargeBack

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > CriterioChargeBack

Forma de cálculo de Charge-back para o Acordo de Nivel de Serviço.

**Exemplo 1: modificação da propriedade CriterioChargeBack**

```
# carrega objeto AcordoNivelServico de identificador 1
acordoNivelServico = AcordoNivelServico.Carrega(1)
# modifica a propriedade CriterioChargeBack
acordoNivelServico.CriterioChargeBack = "Nenhum";
# salva modificação da propriedade CriterioChargeBack
AcordoNivelServico.Salva(acordoNivelServico)
```
