# SuperClasseServico (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > SuperClasseServico

class `Venki.Supravizio.Processo.Custom.SuperClasseServico` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_superclasseservico.md

## Propriedades (4)
- SuperClasseServico SuperClasseServicoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- int DomainId {get;set;}

## Métodos (9)
- static SuperClasseServico Load(int id)
- static SuperClasseServico Carrega(int id)
- static SuperClasseServico New()
- static SuperClasseServico Novo()
- static SuperClasseServico Load(string propertyName, object value)
- static SuperClasseServico Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
