# Propriedade Inputs

Caminho: Propriedade Inputs

Parâmetros de Entrada do Sub-Processo

**Exemplo 1: percorrer objetos da propriedade Inputs**

```
# carrega objeto SubProcesso de identificador 85
subProcesso = SubProcesso.Carrega(85)
# verifica se o objeto foi recuperado com sucesso
if subProcesso != None:
    # percorre objetos da propriedade Inputs e para cada uma escreve conteúdo no log de mensagens
    for inputSubProcesso in subProcesso.Inputs:
        Utils.LogInformation(inputSubProcesso.ToString())
```
