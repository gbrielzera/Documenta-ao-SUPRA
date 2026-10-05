# Itens

Caminho: Customização > Modelo de objetos > Recurso > ChargeBackOrgao > Itens

Itens apurados para o Órgão

**Exemplo 1: percorrer objetos da propriedade Itens**

```
# carrega objeto ChargeBackOrgao de identificador 51
chargeBackOrgao = ChargeBackOrgao.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if chargeBackOrgao != None:
    # percorre objetos da propriedade Itens e para cada uma escreve conteúdo no log de mensagens
    for itemChargeBack in chargeBackOrgao.Itens:
        Utils.LogInformation(itemChargeBack.ToString())
```
