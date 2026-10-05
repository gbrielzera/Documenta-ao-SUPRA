# Alternativas

Caminho: Customização > Modelo de objetos > Processo > Gateway > Alternativas

Alternativas

**Exemplo 1: percorrer objetos da propriedade Alternativas**

```
# carrega objeto Gateway de identificador 78
gateway = Gateway.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if gateway != None:
    # percorre objetos da propriedade Alternativas e para cada uma escreve conteúdo no log de mensagens
    for emissor in gateway.Alternativas:
        Utils.LogInformation(emissor.ToString())
```
