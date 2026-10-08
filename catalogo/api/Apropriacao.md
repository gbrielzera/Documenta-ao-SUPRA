# Apropriacao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > Apropriacao

class `Venki.Supravizio.Processo.Custom.Apropriacao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_apropriacao.md

## Propriedades (7)
- Apropriacao ApropriacaoInstance {get;}
- int Id {get;set;}
- string Referencia {get;set;}
- int PessoaId {get;set;}
- DateTime DataHoraApropriacao {get;set;}
- SessionProxyList ApontamentosApropriados {get;}
- Pessoa Pessoa {get;set;}

## Métodos (10)
- static Apropriacao Load(int id)
- static Apropriacao Carrega(int id)
- static Apropriacao New()
- static Apropriacao Novo()
- static ApontamentoApropriado NewApontamentoApropriado(Apropriacao parentApropriacao)
- static Apropriacao Load(string propertyName, object value)
- static Apropriacao Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
