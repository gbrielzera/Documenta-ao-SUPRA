# Entradas

Caminho: Customização > Modelo de objetos > Processo > Gateway > Entradas

Atividades de Entrada

**Exemplo 1: percorrer objetos da propriedade Entradas**

```
# carrega objeto Gateway de identificador 78
gateway = Gateway.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if gateway != None:
    # percorre objetos da propriedade Entradas e para cada uma escreve conteúdo no log de mensagens
    for receptor in gateway.Entradas:
        Utils.LogInformation(receptor.ToString())
```
