# TemplateMensagem (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo > TemplateMensagem

class `Venki.Supravizio.Processo.TemplateMensagem` — supravizio.dll v18.1.1.0

## Propriedades (15)
- bool ConteudoHTML {get;set;}
- string Complemento5 {get;set;}
- string Complemento4 {get;set;}
- string Complemento3 {get;set;}
- string Complemento2 {get;set;}
- string Complemento1 {get;set;}
- string Remetente {get;set;}
- string NomeRemetente {get;set;}
- ArrayList Destinatarios {get;}
- string Assunto {get;set;}
- string Corpo {get;set;}
- bool Cancelar {get;set;}
- DateTime? DataHoraAgendada {get;set;}
- string ModeloComunicado {get;set;}
- Dictionary<SessionObjectProxy, Dictionary<string, bool>> OrdensServicoImpressao {get;}

## Métodos (4)
- ArrayList ObtemListaSelecionados()
- void PreencheCorpo(string nomeModeloComunicado, SessionObjectProxy ordemServico)
- void AdicionaImpressao(SessionObjectProxy ordemServico)
- void AdicionaImpressao(SessionObjectProxy ordemServico, bool imprimirItensConfiguracao, bool imprimirAprovacoes, bool imprimirComentarios, bool imprimirEventos, bool imprimirAtividadesExecutadas, bool imprimirComunicados, bool imprimirPessoasResponsaveis)
