# FormularioRegistro (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Script > FormularioRegistro

class `Venki.Supravizio.Processo.Script.FormularioRegistro` — supravizio.dll v18.1.1.0

## Propriedades (8)
- Dictionary<string, ControleFormulario> Colunas {get;}
- OrdemServico OrdemServico {get;set;}
- ControleFormulario Item[string nomeCampo] {get;}
- bool PermiteExecutarScriptModificado {get;set;}
- bool IsModified {get;set;}
- object Valor {get;set;}
- bool NecessitaAtualizarFormulario {get;set;}
- string NomeControleFormularioExecucao {get;set;}

## Métodos (5)
- bool PossuiColuna(string nomeColuna)
- void AdicionaColuna(ControleFormulario controle)
- void ModificaVisibilidadeCampo(string campo, bool novoValor)
- void ModificaHabilitadoCampo(string campo, bool novoValor)
- void ModificaMascaraCampo(string campo, string mascara, bool incluiLiteral)
