# Emissor (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > Emissor

class `Venki.Supravizio.Processo.Custom.Emissor` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_emissor.md

## Propriedades (15)
- Emissor EmissorInstance {get;}
- int? AtividadeId {get;set;}
- int Id {get;set;}
- int GatewayId {get;set;}
- string ValorComparacaoDecision {get;set;}
- string ReferenciaDecision {get;set;}
- int SequenciaAvaliacao {get;set;}
- int? GatewaySaidaId {get;set;}
- string RotuloMotivo {get;set;}
- bool MotivoObrigatorio {get;set;}
- bool PublicarRespostaAA {get;set;}
- bool PermiteCancelarPubAA {get;set;}
- Gateway Gateway {get;}
- Atividade Atividade {get;set;}
- Gateway GatewaySaida {get;set;}

## Métodos (2)
- static Emissor Load(int id)
- static Emissor Carrega(int id)
