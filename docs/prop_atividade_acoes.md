# Acoes

Caminho: Customização > Modelo de objetos > Processo > Atividade > Acoes

Ações configuradas em função do prazo do Acordo de Nível Operacional.

**Exemplo 1: percorrer objetos da propriedade Acoes**

```
# carrega objeto Atividade de identificador 78
atividade = Atividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if atividade != None:
    # percorre objetos da propriedade Acoes e para cada uma escreve conteúdo no log de mensagens
    for acaoAcordo in atividade.Acoes:
        Utils.LogInformation(acaoAcordo.ToString())
```
