# FormulaChargeBack

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > FormulaChargeBack

Fórmula para cálculo de Charge-back em um determinado mês. Se o critério de Charge-back for 'Fórmula' ou 'ValorFixo' então esta fórmula é executada uma única vez e deve retornar o valor para Charge-back no período, caso contrário é executada para todo item calculado e permite a modificação do valor calculado inicialmente pelo sistema.

**Exemplo 1: modificação da propriedade FormulaChargeBack**

```
# carrega objeto AcordoNivelServico de identificador 1
acordoNivelServico = AcordoNivelServico.Carrega(1)
# modifica a propriedade FormulaChargeBack
acordoNivelServico.FormulaChargeBack = "Fórmula";
# salva modificação da propriedade FormulaChargeBack
AcordoNivelServico.Salva(acordoNivelServico)
```
