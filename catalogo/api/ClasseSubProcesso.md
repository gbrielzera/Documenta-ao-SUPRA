# ClasseSubProcesso (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > ClasseSubProcesso

class `Venki.Supravizio.Processo.Custom.ClasseSubProcesso` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_classesubprocesso.md

## Propriedades (35)
- ClasseSubProcesso ClasseSubProcessoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- string Sigla {get;set;}
- bool Ativo {get;set;}
- string Objetivo {get;set;}
- int DomainId {get;set;}
- string DescricaoCliente {get;set;}
- int? MetodoPriorizacaoId {get;set;}
- int? FatorPrioridadeId {get;set;}
- int? OrdemExibicao {get;set;}
- decimal? ValorChargeBack {get;set;}
- int? OrgaoDonoId {get;set;}
- int? ResponsavelId {get;set;}
- bool DisponivelConsultaConhecimento {get;set;}
- bool AcessoTotalAdmin {get;set;}
- bool ReaberturaAutoAtendimento {get;set;}
- bool HabilitaConsultaAutomaticaBaseConhecimento {get;set;}
- string EmailsComunicadosManuais {get;set;}
- string ObjetivoPlano {get;set;}
- string NomeRemetenteComunicadosManuais {get;set;}
- string EmailRemetenteComunicadosManuais {get;set;}
- bool PermiteVisualizacaoGestorSubNiveis {get;set;}
- string CriterioChargeBack {get;set;}
- string RegraAutorizacao {get;set;}
- string VisibilidadeAutoAtendimento {get;set;}
- string PublicarApontamentosAA {get;set;}
- SessionProxyList RestricoesServicos {get;}
- SessionProxyList GruposAutorizados {get;}
- SessionProxyList SolucionadoresAutorizados {get;}
- SessionProxyList InfoCliente {get;}
- MetodoPriorizacao MetodoPriorizacao {get;set;}
- FatorPrioridade FatorPrioridade {get;set;}
- Orgao OrgaoDono {get;set;}
- Pessoa Responsavel {get;set;}

## Métodos (14)
- static ClasseSubProcesso Load(int id)
- static ClasseSubProcesso Carrega(int id)
- static ClasseSubProcesso New()
- static ClasseSubProcesso Novo()
- static RestricaoServico NewRestricaoServico(ClasseSubProcesso parentClasseSubProcesso)
- static AutorizacaoGrupo NewAutorizacaoGrupo(ClasseSubProcesso parentClasseSubProcesso)
- static AutorizacaoSolucionador NewAutorizacaoSolucionador(ClasseSubProcesso parentClasseSubProcesso)
- static InfoCliente NewInfoCliente(ClasseSubProcesso parentClasseSubProcesso)
- static ClasseSubProcesso Load(string propertyName, object value)
- static ClasseSubProcesso Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
- int ObtemValorFatorPrioridade(int valorDefault)
