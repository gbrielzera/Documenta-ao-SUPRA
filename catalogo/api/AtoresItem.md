# AtoresItem (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Configuracao.Custom > AtoresItem

class `Venki.Supravizio.Configuracao.Custom.AtoresItem` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_atoresitem.md

## Propriedades (10)
- AtoresItem AtoresItemInstance {get;}
- int Id {get;set;}
- int PapelClasseNegocioId {get;set;}
- int ItemConfiguracaoId {get;set;}
- int? PapelRedirecionamentoId {get;set;}
- int? PessoaId {get;set;}
- ItemConfiguracao ItemConfiguracao {get;}
- PapelClasseNegocio PapelRedirecionado {get;set;}
- PapelClasseNegocio PapelClasseNegocio {get;set;}
- Pessoa Pessoa {get;set;}

## Métodos (2)
- static AtoresItem Load(int id)
- static AtoresItem Carrega(int id)
