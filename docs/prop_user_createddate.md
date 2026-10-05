# CreatedDate

Caminho: Customização > Modelo de objetos > Utilitários > User > CreatedDate

Data de criação do Usuário.

**Exemplo 1: modificação da propriedade CreatedDate**

```
# carrega objeto User de identificador 1
user = User.Carrega(1)
# modifica a propriedade CreatedDate
user.CreatedDate = DateTime;
# salva modificação da propriedade CreatedDate
User.Salva(user)
```
