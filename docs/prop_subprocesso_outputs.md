# Outputs

Caminho: Customização > Modelo de objetos > Processo > SubProcesso > Outputs

Parâmetros de Saída de Subprocesso

**Exemplo 1: percorrer objetos da propriedade Outputs**

```
# carrega objeto SubProcesso de identificador 78
subProcesso = SubProcesso.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if subProcesso != None:
    # percorre objetos da propriedade Outputs e para cada uma escreve conteúdo no log de mensagens
    for outputSubProcesso in subProcesso.Outputs:
        Utils.LogInformation(outputSubProcesso.ToString())
```
