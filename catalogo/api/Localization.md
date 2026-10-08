# Localization (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Dictionary.Custom > Localization

class `Venki.Services.Dictionary.Custom.Localization` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_localization.md

## Propriedades (11)
- Localization LocalizationInstance {get;}
- int DomainId {get;set;}
- int ClassId {get;set;}
- string TextualRepresentation {get;set;}
- string TextValue {get;set;}
- int CultureId {get;set;}
- int PropertyId {get;set;}
- int Id {get;set;}
- Class Class {get;set;}
- Culture Culture {get;set;}
- Property Property {get;set;}

## Métodos (7)
- static Localization New()
- static Localization Novo()
- static Localization Load(string propertyName, object value)
- static Localization Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
