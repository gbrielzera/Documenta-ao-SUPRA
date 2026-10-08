# VersaoPortal (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Portal.Custom > VersaoPortal

class `Venki.Supravizio.Portal.Custom.VersaoPortal` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (12)
- VersaoPortal VersaoPortalInstance {get;}
- int Id {get;set;}
- DateTime? DataAtivacao {get;set;}
- DateTime DataCriacao {get;set;}
- int PessoaId {get;set;}
- int Versao {get;set;}
- int DomainId {get;set;}
- decimal BottomPadding {get;set;}
- decimal LeftPadding {get;set;}
- decimal RightPadding {get;set;}
- decimal TopPadding {get;set;}
- Pessoa Pessoa {get;set;}

## Métodos (9)
- static VersaoPortal Load(int id)
- static VersaoPortal Carrega(int id)
- static VersaoPortal New()
- static VersaoPortal Novo()
- static VersaoPortal Load(string propertyName, object value)
- static VersaoPortal Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
