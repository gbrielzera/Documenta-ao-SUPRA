# VersaoAprovacao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > VersaoAprovacao

class `Venki.Supravizio.Processo.Custom.VersaoAprovacao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_versaoaprovacao.md

## Propriedades (19)
- VersaoAprovacao VersaoAprovacaoInstance {get;}
- int AssuntoAprovacaoId {get;}
- int Versao {get;}
- DateTime DataHoraCriacao {get;}
- DateTime? DataHoraInicio {get;}
- DateTime? DataHoraFim {get;}
- string Escopo {get;set;}
- DateTime? InterrupcaoSLADataHoraInicio {get;set;}
- int? InterrupcaoSLAMotivoInterrupcaoId {get;set;}
- int? InterrupcaoSLAAcordoNivelServicoId {get;set;}
- int? InterrupcaoSLAOrdemServicoId {get;set;}
- int PassoCorrente {get;set;}
- DateTime DataHoraUltimoComunicado {get;set;}
- string Situacao {get;set;}
- SessionProxyList Aprovadores {get;}
- SessionProxyList ItensAprovacao {get;}
- SessionProxyList ApropriacoesAprovacao {get;}
- AssuntoAprovacao AssuntoAprovacao {get;}
- InterrupcaoSLA InterrupcaoSLA {get;set;}
