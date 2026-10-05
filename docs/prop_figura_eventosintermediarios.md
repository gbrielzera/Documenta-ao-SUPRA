# EventosIntermediarios

Caminho: Customização > Modelo de objetos > Processo > Figura > EventosIntermediarios

Eventos intermediários

**Exemplo 1: percorrer objetos da propriedade EventosIntermediarios**

```
# carrega objeto Figura de identificador 78
figura = Figura.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if figura != None:
    # percorre objetos da propriedade EventosIntermediarios e para cada uma escreve conteúdo no log de mensagens
    for figuraAtividadeEventoIntermediario in figura.EventosIntermediarios:
        Utils.LogInformation(figuraAtividadeEventoIntermediario.ToString())
```
