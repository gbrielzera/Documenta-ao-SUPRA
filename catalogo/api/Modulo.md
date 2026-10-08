# Modulo (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Portal.Custom > Modulo

class `Venki.Supravizio.Portal.Custom.Modulo` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (7)
- Modulo ModuloInstance {get;}
- int Id {get;set;}
- string Nome {get;set;}
- string URL {get;set;}
- int DomainId {get;set;}
- string Sigla {get;set;}
- SessionProxyList EstilosModulo {get;}

## Métodos (10)
- static Modulo Load(int id)
- static Modulo Carrega(int id)
- static Modulo New()
- static Modulo Novo()
- static EstiloModulo NewEstiloModulo(Modulo parentModulo)
- static Modulo Load(string propertyName, object value)
- static Modulo Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
