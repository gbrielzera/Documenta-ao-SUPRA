# PapelProcesso (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > PapelProcesso

class `Venki.Supravizio.Processo.Custom.PapelProcesso` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_papelprocesso.md

## Propriedades (16)
- PapelProcesso PapelProcessoInstance {get;}
- string Nome {get;set;}
- int DesenhoProcessoId {get;set;}
- string ScriptSelecaoAtores {get;set;}
- int? GrupoTrabalhoId {get;set;}
- int? PessoaId {get;set;}
- int? PapelClasseNegocioId {get;set;}
- int Id {get;set;}
- string Referencia {get;set;}
- bool IncluiCoordenador {get;set;}
- bool ExcluiAprovacoes {get;set;}
- string AtorGrupoTrabalho {get;set;}
- DesenhoProcesso DesenhoProcesso {get;}
- GrupoTrabalho GrupoTrabalho {get;set;}
- Pessoa Pessoa {get;set;}
- PapelClasseNegocio PapelClasseNegocio {get;set;}

## Métodos (2)
- static PapelProcesso Load(int id)
- static PapelProcesso Carrega(int id)
