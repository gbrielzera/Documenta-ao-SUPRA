# Events

Caminho: Customização > Modelo de objetos > Utilitários > Class > Events

Coleção de Eventos que podem ser customizados para a Classe de Negócio em determinado Domínio. Todos os eventos são implementados por scripts na linguagem Python.

**Exemplo 1: percorrer objetos da propriedade Events**

```
# carrega objeto Class de identificador 94
class = Class.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if class != None:
    # percorre objetos da propriedade Events e para cada uma escreve conteúdo no log de mensagens
    for customEvent in class.Events:
        Utils.LogInformation(customEvent.ToString())
```
