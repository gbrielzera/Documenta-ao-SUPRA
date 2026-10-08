# ApontamentoOcorrencia (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > ApontamentoOcorrencia

class `Venki.Supravizio.Processo.Custom.ApontamentoOcorrencia` — supravizio.custom.dll v18.1.1.0
Herda de **Apontamento** (ver catalogo/api/Apontamento.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_apontamentoocorrencia.md

## Propriedades (3)
- ApontamentoOcorrencia ApontamentoOcorrenciaInstance {get;}
- int OcorrenciaId {get;set;}
- Ocorrencia Ocorrencia {get;set;}

## Métodos (9)
- static ApontamentoOcorrencia Load(int id)
- static ApontamentoOcorrencia Carrega(int id)
- static ApontamentoOcorrencia New()
- static ApontamentoOcorrencia Novo()
- static ApontamentoOcorrencia Load(string propertyName, object value)
- static ApontamentoOcorrencia Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
