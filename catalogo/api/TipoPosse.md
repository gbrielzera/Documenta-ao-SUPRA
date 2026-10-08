# TipoPosse (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Configuracao.Custom > TipoPosse

class `Venki.Supravizio.Configuracao.Custom.TipoPosse` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_tipoposse.md

## Propriedades (5)
- TipoPosse TipoPosseInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- bool Ativo {get;set;}
- int DomainId {get;set;}

## Métodos (9)
- static TipoPosse Load(int id)
- static TipoPosse Carrega(int id)
- static TipoPosse New()
- static TipoPosse Novo()
- static TipoPosse Load(string propertyName, object value)
- static TipoPosse Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
