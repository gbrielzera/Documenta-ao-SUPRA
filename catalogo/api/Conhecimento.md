# Conhecimento (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Configuracao.Custom > Conhecimento

class `Venki.Supravizio.Configuracao.Custom.Conhecimento` — supravizio.custom.dll v18.1.1.0
Herda de **ItemConfiguracao** (ver catalogo/api/ItemConfiguracao.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_conhecimento.md

## Propriedades (10)
- Conhecimento ConhecimentoInstance {get;}
- string Titulo {get;set;}
- string Sumario {get;set;}
- string PalavrasChave {get;set;}
- string SumarioTexto {get;set;}
- SessionProxyList Topicos {get;}
- SessionProxyList AplicacaoConhecimentoServico {get;}
- SessionProxyList RestricoesAcesso {get;}
- SessionProxyList Comentarios {get;}
- SessionProxyList Votos {get;}

## Métodos (14)
- static Conhecimento Load(int id)
- static Conhecimento Carrega(int id)
- static Conhecimento New()
- static Conhecimento Novo()
- static Topico NewTopico(Conhecimento parentConhecimento)
- static AplicacaoConhecimentoServico NewAplicacaoConhecimentoServico(Conhecimento parentConhecimento)
- static PermissaoConhecimentoPapel NewPermissaoConhecimentoPapel(Conhecimento parentConhecimento)
- static ComentarioConhecimento NewComentarioConhecimento(Conhecimento parentConhecimento)
- static VotacaoConhecimento NewVotacaoConhecimento(Conhecimento parentConhecimento)
- static Conhecimento Load(string propertyName, object value)
- static Conhecimento Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
