# FieldRestrictions

Caminho: Customização > Modelo de objetos > Utilitários > Authorization > FieldRestrictions

Uma 'Restrição de campo' permite ocultar ou desabilitar um campo de uma tela de listagem ou edição de registros (Cadastros). IMPORTANTE: Uma ação do tipo Ocultar prevalece sobre uma do tipo Desabilitar. Se o usuário possui vários perfis então vale o princípio da restritividade, ou seja, são aplicadas todas as restrições acumuladas entre os diversos perfis atribuídos.

**Exemplo 1: percorrer objetos da propriedade FieldRestrictions**

```
# carrega objeto Authorization de identificador 94
authorization = Authorization.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if authorization != None:
    # percorre objetos da propriedade FieldRestrictions e para cada uma escreve conteúdo no log de mensagens
    for fieldRestriction in authorization.FieldRestrictions:
        Utils.LogInformation(fieldRestriction.ToString())
```
