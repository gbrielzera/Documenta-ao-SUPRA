# ValorChargeBack

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > ValorChargeBack

Valor para cobrança pela rotina de Charge-back.

**Exemplo 1: modificação da propriedade ValorChargeBack**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade ValorChargeBack
ordemServico.ValorChargeBack = 0;
# salva modificação da propriedade ValorChargeBack
OrdemServico.Salva(ordemServico)
```
