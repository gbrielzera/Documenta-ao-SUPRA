# UnidadeNegocio (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > UnidadeNegocio

class `Venki.Supravizio.Recurso.Custom.UnidadeNegocio` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_unidadenegocio.md

## Propriedades (13)
- UnidadeNegocio UnidadeNegocioInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- bool Ativo {get;set;}
- string Sigla {get;set;}
- string Localizacao {get;set;}
- int EmpresaId {get;set;}
- int CalendarioId {get;set;}
- int DomainId {get;set;}
- string EnderecoAD {get;set;}
- SessionProxyList Predios {get;}
- Empresa Empresa {get;set;}
- Calendario Calendario {get;set;}

## Métodos (11)
- static UnidadeNegocio Load(int id)
- static UnidadeNegocio Carrega(int id)
- static UnidadeNegocio New()
- static UnidadeNegocio Novo()
- static Predio NewPredio(UnidadeNegocio parentUnidadeNegocio)
- static Local NewLocal(Predio parentPredio)
- static UnidadeNegocio Load(string propertyName, object value)
- static UnidadeNegocio Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
