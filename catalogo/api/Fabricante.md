# Fabricante (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Configuracao.Custom > Fabricante

class `Venki.Supravizio.Configuracao.Custom.Fabricante` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_fabricante.md

## Propriedades (5)
- Fabricante FabricanteInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- bool Ativo {get;set;}
- int DomainId {get;set;}

## Métodos (9)
- static Fabricante Load(int id)
- static Fabricante Carrega(int id)
- static Fabricante New()
- static Fabricante Novo()
- static Fabricante Load(string propertyName, object value)
- static Fabricante Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
