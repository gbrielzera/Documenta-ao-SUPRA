# Restricoes

Caminho: Customização > Modelo de objetos > Processo > ClasseAprovacao > Restricoes

Restrição de Itens por Serviço ou Tipo de Serviço

**Exemplo 1: percorrer objetos da propriedade Restricoes**

```
# carrega objeto ClasseAprovacao de identificador 78
classeAprovacao = ClasseAprovacao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if classeAprovacao != None:
    # percorre objetos da propriedade Restricoes e para cada uma escreve conteúdo no log de mensagens
    for restricaoServicoAprovacao in classeAprovacao.Restricoes:
        Utils.LogInformation(restricaoServicoAprovacao.ToString())
```
