# Fatores

Caminho: Customização > Modelo de objetos > Processo > PriorizacaoEntidade > Fatores

Fatores utilizados para cálculo de Prioridade.

**Exemplo 1: percorrer objetos da propriedade Fatores**

```
# carrega objeto PriorizacaoEntidade de identificador 78
priorizacaoEntidade = PriorizacaoEntidade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if priorizacaoEntidade != None:
    # percorre objetos da propriedade Fatores e para cada uma escreve conteúdo no log de mensagens
    for fatorPrioridade in priorizacaoEntidade.Fatores:
        Utils.LogInformation(fatorPrioridade.ToString())
```
