# Visualizacao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > Visualizacao

class `Venki.Supravizio.Recurso.Custom.Visualizacao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (7)
- Visualizacao VisualizacaoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- int? GrupoTrabalhoId {get;set;}
- string LayoutPadraoWorkspace {get;set;}
- SessionProxyList Filtro {get;}
- GrupoTrabalho GrupoTrabalho {get;}

## Métodos (2)
- static Visualizacao Load(int id)
- static Visualizacao Carrega(int id)
