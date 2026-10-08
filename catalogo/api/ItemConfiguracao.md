# ItemConfiguracao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Configuracao.Custom > ItemConfiguracao

class `Venki.Supravizio.Configuracao.Custom.ItemConfiguracao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_itemconfiguracao.md

## Propriedades (43)
- ItemConfiguracao ItemConfiguracaoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- int ClasseConfiguracaoId {get;set;}
- int DomainId {get;set;}
- int SituacaoId {get;set;}
- DateTime? DataExpiracaoGarantia {get;set;}
- string Localizacao {get;set;}
- int? TipoPosseId {get;set;}
- int? ModeloId {get;set;}
- string NumeroSerie {get;set;}
- int? FornecedorId {get;set;}
- DateTime? DataEntrega {get;set;}
- DateTime? DataAceite {get;set;}
- string Comentario {get;set;}
- decimal? ValorCustoAquisicao {get;set;}
- DateTime? DataProducao {get;set;}
- DateTime? DataDesativacao {get;set;}
- decimal? ValorCustoManutencao {get;set;}
- int? FatorPrioridadeId {get;set;}
- int? ResponsavelId {get;set;}
- decimal? ValorPrecoAquisicao {get;set;}
- decimal? ValorPrecoManutencao {get;set;}
- DateTime DataCadastro {get;set;}
- int? AreaProprietariaId {get;set;}
- int? EmpresaProprietariaId {get;set;}
- string CriterioChargeBack {get;set;}
- SessionProxyList Dependencias {get;}
- SessionProxyList Componentes {get;}
- SessionProxyList Observacoes {get;}
- SessionProxyList Copias {get;}
- SessionProxyList Usuarios {get;}
- SessionProxyList Atores {get;}
- SessionProxyList HistoricoItem {get;}
- ClasseConfiguracao ClasseConfiguracao {get;set;}
- SituacaoClasseConfiguracao Situacao {get;set;}
- TipoPosse TipoPosse {get;set;}
- Modelo Modelo {get;set;}
- Fornecedor Fornecedor {get;set;}
- FatorPrioridade FatorPrioridade {get;set;}
- Pessoa Responsavel {get;set;}
- Orgao AreaProprietaria {get;set;}
- Empresa EmpresaProprietaria {get;set;}

## Métodos (22)
- static ItemConfiguracao Load(int id)
- static ItemConfiguracao Carrega(int id)
- static ItemConfiguracao New()
- static ItemConfiguracao Novo()
- static ItemDependencia NewItemDependencia(ItemConfiguracao parentItemConfiguracao)
- static ItemComponente NewItemComponente(ItemConfiguracao parentItemConfiguracao)
- static ObservacaoItem NewObservacaoItem(ItemConfiguracao parentItemConfiguracao)
- static ItemCopia NewItemCopia(ItemConfiguracao parentItemConfiguracao)
- static UsuarioItem NewUsuarioItem(ItemConfiguracao parentItemConfiguracao)
- static AtoresItem NewAtoresItem(ItemConfiguracao parentItemConfiguracao)
- static HistoricoItem NewHistoricoItem(ItemConfiguracao parentItemConfiguracao)
- static ItemConfiguracao Load(string propertyName, object value)
- static ItemConfiguracao Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
- int ObtemValorFatorPrioridade(int valorDefault)
- ItemConfiguracao AdicionaComponentePorOcorrencia(ItemConfiguracao itemComponente, Ocorrencia ocorrencia, decimal tamanho)
- ItemConfiguracao RemoveComponentePorOcorrencia(ItemConfiguracao itemParaRemocao, Ocorrencia ocorrencia)
- ItemConfiguracao AdicionaUsuarioPorOcorrencia(Pessoa usuario, Ocorrencia ocorrencia)
- ItemConfiguracao RemoveUsuarioPorOcorrencia(Pessoa usuario, Ocorrencia ocorrencia)
- void ModificaSituacao(string nomeSituacao)
