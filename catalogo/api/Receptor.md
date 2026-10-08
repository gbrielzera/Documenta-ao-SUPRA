# Receptor (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > Receptor

class `Venki.Supravizio.Processo.Custom.Receptor` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_receptor.md

## Propriedades (8)
- Receptor ReceptorInstance {get;}
- int? AtividadeId {get;set;}
- int Id {get;set;}
- int GatewayId {get;set;}
- int? GatewayEntradaId {get;set;}
- Gateway Gateway {get;}
- Atividade Atividade {get;set;}
- Gateway GatewayEntrada {get;set;}

## Métodos (2)
- static Receptor Load(int id)
- static Receptor Carrega(int id)
