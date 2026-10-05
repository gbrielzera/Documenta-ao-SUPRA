# RecursosAplicados

Caminho: Customização > Modelo de objetos > Recurso > Contrato > RecursosAplicados

Grupos de solucionadores previstos na prestação de Serviço.

**Exemplo 1: percorrer objetos da propriedade RecursosAplicados**

```
# carrega objeto Contrato de identificador 51
contrato = Contrato.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if contrato != None:
    # percorre objetos da propriedade RecursosAplicados e para cada uma escreve conteúdo no log de mensagens
    for recursoAplicado in contrato.RecursosAplicados:
        Utils.LogInformation(recursoAplicado.ToString())
```
