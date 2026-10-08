# ScriptModule (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Dictionary.Custom > ScriptModule

class `Venki.Services.Dictionary.Custom.ScriptModule` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (6)
- ScriptModule ScriptModuleInstance {get;}
- int Id {get;set;}
- string Name {get;set;}
- string Source {get;set;}
- bool VisibleWebService {get;set;}
- bool GenerateWSLog {get;set;}

## Métodos (9)
- static ScriptModule Load(int id)
- static ScriptModule Carrega(int id)
- static ScriptModule New()
- static ScriptModule Novo()
- static ScriptModule Load(string propertyName, object value)
- static ScriptModule Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
