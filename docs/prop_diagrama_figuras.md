# Figuras

Caminho: Customização > Modelo de objetos > Processo > Diagrama > Figuras

Figuras que compoem o diagrama

**Exemplo 1: percorrer objetos da propriedade Figuras**

```
# carrega objeto Diagrama de identificador 78
diagrama = Diagrama.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if diagrama != None:
    # percorre objetos da propriedade Figuras e para cada uma escreve conteúdo no log de mensagens
    for figura in diagrama.Figuras:
        Utils.LogInformation(figura.ToString())
```
