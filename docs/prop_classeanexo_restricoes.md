# Restricoes

Caminho: Customização > Modelo de objetos > Processo > ClasseAnexo > Restricoes

Limita o escopo da regra de associação a Ordens de Serviço cujo campo Serviço ou sua Classe esteja relacionados como Escopo

**Exemplo 1: percorrer objetos da propriedade Restricoes**

```
# carrega objeto ClasseAnexo de identificador 78
classeAnexo = ClasseAnexo.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if classeAnexo != None:
    # percorre objetos da propriedade Restricoes e para cada uma escreve conteúdo no log de mensagens
    for restricaoServicoAnexo in classeAnexo.Restricoes:
        Utils.LogInformation(restricaoServicoAnexo.ToString())
```
