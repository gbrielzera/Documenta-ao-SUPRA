# ChargeBackId

Caminho: Customização > Modelo de objetos > Recurso > HistoricoItem > ChargeBackId

Identificador do processamento de Charge-back que gerou o histórico.

**Exemplo 1: modificação da propriedade ChargeBackId**

```
# carrega objeto HistoricoItem de identificador 1
historicoItem = HistoricoItem.Carrega(1)
# modifica a propriedade ChargeBackId
historicoItem.ChargeBackId = 1;
# salva modificação da propriedade ChargeBackId
HistoricoItem.Salva(historicoItem)
```
