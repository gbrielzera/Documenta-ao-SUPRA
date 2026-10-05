# Motivos

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > Motivos

Motivos

**Exemplo 1: percorrer objetos da propriedade Motivos**

```
# carrega objeto ClasseApontamento de identificador 78
classeApontamento = ClasseApontamento.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if classeApontamento != None:
    # percorre objetos da propriedade Motivos e para cada uma escreve conteúdo no log de mensagens
    for motivoClasseApontamento in classeApontamento.Motivos:
        Utils.LogInformation(motivoClasseApontamento.ToString())
```
