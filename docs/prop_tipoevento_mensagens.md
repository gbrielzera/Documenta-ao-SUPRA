# Mensagens

Caminho: Customização > Modelo de objetos > Processo > TipoEvento > Mensagens

Template de mensagens que serão enviadas quando ocorrer um Evento deste Tipo

**Exemplo 1: percorrer objetos da propriedade Mensagens**

```
# carrega objeto TipoEvento de identificador 78
tipoEvento = TipoEvento.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if tipoEvento != None:
    # percorre objetos da propriedade Mensagens e para cada uma escreve conteúdo no log de mensagens
    for mensagemEvento in tipoEvento.Mensagens:
        Utils.LogInformation(mensagemEvento.ToString())
```
