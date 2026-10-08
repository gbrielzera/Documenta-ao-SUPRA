# Pessoa (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > Pessoa

class `Venki.Supravizio.Recurso.Custom.Pessoa` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_pessoa.md

## Propriedades (48)
- string Senha {get;set;}
- Pessoa PessoaInstance {get;}
- int Id {get;set;}
- string Nome {get;set;}
- string NomeAbreviado {get;set;}
- string Telefone {get;set;}
- string CelularParticular {get;set;}
- string CelularEmpresa {get;set;}
- string SegundoContato {get;set;}
- string TelefoneSegundoContato {get;set;}
- string Email {get;set;}
- string EmailAlternativo {get;set;}
- bool Ativo {get;set;}
- string UsuarioRede {get;set;}
- int OrgaoId {get;set;}
- int DomainId {get;set;}
- string Cargo {get;set;}
- int? FornecedorId {get;set;}
- int? FatorPrioridadeId {get;set;}
- int? PerfilClienteId {get;set;}
- int? LocalId {get;set;}
- int? CulturaClienteId {get;set;}
- int? SubstitutoAprovacaoId {get;set;}
- DateTime? DataInicioSubstituicao {get;set;}
- DateTime? DataFimSubstituicao {get;set;}
- int? PessoaRegistroAprovacaoId {get;set;}
- DateTime? DataHoraUltimoAcessoAA {get;set;}
- int? UserId {get;set;}
- bool AutorizarWorklist {get;set;}
- bool PermiteAcessarPortal {get;set;}
- bool SenhaNaoExpira {get;set;}
- bool Bloqueado {get;set;}
- DateTime? DataUltimaSenha {get;set;}
- int TentativasLoginErro {get;set;}
- bool NecessarioAceitarTermo {get;set;}
- DateTime? DataAceiteTermo {get;set;}
- string TipoColaborador {get;set;}
- string Tipo {get;set;}
- string Autenticacao {get;set;}
- Pessoa SubstitutoAprovacao {get;set;}
- Pessoa PessoaRegistroAprovacao {get;set;}
- Orgao Orgao {get;set;}
- Fornecedor Fornecedor {get;set;}
- FatorPrioridade FatorPrioridade {get;set;}
- PerfilCliente PerfilCliente {get;set;}
- Local Local {get;set;}
- Culture CulturaCliente {get;set;}
- User Usuario {get;set;}

## Métodos (19)
- static Pessoa Load(int id)
- static Pessoa Carrega(int id)
- static Pessoa New()
- static Pessoa Novo()
- static Pessoa Load(string propertyName, object value)
- static Pessoa Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
- Pessoa VerificaDisponibilidadeEncaminhamento()
- Pessoa VerificaDisponibilidadeEm(DateTime data)
- int ObtemValorFatorPrioridade(int valorDefault)
- Pessoa ObtemChefia(bool chefiaGestor)
- Pessoa ObtemChefia(Orgao orgaoPai, bool chefiaGestor)
- TimeSpan ObtemTempoTotalApontado(DateTime inicio, DateTime fim)
- TimeSpan ObtemTempoTotalApontado(DateTime inicio, DateTime fim, Processo processo)
- TimeSpan ObtemTempoTotalApontado(DateTime inicio, DateTime fim, ClasseSubProcesso classeSubProcesso)
- SessionProxyList ObtemOcorrenciasAbertas(ClasseSubProcesso classeSubProcesso, Servico servico)
- SessionProxyList ObtemSubordinados(bool incluiSubniveis, bool somenteAtivos)
