# Module (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Custom > Module

class `Venki.Services.Custom.Module` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_module.md

## Propriedades (12)
- Module ModuleInstance {get;}
- int Id {get;set;}
- int? CommandRootId {get;set;}
- string Name {get;set;}
- string ShortName {get;set;}
- bool Enabled {get;set;}
- string Text {get;set;}
- string Description {get;set;}
- string OriginalText {get;set;}
- string OriginalDescription {get;set;}
- string ParameterClass {get;set;}
- Command CommandRoot {get;set;}

## Métodos (9)
- static Module Load(int id)
- static Module Carrega(int id)
- static Module New()
- static Module Novo()
- static Module Load(string propertyName, object value)
- static Module Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
