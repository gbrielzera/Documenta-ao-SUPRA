# SLA

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > SLA

ANS calculado para Ordem de Serviço

**Exemplo 1: percorrer objetos da propriedade SLA**

```
# carrega objeto OrdemServico de identificador 78
ordemServico = OrdemServico.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if ordemServico != None:
    # percorre objetos da propriedade SLA e para cada uma escreve conteúdo no log de mensagens
    for sLAOrdemServico in ordemServico.SLA:
        Utils.LogInformation(sLAOrdemServico.ToString())
```
