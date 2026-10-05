# AssociacoesSubprocesso

Caminho: Customização > Modelo de objetos > Processo > Atividade > AssociacoesSubprocesso

Associações entre Subprocessos em iniciadores do tipo LinkInicial que originarão novas Ocorrências associadas

**Exemplo 1: percorrer objetos da propriedade AssociacoesSubprocesso**

```
# carrega objeto Atividade de identificador 78
atividade = Atividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if atividade != None:
    # percorre objetos da propriedade AssociacoesSubprocesso e para cada uma escreve conteúdo no log de mensagens
    for associacaoSubprocesso in atividade.AssociacoesSubprocesso:
        Utils.LogInformation(associacaoSubprocesso.ToString())
```
