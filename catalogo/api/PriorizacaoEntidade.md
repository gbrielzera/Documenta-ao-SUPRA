# PriorizacaoEntidade (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > PriorizacaoEntidade

class `Venki.Supravizio.Processo.Custom.PriorizacaoEntidade` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_priorizacaoentidade.md

## Propriedades (6)
- PriorizacaoEntidade PriorizacaoEntidadeInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- string Codigo {get;set;}
- int DomainId {get;set;}
- SessionProxyList Fatores {get;}

## Métodos (10)
- static PriorizacaoEntidade Load(int id)
- static PriorizacaoEntidade Carrega(int id)
- static PriorizacaoEntidade New()
- static PriorizacaoEntidade Novo()
- static FatorPrioridade NewFatorPrioridade(PriorizacaoEntidade parentPriorizacaoEntidade)
- static PriorizacaoEntidade Load(string propertyName, object value)
- static PriorizacaoEntidade Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
