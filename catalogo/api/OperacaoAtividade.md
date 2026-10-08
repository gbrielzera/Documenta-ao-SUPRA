# OperacaoAtividade (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > OperacaoAtividade

class `Venki.Supravizio.Processo.Custom.OperacaoAtividade` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_operacaoatividade.md

## Propriedades (32)
- OperacaoAtividade OperacaoAtividadeInstance {get;}
- int Id {get;set;}
- bool Ativo {get;set;}
- int AtividadeId {get;set;}
- int OperacaoId {get;set;}
- string DescricaoAssuntoAprovacao {get;set;}
- bool BloquearPendencia {get;set;}
- bool CopiarAnexados {get;set;}
- int? MinimoAprovadores {get;set;}
- int Sequencia {get;set;}
- bool ExigeApropriacoes {get;set;}
- bool UtilizaIdentidadeSolicitante {get;set;}
- bool ReutilizaAprovacaoAnterior {get;set;}
- string RotuloPreenchimento {get;set;}
- bool IniciaAutomatico {get;set;}
- bool ReprovarImediato {get;set;}
- int? ReenvioEmailAprovacao {get;set;}
- string RotuloBotaoAprovar {get;set;}
- string RotuloBotaoReprovar {get;set;}
- string Nome {get;set;}
- string Configuracao {get;set;}
- string ObrigatoriedadeMotivo {get;set;}
- string AssinaturaDigital {get;set;}
- SessionProxyList ClassesAprovacao {get;}
- SessionProxyList Aprovadores {get;}
- SessionProxyList Campos {get;}
- SessionProxyList ClassesAnexos {get;}
- SessionProxyList CamposAprovacao {get;}
- SessionProxyList CamposPreenchimentoAprovacao {get;}
- SessionProxyList Relatorios {get;}
- Atividade Atividade {get;}
- Operacao Operacao {get;set;}

## Métodos (2)
- static OperacaoAtividade Load(int id)
- static OperacaoAtividade Carrega(int id)
