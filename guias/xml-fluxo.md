# XML de exportação de fluxo (ModeloImportacaoXml) — estrutura
Caminho: Guias > XML de fluxo

Arquivos em `XMLs para teste/` (5 a 13 MB cada, Supravizio 19.1.1, UTF-8 com BOM duplicado).
Nunca ler o XML cru: usar o resumo em `fluxos/<mesmo nome>.md` ou `python tools/fluxo.py bruto <xml> <Id|NOME>`.

## Raiz

```
ModeloImportacaoXml
├─ ListaSubProcessoDiagrama/SubProcessoDiagramaXml   (1 por arquivo; ~5% do tamanho)
│   ├─ NomeSubProcesso, traducoes
│   ├─ Diagrama/Figuras/Figura      posição e tamanho no desenho (Raia, atividades, links)
│   └─ SubProcesso
│       ├─ ClasseSubProcesso        Sigla, Descricao, OrgaoDono, Responsavel, RestricoesServicos
│       ├─ Atividades/Atividade     o fluxo em si
│       ├─ Gateways/Gateway
│       └─ Outputs
├─ ListaCustomProperty              catálogo GLOBAL de campos customizados (~80% do arquivo, igual em todos)
│   └─ CustomPropertyClassMember (ClassName) / CustomPropertyList / CustomProperty
├─ ListaBibliotecaScript/ScriptModule   Name + Source (biblioteca global de scripts)
├─ DesenhoProcessoString            XML embutido: Versao, ProcessoId, datas, Papeis do desenho
└─ VersaoSupravizio
```

Todo elemento traz `UseParentChangeLog`, `isLoading`, `isImporting` (ruído) e muitos `xsi:nil="true"`.

## Atividade

- `Tipo`: Tarefa, SubProcesso, EventoInicial, EventoFinal, FimCancelamento, LinkInicial,
  EventoIntermediarioMensagem, EventoIntermediarioTimer, EventoIntermediarioRegra.
- Ligações: `FluxosSaida/FluxoSequencia` (`AtividadeOrigemId` → `AtividadeDestinoId`).
- Quem executa: `PapelResponsavel` (→ `PapelClasseNegocio`: Tipo PessoaOrdemServico, RelacaoPessoas,
  Composto, Script...; `ScriptSelecaoAtores`); mensagens usam `PapelDestinatario` e `ModeloComunicado`.
- Scripts: `ScriptInicio`, `ScriptFim`, `ScriptValidacao`, `ScriptFormCarregado`, `ScriptEvento`.
- `Operacoes/OperacaoAtividade` (`Operacao/Codigo`): PR0001 Preencher Campos, PR0002 Aprovar,
  PR0004 Associar Itens Configuração.
  - `Campos/CampoPreenchimento`: `Nome` (nativo) ou `Nome=Customizado` + `NomeCustomizado`, `Rotulo`,
    `Obrigatorio`, `ScriptModificado`, `ScriptConfirmado`; colunas de listagem em `CampoPreenchimentoRegistro`.
  - `ClassesAnexos/ClasseAnexo` (+ `EscopoClasses`), `ClassesAprovacao`, `Aprovadores/Aprovador`,
    `CamposAprovacao`, `Relatorios`.
- Outros: `ValoresInputs/ValorInput` (`ExpressaoValor`), `PassagemItens`, `RetornoItens`,
  `AssociacoesSubprocesso`, `Acoes/AcaoAcordo`, `MotivoInterrupcaoSLA`, `TipoSolicitacao`,
  `ClassePesquisaSatisfacao`, `TiposAnexosMensagem`.

## Gateway

- `Tipo`: DataBasedExclusiveDecision ou EventBasedExclusiveDecision; `ExpressaoComparacaoDecision` (script).
- `Entradas/Receptor`: origem (`AtividadeId` ou `GatewayEntradaId`).
- `Alternativas/Emissor`: destino (`AtividadeId` ou `GatewaySaidaId`), `OperadorDecision`,
  `ReferenciaDecision` (rótulo), `ValorComparacaoDecision` (script), `SequenciaAvaliacao`.

## CustomProperty (campo customizado)

`Name` (usado em script), `Text` (rótulo), `Type` (String, Integer, Decimal, DateTime, Boolean,
RecordList, List), `Control` (TextBox, Memo, DropDownList, SearchList, DataGrid, CheckBox, DatePicker,
DateTimePicker, Label, ListBox), `TableName`/`TableColumn` (onde o valor é gravado, tabelas CP_*/CPE_*),
`Length`, `ListItems` (opções fixas separadas por `;`), `LookupScript`, `RecordColumns/RecordColumn`
(colunas de um DataGrid, cada uma com seu próprio controle e LookupScript).

## Formato do resumo em fluxos/*.md

Cabeçalho (sigla, versão, ids, dono, serviços) → `## Grafo do fluxo` (uma linha por nó, com papel
e destinos) → `## Gateways` → `## Atividades` (config fora do padrão, operações, campos, scripts
inteiros) → `## Papéis usados` → `## Campos customizados usados` → biblioteca referenciada.
Valores padrão e `false` são omitidos; se precisar do detalhe completo de um nó, usar `bruto`.
