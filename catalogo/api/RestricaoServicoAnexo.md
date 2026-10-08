# RestricaoServicoAnexo (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > RestricaoServicoAnexo

class `Venki.Supravizio.Processo.Custom.RestricaoServicoAnexo` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_restricaoservicoanexo.md

## Propriedades (8)
- RestricaoServicoAnexo RestricaoServicoAnexoInstance {get;}
- int Id {get;set;}
- int ClasseAnexoId {get;set;}
- int? ServicoId {get;set;}
- int ClasseServicoId {get;set;}
- ClasseAnexo ClasseAnexo {get;}
- Servico Servico {get;set;}
- ClasseServico ClasseServico {get;set;}

## Métodos (2)
- static RestricaoServicoAnexo Load(int id)
- static RestricaoServicoAnexo Carrega(int id)
