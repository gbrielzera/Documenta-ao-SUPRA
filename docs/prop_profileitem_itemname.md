# ItemName

Caminho: Customização > Modelo de objetos > Utilitários > ProfileItem > ItemName

Nome de identificação para o item de Profile

**Exemplo 1: modificação da propriedade ItemName**

```
# carrega objeto ProfileItem de identificador 1
profileItem = ProfileItem.Carrega(1)
# modifica a propriedade ItemName
profileItem.ItemName = "Name";
# salva modificação da propriedade ItemName
ProfileItem.Salva(profileItem)
```
