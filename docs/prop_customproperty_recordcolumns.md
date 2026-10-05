# RecordColumns

Caminho: Customização > Modelo de objetos > Utilitários > CustomProperty > RecordColumns

Listagem de colunas do registro

**Exemplo 1: percorrer objetos da propriedade RecordColumns**

```
# carrega objeto CustomProperty de identificador 94
customProperty = CustomProperty.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if customProperty != None:
    # percorre objetos da propriedade RecordColumns e para cada uma escreve conteúdo no log de mensagens
    for recordColumn in customProperty.RecordColumns:
        Utils.LogInformation(recordColumn.ToString())
```
