# ItemMenu (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Portal.Custom > ItemMenu

class `Venki.Supravizio.Portal.Custom.ItemMenu` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (14)
- ItemMenu ItemMenuInstance {get;}
- int? PaginaId {get;set;}
- int PosicaoMenu {get;set;}
- int Id {get;set;}
- int? ItemMenuParentId {get;set;}
- string Titulo {get;set;}
- int DomainId {get;set;}
- string RegraRedirecionamento {get;set;}
- int VersaoPortalId {get;set;}
- string UrlImagem {get;set;}
- string ModoLayout {get;set;}
- Pagina Pagina {get;set;}
- ItemMenu ItemMenuParent {get;set;}
- VersaoPortal VersaoPortal {get;set;}

## Métodos (9)
- static ItemMenu Load(int id)
- static ItemMenu Carrega(int id)
- static ItemMenu New()
- static ItemMenu Novo()
- static ItemMenu Load(string propertyName, object value)
- static ItemMenu Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
