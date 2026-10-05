# DataHoraProcessamento

Caminho: Customização > Modelo de objetos > Recurso > ChargeBack > DataHoraProcessamento

Data e hora de processamento do Charge-back

**Exemplo 1: modificação da propriedade DataHoraProcessamento**

```
# carrega objeto ChargeBack de identificador 1
chargeBack = ChargeBack.Carrega(1)
# modifica a propriedade DataHoraProcessamento
chargeBack.DataHoraProcessamento = DateTime;
# salva modificação da propriedade DataHoraProcessamento
ChargeBack.Salva(chargeBack)
```
