# ItensAnexados

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > ItensAnexados

Itens Anexados

**Exemplo 1: percorrer objetos da propriedade ItensAnexados**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if ocorrencia != None:
    # percorre objetos da propriedade ItensAnexados e para cada uma escreve conteúdo no log de mensagens
    for itemOcorrencia in ocorrencia.ItensAnexados:
        Utils.LogInformation(itemOcorrencia.ToString())
```
