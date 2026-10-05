# Parameters

Caminho: Customização > Modelo de objetos > Utilitários > UserReport > Parameters

Parâmetros do relatório

**Exemplo 1: percorrer objetos da propriedade Parameters**

```
# carrega objeto UserReport de identificador 94
userReport = UserReport.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if userReport != None:
    # percorre objetos da propriedade Parameters e para cada uma escreve conteúdo no log de mensagens
    for reportParam in userReport.Parameters:
        Utils.LogInformation(reportParam.ToString())
```
