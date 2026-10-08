# Pesquisa (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > Pesquisa

class `Venki.Supravizio.Processo.Custom.Pesquisa` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_pesquisa.md

## Propriedades (22)
- Pesquisa PesquisaInstance {get;}
- int Id {get;set;}
- string Assunto {get;set;}
- DateTime DataHoraCriacao {get;set;}
- string MotivoCancelamento {get;set;}
- int? ResponsavelCancelamentoId {get;}
- int OrdemServicoId {get;set;}
- string ComentarioAvaliador {get;set;}
- int? EscoreGeral {get;set;}
- int DomainId {get;}
- int AvaliadorId {get;}
- DateTime? DataHoraResposta {get;set;}
- int? ClassePesquisaSatisfacaoId {get;}
- int? QuestaoGeralId {get;}
- bool? RespondidaAutoAtendimento {get;set;}
- string Situacao {get;set;}
- SessionProxyList Itens {get;}
- Pessoa ResponsavelCancelamento {get;set;}
- Pessoa Avaliador {get;set;}
- OrdemServico OrdemServico {get;set;}
- ClassePesquisaSatisfacao ClassePesquisaSatisfacao {get;set;}
- QuestaoPesquisa QuestaoGeral {get;set;}

## Métodos (10)
- static Pesquisa Load(int id)
- static Pesquisa Carrega(int id)
- static Pesquisa New()
- static Pesquisa Novo()
- static ItemPesquisa NewItemPesquisa(Pesquisa parentPesquisa)
- static Pesquisa Load(string propertyName, object value)
- static Pesquisa Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
