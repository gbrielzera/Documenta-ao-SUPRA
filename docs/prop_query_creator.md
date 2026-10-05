# Creator

Caminho: Customização > Modelo de objetos > Utilitários > Query > Creator

Usuário que criou a consulta SQL

**Exemplo 1: modificação da propriedade Creator**

```
# carrega objeto Query de identificador 94
query = Query.Carrega(94)
# modifica a propriedade Creator
query.Creator = User.Carrega(57);
# salva modificação da propriedade Creator
Query.Salva(query)
```
