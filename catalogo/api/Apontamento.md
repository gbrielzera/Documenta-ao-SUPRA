# Apontamento (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > Apontamento

class `Venki.Supravizio.Processo.Custom.Apontamento` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_apontamento.md

## Propriedades (20)
- Apontamento ApontamentoInstance {get;}
- DateTime DataHoraApontamento {get;set;}
- int? ClasseApontamentoId {get;set;}
- int ResponsavelId {get;set;}
- int? CampoInteiro1 {get;set;}
- int? CampoInteiro2 {get;set;}
- string CampoString1 {get;set;}
- string CampoString2 {get;set;}
- DateTime? CampoDataHora1 {get;set;}
- DateTime? CampoDataHora2 {get;set;}
- decimal? CampoDecimal1 {get;set;}
- decimal? CampoDecimal2 {get;set;}
- bool? CampoBooleano1 {get;set;}
- bool? CampoBooleano2 {get;set;}
- int Id {get;set;}
- int DomainId {get;set;}
- string Situacao {get;set;}
- SessionProxyList Motivos {get;}
- ClasseApontamento ClasseApontamento {get;set;}
- Pessoa Responsavel {get;set;}

## Métodos (10)
- static Apontamento Load(int id)
- static Apontamento Carrega(int id)
- static Apontamento New()
- static Apontamento Novo()
- static MotivoApontamento NewMotivoApontamento(Apontamento parentApontamento)
- static Apontamento Load(string propertyName, object value)
- static Apontamento Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
