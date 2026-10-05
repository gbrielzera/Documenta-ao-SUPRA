# UserId

Caminho: Customização > Modelo de objetos > Utilitários > ProfileItem > UserId

Identificador do Usuário

**Exemplo 1: modificação da propriedade UserId**

```
# carrega objeto ProfileItem de identificador 1
profileItem = ProfileItem.Carrega(1)
# modifica a propriedade UserId
profileItem.UserId = 1;
# salva modificação da propriedade UserId
ProfileItem.Salva(profileItem)
```
