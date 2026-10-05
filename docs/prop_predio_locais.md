# Locais

Caminho: Customização > Modelo de objetos > Recurso > Predio > Locais

Locais

**Exemplo 1: percorrer objetos da propriedade Locais**

```
# carrega objeto Predio de identificador 51
predio = Predio.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if predio != None:
    # percorre objetos da propriedade Locais e para cada uma escreve conteúdo no log de mensagens
    for local in predio.Locais:
        Utils.LogInformation(local.ToString())
```
