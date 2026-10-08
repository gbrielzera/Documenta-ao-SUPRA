# DatabaseConnection (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Custom > DatabaseConnection

class `Venki.Services.Custom.DatabaseConnection` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_databaseconnection.md

## Propriedades (7)
- DatabaseConnection DatabaseConnectionInstance {get;}
- int Id {get;set;}
- bool Enabled {get;set;}
- string Shortname {get;set;}
- string ConnectionString {get;set;}
- string ConnectionStringASCII {get;set;}
- string Type {get;set;}

## Métodos (9)
- static DatabaseConnection Load(int id)
- static DatabaseConnection Carrega(int id)
- static DatabaseConnection New()
- static DatabaseConnection Novo()
- static DatabaseConnection Load(string propertyName, object value)
- static DatabaseConnection Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
