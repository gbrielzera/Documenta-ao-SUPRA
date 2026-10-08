# Picture (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Dictionary.Custom > Picture

class `Venki.Services.Dictionary.Custom.Picture` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_picture.md

## Propriedades (12)
- Picture PictureInstance {get;}
- int Id {get;set;}
- string TextualRepresentation {get;set;}
- string Description {get;set;}
- int ClassId {get;set;}
- string KeyValue {get;set;}
- string Format {get;set;}
- object Content {get;set;}
- DateTime CreationDateTime {get;set;}
- DateTime? LastAccessDateTime {get;set;}
- int? Temporality {get;set;}
- Class Class {get;set;}

## Métodos (9)
- static Picture Load(int id)
- static Picture Carrega(int id)
- static Picture New()
- static Picture Novo()
- static Picture Load(string propertyName, object value)
- static Picture Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
