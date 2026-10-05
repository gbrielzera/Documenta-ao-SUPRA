# Gateways

Caminho: Customização > Modelo de objetos > Processo > SubProcesso > Gateways

Representa uma Decisão ou Merge a ser tomado durante a execução do Processo

**Exemplo 1: percorrer objetos da propriedade Gateways**

```
# carrega objeto SubProcesso de identificador 78
subProcesso = SubProcesso.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if subProcesso != None:
    # percorre objetos da propriedade Gateways e para cada uma escreve conteúdo no log de mensagens
    for gateway in subProcesso.Gateways:
        Utils.LogInformation(gateway.ToString())
```
