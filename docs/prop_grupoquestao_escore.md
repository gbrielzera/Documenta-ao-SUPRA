# Escore

Caminho: Customização > Modelo de objetos > Processo > GrupoQuestao > Escore

Escore de Questão

**Exemplo 1: percorrer objetos da propriedade Escore**

```
# carrega objeto GrupoQuestao de identificador 78
grupoQuestao = GrupoQuestao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if grupoQuestao != None:
    # percorre objetos da propriedade Escore e para cada uma escreve conteúdo no log de mensagens
    for escore in grupoQuestao.Escore:
        Utils.LogInformation(escore.ToString())
```
