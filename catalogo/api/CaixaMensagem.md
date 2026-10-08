# CaixaMensagem (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > CaixaMensagem

class `Venki.Supravizio.Processo.Custom.CaixaMensagem` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_caixamensagem.md

## Propriedades (8)
- CaixaMensagem CaixaMensagemInstance {get;}
- int Id {get;set;}
- string NomeCaixa {get;set;}
- string Senha {get;set;}
- int? PortaPOP3 {get;set;}
- string ServidorPOP3 {get;set;}
- bool UtilizaSSL {get;set;}
- string TipoCaixa {get;set;}

## Métodos (9)
- static CaixaMensagem Load(int id)
- static CaixaMensagem Carrega(int id)
- static CaixaMensagem New()
- static CaixaMensagem Novo()
- static CaixaMensagem Load(string propertyName, object value)
- static CaixaMensagem Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
