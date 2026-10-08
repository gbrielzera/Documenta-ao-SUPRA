# ExceptionClass (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Dictionary.Custom > ExceptionClass

class `Venki.Services.Dictionary.Custom.ExceptionClass` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_exceptionclass.md

## Propriedades (13)
- ExceptionClass ExceptionClassInstance {get;}
- int Id {get;set;}
- string Code {get;set;}
- string Message {get;set;}
- string Cause {get;set;}
- string Effect {get;set;}
- string Action {get;set;}
- string OriginalMessage {get;set;}
- string OriginalCause {get;set;}
- string OriginalEffect {get;set;}
- string OriginalAction {get;set;}
- int ClassId {get;set;}
- Class Class {get;set;}

## Métodos (9)
- static ExceptionClass Load(int id)
- static ExceptionClass Carrega(int id)
- static ExceptionClass New()
- static ExceptionClass Novo()
- static ExceptionClass Load(string propertyName, object value)
- static ExceptionClass Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
