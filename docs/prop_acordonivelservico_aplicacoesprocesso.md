# AplicacoesProcesso

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > AplicacoesProcesso

Processos em que o Acordo de Nível de Serviço será aplicado.

**Exemplo 1: percorrer objetos da propriedade AplicacoesProcesso**

```
# carrega objeto AcordoNivelServico de identificador 51
acordoNivelServico = AcordoNivelServico.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if acordoNivelServico != None:
    # percorre objetos da propriedade AplicacoesProcesso e para cada uma escreve conteúdo no log de mensagens
    for aplicacaoProcesso in acordoNivelServico.AplicacoesProcesso:
        Utils.LogInformation(aplicacaoProcesso.ToString())
```
