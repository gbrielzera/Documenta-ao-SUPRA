# EstiloModulo (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Portal.Custom > EstiloModulo

class `Venki.Supravizio.Portal.Custom.EstiloModulo` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (10)
- EstiloModulo EstiloModuloInstance {get;}
- int Id {get;set;}
- int DomainId {get;set;}
- string Descricao {get;set;}
- int ModuloId {get;set;}
- string Sigla {get;set;}
- bool DisponivelTablet {get;set;}
- bool DisponivelMobile {get;set;}
- bool DisponivelClassico {get;set;}
- Modulo Modulo {get;}

## Métodos (2)
- static EstiloModulo Load(int id)
- static EstiloModulo Carrega(int id)
