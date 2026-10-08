# Message (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Custom > Message

class `Venki.Services.Custom.Message` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_message.md

## Propriedades (33)
- Message MessageInstance {get;}
- int DomainId {get;set;}
- int Id {get;set;}
- string Subject {get;set;}
- string Body {get;set;}
- DateTime RequestDate {get;set;}
- string RecoveryCode {get;set;}
- string FromAddress {get;set;}
- string MimeFormat {get;set;}
- bool RequestReadReceipt {get;set;}
- string FromName {get;set;}
- string ErrorDetails {get;set;}
- int? InitialMessageId {get;set;}
- string KeyValue {get;set;}
- string TextualRepresention {get;set;}
- int? AssociatedObjectClassId {get;set;}
- string Parameters {get;set;}
- string ParamInfo {get;set;}
- DateTime? TemporalityExpirationDate {get;set;}
- int? TemporalityClassId {get;set;}
- int? TemporalityId {get;set;}
- string ReplyAddress {get;set;}
- DateTime? ScheduledDate {get;set;}
- int? AssociatedObjectId {get;set;}
- string OriginalAnswer {get;set;}
- string OriginalFromAddress {get;set;}
- string Status {get;set;}
- string Priority {get;set;}
- SessionProxyList Recipients {get;}
- SessionProxyList Attachments {get;}
- Class TemporalityClass {get;set;}
- Class AssociatedObjectClass {get;set;}
- Message InitialMessage {get;set;}

## Métodos (11)
- static Message Load(int id)
- static Message Carrega(int id)
- static Message New()
- static Message Novo()
- static Recipient NewRecipient(Message parentMessage)
- static Attachment NewAttachment(Message parentMessage)
- static Message Load(string propertyName, object value)
- static Message Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
