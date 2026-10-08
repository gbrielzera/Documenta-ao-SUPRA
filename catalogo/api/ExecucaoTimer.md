# ExecucaoTimer (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > ExecucaoTimer

class `Venki.Supravizio.Processo.Custom.ExecucaoTimer` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_execucaotimer.md

## Propriedades (4)
- ExecucaoTimer ExecucaoTimerInstance {get;}
- int AtividadeId {get;set;}
- DateTime DataHoraExecucao {get;set;}
- Atividade Atividade {get;set;}

## Métodos (7)
- static ExecucaoTimer New()
- static ExecucaoTimer Novo()
- static ExecucaoTimer Load(string propertyName, object value)
- static ExecucaoTimer Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
