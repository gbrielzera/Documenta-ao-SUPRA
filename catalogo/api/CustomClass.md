# CustomClass (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Dictionary.Custom > CustomClass

class `Venki.Services.Dictionary.Custom.CustomClass` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_customclass.md

## Propriedades (7)
- CustomClass CustomClassInstance {get;}
- int Id {get;set;}
- int ClassId {get;set;}
- string TypeFullName {get;set;}
- int DomainId {get;set;}
- Domain Domain {get;set;}
- Class Class {get;set;}

## Métodos (9)
- static CustomClass Load(int id)
- static CustomClass Carrega(int id)
- static CustomClass New()
- static CustomClass Novo()
- static CustomClass Load(string propertyName, object value)
- static CustomClass Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
