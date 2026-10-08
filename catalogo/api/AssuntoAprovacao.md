# AssuntoAprovacao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > AssuntoAprovacao

class `Venki.Supravizio.Processo.Custom.AssuntoAprovacao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_assuntoaprovacao.md

## Propriedades (11)
- AssuntoAprovacao AssuntoAprovacaoInstance {get;}
- int Id {get;set;}
- int OcorrenciaId {get;set;}
- string Descricao {get;set;}
- int? OperacaoAtividadeId {get;set;}
- int? AcordoNivelServicoId {get;set;}
- int? MotivoInterrupcaoId {get;set;}
- SessionProxyList Versoes {get;}
- Ocorrencia Ocorrencia {get;}
- OperacaoAtividade OperacaoAtividade {get;set;}
- AcordoInterrupcaoSLA AcordoInterrupcaoSLA {get;set;}

## Métodos (2)
- static AssuntoAprovacao Load(int id)
- static AssuntoAprovacao Carrega(int id)
