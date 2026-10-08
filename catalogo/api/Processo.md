# Processo (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > Processo

class `Venki.Supravizio.Processo.Custom.Processo` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_processo.md

## Propriedades (16)
- Processo ProcessoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- bool Ativo {get;set;}
- string Sigla {get;set;}
- int DomainId {get;set;}
- int? FatorPrioridadeId {get;set;}
- string ExpressaoPastasAnexos {get;set;}
- string ExpressaoPastasAprovacao {get;set;}
- int MacroProcessoId {get;set;}
- string FormulaNumeracao {get;set;}
- string ClasseNegocio {get;set;}
- SessionProxyList Versoes {get;}
- SessionProxyList ModelosManuais {get;}
- FatorPrioridade FatorPrioridade {get;set;}
- MacroProcesso MacroProcesso {get;set;}

## Métodos (46)
- static Processo Load(int id)
- static Processo Carrega(int id)
- static Processo New()
- static Processo Novo()
- static DesenhoProcesso NewDesenhoProcesso(Processo parentProcesso)
- static SubProcesso NewSubProcesso(DesenhoProcesso parentDesenhoProcesso)
- static Atividade NewAtividade(SubProcesso parentSubProcesso)
- static FluxoSequencia NewFluxoSequencia(Atividade parentAtividade)
- static OperacaoAtividade NewOperacaoAtividade(Atividade parentAtividade)
- static ClasseAprovacao NewClasseAprovacao(OperacaoAtividade parentOperacaoAtividade)
- static RestricaoServicoAprovacao NewRestricaoServicoAprovacao(ClasseAprovacao parentClasseAprovacao)
- static EscopoClasseAprovacao NewEscopoClasseAprovacao(ClasseAprovacao parentClasseAprovacao)
- static Aprovador NewAprovador(OperacaoAtividade parentOperacaoAtividade)
- static CampoPreenchimento NewCampoPreenchimento(OperacaoAtividade parentOperacaoAtividade)
- static CampoPreenchimentoRegistro NewCampoPreenchimentoRegistro(CampoPreenchimento parentCampoPreenchimento)
- static ClasseAnexo NewClasseAnexo(OperacaoAtividade parentOperacaoAtividade)
- static RestricaoServicoAnexo NewRestricaoServicoAnexo(ClasseAnexo parentClasseAnexo)
- static EscopoClasseAnexo NewEscopoClasseAnexo(ClasseAnexo parentClasseAnexo)
- static CampoAprovacao NewCampoAprovacao(OperacaoAtividade parentOperacaoAtividade)
- static CampoPreenchimentoAprovacao NewCampoPreenchimentoAprovacao(OperacaoAtividade parentOperacaoAtividade)
- static CampoPreenchimentoAprovacaoRegistro NewCampoPreenchimentoAprovacaoRegistro(CampoPreenchimentoAprovacao parentCampoPreenchimentoAprovacao)
- static RelatorioOperacao NewRelatorioOperacao(OperacaoAtividade parentOperacaoAtividade)
- static ParamRelatorioOperacao NewParamRelatorioOperacao(RelatorioOperacao parentRelatorioOperacao)
- static ValorInput NewValorInput(Atividade parentAtividade)
- static RetornoItens NewRetornoItens(Atividade parentAtividade)
- static PassagemItens NewPassagemItens(Atividade parentAtividade)
- static ClienteAutorizado NewClienteAutorizado(Atividade parentAtividade)
- static TipoAnexoMensagem NewTipoAnexoMensagem(Atividade parentAtividade)
- static AcaoAcordo NewAcaoAcordo(Atividade parentAtividade)
- static OpcaoAtividade NewOpcaoAtividade(Atividade parentAtividade)
- static AssociacaoSubprocesso NewAssociacaoSubprocesso(Atividade parentAtividade)
- static RelatorioAtividade NewRelatorioAtividade(Atividade parentAtividade)
- static ParamRelatorioAtividade NewParamRelatorioAtividade(RelatorioAtividade parentRelatorioAtividade)
- static Gateway NewGateway(SubProcesso parentSubProcesso)
- static Emissor NewEmissor(Gateway parentGateway)
- static Receptor NewReceptor(Gateway parentGateway)
- static OutputSubProcesso NewOutputSubProcesso(SubProcesso parentSubProcesso)
- static PapelProcesso NewPapelProcesso(DesenhoProcesso parentDesenhoProcesso)
- static ModeloManual NewModeloManual(Processo parentProcesso)
- static Processo Load(string propertyName, object value)
- static Processo Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
- Processo AtivaVersao(DesenhoProcesso desenhoProcesso)
- int ObtemValorFatorPrioridade(int valorDefault)
