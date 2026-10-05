# Assuntos

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > Assuntos

Assuntos

**Exemplo 1: percorrer objetos da propriedade Assuntos**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if ocorrencia != None:
    # percorre objetos da propriedade Assuntos e para cada uma escreve conteúdo no log de mensagens
    for assuntoAprovacao in ocorrencia.Assuntos:
        Utils.LogInformation(assuntoAprovacao.ToString())
```
