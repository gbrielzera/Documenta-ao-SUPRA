# CreatedByUserId

Caminho: Customização > Modelo de objetos > Utilitários > User > CreatedByUserId

Usuário administrador de segurança responsável pela criação do Usuário

**Exemplo 1: modificação da propriedade CreatedByUserId**

```
# carrega objeto User de identificador 1
user = User.Carrega(1)
# modifica a propriedade CreatedByUserId
user.CreatedByUserId = 1;
# salva modificação da propriedade CreatedByUserId
User.Salva(user)
```
