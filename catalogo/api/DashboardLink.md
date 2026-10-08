# DashboardLink (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Custom > DashboardLink

class `Venki.Services.Custom.DashboardLink` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (11)
- DashboardLink DashboardLinkInstance {get;}
- int DashboardId {get;set;}
- int UserId {get;set;}
- DateTime CreateDate {get;set;}
- string GUID {get;set;}
- bool Enabled {get;set;}
- string Title {get;set;}
- string Description {get;set;}
- string ImageUrl {get;set;}
- Dashboard Dashboard {get;set;}
- User User {get;set;}

## Métodos (7)
- static DashboardLink New()
- static DashboardLink Novo()
- static DashboardLink Load(string propertyName, object value)
- static DashboardLink Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
