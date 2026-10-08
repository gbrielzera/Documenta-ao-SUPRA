# QuestaoPesquisa (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > QuestaoPesquisa

class `Venki.Supravizio.Processo.Custom.QuestaoPesquisa` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_questaopesquisa.md

## Propriedades (7)
- QuestaoPesquisa QuestaoPesquisaInstance {get;}
- int Id {get;}
- string Texto {get;set;}
- string Descricao {get;set;}
- bool Ativo {get;set;}
- int GrupoQuestaoId {get;set;}
- GrupoQuestao GrupoQuestao {get;set;}

## Métodos (9)
- static QuestaoPesquisa Load(int id)
- static QuestaoPesquisa Carrega(int id)
- static QuestaoPesquisa New()
- static QuestaoPesquisa Novo()
- static QuestaoPesquisa Load(string propertyName, object value)
- static QuestaoPesquisa Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
