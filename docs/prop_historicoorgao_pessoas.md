# Pessoas

Caminho: Customização > Modelo de objetos > Recurso > HistoricoOrgao > Pessoas

Pessoas lotadas no Órgão na ocasião da apuração do Charge-back.

**Exemplo 1: percorrer objetos da propriedade Pessoas**

```
# carrega objeto HistoricoOrgao de identificador 51
historicoOrgao = HistoricoOrgao.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if historicoOrgao != None:
    # percorre objetos da propriedade Pessoas e para cada uma escreve conteúdo no log de mensagens
    for historicoPessoa in historicoOrgao.Pessoas:
        Utils.LogInformation(historicoPessoa.ToString())
```
