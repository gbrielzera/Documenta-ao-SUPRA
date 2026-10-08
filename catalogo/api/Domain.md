# Domain (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Custom > Domain

class `Venki.Services.Custom.Domain` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_domain.md

## Propriedades (5)
- Domain DomainInstance {get;}
- int Id {get;set;}
- string Name {get;set;}
- string ShortName {get;set;}
- bool Enabled {get;set;}

## Métodos (12)
- static Domain Load(int id)
- static Domain Carrega(int id)
- static Domain New()
- static Domain Novo()
- static Domain Load(string propertyName, object value)
- static Domain Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
- void ClearLog()
- bool SaveLogo(Byte[] logo)
- Byte[] LoadLogo()
