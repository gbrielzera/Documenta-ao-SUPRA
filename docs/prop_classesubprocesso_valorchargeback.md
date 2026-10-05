# ValorChargeBack

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > ValorChargeBack

Valor para cobrança pela rotina de Charge-back. Se o critério de charge-back for 'Hora' então o valor total é obtido pela multiplicação do 'Valor' pela quantidade de horas apontadas no período de apuração. Se o critério de charge-back for 'Ocorrência' então o total é obtido pela multiplicação do 'Valor' pela quantidade total de ocorrências finalizadas no período de apuração.

**Exemplo 1: modificação da propriedade ValorChargeBack**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade ValorChargeBack
classeSubProcesso.ValorChargeBack = 0;
# salva modificação da propriedade ValorChargeBack
ClasseSubProcesso.Salva(classeSubProcesso)
```
