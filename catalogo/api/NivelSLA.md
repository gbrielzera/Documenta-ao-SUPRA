# NivelSLA (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > NivelSLA

class `Venki.Supravizio.Processo.Custom.NivelSLA` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_nivelsla.md

## Propriedades (7)
- NivelSLA NivelSLAInstance {get;}
- int DomainId {get;set;}
- int Id {get;set;}
- int Sequencial {get;set;}
- int? PercentualTempoTotal {get;set;}
- bool VisivelPainelWorkspace {get;set;}
- string CorIndicadorGrafico {get;set;}

## Métodos (9)
- static NivelSLA Load(int id)
- static NivelSLA Carrega(int id)
- static NivelSLA New()
- static NivelSLA Novo()
- static NivelSLA Load(string propertyName, object value)
- static NivelSLA Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
