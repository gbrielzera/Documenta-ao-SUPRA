# MotivoInterrupcaoSLA (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > MotivoInterrupcaoSLA

class `Venki.Supravizio.Recurso.Custom.MotivoInterrupcaoSLA` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_motivointerrupcaosla.md

## Propriedades (5)
- MotivoInterrupcaoSLA MotivoInterrupcaoSLAInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- bool ComentarioObrigatorio {get;set;}
- int? TempoPadrao {get;set;}

## Métodos (9)
- static MotivoInterrupcaoSLA Load(int id)
- static MotivoInterrupcaoSLA Carrega(int id)
- static MotivoInterrupcaoSLA New()
- static MotivoInterrupcaoSLA Novo()
- static MotivoInterrupcaoSLA Load(string propertyName, object value)
- static MotivoInterrupcaoSLA Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
