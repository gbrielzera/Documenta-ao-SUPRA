# Itens

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > Itens

Itens do Acordo do Nível de Serviço que define o tempo de atendimento de uma Ordem de Serviço. Para determinar o Acordo de Nível de Serviço o sistema compara a Ordem de Serviço e os vários Critérios de Acordos cujo Cliente possui lotação relacionada (levando-se em conta hierarquia entre Órgãos e parâmetro de incluir sub-áreas de Acordos) são comparados levando-se em consideração aquele que apresenta o menor tempo de atendimento.

**Exemplo 1: percorrer objetos da propriedade Itens**

```
# carrega objeto AcordoNivelServico de identificador 51
acordoNivelServico = AcordoNivelServico.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if acordoNivelServico != None:
    # percorre objetos da propriedade Itens e para cada uma escreve conteúdo no log de mensagens
    for itemSLA in acordoNivelServico.Itens:
        Utils.LogInformation(itemSLA.ToString())
```
