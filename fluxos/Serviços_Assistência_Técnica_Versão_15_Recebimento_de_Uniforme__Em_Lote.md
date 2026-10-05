# Fluxo: Recebimento de Uniforme (Em Lote) (UNIFORMELOTE) — versão 15
Caminho: Fluxos > Serviços Assistência Técnica Versão 15 Recebimento de Uniforme (Em Lote)
XML: `XMLs para teste/Serviços_Assistência_Técnica_Versão_15_Recebimento_de_Uniforme_(Em_Lote).xml` | Supravizio 19.1.1 | SubProcessoId 21645 | DesenhoProcessoId 2993 | ProcessoId 31
Órgão dono: None | Responsável: None
Classe do subprocesso: DescricaoCliente=Recebimento de Uniforme (Em Lote); CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Recebimento de Uniforme (Em Lote) (RECEBIMENTOUNIFORMELOTE)

## Grafo do fluxo
- [343966] EventoInicial "" {Cliente} → [343967] Abertura do chamado Recebimento de Uniformes
- [343967] SubProcesso "Abertura do chamado Recebimento de Uniformes" {Cliente} → [343968] 
- [343968] EventoFinal "" → (fim)

## Atividades

### [343966] EventoInicial ""
Responsável: Cliente (papel 18)
Config: Configuracao={"ServicoIniciador":"RECEBIMENTOUNIFORMELOTE"}
TipoSolicitacao: Recebimento de Uniforme (Em Lote)
**ScriptFormCarregado**
```python
# Script para esconder os campos de informações do favorecido
# Só ativa quando um favorecido é escolhido

Formulario["FAVORECIDO_TODOS"].Visivel = False

campos = ["TE_CARGO", "TE_FUNCAO", "TE_MATRICULA", "TE_UOR", "TAMANHO"]
for i in campos:
        Formulario[i].Visivel = False

Formulario['LABEL10'].Valor = '<p style="color: yellow; font-weight: 800; background-color: blue; border-radius: 22px; padding: 4% 0; text-align: center; font-weight: 600; font-size: 20px;"> RECEBIMENTO DE UNIFORMES - GERED </p><br><br>'
        
Formulario['LABEL109'].Valor = '<br><br><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><p><a href="https://bbts.docnix.com.br/bbts/corporate/index.html#/login?login=&senha=&empresa=1&state=permiLinkDocumento&id=34659591" target="_blank" style="text-decoration: none; color: blue; font-size: 20px;"><i class="fa fa-file-pdf-o" style="font-size:24px"></i> NI 1347 - Padronização, Requisição e Distribuição de Uniformes</a></p>'

Formulario['PS_LABEL1'].Valor = '<p>Clique <a href="https://bbtecno-my.sharepoint.com/:x:/g/personal/gabriel_peres_bbts_com_br/IQBHXpmwTbdNRIFmD46MyTS4AWZHUiPzSh2YVzb8AWYLCzc?e=WNThgh" target="_blank">AQUI</a> para baixar o modelo da planilha</p>'
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados Cadastrais
  - LABEL10 "LABEL10" [Label String(700) → CPE_PDCI2019.LABEL10] obrigatório
  - FAVORECIDO_TODOS "Nome do Empregado beneficiado" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
**FAVORECIDO_TODOS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#Formulario["TE_MATRICULA"].Visivel = True
#Formulario["TE_CARGO"].Visivel = True
#Formulario["TE_FUNCAO"].Visivel = True
#Formulario["TE_UOR"].Visivel = True
#
#Formulario["TE_MATRICULA"].Habilitado = False
#Formulario["TE_CARGO"].Habilitado = False
#Formulario["TE_FUNCAO"].Habilitado = False
#Formulario["TE_UOR"].Habilitado = False
#
#Formulario["TE_MATRICULA"].Valor = None
#Formulario["TE_CARGO"].Valor = None
#Formulario["TE_FUNCAO"].Valor = None
#Formulario["TE_UOR"].Valor = None
#
#matricula = ""
#cargo = ""
#funcao = ""
#uor = ""
#
#
#if Formulario["FAVORECIDO_TODOS"].Valor != "" or Formulario["FAVORECIDO_TODOS"].Valor != None:
#
#    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_TODOS"].Valor)
#    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
#    if favorecidoCustom != None:
#        nomeFavorecido = favorecidoCustom.Nome
#        orgaoFavorecido = favorecidoCustom.OrgaoId
#    else:
#        nomeFavorecido = OrdemServico.Favorecido.Nome
#        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId
#
#    #Formulario["TE_UOR"].Valor = orgaoFavorecido
#    #Consulta o cargo e a função do Favorecido
#
#    lista = Utils.ExecuteDataTable("SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )
#
#    for linha in lista.Rows:
#        cargo = linha["CARGO"].ToString()
#        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
#            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
#        
#        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
#        matricula = linha["MATRICULA"].ToString()
#        uor = linha["DESCRICAO"].ToString()
#
#    Formulario["TE_CARGO"].Valor = cargo.ToString()
#    Formulario["TE_FUNCAO"].Valor = funcao.ToString()
#    #Formulario["DESC_COLABORADOR"].Valor = desc_colaborador.ToString()
#    Formulario["TE_MATRICULA"].Valor = matricula.ToString()
#    Formulario["TE_UOR"].Valor = uor.ToString()
#
#
```
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório — Coluna=2
  - TE_MATRICULA "Matrícula do(a) Empregado(a) beneficiado" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório — Coluna=3
  - TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO] obrigatório
  - TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO] — Coluna=2
  - LABEL1 "<hr style="height: 4px; color: black; border-color: black; background-color: black;"><br>" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - UNIFORMES_EPI_LOTE "Uniformes em lote" [DataGrid RecordList → Z_00143_UNIFORMES_EPI_LOTE.UNIFORMES_EPI_LOTE] obrigatório
**UNIFORMES_EPI_LOTE.ScriptModificado**
```python
item = FormularioRegistro["ITEM"].Valor
quantidade = FormularioRegistro["QUANTIDADE"].Valor
grid = OrdemServico.GetCustom("UNIFORMES_EPI_LOTE")
item_repetido = False

try:
    tamanho = item.split(' | ')[1]
except:
    tamanho = ""

for linha in grid.Rows:
    if linha["ITEM"] == item:
        item_repetido = True
        break

if item_repetido:
    Formulario.ExibeMensagem("Este item já foi solicitado em outra linha. Não é permitido duplicar itens.")
    FormularioRegistro["ITEM"].Valor = ""
    FormularioRegistro["DESCRICAO"].Valor = ""
    FormularioRegistro["CODIGO"].Valor = ""
else:
    if FormularioRegistro["ITEM"].Valor == "Camisa Polo Masculina - R$ 88,04 | PP":
        FormularioRegistro["DESCRICAO"].Valor = "Camisa Polo Masculina - R$ 88,04 | PP"
        FormularioRegistro["DESCRICAO"].Habilitado = False
        FormularioRegistro["CODIGO"].Valor = "100011367"
        FormularioRegistro["CODIGO"].Habilitado = False
        FormularioRegistro['TAMANHO'].Valor = tamanho
        while quantidade > 4:
            Formulario.ExibeMensagem("Número maior que o permitido!")
            FormularioRegistro["QUANTIDADE"].Valor = ""
            break
    else:
        itens = {
            "Camisa Polo Masculina - R$ 88,04 | PP": {
                "descricao": "Camisa Polo Masculina - R$ 88,04 | PP",
                "codigo": "100011367",
                "limite": 4
            },
            "Camisa Polo Masculina - R$ 88,04 | P": {
                "descricao": "Camisa Polo Masculina - R$ 88,04 | P",
                "codigo": "100011368",
                "limite": 4
            },
            "Camisa Polo Masculina - R$ 88,04 | M": {
                "descricao": "Camisa Polo Masculina - R$ 88,04 | M",
                "codigo": "100011369",
                "limite": 4
            },
            "Camisa Polo Masculina - R$ 88,04 | G": {
                "descricao": "Camisa Polo Masculina - R$ 88,04 | G",
                "codigo": "100011370",
                "limite": 4
            },
            "Camisa Polo Masculina - R$ 88,04 | GG": {
                "descricao": "Camisa Polo Masculina - R$ 88,04 | GG",
                "codigo": "100011371",
                "limite": 4
            },
            "Camisa Polo Masculina - R$ 88,04 | XG": {
                "descricao": "Camisa Polo Masculina - R$ 88,04 | XG",
                "codigo": "100011372",
                "limite": 4
            },
            "Camisa Polo Masculina - R$ 88,04 | XGG": {
                "descricao": "Camisa Polo Masculina - R$ 88,04 | XGG",
                "codigo": "100011373",
                "limite": 4
            },
            "Camisa Polo Masculina - R$ 88,04 | EXGG": {
                "descricao": "Camisa Polo Masculina - R$ 88,04 | EXGG",
                "codigo": "100011374",
                "limite": 4
            },
            "Camisa Polo Masculina - R$ 88,04 | Especial E1 5G": {
                "descricao": "Camisa Polo Masculina - R$ 88,04 | Especial E1 5G",
                "codigo": "100011375",
                "limite": 4
            },
            "Camisa Polo Masculina - R$ 88,04 | Especial E2 7G": {
                "descricao": "Camisa Polo Masculina - R$ 88,04 | Especial E2 7G",
                "codigo": "100011376",
                "limite": 4
            },
            "Camisa Polo Feminina Baby Look - R$ 88,04 | PP": {
                "descricao": "Camisa Polo Feminina Baby Look - R$ 88,04 | PP",
                "codigo": "100011377",
                "limite": 4
            },
            "Camisa Polo Feminina Baby Look - R$ 88,04 | P": {
                "descricao": "Camisa Polo Feminina Baby Look - R$ 88,04 | P",
                "codigo": "100011378",
                "limite": 4
            },
            "Camisa Polo Feminina Baby Look - R$ 88,04 | M": {
                "descricao": "Camisa Polo Feminina Baby Look - R$ 88,04 | M",
                "codigo": "100011379",
                "limite": 4
            },
            "Camisa Polo Feminina Baby Look - R$ 88,04 | G": {
                "descricao": "Camisa Polo Feminina Baby Look - R$ 88,04 | G",
                "codigo": "100011380",
                "limite": 4
            },
            "Camisa Polo Feminina Baby Look - R$ 88,04 | GG": {
                "descricao": "Camisa Polo Feminina Baby Look - R$ 88,04 | GG",
                "codigo": "100011382",
                "limite": 4
            },
            "Camisa Polo Feminina Baby Look - R$ 88,04 | XG": {
                "descricao": "Camisa Polo Feminina Baby Look - R$ 88,04 | XG",
                "codigo": "100011383",
                "limite": 4
            },
            "Camisa Polo Feminina Baby Look - R$ 88,04 | XGG": {
                "descricao": "Camisa Polo Feminina Baby Look - R$ 88,04 | XGG",
                "codigo": "100011384",
                "limite": 4
            },
            "Camisa Polo Feminina Baby Look - R$ 88,04 | EXGG": {
                "descricao": "Camisa Polo Feminina Baby Look - R$ 88,04 | EXGG",
                "codigo": "100011385",
                "limite": 4
            },
            "Calça Jeans Masculina - R$ 110,00 | 34": {
                "descricao": "Calça Jeans Masculina - R$ 110,00 | 34",
                "codigo": "100011544",
                "limite": 2
            },
            "Calça Jeans Masculina - R$ 110,00 | 36": {
                "descricao": "Calça Jeans Masculina - R$ 110,00 | 36",
                "codigo": "100011545",
                "limite": 2
            },
            "Calça Jeans Masculina - R$ 110,00 | 38": {
                "descricao": "Calça Jeans Masculina - R$ 110,00 | 38",
                "codigo": "100011546",
                "limite": 2
            },
            "Calça Jeans Masculina - R$ 110,00 | 40": {
                "descricao": "Calça Jeans Masculina - R$ 110,00 | 40",
                "codigo": "100011547",
                "limite": 2
            },
            "Calça Jeans Masculina - R$ 110,00 | 42": {
                "descricao": "Calça Jeans Masculina - R$ 110,00 | 42",
                "codigo": "100011548",
                "limite": 2
            },
            "Calça Jeans Masculina - R$ 110,00 | 44": {
                "descricao": "Calça Jeans Masculina - R$ 110,00 | 44",
                "codigo": "100011549",
                "limite": 2
            },
            "Calça Jeans Masculina - R$ 110,00 | 46": {
                "descricao": "Calça Jeans Masculina - R$ 110,00 | 46",
                "codigo": "100011550",
                "limite": 2
            },
            "Calça Jeans Masculina - R$ 110,00 | 48": {
                "descricao": "Calça Jeans Masculina - R$ 110,00 | 48",
                "codigo": "100011551",
                "limite": 2
            },
            "Calça Jeans Masculina - R$ 110,00 | 50": {
                "descricao": "Calça Jeans Masculina - R$ 110,00 | 50",
                "codigo": "100011552",
                "limite": 2
            },
            "Calça Jeans Masculina - R$ 110,00 | 52": {
                "descricao": "Calça Jeans Masculina - R$ 110,00 | 52",
                "codigo": "100011553",
                "limite": 2
            },
            "Calça Jeans Masculina - R$ 110,00 | 54": {
                "descricao": "Calça Jeans Masculina - R$ 110,00 | 54",
                "codigo": "100011554",
                "limite": 2
            },
            "Calça Jeans Masculina - R$ 110,00 | 56": {
                "descricao": "Calça Jeans Masculina - R$ 110,00 | 56",
                "codigo": "100011555",
                "limite": 2
            },
            "Calça Jeans Feminina - R$ 110,00 | 32": {
                "descricao": "Calça Jeans Feminina - R$ 110,00 | 32",
                "codigo": "100011530",
                "limite": 2
            },
            "Calça Jeans Feminina - R$ 110,00 | 34": {
                "descricao": "Calça Jeans Feminina - R$ 110,00 | 34",
                "codigo": "100011531",
                "limite": 2
            },
            "Calça Jeans Feminina - R$ 110,00 | 36": {
                "descricao": "Calça Jeans Feminina - R$ 110,00 | 36",
                "codigo": "100011532",
                "limite": 2
            },
            "Calça Jeans Feminina - R$ 110,00 | 38": {
                "descricao": "Calça Jeans Feminina - R$ 110,00 | 38",
                "codigo": "100011533",
                "limite": 2
            },
            "Calça Jeans Feminina - R$ 110,00 | 40": {
                "descricao": "Calça Jeans Feminina - R$ 110,00 | 40",
                "codigo": "100011534",
                "limite": 2
            },
            "Calça Jeans Feminina - R$ 110,00 | 42": {
                "descricao": "Calça Jeans Feminina - R$ 110,00 | 42",
                "codigo": "100011535",
                "limite": 2
            },
            "Calça Jeans Feminina - R$ 110,00 | 44": {
                "descricao": "Calça Jeans Feminina - R$ 110,00 | 44",
                "codigo": "100011536",
                "limite": 2
            },
            "Calça Jeans Feminina - R$ 110,00 | 46": {
                "descricao": "Calça Jeans Feminina - R$ 110,00 | 46",
                "codigo": "100011537",
                "limite": 2
            },
            "Calça Jeans Feminina - R$ 110,00 | 48": {
                "descricao": "Calça Jeans Feminina - R$ 110,00 | 48",
                "codigo": "100011538",
                "limite": 2
            },
            "Calça Jeans Feminina - R$ 110,00 | 50": {
                "descricao": "Calça Jeans Feminina - R$ 110,00 | 50",
                "codigo": "100011539",
                "limite": 2
            },
            "Calça Jeans Feminina - R$ 110,00 | 52": {
                "descricao": "Calça Jeans Feminina - R$ 110,00 | 52",
                "codigo": "100011540",
                "limite": 2
            },
            "Calça Jeans Feminina - R$ 110,00 | 54": {
                "descricao": "Calça Jeans Feminina - R$ 110,00 | 54",
                "codigo": "100011541",
                "limite": 2
            },
            "Calça Jeans Feminina - R$ 110,00 | 56": {
                "descricao": "Calça Jeans Feminina - R$ 110,00 | 56",
                "codigo": "100011542",
                "limite": 2
            },
            "Calça Jeans Feminina - R$ 110,00 | 58": {
                "descricao": "Calça Jeans Feminina - R$ 110,00 | 58",
                "codigo": "100011543",
                "limite": 2
            },
            "Camisa Social Jeans Masculina - R$ 125,00 | 1": {
                "descricao": "Camisa Social Jeans Masculina - R$ 125,00 | 1",
                "codigo": "100011563",
                "limite": 2
            },
            "Camisa Social Jeans Masculina - R$ 125,00 | 2": {
                "descricao": "Camisa Social Jeans Masculina - R$ 125,00 | 2",
                "codigo": "100011564",
                "limite": 2
            },
            "Camisa Social Jeans Masculina - R$ 125,00 | 3": {
                "descricao": "Camisa Social Jeans Masculina - R$ 125,00 | 3",
                "codigo": "100011565",
                "limite": 2
            },
            "Camisa Social Jeans Masculina - R$ 125,00 | 4": {
                "descricao": "Camisa Social Jeans Masculina - R$ 125,00 | 4",
                "codigo": "100011566",
                "limite": 2
            },
            "Camisa Social Jeans Masculina - R$ 125,00 | 5": {
                "descricao": "Camisa Social Jeans Masculina - R$ 125,00 | 5",
                "codigo": "100011567",
                "limite": 2
            },
            "Camisa Social Jeans Masculina - R$ 125,00 | 6": {
                "descricao": "Camisa Social Jeans Masculina - R$ 125,00 | 6",
                "codigo": "100011568",
                "limite": 2
            },
            "Camisa Social Jeans Masculina - R$ 125,00 | 7": {
                "descricao": "Camisa Social Jeans Masculina - R$ 125,00 | 7",
                "codigo": "100011569",
                "limite": 2
            },
            "Camisa Social Jeans Masculina - R$ 125,00 | 8": {
                "descricao": "Camisa Social Jeans Masculina - R$ 125,00 | 8",
                "codigo": "100011570",
                "limite": 2
            },
            "Camisa Social Jeans Masculina - R$ 125,00 | 9": {
                "descricao": "Camisa Social Jeans Masculina - R$ 125,00 | 9",
                "codigo": "100011571",
                "limite": 2
            },
            "Camisa Social Jeans Masculina - R$ 125,00 | 10": {
                "descricao": "Camisa Social Jeans Masculina - R$ 125,00 | 10",
                "codigo": "100011572",
                "limite": 2
            },
            "Camisa Social Jeans Masculina - R$ 125,00 | 11": {
                "descricao": "Camisa Social Jeans Masculina - R$ 125,00 | 11",
                "codigo": "100011573",
                "limite": 2
            },
            "Camisa Social Jeans Masculina - R$ 125,00 | 12": {
                "descricao": "Camisa Social Jeans Masculina - R$ 125,00 | 12",
                "codigo": "100011574",
                "limite": 2
            },
            "Camisa Social Jeans Feminina - R$ 125,00 | PP": {
                "descricao": "Camisa Social Jeans Feminina - R$ 125,00 | PP",
                "codigo": "100011556",
                "limite": 2
            },
            "Camisa Social Jeans Feminina - R$ 125,00 | P": {
                "descricao": "Camisa Social Jeans Feminina - R$ 125,00 | P",
                "codigo": "100011557",
                "limite": 2
            },
            "Camisa Social Jeans Feminina - R$ 125,00 | M": {
                "descricao": "Camisa Social Jeans Feminina - R$ 125,00 | M",
                "codigo": "100011558",
                "limite": 2
            },
            "Camisa Social Jeans Feminina - R$ 125,00 | G": {
                "descricao": "Camisa Social Jeans Feminina - R$ 125,00 | G",
                "codigo": "100011559",
                "limite": 2
            },
            "Camisa Social Jeans Feminina - R$ 125,00 | GG": {
                "descricao": "Camisa Social Jeans Feminina - R$ 125,00 | GG",
                "codigo": "100011560",
                "limite": 2
            },
            "Camisa Social Jeans Feminina - R$ 125,00 | XG": {
                "descricao": "Camisa Social Jeans Feminina - R$ 125,00 | XG",
                "codigo": "100011561",
                "limite": 2
            },
            "Camisa Social Jeans Feminina - R$ 125,00 | XGG": {
                "descricao": "Camisa Social Jeans Feminina - R$ 125,00 | XGG",
                "codigo": "100011562",
                "limite": 2
            },
            "Camisa Social Jeans Feminina - R$ 125,00 | EG": {
                "descricao": "Camisa Social Jeans Feminina - R$ 125,00 | EG",
                "codigo": "100011563",
                "limite": 2
            },
            "Jaqueta BBTS Masculina | PP": {
                "descricao": "Jaqueta BBTS Masculina | PP",
                "codigo": "000000001",
                "limite": 1
            },
            "Jaqueta BBTS Masculina | P": {
                "descricao": "Jaqueta BBTS Masculina | P",
                "codigo": "000000001",
                "limite": 1
            },
            "Jaqueta BBTS Masculina | M": {
                "descricao": "Jaqueta BBTS Masculina | M",
                "codigo": "000000001",
                "limite": 1
            },
            "Jaqueta BBTS Masculina | G": {
                "descricao": "Jaqueta BBTS Masculina | G",
                "codigo": "000000001",
                "limite": 1
            },
            "Jaqueta BBTS Masculina | GG": {
                "descricao": "Jaqueta BBTS Masculina | GG",
                "codigo": "000000001",
                "limite": 1
            },
            "Jaqueta BBTS Masculina | G1": {
                "descricao": "Jaqueta BBTS Masculina | G1",
                "codigo": "000000001",
                "limite": 1
            },
            "Jaqueta BBTS Masculina | G2": {
                "descricao": "Jaqueta BBTS Masculina | G2",
                "codigo": "000000001",
                "limite": 1
            },
            "Jaqueta BBTS Feminina | PP": {
                "descricao": "Jaqueta BBTS Feminina | PP",
                "codigo": "000000001",
                "limite": 1
            },
            "Jaqueta BBTS Feminina | P": {
                "descricao": "Jaqueta BBTS Feminina | P",
                "codigo": "000000001",
                "limite": 1
            },
            "Jaqueta BBTS Feminina | M": {
                "descricao": "Jaqueta BBTS Feminina | M",
                "codigo": "000000001",
                "limite": 1
            },
            "Jaqueta BBTS Feminina | G": {
                "descricao": "Jaqueta BBTS Feminina | G",
                "codigo": "000000001",
                "limite": 1
            },
            "Jaqueta BBTS Feminina | GG": {
                "descricao": "Jaqueta BBTS Feminina| GG",
                "codigo": "000000001",
                "limite": 1
            },
            "Jaqueta BBTS Feminina | G1": {
                "descricao": "Jaqueta BBTS Feminina | G1",
                "codigo": "000000001",
                "limite": 1
            },
            "Jaqueta BBTS Feminina | G2": {
                "descricao": "Jaqueta BBTS Feminina| G2",
                "codigo": "000000001",
                "limite": 1
            }}
        
        chave = item
        if chave in itens:
            cfg = itens[chave]

            FormularioRegistro["DESCRICAO"].Valor = cfg.get("descricao", "")
            FormularioRegistro["DESCRICAO"].Habilitado = False

            FormularioRegistro["CODIGO"].Valor = cfg.get("codigo", "")
            FormularioRegistro["CODIGO"].Habilitado = False

            if tamanho:
                FormularioRegistro['TAMANHO'].Valor = tamanho

            
            limite = cfg.get("limite")
            if limite is not None:
                while quantidade > limite:
                    Formulario.ExibeMensagem("Número maior que o permitido!")
                    FormularioRegistro["QUANTIDADE"].Valor = ""
                    break
        else:
            Formulario.ExibeMensagem("Item não encontrado na tabela de itens. Verifique o nome ou atualize a planilha.")


if FormularioRegistro['TAMANHO'].Valor == "Outro":
    Formulario['TAMANHO'].Visivel = True
else:
    Formulario['TAMANHO'].Visivel = False
```
    - coluna MATRICULA obrigatório
    - coluna ITEM obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna DESCRICAO obrigatório
    - coluna TAMANHO obrigatório
    - coluna CODIGO obrigatório
  - TAMANHO "Tamanho do uniforme" [Memo String → CPE_CSC.TAMANHO] obrigatório
  - LABEL109 "LABEL109" [Label String(1000) → CPE_CONTRATOS.LABEL109]
  - CHECKBOX1 "Clique AQUI para ler a planilha/CSV" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX1]
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
        from System import String, DBNull, Convert
        from System.Globalization import CultureInfo

        # ============================================================
        # MAPEAMENTO DOS ITENS
        # ============================================================

        itens = {}
        itens_por_codigo = {}

        def add_item(nome, codigo, limite):
            chave = nome.upper().strip()
            codigo_chave = str(codigo).strip()

            cfg = {
                "item": nome,
                "descricao": nome,
                "codigo": codigo_chave,
                "limite": limite
            }

            itens[chave] = cfg
            #itens_por_codigo[codigo_chave] = cfg
            if codigo_chave not in itens_por_codigo:
                itens_por_codigo[codigo_chave] = cfg

        # Camisa Polo Masculina - limite 4
        add_item("Camisa Polo Masculina - R$ 88,04 | PP", "100011367", 4)
        add_item("Camisa Polo Masculina - R$ 88,04 | P", "100011368", 4)
        add_item("Camisa Polo Masculina - R$ 88,04 | M", "100011369", 4)
        add_item("Camisa Polo Masculina - R$ 88,04 | G", "100011370", 4)
        add_item("Camisa Polo Masculina - R$ 88,04 | GG", "100011371", 4)
        add_item("Camisa Polo Masculina - R$ 88,04 | XG", "100011372", 4)
        add_item("Camisa Polo Masculina - R$ 88,04 | XGG", "100011373", 4)
        add_item("Camisa Polo Masculina - R$ 88,04 | EXGG", "100011374", 4)
        add_item("Camisa Polo Masculina - R$ 88,04 | Especial E1 5G", "100011375", 4)
        add_item("Camisa Polo Masculina - R$ 88,04 | Especial E2 7G", "100011376", 4)

        # Camisa Polo Feminina Baby Look - limite 4
        add_item("Camisa Polo Feminina Baby Look - R$ 88,04 | PP", "100011377", 4)
        add_item("Camisa Polo Feminina Baby Look - R$ 88,04 | P", "100011378", 4)
        add_item("Camisa Polo Feminina Baby Look - R$ 88,04 | M", "100011379", 4)
        add_item("Camisa Polo Feminina Baby Look - R$ 88,04 | G", "100011380", 4)
        add_item("Camisa Polo Feminina Baby Look - R$ 88,04 | GG", "100011382", 4)
        add_item("Camisa Polo Feminina Baby Look - R$ 88,04 | XG", "100011383", 4)
        add_item("Camisa Polo Feminina Baby Look - R$ 88,04 | XGG", "100011384", 4)
        add_item("Camisa Polo Feminina Baby Look - R$ 88,04 | EXGG", "100011385", 4)

        # Calça Jeans Masculina - limite 2
        add_item("Calça Jeans Masculina - R$ 110,00 | 34", "100011544", 2)
        add_item("Calça Jeans Masculina - R$ 110,00 | 36", "100011545", 2)
        add_item("Calça Jeans Masculina - R$ 110,00 | 38", "100011546", 2)
        add_item("Calça Jeans Masculina - R$ 110,00 | 40", "100011547", 2)
        add_item("Calça Jeans Masculina - R$ 110,00 | 42", "100011548", 2)
        add_item("Calça Jeans Masculina - R$ 110,00 | 44", "100011549", 2)
        add_item("Calça Jeans Masculina - R$ 110,00 | 46", "100011550", 2)
        add_item("Calça Jeans Masculina - R$ 110,00 | 48", "100011551", 2)
        add_item("Calça Jeans Masculina - R$ 110,00 | 50", "100011552", 2)
        add_item("Calça Jeans Masculina - R$ 110,00 | 52", "100011553", 2)
        add_item("Calça Jeans Masculina - R$ 110,00 | 54", "100011554", 2)
        add_item("Calça Jeans Masculina - R$ 110,00 | 56", "100011555", 2)

        # Calça Jeans Feminina - limite 2
        add_item("Calça Jeans Feminina - R$ 110,00 | 32", "100011530", 2)
        add_item("Calça Jeans Feminina - R$ 110,00 | 34", "100011531", 2)
        add_item("Calça Jeans Feminina - R$ 110,00 | 36", "100011532", 2)
        add_item("Calça Jeans Feminina - R$ 110,00 | 38", "100011533", 2)
        add_item("Calça Jeans Feminina - R$ 110,00 | 40", "100011534", 2)
        add_item("Calça Jeans Feminina - R$ 110,00 | 42", "100011535", 2)
        add_item("Calça Jeans Feminina - R$ 110,00 | 44", "100011536", 2)
        add_item("Calça Jeans Feminina - R$ 110,00 | 46", "100011537", 2)
        add_item("Calça Jeans Feminina - R$ 110,00 | 48", "100011538", 2)
        add_item("Calça Jeans Feminina - R$ 110,00 | 50", "100011539", 2)
        add_item("Calça Jeans Feminina - R$ 110,00 | 52", "100011540", 2)
        add_item("Calça Jeans Feminina - R$ 110,00 | 54", "100011541", 2)
        add_item("Calça Jeans Feminina - R$ 110,00 | 56", "100011542", 2)
        add_item("Calça Jeans Feminina - R$ 110,00 | 58", "100011543", 2)

        # Camisa Social Jeans Masculina - limite 2
        add_item("Camisa Social Jeans Masculina - R$ 125,00 | 1", "100011563", 2)
        add_item("Camisa Social Jeans Masculina - R$ 125,00 | 2", "100011564", 2)
        add_item("Camisa Social Jeans Masculina - R$ 125,00 | 3", "100011565", 2)
        add_item("Camisa Social Jeans Masculina - R$ 125,00 | 4", "100011566", 2)
        add_item("Camisa Social Jeans Masculina - R$ 125,00 | 5", "100011567", 2)
        add_item("Camisa Social Jeans Masculina - R$ 125,00 | 6", "100011568", 2)
        add_item("Camisa Social Jeans Masculina - R$ 125,00 | 7", "100011569", 2)
        add_item("Camisa Social Jeans Masculina - R$ 125,00 | 8", "100011570", 2)
        add_item("Camisa Social Jeans Masculina - R$ 125,00 | 9", "100011571", 2)
        add_item("Camisa Social Jeans Masculina - R$ 125,00 | 10", "100011572", 2)
        add_item("Camisa Social Jeans Masculina - R$ 125,00 | 11", "100011573", 2)
        add_item("Camisa Social Jeans Masculina - R$ 125,00 | 12", "100011574", 2)

        # Camisa Social Jeans Feminina - limite 2
        add_item("Camisa Social Jeans Feminina - R$ 125,00 | PP", "100011556", 2)
        add_item("Camisa Social Jeans Feminina - R$ 125,00 | P", "100011557", 2)
        add_item("Camisa Social Jeans Feminina - R$ 125,00 | M", "100011558", 2)
        add_item("Camisa Social Jeans Feminina - R$ 125,00 | G", "100011559", 2)
        add_item("Camisa Social Jeans Feminina - R$ 125,00 | GG", "100011560", 2)
        add_item("Camisa Social Jeans Feminina - R$ 125,00 | XG", "100011561", 2)
        add_item("Camisa Social Jeans Feminina - R$ 125,00 | XGG", "100011562", 2)
        add_item("Camisa Social Jeans Feminina - R$ 125,00 | EG", "100011563", 2)
        
        # Jaqueta BBTS Masculina - limite 1
        add_item("Jaqueta BBTS Masculina | PP", "000000001", 1)
        add_item("Jaqueta BBTS Masculina | P", "000000001", 1)
        add_item("Jaqueta BBTS Masculina | M", "000000001", 1)
        add_item("Jaqueta BBTS Masculina | G", "000000001", 1)
        add_item("Jaqueta BBTS Masculina | GG", "000000001", 1)
        add_item("Jaqueta BBTS Masculina | G1", "000000001", 1)
        add_item("Jaqueta BBTS Masculina | G2", "000000001", 1)

        # Jaqueta BBTS Feminina - limite 1
        add_item("Jaqueta BBTS Feminina | PP", "000000001", 1)
        add_item("Jaqueta BBTS Feminina | P", "000000001", 1)
        add_item("Jaqueta BBTS Feminina | M", "000000001", 1)
        add_item("Jaqueta BBTS Feminina | G", "000000001", 1)
        add_item("Jaqueta BBTS Feminina | GG", "000000001", 1)
        add_item("Jaqueta BBTS Feminina | G1", "000000001", 1)
        add_item("Jaqueta BBTS Feminina | G2", "000000001", 1)

        # ============================================================
        # IMPORTAÇÃO
        # ============================================================

# ============================================================
# IMPORTAÇÃO
# ============================================================

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
            "Provider=Microsoft.ACE.OLEDB.12.0;"
            "Data Source={0};"
            "Extended Properties='Text;HDR=YES;FMT=Delimited(;)';",
            pasta
        )
        origens = ["[" + nomeArquivo + "]"]

    elif extensao == ".xls":
        _StringConexao = String.Format(
            "Provider=Microsoft.ACE.OLEDB.12.0;"
            "Data Source={0};"
            "Extended Properties='Excel 8.0;HDR=YES;IMEX=1;TypeGuessRows=0;ImportMixedTypes=Text';",
            _Arquivo
        )
        origens = ["[ITENS$]", "[UNIFORMES_EPI$]", "[UNIFORMES$]"]

    else:
        _StringConexao = String.Format(
            "Provider=Microsoft.ACE.OLEDB.12.0;"
            "Data Source={0};"
            "Extended Properties='Excel 12.0 Xml;HDR=YES;IMEX=1;TypeGuessRows=0;ImportMixedTypes=Text';",
            _Arquivo
        )
        origens = ["[ITENS$]", "[UNIFORMES_EPI$]", "[UNIFORMES$]"]

    total_linhas = 0
    adicionadas = 0
    erros = 0
    duplicadas = 0

    conexao = OleDbConnection(_StringConexao)

    try:
        conexao.Open()

        ds = None
        ultimo_erro = ""

        for origem in origens:
            try:
                try:
                    cmd_text = "SELECT [ITEM],[QUANTIDADE],[DESCRICAO],[TAMANHO],[CODIGO],[MATRICULA] FROM " + origem
                    adapter = OleDbDataAdapter(cmd_text, conexao)

                    ds_teste = DataSet()
                    adapter.Fill(ds_teste)

                except:
                    cmd_text = "SELECT * FROM " + origem
                    adapter = OleDbDataAdapter(cmd_text, conexao)

                    ds_teste = DataSet()
                    adapter.Fill(ds_teste)

                if ds_teste.Tables.Count > 0:
                    ds = ds_teste
                    break

            except Exception as ex:
                ultimo_erro = str(ex)
                continue

        if ds == None:
            raise Exception(
                "Não foi possível ler a planilha. Verifique se a aba se chama ITENS, UNIFORMES_EPI ou UNIFORMES. Último erro: " + ultimo_erro
            )

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

                if valor == DBNull.Value:
                    return None

                texto = str(valor).strip()

                if texto == "":
                    return None

                return texto

            except:
                return None

        def normalizar(valor):
            texto = to_str(valor)

            if texto is None:
                return ""

            texto = texto.replace(u"\xa0", " ")
            texto = texto.strip()

            while texto.find("  ") >= 0:
                texto = texto.replace("  ", " ")

            return texto
            
        def normalizar_matricula(valor):
            texto = normalizar(valor)

            if texto == "":
                return ""

            texto = texto.replace(",", ".")
            texto = texto.strip()

            if texto.endswith(".0"):
                texto = texto[:-2]

            return texto

        def normalizar_codigo(valor):
            texto = normalizar(valor)

            if texto == "":
                return ""

            texto = texto.replace(",", ".")
            texto = texto.strip()

            if texto.endswith(".0"):
                texto = texto[:-2]

            return texto

        def get_campos_linha(row):
            try:
                qtd_colunas = row.Table.Columns.Count
            except:
                qtd_colunas = 0

            # Caso normal com 6 colunas:
            # ITEM | QUANTIDADE | DESCRICAO | TAMANHO | CODIGO | MATRICULA
            if qtd_colunas >= 6:
                c0 = get_idx(row, 0)
                c1 = get_idx(row, 1)
                c2 = get_idx(row, 2)
                c3 = get_idx(row, 3)
                c4 = get_idx(row, 4)
                c5 = get_idx(row, 5)

                texto_primeira = to_str(c0)

                # Caso CSV tenha vindo todo na primeira coluna separado por ;
                if c1 is None and texto_primeira != None and texto_primeira.find(";") >= 0:
                    partes = texto_primeira.split(";")

                    while len(partes) < 6:
                        partes.append("")

                    matricula = partes[5]

                    if len(partes) > 6:
                        matricula = ";".join(partes[5:])

                    return partes[0], partes[1], partes[2], partes[3], partes[4], matricula

                return c0, c1, c2, c3, c4, c5

            # Compatibilidade com planilhas antigas sem MATRICULA
            if qtd_colunas >= 5:
                c0 = get_idx(row, 0)
                c1 = get_idx(row, 1)
                c2 = get_idx(row, 2)
                c3 = get_idx(row, 3)
                c4 = get_idx(row, 4)

                texto_primeira = to_str(c0)

                if c1 is None and texto_primeira != None and texto_primeira.find(";") >= 0:
                    partes = texto_primeira.split(";")

                    while len(partes) < 6:
                        partes.append("")

                    matricula = partes[5]

                    if len(partes) > 6:
                        matricula = ";".join(partes[5:])

                    return partes[0], partes[1], partes[2], partes[3], partes[4], matricula

                return c0, c1, c2, c3, c4, None

            # Caso extremo: CSV inteiro em uma coluna
            valor_unico = get_idx(row, 0)
            texto = to_str(valor_unico)

            if texto != None and texto.find(";") >= 0:
                partes = texto.split(";")

                while len(partes) < 6:
                    partes.append("")

                matricula = partes[5]

                if len(partes) > 6:
                    matricula = ";".join(partes[5:])

                return partes[0], partes[1], partes[2], partes[3], partes[4], matricula

            return valor_unico, None, None, None, None, None

        def linha_vazia(item_excel, quantidade_excel, descricao_excel, tamanho_excel, codigo_excel, matricula_excel):
            if (
                to_str(item_excel) is None and
                to_str(quantidade_excel) is None and
                to_str(descricao_excel) is None and
                to_str(tamanho_excel) is None and
                to_str(codigo_excel) is None and
                to_str(matricula_excel) is None
            ):
                return True

            return False

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
                    raise Exception("Quantidade deve ser maior que zero.")

                return qtd

            except Exception as ex:
                raise Exception("Quantidade inválida: '{0}'. {1}".format(str(valor), str(ex)))

        def obter_cfg_item(valor_item, valor_codigo):
            item_txt = normalizar(valor_item)
            codigo_txt = normalizar_codigo(valor_codigo)

            # Tentativa 1: pelo ITEM
            if item_txt != "":
                chave = item_txt.upper()

                if chave in itens:
                    return itens[chave]

                raise Exception("ITEM inválido ou não cadastrado no mapeamento: '{0}'.".format(item_txt))

            # Tentativa 2: pelo CODIGO, caso o ITEM venha vazio pelo OleDb
            if codigo_txt != "":
                if codigo_txt in itens_por_codigo:
                    return itens_por_codigo[codigo_txt]

                raise Exception("ITEM não informado e CODIGO não cadastrado no mapeamento: '{0}'.".format(codigo_txt))

            raise Exception("ITEM não informado.")

        def obter_tamanho(item_nome, tamanho_excel):
            tamanho_txt = normalizar(tamanho_excel)

            if tamanho_txt != "":
                return tamanho_txt

            try:
                return item_nome.split(" | ")[1]
            except:
                return ""

        def item_ja_existe_no_grid(item_nome, matricula):
            try:
                grid = OrdemServico.GetCustom(nomeGrid)

                for linha_grid in grid.Rows:
                    try:
                        item_grid = linha_grid["ITEM"]
                        matricula_grid = ""

                        try:
                            matricula_grid = linha_grid["MATRICULA"]
                        except:
                            matricula_grid = ""

                        item_grid_txt = normalizar(item_grid).upper()
                        matricula_grid_txt = normalizar(matricula_grid).upper()

                        if (
                            item_grid_txt == item_nome.strip().upper() and
                            matricula_grid_txt == matricula.strip().upper()
                        ):
                            return True

                    except:
                        pass

            except:
                pass

            return False

        itens_importados = {}

        for linha in tbl.Rows:
            total_linhas += 1

            item_excel, quantidade_excel, descricao_excel, tamanho_excel, codigo_excel, matricula_excel = get_campos_linha(linha)

            if linha_vazia(item_excel, quantidade_excel, descricao_excel, tamanho_excel, codigo_excel, matricula_excel):
                continue

            try:
                cfg = obter_cfg_item(item_excel, codigo_excel)

                item_final = cfg["item"]
                descricao_final = cfg["descricao"]
                codigo_final = cfg["codigo"]
                limite = cfg["limite"]

                quantidade_final = to_qtd_int(quantidade_excel)

                matricula_final = normalizar_matricula(matricula_excel)

                if matricula_final == "":
                    raise Exception("MATRICULA não informada.")

                if limite != None and quantidade_final > limite:
                    raise Exception(
                        "Quantidade maior que o permitido para o item '{0}'. Limite: {1}. Quantidade informada: {2}.".format(
                            item_final,
                            limite,
                            quantidade_final
                        )
                    )

                tamanho_final = obter_tamanho(item_final, tamanho_excel)

                # Agora a duplicidade considera ITEM + MATRICULA
                chave_item = item_final.strip().upper() + "|" + matricula_final.strip().upper()

                if chave_item in itens_importados:
                    duplicadas += 1
                    raise Exception(
                        "ITEM duplicado no arquivo para a mesma matrícula: '{0}' / matrícula: '{1}'.".format(
                            item_final,
                            matricula_final
                        )
                    )

                if item_ja_existe_no_grid(item_final, matricula_final):
                    duplicadas += 1
                    raise Exception(
                        "ITEM já existe na GRID para esta matrícula: '{0}' / matrícula: '{1}'.".format(
                            item_final,
                            matricula_final
                        )
                    )

                itens_importados[chave_item] = True

                valores = [
                    item_final,
                    quantidade_final,
                    descricao_final,
                    tamanho_final,
                    codigo_final,
                    matricula_final
                ]

                OrdemServico.AdicionaLinhaRegistro(nomeGrid, nomesCampos, valores)
                adicionadas += 1

            except Exception as ex:
                Formulario.ExibeMensagem("Erro na linha {0}: {1}".format(total_linhas, str(ex)))
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
        "Duplicadas/ignoradas: {2}\n"
        "Erros: {3}\n"
        "Total na GRID agora: {4}"
    ).format(total_linhas, adicionadas, duplicadas, erros, qtd)

    Formulario.ExibeMensagem(resumo)


readExcel(
    [
        "ITEM",
        "QUANTIDADE",
        "DESCRICAO",
        "TAMANHO",
        "CODIGO",
        "MATRICULA"
    ],
    "UNIFORMES_EPI_LOTE"
)
```
  - PS_LABEL1 "Texto Informativo" [Label String(2000) → CPE_PESSOAS.PS_LABEL1]
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Arquivo — RequeridoInicial=true
- ClientesAutorizados:
  - PapelProcessoId=68328; PapelAutorizado=Dires
  - PapelProcessoId=68329; PapelAutorizado=Fila CSC Gabriel

### [343967] SubProcesso "Abertura do chamado Recebimento de Uniformes"
Responsável: Cliente (papel 18)
Config: AssociacaoId=1659; ChamadaAssincrona=true; PassaTodosItens=true; SincronizaCancelamento=true; Configuracao={"ExibirBotaoNovaSubprocessos":true}
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
import clr
import System
clr.AddReference('Supravizio.Custom')

from System import Convert, DBNull
from Venki.Supravizio.Recurso.Custom import Pessoa


def Texto(valor):
    try:
        if valor is None:
            return ""

        if valor == DBNull.Value:
            return ""

        texto = str(valor).strip()

        if texto == "":
            return ""

        return texto
    except:
        return ""


def RegistrarLog(texto):
    try:
        Formulario.ExibeMensagem(texto)
    except:
        pass

    try:
        OrdemServico.AdicionaComentario(texto, True)
    except:
        pass


def ValorLinha(linha, campo):
    try:
        valor = linha[campo]

        if valor is None or valor == DBNull.Value:
            return ""

        return str(valor).strip()
    except:
        return ""


def QuantidadeLinhaValor(valor):
    try:
        texto = Texto(valor)

        if texto == "":
            return 0

        texto = texto.replace(",", ".")

        return Convert.ToInt32(Convert.ToDouble(texto))
    except:
        return 0


def ExtrairTamanho(item):
    try:
        texto = Texto(item)

        if texto.find(" | ") >= 0:
            return texto.split(" | ")[1].strip()

        return ""
    except:
        return ""


def NormalizarCodigo(valor):
    codigo = Texto(valor)

    if codigo == "":
        return ""

    codigo = codigo.replace(",", ".").strip()

    if codigo.endswith(".0"):
        codigo = codigo[:-2]

    return codigo


#def DefinirClienteSubprocesso(sub):
#    try:
#        if OrdemServico.Cliente != None:
#            sub.Cliente = OrdemServico.Cliente
#            return True
#    except:
#        pass
#
#    try:
#        if OrdemServico.Favorecido != None:
#            sub.Cliente = OrdemServico.Favorecido
#            return True
#    except:
#        pass
#
#    try:
#        favorecido = OrdemServico.GetCustom("FAVORECIDO_COBRA")
#        favorecidoTexto = Texto(favorecido)
#
#        if favorecidoTexto != "":
#            sub.Cliente = Pessoa.Carrega(Convert.ToInt32(favorecidoTexto))
#            return True
#    except:
#        pass
#
#    return False


# ============================================================
# MAPA DE CÓDIGOS PARA RECUPERAR ITEM QUANDO ITEM VEM VAZIO
# ============================================================

mapa_codigo_itens = {}

def AddCodigo(codigo, item):
    codigo = NormalizarCodigo(codigo)

    if codigo == "":
        return

    if codigo not in mapa_codigo_itens:
        mapa_codigo_itens[codigo] = []

    mapa_codigo_itens[codigo].append(item)


# Camisa Polo Masculina
AddCodigo("100011367", "Camisa Polo Masculina - R$ 88,04 | PP")
AddCodigo("100011368", "Camisa Polo Masculina - R$ 88,04 | P")
AddCodigo("100011369", "Camisa Polo Masculina - R$ 88,04 | M")
AddCodigo("100011370", "Camisa Polo Masculina - R$ 88,04 | G")
AddCodigo("100011371", "Camisa Polo Masculina - R$ 88,04 | GG")
AddCodigo("100011372", "Camisa Polo Masculina - R$ 88,04 | XG")
AddCodigo("100011373", "Camisa Polo Masculina - R$ 88,04 | XGG")
AddCodigo("100011374", "Camisa Polo Masculina - R$ 88,04 | EXGG")
AddCodigo("100011375", "Camisa Polo Masculina - R$ 88,04 | Especial E1 5G")
AddCodigo("100011376", "Camisa Polo Masculina - R$ 88,04 | Especial E2 7G")

# Camisa Polo Feminina Baby Look
AddCodigo("100011377", "Camisa Polo Feminina Baby Look - R$ 88,04 | PP")
AddCodigo("100011378", "Camisa Polo Feminina Baby Look - R$ 88,04 | P")
AddCodigo("100011379", "Camisa Polo Feminina Baby Look - R$ 88,04 | M")
AddCodigo("100011380", "Camisa Polo Feminina Baby Look - R$ 88,04 | G")
AddCodigo("100011382", "Camisa Polo Feminina Baby Look - R$ 88,04 | GG")
AddCodigo("100011383", "Camisa Polo Feminina Baby Look - R$ 88,04 | XG")
AddCodigo("100011384", "Camisa Polo Feminina Baby Look - R$ 88,04 | XGG")
AddCodigo("100011385", "Camisa Polo Feminina Baby Look - R$ 88,04 | EXGG")

# Calça Jeans Masculina
AddCodigo("100011544", "Calça Jeans Masculina - R$ 110,00 | 34")
AddCodigo("100011545", "Calça Jeans Masculina - R$ 110,00 | 36")
AddCodigo("100011546", "Calça Jeans Masculina - R$ 110,00 | 38")
AddCodigo("100011547", "Calça Jeans Masculina - R$ 110,00 | 40")
AddCodigo("100011548", "Calça Jeans Masculina - R$ 110,00 | 42")
AddCodigo("100011549", "Calça Jeans Masculina - R$ 110,00 | 44")
AddCodigo("100011550", "Calça Jeans Masculina - R$ 110,00 | 46")
AddCodigo("100011551", "Calça Jeans Masculina - R$ 110,00 | 48")
AddCodigo("100011552", "Calça Jeans Masculina - R$ 110,00 | 50")
AddCodigo("100011553", "Calça Jeans Masculina - R$ 110,00 | 52")
AddCodigo("100011554", "Calça Jeans Masculina - R$ 110,00 | 54")
AddCodigo("100011555", "Calça Jeans Masculina - R$ 110,00 | 56")

# Calça Jeans Feminina
AddCodigo("100011530", "Calça Jeans Feminina - R$ 110,00 | 32")
AddCodigo("100011531", "Calça Jeans Feminina - R$ 110,00 | 34")
AddCodigo("100011532", "Calça Jeans Feminina - R$ 110,00 | 36")
AddCodigo("100011533", "Calça Jeans Feminina - R$ 110,00 | 38")
AddCodigo("100011534", "Calça Jeans Feminina - R$ 110,00 | 40")
AddCodigo("100011535", "Calça Jeans Feminina - R$ 110,00 | 42")
AddCodigo("100011536", "Calça Jeans Feminina - R$ 110,00 | 44")
AddCodigo("100011537", "Calça Jeans Feminina - R$ 110,00 | 46")
AddCodigo("100011538", "Calça Jeans Feminina - R$ 110,00 | 48")
AddCodigo("100011539", "Calça Jeans Feminina - R$ 110,00 | 50")
AddCodigo("100011540", "Calça Jeans Feminina - R$ 110,00 | 52")
AddCodigo("100011541", "Calça Jeans Feminina - R$ 110,00 | 54")
AddCodigo("100011542", "Calça Jeans Feminina - R$ 110,00 | 56")
AddCodigo("100011543", "Calça Jeans Feminina - R$ 110,00 | 58")

# Camisa Social Jeans Masculina
AddCodigo("100011563", "Camisa Social Jeans Masculina - R$ 125,00 | 1")
AddCodigo("100011564", "Camisa Social Jeans Masculina - R$ 125,00 | 2")
AddCodigo("100011565", "Camisa Social Jeans Masculina - R$ 125,00 | 3")
AddCodigo("100011566", "Camisa Social Jeans Masculina - R$ 125,00 | 4")
AddCodigo("100011567", "Camisa Social Jeans Masculina - R$ 125,00 | 5")
AddCodigo("100011568", "Camisa Social Jeans Masculina - R$ 125,00 | 6")
AddCodigo("100011569", "Camisa Social Jeans Masculina - R$ 125,00 | 7")
AddCodigo("100011570", "Camisa Social Jeans Masculina - R$ 125,00 | 8")
AddCodigo("100011571", "Camisa Social Jeans Masculina - R$ 125,00 | 9")
AddCodigo("100011572", "Camisa Social Jeans Masculina - R$ 125,00 | 10")
AddCodigo("100011573", "Camisa Social Jeans Masculina - R$ 125,00 | 11")
AddCodigo("100011574", "Camisa Social Jeans Masculina - R$ 125,00 | 12")

# Camisa Social Jeans Feminina
AddCodigo("100011556", "Camisa Social Jeans Feminina - R$ 125,00 | PP")
AddCodigo("100011557", "Camisa Social Jeans Feminina - R$ 125,00 | P")
AddCodigo("100011558", "Camisa Social Jeans Feminina - R$ 125,00 | M")
AddCodigo("100011559", "Camisa Social Jeans Feminina - R$ 125,00 | G")
AddCodigo("100011560", "Camisa Social Jeans Feminina - R$ 125,00 | GG")
AddCodigo("100011561", "Camisa Social Jeans Feminina - R$ 125,00 | XG")
AddCodigo("100011562", "Camisa Social Jeans Feminina - R$ 125,00 | XGG")
AddCodigo("100011563", "Camisa Social Jeans Feminina - R$ 125,00 | EG")

# Jaqueta BBTS Masculina
AddCodigo("000000001", "Jaqueta BBTS Masculina | PP")
AddCodigo("000000001", "Jaqueta BBTS Masculina | P")
AddCodigo("000000001", "Jaqueta BBTS Masculina | M")
AddCodigo("000000001", "Jaqueta BBTS Masculina | G")
AddCodigo("000000001", "Jaqueta BBTS Masculina | GG")
AddCodigo("000000001", "Jaqueta BBTS Masculina | G1")
AddCodigo("000000001", "Jaqueta BBTS Masculina | G2")

# Jaqueta BBTS Feminina
AddCodigo("000000001", "Jaqueta BBTS Feminina | PP")
AddCodigo("000000001", "Jaqueta BBTS Feminina | P")
AddCodigo("000000001", "Jaqueta BBTS Feminina | M")
AddCodigo("000000001", "Jaqueta BBTS Feminina | G")
AddCodigo("000000001", "Jaqueta BBTS Feminina | GG")
AddCodigo("000000001", "Jaqueta BBTS Feminina | G1")
AddCodigo("000000001", "Jaqueta BBTS Feminina | G2")


def ResolverItemPorCodigo(codigo, tamanho):
    codigo = NormalizarCodigo(codigo)
    tamanho = Texto(tamanho)

    if codigo == "":
        return ""

    if codigo not in mapa_codigo_itens:
        return ""

    encontrados = mapa_codigo_itens[codigo]

    if len(encontrados) == 1:
        return encontrados[0]

    # Se tiver código duplicado, tenta resolver pelo tamanho.
    if tamanho != "":
        candidatos = []

        for item in encontrados:
            try:
                if item.endswith("| " + tamanho):
                    candidatos.append(item)
            except:
                pass

        if len(candidatos) == 1:
            return candidatos[0]

    # Código ambíguo.
    return ""


# ============================================================
# LEITURA DA GRID DO LOTE
# ============================================================

# ============================================================
# LEITURA DA GRID DO LOTE AGRUPANDO POR MATRÍCULA
# ============================================================

def NormalizarMatricula(valor):
    texto = Texto(valor)

    if texto == "":
        return ""

    texto = texto.replace(",", ".").strip()

    if texto.endswith(".0"):
        texto = texto[:-2]

    return texto


def DefinirClienteSubprocessoPorMatricula(sub, matricula):
    try:
        matricula = NormalizarMatricula(matricula)

        if matricula != "":
            sql = (
                "Select P.ID_PESSOA "
                "From PESSOA P "
                "Inner Join CP_PESSOA CP On P.ID_PESSOA = CP.ID_PESSOA "
                "Where CP.MATRICULA = '" + matricula.replace("'", "''") + "'"
            )

            dados = DB.ExecuteDataTable(sql)

            if dados.Rows.Count > 0:
                idPessoa = Convert.ToInt32(dados.Rows[0]["ID_PESSOA"])
                sub.Cliente = Pessoa.Carrega(idPessoa)
                return True
    except:
        pass

    try:
        if OrdemServico.Cliente != None:
            sub.Cliente = OrdemServico.Cliente
            return True
    except:
        pass

    try:
        if OrdemServico.Favorecido != None:
            sub.Cliente = OrdemServico.Favorecido
            return True
    except:
        pass

    return False


def LimparGridSubprocesso(sub, nomeGrid):
    try:
        grid_sub = sub.GetCustom(nomeGrid)

        try:
            grid_sub.Rows.Clear()
            return True
        except:
            pass

        try:
            while grid_sub.Rows.Count > 0:
                grid_sub.Rows.RemoveAt(0)
            return True
        except:
            pass

    except:
        pass

    return False


grid = OrdemServico.GetCustom("UNIFORMES_EPI_LOTE")

grupos_por_matricula = {}
itens_ja_lidos = {}
log = ""

try:
    indice = 0

    for linha in grid.Rows:
        indice += 1

        item = ValorLinha(linha, "ITEM")
        quantidade = ValorLinha(linha, "QUANTIDADE")
        descricao = ValorLinha(linha, "DESCRICAO")
        tamanho = ValorLinha(linha, "TAMANHO")
        codigo = ValorLinha(linha, "CODIGO")
        matricula = NormalizarMatricula(ValorLinha(linha, "MATRICULA"))

        if item == "" and descricao != "":
            item = descricao

        if item == "" and codigo != "":
            itemResolvido = ResolverItemPorCodigo(codigo, tamanho)

            if itemResolvido != "":
                item = itemResolvido
                log += "\nLinha {0}: ITEM resolvido pelo CODIGO {1}: {2}".format(
                    indice,
                    codigo,
                    item
                )
            else:
                log += "\nLinha {0}: não conseguiu resolver ITEM pelo CODIGO {1} e TAMANHO {2}".format(
                    indice,
                    codigo,
                    tamanho
                )

        if descricao == "" and item != "":
            descricao = item

        if tamanho == "" and item != "":
            tamanho = ExtrairTamanho(item)

        if item == "" and quantidade == "" and descricao == "" and tamanho == "" and codigo == "" and matricula == "":
            continue

        if matricula == "":
            log += "\nLinha {0} ignorada: MATRÍCULA não informada. ITEM={1}, CODIGO={2}".format(
                indice,
                item,
                codigo
            )
            continue

        chave = (
            matricula.upper().strip() + "|" +
            item.upper().strip() + "|" +
            codigo.upper().strip() + "|" +
            tamanho.upper().strip()
        )

        if chave in itens_ja_lidos:
            log += "\nLinha {0} ignorada por duplicidade no lote: MATRICULA={1}, ITEM={2}, CODIGO={3}, TAMANHO={4}".format(
                indice,
                matricula,
                item,
                codigo,
                tamanho
            )
            continue

        itens_ja_lidos[chave] = True

        if matricula not in grupos_por_matricula:
            grupos_por_matricula[matricula] = []

        grupos_por_matricula[matricula].append({
            "LINHA": indice,
            "ITEM": item,
            "QUANTIDADE": quantidade,
            "DESCRICAO": descricao,
            "TAMANHO": tamanho,
            "CODIGO": codigo,
            "MATRICULA": matricula
        })

except Exception as ex:
    log += "\nErro ao copiar linhas da grid UNIFORMES_EPI_LOTE: " + Texto(ex)


criados = 0
erros = 0
ignorados = 0
avancados = 0
total_itens = 0

if len(grupos_por_matricula) == 0:
    log += "\nNão existem itens válidos na grid UNIFORMES_EPI_LOTE para gerar subprocessos."

else:

    for matricula in grupos_por_matricula:

        itens_da_matricula = grupos_por_matricula[matricula]

        try:
            log += "\n\nCriando subprocesso para matrícula {0}, quantidade de itens: {1}".format(
                matricula,
                len(itens_da_matricula)
            )

            sub = OrdemServico.IniciaSubProcesso(OrdemServico.Atividade)

            clienteDefinido = DefinirClienteSubprocessoPorMatricula(sub, matricula)

            if clienteDefinido == False:
                log += "\nMatrícula {0}: aviso - não foi possível definir Cliente/Favorecido do subprocesso.".format(matricula)

            try:
                sub.Assunto = "Recebimento de Uniformes - Matrícula " + matricula
            except Exception as exAssunto:
                log += "\nMatrícula {0}: aviso ao definir assunto: {1}".format(
                    matricula,
                    Texto(exAssunto)
                )

            # Tenta limpar a grid do subprocesso antes de adicionar os itens.
            limpou = LimparGridSubprocesso(sub, "UNIFORMES_EPI")

            if limpou:
                log += "\nMatrícula {0}: grid UNIFORMES_EPI limpa antes da inserção.".format(matricula)
            else:
                log += "\nMatrícula {0}: aviso - não foi possível limpar a grid UNIFORMES_EPI antes da inserção.".format(matricula)

            itens_adicionados_no_sub = 0

            for dados_linha in itens_da_matricula:

                numero_linha = dados_linha["LINHA"]
                item = dados_linha["ITEM"]
                quantidade_texto = dados_linha["QUANTIDADE"]
                descricao = dados_linha["DESCRICAO"]
                tamanho = dados_linha["TAMANHO"]
                codigo = dados_linha["CODIGO"]

                quantidade = QuantidadeLinhaValor(quantidade_texto)

                log += "\nProcessando linha {0}: MATRICULA={1}, ITEM={2}, CODIGO={3}, TAMANHO={4}, QUANTIDADE={5}".format(
                    numero_linha,
                    matricula,
                    item,
                    codigo,
                    tamanho,
                    quantidade_texto
                )

                if item == "":
                    ignorados += 1
                    log += "\nLinha {0} ignorada: ITEM vazio. CODIGO={1}, DESCRICAO={2}, TAMANHO={3}".format(
                        numero_linha,
                        codigo,
                        descricao,
                        tamanho
                    )
                    continue

                if quantidade <= 0:
                    ignorados += 1
                    log += "\nLinha {0} ignorada: QUANTIDADE inválida. ITEM={1}, QUANTIDADE={2}".format(
                        numero_linha,
                        item,
                        quantidade_texto
                    )
                    continue

                sub.AdicionaLinhaRegistro(
                    "UNIFORMES_EPI",
                    [
                        "MATRICULA",
                        "ITEM",
                        "QUANTIDADE",
                        "DESCRICAO",
                        "TAMANHO",
                        "CODIGO"
                    ],
                    [
                        matricula,
                        item,
                        quantidade,
                        descricao,
                        tamanho,
                        codigo
                    ]
                )

                itens_adicionados_no_sub += 1
                total_itens += 1

            if itens_adicionados_no_sub == 0:
                ignorados += 1
                log += "\nMatrícula {0}: nenhum item válido para salvar subprocesso.".format(matricula)
                continue

            sub.Salva()
            criados += 1

            log += "\nMatrícula {0}: subprocesso salvo com {1} item(ns).".format(
                matricula,
                itens_adicionados_no_sub
            )

            try:
                sub.AvancaAtividade()
                avancados += 1
                log += "\nMatrícula {0}: subprocesso avançado com sucesso.".format(matricula)
            except Exception as exAvanca:
                log += "\nMatrícula {0}: subprocesso criado, mas não avançou. Erro: {1}".format(
                    matricula,
                    Texto(exAvanca)
                )

        except Exception as ex:
            erros += 1
            log += "\nERRO ao gerar subprocesso para matrícula {0}: {1}".format(
                matricula,
                Texto(ex)
            )
            continue


resumo = (
    "Geração de subprocessos concluída!\n\n"
    "Matrículas encontradas: {0}\n"
    "Itens processados/adicionados: {1}\n"
    "Subprocessos criados/salvos: {2}\n"
    "Subprocessos avançados: {3}\n"
    "Ignorados: {4}\n"
    "Erros: {5}\n\n"
    "Detalhes:\n{6}"
).format(
    len(grupos_por_matricula),
    total_itens,
    criados,
    avancados,
    ignorados,
    erros,
    log
)

RegistrarLog(resumo)

# Se quiser avançar a atividade principal automaticamente depois:
# AvancaProximaAtividade = True
```
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
  - CustomPropertyId=5459; CustomProperty=UNIFORMES_EPI
  - PropertyId=1295; Property=Servico
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=1655; ClasseConfiguracao=Arquivo
- Associação: Ativo=true; FraseAssociacao=Recebimento de Uniforme (Em Lote) -> Recebimento de Uniformes; FraseInversaAssociacao=Recebimento de Uniformes -> Recebimento de Uniforme (Em Lote); CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=UNIFORMELOTE; SeparadorSequencial=. | fonte: Recebimento de Uniforme (Em Lote) → alvo: Recebimento de Uniformes

### [343968] EventoFinal ""

## Papéis usados
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```

## Campos customizados usados (definição global)

### LABEL10 — LABEL10
Label String(700) → CPE_PDCI2019.LABEL10

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### TE_CARGO — Cargo
TextBox String → CPE_CSC.TE_CARGO

### TE_FUNCAO — Função
TextBox String → CPE_CSC.TE_FUNCAO

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### UNIFORMES_EPI_LOTE — Uniformes em lote
DataGrid RecordList → Z_00143_UNIFORMES_EPI_LOTE.UNIFORMES_EPI_LOTE
Colunas do registro:
- MATRICULA "MATRICULA" [TextBox String]
- DESCRICAO "Descrição" [Memo String]
- QUANTIDADE "Quantidade" [TextBox Integer]
- ITEM "ITEM" [DropDownList String]
**ITEM.LookupScript**
```python
itens = [
    # Camisa Polo Masculina
    "Camisa Polo Masculina - R$ 88,04 | PP",
    "Camisa Polo Masculina - R$ 88,04 | P",
    "Camisa Polo Masculina - R$ 88,04 | M",
    "Camisa Polo Masculina - R$ 88,04 | G",
    "Camisa Polo Masculina - R$ 88,04 | GG",
    "Camisa Polo Masculina - R$ 88,04 | XG",
    "Camisa Polo Masculina - R$ 88,04 | XGG",
    "Camisa Polo Masculina - R$ 88,04 | EXGG",
    "Camisa Polo Masculina - R$ 88,04 | Especial E1 5G",
    "Camisa Polo Masculina - R$ 88,04 | Especial E2 7G",

    # Camisa Polo Feminina Baby Look
    "Camisa Polo Feminina Baby Look - R$ 88,04 | PP",
    "Camisa Polo Feminina Baby Look - R$ 88,04 | P",
    "Camisa Polo Feminina Baby Look - R$ 88,04 | M",
    "Camisa Polo Feminina Baby Look - R$ 88,04 | G",
    "Camisa Polo Feminina Baby Look - R$ 88,04 | GG",
    "Camisa Polo Feminina Baby Look - R$ 88,04 | XG",
    "Camisa Polo Feminina Baby Look - R$ 88,04 | XGG",
    "Camisa Polo Feminina Baby Look - R$ 88,04 | EXGG",

    # Calça Jeans Masculina
    "Calça Jeans Masculina - R$ 110,00 | 34",
    "Calça Jeans Masculina - R$ 110,00 | 36",
    "Calça Jeans Masculina - R$ 110,00 | 38",
    "Calça Jeans Masculina - R$ 110,00 | 40",
    "Calça Jeans Masculina - R$ 110,00 | 42",
    "Calça Jeans Masculina - R$ 110,00 | 44",
    "Calça Jeans Masculina - R$ 110,00 | 46",
    "Calça Jeans Masculina - R$ 110,00 | 48",
    "Calça Jeans Masculina - R$ 110,00 | 50",
    "Calça Jeans Masculina - R$ 110,00 | 52",
    "Calça Jeans Masculina - R$ 110,00 | 54",
    "Calça Jeans Masculina - R$ 110,00 | 56",

    # Calça Jeans Feminina
    "Calça Jeans Feminina - R$ 110,00 | 32",
    "Calça Jeans Feminina - R$ 110,00 | 34",
    "Calça Jeans Feminina - R$ 110,00 | 36",
    "Calça Jeans Feminina - R$ 110,00 | 38",
    "Calça Jeans Feminina - R$ 110,00 | 40",
    "Calça Jeans Feminina - R$ 110,00 | 42",
    "Calça Jeans Feminina - R$ 110,00 | 44",
    "Calça Jeans Feminina - R$ 110,00 | 46",
    "Calça Jeans Feminina - R$ 110,00 | 48",
    "Calça Jeans Feminina - R$ 110,00 | 50",
    "Calça Jeans Feminina - R$ 110,00 | 52",
    "Calça Jeans Feminina - R$ 110,00 | 54",
    "Calça Jeans Feminina - R$ 110,00 | 56",
    "Calça Jeans Feminina - R$ 110,00 | 58",

    # Camisa Social Jeans Masculina
    "Camisa Social Jeans Masculina - R$ 125,00 | 1",
    "Camisa Social Jeans Masculina - R$ 125,00 | 2",
    "Camisa Social Jeans Masculina - R$ 125,00 | 3",
    "Camisa Social Jeans Masculina - R$ 125,00 | 4",
    "Camisa Social Jeans Masculina - R$ 125,00 | 5",
    "Camisa Social Jeans Masculina - R$ 125,00 | 6",
    "Camisa Social Jeans Masculina - R$ 125,00 | 7",
    "Camisa Social Jeans Masculina - R$ 125,00 | 8",
    "Camisa Social Jeans Masculina - R$ 125,00 | 9",
    "Camisa Social Jeans Masculina - R$ 125,00 | 10",
    "Camisa Social Jeans Masculina - R$ 125,00 | 11",
    "Camisa Social Jeans Masculina - R$ 125,00 | 12",

    # Camisa Social Jeans Feminina
    "Camisa Social Jeans Feminina - R$ 125,00 | PP",
    "Camisa Social Jeans Feminina - R$ 125,00 | P",
    "Camisa Social Jeans Feminina - R$ 125,00 | M",
    "Camisa Social Jeans Feminina - R$ 125,00 | G",
    "Camisa Social Jeans Feminina - R$ 125,00 | GG",
    "Camisa Social Jeans Feminina - R$ 125,00 | XG",
    "Camisa Social Jeans Feminina - R$ 125,00 | XGG",
    "Camisa Social Jeans Feminina - R$ 125,00 | EG",
    
    # Jaqueta BBTS Masculina
    "Jaqueta BBTS Masculina | PP",
    "Jaqueta BBTS Masculina | P",
    "Jaqueta BBTS Masculina | M",
    "Jaqueta BBTS Masculina | G",
    "Jaqueta BBTS Masculina | GG",
    "Jaqueta BBTS Masculina | G1",
    "Jaqueta BBTS Masculina | G2",

    # Jaqueta BBTS Feminina
    "Jaqueta BBTS Feminina | PP",
    "Jaqueta BBTS Feminina | P",
    "Jaqueta BBTS Feminina | M",
    "Jaqueta BBTS Feminina | G",
    "Jaqueta BBTS Feminina | GG",
    "Jaqueta BBTS Feminina | G1",
    "Jaqueta BBTS Feminina | G2"
]

Itens = itens
```
- TAMANHO "TAMANHO" [TextBox String]
- CODIGO "CODIGO" [TextBox String]

### TAMANHO — Tamanho
Memo String → CPE_CSC.TAMANHO

### LABEL109 — LABEL109
Label String(1000) → CPE_CONTRATOS.LABEL109

### CHECKBOX1 — Checkbox1
CheckBox Boolean → CPE_PESSOAS.CHECKBOX1

### PS_LABEL1 — Texto Informativo
Label String(2000) → CPE_PESSOAS.PS_LABEL1

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
