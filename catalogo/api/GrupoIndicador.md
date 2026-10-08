# GrupoIndicador (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > GrupoIndicador

class `Venki.Supravizio.Processo.Custom.GrupoIndicador` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_grupoindicador.md

## Propriedades (4)
- GrupoIndicador GrupoIndicadorInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- int DomainId {get;set;}

## Métodos (9)
- static GrupoIndicador Load(int id)
- static GrupoIndicador Carrega(int id)
- static GrupoIndicador New()
- static GrupoIndicador Novo()
- static GrupoIndicador Load(string propertyName, object value)
- static GrupoIndicador Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
