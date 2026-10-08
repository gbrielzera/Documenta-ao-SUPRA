# Servico (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > Servico

class `Venki.Supravizio.Processo.Custom.Servico` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_servico.md

## Propriedades (26)
- Servico ServicoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- string Sigla {get;set;}
- string Referencia {get;set;}
- int ResponsavelTecnicoId {get;set;}
- int DomainId {get;set;}
- string DescricaoCliente {get;set;}
- int ClasseServicoId {get;set;}
- int ResponsavelAreaId {get;set;}
- string PrerequisitosDependencias {get;set;}
- string Beneficios {get;set;}
- string Disponibilidade {get;set;}
- string ProgramacaoManutencao {get;set;}
- string SolicitacaoServicos {get;set;}
- int? FatorPrioridadeId {get;set;}
- bool DisponibilidadeAA {get;set;}
- bool Ativo {get;set;}
- string ReferenciaPlano {get;set;}
- string RedefinicaoPapeisItem {get;set;}
- SessionProxyList Componentes {get;}
- SessionProxyList AtoresServico {get;}
- Pessoa ResponsavelTecnico {get;set;}
- Pessoa ResponsavelArea {get;set;}
- ClasseServico ClasseServico {get;set;}
- FatorPrioridade FatorPrioridade {get;set;}

## Métodos (13)
- static Servico Load(int id)
- static Servico Carrega(int id)
- static Servico New()
- static Servico Novo()
- static ComponenteServico NewComponenteServico(Servico parentServico)
- static AtoresServico NewAtoresServico(Servico parentServico)
- static Servico Load(string propertyName, object value)
- static Servico Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
- int ObtemValorFatorPrioridade(int valorDefault)
- SessionProxyList ObtemUsuarios()
