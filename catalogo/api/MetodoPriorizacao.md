# MetodoPriorizacao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > MetodoPriorizacao

class `Venki.Supravizio.Processo.Custom.MetodoPriorizacao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_metodopriorizacao.md

## Propriedades (11)
- MetodoPriorizacao MetodoPriorizacaoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- string ExpressaoCalculo {get;set;}
- int DomainId {get;set;}
- bool CalculoAutomatico {get;set;}
- string Referencia {get;set;}
- bool RestringirMudancaPrioridadeCalculada {get;set;}
- string ClasseNegocio {get;set;}
- SessionProxyList Graus {get;}
- SessionProxyList Variaveis {get;}

## Métodos (12)
- static MetodoPriorizacao Load(int id)
- static MetodoPriorizacao Carrega(int id)
- static MetodoPriorizacao New()
- static MetodoPriorizacao Novo()
- static GrauPrioridade NewGrauPrioridade(MetodoPriorizacao parentMetodoPriorizacao)
- static VariavelPriorizacao NewVariavelPriorizacao(MetodoPriorizacao parentMetodoPriorizacao)
- static EnumeracaoVariavel NewEnumeracaoVariavel(VariavelPriorizacao parentVariavelPriorizacao)
- static MetodoPriorizacao Load(string propertyName, object value)
- static MetodoPriorizacao Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
