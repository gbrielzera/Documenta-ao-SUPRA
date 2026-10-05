# Fluxo: Inclusão de Inventário (INCLUDEINV) — versão 2
Caminho: Fluxos > ativação teste Versão 2 Inclusão de Inventário
XML: `XMLs para teste/ativação_teste_Versão_2_Inclusão_de_Inventário.xml` | Supravizio 19.1.1 | SubProcessoId 21427 | DesenhoProcessoId 2941 | ProcessoId 768
Órgão dono: None | Responsável: None
Classe do subprocesso: CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true

## Grafo do fluxo
- [340672] EventoFinal "" → (fim)
- [340671] Tarefa "Aprovação do inventário" {Responsável atual} → [340672] 
- [340670] EventoInicial "" → [340671] Aprovação do inventário

## Atividades

### [340672] EventoFinal ""

### [340671] Tarefa "Aprovação do inventário"
Responsável: Responsável atual (papel 36)
- Operação PR0002 Aprovar
  - (aprovação) SIM_NAO "Aprovado?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO]
  - aprovador: Gestor de Centro -  CEEST (Unico)

### [340670] EventoInicial ""
**ScriptFormCarregado**
```python
Formulario['LABEL1'].Valor = '<p><span style="color: red;">Atenção:</span> insira apenas o número da matrícula e aperte OK que o nome e UOR serão preenchidos automaticamente!</p>'
```
- Operação PR0001 Preencher Campos
  - LABEL1 "Atenção" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - GRIDINVENTARIO "Grid Inclusão de Inventário" [DataGrid RecordList → Z_00143_GRIDINVENTARIO.GRIDINVENTARIO] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna VALOR_FINAL obrigatório
    - coluna DATA_VIAGEM obrigatório
    - coluna NOME_COLABORADOR obrigatório
    - coluna MATINV obrigatório
**GRIDINVENTARIO.MATINV.ScriptModificado**
```python
if FormularioRegistro['MATINV'].Valor != "":
    matricula = FormularioRegistro["MATINV"].Valor

    query = DB.ExecuteDataTable(
        "SELECT "
        "PESSOA.ID_PESSOA, "
        "PESSOA.NOME, "
        "ORGAO.DESCRICAO AS UOR "
        "FROM CP_PESSOA "
        "INNER JOIN PESSOA ON CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA "
        "LEFT JOIN ORGAO ON PESSOA.ID_ORGAO = ORGAO.ID_ORGAO "
        "WHERE CP_PESSOA.MATRICULA = '" + matricula + "'"
    )

    for i in query.Rows:
        id_pessoa = i["ID_PESSOA"]
        nome = i["NOME"]
        uor = i["UOR"]

        if nome != None and nome != "":
            # Se NOMEINV for um campo de seleção/pesquisa, provavelmente ele espera o ID da pessoa
            FormularioRegistro["NOMEINV"].Valor = id_pessoa

            # Se o campo aceitar texto diretamente, use esta linha no lugar da de cima:
            # FormularioRegistro["NOMEINV"].Valor = nome

            FormularioRegistro["NOMEINV"].Habilitado = False
        else:
            FormularioRegistro["NOMEINV"].Valor = ""
            FormularioRegistro["NOMEINV"].Habilitado = True

        if uor != None and uor != "":
            FormularioRegistro["UORINV"].Valor = uor
            FormularioRegistro["UORINV"].Visivel = True
            FormularioRegistro["UORINV"].Habilitado = False
        else:
            FormularioRegistro["UORINV"].Valor = ""
            FormularioRegistro["UORINV"].Habilitado = True

    FormularioRegistro["MATINV"].Habilitado = False
```
    - coluna UORINV obrigatório
    - coluna NOMEINV obrigatório
    - coluna DATEINV obrigatório
    - coluna NUMERO_OC obrigatório
    - coluna VALOR obrigatório
    - coluna CNPJ obrigatório
    - coluna NOME_FORNECEDOR obrigatório
    - coluna L_BASE_TR obrigatório
    - coluna NOMEINV2 obrigatório
    - coluna MATINV2 obrigatório
**GRIDINVENTARIO.MATINV2.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if FormularioRegistro['MATINV2'].Valor != "":
    matricula = str(FormularioRegistro["MATINV2"].Valor).strip()

    query = DB.ExecuteDataTable(
        "SELECT "
        "PESSOA.ID_PESSOA, "
        "PESSOA.NOME, "
        "ORGAO.DESCRICAO AS UOR "
        "FROM CP_PESSOA "
        "INNER JOIN PESSOA ON CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA "
        "LEFT JOIN ORGAO ON PESSOA.ID_ORGAO = ORGAO.ID_ORGAO "
        "WHERE LTRIM(RTRIM(CP_PESSOA.MATRICULA)) LIKE '%" + matricula + "%'"
    )

    if query.Rows.Count > 0:
        i = query.Rows[0]

        id_pessoa = i["ID_PESSOA"]
        nome = i["NOME"]
        uor = i["UOR"]

        if nome != None and nome != "":
            pessoa = Pessoa.Carrega(int(id_pessoa))  # ✅ CORREÇÃO AQUI
            FormularioRegistro["NOMEINV2"].Valor = pessoa
            FormularioRegistro["NOMEINV2"].Habilitado = False
        else:
            FormularioRegistro["NOMEINV2"].Valor = ""
            FormularioRegistro["NOMEINV2"].Habilitado = True

        if uor != None and uor != "":
            FormularioRegistro["UORINV2"].Valor = uor
            FormularioRegistro["UORINV2"].Visivel = True
            FormularioRegistro["UORINV2"].Habilitado = False
        else:
            FormularioRegistro["UORINV2"].Valor = ""
            FormularioRegistro["UORINV2"].Habilitado = True
```
    - coluna UORINV2 obrigatório
    - coluna DATAINV2 obrigatório

## Papéis usados
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```
### papel 1474: Gestor de Centro -  CEEST
Tipo=RelacaoPessoas

## Campos customizados usados (definição global)

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### GRIDINVENTARIO — Grid Inclusão de Inventário
DataGrid RecordList → Z_00143_GRIDINVENTARIO.GRIDINVENTARIO
Colunas do registro:
- NOMEINV2 "Nome do Colaborador" [TextBox String]
- MATINV2 "Matrícula" [TextBox String]
- UORINV2 "UOR" [TextBox String]
- DATAINV2 "Data de Inventário" [DatePicker DateTime]

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
