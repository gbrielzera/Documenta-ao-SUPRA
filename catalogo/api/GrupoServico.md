# GrupoServico (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > GrupoServico

class `Venki.Supravizio.Processo.Custom.GrupoServico` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_gruposervico.md

## Propriedades (6)
- GrupoServico GrupoServicoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- int DomainId {get;set;}
- int? SuperClasseServicoId {get;set;}
- SuperClasseServico SuperClasseServico {get;set;}

## Métodos (9)
- static GrupoServico Load(int id)
- static GrupoServico Carrega(int id)
- static GrupoServico New()
- static GrupoServico Novo()
- static GrupoServico Load(string propertyName, object value)
- static GrupoServico Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
