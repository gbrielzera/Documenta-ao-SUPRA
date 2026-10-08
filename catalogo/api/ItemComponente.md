# ItemComponente (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Configuracao.Custom > ItemComponente

class `Venki.Supravizio.Configuracao.Custom.ItemComponente` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_itemcomponente.md

## Propriedades (23)
- ItemComponente ItemComponenteInstance {get;}
- int ItemConfiguracaoId {get;set;}
- int? ItemComponenteId {get;set;}
- decimal? Tamanho {get;set;}
- string Comentario {get;set;}
- string Descricao {get;set;}
- int? ModeloId {get;set;}
- string NumeroSerie {get;set;}
- decimal? ValorCustoAquisicao {get;set;}
- decimal? ValorCustoManutencao {get;set;}
- DateTime? DataEntrega {get;set;}
- int Id {get;set;}
- int ClasseConfiguracaoId {get;set;}
- int? OcorrenciaId {get;set;}
- decimal? ValorPrecoAquisicao {get;set;}
- decimal? ValorPrecoManutencao {get;set;}
- string CodigoOCS {get;set;}
- string TabelaOCS {get;set;}
- ItemConfiguracao ItemComposto {get;}
- ItemConfiguracao Componente {get;set;}
- Modelo Modelo {get;set;}
- ClasseConfiguracao ClasseConfiguracao {get;set;}
- Ocorrencia Ocorrencia {get;set;}

## Métodos (2)
- static ItemComponente Load(int id)
- static ItemComponente Carrega(int id)
