# ClasseConfiguracao (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Configuracao.Custom > ClasseConfiguracao

class `Venki.Supravizio.Configuracao.Custom.ClasseConfiguracao` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_classeconfiguracao.md

## Propriedades (26)
- ClasseConfiguracao ClasseConfiguracaoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- string Sigla {get;set;}
- bool Ativo {get;set;}
- int DomainId {get;set;}
- decimal? ValorCustoAquisicao {get;set;}
- decimal? ValorCustoManutencao {get;set;}
- int? FatorPrioridadeId {get;set;}
- bool HabilitaRedefinicaoPapeis {get;set;}
- int TamanhoMaximo {get;set;}
- bool ComentarioObrigatorio {get;set;}
- bool FiltroServicoAssociacaoOcorrencia {get;set;}
- bool IncluirBlackList {get;set;}
- bool PermiteAnexarLink {get;set;}
- string SuperClasse {get;set;}
- string FonteDados {get;set;}
- string CriterioChargeBack {get;set;}
- string AgrupamentoItens {get;set;}
- string Acesso {get;set;}
- SessionProxyList Situacoes {get;}
- SessionProxyList ClassesComponentes {get;}
- SessionProxyList ClassesDependencias {get;}
- SessionProxyList ClassesCopia {get;}
- SessionProxyList TemplateTopicos {get;}
- FatorPrioridade FatorPrioridade {get;set;}

## Métodos (15)
- static ClasseConfiguracao Load(int id)
- static ClasseConfiguracao Carrega(int id)
- static ClasseConfiguracao New()
- static ClasseConfiguracao Novo()
- static SituacaoClasseConfiguracao NewSituacaoClasseConfiguracao(ClasseConfiguracao parentClasseConfiguracao)
- static ClasseComponente NewClasseComponente(ClasseConfiguracao parentClasseConfiguracao)
- static ClasseDependencia NewClasseDependencia(ClasseConfiguracao parentClasseConfiguracao)
- static ClasseCopia NewClasseCopia(ClasseConfiguracao parentClasseConfiguracao)
- static TopicoConhecimento NewTopicoConhecimento(ClasseConfiguracao parentClasseConfiguracao)
- static ClasseConfiguracao Load(string propertyName, object value)
- static ClasseConfiguracao Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
- int ObtemValorFatorPrioridade(int valorDefault)
