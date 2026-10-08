# TimeSheet (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > TimeSheet

class `Venki.Supravizio.Processo.Custom.TimeSheet` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_timesheet.md

## Propriedades (20)
- TimeSheet TimeSheetInstance {get;}
- DateTime DataHoraInicio {get;set;}
- DateTime DataHoraFim {get;set;}
- int TecnicoId {get;set;}
- DateTime DataHoraApontamento {get;set;}
- DateTime DataHoraAtualizacao {get;set;}
- string Observacao {get;set;}
- int GrupoTrabalhoId {get;set;}
- int DomainId {get;set;}
- int OcorrenciaId {get;set;}
- int? AtividadeId {get;set;}
- int? TipoApontamentoId {get;set;}
- int Sequencial {get;set;}
- int DuracaoMinutos {get;set;}
- bool GeradoGravacao {get;set;}
- Pessoa Tecnico {get;set;}
- GrupoTrabalho GrupoTrabalho {get;set;}
- Ocorrencia Ocorrencia {get;set;}
- Atividade Atividade {get;set;}
- TipoApontamento TipoApontamento {get;set;}

## Métodos (7)
- static TimeSheet New()
- static TimeSheet Novo()
- static TimeSheet Load(string propertyName, object value)
- static TimeSheet Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
