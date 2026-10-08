# Hardware (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Configuracao.Custom > Hardware

class `Venki.Supravizio.Configuracao.Custom.Hardware` — supravizio.custom.dll v18.1.1.0
Herda de **ItemConfiguracao** (ver catalogo/api/ItemConfiguracao.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_hardware.md

## Propriedades (7)
- Hardware HardwareInstance {get;}
- string EtiquetaIdentificacao {get;set;}
- string Patrimonio {get;set;}
- int? LocalId {get;set;}
- string CodigoOCS {get;set;}
- int? MemoriaOCS {get;set;}
- Local Local {get;set;}

## Métodos (9)
- static Hardware Load(int id)
- static Hardware Carrega(int id)
- static Hardware New()
- static Hardware Novo()
- static Hardware Load(string propertyName, object value)
- static Hardware Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
