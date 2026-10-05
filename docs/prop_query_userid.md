# UserId

Caminho: Customização > Modelo de objetos > Utilitários > Query > UserId

Identificador do usuário criador da consulta

**Exemplo 1: modificação da propriedade UserId**

```
# carrega objeto Query de identificador 1
query = Query.Carrega(1)
# modifica a propriedade UserId
query.UserId = 1;
# salva modificação da propriedade UserId
Query.Salva(query)
```
