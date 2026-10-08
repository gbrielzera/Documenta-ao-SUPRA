# ItemSLA (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > ItemSLA

class `Venki.Supravizio.Recurso.Custom.ItemSLA` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_itemsla.md

## Propriedades (14)
- ItemSLA ItemSLAInstance {get;}
- int AcordoNivelServicoId {get;set;}
- int Id {get;set;}
- int? ClasseServicoId {get;set;}
- int? ServicoId {get;set;}
- int? PerfilClienteId {get;set;}
- string TempoAtendimento {get;set;}
- int? GrauPrioridadeId {get;set;}
- SessionProxyList PeriodosExcecao {get;}
- AcordoNivelServico AcordoNivelServico {get;}
- Servico Servico {get;set;}
- ClasseServico ClasseServico {get;set;}
- PerfilCliente PerfilCliente {get;set;}
- GrauPrioridade GrauPrioridade {get;set;}

## Métodos (2)
- static ItemSLA Load(int id)
- static ItemSLA Carrega(int id)
