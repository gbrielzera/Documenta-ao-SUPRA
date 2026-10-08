# Modelo (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Configuracao.Custom > Modelo

class `Venki.Supravizio.Configuracao.Custom.Modelo` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_modelo.md

## Propriedades (7)
- Modelo ModeloInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- bool Ativo {get;set;}
- int? FabricanteId {get;set;}
- int DomainId {get;set;}
- Fabricante Fabricante {get;set;}

## Métodos (9)
- static Modelo Load(int id)
- static Modelo Carrega(int id)
- static Modelo New()
- static Modelo Novo()
- static Modelo Load(string propertyName, object value)
- static Modelo Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
