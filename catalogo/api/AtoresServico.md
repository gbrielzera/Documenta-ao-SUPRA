# AtoresServico (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > AtoresServico

class `Venki.Supravizio.Processo.Custom.AtoresServico` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_atoresservico.md

## Propriedades (10)
- AtoresServico AtoresServicoInstance {get;}
- int ServicoId {get;set;}
- int PapelClasseNegocioId {get;set;}
- int? PapelRedirecionamentoId {get;set;}
- int Id {get;set;}
- int? PessoaId {get;set;}
- Servico Servico {get;}
- PapelClasseNegocio PapelClasseNegocio {get;set;}
- PapelClasseNegocio PapelRedirecionado {get;set;}
- Pessoa Pessoa {get;set;}

## Métodos (2)
- static AtoresServico Load(int id)
- static AtoresServico Carrega(int id)
