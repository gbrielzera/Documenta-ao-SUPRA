# UserSession (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Security.Custom > UserSession

class `Venki.Services.Security.Custom.UserSession` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_usersession.md

## Propriedades (11)
- UserSession UserSessionInstance {get;}
- int UserId {get;}
- DateTime LogonDateTime {get;}
- string SessionId {get;}
- DateTime? LogoutDateTime {get;}
- string ApplicationId {get;}
- int ConnectedUsers {get;}
- string LogoutReason {get;}
- bool RefusedMaxUser {get;set;}
- string LogonType {get;set;}
- User User {get;set;}

## Métodos (7)
- static UserSession New()
- static UserSession Novo()
- static UserSession Load(string propertyName, object value)
- static UserSession Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
