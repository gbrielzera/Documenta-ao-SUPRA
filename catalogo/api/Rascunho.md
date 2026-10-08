# Rascunho (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Portal.Custom > Rascunho

class `Venki.Supravizio.Portal.Custom.Rascunho` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (8)
- Rascunho RascunhoInstance {get;}
- string InstanciaModuloUId {get;set;}
- string ReferenciaPaginaNome {get;set;}
- int Id {get;set;}
- int OcorrenciaId {get;set;}
- int PessoaId {get;set;}
- Ocorrencia Ocorrencia {get;set;}
- Pessoa Pessoa {get;set;}

## Métodos (9)
- static Rascunho Load(int id)
- static Rascunho Carrega(int id)
- static Rascunho New()
- static Rascunho Novo()
- static Rascunho Load(string propertyName, object value)
- static Rascunho Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
