# Interrupcoes

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > Interrupcoes

Interrupções de cronometragem de tempo de atendimento definido em Acordo de Nível de Serviço

**Exemplo 1: percorrer objetos da propriedade Interrupcoes**

```
# carrega objeto OrdemServico de identificador 78
ordemServico = OrdemServico.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if ordemServico != None:
    # percorre objetos da propriedade Interrupcoes e para cada uma escreve conteúdo no log de mensagens
    for interrupcaoSLA in ordemServico.Interrupcoes:
        Utils.LogInformation(interrupcaoSLA.ToString())
```
