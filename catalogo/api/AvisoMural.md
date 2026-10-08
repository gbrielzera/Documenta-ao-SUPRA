# AvisoMural (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > AvisoMural

class `Venki.Supravizio.Processo.Custom.AvisoMural` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.

## Propriedades (20)
- AvisoMural AvisoMuralInstance {get;}
- int Id {get;set;}
- string Mensagem {get;set;}
- int GrupoTrabalhoId {get;set;}
- int? OcorrenciaId {get;}
- int AutorId {get;set;}
- bool VisivelPortal {get;set;}
- DateTime? DataLimite {get;set;}
- DateTime DataInicio {get;set;}
- bool Desativar {get;set;}
- string MensagemPortal {get;set;}
- int? AtividadeId {get;}
- int? ConhecimentoId {get;set;}
- DateTime? DataHoraRegistro {get;set;}
- SessionProxyList Destinatarios {get;}
- Pessoa Autor {get;set;}
- GrupoTrabalho GrupoTrabalho {get;set;}
- Ocorrencia Ocorrencia {get;set;}
- Atividade Atividade {get;set;}
- Conhecimento Conhecimento {get;set;}

## Métodos (10)
- static AvisoMural Load(int id)
- static AvisoMural Carrega(int id)
- static AvisoMural New()
- static AvisoMural Novo()
- static DestinatarioAviso NewDestinatarioAviso(AvisoMural parentAvisoMural)
- static AvisoMural Load(string propertyName, object value)
- static AvisoMural Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
