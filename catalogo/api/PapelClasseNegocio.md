# PapelClasseNegocio (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > PapelClasseNegocio

class `Venki.Supravizio.Processo.Custom.PapelClasseNegocio` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_papelclassenegocio.md

## Propriedades (32)
- PapelClasseNegocio PapelClasseNegocioInstance {get;}
- string Nome {get;set;}
- bool Ativo {get;set;}
- int DomainId {get;set;}
- string ScriptSelecaoAtores {get;set;}
- int Id {get;set;}
- string Referencia {get;set;}
- bool ExcluiAprovacoes {get;set;}
- bool SomenteConectados {get;set;}
- string NomeCampoOcorrencia {get;set;}
- string FiltroOrgao {get;set;}
- string FiltroEmpresa {get;set;}
- bool FiltroAtivo {get;set;}
- string FiltroCargo {get;set;}
- string FiltroFornecedor {get;set;}
- string FiltroPerfilCliente {get;set;}
- string FiltroUnidadeNegocio {get;set;}
- string FiltroCustomizados {get;set;}
- int? TipoItemAnexoId {get;set;}
- string CodigoAtividade {get;set;}
- bool SomenteUltimaExecucao {get;set;}
- string ClasseNegocio {get;set;}
- string AtorGrupoTrabalho {get;set;}
- string Tipo {get;set;}
- string OpcaoCampoOcorrencia {get;set;}
- string PessoaItemConfiguracao {get;set;}
- string EnvolvimentoAtividadeExecutada {get;set;}
- SessionProxyList PapeisComposicao {get;}
- SessionProxyList RelacaoOrgaos {get;}
- SessionProxyList RelacaoGrupos {get;}
- SessionProxyList RelacaoPessoas {get;}
- ClasseConfiguracao TipoItemAnexo {get;set;}

## Métodos (13)
- static PapelClasseNegocio Load(int id)
- static PapelClasseNegocio Carrega(int id)
- static PapelClasseNegocio New()
- static PapelClasseNegocio Novo()
- static ComposicaoPapel NewComposicaoPapel(PapelClasseNegocio parentPapelClasseNegocio)
- static OrgaoPapel NewOrgaoPapel(PapelClasseNegocio parentPapelClasseNegocio)
- static GrupoPapel NewGrupoPapel(PapelClasseNegocio parentPapelClasseNegocio)
- static PessoaPapel NewPessoaPapel(PapelClasseNegocio parentPapelClasseNegocio)
- static PapelClasseNegocio Load(string propertyName, object value)
- static PapelClasseNegocio Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
