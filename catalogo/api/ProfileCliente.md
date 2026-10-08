# ProfileCliente (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > ProfileCliente

class `Venki.Supravizio.Recurso.Custom.ProfileCliente` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (5)
- ProfileCliente ProfileClienteInstance {get;}
- int PessoaId {get;set;}
- string NomeProfile {get;set;}
- DateTime DataUltimaModificacao {get;set;}
- Pessoa Pessoa {get;set;}

## Métodos (7)
- static ProfileCliente New()
- static ProfileCliente Novo()
- static ProfileCliente Load(string propertyName, object value)
- static ProfileCliente Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
