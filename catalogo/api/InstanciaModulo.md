# InstanciaModulo (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Portal.Custom > InstanciaModulo

class `Venki.Supravizio.Portal.Custom.InstanciaModulo` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (16)
- InstanciaModulo InstanciaModuloInstance {get;}
- int Id {get;set;}
- string Titulo {get;set;}
- int? ModuloId {get;set;}
- int PaginaId {get;set;}
- int? InstanciaModuloReferenteId {get;set;}
- object Configuracao {get;set;}
- bool Habilitado {get;set;}
- string ZoneUID {get;set;}
- int? EstiloModuloId {get;set;}
- string UId {get;set;}
- SessionProxyList PermissoesModulos {get;}
- Pagina Pagina {get;}
- Modulo Modulo {get;set;}
- InstanciaModulo InstanciaModuloReferente {get;set;}
- EstiloModulo EstiloModulo {get;set;}

## Métodos (2)
- static InstanciaModulo Load(int id)
- static InstanciaModulo Carrega(int id)
