# Roles

Caminho: Customização > Modelo de objetos > Utilitários > User > Roles

Perfis de acesso do Usuário

**Exemplo 1: percorrer objetos da propriedade Roles**

```
# carrega objeto User de identificador 94
user = User.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if user != None:
    # percorre objetos da propriedade Roles e para cada uma escreve conteúdo no log de mensagens
    for memberOf in user.Roles:
        Utils.LogInformation(memberOf.ToString())
```
