# FileType (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Dictionary.Custom > FileType

class `Venki.Services.Dictionary.Custom.FileType` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_filetype.md

## Propriedades (5)
- FileType FileTypeInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- bool CommentRequired {get;set;}
- bool PublicAccess {get;set;}

## Métodos (9)
- static FileType Load(int id)
- static FileType Carrega(int id)
- static FileType New()
- static FileType Novo()
- static FileType Load(string propertyName, object value)
- static FileType Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
