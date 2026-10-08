# TipoEvento (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > TipoEvento

class `Venki.Supravizio.Processo.Custom.TipoEvento` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_tipoevento.md

## Propriedades (11)
- TipoEvento TipoEventoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- bool AtivaMensagens {get;set;}
- string Codigo {get;set;}
- string Nome {get;set;}
- int DomainId {get;set;}
- string ExpressaoMensagem {get;set;}
- string ScriptEvento {get;set;}
- string TipoMensagem {get;set;}
- SessionProxyList Mensagens {get;}

## Métodos (10)
- static TipoEvento Load(int id)
- static TipoEvento Carrega(int id)
- static TipoEvento New()
- static TipoEvento Novo()
- static MensagemEvento NewMensagemEvento(TipoEvento parentTipoEvento)
- static TipoEvento Load(string propertyName, object value)
- static TipoEvento Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
