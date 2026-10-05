# Versoes

Caminho: Customização > Modelo de objetos > Processo > Processo > Versoes

Versões do Processo

**Exemplo 1: percorrer objetos da propriedade Versoes**

```
# carrega objeto Processo de identificador 78
processo = Processo.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if processo != None:
    # percorre objetos da propriedade Versoes e para cada uma escreve conteúdo no log de mensagens
    for desenhoProcesso in processo.Versoes:
        Utils.LogInformation(desenhoProcesso.ToString())
```
