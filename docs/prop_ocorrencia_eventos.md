# Eventos

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > Eventos

Eventos de uma Ocorrência de Processo

**Exemplo 1: percorrer objetos da propriedade Eventos**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if ocorrencia != None:
    # percorre objetos da propriedade Eventos e para cada uma escreve conteúdo no log de mensagens
    for evento in ocorrencia.Eventos:
        Utils.LogInformation(evento.ToString())
```
