# AttachmentFile (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Dictionary.Custom > AttachmentFile

class `Venki.Services.Dictionary.Custom.AttachmentFile` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_attachmentfile.md

## Propriedades (14)
- AttachmentFile AttachmentFileInstance {get;}
- int Id {get;set;}
- string KeyValue {get;set;}
- string TextualRepresentation {get;set;}
- int ClassId {get;set;}
- string FileName {get;set;}
- int FileTypeId {get;set;}
- DateTime AttachDate {get;set;}
- int UserId {get;set;}
- string Comment {get;set;}
- string FullFileName {get;set;}
- Class Class {get;set;}
- FileType FileType {get;set;}
- User User {get;set;}

## Métodos (9)
- static AttachmentFile Load(int id)
- static AttachmentFile Carrega(int id)
- static AttachmentFile New()
- static AttachmentFile Novo()
- static AttachmentFile Load(string propertyName, object value)
- static AttachmentFile Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
