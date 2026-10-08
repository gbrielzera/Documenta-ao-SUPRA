# Permissao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Portal.Custom > Permissao

class `Venki.Supravizio.Portal.Custom.Permissao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (7)
- Permissao PermissaoInstance {get;}
- int PerfilPortalId {get;set;}
- int Id {get;set;}
- string PermitirVisualizar {get;set;}
- string PermitirEditar {get;set;}
- string PermitirConfigurar {get;set;}
- PerfilPortal PerfilPortal {get;set;}

## Métodos (9)
- static Permissao Load(int id)
- static Permissao Carrega(int id)
- static Permissao New()
- static Permissao Novo()
- static Permissao Load(string propertyName, object value)
- static Permissao Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
