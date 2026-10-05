# ClassesComponentes

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > ClassesComponentes

Tipos de Itens de Configuração que podem ser utilizadas como Componentes.

**Exemplo 1: percorrer objetos da propriedade ClassesComponentes**

```
# carrega objeto ClasseConfiguracao de identificador 73
classeConfiguracao = ClasseConfiguracao.Carrega(73)
# verifica se o objeto foi recuperado com sucesso
if classeConfiguracao != None:
    # percorre objetos da propriedade ClassesComponentes e para cada uma escreve conteúdo no log de mensagens
    for classeComponente in classeConfiguracao.ClassesComponentes:
        Utils.LogInformation(classeComponente.ToString())
```
