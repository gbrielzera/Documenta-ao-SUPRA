# ClassesCopia

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > ClassesCopia

Tipos de Itens de Configuração que podem ser utilizadas como redundâncias.

**Exemplo 1: percorrer objetos da propriedade ClassesCopia**

```
# carrega objeto ClasseConfiguracao de identificador 73
classeConfiguracao = ClasseConfiguracao.Carrega(73)
# verifica se o objeto foi recuperado com sucesso
if classeConfiguracao != None:
    # percorre objetos da propriedade ClassesCopia e para cada uma escreve conteúdo no log de mensagens
    for classeCopia in classeConfiguracao.ClassesCopia:
        Utils.LogInformation(classeCopia.ToString())
```
