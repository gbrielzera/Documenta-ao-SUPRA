# DataRestrictions

Caminho: Customização > Modelo de objetos > Utilitários > Authorization > DataRestrictions

Uma 'Restrição de registro' permite filtrar os registros que são exibidos em uma transação de Cadastro. Todas as restrições formam uma única expressão montada com o operador lógico AND, ou seja, são recuperados e disponibilizados para edição os registros que atendam TODAS as restrições de registro. Se o usuário possui vários perfis vale sempre o princípio da restritividade, ou seja, todas as restrições são acumuladas entre todos os perfis atribuídos.

**Exemplo 1: percorrer objetos da propriedade DataRestrictions**

```
# carrega objeto Authorization de identificador 94
authorization = Authorization.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if authorization != None:
    # percorre objetos da propriedade DataRestrictions e para cada uma escreve conteúdo no log de mensagens
    for dataRestriction in authorization.DataRestrictions:
        Utils.LogInformation(dataRestriction.ToString())
```
