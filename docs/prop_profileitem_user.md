# User

Caminho: Customização > Modelo de objetos > Utilitários > ProfileItem > User

Usuário dono do Profile

**Exemplo 1: modificação da propriedade User**

```
# carrega objeto ProfileItem de identificador 94
profileItem = ProfileItem.Carrega(94)
# modifica a propriedade User
profileItem.User = User.Carrega(57);
# salva modificação da propriedade User
ProfileItem.Salva(profileItem)
```
