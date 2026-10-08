# ClasseApontamento (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > ClasseApontamento

class `Venki.Supravizio.Processo.Custom.ClasseApontamento` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_classeapontamento.md

## Propriedades (32)
- ClasseApontamento ClasseApontamentoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- string DescricaoCampoInteiro1 {get;set;}
- string DescricaoCampoInteiro2 {get;set;}
- string DescricaoCampoString1 {get;set;}
- string DescricaoCampoString2 {get;set;}
- string DescricaoCampoDataHora1 {get;set;}
- string DescricaoCampoDataHora2 {get;set;}
- string DescricaoCampoDecimal1 {get;set;}
- string DescricaoCampoDecimal2 {get;set;}
- string DescricaoCampoBooleano1 {get;set;}
- string DescricaoCampoBooleano2 {get;set;}
- int? TipoEventoId {get;set;}
- bool PermiteMotivoDigitado {get;set;}
- string Codigo {get;set;}
- bool PermiteMultiplosMotivos {get;set;}
- int? SequencialCampoInteiro1 {get;set;}
- int? SequencialCampoInteiro2 {get;set;}
- int? SequencialCampoString1 {get;set;}
- int? SequencialCampoString2 {get;set;}
- int? SequencialCampoDataHora1 {get;set;}
- int? SequencialCampoDataHora2 {get;set;}
- int? SequencialCampoDecimal1 {get;set;}
- int? SequencialCampoDecimal2 {get;set;}
- int? SequencialCampoBooleano1 {get;set;}
- int? SequencialCampoBooleano2 {get;set;}
- bool PermiteMultiplosApontamentos {get;set;}
- bool MotivoObrigatorio {get;set;}
- int DomainId {get;set;}
- SessionProxyList Motivos {get;}
- TipoEvento TipoEventoGerado {get;set;}

## Métodos (10)
- static ClasseApontamento Load(int id)
- static ClasseApontamento Carrega(int id)
- static ClasseApontamento New()
- static ClasseApontamento Novo()
- static MotivoClasseApontamento NewMotivoClasseApontamento(ClasseApontamento parentClasseApontamento)
- static ClasseApontamento Load(string propertyName, object value)
- static ClasseApontamento Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
