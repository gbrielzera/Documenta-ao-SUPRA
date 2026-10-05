# ClassesAprovacao

Caminho: Customização > Modelo de objetos > Processo > OperacaoAtividade > ClassesAprovacao

Tipos de Itens de Configuração que devem ser Anexados na aprovação

**Exemplo 1: percorrer objetos da propriedade ClassesAprovacao**

```
# carrega objeto OperacaoAtividade de identificador 78
operacaoAtividade = OperacaoAtividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if operacaoAtividade != None:
    # percorre objetos da propriedade ClassesAprovacao e para cada uma escreve conteúdo no log de mensagens
    for classeAprovacao in operacaoAtividade.ClassesAprovacao:
        Utils.LogInformation(classeAprovacao.ToString())
```
