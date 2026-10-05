# Gaps

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > Gaps

Gaps encontrados durante teste de um Controle.

**Exemplo 1: percorrer objetos da propriedade Gaps**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if ocorrencia != None:
    # percorre objetos da propriedade Gaps e para cada uma escreve conteúdo no log de mensagens
    for gap in ocorrencia.Gaps:
        Utils.LogInformation(gap.ToString())
```
