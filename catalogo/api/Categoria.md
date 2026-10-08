# Categoria (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > Categoria

class `Venki.Supravizio.Processo.Custom.Categoria` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_categoria.md

## Propriedades (8)
- Categoria CategoriaInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- bool Ativo {get;set;}
- int Vermelho {get;set;}
- int Verde {get;set;}
- int Azul {get;set;}
- bool VisivelPainelWorkspace {get;set;}

## Métodos (9)
- static Categoria Load(int id)
- static Categoria Carrega(int id)
- static Categoria New()
- static Categoria Novo()
- static Categoria Load(string propertyName, object value)
- static Categoria Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
