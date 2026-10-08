# OrdemServico (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > OrdemServico

class `Venki.Supravizio.Processo.Custom.OrdemServico` — supravizio.custom.dll v18.1.1.0
Herda de **Ocorrencia** (ver catalogo/api/Ocorrencia.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_ordemservico.md

## Propriedades (49)
- OrdemServico OrdemServicoInstance {get;}
- string DescricaoDetalhada {get;set;}
- string TelefoneCliente {get;set;}
- string CelularCliente {get;set;}
- string SegundoContato {get;set;}
- string TelefoneSegundoContato {get;set;}
- DateTime? DataHoraExecucaoMudanca {get;set;}
- int ServicoId {get;set;}
- int FavorecidoId {get;set;}
- string Causa {get;set;}
- string Solucao {get;set;}
- string NumeroReferenciaFornecedor {get;set;}
- string ContatoResponsavelFornecedor {get;set;}
- string ComentarioContato {get;set;}
- int? ClassePesquisaSatisfacaoId {get;set;}
- int? GrauPrioridadeCalculadoId {get;set;}
- int? GrauPrioridadeSelecionadoId {get;set;}
- int? PesoPrioridadeCalculado {get;set;}
- int? PesoPrioridadeSelecionado {get;set;}
- string VariaveisPriorizacao {get;set;}
- int? NivelSLAId {get;set;}
- int? TempoSLA {get;set;}
- bool? ExpirouTempoSLA {get;set;}
- int? MetodoPriorizacaoId {get;set;}
- string UsuarioAutoAtendimento {get;set;}
- string SintomaAnalisado {get;set;}
- string Justificativa {get;set;}
- bool LeituraResponsavel {get;set;}
- string HardwareAutoAtendimento {get;set;}
- int? ItemSLAId {get;set;}
- int? TempoInterrupcaoSLA {get;set;}
- decimal? ValorChargeBack {get;set;}
- int? ContratoId {get;set;}
- int? CategoriaId {get;set;}
- string SituacaoPesquisa {get;set;}
- string Origem {get;set;}
- string IndicadorRespostaEmail {get;set;}
- SessionProxyList SLA {get;}
- SessionProxyList Interrupcoes {get;}
- Servico Servico {get;set;}
- Pessoa Favorecido {get;set;}
- ClassePesquisaSatisfacao ClassePesquisaSatisfacao {get;set;}
- GrauPrioridade GrauPrioridadeCalculado {get;set;}
- GrauPrioridade GrauPrioridadeSelecionado {get;set;}
- NivelSLA NivelSLA {get;set;}
- MetodoPriorizacao MetodoPriorizacao {get;set;}
- ItemSLA ItemSLA {get;set;}
- Contrato Contrato {get;set;}
- Categoria Categoria {get;set;}

## Métodos (26)
- void AdicionaComentario(string comentario, bool publicaNoAutoatendimento)
- static OrdemServico Load(int id)
- static OrdemServico Carrega(int id)
- static OrdemServico New()
- static OrdemServico Novo()
- static SLAOrdemServico NewSLAOrdemServico(OrdemServico parentOrdemServico)
- static InterrupcaoSLA NewInterrupcaoSLA(OrdemServico parentOrdemServico)
- static OrdemServico Load(string propertyName, object value)
- static OrdemServico Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
- OrdemServico RegistraEntregaServico(DateTime? dataHoraExecMudanca)
- int ObtemMaiorValorFatorPrioridadeItensConfiguracao(int valorDefault)
- int ObtemMenorValorFatorPrioridadeItensConfiguracao(int valorDefault)
- Ocorrencia Finaliza(string codigoAtividade, string causa, string solucao, DateTime dataHoraExecucaoMudanca)
- SessionProxyList ObtemServicosImpactados()
- SessionProxyList ObtemUsuariosImpactados()
- SessionProxyList ObtemOrgaosImpactados()
- int ObtemVariavelPrioridade(string nomeVariavel)
- OrdemServico RefazANS()
- Ocorrencia Nova(string siglaClasseSubProcesso, string codigoIniciador, string assunto, Servico servico, Pessoa cliente, Pessoa responsavel)
- void RecalculaANOTempos()
- Ocorrencia Nova(string siglaClasseSubProcesso, string codigoIniciador, string assunto, Servico servico, Pessoa cliente, Pessoa responsavel, Hashtable valoresCustomizados)
- void EnviaPesquisaSatisfacao(Atividade eventoFinal, bool forcaEnvio)
- Ocorrencia Nova(string siglaClasseSubProcesso, string codigoIniciador, string assunto, Servico servico, Pessoa cliente, Pessoa responsavel, Hashtable valoresCustomizados, string numero)
