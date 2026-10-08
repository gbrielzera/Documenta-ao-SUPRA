# Transaction (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Custom > Transaction

class `Venki.Services.Custom.Transaction` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_transaction.md

## Propriedades (14)
- Transaction TransactionInstance {get;}
- int Id {get;set;}
- int ModuleId {get;set;}
- string ShortName {get;set;}
- bool Enabled {get;set;}
- string Url {get;set;}
- string Capabilities {get;set;}
- string Text {get;set;}
- string Description {get;set;}
- string OriginalText {get;set;}
- string OriginalDescription {get;set;}
- string IconName {get;set;}
- string AdapterCRUD {get;set;}
- Module Module {get;set;}

## Métodos (9)
- static Transaction Load(int id)
- static Transaction Carrega(int id)
- static Transaction New()
- static Transaction Novo()
- static Transaction Load(string propertyName, object value)
- static Transaction Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
