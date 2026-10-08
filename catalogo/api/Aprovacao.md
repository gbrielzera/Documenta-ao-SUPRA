# Aprovacao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > Aprovacao

class `Venki.Supravizio.Processo.Custom.Aprovacao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_aprovacao.md

## Propriedades (15)
- Aprovacao AprovacaoInstance {get;}
- int PessoaId {get;}
- DateTime DataHoraEvidencia {get;}
- string Motivo {get;}
- int Versao {get;}
- int AssuntoAprovacaoId {get;}
- string DescricaoPapelAprovador {get;}
- int? AprovadorRealId {get;set;}
- int Passo {get;set;}
- string ExplicacaoAprovador {get;set;}
- bool UtilizouPreAprovacao {get;set;}
- string Situacao {get;set;}
- VersaoAprovacao VersaoAprovacao {get;}
- Pessoa AprovadorReal {get;set;}
- Pessoa Aprovador {get;set;}
