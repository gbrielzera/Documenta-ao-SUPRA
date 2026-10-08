# Query (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Custom > Query

class `Venki.Services.Custom.Query` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_query.md

## Propriedades (9)
- Query QueryInstance {get;}
- int DomainId {get;set;}
- int Id {get;set;}
- string Descricao {get;set;}
- int UserId {get;set;}
- string SQL {get;set;}
- int? DatabaseConnectionId {get;set;}
- User Creator {get;set;}
- DatabaseConnection DatabaseConnection {get;set;}

## Métodos (9)
- static Query Load(int id)
- static Query Carrega(int id)
- static Query New()
- static Query Novo()
- static Query Load(string propertyName, object value)
- static Query Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
