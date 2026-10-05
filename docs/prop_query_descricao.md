# Descricao

Caminho: Customização > Modelo de objetos > Utilitários > Query > Descricao

Descrição detalhada do Query

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto Query de identificador 1
query = Query.Carrega(1)
# modifica a propriedade Descricao
query.Descricao = "Descrição";
# salva modificação da propriedade Descricao
Query.Salva(query)
```
