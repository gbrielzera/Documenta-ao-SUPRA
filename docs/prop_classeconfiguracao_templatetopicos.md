# TemplateTopicos

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > TemplateTopicos

Tópicos que devem ser preenchidos na criação de artigos para a Base de Conhecimento. Quando um artigo é criado todos os tópicos são inicializados com o template.

**Exemplo 1: percorrer objetos da propriedade TemplateTopicos**

```
# carrega objeto ClasseConfiguracao de identificador 73
classeConfiguracao = ClasseConfiguracao.Carrega(73)
# verifica se o objeto foi recuperado com sucesso
if classeConfiguracao != None:
    # percorre objetos da propriedade TemplateTopicos e para cada uma escreve conteúdo no log de mensagens
    for topicoConhecimento in classeConfiguracao.TemplateTopicos:
        Utils.LogInformation(topicoConhecimento.ToString())
```
