# Orgao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > Orgao

class `Venki.Supravizio.Recurso.Custom.Orgao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_orgao.md

## Propriedades (12)
- Orgao OrgaoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- string Sigla {get;set;}
- bool Ativo {get;set;}
- int? GestorId {get;set;}
- int DomainId {get;set;}
- int? OrgaoPaiId {get;set;}
- int EmpresaId {get;set;}
- Pessoa Gestor {get;set;}
- Orgao OrgaoPai {get;set;}
- Empresa Empresa {get;set;}

## Métodos (13)
- static SessionProxyList ObtemTodosGestores()
- static Orgao Load(int id)
- static Orgao Carrega(int id)
- static Orgao New()
- static Orgao Novo()
- static Orgao Load(string propertyName, object value)
- static Orgao Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
- SessionProxyList ObtemSubOrgaos(bool recursivo)
- SessionProxyList ObtemOrgaosPais()
- SessionProxyList ObtemColaboradores(bool incluSubniveis, bool somenteGestores, bool excluiGestores)
