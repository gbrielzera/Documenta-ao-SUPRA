# Class (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Dictionary.Custom > Class

class `Venki.Services.Dictionary.Custom.Class` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_class.md

## Propriedades (20)
- Class ClassInstance {get;}
- int Id {get;set;}
- int ModuleId {get;set;}
- string Name {get;set;}
- bool LogChangeEnabled {get;set;}
- string OriginalText {get;set;}
- string Description {get;set;}
- bool LocalizeEnabled {get;set;}
- string Text {get;set;}
- string OriginalDescription {get;set;}
- int? ParentClassId {get;set;}
- bool OriginalLocalizeEnabled {get;set;}
- bool OriginalLogChangeEnabled {get;set;}
- string TableName {get;}
- bool? ExistsInCurrentVersion {get;set;}
- SessionProxyList Properties {get;}
- SessionProxyList CustomProperties {get;}
- SessionProxyList Events {get;}
- Module Module {get;set;}
- Class ParentClass {get;set;}

## Métodos (16)
- static Class Load(int id)
- static Class Carrega(int id)
- static Class New()
- static Class Novo()
- static Property NewProperty(Class parentClass)
- static CustomProperty NewCustomProperty(Class parentClass)
- static CustomPropertyScope NewCustomPropertyScope(CustomProperty parentCustomProperty)
- static RecordColumn NewRecordColumn(CustomProperty parentCustomProperty)
- static CustomEvent NewCustomEvent(Class parentClass)
- static CustomEventImplementation NewCustomEventImplementation(CustomEvent parentCustomEvent)
- static CustomEventArgs NewCustomEventArgs(CustomEvent parentCustomEvent)
- static Class Load(string propertyName, object value)
- static Class Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
