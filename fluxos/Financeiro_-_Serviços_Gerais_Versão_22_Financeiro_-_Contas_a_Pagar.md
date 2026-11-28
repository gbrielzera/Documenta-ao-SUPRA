# Fluxo: Financeiro - Contas a Pagar (CONTASPAGAR) — versão 22
Caminho: Fluxos > Financeiro - Serviços Gerais Versão 22 Financeiro - Contas a Pagar
XML: `XMLs para teste/Financeiro_-_Serviços_Gerais_Versão_22_Financeiro_-_Contas_a_Pagar.xml` | Supravizio 19.1.1 | SubProcessoId 20857 | DesenhoProcessoId 2796 | ProcessoId 150
Órgão dono: 3000003110 - DIVISAO DE FINANCAS | Responsável: MIGUEL PIRES VILELLA
Classe do subprocesso: DescricaoCliente=Contas a Pagar; CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Contas a Pagar (CONTASPAGAR)

## Grafo do fluxo
- [349168] LinkInicial "" → [332189] Verificar Solicitação

- [354061] FimCancelamento "Cancelamento" → (fim)
- [332179] LinkInicial "" → [332178] Verificar Solicitação

- [332180] Tarefa "Informar Ajustes Necessários" {Responsável atual} → [332146] Comunicado de Reajuste 
- [332181] Tarefa "Avaliar demanda" {Fila CSC - Pagamentos} → [332162] Aguardar data de pagamento
- [332182] EventoIntermediarioTimer "" → [332137] Reprovação por falta de ajustes
- [332183] EventoIntermediarioTimer "" → [332151] Reprovação por falta de ajustes
- [332184] EventoIntermediarioTimer "" → [332136] Reprovação por falta de ajustes
- [332170] LinkInicial "" → [332181] Avaliar demanda
- [332173] Tarefa "Verificar Solicitação
" {Fila CSC - Pagamentos} → [G75499] Dados Ok?
- [332174] Tarefa "Efetuar Pagamento" {Responsável atual} → [332152] Comunicado Contas a Pagar - Aprovado
- [332175] Tarefa "Informar Reajustes Necessários" {Responsável atual} → [332167] Comunicado de Reajuste 
- [332176] Tarefa "Informar Reajustes Necessários" {Responsável atual} → [332140] Comunicado de Ajuste 
- [332177] Tarefa "Corrigir informação
" {Cliente} → [332135] Verificar Solicitação
 | [332184] 
- [332178] Tarefa "Verificar Solicitação
" {Fila CSC - Pagamentos} → [G75497] Dados Ok?
- [332141] Tarefa "Corrigir informação
" {Cliente} → [332189] Verificar Solicitação

- [332143] Tarefa "Corrigir informação
" {Cliente} → [332190]  | [332173] Verificar Solicitação

- [332153] Tarefa "Efetuar Pagamento" {Responsável atual} → [332159] Comunicado Contas a Pagar - Aprovado
- [332155] LinkInicial "Auxilio/Incentivo Adaptação Cedidos BB" → [332178] Verificar Solicitação

- [332157] EventoIntermediarioMensagem "Comunicado de Reajuste " → [332143] Corrigir informação

- [332159] EventoIntermediarioMensagem "Comunicado Contas a Pagar - Aprovado" → [332158] 
- [332160] Tarefa "Informar Reajustes Necessários" {Responsável atual} → [332133] Comunicado de Ajuste 
- [332161] EventoIntermediarioMensagem "Reprovação por falta de ajustes" → [332168] 
- [332162] Tarefa "Aguardar data de pagamento" {Responsável atual} → [332153] Efetuar Pagamento
- [332171] LinkInicial "" → [332132] Verificar Solicitação

- [332172] EventoIntermediarioMensagem "Reprovação por falta de ajustes" → [332164] 
- [332158] EventoFinal "" {Responsável atual} → (fim)
- [332163] LinkInicial "" → [332135] Verificar Solicitação

- [332164] FimCancelamento "" → (fim)
- [332165] FimCancelamento "" → (fim)
- [332166] Tarefa "Informar Reajustes Necessários" {Responsável atual} → [332149] Comunicado de Reajuste 
- [332167] EventoIntermediarioMensagem "Comunicado de Reajuste " → [332150] Corrigir a informação

- [332168] FimCancelamento "" → (fim)
- [332188] LinkInicial "Serviços Despachantes - Estabelecimento" → [332134] Verificar Solicitação

- [332144] FimCancelamento "" → (fim)
- [332189] Tarefa "Verificar Solicitação
" {Fila CSC - Pagamentos} → [G75501] Dados Ok?
- [332190] EventoIntermediarioTimer "" → [332172] Reprovação por falta de ajustes
- [332191] EventoIntermediarioMensagem "Comunicado de Ajuste " → [332186] Corrigir informação

- [332192] Tarefa "Verificar Solicitação
" {Fila CSC - Pagamentos} → [G75496] Dados Ok?
- [332193] LinkInicial "" → [332192] Verificar Solicitação

- [332194] Tarefa "Informar Reajustes Necessários" {Responsável atual} → [332191] Comunicado de Ajuste 
- [332187] Tarefa "Corrigir informação
" {Responsável pelo início do subprocesso} → [332178] Verificar Solicitação
 | [332185] 
- [332145] Tarefa "Informar Reajustes Necessários" {Responsável atual} → [332157] Comunicado de Reajuste 
- [332146] EventoIntermediarioMensagem "Comunicado de Reajuste " → [332147] Corrigir informação

- [332147] Tarefa "Corrigir informação
" {Cliente} → [332182]  | [332132] Verificar Solicitação

- [332148] EventoFinal "" {Responsável atual} → (fim)
- [332149] EventoIntermediarioMensagem "Comunicado de Reajuste " → [332187] Corrigir informação

- [332150] Tarefa "Corrigir a informação
" {Cliente} → [332183]  | [332134] Verificar Solicitação

- [332151] EventoIntermediarioMensagem "Reprovação por falta de ajustes" → [332165] 
- [332152] EventoIntermediarioMensagem "Comunicado Contas a Pagar - Aprovado" → [354061] Cancelamento
- [332185] EventoIntermediarioTimer "" → [332161] Reprovação por falta de ajustes
- [332186] Tarefa "Corrigir informação
" {Cliente} → [332192] Verificar Solicitação

- [332132] Tarefa "Verificar Solicitação
" {Fila CSC - Pagamentos} → [G75500] Dados Ok?
- [332133] EventoIntermediarioMensagem "Comunicado de Ajuste " → [332141] Corrigir informação

- [332134] Tarefa "Verificar Solicitação
" {Fila CSC - Pagamentos} → [G75498] Dados Ok?
- [332135] Tarefa "Verificar Solicitação
" {Fila CSC - Pagamentos} → [G75502] Dados Ok?
- [332136] EventoIntermediarioMensagem "Reprovação por falta de ajustes" → [332144] 
- [332137] EventoIntermediarioMensagem "Reprovação por falta de ajustes" → [332138] 
- [332138] FimCancelamento "" → (fim)
- [332140] EventoIntermediarioMensagem "Comunicado de Ajuste " → [332177] Corrigir informação

- [359524] LinkInicial "" → [359525] Aviso da Abertura da OS
- [359525] EventoIntermediarioMensagem "Aviso da Abertura da OS" → [332178] Verificar Solicitação

- [G75496] Gateway "Dados Ok?" → «Sim» [332153] Efetuar Pagamento | «Não» [332194] Informar Reajustes Necessários
- [G75497] Gateway "Dados Ok?" → «Não» [332166] Informar Reajustes Necessários | «Sim» [332153] Efetuar Pagamento
- [G75498] Gateway "Dados Ok?" → «Sim» [332153] Efetuar Pagamento | «Não» [332175] Informar Reajustes Necessários
- [G75499] Gateway "Dados Ok?" → «Sim» [332153] Efetuar Pagamento | «Não» [332145] Informar Reajustes Necessários
- [G75500] Gateway "Dados Ok?" → «Sim» [332174] Efetuar Pagamento | «Não» [332180] Informar Ajustes Necessários
- [G75501] Gateway "Dados Ok?" → «Sim» [332153] Efetuar Pagamento | «Não» [332160] Informar Reajustes Necessários
- [G75502] Gateway "Dados Ok?" → «Sim» [332153] Efetuar Pagamento | «Não» [332176] Informar Reajustes Necessários

## Gateways
### [G75496] Dados Ok? (EventBasedExclusiveDecision)
Codigo=DADOSOKKKK
- alternativa → [332153] Efetuar Pagamento: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [332194] Informar Reajustes Necessários: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
### [G75497] Dados Ok? (EventBasedExclusiveDecision)
Codigo=DADOS
- alternativa → [332166] Informar Reajustes Necessários: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
- alternativa → [332153] Efetuar Pagamento: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
### [G75498] Dados Ok? (EventBasedExclusiveDecision)
Codigo=DADOSOK2
- alternativa → [332153] Efetuar Pagamento: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [332175] Informar Reajustes Necessários: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
### [G75499] Dados Ok? (EventBasedExclusiveDecision)
Codigo=DADOSOKK
- alternativa → [332153] Efetuar Pagamento: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [332145] Informar Reajustes Necessários: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
### [G75500] Dados Ok? (EventBasedExclusiveDecision)
Codigo=DADOSOK
- alternativa → [332174] Efetuar Pagamento: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [332180] Informar Ajustes Necessários: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
### [G75501] Dados Ok? (EventBasedExclusiveDecision)
Codigo=DADOS__OK
- alternativa → [332153] Efetuar Pagamento: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [332160] Informar Reajustes Necessários: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
### [G75502] Dados Ok? (EventBasedExclusiveDecision)
Codigo=DADOSOKKK
- alternativa → [332153] Efetuar Pagamento: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [332176] Informar Reajustes Necessários: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1

## Atividades

### [349168] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexar Boleto" classes: Anexo — RequeridoInicial=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=DOU
  - NUMERO_RI "Número do RI" [TextBox String → CPE_CSC.NUMERO_RI] obrigatório
  - BOLETO "Valor do Boleto" [TextBox String → CPE_CSC.BOLETO] obrigatório
  - DATA_EMISSAO "Data do Lançamento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_EMISSAO] obrigatório
- Associação de subprocesso: AssociacaoId=1110; FraseAssociacao=Publicação do DOU -> Financeiro - Contas a Pagar (Douglas); Nome=DOUCONPA

### [354061] FimCancelamento "Cancelamento"

### [332179] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
**ScriptFormCarregado**
```python
campo = [
    "CONTA_CONTABIL_PAGAMENTO_RCC",
    "DATA_DE_PAGAMENTO",
    "LABEL1",
    "LABEL10",
    "SIM_NAO1",
    "VALOR",
    "COMBOBOX",
    "FAVORECIDO_TODOS",
    "MATRICULA",
    "ORDEM_DE_SERVICO",
    "SIM_NAO1"
]

for campo in campos:
    try:
        valor = Formulario[campo].Valor
        if valor == "" or valor == None:
            Formulario[campo].Visivel = False
            Formulario[campo].Habilitado = False
        else:
            Formulario[campo].Visivel = True
            Formulario[campo].Habilitado = True
    except Exception:
        # Campo não existe ou erro ignorado
        pass
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Auxílio Adaptação
  - SIM_NAO1 "O Favorecido faz parte do público alvo para o programa de adequação de quadro da Gered (Mudança para base destacada subdimensionada)?" [DropDownList String → CPE_CSC.SIM_NAO1]
**SIM_NAO1.ScriptModificado**
```python
if Formulario["SIM_NAO1"].Valor == "Sim":
    Formulario["COMBOBOX"].Visivel = True
    Formulario["COMBOBOX"].Itens = "TR-QUIXADA;TR-ALTAMIRA;TR-JI-PARANA;TR-ALMENARA;TR-CALDAS NOVAS;TR-UNAI;TR-JAU;TR-PARAGOMINAS;TR-GUANHAES;TR-DIVINOPOLIS;TR-IRECE;TR-SETE LAGOAS;TR-MARILIA;TR-BOM JESUS DA LAPA;CAT-BAURU;TR-GUARAPUAVA;TR-VITORIA DA CONQUISTA;TR-RIO VERDE;TR-VILHENA;TR-SANTA MARIA;TR-IGUATU;TR-VARGINHA;TR-JUIZ DE FORA;TR-SANTO ANTONIO DE JESUS;TR-PETROLINA;CAT-SAO PAULO PM;CAT-NATAL;CAT-MANAUS;TR-CAMPOS DOS GOYTACAZES;TR-OEIRAS;TR-PARAISO;TR-PARAUAPEBAS;TR-JUNDIAI;TR-BATURITE;TR-ARACATI;TR-COLIDER;TR-VIDEIRA;TR-XINGUARA;TR-ORIXIMINA;TR-BAGE;TR-VILA RICA;TR-CHAPADINHA;TR-ALEGRETE;TR-REDENCAO;TR-MACAPA;CAT-PORTO VELHO;TR-JUINA;TR-PRESIDENTE PRUDENTE;TR-PINHEIRO;TR-CATAGUASES;TR-DOURADOS;TR-BARRA DO GARCAS;TR-GUANAMBI;TR-JARDIM;TR-TEFE;TR-SALGUEIRO;TR-ROSARIO;TR-ARACUAI;TR-PARANAVAI;TR-LIMOEIRO DO NORTE;TR-CIDADE DE GOIAS;TR-CHAPADAO DO SUL;TR-SERRINHA;TR-BACABAL"
    
    
if Formulario["SIM_NAO1"].Valor != "Sim":
    Formulario["COMBOBOX"].Visivel = False
```
  - COMBOBOX "Informe a base subdimensionada (deficit de pessoal)?" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX]
  - FAVORECIDO_TODOS "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
**FAVORECIDO_TODOS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario["FAVORECIDO_TODOS"].Valor != "" and Formulario["FAVORECIDO_TODOS"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_TODOS"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        Formulario["MATRICULA"].Valor = favorecidoCustom["MATRICULA"].ToString()
```
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA]
  - ORDEM_DE_SERVICO "Ordem de Serviço de Nomeação/Transfêrencia" [TextBox String → CPE_CSC.ORDEM_DE_SERVICO]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Auxílio Adaptação
  - SIM_NAO1 "O Favorecido faz parte do público alvo para o programa de adequação de quadro da Gered (Mudança para base destacada subdimensionada)?" [DropDownList String → CPE_CSC.SIM_NAO1]
  - LABEL1 "ATENÇÃO: Para o programa de adequação da Gered considerar 75% do valor do salário do empregado." [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - LABEL10 "ATENÇÃO: O programa de adequação da Gered será pago por RCC. Não lance no Peoplesoft" [Label String(700) → CPE_PDCI2019.LABEL10]
  - VALOR "Valor R$" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - DATA_DE_PAGAMENTO "Data de pagamento" [DatePicker DateTime → CPE_CSC.DATA_DE_PAGAMENTO]
  - CONTA_CONTABIL_PAGAMENTO_RCC "Conta contabil pagamento RCC" [TextBox String(200) → CPE_CSC.CONTA_CONTABIL_PAGAMENTO_RCC]
- Associação de subprocesso: AssociacaoId=577; FraseAssociacao=Auxílio/Incentivo Adaptação -> Financeiro - Contas a Pagar; Nome=ADAPTACAOCONTASAPAGAR

### [332180] Tarefa "Informar Ajustes Necessários"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - Justificativa (nativo) "Ajustes Necessários" obrigatório

### [332181] Tarefa "Avaliar demanda"
Responsável: Fila CSC - Pagamentos (papel 705)

### [332182] EventoIntermediarioTimer ""
Config: TempoIntervalo=7200; MaximoExecucao=1
**ScriptEvento**
```python
OrdemServico.AvancaAtividade()
```

### [332183] EventoIntermediarioTimer ""
Config: TempoIntervalo=7200; MaximoExecucao=1
**ScriptEvento**
```python
OrdemServico.AvancaAtividade()
```

### [332184] EventoIntermediarioTimer ""
Config: TempoIntervalo=7200; MaximoExecucao=1
**ScriptEvento**
```python
OrdemServico.AvancaAtividade()
```

### [332170] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo referente ao Serviço (Não Obrigatório)" classes: Arquivo — RequeridoInicial=true; PermiteMultiplosItens=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Documentos (Não Obrigatório)" classes: Documentos — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=ECOA
  - CHAVE_CONTABIL "Chave Contábil para Débito" [TextBox String → CPE_FINANCEIRO.CHAVE_CONTABIL] obrigatório
  - UOR5 "UOR para o Débito" [TextBox String → CPE_FINANCEIRO.UOR5] obrigatório
    - coluna UOR obrigatório
  - CONTA_CONTABIL4 "Conta Contábil para o Débito" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL4] obrigatório
  - VALOR_DOD "Valor do pagamento" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=ECOA
  - COMBOBOX1 "Serviço" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
**COMBOBOX1.ScriptModificado**
```python
if Formulario['COMBOBOX1'].Valor == 'Pedido de Verba':
##        Formulario["CSC_COMBOBOX"].Visivel = True
        Formulario["LABEL10"].Visivel = True
        Formulario["DADOS_DE_PAGAMENTO"].Visivel = True
        Formulario["CSC_CEP"].Visivel = True
        
else:
##        Formulario["CSC_COMBOBOX"].Visivel = False
        Formulario["LABEL10"].Visivel = False
        Formulario["DADOS_DE_PAGAMENTO"].Visivel = False
        Formulario["CSC_CEP"].Visivel = False
        
if Formulario['COMBOBOX1'].Valor == 'Posse' or Formulario['COMBOBOX1'].Valor == 'Exoneração':
        Formulario["NOME_GRUPO"].Visivel = True
else:
        Formulario["NOME_GRUPO"].Visivel = False
```
  - DADOS_DE_PAGAMENTO "Dados do favorecido para pagamento da verba ECOA" [DataGrid RecordList → Z_00143_DADOS_DE_PAGAMENTO.DADOS_DE_PAGAMENTO] obrigatório
    - coluna CONTA obrigatório
    - coluna CPF obrigatório
    - coluna BANCO obrigatório
    - coluna CHAVE_PIX obrigatório
    - coluna AGENCIA obrigatório
  - CSC_CEP "Ano de Exercício" [TextBox String → CPE_CSC.CSC_CEP] obrigatório
  - DescricaoDetalhada (nativo) "Descrição Sobre o Serviço Solicitado" obrigatório
  - FAVORECIDO_COBRA "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
**FAVORECIDO_COBRA.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario["FAVORECIDO_COBRA"].Valor != "" and Formulario["FAVORECIDO_COBRA"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_COBRA"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        orgaoFavorecido = favorecidoCustom.OrgaoId
        Formulario["SCR_PRESTADOR"].Valor = favorecidoCustom.Orgao.Descricao.ToString()
        Formulario["MATRICULA"].Valor = favorecidoCustom["MATRICULA"].ToString()
```
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA] obrigatório
  - SCR_PRESTADOR "UOR" [TextBox String → CP_ORDEM_SERVICO.SCR_PRESTADOR] obrigatório
  - COMBOBOX "ECOA" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
  - PIX_NUMERO "Chave Pix" [TextBox String → CPE_CSC.PIX_NUMERO] obrigatório
- Associação de subprocesso: AssociacaoId=1308; FraseAssociacao=Programa Ecoa -> Financeiro > Contas a Pagar; Nome=PROGRAMA_ECOA_CONTAS_PAGAR

### [332173] Tarefa "Verificar Solicitação
"
Responsável: Fila CSC - Pagamentos (papel 705)
Config: ConfirmaResponsabilidade=true
- Relatorios:
  - FormatoExportacao=PDF

### [332174] Tarefa "Efetuar Pagamento"
Responsável: Responsável atual (papel 36)
Config: Codigo=PAGAMENTO_DOIS
MotivoInterrupcaoSLA: Aguando data de pagamento
**ScriptValidacao**
```python
listaGrid = OrdemServico["GUIASJUDICIAIS"]

for linha in listaGrid.Rows:
    if linha["CUSTASDEPOSITO"] == "Depósito":
        if OrdemServico.PossuiItem("COMPAG")== False:
            Criticas.AdicionaPendencia("Não foi associado um(a) 'Comprovante de pagamento de depósito'")
            
    if linha["CUSTASDEPOSITO"] == "Custas":
        if OrdemServico.PossuiItem("COMPAGCUSTAS")== False:
                Criticas.AdicionaPendencia("Não foi associado um(a) 'Comprovante de pagamento de custas'")
                
if (listaGrid.Rows.Count > 2):    
        Criticas.AdicionaPendencia("Lista de guias não pode ter mais de 2 registros!")
        
tipos_aceitos = ["pdf", "img", "png", "jpg", "bmp", "gif"]

if OrdemServico.PossuiItem("COMPAG"):
    
    anexo = OrdemServico.ObtemItem("COMPAG")
    
    nomeArquivo = anexo.ToString()
    
    # Obtem a extensão do arquivo
    tipoArquivo = nomeArquivo.split(".")[-1].lower()
    
    # Inicializando uma variável para controlar a verificação da extensão do arquivo
    tipoValido = False

    # Verifica se a extensão não está nos tipos aceitos
    # Iterando sobre a lista de tipos aceitos para verificar se a extensão é válida
    for tipo in tipos_aceitos:
        if tipoArquivo == tipo:
            tipoValido = True
            break

    # Se a extensão não for válida, adicionar a pendência
    if not tipoValido:
        Criticas.AdicionaPendencia("Enviar arquivos do tipo PDF ou Imagem para o arquivo de 'Comprovante de pagamento de depósito' ")
        
if OrdemServico.PossuiItem("COMPAGCUSTAS"):
    
    anexo = OrdemServico.ObtemItem("COMPAGCUSTAS")
    
    nomeArquivo = anexo.ToString()
    
    # Obtem a extensão do arquivo
    tipoArquivo = nomeArquivo.split(".")[-1].lower()
    
    # Inicializando uma variável para controlar a verificação da extensão do arquivo
    tipoValido = False

    # Verifica se a extensão não está nos tipos aceitos
    # Iterando sobre a lista de tipos aceitos para verificar se a extensão é válida
    for tipo in tipos_aceitos:
        if tipoArquivo == tipo:
            tipoValido = True
            break

    # Se a extensão não for válida, adicionar a pendência
    if not tipoValido:
        Criticas.AdicionaPendencia("Enviar arquivos do tipo PDF ou Imagem para o arquivo de 'Comprovante de pagamento de custas' ")
```
- Operação PR0001 Preencher Campos
  - DATA_VENCIMENTO "Data Solicitação de Pagamento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO] obrigatório
  - DATA_DO_EXTRATO "Data Limite para Retono ao Jurídico da Guia de Pagamento" [DatePicker DateTime → CPE_CSC.DATA_DO_EXTRATO] obrigatório
- Operação PR0001 Preencher Campos
  - GUIASJUDICIAIS "Guias de pagamento" [DataGrid RecordList → Z_00143_GUIASJUDICIAIS.GUIASJUDICIAIS] obrigatório
    - coluna VALOR
    - coluna PRAZO_FATAL
    - coluna NUMERO_RI
    - coluna MULTASJUROS obrigatório
    - coluna ORGANIZACAO
    - coluna NATUREZA obrigatório
    - coluna TIPO_DOCUMENTO obrigatório
    - coluna CUSTASDEPOSITO obrigatório
    - coluna DATA_PAGAMENTO obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=ANEXO_DOIS
  - anexo "Comprovante pagamento Depósito" classes: Comprovante de Pagamento Depósito — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Comprovante Pagamento Custas" classes: Comprovante de Pagamento Custas — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [332175] Tarefa "Informar Reajustes Necessários"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - Justificativa (nativo) "Ajustes Necessários" obrigatório

### [332176] Tarefa "Informar Reajustes Necessários"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - Justificativa (nativo) "Ajustes Necessários" obrigatório

### [332177] Tarefa "Corrigir informação
"
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptFormCarregado**
```python
Formulario["OBSERVACAO"].Visivel = True
Formulario["OBSERVACAO"].Habilitado = True


Formulario["Justificativa"].Habilitado = False
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Correção dos Campos Citados Acima:
  - OBSERVACAO "Informe os Dados Corretos" [TextBox String(2000) → CPE_CSC.OBSERVACAO] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=ARQUIVO N PARA PAGAMENTO
  - anexo "Anexo" classes: Arquivo — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Campo(s) Passivel(is) de Correção:
  - Justificativa (nativo) "Ajustes Necessários" obrigatório

### [332178] Tarefa "Verificar Solicitação
"
Responsável: Fila CSC - Pagamentos (papel 705)
Config: Codigo=ANALISAR; ConfirmaResponsabilidade=true
**ScriptFormCarregado**
```python
# Lista de campos gerais
campos = ["COMPETENCIA","CONTA_CONTABIL_PAGAMENTO_RCC","DATA_DE_PAGAMENTO","FAVORECIDO_COBRA","FAVORECIDO_TODOS","MATRICULA","MATRICULA_MOVI","MESANOREF","MOTIVO_GERAL","OBS1","OBSERVACAO","RCC_TIPO_SOLICITACAO","SCR_TODOS_RH","TE_MATRICULA","TE_NOME_EMPREGADO","UOR_PAGADORA","VALOR","VALOR_NOTA","VALOR_PAGAMENTO_RCC","VALOR_REEMBOLSO","CSC_BANCO2","CSC_CONTA_CORRENTE","CSC_NUMERO","CSC_NUMERO_AGENCIA", "NUMERO_ATA"]

for campo in campos:
    try:
        valor = Formulario[campo].Valor
        if not valor:
            Formulario[campo].Visivel = False
            Formulario[campo].Habilitado = False
        else:
            Formulario[campo].Visivel = True
            Formulario[campo].Habilitado = True
    except Exception:
        # Campo não existe ou erro ignorado
        pass


#def isVisible(field):
#    if field == None or field == DBNull.Value:
#        return False
#    elif field == '' or String.IsNullOrEmpty(field):
#        return False
#    else:
#        return True
#
#Formulario["MOTIVO_GERAL"].Visivel = isVisible(Formulario["MOTIVO_GERAL"].Valor)
#Formulario["UOR_PAGADORA"].Visivel = isVisible(Formulario["UOR_PAGADORA"].Valor)
#Formulario["OBS1"].Visivel = isVisible(Formulario["OBS1"].Valor)
#Formulario["OBSERVACAO"].Visivel = isVisible(Formulario["OBSERVACAO"].Valor)
#Formulario["MATRICULA_MOVI"].Visivel = isVisible(Formulario["MATRICULA_MOVI"].Valor)
#Formulario["TE_MATRICULA"].Visivel = isVisible(Formulario["TE_MATRICULA"].Valor)
#Formulario["TE_NOME_EMPREGADO"].Visivel = isVisible(Formulario["TE_NOME_EMPREGADO"].Valor)
#Formulario["VALOR_NOTA"].Visivel = isVisible(Convert.ToString(Formulario["VALOR_NOTA"].Valor))
#Formulario["COMPETENCIA"].Visivel = isVisible(Formulario["COMPETENCIA"].Valor)
#Formulario["FAVORECIDO_COBRA"].Visivel = isVisible(Formulario["FAVORECIDO_COBRA"].Valor)
#Formulario["FAVORECIDO_TODOS"].Visivel = isVisible(Formulario["FAVORECIDO_TODOS"].Valor)
#Formulario["MATRICULA"].Visivel = isVisible(Convert.ToString(Formulario["MATRICULA"].Valor))
#Formulario["DATA_DE_PAGAMENTO"].Visivel = isVisible(Convert.ToString(Formulario["DATA_DE_PAGAMENTO"].Valor))
#Formulario["CONTA_CONTABIL_PAGAMENTO_RCC"].Visivel = isVisible(Formulario["CONTA_CONTABIL_PAGAMENTO_RCC"].Valor)
#Formulario["VALOR_PAGAMENTO_RCC"].Visivel = isVisible(Convert.ToString(Formulario["VALOR_PAGAMENTO_RCC"].Valor))
#Formulario["VALOR_REEMBOLSO"].Visivel = isVisible(Convert.ToString(Formulario["VALOR_REEMBOLSO"].Valor))
#Formulario["MESANOREF"].Visivel = isVisible(Formulario["MESANOREF"].Valor)
#Formulario["VALOR"].Visivel = isVisible(Convert.ToString(Formulario["VALOR"].Valor))
#Formulario["SCR_TODOS_RH"].Visivel = isVisible(Formulario["SCR_TODOS_RH"].Valor)
#Formulario["RCC_TIPO_SOLICITACAO"].Visivel = isVisible(Formulario["RCC_TIPO_SOLICITACAO"].Valor)
#
#
#
##if String.IsNullOrEmpty(Formulario['COMPETENCIA'].Valor.Trim()):
#    Formulario["COMPETENCIA"].Visivel = False 
#    
#if String.IsNullOrEmpty(Formulario["MOTIVO_GERAL"].Valor.Trim()):
#    Formulario["MOTIVO_GERAL"].Visivel = False  
#    

#Formulario["MATRICULA_MOVI"].Visivel = isVisible(Formulario["MATRICULA_MOVI"].Valor)
#
#Formulario["TE_MATRICULA"].Visivel = isVisible(Formulario["TE_MATRICULA"].Valor)
#
#Formulario["TE_NOME_EMPREGADO"].Visivel = isVisible(Formulario["TE_NOME_EMPREGADO"].Valor)
#
#Formulario["UOR_PAGADORA"].Visivel = isVisible(Formulario["UOR_PAGADORA"].Valor)
#
#Formulario["SCR_TODOS_RH"].Visivel = isVisible(Formulario["SCR_TODOS_RH"].Valor)

    
#if String.IsNullOrEmpty(Formulario['CONTA_CONTABIL_PAGAMENTO_RCC'].Valor):
#    Formulario["CONTA_CONTABIL_PAGAMENTO_RCC"].Visivel = False  

#if String.IsNullOrEmpty(Formulario['CSC_BANCO2'].Valor):
#    Formulario["CSC_BANCO2"].Visivel = False   
#    
#if String.IsNullOrEmpty(Formulario['CSC_CONTA_CORRENTE'].Valor):
#    Formulario["CSC_CONTA_CORRENTE"].Visivel = False   
#    
#if String.IsNullOrEmpty(Formulario['CSC_NUMERO'].Valor):
#    Formulario["CSC_NUMERO"].Visivel = False    
#    
#if String.IsNullOrEmpty(Formulario['CSC_NUMERO_AGENCIA'].Valor):
#    Formulario["CSC_NUMERO_AGENCIA"].Visivel = False    
#    
#
#
#    
#    
#if String.IsNullOrEmpty(Formulario['DATA_DE_PAGAMENTO'].Valor):
#    Formulario["DATA_DE_PAGAMENTO"].Visivel = False  
#    
#
#
#
#if String.IsNullOrEmpty(Formulario["FAVORECIDO_COBRA"].Valor.Trim()):
#    Formulario["FAVORECIDO_COBRA"].Valor = "aqui"
#if String.IsNullOrEmpty(Formulario['FAVORECIDO_COBRA'].Valor.Trim()):
#    Formulario["FAVORECIDO_COBRA"].Visivel = False
#    
#
#if String.IsNullOrEmpty(Formulario['FAVORECIDO_TODOS'].Valor):
#    Formulario["FAVORECIDO_TODOS"].Visivel = False
#    
#    
#    
# 
#    
#    
#if String.IsNullOrEmpty(Formulario['MATRICULA'].Valor):
#    Formulario["MATRICULA"].Visivel = False 
#    
#    
#if String.IsNullOrEmpty(Formulario['MATRICULA_MOVI'].Valor):
#    Formulario["MATRICULA_MOVI"].Visivel = False 
#    
#    
#    
#
#
#
#if String.IsNullOrEmpty(Formulario['MESANOREF'].Valor):
#    Formulario["MESANOREF"].Visivel = False 
#    
#if String.IsNullOrEmpty(Formulario['MOTIVO_GERAL'].Valor):
#    Formulario["MOTIVO_GERAL"].Visivel = False 
#
#
#
#    
#if String.IsNullOrEmpty(Formulario['RCC_TIPO_SOLICITACAO'].Valor):
#    Formulario["RCC_TIPO_SOLICITACAO"].Visivel = False  
#
#
#
#
##if String.IsNullOrEmpty(Formulario['SCR'].Valor):
##    Formulario["SCR"].Visivel = False  
#    
#if String.IsNullOrEmpty(Formulario['SCR_TODOS_RH'].Valor):
#    Formulario["SCR_TODOS_RH"].Visivel = False    
#
#
#
#
#if String.IsNullOrEmpty(Formulario['TE_NOME_EMPREGADO'].Valor):
#    Formulario["TE_NOME_EMPREGADO"].Visivel = False
#
#if String.IsNullOrEmpty(Formulario['TE_MATRICULA'].Valor):
#    Formulario["TE_MATRICULA"].Visivel = False
#    
#
#
#
#if String.IsNullOrEmpty(Formulario['UOR_PAGADORA'].Valor):
#    Formulario["UOR_PAGADORA"].Visivel = False
#    
#
#
#    
#if String.IsNullOrEmpty(Formulario['VALOR_NOTA'].Valor): 
#    Formulario['VALOR_NOTA'].Visivel = False
#
#if String.IsNullOrEmpty(Formulario['VALOR'].Valor):
#    Formulario["VALOR"].Visivel = False  
#        
#    
#if String.IsNullOrEmpty(Formulario['VALOR_PAGAMENTO_RCC'].Valor):
#    Formulario["VALOR_PAGAMENTO_RCC"].Visivel = False
#    
#if String.IsNullOrEmpty(Formulario['VALOR_REEMBOLSO'].Valor):
#    Formulario["VALOR_REEMBOLSO"].Visivel = False  
#  
#
#
#
#    
#if String.IsNullOrEmpty(Formulario['OBS1'].Valor):
#    Formulario["OBS1"].Visivel = False
#    
#if String.IsNullOrEmpty(Formulario['OBSERVACAO'].Valor):
#    Formulario["OBSERVACAO"].Visivel = False 
#    
#
#    
#
#    
#
#
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados Bancários
  - CSC_CONTA_CORRENTE "Conta Corrente" [TextBox String → CPE_CSC.CSC_CONTA_CORRENTE]
  - CSC_NUMERO "Número da RCC" [TextBox String(100) → CPE_CSC.CSC_NUMERO]
  - CSC_BANCO2 "Banco" [TextBox String → CPE_CSC.CSC_BANCO2]
  - CSC_NUMERO_AGENCIA "Número da Agência" [TextBox String → CPE_CSC.CSC_NUMERO_AGENCIA]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados
  - NUMERO_ATA "Valor:" [TextBox String → CPE_CONTRATOS02.NUMERO_ATA]
  - OBSERVACAO "Dados da Pessoa" [TextBox String(2000) → CPE_CSC.OBSERVACAO]
  - FAVORECIDO_TODOS "Favorecido:" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
  - OBS1 "Dados do Pagamento" [Memo String(2000) → CPE_CONTRATOS.OBS1]
  - COMPETENCIA "Competência (mês/Ano ex: julho/2020)" [TextBox String → CPE_CSC.COMPETENCIA]
  - VALOR_NOTA "Valor da Nota Fiscal" [TextBox String(13) → CP_ORDEM_SERVICO.VALOR_NOTA]
  - VALOR_PAGAMENTO_RCC "Valor Pagamento RCC" [TextBox Decimal → CPE_CSC.VALOR_PAGAMENTO_RCC] obrigatório
  - MESANOREF "Mês e ano referência" [TextBox String → CPE_CSC.MESANOREF]
  - MOTIVO_GERAL "Motivo Genérico" [TextBox String → CPE_CSC.MOTIVO_GERAL]
  - MATRICULA_MOVI "matricula 123" [TextBox Integer → CP_ORDEM_SERVICO.MATRICULA_MOVI]
  - RCC_TIPO_SOLICITACAO "Tipo de Solicitação" [DropDownList String → CPE_CSC.RCC_TIPO_SOLICITACAO]
  - DATA_DE_PAGAMENTO "Data" [DatePicker DateTime → CPE_CSC.DATA_DE_PAGAMENTO] obrigatório
  - UOR_PAGADORA "UOR Pagadora" [TextBox String → CPE_CSC.UOR_PAGADORA] obrigatório
  - VALOR_REEMBOLSO "Valor do Reembolso" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO] obrigatório
  - TE_NOME_EMPREGADO "Nome" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO]
  - FAVORECIDO_COBRA "Favorecido 7:" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA]
  - SCR "UOR" [DropDownList Integer → CP_ORDEM_SERVICO.SCR]
  - SCR_TODOS_RH "UOR para Debitar" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH]
  - CONTA_CONTABIL_PAGAMENTO_RCC "Conta contabil pagamento RCC" [TextBox String(200) → CPE_CSC.CONTA_CONTABIL_PAGAMENTO_RCC] obrigatório
  - VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório

### [332141] Tarefa "Corrigir informação
"
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptFormCarregado**
```python
Formulario["OBSERVACAO"].Visivel = True
Formulario["OBSERVACAO"].Habilitado = True


Formulario["Justificativa"].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - NUMERO_RI "Número do RI" [TextBox String → CPE_CSC.NUMERO_RI] obrigatório
  - BOLETO "Valor do Boleto" [TextBox String → CPE_CSC.BOLETO] obrigatório
  - DATA_EMISSAO "Data do Lançamento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_EMISSAO] obrigatório

### [332143] Tarefa "Corrigir informação
"
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptFormCarregado**
```python
Formulario["OBSERVACAO"].Visivel = True
Formulario["OBSERVACAO"].Habilitado = True


Formulario["Justificativa"].Habilitado = False
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Campo(s) Passivel(is) de Correção:
  - Justificativa (nativo) "Ajustes Necessários" obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Correção dos Campos Citados Acima:
  - OBSERVACAO "Informe os Dados Corretos" [TextBox String(2000) → CPE_CSC.OBSERVACAO] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Guias de Pagamento — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [332153] Tarefa "Efetuar Pagamento"
Responsável: Responsável atual (papel 36)
Config: Codigo=PAGAMENTO
MotivoInterrupcaoSLA: Aguando data de pagamento
**ScriptFormCarregado**
```python
# SERVIÇOS DESPACHANTES: ================================

#if OrdemServico.Servico.Sigla == 'CONTASPAGAR':
 #   Formulario["GUIASJUDICIAIS"].Visivel = False
    
    

# PROGRAMA ECOA: ========================================

#Formulario["DATA_DE_PAGAMENTO"].Habilitado = True
#Formulario["DATA_DE_PAGAMENTO"].Visivel = True
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Data Que Será Realizado o Pagamento
  - DATA_APROVACAO "Data do Pagamento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_APROVACAO] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados Bancários
  - CSC_NUMERO "Número da RCC" [TextBox String(100) → CPE_CSC.CSC_NUMERO]
  - CSC_BANCO2 "Banco" [TextBox String → CPE_CSC.CSC_BANCO2]
  - CSC_NUMERO_AGENCIA "Número da Agência" [TextBox String → CPE_CSC.CSC_NUMERO_AGENCIA]
  - CSC_CONTA_CORRENTE "Conta Corrente" [TextBox String → CPE_CSC.CSC_CONTA_CORRENTE]
- Operação PR0004 Associar Itens Configuração: Nome=ANEXO_DOIS2
  - anexo "" classes: Arquivo para Jurídico — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração: Nome=ANEXO
  - anexo "Comprovante de Pagamento" classes: Arquivo — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [332155] LinkInicial "Auxilio/Incentivo Adaptação Cedidos BB"
Config: Codigo=AINADAPCEDBB; TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Auxílio Adaptação Cedidos
  - ORDEM_DE_SERVICO "Número da Ordem de Serviço Admissão de Funcionário Cedido" [TextBox String → CPE_CSC.ORDEM_DE_SERVICO]
  - COMBOBOX "Informe a base subdimensionada (deficit de pessoal)?" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX]
  - SIM_NAO1 "O Favorecido faz parte do público alvo para o programa de adequação de quadro da Gered (Mudança para base destacada subdimensionada)?" [DropDownList String → CPE_CSC.SIM_NAO1]
**SIM_NAO1.ScriptModificado**
```python
if Formulario["SIM_NAO1"].Valor == "Sim":
    Formulario["COMBOBOX"].Visivel = True
    Formulario["COMBOBOX"].Itens = "TR-QUIXADA;TR-ALTAMIRA;TR-JI-PARANA;TR-ALMENARA;TR-CALDAS NOVAS;TR-UNAI;TR-JAU;TR-PARAGOMINAS;TR-GUANHAES;TR-DIVINOPOLIS;TR-IRECE;TR-SETE LAGOAS;TR-MARILIA;TR-BOM JESUS DA LAPA;CAT-BAURU;TR-GUARAPUAVA;TR-VITORIA DA CONQUISTA;TR-RIO VERDE;TR-VILHENA;TR-SANTA MARIA;TR-IGUATU;TR-VARGINHA;TR-JUIZ DE FORA;TR-SANTO ANTONIO DE JESUS;TR-PETROLINA;CAT-SAO PAULO PM;CAT-NATAL;CAT-MANAUS;TR-CAMPOS DOS GOYTACAZES;TR-OEIRAS;TR-PARAISO;TR-PARAUAPEBAS;TR-JUNDIAI;TR-BATURITE;TR-ARACATI;TR-COLIDER;TR-VIDEIRA;TR-XINGUARA;TR-ORIXIMINA;TR-BAGE;TR-VILA RICA;TR-CHAPADINHA;TR-ALEGRETE;TR-REDENCAO;TR-MACAPA;CAT-PORTO VELHO;TR-JUINA;TR-PRESIDENTE PRUDENTE;TR-PINHEIRO;TR-CATAGUASES;TR-DOURADOS;TR-BARRA DO GARCAS;TR-GUANAMBI;TR-JARDIM;TR-TEFE;TR-SALGUEIRO;TR-ROSARIO;TR-ARACUAI;TR-PARANAVAI;TR-LIMOEIRO DO NORTE;TR-CIDADE DE GOIAS;TR-CHAPADAO DO SUL;TR-SERRINHA;TR-BACABAL"
    
    
if Formulario["SIM_NAO1"].Valor != "Sim":
    Formulario["COMBOBOX"].Visivel = False
```
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA]
  - FAVORECIDO_TODOS "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
**FAVORECIDO_TODOS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario["FAVORECIDO_TODOS"].Valor != "" and Formulario["FAVORECIDO_TODOS"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_TODOS"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        Formulario["MATRICULA"].Valor = favorecidoCustom["MATRICULA"].ToString()
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Auxílio Adaptação Cedidos
  - CONTA_CONTABIL_PAGAMENTO_RCC "Conta contabil pagamento RCC" [TextBox String(200) → CPE_CSC.CONTA_CONTABIL_PAGAMENTO_RCC]
  - LABEL1 "ATENÇÃO: Para o programa de adequação da Gered considerar 75% do valor do salário do empregado." [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - SIM_NAO1 "O Favorecido faz parte do público alvo para o programa de adequação de quadro da Gered (Mudança para base destacada subdimensionada)?" [DropDownList String → CPE_CSC.SIM_NAO1]
  - LABEL10 "ATENÇÃO: O programa de adequação da Gered será pago por RCC. Não lance no Peoplesoft" [Label String(700) → CPE_PDCI2019.LABEL10]
  - VALOR "Valor R$" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - DATA_DE_PAGAMENTO "Data de pagamento" [DatePicker DateTime → CPE_CSC.DATA_DE_PAGAMENTO]
- Associação de subprocesso: AssociacaoId=901; FraseAssociacao=Auxilio/Incentivo Adaptação Cedidos BB -> Pagamentos por RCC; Nome=AUXILIO/INCENTIVO ADAPTAÇÃO CEDIDOS BB

### [332157] EventoIntermediarioMensagem "Comunicado de Reajuste "
Destinatário: Cliente (papel 18)
ModeloComunicado: Comunicado de Ajuste - Contas a Pagar 
Corpo do comunicado: Prezado(a), 
A ordem de serviço número OrdemServico.Numero foi devolvida para sua caixa para a efetivação de ajuste(s) na(s) informação(ões) conforme abaixo. Caso esses ajuste(s) não seja(m) realizado(s) dentro do prazo de 5 (cinco) dias corridos, o chamado será finalizado automaticamente.
Ajustes:
OrdemServico.Justificativa 
Para efetuar os ajustes 
Link.Edicao.
 Central de Serviços.

### [332159] EventoIntermediarioMensagem "Comunicado Contas a Pagar - Aprovado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Comunicado Contas a Pagar - Aprovado
Corpo do comunicado: Prezado(a), 
O chamado OrdemServico.Assunto - OrdemServico.Numero foi aprovado e o pagamento foi agendado. 
Para maiores informações l Link.Edicao 
Atenciosamente, 
Central de Serviços.
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=2281; ClasseConfiguracao=Comprovante de pagamento
  - ClasseConfiguracaoId=2313; ClasseConfiguracao=RCC

### [332160] Tarefa "Informar Reajustes Necessários"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - Justificativa (nativo) "Ajustes Necessários" obrigatório

### [332161] EventoIntermediarioMensagem "Reprovação por falta de ajustes"
Destinatário: Cliente (papel 18)
ModeloComunicado: Reprovação por falta de ajustes - Contas a Pagar 
Corpo do comunicado: Prezado(a),
A Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto foi reprovada por falta de ajustes e informações do cliente. 
Para maiores informações. 
Link.Consulta. Atenciosamente, Central de Serviços.

### [332162] Tarefa "Aguardar data de pagamento"
Responsável: Responsável atual (papel 36)
MotivoInterrupcaoSLA: Aguando data de pagamento

### [332171] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Operação PR0004 Associar Itens Configuração: Nome=GUIAS DE PAGAMENTOS
  - anexo "Guias de pagamento depósito" classes: Guias de Pagamento — RequeridoInicial=true; PermiteMultiplosItens=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração: Nome=GUIAS DE PAGAMENTOS CUSTAS
  - anexo "Guias de pagamento custas" classes: Guias de Pagamento Custas — RequeridoInicial=true; PermiteMultiplosItens=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Pagamentos Judiciais
  - OUTROS_ASSUNTOS "Outros assuntos" [TextBox String → CPE_CSC.OUTROS_ASSUNTOS]
  - DATA_MEMORANDO "Data memorando" [DatePicker DateTime → CPE_CSC.DATA_MEMORANDO]
  - REF_MEMORANDO "REF" [TextBox String → CPE_CSC.REF_MEMORANDO] obrigatório
  - PROCESSO_MEMORANDO "Processo" [TextBox String → CPE_CSC.PROCESSO_MEMORANDO] obrigatório
  - RECLAMADAS_MEMORANDO "Reclamadas" [TextBox String → CPE_CSC.RECLAMADAS_MEMORANDO] obrigatório
  - DIVISAO_JURIDICA "Informar a Divisão Jurídica aprovadora" [DropDownList String → CPE_CJUR.DIVISAO_JURIDICA] obrigatório
  - VALOR_TOTAL_GUIAS "Pagamentos" [TextBox Decimal → CPE_CSC.VALOR_TOTAL_GUIAS] obrigatório
  - GUIASJUDICIAIS "Guias de pagamento" [DataGrid RecordList → Z_00143_GUIASJUDICIAIS.GUIASJUDICIAIS] obrigatório
    - coluna CUSTASDEPOSITO obrigatório
    - coluna VALOR obrigatório
    - coluna PRAZO_FATAL obrigatório
    - coluna NUMERO_RI obrigatório
    - coluna DATA_PAGAMENTO
    - coluna NATUREZA obrigatório
    - coluna TIPO_DOCUMENTO obrigatório
  - DATA_VENCIMENTO "Data Solicitação de Pagamento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO] obrigatório
  - DATA_DO_EXTRATO "Data do Extrato" [DatePicker DateTime → CPE_CSC.DATA_DO_EXTRATO] obrigatório
- Associação de subprocesso: AssociacaoId=532; FraseAssociacao=Solicitar Pagamentos Judiciais -> Financeiro - Contas a Pagar; Nome=SOLICITAR_PAGAMENTO_JURIDICO

### [332172] EventoIntermediarioMensagem "Reprovação por falta de ajustes"
Destinatário: Cliente (papel 18)
ModeloComunicado: Reprovação por falta de ajustes - Contas a Pagar 
Corpo do comunicado: Prezado(a),
A Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto foi reprovada por falta de ajustes e informações do cliente. 
Para maiores informações. 
Link.Consulta. Atenciosamente, Central de Serviços.

### [332158] EventoFinal ""
Responsável: Responsável atual (papel 36)

### [332163] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - DATA_DE_PAGAMENTO "Data Prevista do Pagamento" [DatePicker DateTime → CPE_CSC.DATA_DE_PAGAMENTO] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=ANEXO DE EXPORTAÇÃO; Configuracao={"FiltroArea":true}
  - anexo "Arquivo N para pagamento" classes: Anexo — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Auxílio Funeral
  - NOME_BENEFICIARIO "Nome Completo do(a) Benefíciário(a) - (Quem irá receber o auxílio funeral)" [TextBox String(1000) → CPE_CSC.NOME_BENEFICIARIO] obrigatório
  - DESC_COLABORADOR "SCR / Descrição/ Localidade" [DropDownList String → CP_ORDEM_SERVICO.DESC_COLABORADOR]
  - DESCRICAO_OBRIG "Descrição Detalhada" [TextBox String(2000) → CP_ORDEM_SERVICO.DESCRICAO_OBRIG] obrigatório
  - VALOR_REEMBOLSO "Valor do Reembolso" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO] obrigatório
- Associação de subprocesso: AssociacaoId=623; FraseAssociacao=Auxilio Funeral Lidi -> Financeiro - Contas a Pagar; Nome=AUXILIO FUNERAL

### [332164] FimCancelamento ""

### [332165] FimCancelamento ""

### [332166] Tarefa "Informar Reajustes Necessários"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - Justificativa (nativo) "Ajustes Necessários" obrigatório

### [332167] EventoIntermediarioMensagem "Comunicado de Reajuste "
Destinatário: Cliente (papel 18)
ModeloComunicado: Comunicado de Ajuste - Contas a Pagar 
Corpo do comunicado: Prezado(a), 
A ordem de serviço número OrdemServico.Numero foi devolvida para sua caixa para a efetivação de ajuste(s) na(s) informação(ões) conforme abaixo. Caso esses ajuste(s) não seja(m) realizado(s) dentro do prazo de 5 (cinco) dias corridos, o chamado será finalizado automaticamente.
Ajustes:
OrdemServico.Justificativa 
Para efetuar os ajustes 
Link.Edicao.
 Central de Serviços.

### [332168] FimCancelamento ""

### [332188] LinkInicial "Serviços Despachantes - Estabelecimento"
Config: TipoMensagem=MensagemProcesso
**ScriptFormCarregado**
```python
Formulario["LABEL1"].Valor = '<html><head><link rel="icon" type="image/x-icon" href=""><style>.forma {text-shadow: 2px 2px #e9f507;}</style></head><body><div class="forma"><justify><font color="#1f05b3" size="3"><p><font size="6"><i class="fa fa-cogs fa-fw"></i></font>&nbsp;&nbsp;<b>Informações necessárias para o atendimento da Ordem de Serviço.</div></b></p><b>Caro solicitante,</b><br>Anexar o boleto assinado, <i>conforme a NI 212</i> e clicar no botão <b>Iniciar</b></font></justify><br></body></html>'
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Serviços Despachantes
  - FORNECEDOR "Nome do Formecedor" [TextBox String → CP_ORDEM_SERVICO.FORNECEDOR] obrigatório
  - CSC_DATA_FIM "Data de Pagamento" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM] obrigatório
  - NUMERO_RI "Numero RI" [TextBox String → CPE_CSC.NUMERO_RI] obrigatório
  - CSC_VALOR "Valor" [TextBox String → CPE_CSC.CSC_VALOR] obrigatório
  - LABEL1 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=BOLETOANEXOS
  - anexo "Boleto assinado conforme NI 212" classes: Aquivos 3 — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Associação de subprocesso: AssociacaoId=922; FraseAssociacao=A: CONTAS A PAGAR B DESPACHANTES ESTABELECIMENTO; Nome=A: CONTAS A PAGAR B DESPACHANTES ESTABELECIMENTO

### [332144] FimCancelamento ""

### [332189] Tarefa "Verificar Solicitação
"
Responsável: Fila CSC - Pagamentos (papel 705)
Config: ConfirmaResponsabilidade=true

### [332190] EventoIntermediarioTimer ""
Config: TempoIntervalo=7200; MaximoExecucao=1
**ScriptEvento**
```python
OrdemServico.AvancaAtividade()
```

### [332191] EventoIntermediarioMensagem "Comunicado de Ajuste "
Destinatário: Cliente (papel 18)
ModeloComunicado: Comunicado de Ajuste - Contas a Pagar 
Corpo do comunicado: Prezado(a), 
A ordem de serviço número OrdemServico.Numero foi devolvida para sua caixa para a efetivação de ajuste(s) na(s) informação(ões) conforme abaixo. Caso esses ajuste(s) não seja(m) realizado(s) dentro do prazo de 5 (cinco) dias corridos, o chamado será finalizado automaticamente.
Ajustes:
OrdemServico.Justificativa 
Para efetuar os ajustes 
Link.Edicao.
 Central de Serviços.

### [332192] Tarefa "Verificar Solicitação
"
Responsável: Fila CSC - Pagamentos (papel 705)
Config: ConfirmaResponsabilidade=true

### [332193] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos: RotuloPreenchimento=PDPEP
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO] obrigatório
  - NUMERO_RI "Numero RI" [TextBox String → CPE_CSC.NUMERO_RI] obrigatório
  - NATUREZA_SERV "Natureza do serviço" [DropDownList String → CP_ORDEM_SERVICO.NATUREZA_SERV] obrigatório
  - QUANTIDADE "Quantidade" [TextBox Integer → CP_ORDEM_SERVICO.QUANTIDADE] obrigatório
  - VALOR_DA_NOTA_FISCAL "Número(s) da(s) Nota(s) e Valor(es) da(s) Nota(s)" [DataGrid RecordList → Z_00143_VALOR_DA_NOTA_FISCAL.VALOR_DA_NOTA_FISCAL] obrigatório — QtdColunasFormulario=1
    - coluna DATA_DE_REGISTRO obrigatório
    - coluna ORGANIZACAO
    - coluna NUMERO_OC obrigatório
    - coluna NUMERO_LINHAS obrigatório
    - coluna NOME_ARQUIVO obrigatório
    - coluna NUMERO_DO_DOCUMENTO obrigatório
    - coluna VALOR_DO_DOCUMENTO obrigatório
    - coluna CONDICAO_DE_PGTO
    - coluna DATA_DE_VENCIMENTO_NO_RI
    - coluna CONDICAO_DE_PAGAMENTO
    - coluna NUMERO_NOTA_SERVICO obrigatório
    - coluna NUM_ITEM
    - coluna DATA_PGTO
    - coluna MULTA obrigatório
    - coluna DATA_DE_REGISTRO_NO_RI
    - coluna VALOR_NOTA_FISCAL_SERVICO obrigatório
  - DATA_EMISSAO "Data da Emissão" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_EMISSAO] obrigatório
  - DATA_VENCIMENTO "Data do Vencimento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO] obrigatório
  - CONTA_CONTABIL1 "Conta Contabil" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1] obrigatório
  - DESCRICAO_DETALHADA "Descrição detalhada" [Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Nota Fiscal/Recibo" classes: Nota Fiscal — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração: Nome=NFADITAMENTO3455
  - anexo "Nota Fiscal do Adiantamento" classes: Modelo — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Associação de subprocesso: AssociacaoId=719; FraseAssociacao=PDPEP - Pequenas Despesas de Pronta Entrega e Pagamento -> Financeiro - Contas a Pagar; Nome=PDPEPAG

### [332194] Tarefa "Informar Reajustes Necessários"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - Justificativa (nativo) "Ajustes Necessários" obrigatório

### [332187] Tarefa "Corrigir informação
"
Responsável: Responsável pelo início do subprocesso (papel 79)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
**ScriptFormCarregado**
```python
#Formulario["OBS1"].Visivel = True
#Formulario["OBS1"].Habilitado = True

#Formulario["OBSERVACAO"].Visivel = True
#Formulario["OBSERVACAO"].Habilitado = True


Formulario["Justificativa"].Habilitado = False
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informe os Campos Corretos Listados Acima:
  - OBSERVACAO "Dados da Pessoa" [TextBox String(2000) → CPE_CSC.OBSERVACAO]
  - OBS1 "Dados do Pagamento" [Memo String(2000) → CPE_CONTRATOS.OBS1]
  - COMPETENCIA "Competência (mês/Ano ex: julho/2020)" [TextBox String → CPE_CSC.COMPETENCIA]
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Anexo — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Campo(s) Passivel(is) de Correção:
  - Justificativa (nativo) "Ajustes Necessários" obrigatório

### [332145] Tarefa "Informar Reajustes Necessários"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - Justificativa (nativo) "Ajustes Necessários" obrigatório

### [332146] EventoIntermediarioMensagem "Comunicado de Reajuste "
Destinatário: Cliente (papel 18)
ModeloComunicado: Comunicado de Ajuste - Contas a Pagar 
Corpo do comunicado: Prezado(a), 
A ordem de serviço número OrdemServico.Numero foi devolvida para sua caixa para a efetivação de ajuste(s) na(s) informação(ões) conforme abaixo. Caso esses ajuste(s) não seja(m) realizado(s) dentro do prazo de 5 (cinco) dias corridos, o chamado será finalizado automaticamente.
Ajustes:
OrdemServico.Justificativa 
Para efetuar os ajustes 
Link.Edicao.
 Central de Serviços.

### [332147] Tarefa "Corrigir informação
"
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptFormCarregado**
```python
Formulario["OBSERVACAO"].Visivel = True
Formulario["OBSERVACAO"].Habilitado = True


Formulario["Justificativa"].Habilitado = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Guias de Pagamento — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Campo(s) Passivel(is) de Correção:
  - Justificativa (nativo) "Ajustes Necessários" obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Correção dos Campos Citados Acima:
  - OBSERVACAO "Informe os Dados Corretos" [TextBox String(2000) → CPE_CSC.OBSERVACAO] obrigatório

### [332148] EventoFinal ""
Responsável: Responsável atual (papel 36)

### [332149] EventoIntermediarioMensagem "Comunicado de Reajuste "
Destinatário: Cliente (papel 18)
ModeloComunicado: Comunicado de Ajuste - Contas a Pagar 
Corpo do comunicado: Prezado(a), 
A ordem de serviço número OrdemServico.Numero foi devolvida para sua caixa para a efetivação de ajuste(s) na(s) informação(ões) conforme abaixo. Caso esses ajuste(s) não seja(m) realizado(s) dentro do prazo de 5 (cinco) dias corridos, o chamado será finalizado automaticamente.
Ajustes:
OrdemServico.Justificativa 
Para efetuar os ajustes 
Link.Edicao.
 Central de Serviços.

### [332150] Tarefa "Corrigir a informação
"
Responsável: Cliente (papel 18)
**ScriptFormCarregado**
```python
Formulario["OBSERVACAO"].Visivel = True
Formulario["OBSERVACAO"].Habilitado = True


Formulario["Justificativa"].Habilitado = False
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Correção dos Campos Citados Acima:
  - OBSERVACAO "Informe os Dados Corretos" [TextBox String(2000) → CPE_CSC.OBSERVACAO] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Campo(s) Passivel(is) de Correção:
  - Justificativa (nativo) "Ajustes Necessários" obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Guias de Pagamento — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [332151] EventoIntermediarioMensagem "Reprovação por falta de ajustes"
Destinatário: Cliente (papel 18)
ModeloComunicado: Reprovação por falta de ajustes - Contas a Pagar 
Corpo do comunicado: Prezado(a),
A Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto foi reprovada por falta de ajustes e informações do cliente. 
Para maiores informações. 
Link.Consulta. Atenciosamente, Central de Serviços.

### [332152] EventoIntermediarioMensagem "Comunicado Contas a Pagar - Aprovado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Comunicado Contas a Pagar - Aprovado
Corpo do comunicado: Prezado(a), 
O chamado OrdemServico.Assunto - OrdemServico.Numero foi aprovado e o pagamento foi agendado. 
Para maiores informações l Link.Edicao 
Atenciosamente, 
Central de Serviços.
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=2281; ClasseConfiguracao=Comprovante de pagamento
  - ClasseConfiguracaoId=2313; ClasseConfiguracao=RCC

### [332185] EventoIntermediarioTimer ""
Config: TempoIntervalo=7200; MaximoExecucao=1
**ScriptEvento**
```python
OrdemServico.AvancaAtividade()
```

### [332186] Tarefa "Corrigir informação
"
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptFormCarregado**
```python
Formulario["OBSERVACAO"].Visivel = True
Formulario["OBSERVACAO"].Habilitado = True


Formulario["Justificativa"].Habilitado = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Nota Fiscal/Recibo" classes: Nota Fiscal — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos
  - NATUREZA_SERV "Natureza do serviço" [DropDownList String → CP_ORDEM_SERVICO.NATUREZA_SERV] obrigatório
  - QUANTIDADE "Quantidade" [TextBox Integer → CP_ORDEM_SERVICO.QUANTIDADE] obrigatório
  - VALOR_DA_NOTA_FISCAL "Número(s) da(s) Nota(s) e Valor(es) da(s) Nota(s)" [DataGrid RecordList → Z_00143_VALOR_DA_NOTA_FISCAL.VALOR_DA_NOTA_FISCAL] obrigatório — QtdColunasFormulario=1
    - coluna MULTA obrigatório
    - coluna ORGANIZACAO
    - coluna NOME_ARQUIVO obrigatório
    - coluna DATA_DE_REGISTRO_NO_RI
    - coluna NUMERO_OC obrigatório
    - coluna NUMERO_LINHAS obrigatório
    - coluna NUMERO_DO_DOCUMENTO obrigatório
    - coluna VALOR_DO_DOCUMENTO obrigatório
    - coluna CONDICAO_DE_PGTO
    - coluna VALOR_NOTA_FISCAL_SERVICO obrigatório
    - coluna DATA_DE_REGISTRO obrigatório
    - coluna DATA_DE_VENCIMENTO_NO_RI
    - coluna CONDICAO_DE_PAGAMENTO
    - coluna NUMERO_NOTA_SERVICO obrigatório
    - coluna NUM_ITEM
    - coluna DATA_PGTO
  - DATA_EMISSAO "Data da Emissão" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_EMISSAO] obrigatório
  - DATA_VENCIMENTO "Data do Vencimento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO] obrigatório
  - CONTA_CONTABIL1 "Conta Contabil" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1] obrigatório
  - DESCRICAO_DETALHADA "Descrição detalhada" [Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=NFADITAMENTO34
  - anexo "Nota Fiscal do Adiantamento" classes: Modelo — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [332132] Tarefa "Verificar Solicitação
"
Responsável: Fila CSC - Pagamentos (papel 705)
Config: ConfirmaResponsabilidade=true
- Operação PR0001 Preencher Campos
  - DATA_VENCIMENTO "Data Solicitação de pagamento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO] obrigatório
  - DATA_DO_EXTRATO "Data Limite para Retorno ao Jurídico da Guia de Pagamento" [DatePicker DateTime → CPE_CSC.DATA_DO_EXTRATO] obrigatório
- Relatorios:
  - FormatoExportacao=PDF

### [332133] EventoIntermediarioMensagem "Comunicado de Ajuste "
Destinatário: Cliente (papel 18)
ModeloComunicado: Comunicado de Ajuste - Contas a Pagar 
Corpo do comunicado: Prezado(a), 
A ordem de serviço número OrdemServico.Numero foi devolvida para sua caixa para a efetivação de ajuste(s) na(s) informação(ões) conforme abaixo. Caso esses ajuste(s) não seja(m) realizado(s) dentro do prazo de 5 (cinco) dias corridos, o chamado será finalizado automaticamente.
Ajustes:
OrdemServico.Justificativa 
Para efetuar os ajustes 
Link.Edicao.
 Central de Serviços.

### [332134] Tarefa "Verificar Solicitação
"
Responsável: Fila CSC - Pagamentos (papel 705)
Config: ConfirmaResponsabilidade=true
- Relatorios:
  - FormatoExportacao=PDF

### [332135] Tarefa "Verificar Solicitação
"
Responsável: Fila CSC - Pagamentos (papel 705)
Config: ConfirmaResponsabilidade=true

### [332136] EventoIntermediarioMensagem "Reprovação por falta de ajustes"
Destinatário: Cliente (papel 18)
ModeloComunicado: Reprovação por falta de ajustes - Contas a Pagar 
Corpo do comunicado: Prezado(a),
A Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto foi reprovada por falta de ajustes e informações do cliente. 
Para maiores informações. 
Link.Consulta. Atenciosamente, Central de Serviços.

### [332137] EventoIntermediarioMensagem "Reprovação por falta de ajustes"
Destinatário: Cliente (papel 18)
ModeloComunicado: Reprovação por falta de ajustes - Contas a Pagar 
Corpo do comunicado: Prezado(a),
A Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto foi reprovada por falta de ajustes e informações do cliente. 
Para maiores informações. 
Link.Consulta. Atenciosamente, Central de Serviços.

### [332138] FimCancelamento ""

### [332140] EventoIntermediarioMensagem "Comunicado de Ajuste "
Destinatário: Cliente (papel 18)
ModeloComunicado: Comunicado de Ajuste - Contas a Pagar 
Corpo do comunicado: Prezado(a), 
A ordem de serviço número OrdemServico.Numero foi devolvida para sua caixa para a efetivação de ajuste(s) na(s) informação(ões) conforme abaixo. Caso esses ajuste(s) não seja(m) realizado(s) dentro do prazo de 5 (cinco) dias corridos, o chamado será finalizado automaticamente.
Ajustes:
OrdemServico.Justificativa 
Para efetuar os ajustes 
Link.Edicao.
 Central de Serviços.

### [359524] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
**ScriptFormCarregado**
```python
campos = ["COMPETENCIA","CPF","CSC_BAIRRO","CSC_BANCO2","CSC_CONTA_CORRENTE","CSC_CPF","CSC_NUMERO","CSC_NUMERO_AGENCIA","DESCRICAO_OBRIG","FAVORECIDO_COBRA","FAVORECIDO_TODOS","MATRICULA","RCC_TIPO_SOLICITACAO","SCR_TODOS_RH","Solução","VALOR","VALOR_REEMBOLSO"]

for campo in campos:
    try:
        valor = Formulario[campo].Valor
        if valor == "" or valor == None:
            Formulario[campo].Visivel = False
            Formulario[campo].Habilitado = False
        else:
            Formulario[campo].Visivel = True
            Formulario[campo].Habilitado = True
    except Exception:
        # Campo não existe ou erro ignorado
        pass

#if String.IsNullOrEmpty(Formulario['COMPETENCIA'].Valor.Trim()):
#    Formulario["COMPETENCIA"].Visivel = False 
#    
#if String.IsNullOrEmpty(Formulario["MOTIVO_GERAL"].Valor.Trim()):
#    Formulario["MOTIVO_GERAL"].Visivel = False  
#    
#
#Formulario["MATRICULA_MOVI"].Visivel = isVisible(Formulario["MATRICULA_MOVI"].Valor)
#
#Formulario["TE_MATRICULA"].Visivel = isVisible(Formulario["TE_MATRICULA"].Valor)
#
#Formulario["TE_NOME_EMPREGADO"].Visivel = isVisible(Formulario["TE_NOME_EMPREGADO"].Valor)
#
#Formulario["UOR_PAGADORA"].Visivel = isVisible(Formulario["UOR_PAGADORA"].Valor)
#
#Formulario["SCR_TODOS_RH"].Visivel = isVisible(Formulario["SCR_TODOS_RH"].Valor)
#
#    
#if String.IsNullOrEmpty(Formulario['CONTA_CONTABIL_PAGAMENTO_RCC'].Valor):
#    Formulario["CONTA_CONTABIL_PAGAMENTO_RCC"].Visivel = False  
#
#if String.IsNullOrEmpty(Formulario['CSC_BANCO2'].Valor):
#    Formulario["CSC_BANCO2"].Visivel = False   
#    
#if String.IsNullOrEmpty(Formulario['CSC_CONTA_CORRENTE'].Valor):
#    Formulario["CSC_CONTA_CORRENTE"].Visivel = False   
#    
#if String.IsNullOrEmpty(Formulario['CSC_NUMERO'].Valor):
#    Formulario["CSC_NUMERO"].Visivel = False    
#    
#if String.IsNullOrEmpty(Formulario['CSC_NUMERO_AGENCIA'].Valor):
#    Formulario["CSC_NUMERO_AGENCIA"].Visivel = False    
#    
#
#
#    
#    
#if String.IsNullOrEmpty(Formulario['DATA_DE_PAGAMENTO'].Valor):
#    Formulario["DATA_DE_PAGAMENTO"].Visivel = False  
#    
#
#
#
#if String.IsNullOrEmpty(Formulario["FAVORECIDO_COBRA"].Valor.Trim()):
#    Formulario["FAVORECIDO_COBRA"].Valor = "aqui"
#if String.IsNullOrEmpty(Formulario['FAVORECIDO_COBRA'].Valor.Trim()):
#    Formulario["FAVORECIDO_COBRA"].Visivel = False
#    
#
#if String.IsNullOrEmpty(Formulario['FAVORECIDO_TODOS'].Valor):
#    Formulario["FAVORECIDO_TODOS"].Visivel = False
#    
#    
#    
# 
#    
#    
#if String.IsNullOrEmpty(Formulario['MATRICULA'].Valor):
#    Formulario["MATRICULA"].Visivel = False 
#    
#    
#if String.IsNullOrEmpty(Formulario['MATRICULA_MOVI'].Valor):
#    Formulario["MATRICULA_MOVI"].Visivel = False 
#    
#    
#    
#
#
#
#if String.IsNullOrEmpty(Formulario['MESANOREF'].Valor):
#    Formulario["MESANOREF"].Visivel = False 
#    
#if String.IsNullOrEmpty(Formulario['MOTIVO_GERAL'].Valor):
#    Formulario["MOTIVO_GERAL"].Visivel = False 
#
#
#
#    
#if String.IsNullOrEmpty(Formulario['RCC_TIPO_SOLICITACAO'].Valor):
#    Formulario["RCC_TIPO_SOLICITACAO"].Visivel = False  
#
#
#
#
##if String.IsNullOrEmpty(Formulario['SCR'].Valor):
##    Formulario["SCR"].Visivel = False  
#    
#if String.IsNullOrEmpty(Formulario['SCR_TODOS_RH'].Valor):
#    Formulario["SCR_TODOS_RH"].Visivel = False    
#
#
#
#
#if String.IsNullOrEmpty(Formulario['TE_NOME_EMPREGADO'].Valor):
#    Formulario["TE_NOME_EMPREGADO"].Visivel = False
#
#if String.IsNullOrEmpty(Formulario['TE_MATRICULA'].Valor):
#    Formulario["TE_MATRICULA"].Visivel = False
#    
#
#
#
#if String.IsNullOrEmpty(Formulario['UOR_PAGADORA'].Valor):
#    Formulario["UOR_PAGADORA"].Visivel = False
#    
#
#
#    
#if String.IsNullOrEmpty(Formulario['VALOR_NOTA'].Valor): 
#    Formulario['VALOR_NOTA'].Visivel = False
#
#if String.IsNullOrEmpty(Formulario['VALOR'].Valor):
#    Formulario["VALOR"].Visivel = False  
#        
#    
#if String.IsNullOrEmpty(Formulario['VALOR_PAGAMENTO_RCC'].Valor):
#    Formulario["VALOR_PAGAMENTO_RCC"].Visivel = False
#    
#if String.IsNullOrEmpty(Formulario['VALOR_REEMBOLSO'].Valor):
#    Formulario["VALOR_REEMBOLSO"].Visivel = False  
#  
#
#
#
#    
#if String.IsNullOrEmpty(Formulario['OBS1'].Valor):
#    Formulario["OBS1"].Visivel = False
#    
#if String.IsNullOrEmpty(Formulario['OBSERVACAO'].Valor):
#    Formulario["OBSERVACAO"].Visivel = False 
#    
#
#    
#
#    
#
#
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Efetuar Pagamento
  - RCC_TIPO_SOLICITACAO "Vínculo do funcionário falecido" [DropDownList String → CPE_CSC.RCC_TIPO_SOLICITACAO]
  - CSC_NUMERO "Número da RCC" [TextBox String(100) → CPE_CSC.CSC_NUMERO]
  - FAVORECIDO_TODOS "Gestor que irá receber o reembolso (mesmo nome que aparece na nota fiscal):" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
  - MATRICULA "Matrícula do Gestor" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA]
  - CPF "CPF do Gestor que irá receber o reembolso" [TextBox String(15) → CP_ORDEM_SERVICO.CPF]
  - CSC_BANCO2 "Banco" [TextBox String → CPE_CSC.CSC_BANCO2]
  - CSC_NUMERO_AGENCIA "Número da Agência" [TextBox String → CPE_CSC.CSC_NUMERO_AGENCIA]
  - CSC_CONTA_CORRENTE "Conta Corrente" [TextBox String → CPE_CSC.CSC_CONTA_CORRENTE]
  - SCR_TODOS_RH "UOR para Debitar" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH]
  - CSC_BAIRRO "Conta Contábil" [TextBox String(500) → CPE_CSC.CSC_BAIRRO]
  - COMPETENCIA "Competência (mês/Ano ex: julho/2020)" [TextBox String → CPE_CSC.COMPETENCIA]
  - FAVORECIDO_COBRA "Funcionário(a) Falecido(a)" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
  - CSC_CPF "CPF do(a) Falecido(a)" [TextBox String(300) → CPE_CSC.CSC_CPF]
  - VALOR "Valor R$:" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - VALOR_REEMBOLSO "Valor total do Reembolso (Não pode ultrapassar R$4000):" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO]
  - DESCRICAO_OBRIG "Descrição detalhada" [TextBox String(2000) → CP_ORDEM_SERVICO.DESCRICAO_OBRIG]
  - Solucao (nativo)
**Solucao.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla","CONTASAPAGAR")
```
  - NUMERO_ATA "Valor:" [TextBox String → CPE_CONTRATOS02.NUMERO_ATA]
- Operação PR0004 Associar Itens Configuração
  - anexo "Notas Fiscais" classes: Nota Fiscal — RequeridoInicial=true; PermiteMultiplosItens=true
- Associação de subprocesso: AssociacaoId=530; FraseAssociacao=Executar pagamento por RCC -> Financeiro -  Contas a Pagar; Nome=ASSOCIACAO_PAGAMENTO_RCC

### [359525] EventoIntermediarioMensagem "Aviso da Abertura da OS"
Destinatário: Cliente (papel 18)
ModeloComunicado: Comunicado Contas a Pagar - Boleto Previdência Privada
Corpo do comunicado: Prezado(a),
Consta Ordem de Serviço para para Boleto Previdência Privada:
 Nº de RI: OrdemServico.Customizado.CSC_NUMERO 
Para acessar a solicitação OrdemServico.Numero - OrdemServico.Assunto acesse o link Link.Workspace .
Atenciosamente,
Central de Serviços

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
### papel 705: Fila CSC - Pagamentos
Tipo=RelacaoPessoas | pessoas: Fila CSC - Pagamentos
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 79: Responsável pelo início do subprocesso
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Processo.Custom import Ator
from Venki.Services.Dictionary.Custom import Class
Atores.Adiciona(OrdemServico.ClasseSubProcesso.Responsavel,"Cadastrado como responsável na Classe de Sub-processo")
```

## Campos customizados usados (definição global)

### NUMERO_RI — Numero RI
TextBox String → CPE_CSC.NUMERO_RI

### BOLETO — Numero do Boleto
TextBox String → CPE_CSC.BOLETO

### DATA_EMISSAO — Data da Emissão
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_EMISSAO

### SIM_NAO1 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO1
Itens: Sim;Não

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX
Itens: Órtese;Órtese Dentária; Prótese;Recurso para Saúde

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### MATRICULA — Matrícula
TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA

### ORDEM_DE_SERVICO — Ordem de Serviço
TextBox String → CPE_CSC.ORDEM_DE_SERVICO

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### LABEL10 — LABEL10
Label String(700) → CPE_PDCI2019.LABEL10

### VALOR — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR
Descrição: Informe

### DATA_DE_PAGAMENTO — Data de pagamento
DatePicker DateTime → CPE_CSC.DATA_DE_PAGAMENTO

### CONTA_CONTABIL_PAGAMENTO_RCC — Conta contabil pagamento RCC
TextBox String(200) → CPE_CSC.CONTA_CONTABIL_PAGAMENTO_RCC

### CHAVE_CONTABIL — Chave Contábil
TextBox String → CPE_FINANCEIRO.CHAVE_CONTABIL

### UOR5 — UOR
TextBox String → CPE_FINANCEIRO.UOR5

### CONTA_CONTABIL4 — Conta Contábil
TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL4

### VALOR_DOD — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD
Descrição: Valor do orçamento

### COMBOBOX1 — Chamado Aberto?
DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1

### DADOS_DE_PAGAMENTO — Dados de Pagamento
DataGrid RecordList → Z_00143_DADOS_DE_PAGAMENTO.DADOS_DE_PAGAMENTO
Colunas do registro:
- CONTA "Conta" [TextBox String]
- CPF "CPF" [TextBox String]
- BANCO "Banco" [TextBox String]
- CHAVE_PIX "Chave PIX" [TextBox String]
- AGENCIA "Agência" [TextBox String]

### CSC_CEP — CEP
TextBox String → CPE_CSC.CSC_CEP

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### SCR_PRESTADOR — UOR
TextBox String → CP_ORDEM_SERVICO.SCR_PRESTADOR
Descrição: UOR onde está lotado o prestador de serviço

### PIX_NUMERO — Número do PIX
TextBox String → CPE_CSC.PIX_NUMERO

### DATA_VENCIMENTO — Data do Vencimento
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO

### DATA_DO_EXTRATO — Data do Extrato
DatePicker DateTime → CPE_CSC.DATA_DO_EXTRATO

### GUIASJUDICIAIS — Guias de pagamento
DataGrid RecordList → Z_00143_GUIASJUDICIAIS.GUIASJUDICIAIS
Descrição: Valor e prazo para pagamento de guias judiciais
Colunas do registro:
- CUSTASDEPOSITO "Custas ou Depósito?" [DropDownList String] itens: Custas;
Depósito
- VALOR "Valor R$" [TextBox Decimal]
- PRAZO_FATAL "Prazo" [DatePicker DateTime]
- NUMERO_RI "Número do RI" [TextBox Integer]
- DATA_PAGAMENTO "Data do Pagamento" [DatePicker DateTime]
- NATUREZA "Natureza do Pagamento" [DropDownList String] itens: CUSTAS;HONORARIO;DEPÓSITO RR;DEPÓSITO RO;DEPÓSITO AIRR;PAGAMENTO;GARANTIA DA EXECUÇÃO;TUTELA ANTECIPADA;BLOQUEIO CONTA CORRENTE;ALVARÁ JUDICIAL;DEPÓSITO JUDICIAL;PAGAMENTO INSS;PAGAMENTO IRRF;DIFERENÇA REMANESCENTE DA EXECUÇÃO;PAGAMENTO ACORDO
- TIPO_DOCUMENTO "Tipo do Documento" [DropDownList String] itens: ACORDÃO TRT;NOTIFICAÇÃO;INTIMAÇÃO;DEPÓSITO RECURSAL/JUDICIAL;CONTESTAÇÃO;INICIAL PROCESSO;ALVARÁ DE LEVANTAMENTO;ACORDÃO TST;SENTENÇA;DESPACHO;ACORDO;ANÁLISE DE RISCO;ATA DE AUDIÊNCIA;EMBARGOS DE DECLARAÇÃO;RAZÕES FINAIS;IMPUGNAÇÃO;LAUDOS PERICIAIS;RECURSO DE REVISTA;RECURSO EXTRAORDINÁRIO;AGRAVO DE…

### OBSERVACAO — .
TextBox String(2000) → CPE_CSC.OBSERVACAO
Descrição: Observação

### CSC_CONTA_CORRENTE — Conta Corrente
TextBox String → CPE_CSC.CSC_CONTA_CORRENTE

### CSC_NUMERO — Número
TextBox String(100) → CPE_CSC.CSC_NUMERO

### CSC_BANCO2 — Banco
TextBox String → CPE_CSC.CSC_BANCO2

### CSC_NUMERO_AGENCIA — Número da Agência
TextBox String → CPE_CSC.CSC_NUMERO_AGENCIA

### NUMERO_ATA — Número da ATA
TextBox String → CPE_CONTRATOS02.NUMERO_ATA

### OBS1 — Observação1
Memo String(2000) → CPE_CONTRATOS.OBS1
Descrição: Informe

### COMPETENCIA — Competência (mês/Ano ex: julho/2020)
TextBox String → CPE_CSC.COMPETENCIA
Descrição: Competência

### VALOR_NOTA — Valor da Nota Fiscal
TextBox String(13) → CP_ORDEM_SERVICO.VALOR_NOTA

### VALOR_PAGAMENTO_RCC — Valor Pagamento RCC
TextBox Decimal → CPE_CSC.VALOR_PAGAMENTO_RCC

### MESANOREF — Mês e ano referência
TextBox String → CPE_CSC.MESANOREF

### MOTIVO_GERAL — Motivo Genérico
TextBox String → CPE_CSC.MOTIVO_GERAL

### MATRICULA_MOVI — Matrícula
TextBox Integer → CP_ORDEM_SERVICO.MATRICULA_MOVI

### RCC_TIPO_SOLICITACAO — Tipo de Solicitação
DropDownList String → CPE_CSC.RCC_TIPO_SOLICITACAO
Itens: Funcionário Ativo;Funcionário Inativo;Pensionista;Outros

### UOR_PAGADORA — UOR Pagadora
TextBox String → CPE_CSC.UOR_PAGADORA

### VALOR_REEMBOLSO — Valor do Reembolso
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO

### TE_NOME_EMPREGADO — Nome do empregado
DropDownList String → CPE_CSC.TE_NOME_EMPREGADO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### SCR — UOR
DropDownList Integer → CP_ORDEM_SERVICO.SCR
Descrição: SCR

### SCR_TODOS_RH — UOR Movimentação
DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH
Descrição: SCR Movimentação
**LookupScript**
```python
###PGESV###
Itens = DB.ExecuteDataTable("SELECT to_char(SCR) as SCR, NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO");
```

### DATA_APROVACAO — Data da Aprovação
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_APROVACAO

### OUTROS_ASSUNTOS — Outros assuntos
TextBox String → CPE_CSC.OUTROS_ASSUNTOS
Descrição: Outros assuntos juridicos

### DATA_MEMORANDO — Data memorando
DatePicker DateTime → CPE_CSC.DATA_MEMORANDO

### REF_MEMORANDO — REF memorando
TextBox String → CPE_CSC.REF_MEMORANDO

### PROCESSO_MEMORANDO — Processo Memorando
TextBox String → CPE_CSC.PROCESSO_MEMORANDO
Descrição: Processo memorando

### RECLAMADAS_MEMORANDO — Reclamadas memorando
TextBox String → CPE_CSC.RECLAMADAS_MEMORANDO
Descrição: Reclamadas Memorando

### DIVISAO_JURIDICA — Informar a Divisão Jurídica aprovadora
DropDownList String → CPE_CJUR.DIVISAO_JURIDICA
Itens: Sejun;Dijus;
Dijut Consultivo;
Dijut Contencioso

### VALOR_TOTAL_GUIAS — Valor total das guias
TextBox Decimal → CPE_CSC.VALOR_TOTAL_GUIAS
Descrição: Valor total das guias de pagamentos judiciais

### NOME_BENEFICIARIO — Nome beneficiario
TextBox String(1000) → CPE_CSC.NOME_BENEFICIARIO
Descrição: Nome benefiario

### DESC_COLABORADOR — Tipo de Colaborador
DropDownList String → CP_ORDEM_SERVICO.DESC_COLABORADOR
Itens: Concursado; Contratado; Temporario; Cedido BB;Estagiario;Jovem Aprendiz

### DESCRICAO_OBRIG — Descrição obrigatória
TextBox String(2000) → CP_ORDEM_SERVICO.DESCRICAO_OBRIG
Descrição: Breve descrição

### FORNECEDOR — Fornecedor
TextBox String → CP_ORDEM_SERVICO.FORNECEDOR

### CSC_DATA_FIM — Data Fim
DatePicker DateTime → CPE_CSC.CSC_DATA_FIM

### CSC_VALOR — Valor
TextBox String → CPE_CSC.CSC_VALOR

### CSC_NOME_COMPLETO — Nome Completo
TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO

### NATUREZA_SERV — Natureza do serviço
DropDownList String → CP_ORDEM_SERVICO.NATUREZA_SERV
Itens: Ajudante de Armazém;Aluguel;Aquisição de bens;Despachante;Gestão de Pessoas;Limpeza;Locação de Bens;Manutenção de Bens;Mão de Obra;Outros;Recepção;Serviço de Contabilidade;Serviços de Infraestrutura;Serviços de TI;Vigilância Monitoramento;Vigilância Patrimonial

### QUANTIDADE — Quantidade
TextBox Integer → CP_ORDEM_SERVICO.QUANTIDADE

### VALOR_DA_NOTA_FISCAL — Valor(es) da(s) Nota(s)
DataGrid RecordList → Z_00143_VALOR_DA_NOTA_FISCAL.VALOR_DA_NOTA_FISCAL
Colunas do registro:
- NUMERO_NOTA_SERVICO "Número da Nota Fiscal" [TextBox String]
- VALOR_NOTA_FISCAL_SERVICO "Valor da Nota Fiscal" [TextBox Decimal]
- ORGANIZACAO "ORGANIZACAO" [DropDownList String]
**ORGANIZACAO.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT TO_CHAR(ORGANIZATION_ID) ID,ORGANIZATION_CODE ||' - '|| ORGANIZATION_NAME AS ORGANIZACAO FROM ORG_ORGANIZATION_DEFINITIONS ORDER BY ORGANIZACAO")
```
- NUM_ITEM "Número do RI" [TextBox Integer]
- NOME_ARQUIVO "Nome do Arquivo da Nota Fiscal" [TextBox String]
- DATA_PGTO "Data de Pagamento" [DatePicker DateTime]
- CONDICAO_DE_PGTO "Condição de pagamento da OC (Conforme ERP)" [TextBox String]
- NUMERO_RI "Número da RI" [TextBox String]

### CONTA_CONTABIL1 — Conta Contábil
TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1

### DESCRICAO_DETALHADA — Descrição detalhada
Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA

### CPF — CPF
TextBox String(15) → CP_ORDEM_SERVICO.CPF

### CSC_BAIRRO — Bairro
TextBox String(500) → CPE_CSC.CSC_BAIRRO

### CSC_CPF — CPF
TextBox String(300) → CPE_CSC.CSC_CPF

## Biblioteca de scripts referenciada
teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
