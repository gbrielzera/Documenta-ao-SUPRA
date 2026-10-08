# License (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Custom > License

class `Venki.Services.Custom.License` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_license.md

## Propriedades (6)
- License LicenseInstance {get;}
- int Id {get;set;}
- string Data {get;}
- string Owner {get;set;}
- DateTime RegisterDate {get;set;}
- int DomainId {get;set;}

## Métodos (9)
- static License Load(int id)
- static License Carrega(int id)
- static License New()
- static License Novo()
- static License Load(string propertyName, object value)
- static License Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
