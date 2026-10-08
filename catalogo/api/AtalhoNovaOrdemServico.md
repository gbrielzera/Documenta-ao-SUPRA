# AtalhoNovaOrdemServico (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > AtalhoNovaOrdemServico

class `Venki.Supravizio.Recurso.Custom.AtalhoNovaOrdemServico` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (11)
- AtalhoNovaOrdemServico AtalhoNovaOrdemServicoInstance {get;}
- int Id {get;set;}
- int? GrupoTrabalhoId {get;set;}
- int Seqencia {get;set;}
- int ClasseSubProcessoId {get;set;}
- int? ServicoId {get;set;}
- string Rotulo {get;set;}
- string Assunto {get;set;}
- GrupoTrabalho GrupoTrabalho {get;}
- ClasseSubProcesso ClasseSubProcesso {get;set;}
- Servico Servico {get;set;}

## Métodos (2)
- static AtalhoNovaOrdemServico Load(int id)
- static AtalhoNovaOrdemServico Carrega(int id)
