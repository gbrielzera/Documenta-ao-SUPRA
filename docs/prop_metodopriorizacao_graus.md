# Graus

Caminho: Customização > Modelo de objetos > Processo > MetodoPriorizacao > Graus

Graus de Pririodade

**Exemplo 1: percorrer objetos da propriedade Graus**

```
# carrega objeto MetodoPriorizacao de identificador 78
metodoPriorizacao = MetodoPriorizacao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if metodoPriorizacao != None:
    # percorre objetos da propriedade Graus e para cada uma escreve conteúdo no log de mensagens
    for grauPrioridade in metodoPriorizacao.Graus:
        Utils.LogInformation(grauPrioridade.ToString())
```
