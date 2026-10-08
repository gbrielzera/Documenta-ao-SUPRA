# DesenhoProcesso (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > DesenhoProcesso

class `Venki.Supravizio.Processo.Custom.DesenhoProcesso` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_desenhoprocesso.md

## Propriedades (14)
- DesenhoProcesso DesenhoProcessoInstance {get;}
- int Id {get;set;}
- bool Ativo {get;set;}
- int Versao {get;set;}
- DateTime DataCriacao {get;set;}
- DateTime? DataAtivacao {get;set;}
- DateTime? DataDesativacao {get;set;}
- string Comentarios {get;set;}
- int ProcessoId {get;set;}
- int? AtivadorId {get;set;}
- SessionProxyList SubProcessos {get;}
- SessionProxyList Papeis {get;}
- Processo Processo {get;}
- Pessoa Ativador {get;set;}

## Métodos (2)
- static DesenhoProcesso Load(int id)
- static DesenhoProcesso Carrega(int id)
