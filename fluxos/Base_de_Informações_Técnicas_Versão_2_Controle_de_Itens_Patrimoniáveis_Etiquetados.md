# Fluxo: Controle de Itens Patrimoniáveis Etiquetados (ITENSPATRICONTROL) — versão 2
Caminho: Fluxos > Base de Informações Técnicas Versão 2 Controle de Itens Patrimoniáveis Etiquetados
XML: `XMLs para teste/Base_de_Informações_Técnicas_Versão_2_Controle_de_Itens_Patrimoniáveis_Etiquetados.xml` | Supravizio 19.1.1 | SubProcessoId 21518 | DesenhoProcessoId 2970 | ProcessoId 762
Órgão dono: None | Responsável: None
Classe do subprocesso: DescricaoCliente=Controle de Itens Patrimoniáveis Etiquetados; CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Controle de Itens Patrimoniáveis Etiquetados (ITENSPATRICONTROLE)

## Grafo do fluxo
- [342186] EventoFinal "" → (fim)
- [342187] EventoInicial "" {Cliente} → [342188] Aprovação CEEST
- [342188] Tarefa "Aprovação CEEST" {Cliente} → [342186] 

## Atividades

### [342186] EventoFinal ""

### [342187] EventoInicial ""
Responsável: Cliente (papel 18)
Config: Configuracao={"ServicoIniciador":"ITENSPATRICONTROLE"}
TipoSolicitacao: Controle de Itens Patrimoniáveis Etiquetados
**ScriptFormCarregado**
```python
Formulario['PS_LABEL1'].Valor = '<p>Clique <a href="https://bbtecno-my.sharepoint.com/:x:/g/personal/gabriel_peres_bbts_com_br/IQBJc2bFjsuQToHnX4WNSIhdAWVHV7MTJiUlzZ0OwiMvLlY?e=ZXKgp1" target="_blank">AQUI</a> para baixar o modelo da planilha</p>'
```
- Operação PR0001 Preencher Campos
  - PS_LABEL1 "Modelo de Planilha" [Label String(2000) → CPE_PESSOAS.PS_LABEL1]
  - GRIDITENSPATRI "Cadstro de Itens" [DataGrid RecordList → Z_00143_GRIDITENSPATRI.GRIDITENSPATRI] obrigatório — FormaEdicaoWeb=JanelaPopup; QtdColunasFormulario=3
    - coluna DATA_DO_RECEBIMENTO_DA_NF obrigatório
    - coluna DATA_DA_VERIFICACAO obrigatório
    - coluna RANGE_DAS_ETIQUETAS obrigatório
    - coluna NUMERO_DA_NOTA_FISCAL obrigatório
    - coluna ITEM_PATRIMONIAVEL obrigatório
    - coluna QUANTIDADE_DE_ITENS_ETIQUETADOS obrigatório
  - CHECKBOX1 "Clique aqui para ler a planilha/CSV (Depois de anexar)" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX1]
**CHECKBOX1.ScriptModificado**
```python
from Venki.Services.Dictionary.Custom import Culture
if Controle.Valor == True:
    if OrdemServico.PossuiItem("ARQUIVO"):

        import clr
        import System
        clr.AddReference("System.Data")
        from System.Data import DataSet
        from System.Data.OleDb import OleDbConnection, OleDbDataAdapter
        from System import String, DBNull, Convert, DateTime
        from System.Globalization import CultureInfo

        def readExcel(nomesCampos, nomeGrid):

            repositorio = Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM")
            anexo = OrdemServico.ObtemItem("ARQUIVO")
            _Arquivo = repositorio + "\\" + anexo.Localizacao

            pos_barra = _Arquivo.rfind("\\")
            pasta = _Arquivo[:pos_barra]
            nomeArquivo = _Arquivo[pos_barra + 1:]

            pos_ponto = nomeArquivo.rfind(".")
            extensao = nomeArquivo[pos_ponto:].lower()

            if extensao == ".csv":
                _StringConexao = String.Format(
                    "Provider=Microsoft.ACE.OLEDB.12.0;Data Source={0};Extended Properties='Text;HDR=YES;FMT=Delimited';",
                    pasta
                )
                origem = "[" + nomeArquivo + "]"

            elif extensao == ".xls":
                _StringConexao = String.Format(
                    "Provider=Microsoft.ACE.OLEDB.12.0;Data Source={0};Extended Properties='Excel 8.0;HDR=YES;ReadOnly=False';",
                    _Arquivo
                )
                origem = "[ITENS$]"

            else:
                _StringConexao = String.Format(
                    "Provider=Microsoft.ACE.OLEDB.12.0;Data Source={0};Extended Properties='Excel 12.0 Xml;HDR=YES;ReadOnly=False';",
                    _Arquivo
                )
                origem = "[ITENS$]"

            conexao = OleDbConnection(_StringConexao)
            cmd_text = "SELECT * FROM " + origem
            adapter = OleDbDataAdapter(cmd_text, conexao)

            ds = DataSet()
            conexao.Open()
            adapter.Fill(ds)

            total_linhas = 0
            adicionadas = 0
            erros = 0

            tbl = ds.Tables[0]

            def get_idx(row, idx):
                try:
                    if row.IsNull(idx):
                        return None
                    return row[idx]
                except:
                    return None

            def to_str(valor):
                try:
                    if valor is None:
                        return None

                    texto = str(valor).strip()

                    if texto == "":
                        return None

                    return texto
                except:
                    return None

            def to_qtd_int(valor):
                try:
                    if valor is None:
                        raise Exception("Quantidade não informada.")

                    texto = str(valor).strip()

                    if texto == "":
                        raise Exception("Quantidade não informada.")

                    texto = texto.replace(",", ".")

                    qtd = Convert.ToInt32(Convert.ToDouble(texto, CultureInfo.InvariantCulture))

                    if qtd <= 0:
                        raise Exception("Quantidade de itens etiquetados deve ser maior que zero.")

                    return qtd

                except Exception as ex:
                    raise Exception("Quantidade inválida: '{0}'. {1}".format(str(valor), str(ex)))

            def to_date(valor):
                try:
                    if valor is None:
                        return None

                    if valor.GetType().FullName == "System.DateTime":
                        return valor

                    texto = str(valor).strip()

                    if texto == "":
                        return None

                    try:
                        return DateTime.ParseExact(texto, "dd-MM-yyyy", CultureInfo.InvariantCulture)
                    except:
                        pass

                    try:
                        return DateTime.ParseExact(texto, "dd/MM/yyyy", CultureInfo.InvariantCulture)
                    except:
                        pass

                    return Convert.ToDateTime(texto)

                except:
                    raise Exception("Valor inválido para data: '{0}'".format(str(valor)))

            for linha in tbl.Rows:
                total_linhas += 1

                numero_nf = get_idx(linha, 0)
                item_patrimoniavel = get_idx(linha, 1)
                numero_range_etiquetas = get_idx(linha, 2)
                quantidade_itens = get_idx(linha, 3)
                data_recebimento_nf = get_idx(linha, 4)
                data_verificacao = get_idx(linha, 5)

                if (
                    numero_nf is None and
                    item_patrimoniavel is None and
                    numero_range_etiquetas is None and
                    quantidade_itens is None and
                    data_recebimento_nf is None and
                    data_verificacao is None
                ):
                    continue

                try:
                    qtd_itens = to_qtd_int(quantidade_itens)

                    valores = [
                        to_str(numero_range_etiquetas),
                        to_date(data_recebimento_nf),
                        to_date(data_verificacao),
                        to_str(numero_nf),
                        to_str(item_patrimoniavel),
                        to_str(quantidade_itens)
                    ]

                    OrdemServico.AdicionaLinhaRegistro(nomeGrid, nomesCampos, valores)
                    adicionadas += 1

                except Exception as ex:
                    Formulario.ExibeMensagem("Erro na linha {0}: {1}".format(total_linhas, str(ex)))
                    erros += 1
                    continue

            conexao.Close()

            qtd = 0
            try:
                qtd = OrdemServico.GetCustom(nomeGrid).Rows.Count
            except:
                pass

            resumo = (
                "Importação concluída!\n\n"
                "Linhas lidas: {0}\n"
                "Adicionadas: {1}\n"
                "Erros: {2}\n"
                "Total na GRID agora: {3}"
            ).format(total_linhas, adicionadas, erros, qtd)

            Formulario.ExibeMensagem(resumo)

        readExcel(
            [
                "RANGE_DAS_ETIQUETAS",
                "DATA_DO_RECEBIMENTO_DA_NF",
                "DATA_DA_VERIFICACAO",
                "NUMERO_DA_NOTA_FISCAL",
                "ITEM_PATRIMONIAVEL",
                "QUANTIDADE_DE_ITENS_ETIQUETADOS"
            ],
            "GRIDITENSPATRI"
        )

    else:
        Formulario.ExibeMensagem("Não tem Arquivo anexado para importação.")
        Controle.Valor = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexe a planilha ou csv" classes: Arquivo — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [342188] Tarefa "Aprovação CEEST"
Responsável: Cliente (papel 18)
- Operação PR0002 Aprovar: MinimoAprovadores=1
  - (aprovação) PS_INFORMF1 "Observações" [Memo String(2000) → CPE_PESSOAS.PS_INFORMF1]
  - aprovador: Gestor de Centro -  CEEST (Unico)

## Papéis usados
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 1474: Gestor de Centro -  CEEST
Tipo=RelacaoPessoas | pessoas: ELIEZER RODRIGUES OLIVEIRA JUNIOR, VANESSA RODRIGUES GIAVONI

## Campos customizados usados (definição global)

### PS_LABEL1 — Texto Informativo
Label String(2000) → CPE_PESSOAS.PS_LABEL1

### GRIDITENSPATRI — Cadastro de Itens Etiquetados
DataGrid RecordList → Z_00143_GRIDITENSPATRI.GRIDITENSPATRI
Descrição: Grid Itens Patri
Colunas do registro:
- DATA_DO_RECEBIMENTO_DA_NF "Data do recebimento da NF" [DatePicker DateTime]
- DATA_DA_VERIFICACAO "Data da Verificação" [DatePicker DateTime]
- RANGE_DAS_ETIQUETAS "Número da Etiqueta" [TextBox String]
- NUMERO_DA_NOTA_FISCAL "Número da NF" [TextBox String]
- ITEM_PATRIMONIAVEL "Item Patrimoniável" [TextBox String]
- QUANTIDADE_DE_ITENS_ETIQUETADOS "Quantidade de Itens Etiquetados" [TextBox String]

### CHECKBOX1 — Checkbox1
CheckBox Boolean → CPE_PESSOAS.CHECKBOX1

### PS_INFORMF1 — Informações da Fase1
Memo String(2000) → CPE_PESSOAS.PS_INFORMF1

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
