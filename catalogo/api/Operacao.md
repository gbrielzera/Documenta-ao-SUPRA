# Operacao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > Operacao

class `Venki.Supravizio.Processo.Custom.Operacao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_operacao.md

## Propriedades (5)
- Operacao OperacaoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- string Codigo {get;set;}
- int DomainId {get;set;}

## Métodos (9)
- static Operacao Load(int id)
- static Operacao Carrega(int id)
- static Operacao New()
- static Operacao Novo()
- static Operacao Load(string propertyName, object value)
- static Operacao Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
