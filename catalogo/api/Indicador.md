# Indicador (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > Indicador

class `Venki.Supravizio.Processo.Custom.Indicador` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_indicador.md

## Propriedades (31)
- Indicador IndicadorInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- string ExpressaoSelecao {get;set;}
- string ExpressaoValor {get;set;}
- int GrupoIndicadorId {get;set;}
- int? OrdemServicoProcessoId {get;set;}
- int DomainId {get;set;}
- bool OrdemServicoFiltroAberta {get;set;}
- bool OrdemServicoFiltroFinalizadaSucesso {get;set;}
- bool OrdemServicoFiltroFinalizadaFalha {get;set;}
- bool OrdemServicoFiltroCancelada {get;set;}
- int? PesquisaClassePesquisaId {get;}
- bool OrdemServicoFiltroFinalizadaNReal {get;set;}
- bool PesquisaFiltroConcluida {get;set;}
- bool PesquisaFiltroCancelada {get;set;}
- bool PesquisaFiltroAndamento {get;set;}
- string Codigo {get;set;}
- string ReferenciaCalculo {get;set;}
- string FormulaFiltroComplementar {get;set;}
- string FormulaResponsavel {get;set;}
- string SentidoMelhor {get;set;}
- string Agregacao {get;set;}
- string Provedor {get;set;}
- string PesquisaTipoApuracao {get;set;}
- SessionProxyList ClassesConfiguracao {get;}
- SessionProxyList ClassesSubProcesso {get;}
- SessionProxyList GruposQuestoes {get;}
- GrupoIndicador GrupoIndicador {get;set;}
- Processo OrdemServicoProcesso {get;set;}
- ClassePesquisaSatisfacao PesquisaClassePesquisa {get;set;}

## Métodos (12)
- static Indicador Load(int id)
- static Indicador Carrega(int id)
- static Indicador New()
- static Indicador Novo()
- static ClasseConfiguracaoIndicador NewClasseConfiguracaoIndicador(Indicador parentIndicador)
- static ClasseSubProcessoIndicador NewClasseSubProcessoIndicador(Indicador parentIndicador)
- static GrupoQuestaoIndicador NewGrupoQuestaoIndicador(Indicador parentIndicador)
- static Indicador Load(string propertyName, object value)
- static Indicador Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
