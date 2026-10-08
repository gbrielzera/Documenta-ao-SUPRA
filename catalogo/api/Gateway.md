# Gateway (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > Gateway

class `Venki.Supravizio.Processo.Custom.Gateway` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_gateway.md

## Propriedades (15)
- Gateway GatewayInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- int? EmissorId {get;set;}
- int SubProcessoId {get;set;}
- string ExpressaoComparacaoDecision {get;set;}
- string Referencia {get;set;}
- string Codigo {get;set;}
- string Configuracao {get;set;}
- string SeparadorSequencial {get;set;}
- string Tipo {get;set;}
- SessionProxyList Alternativas {get;}
- SessionProxyList Entradas {get;}
- SubProcesso SubProcesso {get;}
- Emissor EmissorDefault {get;set;}

## Métodos (2)
- static Gateway Load(int id)
- static Gateway Carrega(int id)
