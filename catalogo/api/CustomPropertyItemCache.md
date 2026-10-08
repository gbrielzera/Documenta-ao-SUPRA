# CustomPropertyItemCache (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Dictionary.Custom > CustomPropertyItemCache

class `Venki.Services.Dictionary.Custom.CustomPropertyItemCache` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (7)
- CustomPropertyItemCache CustomPropertyItemCacheInstance {get;}
- int DomainId {get;set;}
- int Id {get;set;}
- string Name {get;set;}
- string Value {get;set;}
- string Text {get;set;}
- string ColumnName {get;set;}

## Métodos (9)
- static CustomPropertyItemCache Load(int id)
- static CustomPropertyItemCache Carrega(int id)
- static CustomPropertyItemCache New()
- static CustomPropertyItemCache Novo()
- static CustomPropertyItemCache Load(string propertyName, object value)
- static CustomPropertyItemCache Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
