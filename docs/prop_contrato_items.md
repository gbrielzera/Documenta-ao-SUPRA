# Items

Caminho: Customização > Modelo de objetos > Recurso > Contrato > Items

Itens de Configuração mantidos pelo Contrato

**Exemplo 1: percorrer objetos da propriedade Items**

```
# carrega objeto Contrato de identificador 51
contrato = Contrato.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if contrato != None:
    # percorre objetos da propriedade Items e para cada uma escreve conteúdo no log de mensagens
    for contratoItem in contrato.Items:
        Utils.LogInformation(contratoItem.ToString())
```
