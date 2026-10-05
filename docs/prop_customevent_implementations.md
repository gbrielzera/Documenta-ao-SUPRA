# Implementations

Caminho: Customização > Modelo de objetos > Utilitários > CustomEvent > Implementations

Implementações do Evento. Cada implementação está associada a um Domínio.

**Exemplo 1: percorrer objetos da propriedade Implementations**

```
# carrega objeto CustomEvent de identificador 94
customEvent = CustomEvent.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if customEvent != None:
    # percorre objetos da propriedade Implementations e para cada uma escreve conteúdo no log de mensagens
    for customEventImplementation in customEvent.Implementations:
        Utils.LogInformation(customEventImplementation.ToString())
```
