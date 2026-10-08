# Tecnico (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > Tecnico

class `Venki.Supravizio.Recurso.Custom.Tecnico` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_tecnico.md

## Propriedades (17)
- Tecnico TecnicoInstance {get;}
- int GrupoTrabalhoId {get;set;}
- int PessoaId {get;set;}
- bool Ativo {get;set;}
- int Id {get;set;}
- DateTime DataHoraAssociacao {get;set;}
- DateTime? DataHoraDesativacao {get;set;}
- bool AlertaSolucionadoresGrupo {get;set;}
- int? CalendarioId {get;set;}
- bool AutorizacaoCoordenador {get;set;}
- int? OrdemServicoId {get;set;}
- DateTime? DataHoraGravacao {get;set;}
- bool? EncerrouGravacao {get;set;}
- GrupoTrabalho GrupoTrabalho {get;}
- Pessoa Pessoa {get;set;}
- Calendario Calendario {get;set;}
- OrdemServico OrdemServico {get;set;}

## Métodos (2)
- static Tecnico Load(int id)
- static Tecnico Carrega(int id)
