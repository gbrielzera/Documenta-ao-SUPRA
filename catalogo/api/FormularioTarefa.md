# FormularioTarefa (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Script > FormularioTarefa

class `Venki.Supravizio.Processo.Script.FormularioTarefa` — supravizio.dll v18.1.1.0

## Propriedades (8)
- Dictionary<string, ControleFormulario> Controles {get;}
- OrdemServico OrdemServico {get;set;}
- Type TipoControleNaoEncontrado {get;set;}
- ControleFormulario Item[string nomeCampo] {get;}
- bool PermiteExecutarScriptModificado {get;set;}
- bool IsModified {get;set;}
- bool NecessitaAtualizarFormulario {get;set;}
- string NomeControleFormularioExecucao {get;set;}

## Métodos (7)
- void ExibeMensagem(string mensagem)
- void ModificaVisibilidadeCampo(string campo, bool novoValor)
- void ModificaHabilitadoCampo(string campo, bool novoValor)
- void ModificaMascaraCampo(string campo, string mascara, bool incluiLiteral)
- bool PossuiControle(NomeCampo nomeCampo, string nomeCustomizado)
- void AdicionaControle(string nomeControle, ControleFormulario controle)
- ControleFormulario ObtemControleFormulario(object controleVisual)
