# AcordoNivelServico (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > AcordoNivelServico

class `Venki.Supravizio.Recurso.Custom.AcordoNivelServico` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_acordonivelservico.md

## Propriedades (19)
- AcordoNivelServico AcordoNivelServicoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- DateTime DataInicioValidade {get;set;}
- DateTime DataFimValidade {get;set;}
- bool ConsideraFeriados {get;set;}
- int DomainId {get;set;}
- int? PlanoGestaoId {get;set;}
- decimal? ValorChargeBack {get;set;}
- string FormulaChargeBack {get;set;}
- int? Penalizacao {get;set;}
- bool PublicaInformacoesAA {get;set;}
- string CriterioChargeBack {get;set;}
- SessionProxyList Itens {get;}
- SessionProxyList DisponibilidadeAtendimento {get;}
- SessionProxyList InterrupcoesAcordadas {get;}
- SessionProxyList AplicacoesProcesso {get;}
- SessionProxyList OrgaosAtendidos {get;}
- PlanoGestao PlanoGestao {get;set;}

## Métodos (18)
- static AcordoNivelServico Load(int id)
- static AcordoNivelServico Carrega(int id)
- static AcordoNivelServico New()
- static AcordoNivelServico Novo()
- static ItemSLA NewItemSLA(AcordoNivelServico parentAcordoNivelServico)
- static ExcecaoSLA NewExcecaoSLA(ItemSLA parentItemSLA)
- static DisponibilidadeAtendimento NewDisponibilidadeAtendimento(AcordoNivelServico parentAcordoNivelServico)
- static AcordoInterrupcaoSLA NewAcordoInterrupcaoSLA(AcordoNivelServico parentAcordoNivelServico)
- static AprovadorInterrupcao NewAprovadorInterrupcao(AcordoInterrupcaoSLA parentAcordoInterrupcaoSLA)
- static AplicacaoProcesso NewAplicacaoProcesso(AcordoNivelServico parentAcordoNivelServico)
- static OrgaoAtendidoANS NewOrgaoAtendidoANS(AcordoNivelServico parentAcordoNivelServico)
- static AcordoNivelServico Load(string propertyName, object value)
- static AcordoNivelServico Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
- SessionProxyList ObtemOrdensServico(DateTime dataInicio, DateTime dataFim)
- int ObtemTempoDisponibilidade(DateTime dataHoraInicio, DateTime dataHoraFim, Pessoa cliente)
