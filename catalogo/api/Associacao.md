# Associacao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > Associacao

class `Venki.Supravizio.Processo.Custom.Associacao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_associacao.md

## Propriedades (16)
- Associacao AssociacaoInstance {get;}
- int Id {get;}
- bool Ativo {get;set;}
- int ClasseFonteId {get;set;}
- int ClasseAlvoId {get;set;}
- string FraseAssociacao {get;set;}
- string FraseInversaAssociacao {get;set;}
- int DomainId {get;set;}
- string Nome {get;set;}
- string SeparadorSequencial {get;set;}
- bool IncluirSubniveisSeparador {get;set;}
- string CardinalidadeFonte {get;set;}
- string CardinalidadeAlvo {get;set;}
- SessionProxyList Gatilhos {get;}
- ClasseSubProcesso ClasseAlvo {get;set;}
- ClasseSubProcesso ClasseFonte {get;set;}

## Métodos (11)
- static Associacao Load(int id)
- static Associacao Carrega(int id)
- static Associacao New()
- static Associacao Novo()
- static GatilhoAssociacao NewGatilhoAssociacao(Associacao parentAssociacao)
- static Associacao Load(string propertyName, object value)
- static Associacao Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
- void AssociaOcorrencias(Ocorrencia fonte, Ocorrencia alvo)
