# HistoricoOrgao

Caminho: Customização > Modelo de objetos > Recurso > ChargeBack > HistoricoOrgao

Histórico de estrutura organizacional na ocasião do processamento do Charge-back.

**Exemplo 1: percorrer objetos da propriedade HistoricoOrgao**

```
# carrega objeto ChargeBack de identificador 51
chargeBack = ChargeBack.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if chargeBack != None:
    # percorre objetos da propriedade HistoricoOrgao e para cada uma escreve conteúdo no log de mensagens
    for historicoOrgao in chargeBack.HistoricoOrgao:
        Utils.LogInformation(historicoOrgao.ToString())
```
