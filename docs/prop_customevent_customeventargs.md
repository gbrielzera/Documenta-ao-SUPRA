# CustomEventArgs

Caminho: Customização > Modelo de objetos > Utilitários > CustomEvent > CustomEventArgs

Parâmetros fornecidos pelo mecanismo de invocação de eventos. Estes argumentos, somente leitura, podem ser utilizados para customização de regras de negócio em classes do sistema.

**Exemplo 1: percorrer objetos da propriedade CustomEventArgs**

```
# carrega objeto CustomEvent de identificador 94
customEvent = CustomEvent.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if customEvent != None:
    # percorre objetos da propriedade CustomEventArgs e para cada uma escreve conteúdo no log de mensagens
    for customEventArgs in customEvent.CustomEventArgs:
        Utils.LogInformation(customEventArgs.ToString())
```
