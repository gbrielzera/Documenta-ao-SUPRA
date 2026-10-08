# CustomProperty (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Dictionary.Custom > CustomProperty

class `Venki.Services.Dictionary.Custom.CustomProperty` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_customproperty.md

## Propriedades (28)
- CustomProperty CustomPropertyInstance {get;}
- int Id {get;set;}
- int ClassId {get;set;}
- string Name {get;set;}
- string Text {get;set;}
- string Description {get;set;}
- string TableName {get;set;}
- string TableColumn {get;set;}
- int DomainId {get;set;}
- int Sequence {get;set;}
- string ControlUrl {get;set;}
- bool Visible {get;set;}
- bool Enabled {get;set;}
- int? Height {get;set;}
- int? Width {get;set;}
- string ListItems {get;set;}
- int? ClassReferenceId {get;set;}
- int? Length {get;set;}
- string LookupScript {get;set;}
- bool Invalid {get;set;}
- bool ShowInListView {get;set;}
- bool IsCripto {get;set;}
- string Type {get;set;}
- SessionProxyList Scopes {get;}
- SessionProxyList RecordColumns {get;}
- Class Class {get;}
- Domain Domain {get;set;}
- Class ClassReference {get;set;}

## Métodos (2)
- static CustomProperty Load(int id)
- static CustomProperty Carrega(int id)
