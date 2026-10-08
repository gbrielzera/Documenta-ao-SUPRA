# GrupoQuestao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > GrupoQuestao

class `Venki.Supravizio.Processo.Custom.GrupoQuestao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_grupoquestao.md

## Propriedades (5)
- GrupoQuestao GrupoQuestaoInstance {get;}
- int DomainId {get;}
- int Id {get;}
- string Descricao {get;set;}
- SessionProxyList Escore {get;}

## Métodos (10)
- static GrupoQuestao Load(int id)
- static GrupoQuestao Carrega(int id)
- static GrupoQuestao New()
- static GrupoQuestao Novo()
- static Escore NewEscore(GrupoQuestao parentGrupoQuestao)
- static GrupoQuestao Load(string propertyName, object value)
- static GrupoQuestao Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
