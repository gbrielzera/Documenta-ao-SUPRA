# User (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Security.Custom > User

class `Venki.Services.Security.Custom.User` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_user.md

## Propriedades (10)
- string Password {get;set;}
- User UserInstance {get;}
- int Id {get;set;}
- string Username {get;set;}
- DateTime CreatedDate {get;}
- int CreatedByUserId {get;}
- int DomainId {get;}
- SessionProxyList Roles {get;}
- SessionProxyList Tokens {get;}
- Domain Domain {get;set;}

## Métodos (11)
- static User Load(int id)
- static User Carrega(int id)
- static User New()
- static User Novo()
- static MemberOf NewMemberOf(User parentUser)
- static TokenWS NewTokenWS(User parentUser)
- static User Load(string propertyName, object value)
- static User Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
