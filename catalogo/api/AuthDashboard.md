# AuthDashboard (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > AuthDashboard

class `Venki.Supravizio.Processo.Custom.AuthDashboard` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (7)
- AuthDashboard AuthDashboardInstance {get;}
- int GrupoTrabalhoId {get;set;}
- int DashboardId {get;set;}
- bool IncluiSubniveis {get;set;}
- bool ApenasCoordenadores {get;set;}
- GrupoTrabalho GrupoTrabalho {get;set;}
- Dashboard Dashboard {get;set;}

## Métodos (7)
- static AuthDashboard New()
- static AuthDashboard Novo()
- static AuthDashboard Load(string propertyName, object value)
- static AuthDashboard Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
