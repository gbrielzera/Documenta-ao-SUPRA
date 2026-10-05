# Acoes

Caminho: Customização > Modelo de objetos > Processo > Gap > Acoes

Plano de Ação

**Exemplo 1: percorrer objetos da propriedade Acoes**

```
# carrega objeto Gap de identificador 78
gap = Gap.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if gap != None:
    # percorre objetos da propriedade Acoes e para cada uma escreve conteúdo no log de mensagens
    for acaoGap in gap.Acoes:
        Utils.LogInformation(acaoGap.ToString())
```
