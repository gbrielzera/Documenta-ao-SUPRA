# Local (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > Local

class `Venki.Supravizio.Recurso.Custom.Local` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_local.md

## Propriedades (6)
- Local LocalInstance {get;}
- int PredioId {get;set;}
- int Id {get;set;}
- string Complemento {get;set;}
- bool Ativo {get;set;}
- Predio Predio {get;}

## Métodos (4)
- static Local Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(string propertyName, object value)
- static Local Load(int id)
- static Local Carrega(int id)
