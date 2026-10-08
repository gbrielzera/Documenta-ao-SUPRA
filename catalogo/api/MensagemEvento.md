# MensagemEvento (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > MensagemEvento

class `Venki.Supravizio.Processo.Custom.MensagemEvento` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_mensagemevento.md

## Propriedades (16)
- MensagemEvento MensagemEventoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- int TipoEventoId {get;set;}
- int? ProcessoId {get;set;}
- int DomainId {get;set;}
- string ScriptMensagem {get;set;}
- int? ModeloComunicadoId {get;set;}
- int? PapelDestinatarioId {get;set;}
- int? Temporalidade {get;set;}
- string ListaDestinatarios {get;set;}
- string EnderecoReply {get;set;}
- TipoEvento TipoEvento {get;}
- Processo Processo {get;set;}
- ModeloComunicado ModeloComunicado {get;set;}
- PapelClasseNegocio PapelDestinatario {get;set;}

## Métodos (2)
- static MensagemEvento Load(int id)
- static MensagemEvento Carrega(int id)
