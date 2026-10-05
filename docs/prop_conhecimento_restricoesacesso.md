# RestricoesAcesso

Caminho: Customização > Modelo de objetos > Ativos > Conhecimento > RestricoesAcesso

Composição entre permissão e conhecimento

**Exemplo 1: percorrer objetos da propriedade RestricoesAcesso**

```
# carrega objeto Conhecimento de identificador 73
conhecimento = Conhecimento.Carrega(73)
# verifica se o objeto foi recuperado com sucesso
if conhecimento != None:
    # percorre objetos da propriedade RestricoesAcesso e para cada uma escreve conteúdo no log de mensagens
    for permissaoConhecimentoPapel in conhecimento.RestricoesAcesso:
        Utils.LogInformation(permissaoConhecimentoPapel.ToString())
```
