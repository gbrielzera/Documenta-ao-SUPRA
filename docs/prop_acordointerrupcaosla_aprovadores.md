# Aprovadores

Caminho: Customização > Modelo de objetos > Recurso > AcordoInterrupcaoSLA > Aprovadores

Aprovadores para a interrupção. Interrupções sem definição de aprovador são automaticamente aprovadas e consideradas no tempo restante de atendimento.

**Exemplo 1: percorrer objetos da propriedade Aprovadores**

```
# carrega objeto AcordoInterrupcaoSLA de identificador 51
acordoInterrupcaoSLA = AcordoInterrupcaoSLA.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if acordoInterrupcaoSLA != None:
    # percorre objetos da propriedade Aprovadores e para cada uma escreve conteúdo no log de mensagens
    for aprovadorInterrupcao in acordoInterrupcaoSLA.Aprovadores:
        Utils.LogInformation(aprovadorInterrupcao.ToString())
```
