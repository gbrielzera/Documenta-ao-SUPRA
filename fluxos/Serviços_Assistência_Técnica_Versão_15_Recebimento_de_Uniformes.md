# Fluxo: Recebimento de Uniformes (RECUNIFORME) — versão 15
Caminho: Fluxos > Serviços Assistência Técnica Versão 15 Recebimento de Uniformes
XML: `XMLs para teste/Serviços_Assistência_Técnica_Versão_15_Recebimento_de_Uniformes.xml` | Supravizio 19.1.1 | SubProcessoId 21646 | DesenhoProcessoId 2993 | ProcessoId 31
Órgão dono: 2000004019 - DIVISAO DE APOIO A REDE DE SERVICOS | Responsável: JOSE AFRANIO ARAUJO BRANDAO
Classe do subprocesso: DescricaoCliente=Recebimento de Uniformes; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Recebimento de Uniforme (RECEBIMENTOUNIFORME)

## Grafo do fluxo
- [343992] EventoIntermediarioMensagem "OS reprovada" → [343970] 
- [343993] EventoIntermediarioTimer "Aviso para aprovação" → [343996] 
- [343996] EventoIntermediarioMensagem "" → [343997] 
- [343997] EventoIntermediarioMensagem "" → [343971] Solicitar aprovação do Funcionário
- [343969] EventoIntermediarioMensagem "Chamado Finalizado - Recebimento de Uniforme" → [343976] Aviso recebimento de Uniforme
- [343970] FimCancelamento "" → (fim)
- [343972] EventoIntermediarioMensagem "OS reprovada" → [343992] OS reprovada
- [343971] Tarefa "Solicitar aprovação do Funcionário" {Cliente} → [343993] Aviso para aprovação | [G77801] Aprovado?
- [343973] EventoInicial "" {Cliente} → [343974] Aviso abertura do chamado
- [343974] EventoIntermediarioMensagem "Aviso abertura do chamado" → [343975] Aviso abertura do chamado
- [343976] EventoIntermediarioMensagem "Aviso recebimento de Uniforme" → [343977] 
- [343977] EventoFinal "" {Cliente} → (fim)
- [343978] LinkInicial "Abertura em lote" {Cliente} → [343974] Aviso abertura do chamado
- [343975] EventoIntermediarioMensagem "Aviso abertura do chamado" → [343971] Solicitar aprovação do Funcionário
- [G77801] Gateway "Aprovado?" → «Aprovado» [343969] Chamado Finalizado - Recebimento de Uniforme | «Reprovado» [343972] OS reprovada

## Gateways
### [G77801] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAR")
```
- alternativa → [343969] Chamado Finalizado - Recebimento de Uniforme: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [343972] OS reprovada: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [343992] EventoIntermediarioMensagem "OS reprovada"
Destinatário: Gerente de Centro do favorecido (papel 1349)
ModeloComunicado: Chamado cancelado
Corpo do comunicado: Prezado(a),
O chamado OrdemServico.Numero - OrdemServico.Assunto foi cancelado. Verifique o motivo abaixo:
Motivo: Complemento2 
Para mais informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [343993] EventoIntermediarioTimer "Aviso para aprovação"
Config: TempoIntervalo=1440

### [343996] EventoIntermediarioMensagem ""
Destinatário: Favorecido Cobra e Gerente (papel 1281)
ModeloComunicado: Pendência de Aprovação - DIRES
Corpo do comunicado: Prezados(as),
O chamado interno OrdemServico.Numero - OrdemServico.Assunto.
Comunicamos que a atividade OrdemServico.Atividade está pendente de aprovação.
 OrdemServico.Customizado.EQUIP_EPI

### [343997] EventoIntermediarioMensagem ""
Destinatário: Gerente de Centro do favorecido (papel 1349)
ModeloComunicado: Pendência de Aprovação - DIRES
Corpo do comunicado: Prezados(as),
O chamado interno OrdemServico.Numero - OrdemServico.Assunto.
Comunicamos que a atividade OrdemServico.Atividade está pendente de aprovação.
 OrdemServico.Customizado.EQUIP_EPI

### [343969] EventoIntermediarioMensagem "Chamado Finalizado - Recebimento de Uniforme"
Destinatário: Favorecido Cobra e Gerente (papel 1281)
Config: ListaDestinatarios=dires@bbts.com.br
ModeloComunicado: Chamado Finalizado
Corpo do comunicado: Prezado(a), OrdemServico.Customizado.FAVORECIDO_COBRA 
Informamos que a Ordem de Serviço nº OrdemServico foi concluída com sucesso!
Atenciosamente,
Central de Serviços

### [343970] FimCancelamento ""

### [343972] EventoIntermediarioMensagem "OS reprovada"
Destinatário: Favorecido Cobra e Gerente (papel 1281)
ModeloComunicado: Chamado cancelado
Corpo do comunicado: Prezado(a),
O chamado OrdemServico.Numero - OrdemServico.Assunto foi cancelado. Verifique o motivo abaixo:
Motivo: Complemento2 
Para mais informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [343971] Tarefa "Solicitar aprovação do Funcionário"
Responsável: Cliente (papel 18)
Config: Codigo=APROVAR
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if OrdemServico.Servico.Sigla == 'RECEBIMENTOUNIFORMELOTE':
    import clr
    import System
    clr.AddReference('Supravizio.Custom')

    from System import Convert, DBNull
    from Venki.Supravizio.Recurso.Custom import Pessoa

    grid = OrdemServico.GetCustom("UNIFORMES_EPI")

    matricula = ""

    for i in grid.Rows:
        matricula = str(i["MATRICULA"]).strip()
        if matricula != "":
            break

    if matricula != "":

        idPessoa = DB.ExecuteScalar("Select P.ID_PESSOA From PESSOA P Inner Join CP_PESSOA CP On P.ID_PESSOA = CP.ID_PESSOA Where CP.MATRICULA = '" + matricula + "'")

        if idPessoa != None and idPessoa != DBNull.Value:

            idPessoa = Convert.ToInt32(idPessoa)

            Formulario["FAVORECIDO_COBRA"].Valor = idPessoa
            Formulario["FAVORECIDO_COBRA"].Habilitado = False
            Formulario["TE_MATRICULA"].Valor = matricula
            Formulario["TE_MATRICULA"].Habilitado = False

    else:
        Formulario.ExibeMensagem("Matrícula não encontrada na grid UNIFORMES_EPI.")
else:
    Formulario['UNIFORMES_EPI'].Visivel = True
    Formulario["FAVORECIDO_COBRA"].Habilitado = False
```
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovar Recebimento de Uniformes; ReenvioEmailAprovacao=24
  - (aprovação) FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] — PermiteModificarAprovado=true
  - (aprovação) TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] — PermiteModificarAprovado=true
  - (aprovação) TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO] — PermiteModificarAprovado=true
  - (aprovação) TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO] — PermiteModificarAprovado=true
  - (aprovação) OBS1 " Declaração" [Memo String(2000) → CPE_CONTRATOS.OBS1]
  - (aprovação) UNIFORMES_EPI "Uniforme" [DataGrid RecordList → Z_00143_UNIFORMES_EPI.UNIFORMES_EPI] — PermiteModificarAprovado=true
  - aprovador: Favorecido Cobra (Unico)
  - relatório: FormatoExportacao=PDF; RotuloLink=FQ1333-002: FICHA DE CONTROLE E ENTREGA DE EPI
- Operação PR0001 Preencher Campos
  - UNIFORMES_EPI "Uniformes Recebidos" [DataGrid RecordList → Z_00143_UNIFORMES_EPI.UNIFORMES_EPI]
    - coluna QUANTIDADE obrigatório
    - coluna DESCRICAO obrigatório
    - coluna MATRICULA
    - coluna TAMANHO obrigatório
    - coluna CODIGO obrigatório
    - coluna ITEM obrigatório
  - FAVORECIDO_COBRA "Nome do colaborador que recebeu os uniformes" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
- Relatorios:
  - FormatoExportacao=PDF

### [343973] EventoInicial ""
Responsável: Cliente (papel 18)
Config: Configuracao={"ServicoIniciador":"RECEBIMENTOUNIFORME"}
TipoSolicitacao: Recebimento de Uniforme
**ScriptFormCarregado**
```python
# Script para esconder os campos de informações do favorecido
# Só ativa quando um favorecido é escolhido

campos = ['TE_CARGO', 'TE_FUNCAO', 'TE_MATRICULA', 'TE_UOR', 'TAMANHO']
for i in campos:
        Formulario[i].Visivel = False

Formulario['LABEL10'].Valor = '<p style="color: yellow; font-weight: 800; background-color: blue; border-radius: 22px; padding: 4% 0; text-align: center; font-weight: 600; font-size: 20px;"> RECEBIMENTO DE UNIFORMES - GERED </p><br><br>'
        
Formulario['LABEL109'].Valor = '<br><br><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><p><a href="https://bbts.docnix.com.br/bbts/corporate/index.html#/login?login=&senha=&empresa=1&state=permiLinkDocumento&id=34659591" target="_blank" style="text-decoration: none; color: blue; font-size: 20px;"><i class="fa fa-file-pdf-o" style="font-size:24px"></i> NI 1347 - Padronização, Requisição e Distribuição de Uniformes</a><br>Atenção, a matrícula só será preenchida na GRID se for uma abertura em lote, caso contrário deixe em branco.</p>'
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados Cadastrais
  - LABEL10 "LABEL10" [Label String(700) → CPE_PDCI2019.LABEL10] obrigatório
  - FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
**FAVORECIDO_COBRA.ScriptModificado**
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


if Formulario["FAVORECIDO_COBRA"].Valor != "" or Formulario["FAVORECIDO_COBRA"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_COBRA"].Valor)
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
  - TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO] — Coluna=2
  - LABEL1 "<hr style="height: 4px; color: black; border-color: black; background-color: black;"><br>" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - UNIFORMES_EPI "Uniforme" [DataGrid RecordList → Z_00143_UNIFORMES_EPI.UNIFORMES_EPI] obrigatório
    - coluna MATRICULA
    - coluna TAMANHO obrigatório
    - coluna CODIGO
    - coluna DESCRICAO obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna ITEM obrigatório
**UNIFORMES_EPI.ITEM.ScriptModificado**
```python
def texto(valor):
    try:
        if valor is None:
            return ""
        return str(valor).strip()
    except:
        return ""


def set_valor(campo, valor):
    try:
        valor_atual = texto(FormularioRegistro[campo].Valor)
        valor_novo = texto(valor)

        if valor_atual != valor_novo:
            FormularioRegistro[campo].Valor = valor_novo
    except:
        pass


def get_quantidade():
    try:
        valor = FormularioRegistro["QUANTIDADE"].Valor

        if valor is None:
            return 0

        texto_qtd = texto(valor)

        if texto_qtd == "":
            return 0

        texto_qtd = texto_qtd.replace(",", ".")

        return int(float(texto_qtd))
    except:
        return 0


def extrair_tamanho(item):
    try:
        if item.find(" | ") >= 0:
            return item.split(" | ")[1].strip()
        return ""
    except:
        return ""


def contar_item_na_grid(item):
    total = 0

    try:
        grid = OrdemServico.GetCustom("UNIFORMES_EPI")

        for linha in grid.Rows:
            try:
                item_grid = texto(linha["ITEM"])

                if item_grid == item:
                    total += 1
            except:
                pass
    except:
        pass

    return total


item = texto(FormularioRegistro["ITEM"].Valor)
quantidade = get_quantidade()
tamanho = extrair_tamanho(item)


if item != "":

    item_repetido = False

    try:
        if contar_item_na_grid(item) > 1:
            item_repetido = True
    except:
        item_repetido = False

    if item_repetido:
        Formulario.ExibeMensagem("Este item já foi solicitado em outra linha. Não é permitido duplicar itens.")
        set_valor("ITEM", "")
        set_valor("DESCRICAO", "")
        set_valor("CODIGO", "")
        set_valor("TAMANHO", "")

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

            descricao = cfg.get("descricao", "")
            codigo = cfg.get("codigo", "")
            limite = cfg.get("limite")

            set_valor("DESCRICAO", descricao)
            set_valor("CODIGO", codigo)

            if tamanho != "":
                set_valor("TAMANHO", tamanho)

            if limite is not None and quantidade > 0:
                if quantidade > limite:
                    Formulario.ExibeMensagem("Número maior que o permitido!")
                    set_valor("QUANTIDADE", "")

        else:
            Formulario.ExibeMensagem("Item não encontrado na tabela de itens. Verifique o nome ou atualize a planilha.")


try:
    if texto(FormularioRegistro["TAMANHO"].Valor) == "Outro":
        Formulario["TAMANHO"].Visivel = True
    else:
        Formulario["TAMANHO"].Visivel = False
except:
    pass
```
  - TAMANHO "Tamanho do uniforme" [Memo String → CPE_CSC.TAMANHO] obrigatório
  - LABEL109 "LABEL109" [Label String(1000) → CPE_CONTRATOS.LABEL109]

### [343974] EventoIntermediarioMensagem "Aviso abertura do chamado"
Destinatário: Favorecido Cobra e Gerente (papel 1281)
ModeloComunicado: Aviso de abertura de chamado - 1
Corpo do comunicado: Prezado(a),
Foi aberta a ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [343976] EventoIntermediarioMensagem "Aviso recebimento de Uniforme"
Destinatário: Gerente de Centro do favorecido (papel 1349)
ModeloComunicado: Chamado Finalizado - Recebimento de EPI
Corpo do comunicado: Prezado(a) Gestor(a),
Informamos que o(a) empregado(a) OrdemServico.Customizado.FAVORECIDO_COBRA recebeu os equipamentos de proteção individual descritos no documento em anexo e confirmou o recebimento através da ordem de serviço número OrdemServico.Numero .
Atenciosamente,
Central de Serviços

### [343977] EventoFinal ""
Responsável: Cliente (papel 18)
- Relatorios:
  - FormatoExportacao=PDF

### [343978] LinkInicial "Abertura em lote"
Responsável: Cliente (papel 18)
Config: TipoMensagem=MensagemProcesso
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#grid = OrdemServico.GetCustom("UNIFORMES_EPI")
#
#matricula = ""
#
#for i in grid.Rows:
#    matricula = str(i["MATRICULA"]).strip()
#    break
#
#idPessoa = DB.ExecuteScalar("Select P.ID_PESSOA From PESSOA P Inner Join CP_PESSOA CP On P.ID_PESSOA = CP.ID_PESSOA Where CP.MATRICULA = '" + matricula + "'")
#
#idPessoa = Convert.ToInt32(idPessoa)
#
#OrdemServico.AdicionaComentario(matricula.ToString(), False)
#
#Formulario["FAVORECIDO_COBRA"].Valor = idPessoa
#Formulario["FAVORECIDO_COBRA"].Habilitado = False


import clr
import System
clr.AddReference('Supravizio.Custom')

from System import Convert, DBNull
from Venki.Supravizio.Recurso.Custom import Pessoa

grid = OrdemServico.GetCustom("UNIFORMES_EPI_LOTE")

matricula = ""

for i in grid.Rows:
    matricula = str(i["MATRICULA"]).strip()
    if matricula != "":
        break

if matricula != "":

    idPessoa = DB.ExecuteScalar("Select P.ID_PESSOA From PESSOA P Inner Join CP_PESSOA CP On P.ID_PESSOA = CP.ID_PESSOA Where CP.MATRICULA = '" + matricula + "'")

    if idPessoa != None and idPessoa != DBNull.Value:

        idPessoa = Convert.ToInt32(idPessoa)

        Formulario["FAVORECIDO_COBRA"].Valor = idPessoa
        Formulario["FAVORECIDO_COBRA"].Habilitado = False

else:
    Formulario.ExibeMensagem("Matrícula não encontrada na grid UNIFORMES_EPI.")
```
- Associação de subprocesso: AssociacaoId=1659; FraseAssociacao=Recebimento de Uniforme (Em Lote) -> Recebimento de Uniformes; Nome=UNIFORMELOTE

### [343975] EventoIntermediarioMensagem "Aviso abertura do chamado"
Destinatário: Gerente de Centro do favorecido (papel 1349)
ModeloComunicado: Aviso de abertura de chamado - 1
Corpo do comunicado: Prezado(a),
Foi aberta a ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

## Papéis usados
### papel 1349: Gerente de Centro do favorecido
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
subordinado = OrdemServico.GetCustom("FAVORECIDO_COBRA")
 
gestor = DB.ExecuteDataTable("Select PESSOA.NOME As NomePessoa, CP_PESSOA.CARGO_FUNCIONAL As CargoPessoa, PESSOA1.NOME As NomeGestor, CP_PESSOA1.CARGO_FUNCIONAL As CargoGestor, PESSOA2.NOME As NomeGestorDoGestor, CP_PESSOA2.CARGO_FUNCIONAL As CargoGestorDoGestor, SUBORDINADO.NOME As NomeSubordinado, CP_SUBORDINADO.CARGO_FUNCIONAL As CargoSubordinado, PESSOA1.ID_PESSOA From PESSOA Left Join ORGAO On ORGAO.ID_ORGAO = PESSOA.ID_ORGAO Left Join CP_PESSOA On CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA Left Join PESSOA PESSOA1 On PESSOA1.ID_PESSOA = ORGAO.ID_GESTOR Left Join CP_PESSOA CP_PESSOA1 On CP_PESSOA1.ID_PESSOA = PESSOA1.ID_PESSOA Left Join ORGAO ORGAO1 On ORGAO1.ID_ORGAO = PESSOA1.ID_ORGAO Left Join PESSOA PESSOA2 On PESSOA2.ID_PESSOA = ORGAO1.ID_GESTOR Left Join CP_PESSOA CP_PESSOA2 On CP_PESSOA2.ID_PESSOA = PESSOA2.ID_PESSOA Left Join ORGAO ORGAO2 On ORGAO2.ID_GESTOR = PESSOA.ID_PESSOA Left Join PESSOA SUBORDINADO On SUBORDINADO.ID_ORGAO = ORGAO2.ID_ORGAO Left Join CP_PESSOA CP_SUBORDINADO On CP_SUBORDINADO.ID_PESSOA = SUBORDINADO.ID_PESSOA Where SUBORDINADO.ID_PESSOA = '"+OrdemServico['FAVORECIDO_COBRA'].ToString()+"'")
 
if gestor.Rows.Count != 0 or gestor.Rows.Count != None:
    for i in gestor.Rows:
        id_gestor = Convert.ToInt32(i['ID_PESSOA'])
    gtor = Pessoa.Carrega(id_gestor)
    Atores.Adiciona(gtor)
```
### papel 1281: Favorecido Cobra e Gerente
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.GetCustom("FAVORECIDO_COBRA"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))

    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")

    
gestorMatricula = str(OrdemServico.GetCustom('MATRICULA'))
 
lista = Utils.ExecuteDataTable("Select PESSOA.ID_PESSOA, CP_PESSOA.MATRICULA, PESSOA.EMAIL, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Where CP_PESSOA.MATRICULA ='" + gestorMatricula + "'")        
 
idAnalista = 0
 
for row in lista.Rows:    
 
    idAnalista = row['ID_PESSOA']
```
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 277: Favorecido Cobra
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.GetCustom("FAVORECIDO_COBRA"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))

    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Campos customizados usados (definição global)

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### TE_CARGO — Cargo
TextBox String → CPE_CSC.TE_CARGO

### TE_FUNCAO — Função
TextBox String → CPE_CSC.TE_FUNCAO

### OBS1 — Observação1
Memo String(2000) → CPE_CONTRATOS.OBS1
Descrição: Informe

### UNIFORMES_EPI — Uniforme
DataGrid RecordList → Z_00143_UNIFORMES_EPI.UNIFORMES_EPI
Colunas do registro:
- MATRICULA "MATRICULA" [TextBox String]
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
- QUANTIDADE "Quantidade" [TextBox Integer]
- DESCRICAO "Descrição" [Memo String]
- TAMANHO "TAMANHO" [TextBox String]
- CODIGO "CODIGO" [TextBox String]

### LABEL10 — LABEL10
Label String(700) → CPE_PDCI2019.LABEL10

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### TAMANHO — Tamanho
Memo String → CPE_CSC.TAMANHO

### LABEL109 — LABEL109
Label String(1000) → CPE_CONTRATOS.LABEL109

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
