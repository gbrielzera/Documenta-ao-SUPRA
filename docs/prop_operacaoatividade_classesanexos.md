# ClassesAnexos

Caminho: Customização > Modelo de objetos > Processo > OperacaoAtividade > ClassesAnexos

Tipos de Itens de Configuração que devem ser anexados na Ordem Serviço.

**Exemplo 1: percorrer objetos da propriedade ClassesAnexos**

```
# carrega objeto OperacaoAtividade de identificador 78
operacaoAtividade = OperacaoAtividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if operacaoAtividade != None:
    # percorre objetos da propriedade ClassesAnexos e para cada uma escreve conteúdo no log de mensagens
    for classeAnexo in operacaoAtividade.ClassesAnexos:
        Utils.LogInformation(classeAnexo.ToString())
```
