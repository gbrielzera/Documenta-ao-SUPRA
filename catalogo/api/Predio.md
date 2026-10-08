# Predio (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > Predio

class `Venki.Supravizio.Recurso.Custom.Predio` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_predio.md

## Propriedades (6)
- Predio PredioInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- int? UnidadeNegocioId {get;set;}
- SessionProxyList Locais {get;}
- UnidadeNegocio UnidadeNegocio {get;}

## Métodos (2)
- static Predio Load(int id)
- static Predio Carrega(int id)
