# ExecucaoAtividade (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > ExecucaoAtividade

class `Venki.Supravizio.Processo.Custom.ExecucaoAtividade` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_execucaoatividade.md

## Propriedades (34)
- ExecucaoAtividade ExecucaoAtividadeInstance {get;}
- int OcorrenciaId {get;set;}
- int AtividadeId {get;set;}
- DateTime DataHoraInicio {get;set;}
- DateTime? DataHoraFim {get;set;}
- int? TecnicoFinalId {get;set;}
- int TecnicoInicialId {get;set;}
- int Sequencial {get;set;}
- string Relatorio {get;set;}
- bool AvancouAutomatico {get;set;}
- string Aviso {get;set;}
- string OrigemAviso {get;set;}
- bool? FinalizadorAtendePapel {get;set;}
- bool Cancelado {get;set;}
- string JustificativaIndicacaoANO {get;set;}
- int? ResponsavelANOId {get;set;}
- int? IndicadorResponsavelId {get;set;}
- int? TempoANORealizado {get;set;}
- int? TempoANOPrevisto {get;set;}
- DateTime? DataHoraIndicacaoResponsavel {get;set;}
- int? TempoExecucaoSegundos {get;set;}
- int? TempoExecucaoDias {get;set;}
- string NomeTecnicoFinal {get;set;}
- string NomeTecnicoInicial {get;set;}
- int? TempoExecucaoLiquidoSegundos {get;set;}
- int? TempoExecucaoLiquidosDias {get;set;}
- int? TempoANORealizadoSegundos {get;set;}
- SessionProxyList TemposANO {get;}
- Ocorrencia Ocorrencia {get;}
- Pessoa ResponsavelANO {get;set;}
- Pessoa TecnicoFinal {get;set;}
- Pessoa IndicadorResponsavel {get;set;}
- Pessoa TecnicoInicial {get;set;}
- Atividade Atividade {get;set;}
