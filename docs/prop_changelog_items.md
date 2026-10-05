# Items

Caminho: Customização > Modelo de objetos > Utilitários > ChangeLog > Items

Modificação de Propriedades

**Exemplo 1: percorrer objetos da propriedade Items**

```
# carrega objeto ChangeLog de identificador 94
changeLog = ChangeLog.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if changeLog != None:
    # percorre objetos da propriedade Items e para cada uma escreve conteúdo no log de mensagens
    for changeItem in changeLog.Items:
        Utils.LogInformation(changeItem.ToString())
```
