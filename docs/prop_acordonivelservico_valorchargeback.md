# ValorChargeBack

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > ValorChargeBack

Valor para cobrança pela rotina de Charge-back. Se o critério de charge-back for 'Hora' então o valor total é obtido pela multiplicação do 'Valor' pela quantidade de horas apontadas no período de apuração. Se o critério de charge-back for 'Ocorrência' então o total é obtido pela multiplicação do 'Valor' pela quantidade total de ocorrências finalizadas no período de apuração. Para o critério 'ValorFixo' o campo 'Valor' já indica o total de charge-back enquanto nos critérios 'Nenhum' ou 'Formula' não fazem uso desta informação.

**Exemplo 1: modificação da propriedade ValorChargeBack**

```
# carrega objeto AcordoNivelServico de identificador 1
acordoNivelServico = AcordoNivelServico.Carrega(1)
# modifica a propriedade ValorChargeBack
acordoNivelServico.ValorChargeBack = 0;
# salva modificação da propriedade ValorChargeBack
AcordoNivelServico.Salva(acordoNivelServico)
```
