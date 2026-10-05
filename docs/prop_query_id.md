# Id

Caminho: Customização > Modelo de objetos > Utilitários > Query > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Query

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Query de identificador 1
query = Query.Carrega(1)
# modifica a propriedade Id
query.Id = 1;
# salva modificação da propriedade Id
Query.Salva(query)
```
