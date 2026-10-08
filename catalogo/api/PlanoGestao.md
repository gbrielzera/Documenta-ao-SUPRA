# PlanoGestao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > PlanoGestao

class `Venki.Supravizio.Processo.Custom.PlanoGestao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_planogestao.md

## Propriedades (8)
- PlanoGestao PlanoGestaoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- DateTime DataInicio {get;set;}
- DateTime DataFim {get;set;}
- bool InformacoesRestritas {get;set;}
- SessionProxyList Indicadores {get;}
- SessionProxyList GruposTrabalhoAutorizados {get;}

## Métodos (12)
- static PlanoGestao Load(int id)
- static PlanoGestao Carrega(int id)
- static PlanoGestao New()
- static PlanoGestao Novo()
- static IndicadorPlano NewIndicadorPlano(PlanoGestao parentPlanoGestao)
- static PeriodoPlano NewPeriodoPlano(IndicadorPlano parentIndicadorPlano)
- static GrupoTrabalhoAutorizado NewGrupoTrabalhoAutorizado(PlanoGestao parentPlanoGestao)
- static PlanoGestao Load(string propertyName, object value)
- static PlanoGestao Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
