# CamposAprovacao

Caminho: Customização > Modelo de objetos > Processo > OperacaoAtividade > CamposAprovacao

Campos visualizados pelo aprovador na tela de aprovação (somente leitura). Uma vez aprovados estes campos não podem ser modificados pelo atendente.

**Exemplo 1: percorrer objetos da propriedade CamposAprovacao**

```
# carrega objeto OperacaoAtividade de identificador 78
operacaoAtividade = OperacaoAtividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if operacaoAtividade != None:
    # percorre objetos da propriedade CamposAprovacao e para cada uma escreve conteúdo no log de mensagens
    for campoAprovacao in operacaoAtividade.CamposAprovacao:
        Utils.LogInformation(campoAprovacao.ToString())
```
