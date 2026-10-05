# ClassesDependencias

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > ClassesDependencias

Tipos de Itens de Configuração que podem ser associados como Dependências

**Exemplo 1: percorrer objetos da propriedade ClassesDependencias**

```
# carrega objeto ClasseConfiguracao de identificador 73
classeConfiguracao = ClasseConfiguracao.Carrega(73)
# verifica se o objeto foi recuperado com sucesso
if classeConfiguracao != None:
    # percorre objetos da propriedade ClassesDependencias e para cada uma escreve conteúdo no log de mensagens
    for classeDependencia in classeConfiguracao.ClassesDependencias:
        Utils.LogInformation(classeDependencia.ToString())
```
