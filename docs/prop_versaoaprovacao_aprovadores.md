# Aprovadores

Caminho: Customização > Modelo de objetos > Processo > VersaoAprovacao > Aprovadores

Aprovadores da Versão

**Exemplo 1: percorrer objetos da propriedade Aprovadores**

```
# carrega objeto VersaoAprovacao de identificador 78
versaoAprovacao = VersaoAprovacao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if versaoAprovacao != None:
    # percorre objetos da propriedade Aprovadores e para cada uma escreve conteúdo no log de mensagens
    for aprovacao in versaoAprovacao.Aprovadores:
        Utils.LogInformation(aprovacao.ToString())
```
