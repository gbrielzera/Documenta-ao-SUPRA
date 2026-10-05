# Afirmacoes

Caminho: Customização > Modelo de objetos > Processo > RiscoProcesso > Afirmacoes

Riscos

**Exemplo 1: percorrer objetos da propriedade Afirmacoes**

```
# carrega objeto RiscoProcesso de identificador 78
riscoProcesso = RiscoProcesso.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if riscoProcesso != None:
    # percorre objetos da propriedade Afirmacoes e para cada uma escreve conteúdo no log de mensagens
    for riscoProcessoAfirmacao in riscoProcesso.Afirmacoes:
        Utils.LogInformation(riscoProcessoAfirmacao.ToString())
```
