# Calendario (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > Calendario

class `Venki.Supravizio.Recurso.Custom.Calendario` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_calendario.md

## Propriedades (6)
- Calendario CalendarioInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- int DomainId {get;set;}
- SessionProxyList Feriados {get;}
- SessionProxyList PeriodosUteis {get;}

## Métodos (12)
- static Calendario Load(int id)
- static Calendario Carrega(int id)
- static Calendario New()
- static Calendario Novo()
- static Feriado NewFeriado(Calendario parentCalendario)
- static PeriodoUtil NewPeriodoUtil(Calendario parentCalendario)
- static Calendario Load(string propertyName, object value)
- static Calendario Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
- int ObtemTempoUtil(DateTime dataHoraInicio, DateTime dataHoraFim, ArrayList interrupcoes)
