# FluxosSaida

Caminho: Customização > Modelo de objetos > Processo > Atividade > FluxosSaida

Fluxos de Saída para a Atividade

**Exemplo 1: percorrer objetos da propriedade FluxosSaida**

```
# carrega objeto Atividade de identificador 78
atividade = Atividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if atividade != None:
    # percorre objetos da propriedade FluxosSaida e para cada uma escreve conteúdo no log de mensagens
    for fluxoSequencia in atividade.FluxosSaida:
        Utils.LogInformation(fluxoSequencia.ToString())
```
