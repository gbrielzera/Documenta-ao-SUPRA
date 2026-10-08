# Software (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Configuracao.Custom > Software

class `Venki.Supravizio.Configuracao.Custom.Software` — supravizio.custom.dll v18.1.1.0
Herda de **ItemConfiguracao** (ver catalogo/api/ItemConfiguracao.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_software.md

## Propriedades (5)
- Software SoftwareInstance {get;}
- string Versao {get;set;}
- string ReferenciaLicenca {get;set;}
- int? CopiasLicenciadas {get;set;}
- int? InstalacoesAuditadas {get;set;}

## Métodos (9)
- static Software Load(int id)
- static Software Carrega(int id)
- static Software New()
- static Software Novo()
- static Software Load(string propertyName, object value)
- static Software Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
