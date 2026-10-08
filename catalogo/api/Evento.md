# Evento (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > Evento

class `Venki.Supravizio.Processo.Custom.Evento` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_evento.md

## Propriedades (12)
- Evento EventoInstance {get;}
- string Mensagem {get;set;}
- DateTime DataHoraEvento {get;set;}
- int TipoEventoId {get;set;}
- int ResponsavelId {get;set;}
- int OcorrenciaId {get;set;}
- bool DisponivelAA {get;set;}
- bool PermiteCancelarPublicacaoAA {get;set;}
- string NomeAutor {get;set;}
- Ocorrencia Ocorrencia {get;}
- TipoEvento TipoEvento {get;set;}
- Pessoa Responsavel {get;set;}
