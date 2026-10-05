# Campos

Caminho: Customização > Modelo de objetos > Processo > OperacaoAtividade > Campos

Campos que devem ser preenchidos pelo usuário ou solicitante.

**Exemplo 1: percorrer objetos da propriedade Campos**

```
# carrega objeto OperacaoAtividade de identificador 78
operacaoAtividade = OperacaoAtividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if operacaoAtividade != None:
    # percorre objetos da propriedade Campos e para cada uma escreve conteúdo no log de mensagens
    for campoPreenchimento in operacaoAtividade.Campos:
        Utils.LogInformation(campoPreenchimento.ToString())
```
