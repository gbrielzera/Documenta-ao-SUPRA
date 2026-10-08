# Role (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Security.Custom > Role

class `Venki.Services.Security.Custom.Role` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_role.md

## Propriedades (7)
- Role RoleInstance {get;}
- int Id {get;set;}
- string Name {get;set;}
- string Reference {get;set;}
- int DomainId {get;set;}
- SessionProxyList Transactions {get;}
- Domain Domain {get;set;}

## Métodos (12)
- static Role Load(int id)
- static Role Carrega(int id)
- static Role New()
- static Role Novo()
- static Authorization NewAuthorization(Role parentRole)
- static DataRestriction NewDataRestriction(Authorization parentAuthorization)
- static FieldRestriction NewFieldRestriction(Authorization parentAuthorization)
- static Role Load(string propertyName, object value)
- static Role Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
