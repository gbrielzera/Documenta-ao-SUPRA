# Transactions

Caminho: Customização > Modelo de objetos > Utilitários > Role > Transactions

Autorizações as transações atribuídos ao Perfil de Acesso.

**Exemplo 1: percorrer objetos da propriedade Transactions**

```
# carrega objeto Role de identificador 94
role = Role.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if role != None:
    # percorre objetos da propriedade Transactions e para cada uma escreve conteúdo no log de mensagens
    for authorization in role.Transactions:
        Utils.LogInformation(authorization.ToString())
```
