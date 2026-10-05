# SubProcessos

Caminho: Customização > Modelo de objetos > Processo > DesenhoProcesso > SubProcessos

Subprocesso

**Exemplo 1: percorrer objetos da propriedade SubProcessos**

```
# carrega objeto DesenhoProcesso de identificador 78
desenhoProcesso = DesenhoProcesso.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if desenhoProcesso != None:
    # percorre objetos da propriedade SubProcessos e para cada uma escreve conteúdo no log de mensagens
    for subProcesso in desenhoProcesso.SubProcessos:
        Utils.LogInformation(subProcesso.ToString())
```
