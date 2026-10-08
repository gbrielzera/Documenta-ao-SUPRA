# MacroProcesso (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo.Custom > MacroProcesso

class `Venki.Supravizio.Processo.Custom.MacroProcesso` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_macroprocesso.md

## Propriedades (5)
- MacroProcesso MacroProcessoInstance {get;}
- int Id {get;set;}
- string Descricao {get;set;}
- string DescricaoCliente {get;set;}
- SessionProxyList GruposEnvolvidos {get;}

## Métodos (10)
- static MacroProcesso Load(int id)
- static MacroProcesso Carrega(int id)
- static MacroProcesso New()
- static MacroProcesso Novo()
- static EnvolvimentoGrupo NewEnvolvimentoGrupo(MacroProcesso parentMacroProcesso)
- static MacroProcesso Load(string propertyName, object value)
- static MacroProcesso Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
