# ApontamentoResponsavel (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > ApontamentoResponsavel

class `Venki.Supravizio.Processo.Custom.ApontamentoResponsavel` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_apontamentoresponsavel.md

## Propriedades (9)
- ApontamentoResponsavel ApontamentoResponsavelInstance {get;}
- int ResponsavelId {get;set;}
- DateTime DataHoraInicio {get;set;}
- int OcorrenciaId {get;set;}
- bool ResponsavelAtendePapel {get;set;}
- string ExplicacaoAtor {get;set;}
- int Sequencial {get;set;}
- Pessoa Responsavel {get;set;}
- Ocorrencia Ocorrencia {get;set;}

## Métodos (7)
- static ApontamentoResponsavel New()
- static ApontamentoResponsavel Novo()
- static ApontamentoResponsavel Load(string propertyName, object value)
- static ApontamentoResponsavel Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
