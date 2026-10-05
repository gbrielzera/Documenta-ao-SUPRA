# Fluxo: Recebimento de Uniformes (RECUNIFORME) — versão 11
Caminho: Fluxos > Serviços Assistência Técnica Versão 11 Recebimento de Uniformes
XML: `XMLs para teste/Serviços_Assistência_Técnica_Versão_11_Recebimento_de_Uniformes.xml` | Supravizio 19.1.1 | SubProcessoId 16007 | DesenhoProcessoId 2472 | ProcessoId 31
Órgão dono: 2000004019 - DIVISAO DE APOIO A REDE DE SERVICOS | Responsável: JOSE AFRANIO ARAUJO BRANDAO
Classe do subprocesso: CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Recebimento de Uniforme (RECEBIMENTOUNIFORME)

## Grafo do fluxo
- [254570] EventoInicial "" → [253901] Solicitar aprovação do cliente
- [253897] EventoFinal "" {Cliente} → (fim)
- [253898] EventoIntermediarioMensagem "Chamado Finalizado - Recebimento de Uniforme" → [253899] Aviso recebimento de Uniforme
- [253899] EventoIntermediarioMensagem "Aviso recebimento de Uniforme" → [253897] 
- [253900] FimCancelamento "" → (fim)
- [253901] Tarefa "Solicitar aprovação do cliente" {Cliente} → [G61184] Aprovado?
- [253903] EventoIntermediarioMensagem "OS reprovada" → [253900] 
- [G61184] Gateway "Aprovado?" → «Aprovado» [253898] Chamado Finalizado - Recebimento de Uniforme | «Reprovado» [253903] OS reprovada

## Gateways
### [G61184] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAR")
```
- alternativa → [253898] Chamado Finalizado - Recebimento de Uniforme: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [253903] OS reprovada: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [254570] EventoInicial ""
Config: Configuracao={"ServicoIniciador":"RECEBIMENTOUNIFORME"}
TipoSolicitacao: Recebimento de Uniforme
**ScriptFormCarregado**
```python
# Script para esconder os campos de informações do favorecido
# Só ativa quando um favorecido é escolhido

campos = ["TE_CARGO", "TE_FUNCAO", "TE_MATRICULA", "TE_UOR", "TAMANHO"]
for i in campos:
        Formulario[i].Visivel = False

Formulario['LABEL10'].Valor = '<p style="color: yellow; font-weight: 800; background-color: blue; border-radius: 22px; padding: 4% 0; text-align: center; font-weight: 600; font-size: 20px;"> RECEBIMENTO DE UNIFORMES - GERED </p><br><br>'
        
Formulario['LABEL109'].Valor = '<br><br><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><p><a href="https://bbts.docnix.com.br/bbts/corporate/index.html#/login?login=&senha=&empresa=1&state=permiLinkDocumento&id=34659591" target="_blank" style="text-decoration: none; color: blue; font-size: 20px;"><i class="fa fa-file-pdf-o" style="font-size:24px"></i> NI 1347 - Padronização, Requisição e Distribuição de Uniformes</a></p>'
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados Cadastrais
  - TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO] — Coluna=2
  - LABEL1 "<hr style="height: 4px; color: black; border-color: black; background-color: black;"><br>" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - UNIFORMES_EPI "Uniformes" [TextBox String → CPE_PESSOAS.UNIFORMES_EPI] obrigatório
**UNIFORMES_EPI.ScriptModificado**
```python
item = FormularioRegistro["ITEM"].Valor
quantidade = FormularioRegistro["QUANTIDADE"].Valor
grid = OrdemServico.GetCustom("UNIFORMES_EPI")
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
    - coluna CODIGO
    - coluna TAMANHO obrigatório
    - coluna DESCRICAO obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna ITEM obrigatório
  - TAMANHO "Tamanho do uniforme" [Memo String → CPE_CSC.TAMANHO] obrigatório
  - LABEL109 "LABEL109" [Label String(1000) → CPE_CONTRATOS.LABEL109]
  - LABEL10 "LABEL10" [Label String(700) → CPE_PDCI2019.LABEL10] obrigatório
  - FAVORECIDO_TODOS "Nome do Empregado beneficiado" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
**FAVORECIDO_TODOS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["TE_MATRICULA"].Visivel = True
Formulario["TE_CARGO"].Visivel = True
Formulario["TE_FUNCAO"].Visivel = True
Formulario["TE_UOR"].Visivel = True

Formulario["TE_MATRICULA"].Habilitado = False
Formulario["TE_CARGO"].Habilitado = False
Formulario["TE_FUNCAO"].Habilitado = False
Formulario["TE_UOR"].Habilitado = False

Formulario["TE_MATRICULA"].Valor = None
Formulario["TE_CARGO"].Valor = None
Formulario["TE_FUNCAO"].Valor = None
Formulario["TE_UOR"].Valor = None

matricula = ""
cargo = ""
funcao = ""
uor = ""


if Formulario["FAVORECIDO_TODOS"].Valor != "" or Formulario["FAVORECIDO_TODOS"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_TODOS"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["TE_UOR"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )

    for linha in lista.Rows:
        cargo = linha["CARGO"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()
        uor = linha["DESCRICAO"].ToString()

    Formulario["TE_CARGO"].Valor = cargo.ToString()
    Formulario["TE_FUNCAO"].Valor = funcao.ToString()
    #Formulario["DESC_COLABORADOR"].Valor = desc_colaborador.ToString()
    Formulario["TE_MATRICULA"].Valor = matricula.ToString()
    Formulario["TE_UOR"].Valor = uor.ToString()
```
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório — Coluna=2
  - TE_MATRICULA "Matrícula do(a) Empregado(a) beneficiado" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório — Coluna=3
  - TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO] obrigatório

### [253897] EventoFinal ""
Responsável: Cliente (papel 18)
- Relatorios:
  - FormatoExportacao=PDF

### [253898] EventoIntermediarioMensagem "Chamado Finalizado - Recebimento de Uniforme"
Destinatário: Cliente e Favorecido (papel 398)
Config: ListaDestinatarios=dires@bbts.com.br
ModeloComunicado: Chamado Finalizado
Corpo do comunicado: Prezado(a), OrdemServico.Customizado.FAVORECIDO_COBRA 
Informamos que a Ordem de Serviço nº OrdemServico foi concluída com sucesso!
Atenciosamente,
Central de Serviços

### [253899] EventoIntermediarioMensagem "Aviso recebimento de Uniforme"
Destinatário: Gerente Favorecido Todos (papel 237)
ModeloComunicado: Chamado Finalizado - Recebimento de EPI
Corpo do comunicado: Prezado(a) Gestor(a),
Informamos que o(a) empregado(a) OrdemServico.Customizado.FAVORECIDO_COBRA recebeu os equipamentos de proteção individual descritos no documento em anexo e confirmou o recebimento através da ordem de serviço número OrdemServico.Numero .
Atenciosamente,
Central de Serviços

### [253900] FimCancelamento ""

### [253901] Tarefa "Solicitar aprovação do cliente"
Responsável: Cliente (papel 18)
Config: Codigo=APROVAR
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovar Recebimento de Uniformes; ReenvioEmailAprovacao=24
  - (aprovação) OBS1 " Declaração" [Memo String(2000) → CPE_CONTRATOS.OBS1]
  - (aprovação) TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO] — PermiteModificarAprovado=true
  - (aprovação) FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] — PermiteModificarAprovado=true
  - (aprovação) TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO] — PermiteModificarAprovado=true
  - (aprovação) UNIFORMES_EPI "Uniformes" [TextBox String → CPE_PESSOAS.UNIFORMES_EPI] — PermiteModificarAprovado=true
  - (aprovação) TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] — PermiteModificarAprovado=true
  - aprovador: Cliente (Unico)
  - relatório: FormatoExportacao=PDF; RotuloLink=FQ1333-002: FICHA DE CONTROLE E ENTREGA DE EPI
- Relatorios:
  - FormatoExportacao=PDF

### [253903] EventoIntermediarioMensagem "OS reprovada"
Destinatário: Cliente e Favorecido (papel 398)
ModeloComunicado: Chamado cancelado
Corpo do comunicado: Prezado(a),
O chamado OrdemServico.Numero - OrdemServico.Assunto foi cancelado. Verifique o motivo abaixo:
Motivo: Complemento2 
Para mais informações Link.Consulta 
Atenciosamente,
Central de Serviços

## Papéis usados
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 398: Cliente e Favorecido
Tipo=Composto
- composto por: Cliente (PessoaOrdemServico)
- composto por: Favorecido (PessoaOrdemServico)
### papel 237: Gerente Favorecido Todos
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico["FAVORECIDO_TODOS"]:
    favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_TODOS"]))
    gestor = favorecidoBBTec.ObtemChefia(False)
    if favorecidoBBTec == gestor:
        gestor = gestor.Orgao.OrgaoPai.Gestor
    Atores.Adiciona(gestor, "Gerente do Favorecido")
```

## Campos customizados usados (definição global)

### TE_FUNCAO — Função
TextBox String → CPE_CSC.TE_FUNCAO

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### UNIFORMES_EPI — Uniformes
TextBox String → CPE_PESSOAS.UNIFORMES_EPI
Descrição: UNIFORMES_EPI

### TAMANHO — Tamanho
Memo String → CPE_CSC.TAMANHO

### LABEL109 — LABEL109
Label String(1000) → CPE_CONTRATOS.LABEL109

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

### OBS1 — Observação1
Memo String(2000) → CPE_CONTRATOS.OBS1
Descrição: Informe

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
