# ChargeBack

Caminho: Customização > Modelo de objetos > Recurso > HistoricoItem > ChargeBack

Cobrança por uso de Ativo ou serviço prestado.

**Exemplo 1: modificação da propriedade ChargeBack**

```
# carrega objeto HistoricoItem de identificador 51
historicoItem = HistoricoItem.Carrega(51)
# modifica a propriedade ChargeBack
historicoItem.ChargeBack = ChargeBack.Carrega(94);
# salva modificação da propriedade ChargeBack
HistoricoItem.Salva(historicoItem)
```
