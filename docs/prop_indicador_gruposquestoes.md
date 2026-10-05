# GruposQuestoes

Caminho: Customização > Modelo de objetos > Processo > Indicador > GruposQuestoes

Grupos de Questões para Filtro durante a Apuração de Pesquisas de Satisfação

**Exemplo 1: percorrer objetos da propriedade GruposQuestoes**

```
# carrega objeto Indicador de identificador 78
indicador = Indicador.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if indicador != None:
    # percorre objetos da propriedade GruposQuestoes e para cada uma escreve conteúdo no log de mensagens
    for grupoQuestaoIndicador in indicador.GruposQuestoes:
        Utils.LogInformation(grupoQuestaoIndicador.ToString())
```
