# Pagina (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Portal.Custom > Pagina

class `Venki.Supravizio.Portal.Custom.Pagina` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (19)
- Pagina PaginaInstance {get;}
- string Descricao {get;set;}
- bool Habilitado {get;set;}
- decimal PrioridadeSiteMap {get;set;}
- bool ForcarSSL {get;set;}
- DateTime? DataInicio {get;set;}
- DateTime? DataFim {get;set;}
- string Disposicao {get;set;}
- int Id {get;set;}
- string Cultura {get;set;}
- int LayoutId {get;set;}
- int SkinId {get;set;}
- int ReferenciaPaginaId {get;set;}
- string ModoLayout {get;set;}
- SessionProxyList PermissoesPaginas {get;}
- SessionProxyList InstanciasModulo {get;}
- ReferenciaPagina ReferenciaPagina {get;}
- Layout Layout {get;set;}
- Skin Skin {get;set;}

## Métodos (2)
- static Pagina Load(int id)
- static Pagina Carrega(int id)
