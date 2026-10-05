# Afirmacoes

Caminho: Customização > Modelo de objetos > Processo > Risco > Afirmacoes

Afirmações Financeiras relacionadas com o Risco

**Exemplo 1: percorrer objetos da propriedade Afirmacoes**

```
# carrega objeto Risco de identificador 78
risco = Risco.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if risco != None:
    # percorre objetos da propriedade Afirmacoes e para cada uma escreve conteúdo no log de mensagens
    for riscoAfirmacao in risco.Afirmacoes:
        Utils.LogInformation(riscoAfirmacao.ToString())
```
