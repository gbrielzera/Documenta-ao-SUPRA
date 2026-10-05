# Variaveis

Caminho: Customização > Modelo de objetos > Processo > MetodoPriorizacao > Variaveis

Variáveis utilizada para compor a Prioridade da Ocorrência.

**Exemplo 1: percorrer objetos da propriedade Variaveis**

```
# carrega objeto MetodoPriorizacao de identificador 78
metodoPriorizacao = MetodoPriorizacao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if metodoPriorizacao != None:
    # percorre objetos da propriedade Variaveis e para cada uma escreve conteúdo no log de mensagens
    for variavelPriorizacao in metodoPriorizacao.Variaveis:
        Utils.LogInformation(variavelPriorizacao.ToString())
```
