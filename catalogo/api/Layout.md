# Layout (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Portal.Custom > Layout

class `Venki.Supravizio.Portal.Custom.Layout` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (8)
- Layout LayoutInstance {get;}
- int Id {get;set;}
- string TituloTemplate {get;set;}
- int DomainId {get;set;}
- string Disposicao {get;set;}
- bool IsTemplate {get;set;}
- string ModoLayout {get;set;}
- SessionProxyList Paineis {get;}

## Métodos (10)
- static Layout Load(int id)
- static Layout Carrega(int id)
- static Layout New()
- static Layout Novo()
- static Painel NewPainel(Layout parentLayout)
- static Layout Load(string propertyName, object value)
- static Layout Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
