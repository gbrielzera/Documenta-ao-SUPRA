# HistoricoItem (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Configuracao.Custom > HistoricoItem

class `Venki.Supravizio.Configuracao.Custom.HistoricoItem` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_historicoitem.md

## Propriedades (8)
- HistoricoItem HistoricoItemInstance {get;}
- int Id {get;set;}
- string Comentario {get;set;}
- DateTime DataAlteracao {get;set;}
- int PessoaId {get;set;}
- int ItemConfiguracaoId {get;set;}
- ItemConfiguracao ItemConfiguracao {get;}
- Pessoa Pessoa {get;set;}

## Métodos (2)
- static HistoricoItem Load(int id)
- static HistoricoItem Carrega(int id)
