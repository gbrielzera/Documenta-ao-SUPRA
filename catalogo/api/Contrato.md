# Contrato (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > Contrato

class `Venki.Supravizio.Recurso.Custom.Contrato` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_contrato.md

## Propriedades (23)
- Contrato ContratoInstance {get;}
- string Descricao {get;set;}
- DateTime DataInicioValidade {get;set;}
- DateTime DataFimValidade {get;set;}
- int ContratanteId {get;set;}
- int FornecedorId {get;set;}
- int Id {get;set;}
- string CodigoReferencia {get;set;}
- int ResponsavelId {get;set;}
- string ResponsavelFornecedor {get;set;}
- string ContatoFornecedor {get;set;}
- int DomainId {get;set;}
- int? PlanoGestaoId {get;set;}
- bool PublicaVigenciaAA {get;set;}
- string FormaApontamento {get;set;}
- SessionProxyList RecursosAplicados {get;}
- SessionProxyList Items {get;}
- SessionProxyList TiposApontamento {get;}
- SessionProxyList ContratoServicos {get;}
- Pessoa Responsavel {get;set;}
- Fornecedor Fornecedor {get;set;}
- Empresa Contratante {get;set;}
- PlanoGestao PlanoGestao {get;set;}

## Métodos (15)
- static Contrato Load(int id)
- static Contrato Carrega(int id)
- static Contrato New()
- static Contrato Novo()
- static RecursoAplicado NewRecursoAplicado(Contrato parentContrato)
- static ContratoTecnico NewContratoTecnico(RecursoAplicado parentRecursoAplicado)
- static ContratoItem NewContratoItem(Contrato parentContrato)
- static TipoApontamentoContrato NewTipoApontamentoContrato(Contrato parentContrato)
- static RestricaoHorarioApontamento NewRestricaoHorarioApontamento(TipoApontamentoContrato parentTipoApontamentoContrato)
- static ContratoServico NewContratoServico(Contrato parentContrato)
- static Contrato Load(string propertyName, object value)
- static Contrato Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
