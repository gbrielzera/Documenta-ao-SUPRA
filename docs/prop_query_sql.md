# SQL

Caminho: Customização > Modelo de objetos > Utilitários > Query > SQL

Texto da consulta SQL editada pelo usuário

**Exemplo 1: modificação da propriedade SQL**

```
# carrega objeto Query de identificador 1
query = Query.Carrega(1)
# modifica a propriedade SQL
query.SQL = "SQL";
# salva modificação da propriedade SQL
Query.Salva(query)
```
