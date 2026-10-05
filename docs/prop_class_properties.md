# Properties

Caminho: Customização > Modelo de objetos > Utilitários > Class > Properties

Propriedades nativas de uma Classe de Negócio.

**Exemplo 1: percorrer objetos da propriedade Properties**

```
# carrega objeto Class de identificador 94
class = Class.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if class != None:
    # percorre objetos da propriedade Properties e para cada uma escreve conteúdo no log de mensagens
    for property in class.Properties:
        Utils.LogInformation(property.ToString())
```
