# Aprovadores

Caminho: Customização > Modelo de objetos > Processo > OperacaoAtividade > Aprovadores

Lista de papéis que definem as pessoas responsáveis pela aprovação

**Exemplo 1: percorrer objetos da propriedade Aprovadores**

```
# carrega objeto OperacaoAtividade de identificador 78
operacaoAtividade = OperacaoAtividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if operacaoAtividade != None:
    # percorre objetos da propriedade Aprovadores e para cada uma escreve conteúdo no log de mensagens
    for aprovador in operacaoAtividade.Aprovadores:
        Utils.LogInformation(aprovador.ToString())
```
