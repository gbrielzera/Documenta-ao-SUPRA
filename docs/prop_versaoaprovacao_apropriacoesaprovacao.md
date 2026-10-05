# ApropriacoesAprovacao

Caminho: Customização > Modelo de objetos > Processo > VersaoAprovacao > ApropriacoesAprovacao

Versão da Aprovação

**Exemplo 1: percorrer objetos da propriedade ApropriacoesAprovacao**

```
# carrega objeto VersaoAprovacao de identificador 78
versaoAprovacao = VersaoAprovacao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if versaoAprovacao != None:
    # percorre objetos da propriedade ApropriacoesAprovacao e para cada uma escreve conteúdo no log de mensagens
    for apropriacaoAprovacao in versaoAprovacao.ApropriacoesAprovacao:
        Utils.LogInformation(apropriacaoAprovacao.ToString())
```
