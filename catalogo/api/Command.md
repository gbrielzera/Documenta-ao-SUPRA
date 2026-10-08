# Command (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Custom > Command

class `Venki.Services.Custom.Command` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_command.md

## Propriedades (10)
- Command CommandInstance {get;}
- int Id {get;set;}
- string Text {get;set;}
- int? ParentCommandId {get;set;}
- int? TransactionId {get;set;}
- int Sequence {get;set;}
- int? UserId {get;set;}
- Transaction Transaction {get;set;}
- Command ParentCommand {get;set;}
- User User {get;set;}

## Métodos (9)
- static Command Load(int id)
- static Command Carrega(int id)
- static Command New()
- static Command Novo()
- static Command Load(string propertyName, object value)
- static Command Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
