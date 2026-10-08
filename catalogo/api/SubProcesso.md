# SubProcesso (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > SubProcesso

class `Venki.Supravizio.Processo.Custom.SubProcesso` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_subprocesso.md

## Propriedades (9)
- SubProcesso SubProcessoInstance {get;}
- int Id {get;set;}
- int ClasseSubProcessoId {get;set;}
- int DesenhoProcessoId {get;set;}
- SessionProxyList Atividades {get;}
- SessionProxyList Gateways {get;}
- SessionProxyList Outputs {get;}
- DesenhoProcesso DesenhoProcesso {get;}
- ClasseSubProcesso ClasseSubProcesso {get;set;}

## Métodos (2)
- static SubProcesso Load(int id)
- static SubProcesso Carrega(int id)
