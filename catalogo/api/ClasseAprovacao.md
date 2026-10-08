# ClasseAprovacao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > ClasseAprovacao

class `Venki.Supravizio.Processo.Custom.ClasseAprovacao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_classeaprovacao.md

## Propriedades (9)
- ClasseAprovacao ClasseAprovacaoInstance {get;}
- int OperacaoAtividadeId {get;set;}
- bool Obrigatorio {get;set;}
- bool CopiarAnexado {get;set;}
- int Id {get;set;}
- string Descricao {get;set;}
- SessionProxyList Restricoes {get;}
- SessionProxyList EscopoClasses {get;}
- OperacaoAtividade OperacaoAtividade {get;}

## Métodos (2)
- static ClasseAprovacao Load(int id)
- static ClasseAprovacao Carrega(int id)
