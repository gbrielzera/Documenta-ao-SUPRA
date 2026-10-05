# Motivos

Caminho: Customização > Modelo de objetos > Processo > Apontamento > Motivos

Motivos indicados pelo Solucionador no instante do Apontamento

**Exemplo 1: percorrer objetos da propriedade Motivos**

```
# carrega objeto Apontamento de identificador 78
apontamento = Apontamento.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if apontamento != None:
    # percorre objetos da propriedade Motivos e para cada uma escreve conteúdo no log de mensagens
    for motivoApontamento in apontamento.Motivos:
        Utils.LogInformation(motivoApontamento.ToString())
```
