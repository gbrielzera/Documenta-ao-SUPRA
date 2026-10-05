# Riscos

Caminho: Customização > Modelo de objetos > Processo > SubProcesso > Riscos

Riscos endereçados no Subprocesso. Estes riscos devem ser tratados pelo fluxo e são validados com controles estabelecidos.

**Exemplo 1: percorrer objetos da propriedade Riscos**

```
# carrega objeto SubProcesso de identificador 78
subProcesso = SubProcesso.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if subProcesso != None:
    # percorre objetos da propriedade Riscos e para cada uma escreve conteúdo no log de mensagens
    for riscoProcesso in subProcesso.Riscos:
        Utils.LogInformation(riscoProcesso.ToString())
```
