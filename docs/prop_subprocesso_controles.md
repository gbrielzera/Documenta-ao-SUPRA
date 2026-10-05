# Controles

Caminho: Customização > Modelo de objetos > Processo > SubProcesso > Controles

Controles utilizados para mitigar os Riscos de um Subprocesso.

**Exemplo 1: percorrer objetos da propriedade Controles**

```
# carrega objeto SubProcesso de identificador 78
subProcesso = SubProcesso.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if subProcesso != None:
    # percorre objetos da propriedade Controles e para cada uma escreve conteúdo no log de mensagens
    for controle in subProcesso.Controles:
        Utils.LogInformation(controle.ToString())
```
