# CamposPreenchimentoAprovacao

Caminho: Customização > Modelo de objetos > Processo > OperacaoAtividade > CamposPreenchimentoAprovacao

Campos exibidos para o aprovador com possibilidade de preenchimento/modificação. Uma vez aprovados estes campos não podem ser modificados pelo atendente.

**Exemplo 1: percorrer objetos da propriedade CamposPreenchimentoAprovacao**

```
# carrega objeto OperacaoAtividade de identificador 78
operacaoAtividade = OperacaoAtividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if operacaoAtividade != None:
    # percorre objetos da propriedade CamposPreenchimentoAprovacao e para cada uma escreve conteúdo no log de mensagens
    for campoPreenchimentoAprovacao in operacaoAtividade.CamposPreenchimentoAprovacao:
        Utils.LogInformation(campoPreenchimentoAprovacao.ToString())
```
