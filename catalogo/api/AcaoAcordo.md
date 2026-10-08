# AcaoAcordo (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > AcaoAcordo

class `Venki.Supravizio.Processo.Custom.AcaoAcordo` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_acaoacordo.md

## Propriedades (14)
- AcaoAcordo AcaoAcordoInstance {get;}
- int Id {get;set;}
- int? PapelProcessoId {get;set;}
- int? ModeloComunicadoId {get;set;}
- int AtividadeId {get;set;}
- decimal Percentual {get;set;}
- int? Temporalidade {get;set;}
- string CodigoGrupoANO {get;set;}
- int? CategoriaId {get;set;}
- string Acao {get;set;}
- Atividade Atividade {get;}
- PapelProcesso PapelProcesso {get;set;}
- ModeloComunicado ModeloComunicado {get;set;}
- Categoria Categoria {get;set;}

## Métodos (2)
- static AcaoAcordo Load(int id)
- static AcaoAcordo Carrega(int id)
