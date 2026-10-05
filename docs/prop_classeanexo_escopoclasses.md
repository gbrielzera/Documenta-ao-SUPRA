# EscopoClasses

Caminho: Customização > Modelo de objetos > Processo > ClasseAnexo > EscopoClasses

Tipos e super tipos de Itens de Configuração que podem ter itens associados. Pelo menos um dos Tipos e/ou Super tipos especificados devem ser atendidas para conformidade com Processo.

**Exemplo 1: percorrer objetos da propriedade EscopoClasses**

```
# carrega objeto ClasseAnexo de identificador 78
classeAnexo = ClasseAnexo.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if classeAnexo != None:
    # percorre objetos da propriedade EscopoClasses e para cada uma escreve conteúdo no log de mensagens
    for escopoClasseAnexo in classeAnexo.EscopoClasses:
        Utils.LogInformation(escopoClasseAnexo.ToString())
```
