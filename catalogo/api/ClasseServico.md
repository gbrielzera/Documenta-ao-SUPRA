# ClasseServico (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > ClasseServico

class `Venki.Supravizio.Processo.Custom.ClasseServico` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_classeservico.md

## Propriedades (10)
- ClasseServico ClasseServicoInstance {get;}
- string Descricao {get;set;}
- bool Ativo {get;set;}
- int DomainId {get;}
- int Id {get;set;}
- int? FatorPrioridadeId {get;set;}
- string Sigla {get;set;}
- int? GrupoServicoId {get;set;}
- FatorPrioridade FatorPrioridade {get;set;}
- GrupoServico GrupoServico {get;set;}

## Métodos (10)
- static ClasseServico Load(int id)
- static ClasseServico Carrega(int id)
- static ClasseServico New()
- static ClasseServico Novo()
- static ClasseServico Load(string propertyName, object value)
- static ClasseServico Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
- int ObtemValorFatorPrioridade(int valorDefault)
