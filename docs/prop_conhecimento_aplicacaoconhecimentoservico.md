# AplicacaoConhecimentoServico

Caminho: Customização > Modelo de objetos > Ativos > Conhecimento > AplicacaoConhecimentoServico

Regras de utilização do artigo em função de Serviços e Tipos de Serviços. Estas regras influenciarão o mecanismo de recuperação de artigos durante a busca manual ou automática.

**Exemplo 1: percorrer objetos da propriedade AplicacaoConhecimentoServico**

```
# carrega objeto Conhecimento de identificador 73
conhecimento = Conhecimento.Carrega(73)
# verifica se o objeto foi recuperado com sucesso
if conhecimento != None:
    # percorre objetos da propriedade AplicacaoConhecimentoServico e para cada uma escreve conteúdo no log de mensagens
    for aplicacaoConhecimentoServico in conhecimento.AplicacaoConhecimentoServico:
        Utils.LogInformation(aplicacaoConhecimentoServico.ToString())
```
