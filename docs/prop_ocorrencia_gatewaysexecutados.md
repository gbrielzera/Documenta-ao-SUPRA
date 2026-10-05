# GatewaysExecutados

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > GatewaysExecutados

Execução Gateway

**Exemplo 1: percorrer objetos da propriedade GatewaysExecutados**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if ocorrencia != None:
    # percorre objetos da propriedade GatewaysExecutados e para cada uma escreve conteúdo no log de mensagens
    for execucaoGateway in ocorrencia.GatewaysExecutados:
        Utils.LogInformation(execucaoGateway.ToString())
```
