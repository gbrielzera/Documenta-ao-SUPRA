# Fluxo: Faturamento de Clientes - Emissão de Notas Fiscais (FATCLIEMISNF) — versão 20
Caminho: Fluxos > Financeiro - Faturamento de Clientes Versão 20 Faturamento de Clientes - Emissão de Notas Fiscais
XML: `XMLs para teste/Financeiro_-_Faturamento_de_Clientes_Versão_20_Faturamento_de_Clientes_-_Emissão_de_Notas_Fiscais.xml` | Supravizio 19.1.1 | SubProcessoId 21971 | DesenhoProcessoId 3024 | ProcessoId 157
Órgão dono: 3000009360 - DIVISAO DE TRIBUTOS | Responsável: JOSE PEREIRA DE SA JUNIOR
Classe do subprocesso: Objetivo=Faturamento de Clientes - Emissão de Notas Fiscais; DescricaoCliente=Faturamento de Clientes - Emissão de Notas Fiscais; CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Emissão de Nota Fiscal - Clientes (EMISSAONFCLIENTE)

## Grafo do fluxo
- [348711] EventoIntermediarioTimer "5 dias " → [348704] Faturamento - Não Faturado
- [348692] Tarefa "Inserir informações EBS/OKS (1S)" {Fila CSC - Faturamento de Clientes} → [348694] Criação do Rascunho
- [348693] Tarefa "Criar espelho da NF no ERP" {Fila CSC - Faturamento de Clientes} → [348702] Comunicado de Finalização de criação de espelho da
- [348694] Tarefa "Criação do Rascunho" {Fila CSC - Faturamento de Clientes} → [348696] Validar inserção e revisão das informações EBS/OKS
- [348695] Tarefa "Ajustar as Informações" {Cliente} → [348711] 5 dias  | [348701] Comunicado de Abertura - Faturamento
- [348696] Tarefa "Validar inserção e revisão das informações EBS/OKS (PAR)" {Fila CSC - Faturamento de Clientes} → [G78744] Primeiro Faturamento?

- [348697] SubProcesso "" {Responsável atual} → [348708] Aguardar Retorno do Parecer DITRI
- [348698] Tarefa "Verificar e Validar Rascunho" {Cliente} → [G78746] Aprovou?
- [348699] EventoInicial "" → [348701] Comunicado de Abertura - Faturamento
- [348700] EventoIntermediarioMensagem "Comunicado para ajustes" → [348695] Ajustar as Informações
- [348701] EventoIntermediarioMensagem "Comunicado de Abertura - Faturamento" → [348707] Verificação solicitação
- [348702] EventoIntermediarioMensagem "Comunicado de Finalização de criação de espelho da NF no ERP" → [348710] Gerar Nota Fiscal na Prefeitura
- [348703] Tarefa "Informar os ajustes necessários" {Responsável atual} → [348700] Comunicado para ajustes
- [348704] EventoIntermediarioMensagem "Faturamento - Não Faturado" → [348705] 
- [348705] FimCancelamento "" → (fim)
- [348706] EventoIntermediarioMensagem "Comunicado Aprovação" → [348693] Criar espelho da NF no ERP
- [348707] Tarefa "Verificação solicitação" {Fila CSC - Faturamento de Clientes} → [G78745] Dados ok?
- [348708] Tarefa "Aguardar Retorno do Parecer DITRI" {Responsável atual} → [348698] Verificar e Validar Rascunho
- [348709] EventoFinal "" {Responsável atual} → (fim)
- [348710] SubProcesso "Gerar Nota Fiscal na Prefeitura" {Fila CSC - Faturamento de Clientes} → [348709] 
- [G78744] Gateway "Primeiro Faturamento?
" → «Não» [348698] Verificar e Validar Rascunho | «Sim» [348697] 
- [G78745] Gateway "Dados ok?" → «Sim» [348692] Inserir informações EBS/OKS (1S) | «Não» [348703] Informar os ajustes necessários
- [G78746] Gateway "Aprovou?" → «Aprovado» [348706] Comunicado Aprovação | «Reprovado» [348695] Ajustar as Informações

## Gateways
### [G78744] Primeiro Faturamento?
 (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.GetCustom("SIM_NAO2")
```
- alternativa → [348698] Verificar e Validar Rascunho: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
'Não'
```
- alternativa → [348697] : OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
'Sim'
```
### [G78745] Dados ok? (EventBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAR")
```
- alternativa → [348692] Inserir informações EBS/OKS (1S): OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
Sim
```
- alternativa → [348703] Informar os ajustes necessários: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
Não
```
### [G78746] Aprovou? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("VALIDAR_RASCUNHO")
```
- alternativa → [348706] Comunicado Aprovação: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [348695] Ajustar as Informações: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [348711] EventoIntermediarioTimer "5 dias "
Config: Codigo=5DNIAS; TempoIntervalo=7200

### [348692] Tarefa "Inserir informações EBS/OKS (1S)"
Referência: Orientações para a tarefa:
Como primeiro solucionador a assumir essa tarefa, você deve inserir as informações contidas e verificadas na Ordem de Serviço no Módulo OKS conforme orientações do POP217-001 - Gerar controle de notas faturadas no ERP, acompanhar as Notas fiscais de Serviços enviadas para o BB. 
Após inserção, a OS retornará para a fila para que outro solucionador do segmento Cesec-FIN realize a revisão dos dados inseridos.
Responsável: Fila CSC - Faturamento de Clientes (papel 733)
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Preencha o campo abaixo comentando ou adicionando comentários na tarefa:
  - Justificativa (nativo) "  " obrigatório

### [348693] Tarefa "Criar espelho da NF no ERP"
Referência: Orientações para a tarefa:
Validada a revisão e inserção das informações no módulo OKS, o solucionador deverá assumir a resposnabilidade da OS e gerar o espelho da Nota Fiscal em formato PDF e anexar na OS para as próximas tarefas conforme orientações do POP217-001 - Gerar controle de notas faturadas no ERP, acompanhar as Notas fiscais de Serviços enviadas para o BB.
Responsável: Fila CSC - Faturamento de Clientes (papel 733)
Config: Codigo=CRIARESPELHONFERP
- Operação PR0004 Associar Itens Configuração
  - anexo "Escopo NFSe" classes: Espelho NFSe — RequeridoInicial=true

### [348694] Tarefa "Criação do Rascunho"
Responsável: Fila CSC - Faturamento de Clientes (papel 733)
Config: Codigo=CRIARRASCUNHONF
- Operação PR0004 Associar Itens Configuração
  - anexo "Rascunho NFs" classes: Rascunho da Nota Fiscal — RequeridoInicial=true

### [348695] Tarefa "Ajustar as Informações"
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
- Operação PR0004 Associar Itens Configuração
  - anexo ""De acordo" por e-mail nos casos de penalidade contratual com multa, glosa ou rebate conforme NI006." classes: De Acordo — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Aceite do Cliente" classes: Aceite do Cliente — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Demais Arquivos" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Rateio das Localidades" classes: Rateio Localidades — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos
  - LABEL_GRANDE "Label Grande" [Label String(2000) → CPE_MOVIMENTACAO_PESSOA.LABEL_GRANDE] obrigatório
  - DGCO_BB "N° do Contrato do Banco (Apenas números, sem caracteres)" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB]
  - OKS_FAT "Contrato OKS" [TextBox String → CPE_FINANCEIRO.OKS_FAT] obrigatório — Coluna=2
  - NUM_DOCU "Quantidade de Notas Fiscais Solicitadas" [TextBox String → CP_ORDEM_SERVICO.NUM_DOCU] obrigatório
  - GRID_NF "Detalhamento da NF" [DataGrid RecordList → Z_00143_GRID_NF.GRID_NF] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna DESCRICAO obrigatório
    - coluna VALOR obrigatório
    - coluna LOCALIDADE obrigatório
  - GERENCIAS_FATURAMENTO "Gerências Faturamento" [DropDownList String → CPE_CONTRATOS02.GERENCIAS_FATURAMENTO] obrigatório
**GERENCIAS_FATURAMENTO.ScriptModificado**
```python
from Venki.Supravizio.Configuracao.Custom import Software
Formulario['COMBOBOX'].Visivel = True

gerencias_faturamento_dict = {
    "Gecob": ["CRBB SSA", "CRBB RJ", "CRBB BSB", "CRBB BB Américas", "Cobrança Extrajudicial", "Kit Pré-Ajuizamento", "GED/UTD", "Microfilmagem", "Outro"],
    "Gecor": ["BB Consórcios", "BB Correspondente Bancário", "Outro"],
    "Gelop/Gered": ["TAA", "Demais Bens", "Rede Man", "PGDM", "DOSI", "DOSA", "DOCA", "Monitoração", "PSIM", "TEYA - Outsourcing de Telefonia","Nobreak Norte", "Nobreak Sul", "Outro"],
    "Gepin": ["Hiveplace", "Outro"],
    "Gesec": ["Licenter", "SOC BB", "SOC BB Américas", "SOC CASSI","Outro"],
    "Geape": ["Fábrica de Software - Credenciamento", "Fábrica de Software - BB Tribunais", "FSW - Autoban", "Outro"],
    "Gesit": ["Intevia - E-mail MKT", "Intevia - SMS", "Aprovve", "Outro"],
    "Outra": None
    }
    
Formulario["VALOR_AUTORIZADO"].Visivel = True if Formulario['GERENCIAS_FATURAMENTO'].Valor == "Gecob" else False

    
valor = Formulario["GERENCIAS_FATURAMENTO"].Valor
itens = gerencias_faturamento_dict.get(valor)

if itens is None:
    Formulario["COMBOBOX"].Visivel = False
else:
    Formulario["COMBOBOX"].Itens = itens
```
  - COMBOBOX "Negócio/Produto" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório — Coluna=2
  - VLFAT_FAT "Faturamento Total - R$" [TextBox Decimal → CPE_FINANCEIRO.VLFAT_FAT] obrigatório
**VLFAT_FAT.ScriptModificado**
```python
if Formulario["VLREBATE_FAT"].Valor == None or Formulario["VLFAT_FAT"].Valor == None:
    Formulario["VALOR FAT LIQUIDO"].Valor = 0
else:
    Formulario["VALOR FAT LIQUIDO"].Valor = Formulario["VLFAT_FAT"].Valor - Formulario["VLREBATE_FAT"].Valor
```
  - VALOR_AUTORIZADO "Bônus" [TextBox Decimal → CPE_MOVIMENTACAO_PESSOA.VALOR_AUTORIZADO] obrigatório — Coluna=2
  - VLREBATE_FAT "Rebate, Glosa ou Multa Total - R$" [TextBox Decimal → CPE_FINANCEIRO.VLREBATE_FAT] obrigatório
**VLREBATE_FAT.ScriptModificado**
```python
if Formulario["GERENCIAS_FATURAMENTO"].Valor == 'Gecob':
    Formulario["VALOR FAT LIQUIDO"].Valor = Formulario["VLFAT_FAT"].Valor + Formulario["VALOR_AUTORIZADO"].Valor - Formulario["VLREBATE_FAT"].Valor
else:
    Formulario["VALOR FAT LIQUIDO"].Valor = Formulario["VLFAT_FAT"].Valor - Formulario["VLREBATE_FAT"].Valor
```
  - VALOR FAT LIQUIDO "Total Líquido a Faturar (FT - RebGloMul) - R$" [TextBox String → CPE_PESSOAS.VALOR_FAT_LIQUIDO] obrigatório — Coluna=2
  - SIM_NAO3 "É repactuação?" [DropDownList String → CPE_CSC.SIM_NAO3] obrigatório
**SIM_NAO3.ScriptModificado**
```python
if Formulario["SIM_NAO3"].Valor == 'Sim':
    Formulario["MESES_ANO"].Visivel = False
    
if Formulario["SIM_NAO3"].Valor != 'Sim':
    Formulario["MESES_ANO"].Visivel = True
```
  - MESES_ANO "Competência (mês a que se refere o faturamento)" [DropDownList String → CPE_CONTRATOS02.MESES_ANO] obrigatório — Coluna=2
  - DTVENC_FAT "Data de Vencimento" [DatePicker DateTime → CPE_FINANCEIRO.DTVENC_FAT] obrigatório
  - DESCRICAO_DETALHADA "Corpo da Nota (Descrição)" [Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório
  - DESTNFSE_FAT "E-mails internos a serem notificados sobre cada etapa do chamado (Separados por ponto e vírgula) (Será enviado e-mail automático após as atividades: devolução para ajustes; Criar espelho da NF no ERP; Gerar Nota Fiscal na Prefeitura; Finalização do chamado)" [TextBox String → CPE_FINANCEIRO.DESTNFSE_FAT]
  - DEC_AUX_HOM "Declaração de Ciência: Estou ciente que no caso de faturamento com penalidades contratuais (rebate, glosa ou multa) deverá ser anexado o documento com de acordo do alçada vigente conforme NI006." [CheckBox Boolean → CPE_PESSOAS.DEC_AUX_HOM] obrigatório
  - CHECKBOX15 "Confirmo que anexei o "De acordo" do cliente" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX15] obrigatório

### [348696] Tarefa "Validar inserção e revisão das informações EBS/OKS (PAR)"
Referência: Considerando as ações dos solucionadores nas tarefas anteriores (inserção e revisão), o Técnico do Cesec-FIN deverá validar as tarefas correspondenjtes ao POP217-001 - xxx xxx x xx xxxx. 
 realizadas pelos solucionadores (1S e 2S) identificando eventuais ajustes a serem realizados.
Responsável: Fila CSC - Faturamento de Clientes (papel 733)
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovar inserção e revisão; CopiarAnexados=true; MinimoAprovadores=1; ReprovarImediato=true; ReenvioEmailAprovacao=1
  - (aprovação) DTVENC_FAT "Data de Vencimento" [DatePicker DateTime → CPE_FINANCEIRO.DTVENC_FAT]
  - (aprovação) SIM_NAO "É repactuação?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO]
  - (aprovação) DESTNFSE_FAT "E-mails internos a serem notificados sobre cada etapa do chamado (Separados por ponto e vírgula) (Será enviado e-mail automático após as atividades: devolução para ajustes; Criar espelho da NF no ERP; Gerar Nota Fiscal na Prefeitura; Finalização do chamado)" [TextBox String → CPE_FINANCEIRO.DESTNFSE_FAT]
  - (aprovação) VLREBATE_FAT "Rebate, Glosa ou Multa Total - R$" [TextBox Decimal → CPE_FINANCEIRO.VLREBATE_FAT]
  - (aprovação) DGCO_BB "N° do Contrato do Banco" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB]
  - (aprovação) DEC_AUX_HOM "Declaração de Ciência: Estou ciente que no caso de faturamento com penalidades contratuais (rebate, glosa ou multa) deverá ser anexado o documento com de acordo do alçada vigente conforme NI006." [CheckBox Boolean → CPE_PESSOAS.DEC_AUX_HOM]
  - (aprovação) VLFAT_FAT "Faturamento Total - R$" [TextBox Decimal → CPE_FINANCEIRO.VLFAT_FAT]
  - (aprovação) VALOR FAT LIQUIDO "Total Líquido a Faturar (FT - RebGloMul) - R$" [TextBox String → CPE_PESSOAS.VALOR_FAT_LIQUIDO]
  - (aprovação) OKS_FAT "Contrato OKS" [TextBox String → CPE_FINANCEIRO.OKS_FAT]
  - aprovador: Cesec Faturamento Gyn (Unico)
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Preencha o campo abaixo comentando ou adicionando comentários na tarefa:
  - Justificativa (nativo) "  " obrigatório

### [348697] SubProcesso ""
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1420; ChamadaAssincrona=true
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "PFANLSESPLHNFFTRDA")
```
  - CustomPropertyId=580; CustomProperty=DESCRICAO_OBRIG
  - CustomPropertyId=1002; CustomProperty=SIM_NAO
  - CustomPropertyId=1977; CustomProperty=SIM_NAO1
  - CustomPropertyId=1960; CustomProperty=SIM_NAO2
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=1655; ClasseConfiguracao=Arquivo
- RetornoItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2178; ClasseConfiguracao=Parecer Tributário
- Associação: Ativo=true; FraseAssociacao=Faturamento de Clientes - Emissão de Notas Fiscais -> Consulta Fisco - Tributária; FraseInversaAssociacao=Consulta Fisco - Tributária -> Faturamento de Clientes - Emissão de Notas Fiscais; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=FATUCLIENTEFISCOTRIBUT; SeparadorSequencial=. | fonte: Faturamento de Clientes - Emissão de Notas Fiscais → alvo: Consulta Fisco - Tributária (Estadual, Municipal ou Federal)

### [348698] Tarefa "Verificar e Validar Rascunho"
Responsável: Cliente (papel 18)
Config: Codigo=VALIDAR_RASCUNHO
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
- Operação PR0002 Aprovar
  - (aprovação) Justificativa (nativo) "  "
  - aprovador: Cliente (Unico)

### [348699] EventoInicial ""
TipoSolicitacao: 15.02. Finanças, Controladoria e Contabilidade - Faturamento de Clientes
**ScriptFim**
```python
linhas = OrdemServico.GetCustom('GRID_NF').Rows.Count
OrdemServico.SetCustom('NUM_DOCU', linhas.ToString())
```
**ScriptValidacao**
```python
if OrdemServico.GetCustom('SIM_NAO2') == 'Sim' and not OrdemServico.PossuiItem('PARECERNOVOSNEG'):
    Criticas.AdicionaPendencia('Por ser o primeiro faturamento, anexe o parecer de novos negócios!')
#if (not String.IsNullOrEmpty(OrdemServico['VLREBATE_FAT'].ToString()) or OrdemServico['VLREBATE_FAT'] != 0) and not OrdemServico.PossuiItem('DEACORDO'):
#    Criticas.AdicionaPendencia('Por existir Rebate, Glosa, ou Multa, anexe o de acordo!')

valorRebate = OrdemServico['VLREBATE_FAT']

if (not String.IsNullOrEmpty(valorRebate.ToString()) and Decimal.Parse(valorRebate.ToString()) != 0 and not OrdemServico.PossuiItem('DEACORDO')):
    Criticas.AdicionaPendencia('Por existir Rebate, Glosa ou Multa, anexe o de acordo!')

grid = OrdemServico.GetCustom('GRID_NF')

valor = 0
for i in grid.Rows:
    valor += Convert.ToDecimal(i['VALOR'])
    
if valor != Convert.ToDecimal(OrdemServico.GetCustom('VALOR FAT LIQUIDO')):
    Criticas.AdicionaPendencia('''A soma dos valores das notas informadas ({0})
    é diferente do total líquido a faturar ({1})
    '''.format(valor.ToString(), OrdemServico.GetCustom('VALOR FAT LIQUIDO').ToString()))


if (OrdemServico.GetCustom("SIM_NAO2")  == 'Sim') :
    if (OrdemServico.PossuiItem("ANEXO") == False) :
        Criticas.AdicionaAviso("O documento deve ser anexado obrigatoriamente.")
```
**ScriptFormCarregado**
```python
Formulario['LABEL_GRANDE'].Valor = '<div style="display: flex; justify-content: center; align-items: center;"><div style="display: flex; align-items: center; width: 100%; background: linear-gradient(90deg, blue, rgb(2, 0, 18)); border-radius: 16px; padding: 2%; padding: 4%;"><br><p style="flex: 1; text-align: center; color: yellow; font-weight: 600; font-size: 30px; font-family: Georgia, "Times New Roman", Times, serif; margin: 0;">EMISSÃO DE NOTAS FISCAIS <br></p></div></div><br><br>'

Formulario['LABEL1'].Valor = '<a href="https://bbtecno-my.sharepoint.com/:x:/g/personal/ext-douglas_moura_bbts_com_br/IQARL4ZszaaMS6lzunGbTk3wAQRXD4zZdqv0R34L40lR7rY?download=1"><p>Clique AQUI para baixar o modelo da planilha</p></a>'

Formulario['DESCRICAO_OBRIG2'].Visivel = False
Formulario['SIM_NAO_FAT'].Visivel = False
Formulario['SIM_NAO1'].Visivel = False
Formulario['ANEXO'].Visivel = True
Formulario['COMBOBOX'].Visivel = False
Formulario["VALOR_AUTORIZADO"].Visivel = False
Formulario['VALOR FAT LIQUIDO'].Habilitado = False
Formulario['NUM_DOCU'].Habilitado = False
Formulario['NUM_DOCU'].Visivel = False
```
- Operação PR0004 Associar Itens Configuração: Nome=PLANILHA DO EXCEL
  - anexo "Planilha do Excel" classes: Arquivo 05 — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - LABEL_GRANDE "Label Grande" [Label String(2000) → CPE_MOVIMENTACAO_PESSOA.LABEL_GRANDE] obrigatório
  - DGCO_BB "N° do Contrato do Banco (Apenas números, sem caracteres)" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB]
  - OKS_FAT "Contrato OKS" [TextBox String → CPE_FINANCEIRO.OKS_FAT] obrigatório — Coluna=2
  - NUM_DOCU "Quantidade de Notas Fiscais Solicitadas" [TextBox String → CP_ORDEM_SERVICO.NUM_DOCU] obrigatório
  - LABEL1 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - CHECKBOX1 "Clique AQUI para ler a planilha" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX1]
**CHECKBOX1.ScriptModificado**
```python
from Venki.Services.Dictionary.Custom import Culture
if Controle.Valor == True:

    if OrdemServico.PossuiItem("ARQUIVO05"):

        import clr
        import System

        clr.AddReference("System.Data")

        from System.Data import DataSet
        from System.Data.OleDb import OleDbConnection, OleDbDataAdapter
        from System import String, DBNull, Convert
        from System.Globalization import CultureInfo


        # ============================================================
        # FUNÇÕES AUXILIARES
        # ============================================================

        def Texto(valor):
            try:
                if valor is None:
                    return ""

                if valor == DBNull.Value:
                    return ""

                texto = Convert.ToString(valor)

                if texto is None:
                    return ""

                return texto.Trim()

            except:
                return ""


        def ConverterValor(valor):
            try:
                texto = Texto(valor)

                if texto == "":
                    raise Exception(
                        "VALOR não informado."
                    )

                # Remove espaços.
                texto = texto.Replace(" ", "")

                # Aceita:
                # 1500
                # 1500,50
                # 1500.50
                texto = texto.Replace(",", ".")

                return Convert.ToDecimal(
                    texto,
                    CultureInfo.InvariantCulture
                )

            except Exception as ex:
                raise Exception(
                    "VALOR inválido: '{0}'. {1}".format(
                        Texto(valor),
                        Texto(ex)
                    )
                )


        def GridPossuiRegistro(localidade, valor):
            try:
                grid = OrdemServico.GetCustom(
                    "GRID_NF"
                )

                localidadeProcurada = Texto(
                    localidade
                ).ToUpper()

                valorProcurado = Texto(
                    valor
                )

                for linhaGrid in grid.Rows:
                    try:
                        localidadeGrid = Texto(
                            linhaGrid["LOCALIDADE"]
                        ).ToUpper()

                        valorGrid = Texto(
                            linhaGrid["VALOR"]
                        )

                        if (
                            localidadeGrid == localidadeProcurada and
                            valorGrid == valorProcurado
                        ):
                            return True

                    except:
                        pass

            except:
                pass

            return False


        # ============================================================
        # FUNÇÃO DE IMPORTAÇÃO
        # ============================================================

        def LerExcel():

            repositorio = Utils.ExecuteScalar(
                "select FILES_PATH from SERVICES_PARAM"
            )

            anexo = OrdemServico.ObtemItem(
                "ARQUIVO05"
            )

            caminhoArquivo = (
                Texto(repositorio) +
                "\\" +
                Texto(anexo.Localizacao)
            )


            # ========================================================
            # CONEXÃO COM O EXCEL
            # ========================================================

            stringConexao = String.Format(
                "Provider=Microsoft.ACE.OLEDB.12.0;"
                "Data Source={0};"
                "Extended Properties='Excel 12.0 Xml;"
                "HDR=YES;"
                "IMEX=1;"
                "TypeGuessRows=0;"
                "ImportMixedTypes=Text';",
                caminhoArquivo
            )

            conexao = OleDbConnection(
                stringConexao
            )


            # ========================================================
            # CONTADORES
            # ========================================================

            totalLinhas = 0
            adicionadas = 0
            linhasVazias = 0
            duplicadas = 0
            erros = 0

            detalhes = ""


            try:
                conexao.Open()


                # ====================================================
                # CONSULTA À GUIA DADOS
                # ====================================================

                comando = (
                    "SELECT "
                    "[LOCALIDADE], "
                    "[VALOR] "
                    "FROM [Dados$]"
                )

                adapter = OleDbDataAdapter(
                    comando,
                    conexao
                )

                ds = DataSet()

                adapter.Fill(
                    ds
                )


                if ds.Tables.Count == 0:
                    raise Exception(
                        "A guia Dados não retornou nenhuma tabela."
                    )


                tabela = ds.Tables[0]


                # ====================================================
                # PROCESSAMENTO DAS LINHAS
                # ====================================================

                for linha in tabela.Rows:

                    totalLinhas += 1

                    try:
                        localidade = Texto(
                            linha["LOCALIDADE"]
                        )

                        valorTexto = Texto(
                            linha["VALOR"]
                        )


                        # --------------------------------------------
                        # LINHA VAZIA
                        # --------------------------------------------

                        if (
                            localidade == "" and
                            valorTexto == ""
                        ):
                            linhasVazias += 1
                            continue


                        # --------------------------------------------
                        # VALIDAÇÕES
                        # --------------------------------------------

                        if localidade == "":
                            raise Exception(
                                "LOCALIDADE não informada."
                            )

                        if valorTexto == "":
                            raise Exception(
                                "VALOR não informado."
                            )


                        valor = ConverterValor(
                            valorTexto
                        )


                        # --------------------------------------------
                        # DUPLICIDADE
                        # --------------------------------------------

                        if GridPossuiRegistro(
                            localidade,
                            valor
                        ):
                            duplicadas += 1

                            if duplicadas <= 20:
                                detalhes += (
                                    "\nLinha {0} ignorada: "
                                    "LOCALIDADE={1} e VALOR={2} "
                                    "já existem na GRID_NF."
                                ).format(
                                    totalLinhas,
                                    localidade,
                                    valor
                                )

                            continue


                        # --------------------------------------------
                        # ADICIONA NA GRID
                        # --------------------------------------------

                        OrdemServico.AdicionaLinhaRegistro(
                            "GRID_NF",
                            [
                                "LOCALIDADE",
                                "VALOR"
                            ],
                            [
                                localidade,
                                valor
                            ]
                        )

                        adicionadas += 1


                        if adicionadas <= 10:
                            detalhes += (
                                "\nLinha {0} adicionada: "
                                "LOCALIDADE={1}; VALOR={2}"
                            ).format(
                                totalLinhas,
                                localidade,
                                valor
                            )


                    except Exception as exLinha:

                        erros += 1

                        if erros <= 30:
                            detalhes += (
                                "\nErro na linha {0}: {1}"
                            ).format(
                                totalLinhas,
                                Texto(exLinha)
                            )


                # ====================================================
                # COMPLEMENTO DOS CONTADORES
                # ====================================================

                if erros > 30:
                    detalhes += (
                        "\nExistem mais {0} erro(s) "
                        "não exibidos no resumo."
                    ).format(
                        erros - 30
                    )


                if duplicadas > 20:
                    detalhes += (
                        "\nExistem mais {0} duplicidade(s) "
                        "não exibidas no resumo."
                    ).format(
                        duplicadas - 20
                    )


            except Exception as ex:

                erros += 1

                detalhes += (
                    "\nErro geral ao importar o arquivo: {0}"
                ).format(
                    Texto(ex)
                )


            finally:

                try:
                    conexao.Close()
                except:
                    pass


            # ========================================================
            # TOTAL FINAL DA GRID
            # ========================================================

            totalGrid = 0

            try:
                totalGrid = OrdemServico.GetCustom(
                    "GRID_NF"
                ).Rows.Count

            except Exception as exGrid:

                detalhes += (
                    "\nNão foi possível contar as linhas "
                    "da GRID_NF: {0}"
                ).format(
                    Texto(exGrid)
                )


            # ========================================================
            # RESUMO
            # ========================================================

            resumo = (
                "Importação concluída!\n\n"
                "Arquivo: ARQUIVO05\n"
                "Guia utilizada: Dados\n"
                "Linhas lidas: {0}\n"
                "Linhas vazias: {1}\n"
                "Adicionadas: {2}\n"
                "Duplicadas/ignoradas: {3}\n"
                "Erros: {4}\n"
                "Total na GRID_NF: {5}\n\n"
                "Detalhes:{6}"
            ).format(
                totalLinhas,
                linhasVazias,
                adicionadas,
                duplicadas,
                erros,
                totalGrid,
                detalhes
            )

            Formulario.ExibeMensagem(
                resumo
            )


        # ============================================================
        # EXECUTA A IMPORTAÇÃO
        # ============================================================

        LerExcel()


    else:

        Formulario.ExibeMensagem(
            "Não há arquivo anexado no campo ARQUIVO05 "
            "para importação."
        )

        Controle.Valor = False
```
  - GRID_NF "Detalhamento da NF" [DataGrid RecordList → Z_00143_GRID_NF.GRID_NF] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna DESCRICAO obrigatório
    - coluna VALOR obrigatório
    - coluna LOCALIDADE obrigatório
  - GERENCIAS_FATURAMENTO "Gerências Faturamento" [DropDownList String → CPE_CONTRATOS02.GERENCIAS_FATURAMENTO] obrigatório
**GERENCIAS_FATURAMENTO.ScriptModificado**
```python
from Venki.Supravizio.Configuracao.Custom import Software
Formulario['COMBOBOX'].Visivel = True

gerencias_faturamento_dict = {
    "Gecob": ["CRBB SSA", "CRBB RJ", "CRBB BSB", "CRBB BB Américas", "Cobrança Extrajudicial", "Kit Pré-Ajuizamento", "GED/UTD", "Microfilmagem", "Outro"],
    "Gecor": ["BB Consórcios", "BB Correspondente Bancário", "Outro"],
    "Gelop/Gered": ["TAA", "Demais Bens", "Rede Man", "PGDM", "DOSI", "DOSA", "DOCA", "Monitoração", "PSIM", "TEYA - Outsourcing de Telefonia","Nobreak Norte", "Nobreak Sul", "Outro"],
    "Gepin": ["Hiveplace", "Outro"],
    "Gesec": ["Licenter", "SOC BB", "SOC BB Américas", "SOC CASSI","Outro"],
    "Geape": ["Fábrica de Software - Credenciamento", "Fábrica de Software - BB Tribunais", "FSW - Autoban", "Outro"],
    "Gesit": ["Intevia - E-mail MKT", "Intevia - SMS", "Aprovve", "Outro"],
    "Outra": None
    }
    
Formulario["VALOR_AUTORIZADO"].Visivel = True if Formulario['GERENCIAS_FATURAMENTO'].Valor == "Gecob" else False

    
valor = Formulario["GERENCIAS_FATURAMENTO"].Valor
itens = gerencias_faturamento_dict.get(valor)

if itens is None:
    Formulario["COMBOBOX"].Visivel = False
else:
    Formulario["COMBOBOX"].Itens = itens
```
  - COMBOBOX "Negócio/Produto" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório — Coluna=2
  - VLFAT_FAT "Faturamento Total - R$" [TextBox Decimal → CPE_FINANCEIRO.VLFAT_FAT] obrigatório
**VLFAT_FAT.ScriptModificado**
```python
if Formulario["VLREBATE_FAT"].Valor == None or Formulario["VLFAT_FAT"].Valor == None:
    Formulario["VALOR FAT LIQUIDO"].Valor = 0
else:
    Formulario["VALOR FAT LIQUIDO"].Valor = Formulario["VLFAT_FAT"].Valor - Formulario["VLREBATE_FAT"].Valor
```
  - VALOR_AUTORIZADO "Bônus" [TextBox Decimal → CPE_MOVIMENTACAO_PESSOA.VALOR_AUTORIZADO] obrigatório — Coluna=2
  - VLREBATE_FAT "Rebate, Glosa ou Multa Total - R$" [TextBox Decimal → CPE_FINANCEIRO.VLREBATE_FAT] obrigatório
**VLREBATE_FAT.ScriptModificado**
```python
if Formulario["GERENCIAS_FATURAMENTO"].Valor == 'Gecob':
    if not String.IsNullOrEmpty(Formulario["VALOR_AUTORIZADO"].Valor.ToString()): 
        Formulario["VALOR FAT LIQUIDO"].Valor = Formulario["VLFAT_FAT"].Valor + Formulario["VALOR_AUTORIZADO"].Valor - Formulario["VLREBATE_FAT"].Valor
    else:
        Formulario.ExibeMensagem('Preencha o campo bônus primeiro.')
else:
    Formulario["VALOR FAT LIQUIDO"].Valor = Formulario["VLFAT_FAT"].Valor - Formulario["VLREBATE_FAT"].Valor
```
  - VALOR FAT LIQUIDO "Total Líquido a Faturar (FT - RebGloMul) - R$" [TextBox String → CPE_PESSOAS.VALOR_FAT_LIQUIDO] obrigatório — Coluna=2
  - SIM_NAO3 "É repactuação?" [DropDownList String → CPE_CSC.SIM_NAO3] obrigatório
**SIM_NAO3.ScriptModificado**
```python
if Formulario["SIM_NAO3"].Valor == 'Sim':
    Formulario["MESES_ANO"].Visivel = False
    
if Formulario["SIM_NAO3"].Valor != 'Sim':
    Formulario["MESES_ANO"].Visivel = True
```
  - MESES_ANO "Competência (mês a que se refere o faturamento)" [DropDownList String → CPE_CONTRATOS02.MESES_ANO] obrigatório — Coluna=2
  - DTVENC_FAT "Data de Vencimento" [DatePicker DateTime → CPE_FINANCEIRO.DTVENC_FAT] obrigatório
  - DESCRICAO_DETALHADA "Corpo da Nota (Descrição)" [Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório
  - DESTNFSE_FAT "E-mails internos a serem notificados sobre cada etapa do chamado (Separados por ponto e vírgula) (Será enviado e-mail automático após as atividades: devolução para ajustes; Criar espelho da NF no ERP; Gerar Nota Fiscal na Prefeitura; Finalização do chamado)" [TextBox String → CPE_FINANCEIRO.DESTNFSE_FAT]
  - DEC_AUX_HOM "Declaração de Ciência: Estou ciente que no caso de faturamento com penalidades contratuais (rebate, glosa ou multa) deverá ser anexado o documento com de acordo do alçada vigente conforme NI006." [CheckBox Boolean → CPE_PESSOAS.DEC_AUX_HOM] obrigatório
  - CHECKBOX15 "Confirmo que anexei o "De acordo" do cliente" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX15] obrigatório
- Operação PR0001 Preencher Campos
  - SIM_NAO2 "Primeiro faturamento?" [DropDownList String → CPE_CSC.SIM_NAO2] obrigatório
**SIM_NAO2.ScriptModificado**
```python
if Formulario['SIM_NAO2'].Valor == "Sim":
    Formulario['DESCRICAO_OBRIG2'].Visivel = True
    Formulario['SIM_NAO1'].Visivel = True
    Formulario['ANEXO'].Visivel = True
    
if Formulario['SIM_NAO2'].Valor != "Sim":
    Formulario['DESCRICAO_OBRIG2'].Visivel = False
    Formulario['SIM_NAO1'].Visivel = False
    Formulario['ANEXO'].Visivel = False
```
  - DESCRICAO_OBRIG2 "Descrição do Questionamento" [Memo String(2000) → CPE_CSC.DESCRICAO_OBRIG2]
**DESCRICAO_OBRIG2.ScriptModificado**
```python
#if (OrdemServico.Servico.Sigla) == "PFANLSESPLHNFFTRDA":
    #Formulario["DESCRICAO_OBRIGATORIA"].Visivel = True
```
  - SIM_NAO1 "O lançamento vai gerar pagamento a fornecedor?" [DropDownList String → CPE_CSC.SIM_NAO1] obrigatório
**SIM_NAO1.ScriptModificado**
```python
if Formulario["SIM_NAO1"].Valor == 'Sim':
    Formulario["SIM_NAO"].Visivel = True
    Formulario["SIM_NAO"].Habilitado = True
    
if Formulario["SIM_NAO1"].Valor != 'Sim':
    Formulario["SIM_NAO"].Visivel = False
    Formulario["SIM_NAO"].Habilitado = False
```
  - SIM_NAO_FAT "Tem contrato?" [DropDownList String(50) → CPE_CSC.SIM_NAO_FAT] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Parecer de Novos Negócios  — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Rateio das Localidades" classes: Rateio Localidades — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Demais Arquivos" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo ""De acordo" por e-mail nos casos de penalidade contratual com multa, glosa ou rebate conforme NI006." classes: De Acordo — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Aceite do Cliente" classes: Aceite do Cliente — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração: Nome=ANEXO
  - anexo "Documento" classes: Arquivo — RequeridoInicial=true

### [348700] EventoIntermediarioMensagem "Comunicado para ajustes"
Destinatário: Cliente (papel 18)
Config: ListaDestinatarios=difin@bbts.com.br;contratos.clientes@bbts.com.br;cesec.bsb@bbts.com.br
ModeloComunicado: Comunicado para Ajustes - 5 dias
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
A ordem de serviço número OrdemServico.Numero necessita de ajustes e informações. 
Pedimos por gentileza, efetuar os ajuste em até 5 (cinco) dias para não impactar no atendimento da sua solicitação. 
Ajustes necessários:
OrdemServico.Justificativa 
Após finalizar as correções clique na opção "Avançar".
Para maiores informações Link.Edicao .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
##Mensagem.Destinatarios.Add(OrdemServico.GetCustom("DESTNFSE_FAT"))

if OrdemServico["DESTNFSE_FAT"] != None:    
    lista = OrdemServico["DESTNFSE_FAT"].Split(";")  
    for email in lista:        
        Mensagem.Destinatarios.Add(email)
```

### [348701] EventoIntermediarioMensagem "Comunicado de Abertura - Faturamento"
Destinatário: Cliente (papel 18)
Config: ListaDestinatarios=contratos.clientes@bbts.com.br; difin@bbts.com.br;priscilla.santos@bbts.com.br;edna.brito@bbts.com.br;charles.carvalho@bbts.com.br
ModeloComunicado: Faturamento - Abertura
Corpo do comunicado: Prezado(a) OrdemServico.Cliente ,
Comunicamos sobre o andamento do processo de faturamento abaixo:
Número OKS: OrdemServico.Customizado.OKS_FAT 
Vencimento:OrdemServico.Customizado.DTVENC_FAT
Faturamento Total:OrdemServico.Customizado.VLFAT_FAT
Valor de Rebate:OrdemServico.Customizado.VLREBATE_FAT
As notas fiscais serão emitidas nos sites das prefeituras, iremos envia-las ao Cliente e lhe informaremos quando o faturamento for concluído.
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
##Mensagem.Destinatarios.Add(OrdemServico.GetCustom("DESTNFSE_FAT"))

if OrdemServico["DESTNFSE_FAT"] != None:    
    lista = OrdemServico["DESTNFSE_FAT"].Split(";")  
    for email in lista:        
        Mensagem.Destinatarios.Add(email)
```

### [348702] EventoIntermediarioMensagem "Comunicado de Finalização de criação de espelho da NF no ERP"
Destinatário: Cliente (papel 18)
Config: ListaDestinatarios=difin@bbts.com.br;contratos.clientes@bbts.com.br;faturamento@bbts.com.br
ModeloComunicado: Faturamento - Espelho nota fiscal
Corpo do comunicado: Prezado(a),
Informamos que o espelho da nota fiscal foi gerado com sucesso.
Para maiores informações Link.Consulta 
Atenciosamente,
Portal de Atendimento.
**ScriptEvento**
```python
if OrdemServico["DESTNFSE_FAT"] != None:    
    lista = OrdemServico["DESTNFSE_FAT"].Split(";")  
    for email in lista:        
        Mensagem.Destinatarios.Add(email)
```
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=1683; ClasseConfiguracao=Nota Fiscal de Serviço

### [348703] Tarefa "Informar os ajustes necessários"
Responsável: Responsável atual (papel 36)
**ScriptFormCarregado**
```python
Formulario["Justificativa"].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - LABEL1 "Informe os Ajustes Necessários:" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - Justificativa (nativo) "Adicione comentários sobre a devolução para ajustes:" obrigatório

### [348704] EventoIntermediarioMensagem "Faturamento - Não Faturado"
Destinatário: Cliente (papel 18)
Config: ListaDestinatarios=difin@bbts.com.br;contratos.clientes@bbts.com.br
ModeloComunicado: Faturamento - Não Faturado
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Comunicamos o término sem sucesso do processo de faturamento abaixo:
Número OKS: OrdemServico.Customizado.OKS_FAT 
Vencimento:OrdemServico.Customizado.DTVENC_FAT
Faturamento Total:OrdemServico.Customizado.VLFAT_FAT
Valor de Rebate:OrdemServico.Customizado.VLREBATE_FAT
Para maiores informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [348705] FimCancelamento ""

### [348706] EventoIntermediarioMensagem "Comunicado Aprovação"
Destinatário: Fila CSC - Pendente de Aprovação (papel 461)
ModeloComunicado: Comunicado - Pendencia de Aprovação
Corpo do comunicado: Prezado(a),
O chamado interno OrdemServico.Numero - OrdemServico.Assunto.
Comunicamos que a atividade OrdemServico.Atividade está pendente de aprovação.

### [348707] Tarefa "Verificação solicitação"
Referência: Orientações para a tarefa:
Verifique as informações inseridas pelo cliente solicitante;
Avalie se houve ausências de informações ou divergências;
Observe orientações contidas no POP217-001 - xxx xxx x xx xxxx. 
Após verificação e ao avançar a tarefa, a OS retornará para a fila para que solucionadores do Cesec-FIN assumam a responsabilidade e realizem a inserção dos dados no módulo OKS do EBS.
IMPORTANTE ü
- Verificar Penalidades
 Verifique se há penalidade contratual. Em caso positivo, verifique se foi anexado o "De acordo" dos Gestores" do comitê da Gerência Executiva composta por: Gerente Ex
Responsável: Fila CSC - Faturamento de Clientes (papel 733)
Config: ConfirmaResponsabilidade=true
**ScriptInicio**
```python
OrdemServico.ModificaCampoFormularioVisivel('NUM_DOCU', True)
```

### [348708] Tarefa "Aguardar Retorno do Parecer DITRI"
Responsável: Responsável atual (papel 36)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
- Acoes:
  - Acao=Email; Percentual=0; CodigoGrupoANO=4ae376b3-01fc-4da4-91e4-b23700c8c5a3

### [348709] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [348710] SubProcesso "Gerar Nota Fiscal na Prefeitura"
Responsável: Fila CSC - Faturamento de Clientes (papel 733)
Config: AssociacaoId=1522; ChamadaAssincrona=true; PassaTodosItens=true; RetornaTodosItens=true
- ValoresInputs:
  - CustomPropertyId=2027; CustomProperty=VLREBATE_FAT
  - CustomPropertyId=3188; CustomProperty=VALOR FAT LIQUIDO
  - CustomPropertyId=1965; CustomProperty=SIM_NAO3
  - CustomPropertyId=2021; CustomProperty=OKS_FAT
  - CustomPropertyId=5021; CustomProperty=GERENCIAS_FATURAMENTO
  - CustomPropertyId=1032; CustomProperty=COMBOBOX
  - CustomPropertyId=2028; CustomProperty=VLFAT_FAT
  - CustomPropertyId=5039; CustomProperty=MESES_ANO
  - CustomPropertyId=2022; CustomProperty=DTVENC_FAT
  - CustomPropertyId=2026; CustomProperty=DESTNFSE_FAT
  - CustomPropertyId=2246; CustomProperty=DEC_AUX_HOM
  - CustomPropertyId=128; CustomProperty=DGCO
  - CustomPropertyId=288; CustomProperty=NUM_DOCU
  - CustomPropertyId=1967; CustomProperty=DGCO_BB
- Associação: FraseAssociacao=Faturamento --> Gerar NF Prefeitura; FraseInversaAssociacao=Gerar NF Prefeitura --> Faturamento; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=GERARNFPREF; SeparadorSequencial=. | fonte: Faturamento de Clientes - Emissão de Notas Fiscais → alvo: Gerar Nota Fiscal na Prefeitura

## Papéis usados
### papel 733: Fila CSC - Faturamento de Clientes
Tipo=RelacaoPessoas | pessoas: Fila CSC - Faturamento de Clientes
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 1321: Cesec Faturamento Gyn
Tipo=RelacaoPessoas | pessoas: CHARLES HENRIQUE DE CARVALHO, EDNA RODRIGUES BRITO GONTIJO, JACILENE ROCHA DE SOUZA
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```
### papel 461: Fila CSC - Pendente de Aprovação
Tipo=RelacaoPessoas | pessoas: Fila CSC - Pendente de Aprovação

## Campos customizados usados (definição global)

### LABEL_GRANDE — Label Grande
Label String(2000) → CPE_MOVIMENTACAO_PESSOA.LABEL_GRANDE

### DGCO_BB — DGCO
TextBox String(300) → CPE_FINANCEIRO.DGCO_BB

### OKS_FAT — Contrato OKS
TextBox String → CPE_FINANCEIRO.OKS_FAT

### NUM_DOCU — Número do documento
TextBox String → CP_ORDEM_SERVICO.NUM_DOCU

### GRID_NF — Grid de Emissão de notas Fiscais
DataGrid RecordList → Z_00143_GRID_NF.GRID_NF
Colunas do registro:
- LOCALIDADE "Localidade da NF" [TextBox String]
- VALOR "Valor da NF" [TextBox Decimal]

### GERENCIAS_FATURAMENTO — Gerências Faturamento
DropDownList String → CPE_CONTRATOS02.GERENCIAS_FATURAMENTO
Descrição: Gerências
Itens: Gelop/Gered;Gecob;Gesec;Gepin;Gesit;Gecor;Geape;Outra

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX
Itens: Órtese;Órtese Dentária; Prótese;Recurso para Saúde

### VLFAT_FAT — Faturamento Total - R$
TextBox Decimal → CPE_FINANCEIRO.VLFAT_FAT

### VALOR_AUTORIZADO — Valor Autorizado
TextBox Decimal → CPE_MOVIMENTACAO_PESSOA.VALOR_AUTORIZADO

### VLREBATE_FAT — Rebate, Glosa ou Multa Total - R$
TextBox Decimal → CPE_FINANCEIRO.VLREBATE_FAT

### VALOR FAT LIQUIDO — VALOR FAT LIQUIDO
TextBox String → CPE_PESSOAS.VALOR_FAT_LIQUIDO

### SIM_NAO3 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO3
Descrição: Informe
Itens: Sim;Não

### MESES_ANO — Meses
DropDownList String → CPE_CONTRATOS02.MESES_ANO
Itens: Janeiro;Fevereiro;Março;Abril;Maio;Junho;Julho;Agosto;Setembro;Outubro;Novembro;Dezembro

### DTVENC_FAT — Data de Vencimento
DatePicker DateTime → CPE_FINANCEIRO.DTVENC_FAT

### DESCRICAO_DETALHADA — Descrição detalhada
Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA

### DESTNFSE_FAT — Destinatário NFSe
TextBox String → CPE_FINANCEIRO.DESTNFSE_FAT

### DEC_AUX_HOM — declaração auxilio home
CheckBox Boolean → CPE_PESSOAS.DEC_AUX_HOM
Descrição: declaração auxilio home 

### CHECKBOX15 — Checkbox15
CheckBox Boolean → CPE_PESSOAS.CHECKBOX15
Descrição: Validar Locomoções

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### CHECKBOX1 — Checkbox1
CheckBox Boolean → CPE_PESSOAS.CHECKBOX1

### SIM_NAO2 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO2
Itens: Sim;Não

### DESCRICAO_OBRIG2 — Descrição obrigatória
Memo String(2000) → CPE_CSC.DESCRICAO_OBRIG2
Descrição: Breve descrição

### SIM_NAO1 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO1
Itens: Sim;Não

### SIM_NAO_FAT — Sim ou Nao
DropDownList String(50) → CPE_CSC.SIM_NAO_FAT
Descrição: Selecione uma das opções.
Itens: Sim;Não

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
