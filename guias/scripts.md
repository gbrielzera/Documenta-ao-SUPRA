# Scripts no Supravizio (IronPython) — guia rápido
Caminho: Guias > Scripts

Linguagem: IronPython (sintaxe Python 2 + classes .NET). O editor insere sozinho o
preâmbulo (`import clr`, `from System import *`, imports de `Venki.Supravizio...Custom`)
e a linha `# INICIO SCRIPT USUARIO`; escreva só o que vem depois dela.

Antes de escrever um script, confira sempre:
1. `guias/scripts_contexto.md` — objetos e membros realmente usados em cada tipo de script, com exemplos reais.
2. Um fluxo parecido em `fluxos/` (`python tools/buscar.py "termo" -t fluxo`).
3. A página oficial do objeto em `docs/` (tabela abaixo).

## Onde cada script roda e o que está disponível

| Script (tag no XML) | Onde se configura | Variáveis específicas | Página oficial |
|---|---|---|---|
| ScriptInicio | Tarefa: ao iniciar | `OrdemServico`; `AvancaProximaAtividade = True` avança sozinho | docs/tarefas.md |
| ScriptValidacao | Tarefa: antes de avançar (por padrão roda também na finalização) | `Criticas.AdicionaPendencia(msg)` bloqueia; `Criticas.AdicionaAviso(msg)` | docs/tarefas.md |
| ScriptFim | Tarefa: ao finalizar (manual ou automático) | `OrdemServico` | docs/tarefas.md |
| Script Volta | Tarefa: quando o fluxo volta para ela | `OrdemServico` | docs/tarefas.md |
| ScriptFormCarregado | Tarefa: uma vez, ao abrir o formulário | `Formulario["CAMPO"].Visivel/.Habilitado/.Valor/.Itens`; `Formulario.ExibeMensagem(...)` | docs/utilizacao_de_scripts_em_data_.md |
| ScriptModificado (campo) | Entrada de dados: a cada mudança do campo | `Formulario`, `Controle` (o próprio campo) | docs/topicos_avancados_campos.md |
| ScriptModificado (coluna de listagem) | Listagem de registros: ao editar linha | `Formulario`, `Controle`, `FormularioRegistro["COLUNA"]` | docs/topicos_avancados_listagem.md |
| ScriptAdicionado | Listagem: ao adicionar linha | `Formulario`, `Tabela` (DataTable), `NovoRegistro`, `Posicao` | docs/utilizacao_de_scripts_em_data_.md |
| ScriptConfirmado | Listagem: ao confirmar linha | `Formulario`, `Registro`, `Cancela = True` desfaz | docs/utilizacao_de_scripts_em_data_.md |
| Script Removido | Listagem: ao remover linha | `Formulario`, `Tabela`, `RegistroRemovido`, `Posicao` | docs/utilizacao_de_scripts_em_data_.md |
| LookupScript | Campo customizado (DropDownList, SearchList, coluna de grid) | atribuir `Itens` (DataTable); em SearchList: `EntradaUsuario`, `ValorCorrente` | docs/controle_searchlist.md, docs/topicos_avancados_campos.md |
| ScriptSelecaoAtores | Papel "customizado por script" | `Atores.Adiciona(pessoa, "motivo")` | docs/customizado_por_script.md |
| ScriptEvento | Evento intermediário de mensagem | `Mensagem.Complemento1..n`, `.Assunto`, `.Corpo`, `.Destinatarios` | docs/uso_complementos_comunicados.md |
| ExpressaoComparacaoDecision | Gateway | expressão avaliada, ex.: `OrdemServico["CAMPO"]` | docs/objetos_gateway.md |
| ValorComparacaoDecision | Alternativa do gateway | literal/expressão comparada (OperadorDecision) | docs/objetos_emissor.md |
| Source | Biblioteca de Scripts (só `def`s) | importada pelo menu "Importar bibliotecas de scripts" | docs/biblioteca_de_scripts.md |

## Objetos globais (Recursos Avançados)

| Objeto | Para quê | Página |
|---|---|---|
| `DB` | `ExecuteDataTable(sql[, database])`, `ExecuteScalar`, `ExecuteNonQuery`, `ExecuteStoredProc`, `NewDBInputParam`... | docs/objeto_db.md e docs/db_*.md |
| `Utils` | `LogError`, `LogInformation`, `LogWarning`, `SendMail`, `IF`; nos fluxos reais também `Utils.ExecuteDataTable/ExecuteScalar` | docs/utils.md |
| `AD` / `LDAP` | Active Directory e OpenLDAP (criar usuário, grupos, propriedades) | docs/objeto_ad.md, docs/objeto_ldap.md |
| `Webservices` | `LoadWebService` (SOAP) | docs/webservices.md, docs/loadwebservice.md |
| PowerShell | `PSExecuteCmdlet` | docs/objeto_powershell.md |
| Jobs | scripts agendados | docs/recursos_avancados_jobs_customizados.md |

Chamadas REST nos fluxos reais usam .NET direto (`HttpClient`, `StringContent`,
`AuthenticationHeaderValue`, `Newtonsoft.Json`): ver `catalogo/biblioteca/api*.py`.
Web services do próprio Supravizio (abrir OS de fora, token): docs/web_services.md,
docs/realizando_chamadas_web_servic.md, docs/iniciador_por_mensagem.md.

## Campos da Ordem de Serviço em script

- Nativos: propriedades do objeto (`OrdemServico.Numero`, `.Cliente`, `.Favorecido`, `.Responsavel`,
  `.Servico`, `.ClasseSubProcesso`...). Lista: docs/objetos_ordemservico.md e docs/objetos_ocorrencia.md.
- Customizados: `OrdemServico["NOME"]` ou `OrdemServico.GetCustom("NOME")` / `SetCustom("NOME", valor)`.
  Campo do tipo listagem devolve DataTable (`.Rows.Count`, `AdicionaLinhaRegistro`).
- O NOME é o `Name` do campo customizado: procure em `catalogo/campos.tsv` (traz tipo, controle e tabela/coluna física).
- No formulário aberto use `Formulario["NOME"].Valor`; fora dele, `OrdemServico[...]`.

## Regras ao responder

- Não inventar método ou propriedade. Se não aparece em `docs/` nem em `guias/scripts_contexto.md`
  nem em algum fluxo, dizer que não foi encontrado e sugerir conferir no autocompletar do Editor de Scripts.
- Indentação com 4 espaços; nada de f-string, `print()` como função ou recursos de Python 3.
- SQL dentro de script: sintaxe Oracle; conferir tabela e coluna em `catalogo/schema.txt` antes de usar.
- Citar de onde veio cada padrão (arquivo de docs ou fluxo de origem).
