# CommandClass (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Dictionary.Custom > CommandClass

class `Venki.Services.Dictionary.Custom.CommandClass` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_commandclass.md

## Propriedades (8)
- CommandClass CommandClassInstance {get;}
- int Id {get;set;}
- int ClassId {get;set;}
- string Name {get;set;}
- string Description {get;set;}
- string Source {get;set;}
- string Binary {get;set;}
- Class Class {get;set;}

## Métodos (9)
- static CommandClass Load(int id)
- static CommandClass Carrega(int id)
- static CommandClass New()
- static CommandClass Novo()
- static CommandClass Load(string propertyName, object value)
- static CommandClass Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
