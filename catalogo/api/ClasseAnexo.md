# ClasseAnexo (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > ClasseAnexo

class `Venki.Supravizio.Processo.Custom.ClasseAnexo` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_classeanexo.md

## Propriedades (17)
- bool IncluirPaginaAssinatura {get;set;}
- ClasseAnexo ClasseAnexoInstance {get;}
- int OperacaoAtividadeId {get;set;}
- int Sequencial {get;set;}
- int Id {get;set;}
- string Descricao {get;set;}
- bool RequeridoInicial {get;set;}
- bool ProduzidoTermino {get;set;}
- bool ExibicaoAutomaticaAA {get;set;}
- bool PermiteMultiplosItens {get;set;}
- int? PapelAssinaturaId {get;set;}
- bool IncluirQRCode {get;set;}
- string ConfiguracaoUsuarios {get;set;}
- SessionProxyList Restricoes {get;}
- SessionProxyList EscopoClasses {get;}
- OperacaoAtividade OperacaoAtividade {get;}
- PapelProcesso PapelAssinatura {get;set;}

## Métodos (2)
- static ClasseAnexo Load(int id)
- static ClasseAnexo Carrega(int id)
