# SessionObjectProxy (API de script)
Caminho: Catálogo > API de scripts > Venki.Core.Custom > SessionObjectProxy

class `Venki.Core.Custom.SessionObjectProxy` — core.dll v1.0.9039.38813

## Propriedades (5)
- object Item[string propertyName] {get;set;}
- bool Modified {get;}
- bool IsNew {get;}
- SessionObject Instance {get;}
- bool ReadOnly {get;}

## Métodos (4)
- object GetCustom(string propertyName)
- object GetCustom(string propertyName, object defaultValue)
- void SetCustom(string propertyName, object value)
- static void ApplyUpdates(SessionObjectProxy proxy)
