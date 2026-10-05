# ClassesConfiguracao

Caminho: Customização > Modelo de objetos > Processo > Indicador > ClassesConfiguracao

Tipos ou super tipos de Itens de Configuração utilizados como filtro na recuperação de Ativos. Esta relação só faz sentido para Indicadores apurados a partir da base de dados de Itens de Configuração.

**Exemplo 1: percorrer objetos da propriedade ClassesConfiguracao**

```
# carrega objeto Indicador de identificador 78
indicador = Indicador.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if indicador != None:
    # percorre objetos da propriedade ClassesConfiguracao e para cada uma escreve conteúdo no log de mensagens
    for classeConfiguracaoIndicador in indicador.ClassesConfiguracao:
        Utils.LogInformation(classeConfiguracaoIndicador.ToString())
```
