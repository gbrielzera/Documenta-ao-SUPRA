# GrupoTrabalho (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > GrupoTrabalho

class `Venki.Supravizio.Recurso.Custom.GrupoTrabalho` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_grupotrabalho.md

## Propriedades (54)
- GrupoTrabalho GrupoTrabalhoInstance {get;}
- string Descricao {get;set;}
- bool Ativo {get;set;}
- int? GrupoTrabalhoPaiId {get;set;}
- int CoordenadorId {get;set;}
- int DomainId {get;set;}
- int Id {get;set;}
- string Sigla {get;set;}
- bool PermiteVisualizarOutrosGrupos {get;set;}
- bool WorklistVisualizaProcesso {get;set;}
- bool WorklistPermiteImprimirOS {get;set;}
- bool ExibeAssociadas {get;set;}
- bool ExibeTimesheet {get;set;}
- bool ExibeArquivos {get;set;}
- bool ExibeAprovacao {get;set;}
- bool ExibeInformacoes {get;set;}
- bool ExibePriorizacao {get;set;}
- bool ExibeCamposPreenchidos {get;set;}
- bool ExibeFluxoProcesso {get;set;}
- bool ExibeComunicados {get;set;}
- bool ExibeEdicaoBotaoConhecimento {get;set;}
- bool ExibeEdicaoBotaoMaisAcoes {get;set;}
- bool ExibeWorkspaceDashboard {get;set;}
- bool ExibeWorkspaceBaseConhecimento {get;set;}
- bool ExibeWorkspaceOpcoes {get;set;}
- bool ExibeWorkspaceFiltroOS {get;set;}
- bool ExibeComentarios {get;set;}
- bool ExibeClassificacao {get;set;}
- bool ExibeDadosCliente {get;set;}
- bool ExibeTodosEdicaoCoordenador {get;set;}
- bool ExibeTodosWorkspaceCoordenador {get;set;}
- bool PermiteAlterarOrdenacao {get;set;}
- bool PermiteAlterarAgrupamento {get;set;}
- bool PermiteAlterarOrdemColunas {get;set;}
- string LayoutPadraoWorkspace {get;set;}
- bool PermiteGravarApontamentos {get;set;}
- string PermiteCancelar {get;set;}
- string PermiteEncaminhar {get;set;}
- string PermiteClassificar {get;set;}
- string PermiteReabrir {get;set;}
- string PermiteInterromperANS {get;set;}
- string PermitePriorizar {get;set;}
- string ExibeAlertaOSGrupo {get;set;}
- string PermiteCriarAvisoInterno {get;set;}
- string PermiteCriarAvisoExterno {get;set;}
- string PermitePublicarDashboard {get;set;}
- string PermiteAgendar {get;set;}
- string PermiteCategorizar {get;set;}
- SessionProxyList Tecnicos {get;}
- SessionProxyList FilasAutorizadas {get;}
- SessionProxyList Atalhos {get;}
- SessionProxyList Visualizacoes {get;}
- Pessoa Coordenador {get;set;}
- GrupoTrabalho GrupoTrabalhoPai {get;set;}

## Métodos (19)
- static SessionProxyList ObtemTodosCoordenadores()
- static GrupoTrabalho Load(int id)
- static GrupoTrabalho Carrega(int id)
- static GrupoTrabalho New()
- static GrupoTrabalho Novo()
- static Tecnico NewTecnico(GrupoTrabalho parentGrupoTrabalho)
- static AutorizaFila NewAutorizaFila(GrupoTrabalho parentGrupoTrabalho)
- static AtalhoNovaOrdemServico NewAtalhoNovaOrdemServico(GrupoTrabalho parentGrupoTrabalho)
- static Visualizacao NewVisualizacao(GrupoTrabalho parentGrupoTrabalho)
- static CondicaoFiltro NewCondicaoFiltro(Visualizacao parentVisualizacao)
- static GrupoTrabalho Load(string propertyName, object value)
- static GrupoTrabalho Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
- Tecnico ObtemTecnico(int idPessoa)
- SessionProxyList ObtemSubGrupos(bool recursivo)
- SessionProxyList ObtemSolucionadores(bool incluSubniveis, bool somenteCoordenadores, bool excluiCoordenadores)
- SessionProxyList ObtemGruposPais()
