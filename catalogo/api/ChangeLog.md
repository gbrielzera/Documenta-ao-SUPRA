# ChangeLog (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Dictionary.Custom > ChangeLog

class `Venki.Services.Dictionary.Custom.ChangeLog` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_changelog.md

## Propriedades (12)
- ChangeLog ChangeLogInstance {get;}
- decimal Id {get;set;}
- DateTime DateTime {get;set;}
- int DomainId {get;set;}
- int ClassId {get;set;}
- int UserId {get;set;}
- int? ParentId {get;set;}
- string KeyValue {get;set;}
- string TextualRepresentation {get;set;}
- int Version {get;set;}
- SessionProxyList Items {get;}
- Class Class {get;set;}

## Métodos (8)
- static ChangeLog New()
- static ChangeLog Novo()
- static ChangeItem NewChangeItem(ChangeLog parentChangeLog)
- static ChangeLog Load(string propertyName, object value)
- static ChangeLog Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
