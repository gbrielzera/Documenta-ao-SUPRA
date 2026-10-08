# ModeloComunicado (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > ModeloComunicado

class `Venki.Supravizio.Processo.Custom.ModeloComunicado` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_modelocomunicado.md

## Propriedades (4)
- ModeloComunicado ModeloComunicadoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- object Corpo {get;set;}

## Métodos (9)
- static ModeloComunicado Load(int id)
- static ModeloComunicado Carrega(int id)
- static ModeloComunicado New()
- static ModeloComunicado Novo()
- static ModeloComunicado Load(string propertyName, object value)
- static ModeloComunicado Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
