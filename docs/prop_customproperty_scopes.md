# Scopes

Caminho: Customização > Modelo de objetos > Utilitários > CustomProperty > Scopes

Conjunto de condições que devem ser atendidas pela Ordem de Serviço para que o campo seja visível.

**Exemplo 1: percorrer objetos da propriedade Scopes**

```
# carrega objeto CustomProperty de identificador 94
customProperty = CustomProperty.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if customProperty != None:
    # percorre objetos da propriedade Scopes e para cada uma escreve conteúdo no log de mensagens
    for customPropertyScope in customProperty.Scopes:
        Utils.LogInformation(customPropertyScope.ToString())
```
