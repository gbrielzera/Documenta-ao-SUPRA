# RecursoAplicado (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > RecursoAplicado

class `Venki.Supravizio.Recurso.Custom.RecursoAplicado` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_recursoaplicado.md

## Propriedades (11)
- RecursoAplicado RecursoAplicadoInstance {get;}
- int? ContratoId {get;set;}
- string DescricaoRecurso {get;set;}
- int Id {get;set;}
- decimal? ValorMensal {get;set;}
- decimal? ValorHora {get;set;}
- int? QuantidadeHoras {get;set;}
- int? ValidadeSaldo {get;set;}
- bool UtilizaAcumuladosPrimeiramente {get;set;}
- SessionProxyList GruposSolucionadores {get;}
- Contrato Contrato {get;}

## Métodos (2)
- static RecursoAplicado Load(int id)
- static RecursoAplicado Carrega(int id)
