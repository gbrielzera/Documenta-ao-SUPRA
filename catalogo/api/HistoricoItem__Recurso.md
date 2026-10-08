# HistoricoItem (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > HistoricoItem

class `Venki.Supravizio.Recurso.Custom.HistoricoItem` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_historicoitem.md

## Propriedades (11)
- HistoricoItem HistoricoItemInstance {get;}
- int ChargeBackId {get;set;}
- int ItemConfiguracaoId {get;set;}
- decimal? ValorPrecoAquisicao {get;set;}
- decimal? ValorPrecoManutencao {get;set;}
- int? ResponsavelId {get;set;}
- SessionProxyList Usuarios {get;}
- SessionProxyList Componentes {get;}
- ItemConfiguracao ItemConfiguracao {get;set;}
- ChargeBack ChargeBack {get;set;}
- Pessoa Responsavel {get;set;}

## Métodos (9)
- static HistoricoItem New()
- static HistoricoItem Novo()
- static HistoricoUsuario NewHistoricoUsuario(HistoricoItem parentHistoricoItem)
- static HistoricoComponente NewHistoricoComponente(HistoricoItem parentHistoricoItem)
- static HistoricoItem Load(string propertyName, object value)
- static HistoricoItem Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
