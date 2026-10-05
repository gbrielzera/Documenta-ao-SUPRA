# EscopoClasses

Caminho: Customização > Modelo de objetos > Processo > ClasseAprovacao > EscopoClasses

Tipos e Super tipos de Itens de Configuração que podem ter itens associados na solicitação de aprovação. Pelo menos uma dos Tipos e/ou Super tipos especificados devem ser atendidos para conformidade com Processo.

**Exemplo 1: percorrer objetos da propriedade EscopoClasses**

```
# carrega objeto ClasseAprovacao de identificador 78
classeAprovacao = ClasseAprovacao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if classeAprovacao != None:
    # percorre objetos da propriedade EscopoClasses e para cada uma escreve conteúdo no log de mensagens
    for escopoClasseAprovacao in classeAprovacao.EscopoClasses:
        Utils.LogInformation(escopoClasseAprovacao.ToString())
```
