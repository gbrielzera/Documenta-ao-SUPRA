# ReferenciaPagina (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Portal.Custom > ReferenciaPagina

class `Venki.Supravizio.Portal.Custom.ReferenciaPagina` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (9)
- ReferenciaPagina ReferenciaPaginaInstance {get;}
- int Id {get;set;}
- int DomainId {get;set;}
- int VersaoPortalId {get;set;}
- string Nome {get;set;}
- string Titulo {get;set;}
- bool IsPaginaPrincipal {get;set;}
- SessionProxyList Paginas {get;}
- VersaoPortal VersaoPortal {get;set;}

## Métodos (13)
- static ReferenciaPagina Load(int id)
- static ReferenciaPagina Carrega(int id)
- static ReferenciaPagina New()
- static ReferenciaPagina Novo()
- static Pagina NewPagina(ReferenciaPagina parentReferenciaPagina)
- static PermissaoPagina NewPermissaoPagina(Pagina parentPagina)
- static InstanciaModulo NewInstanciaModulo(Pagina parentPagina)
- static PermissaoInstanciaModulo NewPermissaoInstanciaModulo(InstanciaModulo parentInstanciaModulo)
- static ReferenciaPagina Load(string propertyName, object value)
- static ReferenciaPagina Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
