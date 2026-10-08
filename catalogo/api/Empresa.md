# Empresa (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > Empresa

class `Venki.Supravizio.Recurso.Custom.Empresa` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_empresa.md

## Propriedades (11)
- Empresa EmpresaInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- string Sigla {get;set;}
- bool Ativo {get;set;}
- int? GrupoEmpresaId {get;set;}
- int DomainId {get;set;}
- int? FatorPrioridadeId {get;set;}
- string EnderecoAD {get;set;}
- GrupoEmpresa GrupoEmpresas {get;set;}
- FatorPrioridade FatorPrioridade {get;set;}

## Métodos (10)
- static Empresa Load(int id)
- static Empresa Carrega(int id)
- static Empresa New()
- static Empresa Novo()
- static Empresa Load(string propertyName, object value)
- static Empresa Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
- int ObtemValorFatorPrioridade(int valorDefault)
