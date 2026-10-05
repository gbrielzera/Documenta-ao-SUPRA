# Atores

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > Atores

Atores

**Exemplo 1: percorrer objetos da propriedade Atores**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if ocorrencia != None:
    # percorre objetos da propriedade Atores e para cada uma escreve conteúdo no log de mensagens
    for ator in ocorrencia.Atores:
        Utils.LogInformation(ator.ToString())
```
