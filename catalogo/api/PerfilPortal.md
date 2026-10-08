# PerfilPortal (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Portal.Custom > PerfilPortal

class `Venki.Supravizio.Portal.Custom.PerfilPortal` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (8)
- PerfilPortal PerfilPortalInstance {get;}
- int Id {get;set;}
- string Nome {get;set;}
- int? PapelClasseNegocioId {get;set;}
- int DomainId {get;set;}
- int VersaoPortalId {get;set;}
- PapelClasseNegocio PapelClasseNegocio {get;set;}
- VersaoPortal VersaoPortal {get;set;}

## Métodos (9)
- static PerfilPortal Load(int id)
- static PerfilPortal Carrega(int id)
- static PerfilPortal New()
- static PerfilPortal Novo()
- static PerfilPortal Load(string propertyName, object value)
- static PerfilPortal Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
