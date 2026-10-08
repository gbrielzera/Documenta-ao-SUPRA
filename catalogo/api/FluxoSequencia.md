# FluxoSequencia (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > FluxoSequencia

class `Venki.Supravizio.Processo.Custom.FluxoSequencia` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_fluxosequencia.md

## Propriedades (7)
- FluxoSequencia FluxoSequenciaInstance {get;}
- int Id {get;set;}
- int? AtividadeOrigemId {get;set;}
- int AtividadeDestinoId {get;set;}
- bool AcopladoOrigem {get;set;}
- Atividade AtividadeOrigem {get;}
- Atividade AtividadeDestino {get;set;}

## Métodos (2)
- static FluxoSequencia Load(int id)
- static FluxoSequencia Carrega(int id)
