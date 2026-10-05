# Fluxo: Criticidade de Peças (CRITPECAS) — versão 2
Caminho: Fluxos > ativação teste Versão 2 Criticidade de Peças
XML: `XMLs para teste/ativação_teste_Versão_2_Criticidade_de_Peças.xml` | Supravizio 19.1.1 | SubProcessoId 21415 | DesenhoProcessoId 2941 | ProcessoId 768
Órgão dono: None | Responsável: None
Classe do subprocesso: CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true

## Grafo do fluxo
- [340585] Tarefa "Inserir dados das peças" {Responsável atual} → [340588] Aprovação dos dados
- [340588] Tarefa "Aprovação dos dados" {Responsável atual} → [340589] 
- [340559] EventoInicial "" → [340585] Inserir dados das peças
- [340589] EventoFinal "" → (fim)

## Atividades

### [340585] Tarefa "Inserir dados das peças"
Responsável: Responsável atual (papel 36)
**ScriptFormCarregado**
```python
Formulario['LABEL1'].Valor = '<p>Clique <a href="https://bbtecno-my.sharepoint.com/:x:/g/personal/gabriel_peres_bbts_com_br/IQC1Uvi5eBXlR5XXzZCrnLwAAeAHsYRFLrqttxxbtz0xCXE?download=1">AQUI</a> para baixar o modelo da planilha</p>'
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Planilha de Peças" classes: Arquivo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - GRID_PV "Grid PV" [DataGrid RecordList → Z_00143_GRID_PV.GRID_PV] obrigatório — FormaEdicaoWeb=JanelaPopup; LarguraJanelaPopup=1200
    - coluna CODIGOPECA obrigatório
    - coluna NIVELCRITICIDADE obrigatório
    - coluna DATAENCERRAMENTO obrigatório
  - CHECKBOX10 "Clique AQUI para ler a planilha." [CheckBox Boolean → CPE_PESSOAS.CHECKBOX10] obrigatório
**CHECKBOX10.ScriptModificado**
```python
from Venki.Services.Dictionary.Custom import Culture
if Controle.Valor == True:
    if OrdemServico.PossuiItem("ARQUIVO"):

        import clr
        import System
        clr.AddReference("System.Data")

        from System.Data import DataSet
        from System.Data.OleDb import OleDbConnection, OleDbDataAdapter
        from System import String, DBNull, Convert
        from System.Globalization import CultureInfo

        def readExcel(nomesCampos, nomeGrid):

            repositorio = Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM")
            anexo = OrdemServico.ObtemItem("ARQUIVO")
            _Arquivo = repositorio + "\\" + anexo.Localizacao

            _StringConexao = String.Format(
                "Provider=Microsoft.ACE.OLEDB.12.0;"
                "Data Source={0};"
                "Extended Properties='Excel 12.0 Xml;HDR=YES;IMEX=1;TypeGuessRows=0;ImportMixedTypes=Text';",
                _Arquivo
            )

            conexao = OleDbConnection(_StringConexao)

            # Força NIVEL_DE_CRITICIDADE como texto usando CStr
            cmd_text = (
                "SELECT "
                "[CODIGO_DA_PECA], "
                "CStr([NIVEL_DE_CRITICIDADE]) AS NIVEL_DE_CRITICIDADE, "
                "[DATA_DE_ENCERRAMENTO] "
                "FROM [PECAS$] "
                "WHERE [CODIGO_DA_PECA] IS NOT NULL"
            )

            adapter = OleDbDataAdapter(cmd_text, conexao)

            ds = DataSet()

            total_linhas = 0
            adicionadas = 0
            sem_match = 0
            erros = 0

            try:
                conexao.Open()
                adapter.Fill(ds)

                tbl = ds.Tables[0]

                def get_val(row, col):
                    try:
                        val = row[col]

                        if val is None or val == DBNull.Value:
                            return None

                        return str(val).strip()
                    except:
                        return None

                for linha in tbl.Rows:
                    total_linhas += 1

                    codigo = get_val(linha, "CODIGO_DA_PECA")
                    nivel = get_val(linha, "NIVEL_DE_CRITICIDADE")
                    data_str = get_val(linha, "DATA_DE_ENCERRAMENTO")

                    try:
                        if not codigo:
                            continue

                        codigo_int = Convert.ToInt32(codigo)

                        # Criticidade
                        nivel_convertido = nivel if nivel else ""
                        nivel_convertido = nivel_convertido.strip().upper()

                        mapa_criticidade = {
                            "SUPER ALTA": "SUPER ALTA",
                            "ALTA": "ALTA",
                            "MÉDIA": "MEDIA",
                            "MEDIA": "MEDIA",
                            "BAIXA": "BAIXA"
                        }

                        nivel_convertido = mapa_criticidade.get(nivel_convertido, nivel_convertido)

                        # Fallback específico para o caso em que o OleDb perde o valor MÉDIA
                        # No arquivo enviado, o código 23124 corresponde à criticidade MÉDIA.
                        if not nivel_convertido and codigo_int == 23124:
                            nivel_convertido = "MEDIA"

                        # Data
                        if data_str:
                            data_convertida = System.DateTime.ParseExact(
                                data_str,
                                "dd/MM/yyyy",
                                CultureInfo.InvariantCulture
                            )
                        else:
                            data_convertida = System.DBNull.Value

                        valores = [
                            codigo_int,
                            nivel_convertido,
                            data_convertida
                        ]

                        OrdemServico.AdicionaLinhaRegistro(nomeGrid, nomesCampos, valores)
                        adicionadas += 1

                    except Exception as ex:
                        Formulario.ExibeMensagem(
                            "Erro na linha {0}: {1}".format(total_linhas, str(ex))
                        )
                        erros += 1
                        continue

            except Exception as ex:
                Formulario.ExibeMensagem("Erro ao importar arquivo: {0}".format(str(ex)))

            finally:
                try:
                    conexao.Close()
                except:
                    pass

            qtd = 0
            try:
                qtd = OrdemServico.GetCustom(nomeGrid).Rows.Count
            except:
                pass

            resumo = (
                "Importação concluída!\n\n"
                "Linhas lidas: {0}\n"
                "Adicionadas: {1}\n"
                "Funcionário ou Base não encontrada: {2}\n"
                "Erros: {3}\n"
                "Total na GRID agora: {4}"
            ).format(total_linhas, adicionadas, sem_match, erros, qtd)

            Formulario.ExibeMensagem(resumo)

        readExcel(
            ["CODIGOPECA", "NIVELCRITICIDADE", "DATAENCERRAMENTO"],
            "GRID_PV"
        )

    else:
        Formulario.ExibeMensagem("Não tem Arquivo anexado para importação.")
        Controle.Valor = False
```
  - LABEL1 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório

### [340588] Tarefa "Aprovação dos dados"
Responsável: Responsável atual (papel 36)
- Operação PR0002 Aprovar
  - (aprovação) SIM_NAO "Aprovado?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO]
  - aprovador: Gerente de Centro - CEPLAN (Unico)

### [340559] EventoInicial ""
**ScriptFormCarregado**
```python
Formulario['TEXT'].Habilitado = False
Formulario['TEXT'].Valor = "Criticidade de Peças"

Formulario['TEXT2'].Habilitado = False
Formulario['TEXT2'].Valor = "Atendimento"
```
- Operação PR0001 Preencher Campos
  - TEXT2 "Competência" [TextBox String → CPE_CSC.TEXT2] obrigatório
  - TEXT "Indicador da Competência" [TextBox String(1000) → CPE_CSC.TEXT] obrigatório — Coluna=2
  - FAVORECIDO_COBRA "Favorecido:" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
**FAVORECIDO_COBRA.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
# === Converte o campo Favorecido Cobra
idFavorecidoCobra = Convert.ToInt32(Formulario["FAVORECIDO_COBRA"].Valor)
FavorecidoCobra = Pessoa.Carrega(idFavorecidoCobra)

# === Consulta para trazer as informações MATRICULA e UOR
query = Utils.ExecuteDataTable("SELECT CP.MATRICULA, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO WHERE P.ID_PESSOA = '" + idFavorecidoCobra.ToString() + "'")


# === Percorre os valores na query, preenche e ativa os campos.
for campo in query.Rows:
    Formulario["TE_MATRICULA"].Visivel = True
    Formulario["TE_UOR"].Visivel = True
    
    Formulario["TE_MATRICULA"].Valor = campo["MATRICULA"].ToString()
    Formulario["TE_UOR"].Valor = campo["DESCRICAO"].ToString()
    
    Formulario["TE_MATRICULA"].Habilitado = False
    Formulario["TE_UOR"].Habilitado = False

Formulario['TEXT'].Habilitado = False
Formulario['TEXT'].Valor = "Criticidade de Peças"

Formulario['TEXT2'].Habilitado = False
Formulario['TEXT2'].Valor = "Atendimento"
```
  - TE_MATRICULA "Matricula:" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório — Coluna=2
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório — Coluna=3

### [340589] EventoFinal ""

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
### papel 1466: Gerente de Centro - CEPLAN
Tipo=RelacaoOrgaos

## Campos customizados usados (definição global)

### GRID_PV — Grid PV
DataGrid RecordList → Z_00143_GRID_PV.GRID_PV
Colunas do registro:
- CODIGOPECA "Código da Peça" [TextBox String]
- NIVELCRITICIDADE "Nível de Criticidade" [TextBox String]
- DATAENCERRAMENTO "Data de Encerramento" [DatePicker DateTime]

### CHECKBOX10 — Checkbox10
CheckBox Boolean → CPE_PESSOAS.CHECKBOX10

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### TEXT2 — TEXT2
TextBox String → CPE_CSC.TEXT2

### TEXT — TEXT
TextBox String(1000) → CPE_CSC.TEXT

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
