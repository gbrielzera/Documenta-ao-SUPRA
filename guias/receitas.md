# Receitas — perguntas frequentes já resolvidas
Caminho: Guias > Receitas

Respostas curtas e verificadas para as dúvidas mais comuns. Cada receita indica a fonte:
**[doc]** = documentação oficial; **[fluxo]** = padrão observado nos fluxos reais do cliente
(não documentado oficialmente); **[api]** = assinatura confirmada nas DLLs do Client v18.1.1
(guias/api_scripts.md), sem garantia de comportamento além da assinatura. Nomes de campos são exemplos; confira em `catalogo/campos.tsv`.

## 1. Importar um fluxo exportado (ex.: de produção) na árvore do Process Explorer
[doc] docs/importacao.md
1. Origem e destino precisam estar na mesma versão do Supravizio.
2. No destino, abrir o Editor de Processos. Se o processo não existe, criar em **Novo Processo**
   (já nasce com uma versão **Em Edição**); se existe, botão direito no processo > **Nova Versão**.
3. Botão direito na versão **Em Edição** > **Importar** > escolher o XML.
4. Selecionar os subprocessos a importar.
5. Revisar a tela **Pendências de Importação** (cadastros que serão criados/alterados). Se houver
   mensagem de categoria **Erro**, a importação não é permitida. Clicar em **Confirmar Importação**.
6. Botão direito na versão > **Validar Versão**; sem pendências, **Ativar a versão**.
Atenção: o importador cria cadastros novos, mas não altera existentes (exceto campos customizados).
Scripts são copiados como estão: campos, ids e cadastros citados neles podem não existir no destino.
Bibliotecas de script com o mesmo nome são sobrescritas. Revisar papéis, serviços, modelos de
comunicado, grupos de trabalho e motivos de interrupção de ANS.

## 2. Criar um fluxo do zero
[doc] docs/criando_um_processo.md, docs/criando_um_sub-processo.md, docs/criando_fluxos_de_processos.md, docs/tutorial_01.md
1. Editor de Processos > Process Explorer > botão de novo Processo (ou **Nova Versão** em um existente).
2. Botão direito na versão Em Edição > **Adicionar novo Subprocesso**; preencher o cadastro do
   Tipo de Subprocesso (Descrição, Nome abreviado = sigla usada em scripts, Órgão proprietário...).
3. No diagrama, pela Toolbox: Evento Inicial, Tarefas, Desvios, Evento Final; ligar com **Fluxo**.
4. Em cada tarefa: papel responsável, Data Objects (Entrada de Dados, Itens de Configuração, Aprovação) e scripts.
5. Associar um Serviço ao subprocesso (docs/tutorial_02.md), salvar, **Validar Versão**, **Ativar**.

## 3. Esconder, mostrar, habilitar ou desabilitar um campo
[doc] docs/utilizacao_de_scripts_em_data_.md, docs/topicos_avancados_campos.md
```python
# Script Formulário carregado (estado inicial) ou Script Modificado (reação a outro campo)
Formulario["NOME_DO_CAMPO"].Visivel = True       # ou False
Formulario["NOME_DO_CAMPO"].Habilitado = False   # ou True

# forma condicional explícita (preferir esta ao responder: é a que o usuário usa)
if Formulario["POSSUI_DESPESAS"].Valor == True:
    Formulario["DESPESAS"].Visivel = True
else:
    Formulario["DESPESAS"].Visivel = False
```
A doc oficial também usa a forma compacta, equivalente ao if/else acima:
`Formulario["DESPESAS"].Visivel = Formulario["POSSUI_DESPESAS"].Valor == True`.
Dentro do Script Modificado, `Controle` é o próprio campo (`Controle.Valor`).
Sem script: propriedades **Visível**/**Habilitado** do campo e a Visualização Condicional (docs/visualizacao_condicional.md).
[api] Fora do formulário (ex.: Script Início): `OrdemServico.ModificaCampoFormularioVisivel("CAMPO", True)`,
`OrdemServico.ModificaCampoFormularioHabilitado("CAMPO", False)` e
`OrdemServico.ModificaCampoFormularioMascara("CAMPO", "mascara", incluiLiteral)`.
No formulário também existem `Formulario.ModificaVisibilidadeCampo("CAMPO", bool)` e `ModificaHabilitadoCampo`.

## 4. Criar um campo customizado
[doc] docs/criacao_de_campos_customizados_os.md, docs/criando_propriedade_customizada.md, docs/armazenando_dados_de_campos_cu.md
- Pelo Editor de Processos: menu **Campos** > Novo. Preencher Nome (formato de coluna de banco),
  Descrição resumida (rótulo), Tipo, Controle, largura; para listas, **Script para a recuperação de opções**.
- Pelo cadastro: Utilitários > Dicionário de Classes > classe (ex.: `Venki.Supravizio.Processo.OrdemServico`)
  > aba Propriedades Customizadas > Novo.
- Para usar no fluxo: Data Object **Entrada de Dados** na tarefa > **Campos para Preenchimento** >
  adicionar o campo e definir Tipo de preenchimento (Obrigatório, Opcional, Opcional recomendado).

## 5. Criar um papel
[doc] docs/cadastrar_usuario_2_2.md, docs/tipos_papeis.md
Editor de Processos > comando **Papéis** > Novo. Escolher o tipo: Relação de Grupos de Trabalho,
Relação de Pessoas e filas, Filtro no cadastro de pessoas, Relação de Áreas, Pessoa relacionada na
ocorrência, Item de configuração anexado, Composto por outros papéis, Customizado por script,
Execução de Tarefa do Processo. Definir o Critério de Seleção Final (menor quantidade de ocorrências,
fila, ou todas as pessoas). Depois usar o papel como responsável de tarefa, aprovador, destinatário
de comunicado ou cliente autorizado do iniciador.

## 6. SQL: nome do colaborador pela matrícula
[fluxo] MATRICULA é campo customizado de Pessoa, gravado em `CP_PESSOA.MATRICULA` (String).
```sql
SELECT P.NOME
FROM PESSOA P
INNER JOIN CP_PESSOA CP ON CP.ID_PESSOA = P.ID_PESSOA
WHERE CP.MATRICULA = '123456'
```
Em script: `nome = DB.ExecuteScalar("SELECT P.NOME FROM PESSOA P INNER JOIN CP_PESSOA CP ON CP.ID_PESSOA = P.ID_PESSOA WHERE CP.MATRICULA = '" + matricula + "'")`.
Os fluxos também usam a view do cliente `CAD_FUNCIONARIO_V` (NOME, MATRICULA, DATA_DE_DEMISSAO, STATUS_MATRICULA), fora do modelo oficial.

## 7. Papel por script: todas as pessoas cujo nome começa com "A"
[doc] docs/customizado_por_script.md + [fluxo] padrão DataTable → Pessoa.Carrega → Atores.Adiciona
```python
lista = DB.ExecuteDataTable("SELECT ID_PESSOA FROM PESSOA WHERE ATIVO = 'Sim' AND UPPER(NOME) LIKE 'A%'")
for linha in lista.Rows:
    pessoa = Pessoa.Carrega(Convert.ToInt32(linha["ID_PESSOA"]))
    Atores.Adiciona(pessoa, "Nome iniciado com A")
```
Tipo do papel: Customizado por script; critério final "Todas as pessoas recuperadas pela regra".
Nos XMLs o preâmbulo traz `from Venki.Supravizio.Recurso.Custom import Pessoa`.

## 8. Tipos de campo
[doc] docs/criacao_de_campos_customizados_os.md, docs/tipos_de_controle_os.md
- Tipos de dado: Alfanumérico, Data e Hora, Decimal (15 dígitos, 2 casas), Inteiro, Lógico,
  Listagem de Objetos, Listagem de Registros.
- Controles: TextBox, Memo, Label, CheckBox, Combobox, SearchList, DatePicker, DateTimePicker, Grid.
- No XML: String, DateTime, Decimal, Integer, Boolean, List, RecordList; controles DropDownList
  (Combobox), DataGrid (Grid), ListBox.

## 9. Preencher UOR e MATRÍCULA ao selecionar a pessoa
[fluxo] ScriptModificado do campo de pessoa (ex.: fluxos de Benefícios)
```python
# Script Modificado do campo FAVORECIDO_COBRA (combo cujo valor é o ID_PESSOA)
if Formulario["FAVORECIDO_COBRA"].Valor != None:
    idPessoa = Convert.ToInt32(Formulario["FAVORECIDO_COBRA"].Valor)
    lista = Utils.ExecuteDataTable("SELECT CP.MATRICULA, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO WHERE P.ID_PESSOA = " + idPessoa.ToString())
    for linha in lista.Rows:
        Formulario["TE_MATRICULA"].Valor = linha["MATRICULA"].ToString()
        Formulario["TE_UOR"].Valor = linha["DESCRICAO"].ToString()
    Formulario["TE_MATRICULA"].Habilitado = False
    Formulario["TE_UOR"].Habilitado = False
```
O combo de pessoa usa Script de recuperação de opções como
`Itens = DB.ExecuteDataTable("SELECT to_char(p.id_pessoa) as id_pessoa, p.nome FROM PESSOA p WHERE p.ativo = 'Sim' ORDER BY p.nome")`.

## 10. Mensagem para mais de um destinatário por script
[fluxo] ScriptEvento do Evento Intermediário de Mensagem (Faturamento de Clientes v20)
```python
if OrdemServico["DESTNFSE_FAT"] != None:
    for email in OrdemServico["DESTNFSE_FAT"].Split(";"):
        Mensagem.Destinatarios.Add(email)
```
Sem script: propriedade de lista de e-mails do evento (`ListaDestinatarios`, separados por `;`) ou um
papel destinatário que retorne várias pessoas (inclusive papel Composto). [doc] docs/cadastrar_usuario_2_2.md

## 11. Gateway que segue conforme o resultado de uma aprovação
[doc] docs/por_formula.md, docs/data_obj_aprovacao.md + [fluxo] vários (Bens Patrimoniais v38, Disec v1)
- Dar um **Código** à tarefa de aprovação (ex.: `APROV_GESTOR`).
- Desvio Exclusivo logo após: Fórmula critério `OrdemServico.PossuiAprovacao("APROV_GESTOR")`.
- Alternativas com Valor comparação `True` (aprovado) e `False` (reprovado).
- Ou, sem fórmula: propriedade **Regra de Desvio** do Desvio Exclusivo apontando para a tarefa de aprovação.
- Motivo da reprovação: `OrdemServico.ObtemMotivoReprovacao("APROV_GESTOR")`.

## 12. Ler em um script o valor de campo preenchido em outra tarefa
[doc] docs/topicos_avancados_campos.md (Exemplo 3)
O campo pertence à Ordem de Serviço, não à tarefa: `OrdemServico.GetCustom("CAMPO")` ou
`OrdemServico["CAMPO"]`; com valor padrão: `OrdemServico.GetCustom("CAMPO", "None")`.
`Formulario["CAMPO"]` só enxerga campos do formulário aberto. Gravar: `OrdemServico.SetCustom("CAMPO", valor)`.

## 13. Scripts em grids (Listagem de Registros)
[doc] docs/utilizacao_de_scripts_em_data_.md, docs/topicos_avancados_listagem.md, docs/controle_grid.md
| Evento | Variáveis | Uso típico |
|---|---|---|
| Script Adicionado (do grid) | `NovoRegistro`, `Tabela`, `Posicao` | valores iniciais: `NovoRegistro["QUANTIDADE"] = 0` |
| Script Modificado (da coluna) | `FormularioRegistro["COL"]`, `Controle` | cálculo e cascata na linha |
| Script Confirmado (do grid) | `Registro`, `Cancela` | validar a linha; `Cancela = True` rejeita |
| Script Removido (do grid) | `RegistroRemovido`, `Tabela`, `Posicao` | reagir à exclusão |
```python
# ler o grid inteiro (DataTable) em qualquer script
dt = OrdemServico.GetCustom("LISTA_ITENS")
total = 0
for dr in dt.Rows:
    total = total + dr["PESO"]
```
[fluxo] Incluir linha por script: `OrdemServico.AdicionaLinhaRegistro("GRID", ["COL1", "COL2"], [v1, v2])`.
[fluxo] Mensagem ao usuário dentro do formulário: `Formulario.ExibeMensagem("texto")`.
Colunas calculadas (Fórmula de Cálculo) não são gravadas no banco.

## 14. Chamar uma API REST, tratar a resposta e gravar em campo
[fluxo] padrão de catalogo/biblioteca/api*.py (HttpClient + Newtonsoft); não há página oficial para REST
```python
clr.AddReference("System.Net.Http")
clr.AddReference("Newtonsoft.Json")
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue
from System.Text import Encoding
from Newtonsoft.Json import JsonConvert
from Newtonsoft.Json.Linq import JObject

try:
    client = HttpClient()
    client.Timeout = TimeSpan.FromSeconds(60)
    client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
    payload = JsonConvert.SerializeObject({"matricula": OrdemServico["TE_MATRICULA"]})
    conteudo = StringContent(payload, Encoding.UTF8, "application/json")
    response = client.PostAsync("https://api.exemplo.com/v1/colaboradores/consulta", conteudo).Result
    corpo = response.Content.ReadAsStringAsync().Result
    if response.IsSuccessStatusCode:
        dados = JObject.Parse(corpo)
        OrdemServico.SetCustom("TE_CARGO", dados["cargo"].ToString())
    else:
        Utils.LogError("API colaboradores: " + corpo, "Integração")
except Exception as e:
    Utils.LogError("API colaboradores: " + str(e), "Integração")
```
GET: `client.GetAsync(url).Result`. Token/URL: buscar de parâmetro (ex.: tabelas `SV_PARAM`/`SERVICES_PARAM`
usadas nos fluxos), não fixar no script. SOAP: `Webservices.LoadWebService` (docs/loadwebservice.md).

## 15. Travas no Script Validação
[doc] docs/tarefas.md + [fluxo] `Criticas`
```python
if String.IsNullOrEmpty(OrdemServico["JUSTIFICATIVA"]):
    Criticas.AdicionaPendencia("É obrigatório informar a 'Justificativa'")
if OrdemServico.GetCustom("LISTA_NF").Rows.Count == 0:
    Criticas.AdicionaPendencia("Inclua pelo menos uma nota fiscal")
```
Uma pendência basta para impedir o avanço; `Criticas.AdicionaAviso(msg)` só alerta.
Por padrão o Script Validação roda também na finalização do processo (parâmetro
"Executar Script de validação na finalização" da tarefa).

## 16. Abrir várias OS a partir de uma planilha (fluxo "em lote")
[fluxo] padrão repetido nos fluxos do cliente. Referências para copiar:
`fluxos/Gabriel_Teste_Ativações_Versão_3__LOTE__Pré-Notificação_...IDF.md` (lote) e
`fluxos/Administração_-_Contratos_Versão_45_Pré-Notificação_...IDF_.md` (filho, só Link Inicial);
`fluxos/Serviços_Assistência_Técnica_Versão_15_Recebimento_de_Uniforme__Em_Lote.md` (agrupa linhas por matrícula).
Estrutura:
1. **Fluxo LOTE**: Evento Inicial com Data Object Associar Itens de Configuração (anexo "Planilha", classe Arquivo)
   + Entrada de Dados com um CheckBox "Clique aqui para ler a planilha" + um campo DataGrid (RecordList).
2. `ScriptModificado` do checkbox lê o .xlsx e chama `OrdemServico.AdicionaLinhaRegistro("GRID", [colunas], [valores])`.
   Caminho do arquivo: `Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM")` + `"\\"` + `OrdemServico.ObtemItem("ARQUIVO").Localizacao`.
   Só .xlsx (leitura via ZipArchive/XML; funções `LerXlsx`, `NomeLocal`, `ElementosPorNome` etc. nos fluxos acima).
3. Atividade **Subprocesso** (com Associação "Lote -> Individual", ValoresInputs Cliente/Servico) cujo `ScriptInicio` faz,
   para cada linha: `sub = OrdemServico.IniciaSubProcesso(OrdemServico.Atividade)`; `sub.Assunto = ...`;
   limpa a grid herdada (`sub.GetCustom("GRID").Rows.Clear()`); `sub.AdicionaLinhaRegistro(...)`; `sub.Salva()`; `sub.AvancaAtividade()`.
4. **Fluxo filho**: precisa de um **Link Inicial** (TipoAberturaLinkInicial=ApenasChamador) com a mesma Associação (frase inversa).
   Um fluxo pode ter Evento Inicial e Link Inicial ao mesmo tempo (docs/iniciador_multiplas_formas_subpr.md, docs/iniciador_link_inicial.md).
5. Pessoa por matrícula na OS filha: `SELECT P.ID_PESSOA FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA WHERE CP.MATRICULA = '...'`
   e `sub.Cliente = Pessoa.Carrega(id)` (padrão do lote de Uniformes).
Boas práticas observadas: contar criadas/ignoradas/erros e gravar resumo com `OrdemServico.AdicionaComentario(texto, False)`;
limitar o detalhe do log (20 a 30 linhas); validar linha a linha antes de criar; `Formulario.ExibeMensagem` com o resumo da leitura.

## 17. Complementos às receitas confirmados pela API (DLLs v18.1.1)
[api] guias/api_scripts.md; assinaturas reais, comportamento a validar em Qualidade.
- **Consulta parametrizada (receitas 6, 7, 9)**: além de concatenar texto, o `DB` tem sobrecargas com parâmetros:
  `DB.ExecuteScalar(sql, nomesParametros, valoresParametros)`, idem `ExecuteDataTable` e `ExecuteNonQuery`
  (listas .NET). Evita aspas e injeção de SQL. A sintaxe do marcador no SQL (ex.: `:nome` no Oracle) não foi testada.
- **Mensagem (receita 10)**: `Mensagem` é um `TemplateMensagem`: `Destinatarios` (lista), `Assunto`, `Corpo`,
  `Remetente`, `NomeRemetente`, `Complemento1` a `Complemento5`, `ConteudoHTML`, `DataHoraAgendada` e
  **`Cancelar`** (`Mensagem.Cancelar = True` impede o envio). `PreencheCorpo(nomeModeloComunicado, OrdemServico)`.
- **Aprovação (receita 11)**: `PossuiAprovacao(codigoAtividade)`, `ObtemMotivoReprovacao(codigoAtividade)`,
  `Aprova(codigoAtividade[, aprovador, comentario])`, `Reprova(codigoAtividade, motivo)`, `CancelaAprovacao(codigoAtividade)`.
  Desvios: `ObtemMotivoGateway(codigoGateway)`, `ContaExecucaoGateway(codigoGateway[, textoAlternativa])`.
- **Campos (receita 12)**: `GetCustom(nome[, valorPadrao])` e `SetCustom(nome, valor)` vêm de `SessionObjectProxy`,
  base de TODAS as entidades: valem para OrdemServico, Pessoa, Servico, Orgao etc. e também `objeto["NOME"]`.
- **Grids (receita 13)**: `AdicionaLinhaRegistro(nomeCampo, nomes, valores)` devolve o `DataRow` criado.
  `FormularioRegistro.Colunas`, `PossuiColuna(nome)`; cada coluna é um `ControleFormulario`
  (`Valor`, `Visivel`, `Habilitado`, `Itens`, `Mascara`).
- **Validação (receita 15)**: `Criticas.AdicionaPendencia(mensagem[, grupo[, campoAssociado]])`,
  `AdicionaAviso(...)` e `AdicionaInformacao(...)` com as mesmas sobrecargas.
- **Papéis (receita 7)**: `Atores.Adiciona(pessoa[, comentario])`, `AdicionaLista(arrayList[, comentario])`,
  `Limpar()`, `Quantidade`.
- **Lote (receita 16)**: `IniciaSubProcesso(atividade[, numero])` devolve uma `Ocorrencia`, então
  `sub.SetCustom("CAMPO", valor)` existe para preencher campos simples da OS filha. Alternativa sem Link Inicial:
  `OrdemServico.Nova(siglaClasseSubProcesso, codigoIniciador, assunto, servico, cliente, responsavel, valoresCustomizados)`
  abre a OS já com um `Hashtable` de campos customizados (usado em vários fluxos do cliente sem o Hashtable).
- **Outros úteis**: `AnexaArquivo(nomeArquivo, siglaTipoItem, apagarOriginal)`, `AssociaOrdemServico(numeroAlvo, siglaAssociacao)`,
  `ObtemAssociadasComoFonte/ComoAlvo(nomeAssociacao)`, `ObtemPrincipal()`, `ObtemDerivadas()`, `Cancela(motivo)`,
  `VoltaAtividade()`, `AvancaAtividade()`, `Encaminha(tecnico, explicacao)`, `ContaExecucaoAtividade(codigo)`,
  `AnexaExportacaoRelatorio(...)`, `Utils.NewSequenceValue(sequence)`, `Utils.SendMail(from, to, subject, body)`.
