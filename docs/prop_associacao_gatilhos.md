# Gatilhos

Caminho: Customização > Modelo de objetos > Processo > Associacao > Gatilhos

Eventos que são disparados pelo sistema na ocorrência de um determinado Tipo de Evento.

**Exemplo 1: percorrer objetos da propriedade Gatilhos**

```
# carrega objeto Associacao de identificador 78
associacao = Associacao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if associacao != None:
    # percorre objetos da propriedade Gatilhos e para cada uma escreve conteúdo no log de mensagens
    for gatilhoAssociacao in associacao.Gatilhos:
        Utils.LogInformation(gatilhoAssociacao.ToString())
```
