# ClassePesquisaSatisfacao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > ClassePesquisaSatisfacao

class `Venki.Supravizio.Processo.Custom.ClassePesquisaSatisfacao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_classepesquisasatisfacao.md

## Propriedades (10)
- ClassePesquisaSatisfacao ClassePesquisaSatisfacaoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- bool Ativo {get;set;}
- int? PercentualEnvio {get;set;}
- string ExpressaoPercentualEnvio {get;set;}
- int DomainId {get;set;}
- int? QuestaoGeralId {get;}
- SessionProxyList Questoes {get;}
- QuestaoPesquisa QuestaoGeral {get;set;}

## Métodos (10)
- static ClassePesquisaSatisfacao Load(int id)
- static ClassePesquisaSatisfacao Carrega(int id)
- static ClassePesquisaSatisfacao New()
- static ClassePesquisaSatisfacao Novo()
- static QuestaoClassePesquisa NewQuestaoClassePesquisa(ClassePesquisaSatisfacao parentClassePesquisaSatisfacao)
- static ClassePesquisaSatisfacao Load(string propertyName, object value)
- static ClassePesquisaSatisfacao Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
