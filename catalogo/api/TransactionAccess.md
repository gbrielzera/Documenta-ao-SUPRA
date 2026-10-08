# TransactionAccess (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Security.Custom > TransactionAccess

class `Venki.Services.Security.Custom.TransactionAccess` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_transactionaccess.md

## Propriedades (6)
- TransactionAccess TransactionAccessInstance {get;}
- string UserSessionSessionId {get;}
- int TransactionId {get;}
- DateTime AccessDateTime {get;}
- UserSession UserSession {get;set;}
- Transaction Transaction {get;set;}

## Métodos (7)
- static TransactionAccess New()
- static TransactionAccess Novo()
- static TransactionAccess Load(string propertyName, object value)
- static TransactionAccess Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
