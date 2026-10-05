# ClientesAutorizados

Caminho: Customização > Modelo de objetos > Processo > Atividade > ClientesAutorizados

Relação de papéis de processo que definem os clientes autorizados a gerar uma solicitação pelo iniciador.

**Exemplo 1: percorrer objetos da propriedade ClientesAutorizados**

```
# carrega objeto Atividade de identificador 78
atividade = Atividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if atividade != None:
    # percorre objetos da propriedade ClientesAutorizados e para cada uma escreve conteúdo no log de mensagens
    for clienteAutorizado in atividade.ClientesAutorizados:
        Utils.LogInformation(clienteAutorizado.ToString())
```
