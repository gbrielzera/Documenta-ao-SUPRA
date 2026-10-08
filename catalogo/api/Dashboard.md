# Dashboard (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Custom > Dashboard

class `Venki.Services.Custom.Dashboard` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (6)
- Dashboard DashboardInstance {get;}
- int DomainId {get;set;}
- int Id {get;set;}
- object Data {get;set;}
- string Title {get;set;}
- SessionProxyList Queries {get;}

## Métodos (10)
- static Dashboard Load(int id)
- static Dashboard Carrega(int id)
- static Dashboard New()
- static Dashboard Novo()
- static DashboardQuery NewDashboardQuery(Dashboard parentDashboard)
- static Dashboard Load(string propertyName, object value)
- static Dashboard Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
