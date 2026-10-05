# Areas

Caminho: Customização > Modelo de objetos > Recurso > ChargeBack > Areas

Itens apurados para o Charge-back

**Exemplo 1: percorrer objetos da propriedade Areas**

```
# carrega objeto ChargeBack de identificador 51
chargeBack = ChargeBack.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if chargeBack != None:
    # percorre objetos da propriedade Areas e para cada uma escreve conteúdo no log de mensagens
    for chargeBackOrgao in chargeBack.Areas:
        Utils.LogInformation(chargeBackOrgao.ToString())
```
