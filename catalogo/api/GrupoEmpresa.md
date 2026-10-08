# GrupoEmpresa (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > GrupoEmpresa

class `Venki.Supravizio.Recurso.Custom.GrupoEmpresa` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_grupoempresa.md

## Propriedades (6)
- GrupoEmpresa GrupoEmpresaInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- string Sigla {get;set;}
- bool Ativo {get;set;}
- int DomainId {get;set;}

## Métodos (9)
- static GrupoEmpresa Load(int id)
- static GrupoEmpresa Carrega(int id)
- static GrupoEmpresa New()
- static GrupoEmpresa Novo()
- static GrupoEmpresa Load(string propertyName, object value)
- static GrupoEmpresa Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
