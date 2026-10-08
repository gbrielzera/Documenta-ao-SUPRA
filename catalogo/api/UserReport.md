# UserReport (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Custom > UserReport

class `Venki.Services.Custom.UserReport` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_userreport.md

## Propriedades (16)
- UserReport UserReportInstance {get;}
- int Id {get;set;}
- string Description {get;set;}
- bool Enabled {get;set;}
- DateTime CreationDate {get;set;}
- int CreatorId {get;set;}
- int DomainId {get;set;}
- string LockComment {get;set;}
- int? LockedById {get;set;}
- object ReportLayout {get;set;}
- int? UnlockerId {get;set;}
- SessionProxyList Parameters {get;}
- SessionProxyList Queries {get;}
- User Creator {get;set;}
- User Unlocker {get;set;}
- User LockedBy {get;set;}

## Métodos (11)
- static UserReport Load(int id)
- static UserReport Carrega(int id)
- static UserReport New()
- static UserReport Novo()
- static ReportParam NewReportParam(UserReport parentUserReport)
- static ReportQuery NewReportQuery(UserReport parentUserReport)
- static UserReport Load(string propertyName, object value)
- static UserReport Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
