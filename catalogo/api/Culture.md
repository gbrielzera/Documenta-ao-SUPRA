# Culture (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Dictionary.Custom > Culture

class `Venki.Services.Dictionary.Custom.Culture` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_culture.md

## Propriedades (4)
- Culture CultureInstance {get;}
- int Id {get;set;}
- string Description {get;set;}
- string ShortName {get;set;}

## Métodos (9)
- static Culture Load(int id)
- static Culture Carrega(int id)
- static Culture New()
- static Culture Novo()
- static Culture Load(string propertyName, object value)
- static Culture Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
