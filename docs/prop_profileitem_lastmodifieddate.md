# LastModifiedDate

Caminho: Customização > Modelo de objetos > Utilitários > ProfileItem > LastModifiedDate

Data de última modificação

**Exemplo 1: modificação da propriedade LastModifiedDate**

```
# carrega objeto ProfileItem de identificador 1
profileItem = ProfileItem.Carrega(1)
# modifica a propriedade LastModifiedDate
profileItem.LastModifiedDate = DateTime;
# salva modificação da propriedade LastModifiedDate
ProfileItem.Salva(profileItem)
```
