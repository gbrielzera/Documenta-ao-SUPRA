# HistoricoComponente (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > HistoricoComponente

class `Venki.Supravizio.Recurso.Custom.HistoricoComponente` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_historicocomponente.md

## Propriedades (12)
- HistoricoComponente HistoricoComponenteInstance {get;}
- int HistoricoItemChargeBackId {get;set;}
- int HistoricoItemItemConfiguracaoId {get;set;}
- int? ComponenteId {get;set;}
- decimal? Tamanho {get;set;}
- int ClasseConfiguracaoId {get;set;}
- int Id {get;set;}
- decimal? ValorPrecoAquisicao {get;set;}
- decimal? ValorPrecoManutencao {get;set;}
- HistoricoItem HistoricoItem {get;}
- ItemConfiguracao Componente {get;set;}
- ClasseConfiguracao ClasseConfiguracao {get;set;}

## Métodos (2)
- static HistoricoComponente Load(int id)
- static HistoricoComponente Carrega(int id)
