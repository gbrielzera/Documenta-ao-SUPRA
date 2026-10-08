# InterrupcaoSLA (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > InterrupcaoSLA

class `Venki.Supravizio.Processo.Custom.InterrupcaoSLA` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_interrupcaosla.md

## Propriedades (16)
- InterrupcaoSLA InterrupcaoSLAInstance {get;}
- DateTime DataHoraInicio {get;set;}
- DateTime? DataHoraFim {get;set;}
- int MotivoInterrupcaoId {get;set;}
- int AcordoNivelServicoId {get;set;}
- int OrdemServicoId {get;set;}
- int? TempoInterrupcao {get;set;}
- int? AtividadeGeradoraId {get;set;}
- DateTime? DataHoraFimPrevisto {get;set;}
- int? QuantidadeHorasAvisoFimPrevisto {get;set;}
- string Comentario {get;set;}
- bool EnviouAviso {get;set;}
- string Situacao {get;set;}
- OrdemServico OrdemServico {get;}
- AcordoInterrupcaoSLA AcordoInterrupcaoSLA {get;set;}
- Atividade AtividadeGeradora {get;set;}
