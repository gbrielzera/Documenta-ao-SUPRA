# Skin (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Portal.Custom > Skin

class `Venki.Supravizio.Portal.Custom.Skin` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (6)
- Skin SkinInstance {get;}
- int Id {get;set;}
- int DomainId {get;set;}
- string Descricao {get;set;}
- string URL {get;set;}
- string Sigla {get;set;}

## Métodos (9)
- static Skin Load(int id)
- static Skin Carrega(int id)
- static Skin New()
- static Skin Novo()
- static Skin Load(string propertyName, object value)
- static Skin Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
