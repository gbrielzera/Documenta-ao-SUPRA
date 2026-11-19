# Fluxo: Prestação de Contas - Deslocamento (PRESDESLOC) — versão 39
Caminho: Fluxos > Administração - Passagens Aéreas e ou Hospedagem Versão 39 Prestação de Contas - Deslocamento
XML: `XMLs para teste/Administração_-_Passagens_Aéreas_e_ou_Hospedagem_Versão_39_Prestação_de_Contas_-_Deslocamento.xml` | Supravizio 19.1.1 | SubProcessoId 21901 | DesenhoProcessoId 2962 | ProcessoId 103
Órgão dono: 3000008444 - SUP. SERV. COMPART. | Responsável: ADIR CORDEIRO DOS SANTOS FILHO
Classe do subprocesso: Objetivo=Prestação de Contas - Deslocamento; DescricaoCliente=Prestação de Contas - Deslocamento; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true

## Grafo do fluxo
- [347977] Tarefa "Confirmar valores de passagens, hospedagens e locação de veículo" {Fila CSC - Passagens Aéreas e Hospedagem} → [347992] Aprovar Prestação de contas

- [347978] Tarefa "Realizar Prestação de Contas" {Cliente} → [347987]  | [347979]  | [G78638] Houve aquisição de passagens e/ou hospedagem e/ou 
- [347979] EventoIntermediarioTimer "" → [347993] Cobrança - Prestação de Contas - Deslocamento
- [347980] EventoIntermediarioMensagem "Cobrança Prestação de Contas - Deslocamento " → [347978] Realizar Prestação de Contas
- [347981] EventoFinal "" {Responsável atual} → (fim)
- [347982] EventoIntermediarioMensagem "Corrigir solicitação" → [347983] Corrigir Prestação de Contas
- [347983] Tarefa "Corrigir Prestação de Contas" {Cliente} → [347984]  | [347988]  | [347992] Aprovar Prestação de contas

- [347984] EventoIntermediarioTimer "" → [347990] Corrigir Prestação de Contas - Deslocamento 
- [347985] EventoIntermediarioMensagem "Prestação de Contas - Deslocamento" → [347978] Realizar Prestação de Contas
- [347986] Tarefa "Efetuar Pagamento" {Responsável atual} → [347994] Término de serviço
- [347987] EventoIntermediarioTimer "" → [347980] Cobrança Prestação de Contas - Deslocamento 
- [347988] EventoIntermediarioTimer "" → [347991] Corrigir Prestação de Contas - Deslocamento
- [347989] LinkInicial "" {Cliente} → [347995] Aguardar viagem
- [347990] EventoIntermediarioMensagem "Corrigir Prestação de Contas - Deslocamento " → [347983] Corrigir Prestação de Contas
- [347991] EventoIntermediarioMensagem "Corrigir Prestação de Contas - Deslocamento" → [347983] Corrigir Prestação de Contas
- [347992] Tarefa "Aprovar Prestação de contas
" {Fila CSC - Pendente de Aprovação} → [G78637] Prestação de Contas aprovada?
- [347993] EventoIntermediarioMensagem "Cobrança - Prestação de Contas - Deslocamento" → [347978] Realizar Prestação de Contas
- [347995] Tarefa "Aguardar viagem" {Cliente} → [347978] Realizar Prestação de Contas | [347996] 
- [347994] EventoIntermediarioMensagem "Término de serviço" → [347981] 
- [347996] EventoIntermediarioRegra "" → [347985] Prestação de Contas - Deslocamento
- [G78637] Gateway "Prestação de Contas aprovada?" → «Aprovado» [347986] Efetuar Pagamento | «Reprovado» [347982] Corrigir solicitação
- [G78638] Gateway "Houve aquisição de passagens e/ou hospedagem e/ou locação de carro?
" → «Sim» [347977] Confirmar valores de passagens, hospedagens e loca | «Não» [347992] Aprovar Prestação de contas


## Gateways
### [G78637] Prestação de Contas aprovada? (DataBasedExclusiveDecision)
Codigo=APROVAR
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAR_PRESTACAO")
```
- alternativa → [347986] Efetuar Pagamento: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [347982] Corrigir solicitação: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1; MotivoObrigatorio=true; PublicarRespostaAA=true
**ValorComparacaoDecision**
```python
False
```
### [G78638] Houve aquisição de passagens e/ou hospedagem e/ou locação de carro?
 (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["PAHL_HOSPEDAGENS"] == True or OrdemServico["PAHL_LOCACOES"] == True or OrdemServico["PAHL_PASSAGENS"] == True
```
- alternativa → [347977] Confirmar valores de passagens, hospedagens e loca: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [347992] Aprovar Prestação de contas
: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [347977] Tarefa "Confirmar valores de passagens, hospedagens e locação de veículo"
Responsável: Fila CSC - Passagens Aéreas e Hospedagem (papel 508)
Config: ConfirmaResponsabilidade=true
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
favorecido = OrdemServico.GetCustom("FAVORECIDO_DESLOCAMENTO")
data_atual = DateTime.Now.Date

consulta = 'Select PESSOA.NOME, OCORRENCIA.NUMERO, OCORRENCIA.DATA_HORA_CRIACAO, CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO, OCORRENCIA.SITUACAO, ATIVIDADE.DESCRICAO, CPE_CSC.CSC_VALOR1_A As "VALOR TOTAL DIARIAS", CPE_CSC.CSC_VALOR1_TOTAL_A As "VALOR DAS PASSAGENS", CPE_CSC.CSC_VALOR2_A As "VALOR TOTAL CARROS" From OCORRENCIA Inner Join CPE_CSC On CPE_CSC.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA Inner Join ORDEM_SERVICO On ORDEM_SERVICO.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA Inner Join CLASSE_SUB_PROCESSO On OCORRENCIA.ID_CLASSE_SUB_PROC = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO Inner Join PESSOA On OCORRENCIA.ID_CLIENTE = PESSOA.ID_PESSOA Inner Join CPE_DESLOCAMENTO On CPE_DESLOCAMENTO.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA Inner Join ATIVIDADE On OCORRENCIA.ID_ATIVIDADE = ATIVIDADE.ID_ATIVIDADE '
consulta2 = "Where CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO = '"+ favorecido.ToString() +"' And CLASSE_SUB_PROCESSO.SIGLA = 'DESLOCAMENTOALTERACAOCANCELA' Order By OCORRENCIA.DATA_HORA_CRIACAO Desc"


query_final = consulta + consulta2
sql         = DB.ExecuteDataTable(query_final) 
texto       = "===== RESUMO DAS OUTRAS SOLICITAÇÕES ====="

if sql.Rows.Count != 0:
    for index, i in enumerate(sql.Rows):
        if index == 0:
    
            valor_diarias       = i['VALOR TOTAL DIARIAS']      .ToString()
            valor_passagens     = i['VALOR DAS PASSAGENS']      .ToString()
            valor_carros        = i['VALOR TOTAL CARROS' ]      .ToString()
            numero_os           = i['NUMERO']                   .ToString()
            data_criacao        = i['DATA_HORA_CRIACAO']        
            atividade           = i['DESCRICAO']                .ToString()
            situacao            = i['SITUACAO']                 .ToString()
            
            criacao             = Convert.ToDateTime(data_criacao).Date
            diferenca_dias      = (data_atual - criacao).Days
            
            if Convert.ToInt32(diferenca_dias) < 90:
            
                # === ATRIBUIÇÃO DOS VALORES NOS CAMPOS: ===
                
                Formulario["TEXT"       ].Valor =  valor_diarias              # VALOR TOTAL DIARIAS
                Formulario["TEXT_1"     ].Valor =  valor_passagens            # VALOR DAS PASSAGENS
                Formulario["TEXT2"      ].Valor =  valor_carros               # VALOR TOTAL CARROS
                Formulario["NUMERO_OC2" ].Valor =  Convert.ToInt32(numero_os) # NUMERO DA OS
        
            
        else:
            # === RESUMO DO RESTO EM DESCRIÇÃO1: ===
            
            valor_diarias       = i['VALOR TOTAL DIARIAS']      .ToString()
            valor_passagens     = i['VALOR DAS PASSAGENS']      .ToString()
            valor_carros        = i['VALOR TOTAL CARROS' ]      .ToString()
            numero_os           = i['NUMERO']                   .ToString()
            data_criacao        = i['DATA_HORA_CRIACAO']        .ToString()
            atividade           = i['DESCRICAO']                .ToString()
            situacao            = i['SITUACAO']                 .ToString()
            
            id_favorecido       = Convert.ToInt32(i['FAVORECIDO_DESLOCAMENTO'])
            
            try:
                fav = Pessoa.Carrega(id_favorecido)
            except:
                fav = ""
                
            criacao             = Convert.ToDateTime(data_criacao).Date
            diferenca_dias      = (data_atual - criacao).Days
            
            if Convert.ToInt32(diferenca_dias) < 90:
            
                texto += """

{0} - NÚMERO DA OS            : {1},
{0} - DATA CRIAÇÃO            : {2},
{0} - NOME DO FAVORECIDO      : {3},
{0} - VALOR DAS DIÁRIAS       : {4},
{0} - VALOR DAS PASSAGENS     : {5},
{0} - VALOR TOTAL CARROS      : {6},
{0} - SITUAÇÃO DA OS          : {7},
{0} - ATIVIDADE ATUAL DA OS   : {8} 
""".format(index,   numero_os,   criacao,   fav,   valor_diarias,  valor_passagens,    valor_carros, situacao, atividade)
        
            
    #Formulario.ExibeMensagem(texto)
    Formulario["DESCRICAO_DETALHADA"].Valor = texto if len(texto) < 2000 else texto[:2000]
            
    
        
else:
    Formulario["DESCRICAO_DETALHADA"].Valor = "Não foi encontrado OS de Ajustes para esse favorecido"
    
    
for i in Formulario.Controles:
    Formulario[i.Key].Habilitado = False
    
Formulario['CHECKBOX1'].Habilitado = True
    
    
    
if Formulario["DESCRICAO_DETALHADA"].Valor == "Não foi encontrado OS de Ajustes para esse favorecido":

    Formulario["TEXT"       ].Visivel =  False
    Formulario["TEXT_1"     ].Visivel =  False
    Formulario["TEXT2"      ].Visivel =  False
    Formulario["NUMERO_OC2" ].Visivel =  False
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Opções de Reserva
  - PAHL_LOCACOES "Locações de Carro" [CheckBox Boolean → CPE_CSC.PAHL_LOCACOES]
**PAHL_LOCACOES.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#camposVisiveis = None
#camposHabilitados = None
#vis = False
#hab = False
#
#pessoa = Pessoa.Carrega(Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
#if OrdemServico.Servico.Sigla == "DESLOCAMENTO":
#   # lista de campos a serem alteradas a visibilidade.
#   camposVisiveis = ["PAHL_LOCACOES_CARRO", "CSC_OBS"]
#   camposHabilitados = ["PAHL_LOCACOES_CARRO", "CSC_OBS"]
#   if Formulario["PAHL_LOCACOES"].Valor == True:
#      vis = True
#      hab = True
#
#   for controle in Formulario.Controles:
#       # preserva a visibilidade atual dos campos
#       visivel = Formulario[controle.Key].Visivel
#       habilitado = Formulario[controle.Key].Habilitado
#       valor = Formulario[controle.Key].Valor
#       for campo in camposVisiveis:
#           if controle.Key == campo:
#              visivel = vis
#              valor = None
#              break
#       Formulario[controle.Key].Visivel = visivel
#       
#       for campo in camposHabilitados:
#           if controle.Key == campo:
#              habilitado = hab
#              break
#       Formulario[controle.Key].Habilitado = habilitado
#       Formulario[controle.Key].Valor = valor
#       
#   #Formulario["PAH_MOTIVO_SOL"].Visivel = False
#   
#   #cargos = ["TECNICO", "TECNICO DE OPERACOES", "TECNICO ESPECIALISTA"]
#   
#   #if (Formulario["PAHL_PASSAGENS"].Valor == True or Formulario["PAHL_HOSPEDAGENS"].Valor == True or Formulario["PAHL_LOCACOES"].Valor == True) and cargos.Contains(pessoa["CARGO_FUNCIONAL"]):
#   Formulario["PAH_MOTIVO_SOL"].Visivel = True
#   Formulario["PAH_MOTIVO_SOL"].Habilitado = True
#   #else:
#   #   Formulario["PAH_MOTIVO_SOL"].Visivel = False
#   #   Formulario["PAH_MOTIVO_SOL"].Habilitado = False
#
```
  - PAHL_PASSAGENS "Reserva de Passagens Aéreas" [CheckBox Boolean → CPE_CSC.PAHL_PASSAGENS]
**PAHL_PASSAGENS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#camposVisiveis = None
#camposHabilitados = None
#vis = False
#hab = False
#
#pessoa = Pessoa.Carrega(Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
#if OrdemServico.Servico.Sigla == "DESLOCAMENTO":
#   # lista de campos a serem alteradas a visibilidade.
#   camposVisiveis = ["RESERVA_DE_VOO", "DESCRICAO_OBRIG", "CSC_OBS"]
#   camposHabilitados = ["RESERVA_DE_VOO", "DESCRICAO_OBRIG", "CSC_OBS"]
#   camposVisiveis = ["DESCRICAO_OBRIG", "CSC_OBS"]
#   camposHabilitados = ["DESCRICAO_OBRIG", "CSC_OBS"]
#   if Formulario["PAHL_PASSAGENS"].Valor == True:
#      vis = True
#      hab = True
#    
#
#   for controle in Formulario.Controles:
#       # preserva a visibilidade atual dos campos
#       visivel = Formulario[controle.Key].Visivel
#       habilitado = Formulario[controle.Key].Habilitado
#       valor = Formulario[controle.Key].Valor
#       for campo in camposVisiveis:
#           if controle.Key == campo:
#              visivel = vis
#              valor = None
#              break
#       Formulario[controle.Key].Visivel = visivel
#       
#       for campo in camposHabilitados:
#           if controle.Key == campo:
#              habilitado = hab
#              break
#       Formulario[controle.Key].Habilitado = habilitado
#       Formulario[controle.Key].Valor = valor
#       
#   cargos = ["TECNICO", "TECNICO DE OPERACOES", "TECNICO ESPECIALISTA"]

#if (Formulario["PAHL_PASSAGENS"].Valor == True) and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional"):
#    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Visivel = True
#    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Habilitado = True
#    Formulario["RESERVA_DE_VOO"].Visivel = False
#    Formulario["RESERVA_DE_VOO"].Habilitado = False
#    Formulario["DESCRICAO_OBRIG"].Visivel = True
#    Formulario["DESCRICAO_OBRIG"].Habilitado = True
#    Formulario["CSC_OBS"].Visivel = True
#    Formulario["CSC_OBS"].Habilitado = True
#elif (Formulario["PAHL_PASSAGENS"].Valor == True) and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
#    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Visivel = False
#    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Habilitado = False
#    Formulario["RESERVA_DE_VOO"].Visivel = True
#    Formulario["RESERVA_DE_VOO"].Habilitado = True    
#    Formulario["DESCRICAO_OBRIG"].Visivel = True
#    Formulario["DESCRICAO_OBRIG"].Habilitado = True
#    Formulario["CSC_OBS"].Visivel = True
#    Formulario["CSC_OBS"].Habilitado = True
#else:
#    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Visivel = False
#    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Habilitado = False
#    Formulario["RESERVA_DE_VOO"].Visivel = False
#    Formulario["RESERVA_DE_VOO"].Habilitado = False    
#    Formulario["DESCRICAO_OBRIG"].Visivel = False
#    Formulario["DESCRICAO_OBRIG"].Habilitado = False
#    Formulario["CSC_OBS"].Visivel = False
#    Formulario["CSC_OBS"].Habilitado = False
```
  - PAHL_HOSPEDAGENS "Reserva de Hospedagens" [CheckBox Boolean → CPE_CSC.PAHL_HOSPEDAGENS]
**PAHL_HOSPEDAGENS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#camposVisiveis = None
#camposHabilitados = None
#vis = False
#hab = False
#
#pessoa = Pessoa.Carrega(Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
#if OrdemServico.Servico.Sigla == "DESLOCAMENTO":
#   # lista de campos a serem alteradas a visibilidade.
#   camposVisiveis = ["PAH_DATA_ENTRADA", "PAH_DATA_SAIDA", "PAH_EVENTO_HOTEL", "DESCRICAO_OBRIG", "CSC_OBS"]
#   camposHabilitados = ["PAH_DATA_ENTRADA", "PAH_DATA_SAIDA", "PAH_EVENTO_HOTEL", "DESCRICAO_OBRIG", "CSC_OBS"]
#   if Formulario["PAHL_HOSPEDAGENS"].Valor == True:
#      vis = True
#      hab = True
#   for controle in Formulario.Controles:
#       # preserva a visibilidade atual dos campos
#       visivel = Formulario[controle.Key].Visivel
#       habilitado = Formulario[controle.Key].Habilitado
#       valor = Formulario[controle.Key].Valor
#       for campo in camposVisiveis:
#           if controle.Key == campo:
#              visivel = vis
#              valor = None
#              break
#       Formulario[controle.Key].Visivel = visivel
#       
#       for campo in camposHabilitados:
#           if controle.Key == campo:
#              habilitado = hab
#              break
#       Formulario[controle.Key].Habilitado = habilitado
#       Formulario[controle.Key].Valor = valor
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Roteiro da Viagem" classes: Roteiro — RequeridoInicial=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Inclua o roteiro da viagem e os valores gastos com passagens, hospedagens e/ou locação de veículos
  - LISTA_DE_OS_ALTCANC_DESLOCAMENTO "OS's de Alteração e Cancelamento" [DataGrid RecordList → Z_00143_LISTA_DE_OS_ALTCANC_DESLOCAMENTO.LISTA_DE_OS_ALTCANC_DESLOCAMENTO] — QtdColunasFormulario=1
    - coluna SOLICITACAO obrigatório
    - coluna OS obrigatório
  - PAH_VOUCHER_HOSPEDAGEM "Voucher Hospedagem" [TextBox String → CPE_CSC.PAH_VOUCHER_HOSPEDAGEM]
  - PAHL_VOUCHER_CARRO "Voucher de Locação de Carro" [TextBox String → CPE_CSC.PAHL_VOUCHER_CARRO]
  - PAHL_LOCACOES_CARRO "Locações de Carro" [DataGrid RecordList → Z_00143_PAHL_LOCACOES_CARRO.PAHL_LOCACOES_CARRO]
    - coluna LOCAL_DEVOLUCAO obrigatório
    - coluna DATA_HORA_DEVOLUCAO obrigatório
    - coluna VALOR_LOCACAO
    - coluna CARRO4X4 obrigatório
    - coluna LOCAL_RETIRADA obrigatório
    - coluna DATA_HORA_RETIRADA obrigatório
  - PAHL_NUM_ARGO "Número da OS Argo" [TextBox String → CPE_CSC.PAHL_NUM_ARGO] obrigatório
  - CSC_VALOR1_TOTAL "Valor das passagens aéreas" [TextBox Decimal → CPE_CSC.CSC_VALOR1_TOTAL]
  - CSC_VALOR1 "Valor Diarias Hotel" [TextBox Decimal → CPE_CSC.CSC_VALOR1]
  - CSC_VALOR2 "Valor Total das Locações de Carro" [TextBox Decimal → CPE_CSC.CSC_VALOR2]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Resumo das OS's de Edição
  - TEXT_1 "Valor das Passagens" [TextBox String(1000) → CPE_CSC.TEXT_1]
  - TEXT2 "Valor Total das locações de carro" [TextBox String → CPE_CSC.TEXT2]
  - NUMERO_OC2 "Número da Ordem de Serviço de EDIÇÃO" [TextBox Integer → CPE_CONTRATOS.NUMERO_OC2]
  - DESCRICAO_DETALHADA "Descrição detalhada" [Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA]
  - CHECKBOX1 "Pesquisar por novas OS's de Edição (Se houver)" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX1]
**CHECKBOX1.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Controle.Valor == True:
    favorecido = OrdemServico.GetCustom("FAVORECIDO_DESLOCAMENTO")
    data_atual = DateTime.Now.Date

    consulta = 'Select PESSOA.NOME, OCORRENCIA.NUMERO, OCORRENCIA.DATA_HORA_CRIACAO, CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO, OCORRENCIA.SITUACAO, ATIVIDADE.DESCRICAO, CPE_CSC.CSC_VALOR1_A As "VALOR TOTAL DIARIAS", CPE_CSC.CSC_VALOR1_TOTAL_A As "VALOR DAS PASSAGENS", CPE_CSC.CSC_VALOR2_A As "VALOR TOTAL CARROS" From OCORRENCIA Inner Join CPE_CSC On CPE_CSC.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA Inner Join ORDEM_SERVICO On ORDEM_SERVICO.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA Inner Join CLASSE_SUB_PROCESSO On OCORRENCIA.ID_CLASSE_SUB_PROC = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO Inner Join PESSOA On OCORRENCIA.ID_CLIENTE = PESSOA.ID_PESSOA Inner Join CPE_DESLOCAMENTO On CPE_DESLOCAMENTO.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA Inner Join ATIVIDADE On OCORRENCIA.ID_ATIVIDADE = ATIVIDADE.ID_ATIVIDADE '
    consulta2 = "Where CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO = '"+ favorecido.ToString() +"' And CLASSE_SUB_PROCESSO.SIGLA = 'DESLOCAMENTOALTERACAOCANCELA' Order By OCORRENCIA.DATA_HORA_CRIACAO Desc"

    query_final = consulta + consulta2

    sql = DB.ExecuteDataTable(query_final)

    texto = "===== RESUMO DAS OUTRAS SOLICITAÇÕES ====="

    if sql.Rows.Count > 0:

        indice = 0

        for i in sql.Rows:

            valor_diarias = i["VALOR TOTAL DIARIAS"].ToString()
            valor_passagens = i["VALOR DAS PASSAGENS"].ToString()
            valor_carros = i["VALOR TOTAL CARROS"].ToString()
            numero_os = i["NUMERO"].ToString()
            atividade = i["DESCRICAO"].ToString()
            situacao = i["SITUACAO"].ToString()

            criacao = Convert.ToDateTime(i["DATA_HORA_CRIACAO"]).Date
            diferenca_dias = (data_atual - criacao).Days

            if diferenca_dias < 90:

                if indice == 0:

                    Formulario["TEXT"].Valor = valor_diarias
                    Formulario["TEXT_1"].Valor = valor_passagens
                    Formulario["TEXT2"].Valor = valor_carros
                    Formulario["NUMERO_OC2"].Valor = Convert.ToInt32(numero_os)

                else:

                    id_favorecido = Convert.ToInt32(i["FAVORECIDO_DESLOCAMENTO"])

                    fav = Pessoa.Carrega(id_favorecido)

                    texto += "\r\n\r\n"
                    texto += str(indice) + " - NÚMERO DA OS: " + numero_os
                    texto += "\r\n"
                    texto += str(indice) + " - DATA CRIAÇÃO: " + criacao.ToString()
                    texto += "\r\n"
                    texto += str(indice) + " - NOME DO FAVORECIDO: " + fav.ToString()
                    texto += "\r\n"
                    texto += str(indice) + " - VALOR DAS DIÁRIAS: " + valor_diarias
                    texto += "\r\n"
                    texto += str(indice) + " - VALOR DAS PASSAGENS: " + valor_passagens
                    texto += "\r\n"
                    texto += str(indice) + " - VALOR TOTAL CARROS: " + valor_carros
                    texto += "\r\n"
                    texto += str(indice) + " - SITUAÇÃO DA OS: " + situacao
                    texto += "\r\n"
                    texto += str(indice) + " - ATIVIDADE ATUAL DA OS: " + atividade

            indice = indice + 1

        if len(texto) > 1000:
            Formulario["DESCRICAO_DETALHADA"].Valor = texto.Substring(0, 1000)
        else:
            Formulario["DESCRICAO_DETALHADA"].Valor = texto

    else:

        Formulario["DESCRICAO_DETALHADA"].Valor = "Não foi encontrado OS de Ajustes para esse favorecido"

    for i in Formulario.Controles:
        Formulario[i.Key].Habilitado = False

    Formulario["CHECKBOX1"].Habilitado = True

    if Formulario["DESCRICAO_DETALHADA"].Valor == "Não foi encontrado OS de Ajustes para esse favorecido":

        Formulario["TEXT"].Visivel = False
        Formulario["TEXT_1"].Visivel = False
        Formulario["TEXT2"].Visivel = False
    Formulario["NUMERO_OC2"].Visivel = False
```
  - TEXT "Valor Total das Diárias" [TextBox String(1000) → CPE_CSC.TEXT]

### [347978] Tarefa "Realizar Prestação de Contas"
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
import apiOrdsSV
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

ret = consultaTab(OrdemServico.NumeroSistema.ToString())
if ret.items.ToString() != None and ret.items.ToString() != '[]' :
    for linha in ret.items:
        cadastro_id = linha['cadastro_id'].ToString()
        chamado = linha['chamado'].ToString()
        cliente = linha['cliente'].ToString()
        nome_arq = linha['nome_arq'].ToString()
        tipo_arq = linha['tipo_arq'].ToString()
        arquivo_base64 = linha['arquivo_base64'].ToString().Trim("'")
        arquivo_base64 = linha['arquivo_base64'].ToString().Trim('"')
        #OrdemServico.AdicionaComentario(cadastro_id+'///'+ chamado +'///'+cliente+'///'+nome_arq+'///'+tipo_arq ,False)
        #Formulario["DESCRICAODETALHADA"].Valor = arquivo_base64
        ###############
        
        
        processo=OrdemServico.DesenhoProcesso.Processo.Descricao.ToString()
        repositorio = Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM")
        #caminho_arquivo = "\\\santacruz0.cobra.com.br\supravizio$/Anexos/"+processo+"/DOCPRESTACAOCONTAS/"+cadastro_id+'_'+nome_arq+tipo_arq
        ##OrdemServico.AdicionaComentario(caminho_arquivo.ToString(),False)
        caminho_arquivo = repositorio+"/Anexos/"+processo+"/Documentos da Prestação de Contas/"+cadastro_id+'_'+nome_arq+tipo_arq
        
        bytes_arquivo = Convert.FromBase64String(arquivo_base64)
        File.WriteAllBytes(caminho_arquivo, bytes_arquivo)
        os = OrdemServico
        os.AnexaArquivo(caminho_arquivo, "DOCPRESTACAOCONTAS", True)
        os.Salva()
        retorno = atualizaTab(cadastro_id.ToString())
        Utils.LogInformation("API bot afranio chamado: "+chamado+" cad_id: "+cadastro_id+" arq_nome: "+nome_arq,"DEBUG")
else:
    OrdemServico.AdicionaComentario('Não tem arquivo para ser anexado nesta OS.',False)
```
**ScriptFim**
```python
OrdemServico.Salva()
```
**ScriptValidacao**
```python
if OrdemServico["SIM_NAO2"] == "Sim" and OrdemServico["SIM_NAO3"] == "Sim":
    Criticas.AdicionaPendencia("Não é permitido solicitar reembolso e devolução na mesma OS")
    
if OrdemServico["VALORTOTALPB"] != "" and Convert.ToDecimal(OrdemServico["VALORTOTALPB"]) < 0:
    Criticas.AdicionaPendencia("O campo Valor de devolução não pode ser negativo.")
    
if OrdemServico["VALOR_DOD"] != "" and Convert.ToDecimal(OrdemServico["VALOR_DOD"]) < 0:
    Criticas.AdicionaPendencia("O campo Valor do reembolso não pode ser negativo.")
    
if OrdemServico["SIM_NAO3"] == "Não" and Convert.ToDecimal(OrdemServico["VALOR_DIFERENCA_DESLOCAMENTO"]) < 0:
    Criticas.AdicionaPendencia("Haverá necessidade de devolução de valor para a BBTS. Marque a opção Sim e preencha o valor da devolução.")
    
if OrdemServico["SIM_NAO2"] == "Não" and Convert.ToDecimal(OrdemServico["VALOR_DIFERENCA_DESLOCAMENTO"]) > 0:
    Criticas.AdicionaPendencia("O funcionário/Gestor receberá um valor não previsto no pedido inicial do deslocamento. Marque a opção Sim e verifique o valor do reembolso.")
    
    
#Valida cidades que possuem CAT quanto a solicitação avulsa e que são capitais
listaCidadesCAT = ["ARACAJU - SE", "BELEM - PA", "BELO HORIZONTE - MG", "BOA VISTA - RR", "BRASILIA - DF", "CAMPO GRANDE - MS", "CUIABA - MT", "CURITIBA - PR", "FLORIANOPOLIS - SC", "FORTALEZA - CE", "GOIANIA - GO", "SAO LUIS - MA", "MACAPA - AP", "MACEIO - AL", "NATAL - RN", "PALMAS - TO", "PORTO ALEGRE - RS", "PORTO VELHO - RO", "RECIFE - PE", "RIO BRANCO - AC", "RIO DE JANEIRO - RJ", "SALVADOR - BA", "SAO PAULO - SP", "SERRA - ES", "TERESINA - PI", "VITORIA - ES", "BAURU - SP", "CAMPINAS - SP", "JOINVILLE - SC", "LONDRINA - PR", "PASSO FUNDO - RS", "RIBEIRAO PRETO - SP", "UBERLANDIA - MG"]

cidadeDestinoNome = ""
cidadeDestinoDescricao = DB.ExecuteDataTable("SELECT DISTINCT id_cidade, descricao || ' - ' || id_estado AS cidadeuf FROM cidade_v WHERE id_cidade = '"+ OrdemServico["CIDADE_DESTINO"] + "'")

for cidadeDestino in cidadeDestinoDescricao.Rows:
    cidadeDestinoNome = cidadeDestino['CIDADEUF'].ToString()
    
for cidade in listaCidadesCAT:  
    if cidade.ToString() == cidadeDestinoNome.ToString() and OrdemServico["TIPO_HOSPEDAGEM"].ToString() == "Avulsa SEM apresentação de NF":
        Criticas.AdicionaPendencia("Não é permitido a abertura de solicitaçoes de hospedagens avulsas para capitais e ou cidades que possui CAT.")
        
queryAdesaoDiariaAvulaSemApresentarNF = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, PESSOA.NOME From OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = CP_ORDEM_SERVICO.FAVORECIDO_COBRA Where OCORRENCIA.ASSUNTO = 'Adesão a diárias avulsas sem comprovação documental' And (OCORRENCIA.SITUACAO = 'FinalizadaSucesso' Or OCORRENCIA.SITUACAO = 'Aberto') and PESSOA.ID_PESSOA = '"+OrdemServico["FAVORECIDO_DESLOCAMENTO"]+"'")

if queryAdesaoDiariaAvulaSemApresentarNF.Rows.Count == 0 and OrdemServico["TIPO_HOSPEDAGEM"] == "Avulsa SEM apresentação de NF":
    Criticas.AdicionaPendencia("Parece que seu aceite, Adesão a diárias avulsas sem comprovação documental, não foi feito. O Aceite é necessário para este tipo de solicitação.") 
    
#Valida os checkbox que devem ser marcados
if OrdemServico["CHECKBOX8"] == False and OrdemServico["CHECKBOX9"] == False:
    Criticas.AdicionaPendencia("Você deve informar se houve alteração no seu deslocamento.")
    
if OrdemServico["CHECKBOX10"] == False:
    Criticas.AdicionaPendencia("E necessário calcular a diferença do deslocamento.")
    
if OrdemServico["COMBOBOX_CONFIRMA_TREINAMENTO"] == False:
    Criticas.AdicionaPendencia("E necessário calcular o custo total do deslocamento.")
    
if OrdemServico["VALOR_DESPESAS"] < 0:
    Criticas.AdicionaPendencia("No campo, Valor de outras despesas R$, não é permitido o preenchimento de valores negativos. preencher com 0 caso não tenha.")
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Servico
import apiOrdsSV
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.
Formulario["FAVORECIDO_DESLOCAMENTO"].Habilitado = True
Formulario["FAVORECIDO_DESLOCAMENTO"].Visivel = True
ret = consultaTab(OrdemServico.NumeroSistema.ToString())
if ret.items.ToString() != None and ret.items.ToString() != '[]' :
    for linha in ret.items:
        cadastro_id = linha['cadastro_id'].ToString()
        chamado = linha['chamado'].ToString()
        cliente = linha['cliente'].ToString()
        nome_arq = linha['nome_arq'].ToString()
        tipo_arq = linha['tipo_arq'].ToString()
        arquivo_base64 = linha['arquivo_base64'].ToString().Trim("'")
        arquivo_base64 = linha['arquivo_base64'].ToString().Trim('"')
        #OrdemServico.AdicionaComentario(cadastro_id+'///'+ chamado +'///'+cliente+'///'+nome_arq+'///'+tipo_arq ,False)
        Formulario["DESCRICAODETALHADA"].Valor = arquivo_base64
        ###############
        
        
        processo=OrdemServico.DesenhoProcesso.Processo.Descricao.ToString()
        repositorio = Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM")
        #caminho_arquivo = "\\\santacruz0.cobra.com.br\supravizio$/Anexos/"+processo+"/DOCPRESTACAOCONTAS/"+cadastro_id+'_'+nome_arq+tipo_arq
        ##OrdemServico.AdicionaComentario(caminho_arquivo.ToString(),False)
        caminho_arquivo = repositorio+"/Anexos/"+processo+"/Documentos da Prestação de Contas/"+cadastro_id+'_'+nome_arq+tipo_arq
        
        bytes_arquivo = Convert.FromBase64String(arquivo_base64)
        File.WriteAllBytes(caminho_arquivo, bytes_arquivo)
        os = OrdemServico
        os.AnexaArquivo(caminho_arquivo, "DOCPRESTACAOCONTAS", True)
        os.Salva()
        retorno = atualizaTab(cadastro_id.ToString())
        Utils.LogInformation("API bot afranio chamado: "+chamado+" cad_id: "+cadastro_id+" arq_nome: "+nome_arq,"DEBUG")
else:
    OrdemServico.AdicionaComentario('Não tem arquivo para ser anexado nesta OS.',False)

#SCRIPT PARA LIMPAR OS DADOS DO FORMULARIO #######################
#Formulario["FAVORECIDO_DESLOCAMENTO"].Visivel = False
#Formulario["MATRICULA_DESLOCAMENTO"].Visivel = False
#Formulario["CARGO_DESLOCAMENTO"].Visivel = False
#Formulario["FUNCAO_DESLOCAMENTO"].Visivel = False
#Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = False
#Formulario["CELULAR"].Visivel = False
#Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False
#Formulario["SIM_NAO"].Visivel = False
#Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
#
#Formulario["TIPO_DESLOCAMENTO"].Visivel = False
#Formulario["CIDADE_ORIGEM"].Visivel = False
#Formulario["CIDADE_DESTINO"].Visivel = False
#Formulario["CIDADE_CLASSIFICACAO"].Visivel = False
#Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = False
#Formulario["PAIS"].Visivel = False
#Formulario["TIPO_DESTINO"].Visivel = False
#Formulario["SAIDA"].Visivel = False
#Formulario["RETORNO_DIA"].Visivel = False
#Formulario["SAIDA_HORA"].Visivel = False
#Formulario["RETORNO_HORA"].Visivel = False
#Formulario["DIAS_DE_TRA"].Visivel = False
#Formulario["TIPO_HOSPEDAGEM"].Visivel = False
#Formulario["QUANTIDADE_DIARIA"].Visivel = False
#Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
#Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
#Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
#Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
#Formulario["VALOR_DIARIA"].Visivel = False
#Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
#Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
#Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
#Formulario["COTACAO_DOLAR"].Visivel = False
#Formulario["DIARIA_COTACAO_REAL"].Visivel = False
#Formulario["NUMERO_NT"].Visivel = False
#Formulario["PARCELA_COMPLEMENTAR"].Visivel = False
#Formulario["TOTAL_COMPLEMENTAR"].Visivel = False
#Formulario["LISTA_INVIABILIDADE"].Visivel = False
#Formulario["OBJETIVO_VIAGEM"].Visivel = False
#Formulario["MEIO_LOCOMOCAO"].Visivel = False
#Formulario["VIAGEM_LONGA"].Visivel = False
#Formulario["SIM_NAO_REFEICAO"].Visivel = False
#Formulario["PREVISAO_DISTANCIA_KM"].Visivel = False
#Formulario["VALOR_DISTANCIA"].Visivel = False
#Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
#Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
#Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
#Formulario["VALOR_REF_REDUZIDA"].Visivel = False
#Formulario["VALOR_REF_INTEGRAL"].Visivel = False
#Formulario["DESCRICAO_DESPESAS"].Visivel = False
#Formulario["VALOR_DESPESAS"].Visivel = False
#Formulario["VALOR_TOTAL_ADIANTAMENTO"].Visivel = False
#Formulario["PAHL_HOSPEDAGENS"].Visivel = False
#Formulario["PAHL_LOCACOES"].Visivel = False
#Formulario["PAHL_PASSAGENS"].Visivel = False

Formulario["CIDADE_ORIGEM"].Habilitado = False
Formulario["CIDADE_DESTINO"].Habilitado = False
Formulario["SAIDA_HORA"].Habilitado = False
Formulario["TIPO_DESTINO"].Habilitado = False
Formulario["MEIO_LOCOMOCAO"].Habilitado = True
Formulario["TIPO_DESLOCAMENTO"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
Formulario["TIPO_HOSPEDAGEM"].Habilitado = False

#Limpa os valores da seleção SIM e Não quando carregar o formulario
Formulario["CHECKBOX9"].Habilitado = True
Formulario["CHECKBOX8"].Habilitado = True

Formulario["CHECKBOX8"].Valor = False
Formulario["CHECKBOX9"].Valor = False
Formulario["CHECKBOX10"].Valor = False
Formulario["COMBOBOX_CONFIRMA_TREINAMENTO"].Valor = False


#SQL PARA RECUPERAR O VALOR DO REPASSE DA SOLICITAÇÃO DE DESLOCAMENTO PAI##########################
os = OrdemServico.Numero.Split(".")
sqlDeslocamento = DB.ExecuteDataTable("Select o.NUMERO, csp.DESCRICAO, mp.DESCRICAO As MACRO_PROCESSO, pr.DESCRICAO As PROCESSO, csp.DESCRICAO As SUBPROCESSO, s.DESCRICAO As Servico, o.SITUACAO, p1.NOME As Cliente, p2.NOME As responsavel, o.DATA_HORA_CRIACAO, o.DATA_HORA_FIM_REAL, cped.VALOR_TOTAL_ADIANTAMENTO From ocorrencia o Inner Join pessoa p1 On p1.id_pessoa = o.ID_CLIENTE Inner Join pessoa p2 On p2.id_pessoa = o.ID_RESPONSAVEL Inner Join atividade a On a.id_atividade = o.ID_ATIVIDADE Inner Join ordem_servico os On os.id_ocorrencia = o.ID_OCORRENCIA Inner Join servico s On s.id_servico = os.ID_SERVICO Inner Join classe_sub_processo csp On csp.id_classe_sub_processo = o.ID_CLASSE_SUB_PROC Inner Join desenho_processo dp On dp.id_desenho_processo = o.ID_DESENHO_PROCESSO Inner Join processo pr On pr.id_processo = dp.ID_PROCESSO Inner Join macro_processo mp On mp.id_macro_processo = pr.ID_MACRO_PROCESSO Inner Join CP_ORDEM_SERVICO On o.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join CPE_DESLOCAMENTO cped on O.ID_OCORRENCIA = cped.ID_OCORRENCIA Where o.NUMERO = '"+os[0].ToString()+"'")

for deslocamento in sqlDeslocamento.Rows:
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = deslocamento["VALOR_TOTAL_ADIANTAMENTO"]
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = deslocamento["VALOR_TOTAL_ADIANTAMENTO"]

Formulario["CIDADE_DESTINO"].Visivel = True
Formulario["LABEL10"].Visivel = False
Formulario["CHECKBOX9"].Visivel = True
Formulario["CHECKBOX8"].Visivel = True
Formulario["LABEL2"].Visivel = True

#Script para "Houve alteração no Deslocamento"?    
if Formulario["CHECKBOX9"].Valor == True:
    Formulario["FAVORECIDO_DESLOCAMENTO"].Visivel = True
    Formulario["MATRICULA_DESLOCAMENTO"].Visivel = True
    Formulario["CARGO_DESLOCAMENTO"].Visivel = True
    Formulario["FUNCAO_DESLOCAMENTO"].Visivel = True
    Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = True
    Formulario["CELULAR"].Visivel = True
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
    Formulario["SIM_NAO"].Visivel = True
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True
    Formulario["CIDADE_DESTINO"].Visivel = True

    #Formulario["TIPO_DESLOCAMENTO"].Valor = ""
    #Formulario["CIDADE_ORIGEM"].Valor = ""
    #Formulario["CIDADE_DESTINO"].Valor = ""
    #Formulario["CIDADE_CLASSIFICACAO"].Valor = ""
    #Formulario["CIDADE_DESTINO_INTERNACIONAL"].Valor = ""
    #Formulario["PAIS"].Valor = ""
    #Formulario["TIPO_DESTINO"].Valor = ""
    Formulario["RETORNO_DIA"].Valor = None
    #Formulario["SAIDA_HORA"].Valor = ""
    Formulario["RETORNO_HORA"].Valor = ""
    Formulario["DIAS_DE_TRA"].Valor = ""
    Formulario["TIPO_HOSPEDAGEM"].Valor = ""
    Formulario["QUANTIDADE_DIARIA"].Valor = ""
    #Formulario["VALOR_DIARIA_DOLAR"].Valor = ""
    #Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = ""
    #Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = ""
    #Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = ""
    Formulario["VALOR_DIARIA"].Valor = ""
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = ""
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = ""
    Formulario["VALOR_TOTAL_DIARIA"].Valor = ""
    Formulario["COTACAO_DOLAR"].Valor = ""
    #Formulario["DIARIA_COTACAO_REAL"].Valor = ""
    #Formulario["NUMERO_NT"].Valor = ""
    Formulario["PARCELA_COMPLEMENTAR"].Valor = ""
    Formulario["TOTAL_COMPLEMENTAR"].Valor = ""

    #Formulario["MEIO_LOCOMOCAO"].Valor = ""
    Formulario["VIAGEM_LONGA"].Valor = ""
    Formulario["SIM_NAO_REFEICAO"].Valor = ""
    Formulario["PREVISAO_DISTANCIA_KM"].Valor = ""
    #Formulario["VALOR_DISTANCIA"].Valor = ""
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = ""
    Formulario["VALOR_TOTAL_REFEICAO"].Valor = ""
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = ""
    Formulario["VALOR_REF_REDUZIDA"].Valor = ""
    Formulario["VALOR_REF_INTEGRAL"].Valor = ""
    Formulario["DESCRICAO_DESPESAS"].Valor = ""
#    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = ""

#Formulario["QUANTIDADE_DIARIA"].Visivel = False
#Formulario["QUANTIDADE_DIARIA"].Habilitado = False
Formulario["VALOR_DIARIA"].Visivel = False
Formulario["VALOR_DIARIA"].Habilitado = True
#Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
Formulario["DIARIA_COTACAO_REAL"].Visivel = False
Formulario["DIARIA_COTACAO_REAL"].Habilitado = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True


#Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
#Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False  


Formulario["VALOR_REF_INTEGRAL"].Visivel = False
Formulario["VALOR_REF_INTEGRAL"].Habilitado = False
Formulario["VALOR_REF_REDUZIDA"].Visivel = False
Formulario["VALOR_REF_REDUZIDA"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False        
Formulario["COTACAO_DOLAR"].Visivel = False
Formulario["COTACAO_DOLAR"].Habilitado = False  


#Formulario["VALOR_DISTANCIA"].Valor = "0"
#Formulario["VALOR_TOTAL_REFEICAO"].Valor = "0"
#Formulario["QTD_REFEICAO_REDUZIDA"].Valor = "0"




#Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = "0"
#Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "0"
#Formulario["VALOR_DIARIA_DOLAR"].Valor = "0"
#Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "0"
Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False




Formulario["CARGO_DESLOCAMENTO"].Visivel = False
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = False
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = False
Formulario["CARGO_DESLOCAMENTO"].Habilitado = False
Formulario["FUNCAO_DESLOCAMENTO"].Habilitado = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Habilitado = False
Formulario["MATRICULA_DESLOCAMENTO"].Habilitado = False

    

Formulario["PREVISAO_DISTANCIA_KM"].Visivel = False
Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = False 
Formulario["VALOR_DISTANCIA"].Visivel = False
Formulario["VALOR_DISTANCIA"].Habilitado = False
#Formulario["VALOR_PASSAGEM"].Visivel = False
#Formulario["VALOR_PASSAGEM"].Habilitado = False
#Formulario["VALIDADE_PASSAGEM"].Visivel = False
#Formulario["VALIDADE_PASSAGEM"].Habilitado = False
#Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = False
#Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = False


#Formulario["QUANTIDADE_DIARIA"].Visivel = True
#Formulario["QUANTIDADE_DIARIA"].Habilitado = True
#Formulario["VALOR_DIARIA"].Visivel = False
#Formulario["VALOR_DIARIA"].Habilitado = False
#Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False

Formulario["CIDADE_DESTINO"].Visivel = True
Formulario["CIDADE_CLASSIFICACAO"].Visivel = True
Formulario["CIDADE_CLASSIFICACAO"].Habilitado = False
Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = False
Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = False
Formulario["PAIS"].Visivel = False
Formulario["PAIS"].Habilitado = False

#Dados das Reservas

#Formulario["PAH_MOTIVO_SOL"].Visivel = False
#Formulario["PAH_MOTIVO_SOL"].Habilitado = False 
#Formulario["PAH_LOCALIZADORES"].Visivel = False
#Formulario["PAH_LOCALIZADORES"].Habilitado = False
#Formulario["PAH_VOUCHER_HOSPEDAGEM"].Visivel = False
#Formulario["PAH_VOUCHER_HOSPEDAGEM"].Habilitado = False
#Formulario["RESERVA_DE_VOO"].Visivel = False
#Formulario["RESERVA_DE_VOO"].Habilitado = False
#Formulario["PAH_DATA_ENTRADA"].Visivel = False
#Formulario["PAH_DATA_ENTRADA"].Habilitado = False
#Formulario["PAH_DATA_SAIDA"].Visivel = False
#Formulario["PAH_DATA_SAIDA"].Habilitado = False 
#Formulario["PAH_LOCALIZADORES"].Visivel = False
#Formulario["PAH_LOCALIZADORES"].Habilitado = False
#Formulario["PAH_EVENTO_HOTEL"].Visivel = False
#Formulario["PAH_EVENTO_HOTEL"].Habilitado = False
#Formulario["PAH_HOTEL_EVENTO"].Visivel = False
#Formulario["PAH_HOTEL_EVENTO"].Habilitado = False
#Formulario["PAHL_VOUCHER_CARRO"].Visivel = False
#Formulario["PAHL_VOUCHER_CARRO"].Habilitado = False
#Formulario["PAHL_LOCACOES_CARRO"].Visivel = False
#Formulario["PAHL_LOCACOES_CARRO"].Habilitado = False 
###Formulario["DESCRICAO_OBRIG"].Visivel = False
###Formulario["DESCRICAO_OBRIG"].Habilitado = False
#Formulario["CSC_OBS"].Visivel = False
#Formulario["CSC_OBS"].Habilitado = False
#Formulario["RESERVA_DE_VOO"].Visivel = False
#Formulario["RESERVA_DE_VOO"].Habilitado = False
#Formulario["DATA_INICIO_AUX1"].Visivel = False
#Formulario["DATA_INICIO_AUX1"].Habilitado = False
#Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Visivel = False
#Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Habilitado = False


Formulario["SIM_NAO"].Visivel = False

Formulario["PARCELA_COMPLEMENTAR"].Visivel = True
Formulario["PARCELA_COMPLEMENTAR"].Habilitado = True   
Formulario["TOTAL_COMPLEMENTAR"].Visivel = True
Formulario["TOTAL_COMPLEMENTAR"].Habilitado = True  

Formulario["VIAGEM_LONGA"].Visivel = False
Formulario["VIAGEM_LONGA"].Habilitado = False 

Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False 

Formulario["LABEL1"].Visivel = False
Formulario["LABEL1"].Habilitado = False
Formulario["NUMERO_NT"].Visivel = False
#Formulario["NUMERO_NT"].Habilitado = False

#Formulario["VALOR_EXTRA"].Habilitado = True    
#Formulario["VALOR_EXTRA"].Visivel = True

#LISTA DE PAÍSES

Formulario["PAIS"].Itens = "AFEGANISTÃO;ARMÊNIA;BANGLADESH;BELARUS;BENIN;BOLÍVIA;BURKINAFASSO;BUTÃO;CHILE; COMORES;REPÚBLICA POPULAR DEMOCRÁTICA DA CORÉIA;COSTA RICA;EL SALVADOR; EQUADOR;ESLOVÊNIA;FILIPINAS;GÂMBIA;GUIANA;GUINÉ BISSAU;GUINÉ;HONDURAS;INDONÉSIA;IRÃ;IRAQUE;LAOS;LÍBANO;MALÁSIA;MALDIVAS; MARROCOS;MONGÓLIA;MYANMAR;NAMÍBIA;NAURU;NEPAL;NICARÁGUA;PANAMÁ;PARAGUAI; REP. CENTRO AFRICANA;REPÚBLICA TOGOLESA;SALOMÃO;SAMOA;SERRA LEOA;SÍRIA;SOMÁLIA;SRI LANKA;SURINAME;TADJIQUISTÃO;TAILÂNDIA;TIMOR LESTE;TONGA;TUNÍSIA;TURCOMENISTÃO;TURQUIA;TUVALU;VIETNÃ;ZIMBÁBUE;ÁFRICA DO SUL;ALBÂNIA;ANDORA;ARGÉLIA;ARGENTINA;AUSTRÁLIA;BELIZE;BÓSNIA-HERZEGÓVINA;BURUNDI;CABO VERDE;CAMARÕES;CAMBOJA;CATAR;CHADE;CHINA;CHIPRE;COLÔMBIA;DOMINICA;EGITO;ERITRÉIA;ESTÔNIA;ETIÓPIA;GANA;GEÓRGIA;GUINÉ EQUATORIAL;HAITI;HUNGRIA;IEMEN;ILHAS MARSHALL;ÍNDIA;KIRIBATI;LESOTO;LÍBIA;MACEDÔNIA;MADAGASCAR;MALAUÍ;MICRONÉSIA;MOÇAMBIQUE;MOLDÁVIA;NÍGER;NIGÉRIA;NOVA ZELÂNDIA;PALAU;PAPUA NOVAGUINÉ;PAQUISTÃO;PERU;POLÔNIA;QUÊNIA;REPÚBLICA DOMINICANA;ROMÊNIA;RUANDA;SÃO TOMÉ E PRÍNCIPE;SENEGAL; SUDÃO;TANZÂNIA;URUGUAI;UZBEQUISTÃO;VENEZUELA;ANTÍGUA E BARBUDA;ARÁBIA SAUDITA;AZERBAIDJÃO;BAHAMAS;BAREINE;BOTSUANA;BRUNEI DARUSSALAM;BULGÁRIA;CANADÁ;CINGAPURA;CONGO;COSTA DO MARFIM;CUBA;DJIBUTI;EMIRADOS ÁRABES;FIJI;GABÃO;GUATEMALA;JAMAICA;JORDÂNIA;LETÔNIA;LIBÉRIA;LITUÂNIA;MALI;MALTA;MAURÍCIO;MAURITÂNIA;MÉXICO;REPÚBLICA DEMOCRÁTICA DO CONGO;REPÚBLICA TCHECA;RÚSSIA;SAN MARINO;SANTA LÚCIA;SÃO CRISTOVÃO E NÉVIS;SÃO VICENTE EGRANADINAS;TAIWAN;TRINIDAD E TOBAGO;UCRÂNIA;UGANDA;ZÂMBIA;ALEMANHA;ANGOLA;ÁUSTRIA;BARBADOS;BÉLGICA;CAZAQUISTÃO;CORÉIA DOSUL;CROÁCIA;DINAMARCA;ESPANHA;ESTADOS UNIDOS DA AMÉRICA;FINLÂNDIA;FRANÇA;GRANADA;GRÉCIA;HONG KONG;IRLANDA;ISLÂNDIA;ISRAEL;ITÁLIA;JAPÃO;KUAITE;LIECHTENSTEIN;LUXEMBURGO;MÔNACO;MONTENEGRO;NORUEGA;OMÃ;PEÍSES BAIXOS;PORTUGAL;REINO UNIDO;REPÚBLICA QUIRGUIZ;SEICHELES;SÉRVIA SUAZILÂNDIA;SUÉCIA;SUÍÇA;VANUATU"




#INICIO SCRIPT PARA FAVORECIDO DESLOCAMENTO###############################################
Formulario["FAVORECIDO_DESLOCAMENTO"].Habilitado = False

Formulario["CARGO_DESLOCAMENTO"].Visivel = True
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = True
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = True
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = True

Formulario["CARGO_DESLOCAMENTO"].Habilitado = False
Formulario["FUNCAO_DESLOCAMENTO"].Habilitado = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Habilitado = False
Formulario["MATRICULA_DESLOCAMENTO"].Habilitado = False

Formulario["CARGO_DESLOCAMENTO"].Valor = None
Formulario["FUNCAO_DESLOCAMENTO"].Valor = None
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = None
Formulario["MATRICULA_DESLOCAMENTO"].Valor = None

cargo = ""
funcao = ""
desc_colaborador = ""
matricula = ""

if Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != "" or Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["ORGAO_FAVORECIDO"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT SUBSTR(c.CARGO,INSTR(c.CARGO,'|')+1,LENGTH(c.CARGO)) AS CARGO1, c.FUNCAO_GRATIFICADA, c.DESC_COLABORADOR, c.MATRICULA, c.FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND C.NUMERO_SUBCR_NIVEL1 = O.SIGLA AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    #lista = Utils.ExecuteDataTable("SELECT SUBSTR(CARGO,INSTR(CARGO,'|')+1,LENGTH(CARGO)) AS CARGO1, FUNCAO_GRATIFICADA, DESC_COLABORADOR, MATRICULA, FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND LPAD(C.NUMERO_SUBCR_NIVEL1,5) = LPAD(O.SIGLA,5) AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    for linha in lista.Rows:
        cargo = linha["CARGO1"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()

    Formulario["CARGO_DESLOCAMENTO"].Valor = cargo.ToString()
    Formulario["FUNCAO_DESLOCAMENTO"].Valor = funcao.ToString()
    Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = desc_colaborador.ToString()
    Formulario["MATRICULA_DESLOCAMENTO"].Valor = matricula.ToString()

if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False
else:
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
    Formulario["ACOMPANHANDO_GRUPO_A"].Valor = "Não"
    
#FIM SCRIPT PARA FAVORECIDO DESLOCAMENTO###############################################


#INICIO SCRIPT PARA BLOCO 2 ####################################
Formulario['DIAS_DE_TRA'].Visivel = False

if Formulario['DIAS_DE_TRA'].Valor == 0 or Formulario['DIAS_DE_TRA'].Valor == '0' or Formulario['TIPO_HOSPEDAGEM'].Valor == 'Sem Hospedagem':

    Formulario['QUANTIDADE_DIARIA'].Habilitado = False
    Formulario['QUANTIDADE_DIARIA'].Valor = 0
    

if Formulario['PARCELA_COMPLEMENTAR'].Valor == 0 or Formulario['PARCELA_COMPLEMENTAR'].Valor == '':
    Formulario['PARCELA_COMPLEMENTAR'].Habilitado = False
    Formulario['PARCELA_COMPLEMENTAR'].Visivel = False
    
else:
    Formulario['PARCELA_COMPLEMENTAR'].Habilitado = True
    Formulario['PARCELA_COMPLEMENTAR'].Visivel = True

if Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Próprio":
    Formulario['VALOR_DISTANCIA'].Habilitado = True
    Formulario['VALOR_DISTANCIA'].Visivel = True    
    Formulario['PREVISAO_DISTANCIA_KM'].Habilitado = True
    Formulario['PREVISAO_DISTANCIA_KM'].Visivel = True
    
else:
    Formulario['VALOR_DISTANCIA'].Habilitado = False
    Formulario['VALOR_DISTANCIA'].Visivel = False    
    Formulario['PREVISAO_DISTANCIA_KM'].Habilitado = False
    Formulario['PREVISAO_DISTANCIA_KM'].Visivel = False
 
#################################    
#if Formulario['CSC_VALOR1_TOTAL'].Valor != 0 or Formulario['CSC_VALOR1_TOTAL'].Valor != '' or Formulario['CSC_VALOR1_TOTAL'].Valor != '0':
#    Formulario['CSC_VALOR1_TOTAL'].Habilitado = False
#    Formulario['CSC_VALOR1_TOTAL'].Visivel = True
#else:
#    Formulario['CSC_VALOR1_TOTAL'].Habilitado = False
#    Formulario['CSC_VALOR1_TOTAL'].Visivel = False
#       
##################################     
#if Formulario['CSC_VALOR1'].Valor != 0 or Formulario['CSC_VALOR1'].Valor != '' or Formulario['CSC_VALOR1'].Valor != '0':
#    Formulario['CSC_VALOR1'].Habilitado = False
#    Formulario['CSC_VALOR1'].Visivel = True
#else:
#    Formulario['CSC_VALOR1'].Habilitado = False
#    Formulario['CSC_VALOR1'].Visivel = False
    
#################################     
#if Formulario['CSC_VALOR2'].Valor != 0 or Formulario['CSC_VALOR2'].Valor != '' or Formulario['CSC_VALOR2'].Valor != '0':
#    Formulario['CSC_VALOR2'].Habilitado = False
#    Formulario['CSC_VALOR2'].Visivel = True
#else:
#    Formulario['CSC_VALOR2'].Habilitado = False
#    Formulario['CSC_VALOR2'].Visivel = False
       
#Formulario['MEIO_LOCOMOCAO'].Habilitado = False
Formulario['VALOR_TOTAL_REFEICAO'].Habilitado = False
Formulario['VALOR_TOTAL_REFEICAO'].Visivel = True
Formulario['CUSTO_TOT_DESLOC'].Habilitado = False
Formulario['CUSTO_TOT_DESLOC'].Visivel = False
Formulario['VALOR_TOT_PREST_CONTAS'].Habilitado = False
Formulario['VALOR_TOTAL_ADIANTAMENTO'].Habilitado = True
Formulario['VALOR_TOTAL_ADIANTAMENTO'].Visivel = True
Formulario['VALORTOTSEMCOMPROV'].Habilitado = False

#FIM SCRIPT PARA BLOCO 2 #######################################

Formulario["OBJETIVO_VIAGEM"].Habilitado = False
Formulario["SAIDA"].Habilitado = False
Formulario["VALOR_DESPESAS"].Habilitado = False
Formulario["LISTA_INVIABILIDADE"].Habilitado = False


#Formulario["NOME_PROJETO"].Habilitado = False    
#Formulario["NOME_PROJETO"].Visivel = False    
#Formulario["VALOR_EXTRA"].Habilitado = False    
#Formulario["VALOR_EXTRA"].Visivel = False
#Formulario["SIM_NAO4"].Habilitado = False    
#Formulario["SIM_NAO4"].Visivel = False

Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False

if OrdemServico["TIPO_DESLOCAMENTO"] == "Viagem a Serviço - Internacional":
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
    #Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
    Formulario["COTACAO_DOLAR"].Visivel = True
    #Formulario["COTACAO_DOLAR"].Habilitado = True  
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
    #Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = True
    #Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = True
    Formulario["PAIS"].Visivel = True
    #Formulario["PAIS"].Habilitado = True       
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
    Formulario["TIPO_HOSPEDAGEM"].Visivel = True
    Formulario["TIPO_HOSPEDAGEM"].Habilitado = False    
    Formulario["TIPO_HOSPEDAGEM"].Valor = "Avulsa"
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True    
    
    Formulario["CIDADE_DESTINO"].Visivel = False
    Formulario["CIDADE_DESTINO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["DIARIA_COTACAO_REAL"].Visivel = True
    #Formulario["DIARIA_COTACAO_REAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    
    Formulario["LABEL1"].Visivel = True
    Formulario["LABEL1"].Habilitado = True
    Formulario["NUMERO_NT"].Visivel =  True
    #Formulario["NUMERO_NT"].Habilitado = True
Formulario["FAVORECIDO_DESLOCAMENTO"].Habilitado = True
Formulario["FAVORECIDO_DESLOCAMENTO"].Visivel = True
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Documentos da Prestação de Contas" classes: Documentos da Prestação de Contas — RequeridoInicial=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações do Deslocamento
  - DIAS_DE_TRA "Dias em Deslocamento" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA] obrigatório
  - TIPO_HOSPEDAGEM "Tipo de Hospedagem" [DropDownList String → CPE_DESLOCAMENTO.TIPO_HOSPEDAGEM] obrigatório
**TIPO_HOSPEDAGEM.ScriptModificado**
```python
Formulario["VALOR_DIARIA"].Valor = ""

if Formulario["TIPO_HOSPEDAGEM"].Valor == "Sem Hospedagem":
    Formulario["QUANTIDADE_DIARIA"].Visivel = False
    Formulario["QUANTIDADE_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    Formulario["PARCELA_COMPLEMENTAR"].Visivel = False
    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False
    Formulario["TOTAL_COMPLEMENTAR"].Visivel = False
    Formulario["TOTAL_COMPLEMENTAR"].Habilitado = False    
    Formulario["TOTAL_COMPLEMENTAR"].Valor = "0"   


##NOVO SCRIPT ADICIONADO PARA AVULSA SEM APRESENTAÇÃO DE NF    
if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa COM apresentação de NF" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA"].Visivel = True
    Formulario["VALOR_DIARIA"].Habilitado = True
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    #Formulario["PAHL_HOSPEDAGENS"].Visivel = True
    #Formulario["PAHL_HOSPEDAGENS"].Habilitado = True
    
    Formulario["QUANTIDADE_DIARIA"].Valor = ""

    
    
if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA"].Visivel = True
    Formulario["VALOR_DIARIA"].Habilitado = True
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    
    Formulario["QUANTIDADE_DIARIA"].Valor = ""
    

queryAdesaoDiariaAvulaSemApresentarNF = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, PESSOA.NOME From OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = CP_ORDEM_SERVICO.FAVORECIDO_COBRA Where OCORRENCIA.ASSUNTO = 'Adesão a diárias avulsas sem comprovação documental' And (OCORRENCIA.SITUACAO = 'FinalizadaSucesso' Or OCORRENCIA.SITUACAO = 'Aberto') and PESSOA.ID_PESSOA = '"+Formulario["FAVORECIDO_DESLOCAMENTO"].Valor+"'")

if queryAdesaoDiariaAvulaSemApresentarNF.Rows.Count == 0 and Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF":
    Formulario.ExibeMensagem("Parece que seu aceite, Adesão a diárias avulsas sem comprovação documental, não foi feito. O Aceite é necessário para este tipo de solicitação.")
    
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa":
    Formulario["QUANTIDADE_DIARIA"].Valor = ""
    Formulario["VALOR_DIARIA"].Valor = ""
    
#if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional"):
#    Formulario["QUANTIDADE_DIARIA"].Visivel = True
#    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA"].Visivel = True
#    Formulario["VALOR_DIARIA"].Habilitado = True
#    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
#    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
#    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False    
    

#if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional"):
#    Formulario["QUANTIDADE_DIARIA"].Visivel = False
#    Formulario["QUANTIDADE_DIARIA"].Habilitado = False
#    Formulario["VALOR_DIARIA"].Visivel = False
#    Formulario["VALOR_DIARIA"].Habilitado = False
#    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
#    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
#    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
```
  - QUANTIDADE_DIARIA "Quantidade de Diárias" [TextBox Integer → CPE_DESLOCAMENTO.QUANTIDADE_DIARIA] obrigatório
**QUANTIDADE_DIARIA.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import OutputSubProcesso
def calculaDiaria():
    ############### SE O FAVORECIDO FOR DO GRUPO C MAS ESTARÁ ACOMPANHANDO O GRUPO B RECEBE O VALOR DO GRUPO B 
    
    if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
            Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
    
    elif Formulario["SIM_NAO"].Valor == "Sim" :
          if Formulario["CIDADE_DESTINO"].Valor == "3550308": # SAO PAULO 
                 Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "650"
                
          elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO E BRASILIA
            Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550"
            
          elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
              Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
          else: 
            Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
      
    else:     
            
        ############## SE FOR DO GRUPO A -  PRESIDENTE / DIRETOR / CONSELHEIRO NÃO TEM LIMITE   
        if Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "PRESIDENTE":
            Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
            
            
            
        ############## SE O FAVORECIDO FOR DO GRUPO B  ELE RECEBE REFERENTE A CIDADE     
        elif Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "GERENTE EXECUTIVO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE DE PROJETOS I" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "ASSESSOR EXEC DA PRESIDENCIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "SUPERINTENDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "SUPERINTENDENTE":
            if Formulario["CIDADE_DESTINO"].Valor == "3550308 ": # SAO PAULO 
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "650"
                    
            elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO OutputSubProcesso BRASILIA
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550"
                    
            elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or      Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
                      Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450" 
            else:
                Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
                  
                  
        ############## DEMAIS CARGOS
        elif Formulario["FUNCAO_DESLOCAMENTO"].Valor != "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "PRESIDENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE DE PROJETOS I" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "ASSESSOR EXEC DA PRESIDENCIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "SUPERINTENDENTE":
              
              if Formulario["CIDADE_DESTINO"].Valor == "3550308": # SAO PAULO 3550308 
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550" 
                    
              elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO ou BRASILIA
                        Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
                        
              elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or      Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
                          Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "370" 
                          
              else:
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "350"
                  

              
              
calculaDiaria()
     
############ VALOR FINAL DO ADIANTAMENTO EM DIARIAS      
diasViagem = Convert.ToInt32(Formulario["DIAS_DE_TRA"].Valor)
diasHospedagem = Convert.ToInt32(Formulario["QUANTIDADE_DIARIA"].Valor)



if diasHospedagem > diasViagem:
    mensagem = "Quantidade de Diária Excedida! Máximo Permitido: " + Formulario["DIAS_DE_TRA"].Valor + " Verifique a saída e o retorno"
    Formulario.ExibeMensagem(mensagem)      
    Formulario["VALOR_DIARIA"].Habilitado = False
else:
    Formulario["VALOR_DIARIA"].Habilitado = True   


#Valor parcela complementar    



if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":

    Formulario["PARCELA_COMPLEMENTAR"].Valor = "0"
    Formulario["PARCELA_COMPLEMENTAR"].Visivel = False
    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False    
    Formulario["TOTAL_COMPLEMENTAR"].Habilitado = False
    Formulario["TOTAL_COMPLEMENTAR"].Visivel = False
    Formulario["TOTAL_COMPLEMENTAR"].Valor = "0"
   
else:    
    Formulario["PARCELA_COMPLEMENTAR"].Valor = "19,74"
    Formulario["PARCELA_COMPLEMENTAR"].Visivel = True
    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False    
    
    pc = Formulario["PARCELA_COMPLEMENTAR"].Valor 
    qtd = Formulario["QUANTIDADE_DIARIA"].Valor
    total = 0

    total = pc * qtd
    
    Formulario["TOTAL_COMPLEMENTAR"].Valor = total
    Formulario["TOTAL_COMPLEMENTAR"].Visivel = True


#Define o valor para hospedagem do tipo avulsa
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" and Formulario["CIDADE_CLASSIFICACAO"].Valor == "A":
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = 230.00
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = 230.00
    
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" and Formulario["CIDADE_CLASSIFICACAO"].Valor == "B":
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = 250.00
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = 250.00

if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" and Formulario["CIDADE_CLASSIFICACAO"].Valor == "C":
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = 270.00
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = 270.00
    

#if (Formulario["TIPO_DESTINO"].Valor == "Interior") and (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa"):
#    Formulario["VALOR_DIARIA"].Valor = "350"
#    
#if (Formulario["TIPO_DESTINO"].Valor == "Capital") and (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa"):
#    Formulario["VALOR_DIARIA"].Valor = "500"
#
#import System.Text
#daysOffText = System.Text.StringBuilder()
#
# #RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
#def isHoliday(day):
#    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C  inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
#   
#    for holiday in holidays.Rows:
#        if day == holiday["DATA"].Date:
#            return True
#    return False
#   
#def workingDays(totalDays, firstDate):
#    
#    totalWorkingDays = 0
#    totalDaysOff = 0
#    count = 0
#   
#    while count <= totalDays:
#        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
#        day = firstDate.Date.AddDays(count)
#        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
#            totalDaysOff = totalDaysOff + 1
#            daysOffText.AppendLine(" dayOff: "+str(day))
#        
#        count = count + 1
#        totalWorkingDays = totalWorkingDays + 1
#    return totalWorkingDays - totalDaysOff
#   
#
#saida = Formulario["SAIDA"].Valor
#retorno  = Formulario["RETORNO_DIA"].Valor
#
#totalDias = (retorno - saida).TotalDays  
#count = 0
#
#totalDiasUteis = workingDays(totalDias,saida) 
#totalDiasNaoUteis = totalDias - totalDiasUteis
#
############### almoço e janta de ambos os dias
#quantReduzida = totalDiasUteis  
#quantIntegral = (totalDiasNaoUteis * 2) + totalDiasUteis
#
#
#

#Formulario["QTD_REFEICAO_REDUZIDA"].Valor = totalDiasUteis 
#Formulario["QTD_REFEICAO_INTEGRAL"].Valor = totalDiasNaoUteis
#
#
#Formulario["VALOR_REF_REDUZIDA"].Valor = totalDiasUteis * 18.39
#Formulario["VALOR_REF_INTEGRAL"].Valor = totalDiasNaoUteis *  64.36
#
#
#OrdemServico.AdicionaComentario("WorkingDays "+totalWorkingDays.ToString(),False)
#OrdemServico.AdicionaComentario(daysOffText.ToString(),False )

#OrdemServico["totalWorkingDays"] = totalWorkingDays
```
  - VALOR_DIARIA_AUTORIZADO "Valor Diária Autorizado" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_AUTORIZADO] obrigatório — Coluna=2
  - CAMPO_VALIDACAO_DIARIA "Diária máxima autorizada R$ (TAB320-001)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DIARIA] obrigatório
  - VALOR_TOTAL_DIARIA "Valor Total Diária:" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_DIARIA]
  - LABEL1 "Cotação do Dólar Americano Conforme Aprovado na NT" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - COTACAO_DOLAR "Cotação do Dólar americano (USD) " [TextBox String → CPE_DESLOCAMENTO.COTACAO_DOLAR] obrigatório
**COTACAO_DOLAR.ScriptModificado**
```python
#import System
#
#valorTotal = 0
#
#
#valorTotal = Formulario["VALOR_TOTAL_DIARIA"].Valor * Convert.ToDecimal(Formulario["COTACAO_DOLAR"].Valor)
#
#
#Convert.ToDecimal(Formulario["DIARIA_COTACAO_REAL"].Valor) = valorTotal


valorTotal = 0
vtd = Formulario["VALOR_TOTAL_DIARIA"].Valor
cd = Convert.ToDecimal(Formulario["COTACAO_DOLAR"].Valor)

valorTotal = vtd * cd

Formulario["DIARIA_COTACAO_REAL"].Valor = valorTotal




#valorTotal = 0
#
#
#valorTotal = Formulario["VALOR_TOTAL_DIARIA"].Valor * (Formulario["COTACAO_DOLAR"].Valor)
#
#
#Formulario["DIARIA_COTACAO_REAL"].Valor = valorTotal
#

#diariaReal = ""
#cotacao = ""
#valorTotal = ""
#
#diariaReal = Convert.ToDouble(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#cotacao = Convert.ToDouble(Formulario["COTACAO_DOLAR"].Valor)
```
  - DIARIA_COTACAO_REAL "Diária em Real" [TextBox String → CPE_DESLOCAMENTO.DIARIA_COTACAO_REAL] obrigatório — Coluna=2
  - NUMERO_NT "Número da Nota Técnica" [TextBox String → CPE_CONTRATOS.NUMERO_NT] obrigatório — Configuracao={"Mascara":"0000/0000"}
  - PARCELA_COMPLEMENTAR "Parcela Complementar de hospedagem" [TextBox Decimal → CPE_DESLOCAMENTO.PARCELA_COMPLEMENTAR] obrigatório
  - TOTAL_COMPLEMENTAR "Total Parcela Complementar (Não é necessário prestar contas)" [TextBox Decimal → CPE_DESLOCAMENTO.TOTAL_COMPLEMENTAR] obrigatório
  - PREVISAO_DISTANCIA_KM "Previsão de distancia em KM (Para recebimento de R$1,30 por KM)" [TextBox Decimal → CPE_DESLOCAMENTO.PREVISAO_DISTANCIA_KM] obrigatório
**PREVISAO_DISTANCIA_KM.ScriptModificado**
```python
import System


Formulario["VALOR_DISTANCIA"].Habilitado = False

valorTotal = 0

distancia = Formulario["PREVISAO_DISTANCIA_KM"].Valor
valorTotal = distancia * 1.30 


Formulario["VALOR_DISTANCIA"].Valor = valorTotal
#OrdemServico["VALOR_DISTANCIA"] = valorTotal
#
```
  - VALOR_DISTANCIA "Valor previsto para percorrer distância R$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DISTANCIA] obrigatório — Coluna=2
  - SIM_NAO_REFEICAO "O Empregado/Gestor terá direito a refeição complementar?" [DropDownList String → CPE_DESLOCAMENTO.SIM_NAO_REFEICAO] obrigatório
**SIM_NAO_REFEICAO.ScriptModificado**
```python
import clr 
import datetime
import System.Text
 


zero = 0
valorRefIntegral = 71
valorRefReduzida = 20.29



daysOffText = System.Text.StringBuilder()


##RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
def isHoliday(day):
    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
    #feriados = 0
    
    for holiday in holidays.Rows:
        if day == holiday["DATA"].Date:
            #feriados += 2
            return True
    return False


def countHolidays(firstDate, lastDate):
    totalHolidays = 0
    currentDay = firstDate

    while currentDay <= lastDate:
        if isHoliday(currentDay):
            totalHolidays += 1
        currentDay = currentDay.AddDays(1)

    return totalHolidays

    
def workingDays(totalDays, firstDate):

    totalWorkingDays = 0
    totalDaysOff = 0
    count = 0

   
    while count <= totalDays:
        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
        day = firstDate.Date.AddDays(count)
        
        
        
        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
            totalDaysOff = totalDaysOff + 1
            daysOffText.AppendLine(" dayOff: "+str(day))
        
        count = count + 1
        totalWorkingDays = totalWorkingDays + 1
    return totalWorkingDays - totalDaysOff
   


    
def countSaturdays(firstDate, lastDate):
    saturdays = 0
    currentDay = firstDate
    
    while currentDay <= lastDate:
        if (currentDay.DayOfWeek == DayOfWeek.Sunday or currentDay.DayOfWeek == DayOfWeek.Saturday):
            saturdays += 2
        currentDay = currentDay.AddDays(1)  # Avance para o próximo dia
    
    return saturdays

    
firstDate = Formulario["SAIDA"].Valor
lastDate = Formulario["RETORNO_DIA"].Valor

totalDays = (lastDate - firstDate).TotalDays
count = 0





totalWorkingDays = workingDays(totalDays,firstDate)
holidaysCount = countHolidays(firstDate, lastDate)
saturdays = countSaturdays(firstDate, lastDate) + holidaysCount * 2


#Quantidade de refeições Reduzias e integrais
quantRed = totalWorkingDays
quantInt = saturdays + totalWorkingDays 






#Atribuindo valor a variável
saidaHora = Formulario["SAIDA_HORA"].Valor 
retornoHora = Formulario["RETORNO_HORA"].Valor 

#Split de horário, separando hora de minuto
hora = saidaHora.Split(':');     
horaRetorno = retornoHora.Split(':');

#Atribuindo valor de horário e minuto de acordo com o índice da variável
horarioSaida = hora[0]
minutoSaida = hora[1]

horarioRetorno = horaRetorno[0] 
minutoRetorno = horaRetorno[1]



#SAIDA DIAS ÚTEIS


#1 maior q o 2
#if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) >= 13 and Convert.ToInt32(horarioSaida) < 21):
#    quantRed = quantRed - 1
#   
#if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) > 21):
#    quantInt = quantInt - 1
#   
#RETORNO DIAS ÚTEIS
#1 menor q o 2   
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 13:
#    quantRed = quantRed - 1
#    quantInt = quantInt - 1
#    
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 19 and Convert.ToInt32(horarioRetorno) > 13:
#    quantInt = quantInt - 1
#    #teste abaixo
#    quantRed = quantRed - 1





#DIAS UTEIS

if workingDays(0,firstDate):
    if (Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0)):
        quantRed = quantRed - 1
    if (Convert.ToInt32(horarioSaida) > 21) or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
        quantInt = quantInt - 1
if workingDays(0,lastDate):    
    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
        quantRed = quantRed - 1
    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
        quantInt = quantInt - 1
#Formulario.ExibeMensagem("hora:"+horarioRetorno.ToString()+" minuto:"+minutoRetorno.ToString())    
###############################################################
    
#SAÍDA FINAIS DE SEMANA E/OU FERIADOS

if not  workingDays(0,firstDate):
    if Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0):
        quantInt = quantInt - 1
    if Convert.ToInt32(horarioSaida) > 21 or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
        quantInt = quantInt - 1
if not  workingDays(0,lastDate):
    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
        quantInt = quantInt - 1
    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
        quantInt = quantInt - 1   


if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA": 
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = zero
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = zero
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["VALOR_REF_REDUZIDA"].Visivel = False
    Formulario["VALOR_REF_INTEGRAL"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
    Formulario["SIM_NAO_REFEICAO"].Visivel = False
    Formulario["SIM_NAO_REFEICAO"].Habilitado = False
else:
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = quantRed
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = quantInt
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = True
    Formulario["VALOR_REF_REDUZIDA"].Visivel = True
    Formulario["VALOR_REF_INTEGRAL"].Visivel = True
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = True
    Formulario["SIM_NAO_REFEICAO"].Visivel = True
    Formulario["SIM_NAO_REFEICAO"].Habilitado = True
  
    
if quantRed > (totalWorkingDays):
    mensagem = ("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + str(totalWorkingDays + 1) + " Verifique a Saída e o Retorno.")
    Formulario.ExibeMensagem(mensagem)    
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    

############# calculo valor total

refIntegral = Formulario["QTD_REFEICAO_INTEGRAL"].Valor * valorRefIntegral
refReduzida = Formulario["QTD_REFEICAO_REDUZIDA"].Valor * valorRefReduzida
valorTotalRefeicoes = refIntegral + refReduzida

if Formulario["SIM_NAO_REFEICAO"].Valor == "Sim":
    Formulario["VALOR_TOTAL_REFEICAO"].Valor  = valorTotalRefeicoes
    Formulario["VALOR_REF_REDUZIDA"].Valor = refReduzida
    Formulario["VALOR_REF_INTEGRAL"].Valor = refIntegral
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = True
    Formulario["VALOR_REF_REDUZIDA"].Visivel = True
    Formulario["VALOR_REF_INTEGRAL"].Visivel = True
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = True
else:
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = zero
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = zero
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["VALOR_REF_REDUZIDA"].Valor = zero
    Formulario["VALOR_REF_INTEGRAL"].Valor = zero
    Formulario["VALOR_TOTAL_REFEICAO"].Valor = zero  
    Formulario["VALOR_REF_REDUZIDA"].Visivel = False
    Formulario["VALOR_REF_INTEGRAL"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
```
  - VALOR_REF_INTEGRAL "Valor refeições integrais" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_INTEGRAL]
  - DESCRICAO_DESPESAS "Descrição de outras despesas (Preencher com "NA" caso não tenha) " [TextBox String(1000) → CPE_DESLOCAMENTO.DESCRICAO_DESPESAS]
**DESCRICAO_DESPESAS.ScriptModificado**
```python
import System

diariaAvulsa = 0
valorDist = 0 



#valorTotalPrestContas = OrdemServico.GetCustom("VALOR_DESPESAS") + OrdemServico.GetCustom("VALOR_DISTANCIA") + OrdemServico.GetCustom("VALOR_TOTAL_DIARIA")
#valorTotSemPrestContas = refeições, diaria de hotel contratada/sem hospedagem e parcela complementar

if Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
    
    valorTotalAdiantamento = 0


    totalDiaria = 0
    ##valorAvicao = 0
    outrasDespesas = 0
    ##valorDistancia = 0
    #complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    totalDiaria = Convert.ToDecimal(Formulario["DIARIA_COTACAO_REAL"].Valor)
    ##valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    ##valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    #complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    ##valorTotalAdiantamento =  totalDiaria + outrasDespesas + valorDistancia 
    valorTotalAdiantamento = totalDiaria + outrasDespesas
    
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False

    ##OrdemServico["VALOR_UTILIZADO_DESLOCAMENTO"] = valorTotalAdiantamento

elif (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):

    valorTotalAdiantamento = 0
    valorTotalRefeicao = 0
    totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    valorTotalAdiantamento = valorTotalRefeicao + totalDiaria + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False
    
elif (Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    valorTotalAdiantamento = 0
    valorTotalRefeicao = 0
    #totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    #totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    valorTotalAdiantamento = valorTotalRefeicao + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False


    ##OrdemServico["VALOR_UTILIZADO_DESLOCAMENTO"] = valorTotalAdiantamento    
else:
    valorTotalAdiantamento = 0

    valorTotalRefeicao = 0
    #totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0
    
    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    #totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    
    valorTotalAdiantamento = valorTotalRefeicao + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False
```
  - VALOR_DESPESAS "Valor de outras despesas R$ (preencher com "0" caso não tenha)" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DESPESAS] obrigatório — Coluna=2
**VALOR_DESPESAS.ScriptModificado**
```python
import System

diariaAvulsa = 0
valorDist = 0 

Formulario["CHECKBOX10"].Valor = False
Formulario["COMBOBOX_CONFIRMA_TREINAMENTO"].Valor = False

#valorTotalPrestContas = OrdemServico.GetCustom("VALOR_DESPESAS") + OrdemServico.GetCustom("VALOR_DISTANCIA") + OrdemServico.GetCustom("VALOR_TOTAL_DIARIA")
#valorTotSemPrestContas = refeições, diaria de hotel contratada/sem hospedagem e parcela complementar

if Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
    
    valorTotalAdiantamento = 0


    totalDiaria = 0
    ##valorAvicao = 0
    outrasDespesas = 0
    ##valorDistancia = 0
    #complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    totalDiaria = Convert.ToDecimal(Formulario["DIARIA_COTACAO_REAL"].Valor)
    ##valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    ##valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    #complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    ##valorTotalAdiantamento =  totalDiaria + outrasDespesas + valorDistancia 
    valorTotalAdiantamento = totalDiaria + outrasDespesas
    
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False

    ##OrdemServico["VALOR_UTILIZADO_DESLOCAMENTO"] = valorTotalAdiantamento

#elif (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):

elif (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica") or (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):

    valorTotalAdiantamento = 0
    valorTotalRefeicao = 0
    totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    valorTotalAdiantamento = valorTotalRefeicao + totalDiaria + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False
    
elif (Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    valorTotalAdiantamento = 0
    valorTotalRefeicao = 0
    #totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    #totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    valorTotalAdiantamento = valorTotalRefeicao + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False


    ##OrdemServico["VALOR_UTILIZADO_DESLOCAMENTO"] = valorTotalAdiantamento    
else:
    valorTotalAdiantamento = 0

    valorTotalRefeicao = 0
    #totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0
    
    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    #totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    
    valorTotalAdiantamento = valorTotalRefeicao + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False
    #Esta faltando pegar valor de diaria e da parcela complementar para o valor total
    


 
#Valores a prestar conta 
    
#if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa":
#    
#    
#    diariaAvulsa = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#    
#    
#else:
#    diariaAvulsa = 0
#
#
#    
#if Formulario["VALOR_DISTANCIA"].Valor != 0:
#    valorDist = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
#
#else:
#    valorDist = 0 
#    
#outrasDespesas2 = Convert.ToDecimal(outrasDespesas)
#
#valorTotalPrestContas = outrasDespesas2 + diariaAvulsa + valorDist
#
#
#
#Formulario["VALOR_TOT_PREST_CONTAS"].Valor = Convert.ToDecimal(valorTotalPrestContas)
#
#
#
##Valores sem necessidade de prestação de contas
#
#refeicoes = 0
#hospeda = 0
#complementar = 0
#
#
#
#if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA":
#
#    refeicoes = 0
#
#else:
#    refeicoes = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
#    
#
#    
#if Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada":
#   hospeda = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#   
#elif Formulario["TIPO_HOSPEDAGEM"].Valor == "Sem Hospedagem":
#   hospeda = 0
#
#   
# 
#if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
#    complementar = 0
#else:
#    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
#    
#
#    
#totalSemPrestContas = complementar + hospeda + refeicoes
#
#Formulario["VALORTOTSEMCOMPROV"].Valor = Convert.ToDecimal(totalSemPrestContas)
















    #OrdemServico["VALOR_UTILIZADO_DESLOCAMENTO"] = valorTotalAdiantamento
```
  - VALOR_UTILIZADO_DESLOCAMENTO "Valor Utilizado" [TextBox Decimal → CPE_CSC.VALOR_UTILIZADO_DESLOCAMENTO]
  - VALOR_TOTAL_ADIANTAMENTO "Valor total do adiantamento R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_ADIANTAMENTO]
  - CIDADE_DESTINO "Cidade de Destino" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_DESTINO] — Coluna=2
**CIDADE_DESTINO.ScriptModificado**
```python
sqlConsultaCidadeDestino = DB.ExecuteDataTable("SELECT to_char(id_cidade) as id, c.descricao ||' - '|| c.id_estado as cidade FROM cidade_v c WHERE id_cidade = '"+Formulario["CIDADE_DESTINO"].Valor.ToString()+"'")

sqlConsultaClassificacao = DB.ExecuteDataTable("select DISTINCT CLASSIFICACAO, CIDADE || ' - ' || UF AS cidadeuf from Z_00143_CIDADES_CLASSIFICACOES where CIDADE || ' - ' || UF = '"+sqlConsultaCidadeDestino.Rows[0]["CIDADE"].ToString()+"'")

for classificacao in sqlConsultaClassificacao.Rows:
    Formulario["CIDADE_CLASSIFICACAO"].Valor = classificacao["CLASSIFICACAO"].ToString()
```
  - CIDADE_CLASSIFICACAO "Cidade Classificação" [TextBox String → CPE_CSC.CIDADE_CLASSIFICACAO]
  - CIDADE_DESTINO_INTERNACIONAL "Cidade de Destino (Internacional)" [TextBox String → CPE_DESLOCAMENTO.CIDADE_DESTINO_INTERNACIONAL] obrigatório — Coluna=2
  - PAIS "País de Destino" [DropDownList String → CPE_DESLOCAMENTO.PAIS] obrigatório — Coluna=3
**PAIS.ScriptModificado**
```python
  
        ################## grupo A
if Formulario["PAIS"].Valor == "AFEGANISTÃO" or Formulario["PAIS"].Valor == "ARMÊNIA" or Formulario["PAIS"].Valor == "BANGLADESH" or Formulario["PAIS"].Valor == "BELARUS" or Formulario["PAIS"].Valor == "BENIN" or Formulario["PAIS"].Valor == "BOLÍVIA" or Formulario["PAIS"].Valor == "BURKINAFASSO" or Formulario["PAIS"].Valor == "BUTÃO"  or Formulario["PAIS"].Valor == "CHILE" or Formulario["PAIS"].Valor == "COMORES" or Formulario["PAIS"].Valor == "REPÚBLICA POPULAR DEMOCRÁTICA DA CORÉIA" or Formulario["PAIS"].Valor == "COSTA RICA" or Formulario["PAIS"].Valor == "EL SALVADOR" or Formulario["PAIS"].Valor == "EQUADOR" or Formulario["PAIS"].Valor == "ESLOVÊNIA" or Formulario["PAIS"].Valor == "FILIPINAS" or Formulario["PAIS"].Valor == "GÂMBIA" or Formulario["PAIS"].Valor == "GUIANA" or Formulario["PAIS"].Valor == "GUINÉ BISSAU" or Formulario["PAIS"].Valor == "GUINÉ" or Formulario["PAIS"].Valor == "HONDURAS" or Formulario["PAIS"].Valor == "INDONÉSIA" or Formulario["PAIS"].Valor == "IRÃ" or Formulario["PAIS"].Valor == "IRAQUE" or Formulario["PAIS"].Valor == "LAOS" or Formulario["PAIS"].Valor == "LÍBANO" or Formulario["PAIS"].Valor == "MALÁSIA" or Formulario["PAIS"].Valor == "MALDIVAS" or Formulario["PAIS"].Valor == "MARROCOS" or Formulario["PAIS"].Valor == "MONGÓLIA" or Formulario["PAIS"].Valor == "NAMÍBIA" or Formulario["PAIS"].Valor == "MYANMAR" or Formulario["PAIS"].Valor == "NAURU" or Formulario["PAIS"].Valor == "NEPAL"or Formulario["PAIS"].Valor == "NICARÁGUA" or Formulario["PAIS"].Valor == "PANAMÁ" or Formulario["PAIS"].Valor == "PARAGUAI" or Formulario["PAIS"].Valor == " REP. CENTRO AFRICANA" or Formulario["PAIS"].Valor == "REPÚBLICA TOGOLESA" or Formulario["PAIS"].Valor == "SALOMÃO" or Formulario["PAIS"].Valor == "SAMOA" or Formulario["PAIS"].Valor == "SERRA LEOA" or Formulario["PAIS"].Valor == "SÍRIA" or Formulario["PAIS"].Valor == "SOMÁLIA" or Formulario["PAIS"].Valor == "SRI LANKA" or Formulario["PAIS"].Valor == "TURQUIA" or Formulario["PAIS"].Valor == "TADJIQUISTÃO" or Formulario["PAIS"].Valor == "TAILÂNDIA" or Formulario["PAIS"].Valor == "TIMOR LESTE" or Formulario["PAIS"].Valor == "TONGA" or Formulario["PAIS"].Valor == "TUNÍSIA" or Formulario["PAIS"].Valor == "TURCOMENISTÃO" or Formulario["PAIS"].Valor == "TUVALU" or Formulario["PAIS"].Valor == "VIETNÃ" or Formulario["PAIS"].Valor == "ZIMBÁBUE":
    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "220"
                        
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "200"
            
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "190"
            
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
          Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "180"
          
    else:
          Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "170"
            
        ###################### grupo B    
            
elif Formulario["PAIS"].Valor == "ÁFRICA DO SUL" or Formulario["PAIS"].Valor == "ALBÂNIA" or Formulario["PAIS"].Valor == "ANDORA" or Formulario["PAIS"].Valor == "ARGÉLIA" or Formulario["PAIS"].Valor == "ARGENTINA" or Formulario["PAIS"].Valor == "AUSTRÁLIA" or Formulario["PAIS"].Valor == "BELIZE" or Formulario["PAIS"].Valor == "BÓSNIA-HERZEGÓVINA"  or Formulario["PAIS"].Valor == "BURUNDI" or Formulario["PAIS"].Valor == " CABO VERDE" or Formulario["PAIS"].Valor == "CAMARÕES" or Formulario["PAIS"].Valor == "CAMBOJA" or Formulario["PAIS"].Valor == "CATAR" or Formulario["PAIS"].Valor == "CHADE" or Formulario["PAIS"].Valor == "CHINA" or Formulario["PAIS"].Valor == "CHIPRE" or Formulario["PAIS"].Valor == "COLÔMBIA" or Formulario["PAIS"].Valor == "DOMINICA" or Formulario["PAIS"].Valor == "EGITO" or Formulario["PAIS"].Valor == "ERITRÉIA" or Formulario["PAIS"].Valor == "ESTÔNIA" or Formulario["PAIS"].Valor == "ETIÓPIA" or Formulario["PAIS"].Valor == "GANA" or Formulario["PAIS"].Valor == "GEÓRGIA" or Formulario["PAIS"].Valor == "GUINÉ EQUATORIAL" or Formulario["PAIS"].Valor == "HAITI" or Formulario["PAIS"].Valor == "HUNGRIA" or Formulario["PAIS"].Valor == "IEMEN" or Formulario["PAIS"].Valor == " ILHAS MARSHALL" or Formulario["PAIS"].Valor == "ÍNDIA" or Formulario["PAIS"].Valor == "KIRIBATI" or Formulario["PAIS"].Valor == "LESOTO" or Formulario["PAIS"].Valor == "LÍBIA" or Formulario["PAIS"].Valor == "MACEDÔNIA"or Formulario["PAIS"].Valor == "MADAGASCAR" or Formulario["PAIS"].Valor == "MALAUÍ" or Formulario["PAIS"].Valor == "MICRONÉSIA" or Formulario["PAIS"].Valor == "MOÇAMBIQUE" or Formulario["PAIS"].Valor == "MOLDÁVIA" or Formulario["PAIS"].Valor == "NÍGER" or Formulario["PAIS"].Valor == "NIGÉRIA" or Formulario["PAIS"].Valor == "NOVA ZELÂNDIA" or Formulario["PAIS"].Valor == "PALAU" or Formulario["PAIS"].Valor == "PAPUA NOVA GUINÉ" or Formulario["PAIS"].Valor == "PAQUISTÃO" or Formulario["PAIS"].Valor == "PERU" or Formulario["PAIS"].Valor == "POLÔNIA" or Formulario["PAIS"].Valor == "QUÊNIA" or Formulario["PAIS"].Valor == "REPÚBLICA DOMINICANA" or Formulario["PAIS"].Valor == "ROMÊNIA" or Formulario["PAIS"].Valor == "RUANDA" or Formulario["PAIS"].Valor == " SÃO TOMÉ E PRÍNCIPE" or Formulario["PAIS"].Valor == "SENEGAL" or Formulario["PAIS"].Valor == "TANZÂNIA" or Formulario["PAIS"].Valor == "SUDÃO"  or Formulario["PAIS"].Valor == "URUGUAI" or Formulario["PAIS"].Valor == "UZBEQUISTÃO" or Formulario["PAIS"].Valor == "VENEZUELA":

    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "300"
                    
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "280"

    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "270"
                
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "260"
        
    else:
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "250"
                    
                    

            ################### grupo C

            
elif Formulario["PAIS"].Valor == "ANTÍGUA E BARBUDA" or Formulario["PAIS"].Valor == "ARÁBIA SAUDITA" or Formulario["PAIS"].Valor == "AZERBAIDJÃO" or Formulario["PAIS"].Valor == "BAHAMAS" or Formulario["PAIS"].Valor == "BAREINE" or Formulario["PAIS"].Valor == "BOTSUANA" or Formulario["PAIS"].Valor == "BRUNEI DARUSSALAM" or Formulario["PAIS"].Valor == "BULGÁRIA"  or Formulario["PAIS"].Valor == "CANADÁ" or Formulario["PAIS"].Valor == "CINGAPURA" or Formulario["PAIS"].Valor == "CONGO" or Formulario["PAIS"].Valor == "COSTA DO MARFIM" or Formulario["PAIS"].Valor == "CUBA" or Formulario["PAIS"].Valor == "DJIBUTI" or Formulario["PAIS"].Valor == "EMIRADOS ÁRABES" or Formulario["PAIS"].Valor == "FIJI" or Formulario["PAIS"].Valor == "GABÃO" or Formulario["PAIS"].Valor == "GUATEMALA" or Formulario["PAIS"].Valor == "REPÚBLICA DEMOCRÁTICA DO CONGO" or Formulario["PAIS"].Valor == "JAMAICA" or Formulario["PAIS"].Valor == "JORDÂNIA" or Formulario["PAIS"].Valor == "LETÔNIA" or Formulario["PAIS"].Valor == "LIBÉRIA" or Formulario["PAIS"].Valor == "GEÓRGIA" or Formulario["PAIS"].Valor == "GUINÉ EQUATORIAL" or Formulario["PAIS"].Valor == "HAITI" or Formulario["PAIS"].Valor == "MAURÍCIO" or Formulario["PAIS"].Valor == "MAURITÂNIA" or Formulario["PAIS"].Valor == "MÉXICO" or Formulario["PAIS"].Valor == "MALTA" or Formulario["PAIS"].Valor == " REPÚBLICA TCHECA" or Formulario["PAIS"].Valor == "RÚSSIA" or Formulario["PAIS"].Valor == "SAN MARINO" or Formulario["PAIS"].Valor == "SANTA LÚCIA"or Formulario["PAIS"].Valor == "SÃO CRISTOVÃO E NÉVIS" or Formulario["PAIS"].Valor == "SÃO VICENTE E GRANADINAS" or Formulario["PAIS"].Valor == "TAIWAN" or Formulario["PAIS"].Valor == "TRINIDAD E TOBAGO" or Formulario["PAIS"].Valor == "UCRÂNIA" or Formulario["PAIS"].Valor == "UGANDA" or Formulario["PAIS"].Valor == "ZÂMBIA":
    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "350"
                
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "330"
                    
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "320"
                
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "310"
    
    else:
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "300"     
                    
                
            #################### grupo D 
if Formulario["PAIS"].Valor == "ALEMANHA" or Formulario["PAIS"].Valor == "ANGOLA" or Formulario["PAIS"].Valor == "ÁUSTRIA" or Formulario["PAIS"].Valor == "BARBADOS" or Formulario["PAIS"].Valor == "BÉLGICA"or Formulario["PAIS"].Valor == "CAZAQUISTÃO" or Formulario["PAIS"].Valor == "CORÉIA DO SUL" or Formulario["PAIS"].Valor == "CROÁCIA"  or Formulario["PAIS"].Valor == "DINAMARCA" or Formulario["PAIS"].Valor == "ESPANHA" or Formulario["PAIS"].Valor == "ESTADOS UNIDOS DA AMÉRICA" or Formulario["PAIS"].Valor == "FINLÂNDIA" or Formulario["PAIS"].Valor == "FRANÇA" or Formulario["PAIS"].Valor == "GRANADA" or Formulario["PAIS"].Valor == "GRÉCIA HONG KONG" or Formulario["PAIS"].Valor == "IRLANDA" or Formulario["PAIS"].Valor == "ISLÂNDIA" or Formulario["PAIS"].Valor == "ISRAEL" or Formulario["PAIS"].Valor == "ITÁLIA" or Formulario["PAIS"].Valor == "JAPÃO" or Formulario["PAIS"].Valor == "KUAITE" or Formulario["PAIS"].Valor == "LIECHTENSTEIN" or Formulario["PAIS"].Valor == "LUXEMBURGO" or Formulario["PAIS"].Valor == "MÔNACO" or Formulario["PAIS"].Valor == "MONTENEGRO" or Formulario["PAIS"].Valor == "NORUEGA" or Formulario["PAIS"].Valor == "OMÃ" or Formulario["PAIS"].Valor == "PEÍSES BAIXOS" or Formulario["PAIS"].Valor == "PORTUGAL" or Formulario["PAIS"].Valor == "REINO UNIDO" or Formulario["PAIS"].Valor == "REPÚBLICA QUIRGUIZ" or Formulario["PAIS"].Valor == "SEICHELES" or Formulario["PAIS"].Valor == "SÉRVIA SUAZILÂNDIA" or Formulario["PAIS"].Valor == "SUÉCIA" or Formulario["PAIS"].Valor == "SUÍÇA" or Formulario["PAIS"].Valor == "VANUATU":
    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "460"
                
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "420"
            
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "390"
            
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "370"
                  
                  
    else:
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "350"
```
  - TIPO_DESTINO "Tipo da localidade de destino" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESTINO] obrigatório
  - SAIDA "Saída dia" [DatePicker DateTime → CPE_DESLOCAMENTO.SAIDA] obrigatório
  - RETORNO_DIA "Retorno dia" [DatePicker DateTime → CPE_DESLOCAMENTO.RETORNO_DIA] obrigatório — Coluna=3
  - SAIDA_HORA "Horário da Saída" [TextBox String → CPE_DESLOCAMENTO.SAIDA_HORA] obrigatório — Configuracao={"Mascara":"00:00"}
  - RETORNO_HORA "Horário do Retorno" [TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA] obrigatório — Coluna=3; Configuracao={"Mascara":"00:00"}
**RETORNO_HORA.ScriptModificado**
```python
import clr 
import datetime

data1 = ""
data2 = ""

data1 = Formulario["SAIDA"].Valor
data2 = Formulario["RETORNO_DIA"].Valor
 
delta = data2 - data1
diferenca = delta.Days

if diferenca == 0 or diferenca == '0':
    diferenca = 1


Formulario["DIAS_DE_TRA"].Valor = diferenca
Formulario["DIAS_DE_TRA"].Habilitado = False
```
  - CHECKBOX10 "Marque este campo para calcular o valor da diferença do deslocamento. (Se você alterar algum preenchimento do formulario, desmarque e marque novamente este campo para recalcular o valor)." [CheckBox Boolean → CPE_PESSOAS.CHECKBOX10]
**CHECKBOX10.ScriptModificado**
```python
Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor = Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor - Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor

#if Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor < 0:
#    Formulario["SIM_NAO3"].Valor = "Sim"
#    Formulario["SIM_NAO3"].Habilitado = False
#    Formulario["STRING_ERP"].Visivel = True
#    Formulario["STRING_ERP"].Habilitado = True
#
OrdemServico.Salva()
```
  - LISTA_INVIABILIDADE "Lista de Motivos que inviabilizam a videoconferência" [DropDownList String → CPE_DESLOCAMENTO.LISTA_INVIABILIDADE] obrigatório
  - OBJETIVO_VIAGEM "Objetivo / Informações Adicionais:" [TextBox String → CPE_DESLOCAMENTO.OBJETIVO_VIAGEM] obrigatório
  - MEIO_LOCOMOCAO "Meio de locomoção principal" [DropDownList String → CPE_DESLOCAMENTO.MEIO_LOCOMOCAO] obrigatório
**MEIO_LOCOMOCAO.ScriptModificado**
```python
if Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Próprio":
    Formulario["PREVISAO_DISTANCIA_KM"].Visivel = True
    Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = True
    Formulario["VALOR_DISTANCIA"].Visivel = True
    Formulario["VALOR_DISTANCIA"].Habilitado = True
else:
    Formulario["PREVISAO_DISTANCIA_KM"].Visivel = False
    Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = False
    Formulario["VALOR_DISTANCIA"].Visivel = False
    Formulario["VALOR_DISTANCIA"].Habilitado = False
    
if (Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Próprio" or Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Locado" or Formulario["MEIO_LOCOMOCAO"].Valor == "Carro da Frota" or Formulario["MEIO_LOCOMOCAO"].Valor == "Barco") and Formulario ["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica":
    Formulario["VIAGEM_LONGA"].Visivel = True
    Formulario["VIAGEM_LONGA"].Habilitado = True
else:
    Formulario["VIAGEM_LONGA"].Visivel = False
    Formulario["VIAGEM_LONGA"].Habilitado = False 
    
    
    
##if Formulario["MEIO_LOCOMOCAO"].Valor == "Avião" or Formulario["MEIO_LOCOMOCAO"] == "Ônibus Interestadual":
##    Formulario["VALOR_PASSAGEM"].Visivel = True
##    Formulario["VALOR_PASSAGEM"].Habilitado = True
##    Formulario["VALIDADE_PASSAGEM"].Visivel = True
##    Formulario["VALIDADE_PASSAGEM"].Habilitado = True
##    Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = True
##    Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = True
##else:
##    Formulario["VALOR_PASSAGEM"].Visivel = False
##    Formulario["VALOR_PASSAGEM"].Habilitado = False
##    Formulario["VALIDADE_PASSAGEM"].Visivel = False
##    Formulario["VALIDADE_PASSAGEM"].Habilitado = False
##    Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = False
##    Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = False    
#    
    






##finais de semana um almoço e janta integral
##dias de semana uma refeição reduzida e uma integral
############# calculo dias
#import clr 
#import datetime
#import System.Text
# 
#
#
#zero = 0
#valorRefIntegral = 64.36
#valorRefReduzida = 18.39
#
#
#
#daysOffText = System.Text.StringBuilder()
#
#
###RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
#def isHoliday(day):
#    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
#    #feriados = 0
#    
#    for holiday in holidays.Rows:
#        if day == holiday["DATA"].Date:
#            #feriados += 2
#            return True
#    return False
#
#
#def countHolidays(firstDate, lastDate):
#    totalHolidays = 0
#    currentDay = firstDate
#
#    while currentDay <= lastDate:
#        if isHoliday(currentDay):
#            totalHolidays += 1
#        currentDay = currentDay.AddDays(1)
#
#    return totalHolidays
#
#    
#def workingDays(totalDays, firstDate):
#
#    totalWorkingDays = 0
#    totalDaysOff = 0
#    count = 0
#
#   
#    while count <= totalDays:
#        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
#        day = firstDate.Date.AddDays(count)
#        
#        
#        
#        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
#            totalDaysOff = totalDaysOff + 1
#            daysOffText.AppendLine(" dayOff: "+str(day))
#        
#        count = count + 1
#        totalWorkingDays = totalWorkingDays + 1
#    return totalWorkingDays - totalDaysOff
#   
#
#
#    
#def countSaturdays(firstDate, lastDate):
#    saturdays = 0
#    currentDay = firstDate
#    
#    while currentDay <= lastDate:
#        if (currentDay.DayOfWeek == DayOfWeek.Sunday or currentDay.DayOfWeek == DayOfWeek.Saturday):
#            saturdays += 2
#        currentDay = currentDay.AddDays(1)  # Avance para o próximo dia
#    
#    return saturdays
#
#    
#firstDate = Formulario["SAIDA"].Valor
#lastDate = Formulario["RETORNO_DIA"].Valor
#
#totalDays = (lastDate - firstDate).TotalDays
#count = 0
#
#
#
#
#
#totalWorkingDays = workingDays(totalDays,firstDate)
#holidaysCount = countHolidays(firstDate, lastDate)
#saturdays = countSaturdays(firstDate, lastDate) + holidaysCount * 2
#
#
##Quantidade de refeições Reduzias e integrais
#quantRed = totalWorkingDays
#quantInt = saturdays + totalWorkingDays 
#
#
#
#
#
#
##Atribuindo valor a variável
#saidaHora = Formulario["SAIDA_HORA"].Valor 
#retornoHora = Formulario["RETORNO_HORA"].Valor 
#
##Split de horário, separando hora de minuto
#hora = saidaHora.Split(':');     
#horaRetorno = retornoHora.Split(':');
#
##Atribuindo valor de horário e minuto de acordo com o índice da variável
#horarioSaida = hora[0]
#minutoSaida = hora[1]
#
#horarioRetorno = horaRetorno[0] 
#minutoRetorno = horaRetorno[1]
#
#
#
##SAIDA DIAS ÚTEIS
#
#
##1 maior q o 2
##if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) >= 13 and Convert.ToInt32(horarioSaida) < 21):
##    quantRed = quantRed - 1
##   
##if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) > 21):
##    quantInt = quantInt - 1
##   
##RETORNO DIAS ÚTEIS
##1 menor q o 2   
##if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 13:
##    quantRed = quantRed - 1
##    quantInt = quantInt - 1
##    
##if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 19 and Convert.ToInt32(horarioRetorno) > 13:
##    quantInt = quantInt - 1
##    #teste abaixo
##    quantRed = quantRed - 1
#
#
#
#
#
##DIAS UTEIS
#
#if workingDays(0,firstDate):
#    if (Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0)):
#        quantRed = quantRed - 1
#    if (Convert.ToInt32(horarioSaida) > 21) or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
#        quantInt = quantInt - 1
#if workingDays(0,lastDate):    
#    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantRed = quantRed - 1
#    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantInt = quantInt - 1
##Formulario.ExibeMensagem("hora:"+horarioRetorno.ToString()+" minuto:"+minutoRetorno.ToString())    
################################################################
#    
##SAÍDA FINAIS DE SEMANA E/OU FERIADOS
#
#if not  workingDays(0,firstDate):
#    if Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0):
#        quantInt = quantInt - 1
#    if Convert.ToInt32(horarioSaida) > 21 or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
#        quantInt = quantInt - 1
#if not  workingDays(0,lastDate):
#    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantInt = quantInt - 1
#    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantInt = quantInt - 1   
#
#
#if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA": 
#  
#    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = zero
#    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = zero
#    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
#    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
#    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
#    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
#    Formulario["VALOR_REF_REDUZIDA"].Visivel = False
#    Formulario["VALOR_REF_INTEGRAL"].Visivel = False
#    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
#    
#else:
#    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = quantRed
#    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = quantInt
#    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = True
#    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = True
#    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = True
#    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = True
#    Formulario["VALOR_REF_REDUZIDA"].Visivel = True
#    Formulario["VALOR_REF_INTEGRAL"].Visivel = True
#    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = True
#  
#    
#if quantRed > (totalWorkingDays):
#    mensagem = ("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + str(totalWorkingDays + 1) + " Verifique a Saída e o Retorno.")
#    Formulario.ExibeMensagem(mensagem)    
#    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
#    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
#    
#
############## calculo valor total
#
#refIntegral = Formulario["QTD_REFEICAO_INTEGRAL"].Valor * valorRefIntegral
#refReduzida = Formulario["QTD_REFEICAO_REDUZIDA"].Valor * valorRefReduzida
#valorTotalRefeicoes = refIntegral + refReduzida
#Formulario["VALOR_TOTAL_REFEICAO"].Valor  = valorTotalRefeicoes
#Formulario["VALOR_REF_REDUZIDA"].Valor = refReduzida
#Formulario["VALOR_REF_INTEGRAL"].Valor = refIntegral
#
#
#
#
#
#
```
  - VIAGEM_LONGA "Distância da Viagem de Carro (Programa Valor)" [DropDownList String → CPE_DESLOCAMENTO.VIAGEM_LONGA] obrigatório
  - VALOR_DIFERENCA_DESLOCAMENTO "Valor Diferença (Se o valor for negativo, necessário que o viajante realize a devolução para a BBTS)" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DIFERENCA_DESLOCAMENTO]
  - QTD_REFEICAO_REDUZIDA "Quantidade de refeições reduzidas" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_REDUZIDA] obrigatório
**QTD_REFEICAO_REDUZIDA.ScriptModificado**
```python
import calculos_deslocamento_v29
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.


import clr 
import datetime
import System.Text

Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    
qtdRef = qtdRefeicoes(Formulario["SAIDA"].Valor, Formulario["RETORNO_DIA"].Valor, Formulario["SAIDA_HORA"].Valor, Formulario["RETORNO_HORA"].Valor)


if Convert.ToInt32(qtdRef[0]['integral']) < Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor):
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = qtdRef[0]['integral']
    Formulario.ExibeMensagem("Quantidade de Refeições Integrais Excedida! Máximo permitido: " + qtdRef[0]['integral'].ToString() + " Verifique a Saída e o Retorno.")
if Convert.ToInt32(qtdRef[0]['reduzida']) < Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor):
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = qtdRef[0]['reduzida']
    Formulario.ExibeMensagem("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + qtdRef[0]['reduzida'].ToString() + " Verifique a Saída e o Retorno.")
    
valor = valorRefeicoes(Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor),Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor))

Formulario["VALOR_TOTAL_REFEICAO"].Valor = valor[0]['total']
Formulario["VALOR_REF_REDUZIDA"].Valor = valor[0]['reduzida']
Formulario["VALOR_REF_INTEGRAL"].Valor = valor[0]['integral']
```
  - VALOR_TOTAL_REFEICAO "Valor total previsto para refeições: R$" [TextBox String → CPE_ORDEM_SERVICO.VALOR_TOTAL_REFEICAO] obrigatório — Coluna=2
  - QTD_REFEICAO_INTEGRAL "Quantidade de Refeições Integrais" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_INTEGRAL] obrigatório
**QTD_REFEICAO_INTEGRAL.ScriptModificado**
```python
import calculos_deslocamento_v29
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.


import System
import clr 
import datetime
import System.Text

Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False

qtdRef = qtdRefeicoes(Formulario["SAIDA"].Valor, Formulario["RETORNO_DIA"].Valor, Formulario["SAIDA_HORA"].Valor, Formulario["RETORNO_HORA"].Valor)


if Convert.ToInt32(qtdRef[0]['integral']) < Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor):
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = qtdRef[0]['integral']
    Formulario.ExibeMensagem("Quantidade de Refeições Integrais Excedida! Máximo permitido: " + qtdRef[0]['integral'].ToString() + " Verifique a Saída e o Retorno.")
if Convert.ToInt32(qtdRef[0]['reduzida']) < Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor):
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = qtdRef[0]['reduzida']
    Formulario.ExibeMensagem("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + qtdRef[0]['reduzida'].ToString() + " Verifique a Saída e o Retorno.")
    
valor = valorRefeicoes(Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor),Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor))

Formulario["VALOR_TOTAL_REFEICAO"].Valor = valor[0]['total']
Formulario["VALOR_REF_REDUZIDA"].Valor = valor[0]['reduzida']
Formulario["VALOR_REF_INTEGRAL"].Valor = valor[0]['integral']
```
  - VALOR_REF_REDUZIDA "Valor Refeições Reduzidas" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_REDUZIDA] obrigatório
  - LABEL2 "<h3 style="margin-bottom: -20px"><b>Houve alteração no deslocamento como data de estadia ou valores a receber?</b></h3>" [Label String(2000) → CP_ORDEM_SERVICO.LABEL2] obrigatório
  - CHECKBOX8 "Não" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX8]
**CHECKBOX8.ScriptModificado**
```python
Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor = 0
Formulario["CHECKBOX10"].Valor = True
#Formulario["CHECKBOX9"].Visivel = False
#Formulario["CHECKBOX8"].Visivel = False
Formulario["CHECKBOX9"].Habilitado = False
Formulario["CHECKBOX8"].Habilitado = False

#Formulario["LABEL10"].Visivel = False
#Formulario["LABEL2"].Visivel = False

Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False

Formulario["SIM_NAO2"].Valor = "Não"
Formulario["SIM_NAO3"].Valor = "Não"

Formulario["SIM_NAO2"].Habilitado = False
Formulario["SIM_NAO3"].Habilitado = False

Formulario["VALOR_DOD"].Visivel = False
Formulario["VALORTOTALPB"].Visivel = False
```
  - CHECKBOX9 "Sim" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX9]
**CHECKBOX9.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["FAVORECIDO_DESLOCAMENTO"].Visivel = True
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = True
Formulario["CARGO_DESLOCAMENTO"].Visivel = True
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = True
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = True
Formulario["CELULAR"].Visivel = True
Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
Formulario["SIM_NAO"].Visivel = True
Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True

Formulario["VALOR_DESPESAS"].Valor = ""

Formulario["PARCELA_COMPLEMENTAR"].Habilitado = True

Formulario["TIPO_HOSPEDAGEM"].Habilitado = True

Formulario["VALOR_DESPESAS"].Habilitado = True

Formulario["SIM_NAO2"].Habilitado = True
Formulario["SIM_NAO3"].Habilitado = True

Formulario["TIPO_DESLOCAMENTO"].Visivel = True
Formulario["CIDADE_ORIGEM"].Visivel = True
Formulario["CIDADE_DESTINO"].Visivel = True
Formulario["CIDADE_CLASSIFICACAO"].Visivel = True
Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = True
Formulario["PAIS"].Visivel = True
Formulario["TIPO_DESTINO"].Visivel = True
Formulario["SAIDA"].Visivel = True
Formulario["RETORNO_DIA"].Visivel = True
Formulario["SAIDA_HORA"].Visivel = True
Formulario["RETORNO_HORA"].Visivel = True
Formulario["DIAS_DE_TRA"].Visivel = True
Formulario["TIPO_HOSPEDAGEM"].Visivel = True
Formulario["QUANTIDADE_DIARIA"].Visivel = True
Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = True
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
Formulario["VALOR_DIARIA"].Visivel = True
Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
Formulario["COTACAO_DOLAR"].Visivel = True
Formulario["DIARIA_COTACAO_REAL"].Visivel = True
#Formulario["NUMERO_NT"].Visivel = True
Formulario["PARCELA_COMPLEMENTAR"].Visivel = True
Formulario["TOTAL_COMPLEMENTAR"].Visivel = True
Formulario["LISTA_INVIABILIDADE"].Visivel = True
Formulario["MEIO_LOCOMOCAO"].Visivel = True
Formulario["VIAGEM_LONGA"].Visivel = True
Formulario["SIM_NAO_REFEICAO"].Visivel = True
Formulario["PREVISAO_DISTANCIA_KM"].Visivel = True
Formulario["VALOR_DISTANCIA"].Visivel = True
Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = True
Formulario["VALOR_TOTAL_REFEICAO"].Visivel = True
Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = True
Formulario["VALOR_REF_REDUZIDA"].Visivel = True
Formulario["VALOR_REF_INTEGRAL"].Visivel = True
Formulario["DESCRICAO_DESPESAS"].Visivel = True
Formulario["VALOR_DESPESAS"].Visivel = True
Formulario["VALOR_TOTAL_ADIANTAMENTO"].Visivel = True

#Formulario["MEIO_LOCOMOCAO"].Habilitado = True

#Formulario["TIPO_DESLOCAMENTO"].Valor = ""
#Formulario["CIDADE_CLASSIFICACAO"].Valor = ""
#Formulario["TIPO_DESTINO"].Valor = ""
Formulario["RETORNO_DIA"].Valor = None
#Formulario["SAIDA_HORA"].Valor = ""
Formulario["RETORNO_HORA"].Valor = ""
Formulario["DIAS_DE_TRA"].Valor = ""
Formulario["TIPO_HOSPEDAGEM"].Valor = ""
Formulario["QUANTIDADE_DIARIA"].Valor = ""
Formulario["VALOR_DIARIA_DOLAR"].Valor = ""
#Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = ""
#Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = ""
Formulario["VALOR_DIARIA"].Valor = ""
Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = ""
Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = ""
Formulario["VALOR_TOTAL_DIARIA"].Valor = ""
Formulario["COTACAO_DOLAR"].Valor = ""
#Formulario["DIARIA_COTACAO_REAL"].Valor = ""
#Formulario["NUMERO_NT"].Valor = ""
Formulario["PARCELA_COMPLEMENTAR"].Valor = ""
Formulario["TOTAL_COMPLEMENTAR"].Valor = ""
Formulario["MEIO_LOCOMOCAO"].Valor = ""
Formulario["VIAGEM_LONGA"].Valor = ""
Formulario["SIM_NAO_REFEICAO"].Valor = ""
Formulario["PREVISAO_DISTANCIA_KM"].Valor = ""
#Formulario["VALOR_DISTANCIA"].Valor = ""
Formulario["QTD_REFEICAO_REDUZIDA"].Valor = ""
Formulario["VALOR_TOTAL_REFEICAO"].Valor = ""
Formulario["QTD_REFEICAO_INTEGRAL"].Valor = ""
Formulario["VALOR_REF_REDUZIDA"].Valor = ""
Formulario["VALOR_REF_INTEGRAL"].Valor = ""
Formulario["DESCRICAO_DESPESAS"].Valor = ""

#SCRIPT PARA LIMPAR OS DADOS DO FORMULARIO #######################
Formulario["QUANTIDADE_DIARIA"].Visivel = False
Formulario["QUANTIDADE_DIARIA"].Habilitado = False
Formulario["VALOR_DIARIA"].Visivel = False
Formulario["VALOR_DIARIA"].Habilitado = False
#Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
#Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
#Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
#Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
#Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
Formulario["DIARIA_COTACAO_REAL"].Visivel = False
Formulario["DIARIA_COTACAO_REAL"].Habilitado = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False

Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False  


Formulario["VALOR_REF_INTEGRAL"].Visivel = False
Formulario["VALOR_REF_INTEGRAL"].Habilitado = False
Formulario["VALOR_REF_REDUZIDA"].Visivel = False
Formulario["VALOR_REF_REDUZIDA"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = True
#Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = True
Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
#Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False        
Formulario["COTACAO_DOLAR"].Visivel = False
Formulario["COTACAO_DOLAR"].Habilitado = False  


#Formulario["VALOR_DISTANCIA"].Valor = "0"
Formulario["VALOR_TOTAL_REFEICAO"].Valor = "0"
Formulario["QTD_REFEICAO_REDUZIDA"].Valor = "0"




Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = "0"
Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "0"
#Formulario["VALOR_DIARIA_DOLAR"].Valor = "0"
#Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "0"
Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False




Formulario["CARGO_DESLOCAMENTO"].Visivel = False
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = False
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = False
Formulario["CARGO_DESLOCAMENTO"].Habilitado = False
Formulario["FUNCAO_DESLOCAMENTO"].Habilitado = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Habilitado = False
Formulario["MATRICULA_DESLOCAMENTO"].Habilitado = False

    

Formulario["PREVISAO_DISTANCIA_KM"].Visivel = False
Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = False 
Formulario["VALOR_DISTANCIA"].Visivel = False
Formulario["VALOR_DISTANCIA"].Habilitado = False
#Formulario["VALOR_PASSAGEM"].Visivel = False
#Formulario["VALOR_PASSAGEM"].Habilitado = False
#Formulario["VALIDADE_PASSAGEM"].Visivel = False
#Formulario["VALIDADE_PASSAGEM"].Habilitado = False
#Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = False
#Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = False


#Formulario["QUANTIDADE_DIARIA"].Visivel = True
#Formulario["QUANTIDADE_DIARIA"].Habilitado = True
#Formulario["VALOR_DIARIA"].Visivel = False
#Formulario["VALOR_DIARIA"].Habilitado = False
#Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False

Formulario["CIDADE_DESTINO"].Visivel = True
Formulario["CIDADE_DESTINO"].Habilitado = False
#Formulario["CIDADE_CLASSIFICACAO"].Visivel = False
Formulario["CIDADE_CLASSIFICACAO"].Habilitado = False
Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = False
Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = False
Formulario["PAIS"].Visivel = False
Formulario["PAIS"].Habilitado = False


Formulario["SIM_NAO"].Visivel = False

Formulario["PARCELA_COMPLEMENTAR"].Visivel = True
Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False   
Formulario["TOTAL_COMPLEMENTAR"].Visivel = True
Formulario["TOTAL_COMPLEMENTAR"].Habilitado = False  

Formulario["VIAGEM_LONGA"].Visivel = False
Formulario["VIAGEM_LONGA"].Habilitado = False 

Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False 

Formulario["LABEL1"].Visivel = False
Formulario["LABEL1"].Habilitado = False
Formulario["NUMERO_NT"].Visivel = False
Formulario["NUMERO_NT"].Habilitado = False


#LISTA DE PAÍSES

Formulario["PAIS"].Itens = "AFEGANISTÃO;ARMÊNIA;BANGLADESH;BELARUS;BENIN;BOLÍVIA;BURKINAFASSO;BUTÃO;CHILE; COMORES;REPÚBLICA POPULAR DEMOCRÁTICA DA CORÉIA;COSTA RICA;EL SALVADOR; EQUADOR;ESLOVÊNIA;FILIPINAS;GÂMBIA;GUIANA;GUINÉ BISSAU;GUINÉ;HONDURAS;INDONÉSIA;IRÃ;IRAQUE;LAOS;LÍBANO;MALÁSIA;MALDIVAS; MARROCOS;MONGÓLIA;MYANMAR;NAMÍBIA;NAURU;NEPAL;NICARÁGUA;PANAMÁ;PARAGUAI; REP. CENTRO AFRICANA;REPÚBLICA TOGOLESA;SALOMÃO;SAMOA;SERRA LEOA;SÍRIA;SOMÁLIA;SRI LANKA;SURINAME;TADJIQUISTÃO;TAILÂNDIA;TIMOR LESTE;TONGA;TUNÍSIA;TURCOMENISTÃO;TURQUIA;TUVALU;VIETNÃ;ZIMBÁBUE;ÁFRICA DO SUL;ALBÂNIA;ANDORA;ARGÉLIA;ARGENTINA;AUSTRÁLIA;BELIZE;BÓSNIA-HERZEGÓVINA;BURUNDI;CABO VERDE;CAMARÕES;CAMBOJA;CATAR;CHADE;CHINA;CHIPRE;COLÔMBIA;DOMINICA;EGITO;ERITRÉIA;ESTÔNIA;ETIÓPIA;GANA;GEÓRGIA;GUINÉ EQUATORIAL;HAITI;HUNGRIA;IEMEN;ILHAS MARSHALL;ÍNDIA;KIRIBATI;LESOTO;LÍBIA;MACEDÔNIA;MADAGASCAR;MALAUÍ;MICRONÉSIA;MOÇAMBIQUE;MOLDÁVIA;NÍGER;NIGÉRIA;NOVA ZELÂNDIA;PALAU;PAPUA NOVAGUINÉ;PAQUISTÃO;PERU;POLÔNIA;QUÊNIA;REPÚBLICA DOMINICANA;ROMÊNIA;RUANDA;SÃO TOMÉ E PRÍNCIPE;SENEGAL; SUDÃO;TANZÂNIA;URUGUAI;UZBEQUISTÃO;VENEZUELA;ANTÍGUA E BARBUDA;ARÁBIA SAUDITA;AZERBAIDJÃO;BAHAMAS;BAREINE;BOTSUANA;BRUNEI DARUSSALAM;BULGÁRIA;CANADÁ;CINGAPURA;CONGO;COSTA DO MARFIM;CUBA;DJIBUTI;EMIRADOS ÁRABES;FIJI;GABÃO;GUATEMALA;JAMAICA;JORDÂNIA;LETÔNIA;LIBÉRIA;LITUÂNIA;MALI;MALTA;MAURÍCIO;MAURITÂNIA;MÉXICO;REPÚBLICA DEMOCRÁTICA DO CONGO;REPÚBLICA TCHECA;RÚSSIA;SAN MARINO;SANTA LÚCIA;SÃO CRISTOVÃO E NÉVIS;SÃO VICENTE EGRANADINAS;TAIWAN;TRINIDAD E TOBAGO;UCRÂNIA;UGANDA;ZÂMBIA;ALEMANHA;ANGOLA;ÁUSTRIA;BARBADOS;BÉLGICA;CAZAQUISTÃO;CORÉIA DOSUL;CROÁCIA;DINAMARCA;ESPANHA;ESTADOS UNIDOS DA AMÉRICA;FINLÂNDIA;FRANÇA;GRANADA;GRÉCIA;HONG KONG;IRLANDA;ISLÂNDIA;ISRAEL;ITÁLIA;JAPÃO;KUAITE;LIECHTENSTEIN;LUXEMBURGO;MÔNACO;MONTENEGRO;NORUEGA;OMÃ;PEÍSES BAIXOS;PORTUGAL;REINO UNIDO;REPÚBLICA QUIRGUIZ;SEICHELES;SÉRVIA SUAZILÂNDIA;SUÉCIA;SUÍÇA;VANUATU"




#INICIO SCRIPT PARA FAVORECIDO DESLOCAMENTO###############################################
Formulario["FAVORECIDO_DESLOCAMENTO"].Habilitado = False

Formulario["CARGO_DESLOCAMENTO"].Visivel = True
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = True
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = True
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = True

Formulario["CARGO_DESLOCAMENTO"].Habilitado = False
Formulario["FUNCAO_DESLOCAMENTO"].Habilitado = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Habilitado = False
Formulario["MATRICULA_DESLOCAMENTO"].Habilitado = False

Formulario["CARGO_DESLOCAMENTO"].Valor = None
Formulario["FUNCAO_DESLOCAMENTO"].Valor = None
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = None
Formulario["MATRICULA_DESLOCAMENTO"].Valor = None

cargo = ""
funcao = ""
desc_colaborador = ""
matricula = ""

if Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != "" or Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["ORGAO_FAVORECIDO"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT SUBSTR(c.CARGO,INSTR(c.CARGO,'|')+1,LENGTH(c.CARGO)) AS CARGO1, c.FUNCAO_GRATIFICADA, c.DESC_COLABORADOR, c.MATRICULA, c.FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND C.NUMERO_SUBCR_NIVEL1 = O.SIGLA AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    #lista = Utils.ExecuteDataTable("SELECT SUBSTR(CARGO,INSTR(CARGO,'|')+1,LENGTH(CARGO)) AS CARGO1, FUNCAO_GRATIFICADA, DESC_COLABORADOR, MATRICULA, FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND LPAD(C.NUMERO_SUBCR_NIVEL1,5) = LPAD(O.SIGLA,5) AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    for linha in lista.Rows:
        cargo = linha["CARGO1"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()

    Formulario["CARGO_DESLOCAMENTO"].Valor = cargo.ToString()
    Formulario["FUNCAO_DESLOCAMENTO"].Valor = funcao.ToString()
    Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = desc_colaborador.ToString()
    Formulario["MATRICULA_DESLOCAMENTO"].Valor = matricula.ToString()

if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False
else:
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
    Formulario["ACOMPANHANDO_GRUPO_A"].Valor = "Não"
    
#FIM SCRIPT PARA FAVORECIDO DESLOCAMENTO###############################################

Formulario["CHECKBOX8"].Valor = False
Formulario["CHECKBOX8"].Habilitado = False
Formulario["CHECKBOX9"].Habilitado = False
Formulario["LABEL10"].Visivel = True
#Formulario["LABEL2"].Visivel = False

if OrdemServico["TIPO_DESLOCAMENTO"] == "Viagem a Serviço - Internacional":
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
    #Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
    Formulario["COTACAO_DOLAR"].Visivel = True
    Formulario["COTACAO_DOLAR"].Habilitado = True  
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
    #Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = True
    #Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = True
    Formulario["PAIS"].Visivel = True
    #Formulario["PAIS"].Habilitado = True       
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
    Formulario["TIPO_HOSPEDAGEM"].Visivel = True
    Formulario["TIPO_HOSPEDAGEM"].Habilitado = False    
    Formulario["TIPO_HOSPEDAGEM"].Valor = "Avulsa"
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True    
    
    Formulario["CIDADE_DESTINO"].Visivel = False
    Formulario["CIDADE_DESTINO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["DIARIA_COTACAO_REAL"].Visivel = True
    #Formulario["DIARIA_COTACAO_REAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    
    Formulario["LABEL1"].Visivel = True
    Formulario["LABEL1"].Habilitado = True
    Formulario["NUMERO_NT"].Visivel =  True
    Formulario["NUMERO_NT"].Habilitado = True
```
  - LABEL10 "<h3><b>Preencha com os dados de deslocamento.</b></h3>" [Label String(700) → CPE_PDCI2019.LABEL10] obrigatório
  - FAVORECIDO_DESLOCAMENTO "Favorecido" [DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO] obrigatório
**FAVORECIDO_DESLOCAMENTO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["CARGO_DESLOCAMENTO"].Visivel = True
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = True
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = True
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = True



Formulario["CARGO_DESLOCAMENTO"].Habilitado = False
Formulario["FUNCAO_DESLOCAMENTO"].Habilitado = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Habilitado = False
Formulario["MATRICULA_DESLOCAMENTO"].Habilitado = False



Formulario["CARGO_DESLOCAMENTO"].Valor = None
Formulario["FUNCAO_DESLOCAMENTO"].Valor = None
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = None
Formulario["MATRICULA_DESLOCAMENTO"].Valor = None



cargo = ""
funcao = ""
desc_colaborador = ""
matricula = ""

if Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != "" or Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["ORGAO_FAVORECIDO"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT SUBSTR(c.CARGO,INSTR(c.CARGO,'|')+1,LENGTH(c.CARGO)) AS CARGO1, c.FUNCAO_GRATIFICADA, c.DESC_COLABORADOR, c.MATRICULA, c.FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"' AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    #lista = Utils.ExecuteDataTable("SELECT SUBSTR(CARGO,INSTR(CARGO,'|')+1,LENGTH(CARGO)) AS CARGO1, FUNCAO_GRATIFICADA, DESC_COLABORADOR, MATRICULA, FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND LPAD(C.NUMERO_SUBCR_NIVEL1,5) = LPAD(O.SIGLA,5) AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    for linha in lista.Rows:
        cargo = linha["CARGO1"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()

    Formulario["CARGO_DESLOCAMENTO"].Valor = cargo.ToString()
    Formulario["FUNCAO_DESLOCAMENTO"].Valor = funcao.ToString()
    Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = desc_colaborador.ToString()
    Formulario["MATRICULA_DESLOCAMENTO"].Valor = matricula.ToString()

    
        


if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False
else:
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
    Formulario["ACOMPANHANDO_GRUPO_A"].Valor = "Não"
```
  - MATRICULA_DESLOCAMENTO "Matrícula" [TextBox Integer → CPE_DESLOCAMENTO.MATRICULA_DESLOCAMENTO]
  - CARGO_DESLOCAMENTO "Cargo" [TextBox String → CPE_DESLOCAMENTO.CARGO_DESLOCAMENTO]
  - FUNCAO_DESLOCAMENTO "Função" [TextBox String → CPE_DESLOCAMENTO.FUNCAO_DESLOCAMENTO]
  - DESC_COLABORADOR_DESLOCAMENTO "Tipo de Colaborador" [TextBox String → CPE_DESLOCAMENTO.DESC_COLABORADOR_DESLOCAMENTO]
  - CELULAR "Celular do Favorecido" [TextBox String → CP_ORDEM_SERVICO.CELULAR] — Configuracao={"Mascara":"00000000000"}
  - ACOMPANHANDO_GRUPO_A "Estará acompanhando Presidente / Diretor / Conselheiro " [DropDownList String → CPE_DESLOCAMENTO.ACOMPANHANDO_GRUPO_A] obrigatório
**ACOMPANHANDO_GRUPO_A.ScriptModificado**
```python
if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True 
    Formulario["NUM_ABERTURA_CHAMADO"].Habilitado = True 
    Formulario["SIM_NAO"].Visivel = False
    Formulario["SIM_NAO"].Habilitado = False 
  

else:
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False 
    Formulario["SIM_NAO"].Visivel = True
    Formulario["SIM_NAO"].Habilitado = True
     
    
    
#    
#if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Não":
#    Formulario["SIM_NAO"].Visivel = True
#    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True 
#    Formulario["NUM_ABERTURA_CHAMADO"].Habilitado = True 
#
#else:
#     Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
#
```
  - SIM_NAO "Estará acompanhado Gerente Executivo / Gerente de Projeto I / Assesor Executivo / Superintendente?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
if Formulario["SIM_NAO"].Valor == "Sim":
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True
else:
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
```
  - NUM_ABERTURA_CHAMADO "N° da Abertura de Chamado do Deslocamento a Serviço de Quem Está Acompanhando" [TextBox String → CPE_DESLOCAMENTO.NUM_ABERTURA_CHAMADO] obrigatório
  - TIPO_DESLOCAMENTO "Tipo de Deslocamento" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESLOCAMENTO] obrigatório
**TIPO_DESLOCAMENTO.ScriptModificado**
```python
##Viagem internacional

if Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
    Formulario["COTACAO_DOLAR"].Visivel = True
    Formulario["COTACAO_DOLAR"].Habilitado = True  
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = True
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = True
    Formulario["PAIS"].Visivel = True
    Formulario["PAIS"].Habilitado = True       
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
    Formulario["TIPO_HOSPEDAGEM"].Visivel = True
    Formulario["TIPO_HOSPEDAGEM"].Habilitado = False    
    Formulario["TIPO_HOSPEDAGEM"].Valor = "Avulsa"
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True    
    
    Formulario["CIDADE_DESTINO"].Visivel = False
    Formulario["CIDADE_DESTINO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["DIARIA_COTACAO_REAL"].Visivel = True
    Formulario["DIARIA_COTACAO_REAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    
    Formulario["LABEL1"].Visivel = True
    Formulario["LABEL1"].Habilitado = True
    Formulario["NUMERO_NT"].Visivel =  True
    Formulario["NUMERO_NT"].Habilitado = True  
    
else:
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    Formulario["COTACAO_DOLAR"].Visivel = False
    Formulario["COTACAO_DOLAR"].Habilitado = False   
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = False
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = False
    Formulario["PAIS"].Visivel = False
    Formulario["PAIS"].Habilitado = False  
    Formulario["TIPO_HOSPEDAGEM"].Habilitado = True
    
    Formulario["CIDADE_DESTINO"].Visivel = True
    Formulario["CIDADE_DESTINO"].Habilitado = True
    Formulario["CIDADE_DESTINO"].Visivel = True
    Formulario["CIDADE_DESTINO"].Habilitado = True
    Formulario["CIDADE_CLASSIFICACAO"].Visivel = True
    Formulario["VALOR_DIARIA"].Visivel = True
    Formulario["VALOR_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
    Formulario["DIARIA_COTACAO_REAL"].Visivel = False
    Formulario["DIARIA_COTACAO_REAL"].Habilitado = False
    
    Formulario["LABEL1"].Visivel =  False
    Formulario["LABEL1"].Habilitado = False
    Formulario["NUMERO_NT"].Visivel =  False
    Formulario["NUMERO_NT"].Habilitado = False
    
    Formulario["VALOR_DIARIA"].Valor = ""
```
  - CIDADE_ORIGEM "Cidade de Origem" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_ORIGEM]
  - VALOR_DIARIA_DOLAR "Valor Diária US$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_DOLAR] obrigatório
**VALOR_DIARIA_DOLAR.ScriptModificado**
```python
if Convert.ToDecimal(Formulario["VALOR_DIARIA_DOLAR"].Valor) >= Convert.ToDecimal(Formulario["CAMPO_VALIDACAO_DOLAR"].Valor):
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = Formulario["CAMPO_VALIDACAO_DOLAR"].Valor
else:
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = Formulario["VALOR_DIARIA_DOLAR"].Valor
    
    
Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True

valorTotal1 = 0

quantDiaria = Convert.ToDecimal(Formulario["QUANTIDADE_DIARIA"].Valor)
valorDiaria = Convert.ToDecimal(Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor)

valorTotal1 = quantDiaria * valorDiaria 

Formulario["VALOR_TOTAL_DIARIA"].Valor =  valorTotal1 


#OrdemServico["VALOR_TOTAL_DIARIA"] = valorTotal1
```
  - CAMPO_VALIDACAO_DOLAR "Diária máxima autorizada US$ (TAB320-001)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DOLAR] obrigatório — Coluna=2
  - DIARIA_AUTORIZADO_INTERNACIONAL "Valor Diária Autorizado US$" [TextBox String → CPE_DESLOCAMENTO.DIARIA_AUTORIZADO_INTERNACIONAL] obrigatório — Coluna=3
  - VALOR_DIARIA "Valor da Diaria R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DIARIA] obrigatório
**VALOR_DIARIA.ScriptModificado**
```python
if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
         Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = Formulario["VALOR_DIARIA"].Valor
    



if Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "PRESIDENTE": 
     Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = Formulario["VALOR_DIARIA"].Valor


     
     
if Convert.ToDecimal(Formulario["VALOR_DIARIA"].Valor) >= Convert.ToDecimal(Formulario["CAMPO_VALIDACAO_DIARIA"].Valor):
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["CAMPO_VALIDACAO_DIARIA"].Valor
else:
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
    
    
Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True

valorTotal = 0

quantDiaria = Convert.ToDecimal(Formulario["QUANTIDADE_DIARIA"].Valor)
valorDiaria = Convert.ToDecimal(Formulario["VALOR_DIARIA_AUTORIZADO"].Valor)

valorTotal = quantDiaria * valorDiaria 

Formulario["VALOR_TOTAL_DIARIA"].Valor =  valorTotal 


OrdemServico["VALOR_TOTAL_DIARIA"] = valorTotal
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Bloco 2
  - DescricaoDetalhada (nativo)
  - SIM_NAO2 "O funcionário/Gestor receberá um valor não previsto no pedido inicial do deslocamento?" [DropDownList String → CPE_CSC.SIM_NAO2] obrigatório
**SIM_NAO2.ScriptModificado**
```python
if Formulario["SIM_NAO2"].Valor == "Sim":    
#    Formulario["NOME_PROJETO"].Habilitado = True    
#    Formulario["NOME_PROJETO"].Visivel = True    
    Formulario["VALOR_DOD"].Habilitado = True    
    Formulario["VALOR_DOD"].Visivel = True
#    Formulario["VALOR_EXTRA"].Habilitado = True    
#    Formulario["VALOR_EXTRA"].Visivel = True  
    #Formulario["SIM_NAO4"].Habilitado = True    
    #Formulario["SIM_NAO4"].Visivel = True     
    
else:    

#    Formulario["NOME_PROJETO"].Habilitado = False    
#    Formulario["NOME_PROJETO"].Visivel = False    
    Formulario["VALOR_DOD"].Habilitado = False    
    Formulario["VALOR_DOD"].Visivel = False
#    Formulario["VALOR_EXTRA"].Habilitado = False    
#    Formulario["VALOR_EXTRA"].Visivel = False
    #Formulario["SIM_NAO4"].Habilitado = False    
    #Formulario["SIM_NAO4"].Visivel = False
    Formulario["VALOR_DOD"].Valor = 0
    
if Formulario["SIM_NAO2"].Valor == "Sim" and Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor != "": 
    Formulario["VALOR_DOD"].Valor = Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor
    Formulario["VALOR_DOD"].Habilitado = False
```
  - VALOR_DOD "Valor do reembolso:" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD] obrigatório
**VALOR_DOD.ScriptModificado**
```python
if Formulario["VALOR_DOD"].Valor >= 0:
    Formulario.ExibeMensagem("IMPORTANTE: Clique no botão SALVAR antes de cálcular o custo total da viagem.")
    OrdemServico.Salva
```
  - SIM_NAO3 "Haverá necessidade de devolução de valor para a BBTS?" [DropDownList String → CPE_CSC.SIM_NAO3] obrigatório
**SIM_NAO3.ScriptModificado**
```python
if Formulario["SIM_NAO3"].Valor == "Sim":
    Formulario["STRING_ERP"].Habilitado = True
    Formulario["STRING_ERP"].Visivel = True
    Formulario["VALORTOTALPB"].Habilitado = True
    Formulario["VALORTOTALPB"].Visivel = True
else:
    Formulario["STRING_ERP"].Habilitado = False
    Formulario["STRING_ERP"].Visivel = False
    Formulario["VALORTOTALPB"].Habilitado = False
    Formulario["VALORTOTALPB"].Visivel = False
   
if Formulario["SIM_NAO3"].Valor == "Sim" and Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor != "" and Convert.ToDecimal(Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor) < 0: 
    Formulario["VALORTOTALPB"].Valor = Convert.ToDecimal(Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor) * -1
    Formulario["VALORTOTALPB"].Habilitado = False
    
OrdemServico.Salva()
```
  - STRING_ERP "Descrição dos valores a devolver" [TextBox String → CP_ORDEM_SERVICO.STRING_ERP] obrigatório
  - VALORTOTALPB "Valor de devolução:" [TextBox Decimal → CPE_PRJ_BB.VALORTOTALPB] obrigatório
**VALORTOTALPB.ScriptModificado**
```python
#if Formulario["VALORTOTALPB"].Valor >= 0:
    #Formulario.ExibeMensagem("IMPORTANTE: Clique no botão SALVAR antes de cálcular o custo total da viagem.")
    #OrdemServico.Salva
```
  - VALOR_TOT_PREST_CONTAS "Valor total a prestar contas com documentação (incluindo comprovante de devolução, se houver)" [TextBox Decimal → CPE_CSC.VALOR_TOT_PREST_CONTAS]
  - VALOR_TOTAL_ADIANTAMENTO "Valor total do adiantamento ao empregado" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_ADIANTAMENTO]
  - CUSTO_TOT_DESLOC "Custo total do deslocamento (descontado o valor de devolução)" [TextBox Decimal → CPE_HOMOLOGACAO.CUSTO_TOT_DESLOC] obrigatório
  - COMBOBOX_CONFIRMA_TREINAMENTO "Clique aqui para verificar o custo total da viagem" [CheckBox Boolean → CPE_PESSOAS.COMBOBOX_CONFIRMA_TREINAMENTO] obrigatório
**COMBOBOX_CONFIRMA_TREINAMENTO.ScriptModificado**
```python
zero = 0

if Formulario["SIM_NAO2"].Valor == "Sim":
    despesas = Convert.ToDecimal(Formulario["VALOR_DOD"].Valor)  
else:
    despesas = 0



valorDistCampo = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)

gastorNPrevi = Formulario["SIM_NAO2"].Valor
devolucao = Formulario["SIM_NAO3"].Valor
tipoHospeda = Formulario["TIPO_HOSPEDAGEM"].Valor
cargoDes = Formulario["CARGO_DESLOCAMENTO"].Valor
funcaoDes = Formulario["FUNCAO_DESLOCAMENTO"].Valor
tipoDeslocament = Formulario["TIPO_DESLOCAMENTO"].Valor
valorReembolso = Convert.ToDecimal(Formulario["VALOR_DOD"].Valor)
outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
diariaAvulsaSemPrestarContas = 0

#inicia a variavel valorTotalPrestContas
valorTotalPrestContas = 0

#Inicia a variavel totalSemPrestContas
totalSemPrestContas = 0
   

if gastorNPrevi == "Não":
    Formulario["VALORTOTSEMCOMPROV"].Valor = zero
    
    #novo - adiciona ao campo do formulario
    Formulario["VALORTOTSEMCOMPROV"].Valor = 0

if devolucao == "Não":
    Formulario["VALOR_TOT_PREST_CONTAS"].Valor = zero
    
    #novo - adiciona ao campo do formulario
    Formulario["VALOR_TOT_PREST_CONTAS"].Valor = 0


if tipoHospeda == "Avulsa":
    diariaAvulsa = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)  
else:
    diariaAvulsa = 0
    diariaAvulsaSemPrestarContas = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
 
     
if valorDistCampo != 0:
    valorDist = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)

else:
    valorDist = 0 
    

if Formulario["COMBOBOX_CONFIRMA_TREINAMENTO"].Valor == True:

    #Se for viagem nacional contabilizar outras despesas, diaria avulsa e valor distancia
    #valorTotalPrestContas = outrasDespesas + diariaAvulsa + valorDist + valorReembolso
    if OrdemServico["TIPO_DESLOCAMENTO"] != "Viagem a Serviço - Internacional":
        valorTotalPrestContas = outrasDespesas + diariaAvulsa + valorDist
        Formulario['VALOR_TOT_PREST_CONTAS'].Valor = valorTotalPrestContas
   
    #Se for viagem internacional contabilizar apenas outras despesas
    #valorTotalPrestContas = outrasDespesas
    if OrdemServico["TIPO_DESLOCAMENTO"] == "Viagem a Serviço - Internacional":
        valorTotalPrestContas = outrasDespesas
        Formulario['VALOR_TOT_PREST_CONTAS'].Valor = valorTotalPrestContas
    
    
#else:
 #   Formulario['VALOR_TOT_PREST_CONTAS'].Valor = 0
      


#Valores sem necessidade de prestação de contas

refeicoes = 0
hospeda = 0
complementar = 0
valorPassagens = Convert.ToDecimal(OrdemServico.GetCustom('CSC_VALOR1_TOTAL'))
valorCarro = Convert.ToDecimal(OrdemServico.GetCustom('CSC_VALOR2'))

if cargoDes == "PRESIDENTE" or cargoDes == "DIRETOR" or cargoDes == "CONSELHEIRO FISCAL" or cargoDes == "CONSELHEIRO DE ADMINISTRACAO" or cargoDes == "MEMBRO COMITE DE AUDITORIA" or funcaoDes == "PRESIDENTE" or  funcaoDes == "DIRETOR" or  funcaoDes == "CONSELHEIRO  FISCAL" or funcaoDes == "CONSELHEIRO DE ADMINISTRACAO" or funcaoDes == "MEMBRO COMITE DE AUDITORIA":
    refeicoes = 0
else:
    refeicoes = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)

#valor total da diária informada pelo Cesec após seleção no argo. CSC_VALOR1 = Valor total das diárias    
if tipoHospeda == "Contratada":
   hospeda = Convert.ToDecimal(OrdemServico.GetCustom("CSC_VALOR1"))
   
elif tipoHospeda == "Sem Hospedagem":
   hospeda = 0
   
 
if cargoDes == "PRESIDENTE" or cargoDes == "DIRETOR" or cargoDes == "MEMBRO COMITE DE AUDITORIA" or cargoDes == "CONSELHEIRO DE ADMINISTRACAO" or cargoDes == "CONSELHEIRO FISCAL" or funcaoDes == "PRESIDENTE" or  funcaoDes == "DIRETOR" or funcaoDes == "MEMBRO COMITE DE AUDITORIA" or  funcaoDes == "CONSELHEIRO DE ADMINISTRACAO" or funcaoDes == "CONSELHEIRO  FISCAL" or tipoDeslocament == "Viagem a Serviço - Internacional":
    complementar = 0
else:
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)

if OrdemServico["TIPO_DESLOCAMENTO"] != "Viagem a Serviço - Internacional":
    #VALOR TOTAL SEM NECESSIDADE DE PRESTAÇÃO DE CONTAS COM DOCUMENTAÇÃO
    #totalSemPrestContas = 0    
    if tipoHospeda == "Contratada": 
        #totalSemPrestContas = complementar + hospeda + refeicoes + valorPassagens + valorCarro + valorReembolso
        totalSemPrestContas = complementar + hospeda + refeicoes + valorPassagens + valorCarro
    #    Formulario['VALORTOTSEMCOMPROV'].Valor = totalSemPrestContas
        
    if tipoHospeda == "Avulsa" or tipoHospeda == "Sem Hospedagem":
        #totalSemPrestContas = complementar + hospeda + refeicoes + valorPassagens + valorCarro + valorReembolso
        #totalSemPrestContas = complementar + refeicoes + valorPassagens + valorCarro + valorReembolso
        totalSemPrestContas = complementar + refeicoes + valorPassagens + valorCarro
    #    Formulario['VALORTOTSEMCOMPROV'].Valor = totalSemPrestContas

    if tipoHospeda == "Avulsa SEM apresentação de NF":
        #totalSemPrestContas = complementar + hospeda + refeicoes + valorPassagens + valorCarro + valorReembolso
        #totalSemPrestContas = complementar + refeicoes + valorPassagens + valorCarro + valorReembolso
        totalSemPrestContas = complementar + refeicoes + valorPassagens + valorCarro + diariaAvulsaSemPrestarContas
    #    Formulario['VALORTOTSEMCOMPROV'].Valor = totalSemPrestContas     
        
    if totalSemPrestContas != 0:
        Formulario['VALORTOTSEMCOMPROV'].Valor = totalSemPrestContas
    #else:
    #    Formulario['VALORTOTSEMCOMPROV'].Valor = totalSemPrestContas
    
if OrdemServico["TIPO_DESLOCAMENTO"] == "Viagem a Serviço - Internacional":
    diariaCotacaoReal = Convert.ToDecimal(Formulario["DIARIA_COTACAO_REAL"].Valor)
    totalSemPrestContas = diariaCotacaoReal
    Formulario['VALORTOTSEMCOMPROV'].Valor = totalSemPrestContas

##########################################################################################################

    

Formulario['CUSTO_TOT_DESLOC'].Visivel = True    
Formulario["VALOR_TOT_PREST_CONTAS"].Visivel = True
Formulario["VALORTOTSEMCOMPROV"].Visivel = True


#######Custo total de deslocamento

#    custoTotalDeslocamento = 0    
#    valortotAdiant = Convert.ToDecimal(Formulario['VALOR_TOTAL_ADIANTAMENTO'].Valor)
#    valorDiariaDolar = Convert.ToDecimal(Formulario['VALOR_DIARIA_DOLAR'].Valor)
#    valorPassagens = Convert.ToDecimal(OrdemServico.GetCustom('CSC_VALOR1_TOTAL'))
#    valorDevolucao = Convert.ToDecimal(Formulario['VALORTOTALPB'].Valor)
#    ##valorReembolso = Convert.ToDecimal(OrdemServico.GetCustom('VALOR_EXTRA'))
#
#    if tipoHospeda == "Contratada" or tipoHospeda == "Sem Hospedagem": 
#        custoTotalDeslocamento = valortotAdiant + valorDiariaDolar + valorPassagens + despesas + valorCarro + hospeda - valorDevolucao
#        
#    if tipoHospeda == "Avulsa": 
#        custoTotalDeslocamento = valortotAdiant + valorDiariaDolar + valorPassagens + despesas + valorCarro - valorDevolucao
#        #Formulario["VALORTOTSEMCOMPROV"].Valor = custoTotalDeslocamento
#        #Formulario["VALOR_TOT_PREST_CONTAS"].Valor = valortotAdiant + valorDiariaDolar + valorPassagens + despesas + valorCarro
#        #Formulario["VALOR_TOT_PREST_CONTAS"].Valor = 0
#    Formulario['CUSTO_TOT_DESLOC'].Valor = custoTotalDeslocamento    

#if tipoHospeda == "Avulsa": 
    #custoTotalDeslocamento = valortotAdiant + valorDiariaDolar + valorPassagens + despesas + valorCarro - valorDevolucao
#Formulario['CUSTO_TOT_DESLOC'].Valor = custoTotalDeslocamento

custoTotalDeslocamento = 0   
valorDevolucao = Convert.ToDecimal(Formulario['VALORTOTALPB'].Valor)

if tipoHospeda == "Avulsa" or tipoHospeda == "Avulsa SEM apresentação de NF" or tipoHospeda == "Contratada" or tipoHospeda == "Sem Hospedagem":
    custoTotalDeslocamento = totalSemPrestContas + valorTotalPrestContas
    Formulario['CUSTO_TOT_DESLOC'].Valor = custoTotalDeslocamento
```
  - VALORTOTSEMCOMPROV "Valor total sem necessidade de comprovação documental" [TextBox Decimal → CPE_CSC.VALORTOTSEMCOMPROV]

### [347979] EventoIntermediarioTimer ""
Config: TempoIntervalo=2880

### [347980] EventoIntermediarioMensagem "Cobrança Prestação de Contas - Deslocamento "
Destinatário: Cliente e Favorecido Deslocamento (papel 1021)
ModeloComunicado: Cobrança Prestação de Contas - Deslocamento 
Corpo do comunicado: Prezado(a),
aguardamos sua prestação de contas referente ao deslocamento realizado no dia OrdemServico.Customizado.SAIDA .
Para realizar a prestação de contas, Link.Edicao Worklist .
Insiras as informações e documentos, salve e clique em avançar. 
Atenciosamente,
Central de Serviços

### [347981] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [347982] EventoIntermediarioMensagem "Corrigir solicitação"
Destinatário: Cliente e Favorecido Deslocamento (papel 1021)
ModeloComunicado: Corrigir solicitação - Deslocamento
Corpo do comunicado: Prezado(a),
A Ordem de Serviço OrdemServico.Numero - OrdemServico.Assunto foi reprovada por seu gestor e necessita de ajustes para finalizar.
 Link.Edicao Worklist e corrija as informações.
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoGateway("APROVAR")
```

### [347983] Tarefa "Corrigir Prestação de Contas"
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptFim**
```python
OrdemServico.CancelaAprovacao("APROVAR_PRESTACAO")
```
**ScriptValidacao**
```python
if OrdemServico["SIM_NAO2"] == "Sim" and OrdemServico["SIM_NAO3"] == "Sim":
    Criticas.AdicionaPendencia("Não é permitido solicitar reembolso e devolução na mesma OS")
    
if OrdemServico["VALORTOTALPB"] != "" and Convert.ToDecimal(OrdemServico["VALORTOTALPB"]) < 0:
    Criticas.AdicionaPendencia("O campo Valor de devolução não pode ser negativo.")
    
if OrdemServico["VALOR_DOD"] != "" and Convert.ToDecimal(OrdemServico["VALOR_DOD"]) < 0:
    Criticas.AdicionaPendencia("O campo Valor do reembolso não pode ser negativo.")
    
if OrdemServico["SIM_NAO3"] == "Não" and Convert.ToDecimal(OrdemServico["VALOR_DIFERENCA_DESLOCAMENTO"]) < 0:
    Criticas.AdicionaPendencia("Haverá necessidade de devolução de valor para a BBTS. Marque a opção Sim e preencha o valor da devolução.")
    
if OrdemServico["SIM_NAO2"] == "Não" and Convert.ToDecimal(OrdemServico["VALOR_DIFERENCA_DESLOCAMENTO"]) > 0:
    Criticas.AdicionaPendencia("O funcionário/Gestor receberá um valor não previsto no pedido inicial do deslocamento. Marque a opção Sim e verifique o valor do reembolso.")
    
#Valida cidades que possuem CAT quanto a solicitação avulsa e que são capitais
listaCidadesCAT = ["ARACAJU - SE", "BELEM - PA", "BELO HORIZONTE - MG", "BOA VISTA - RR", "BRASILIA - DF", "CAMPO GRANDE - MS", "CUIABA - MT", "CURITIBA - PR", "FLORIANOPOLIS - SC", "FORTALEZA - CE", "GOIANIA - GO", "SAO LUIS - MA", "MACAPA - AP", "MACEIO - AL", "NATAL - RN", "PALMAS - TO", "PORTO ALEGRE - RS", "PORTO VELHO - RO", "RECIFE - PE", "RIO BRANCO - AC", "RIO DE JANEIRO - RJ", "SALVADOR - BA", "SAO PAULO - SP", "SERRA - ES", "TERESINA - PI", "VITORIA - ES", "BAURU - SP", "CAMPINAS - SP", "JOINVILLE - SC", "LONDRINA - PR", "PASSO FUNDO - RS", "RIBEIRAO PRETO - SP", "UBERLANDIA - MG"]

cidadeDestinoNome = ""
cidadeDestinoDescricao = DB.ExecuteDataTable("SELECT DISTINCT id_cidade, descricao || ' - ' || id_estado AS cidadeuf FROM cidade_v WHERE id_cidade = '"+ OrdemServico["CIDADE_DESTINO"] + "'")

for cidadeDestino in cidadeDestinoDescricao.Rows:
    cidadeDestinoNome = cidadeDestino['CIDADEUF'].ToString()
    
for cidade in listaCidadesCAT:  
    if cidade.ToString() == cidadeDestinoNome.ToString() and OrdemServico["TIPO_HOSPEDAGEM"].ToString() == "Avulsa SEM apresentação de NF":
        Criticas.AdicionaPendencia("Não é permitido a abertura de solicitaçoes de hospedagens avulsas para capitais e ou cidades que possui CAT.")
        
queryAdesaoDiariaAvulaSemApresentarNF = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, PESSOA.NOME From OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = CP_ORDEM_SERVICO.FAVORECIDO_COBRA Where OCORRENCIA.ASSUNTO = 'Adesão a diárias avulsas sem comprovação documental' And (OCORRENCIA.SITUACAO = 'FinalizadaSucesso' Or OCORRENCIA.SITUACAO = 'Aberto') and PESSOA.ID_PESSOA = '"+OrdemServico["FAVORECIDO_DESLOCAMENTO"]+"'")

if queryAdesaoDiariaAvulaSemApresentarNF.Rows.Count == 0 and OrdemServico["TIPO_HOSPEDAGEM"] == "Avulsa SEM apresentação de NF":
    Criticas.AdicionaPendencia("Parece que seu aceite, Adesão a diárias avulsas sem comprovação documental, não foi feito. O Aceite é necessário para este tipo de solicitação.") 
    
#Valida os checkbox que devem ser marcados
if OrdemServico["CHECKBOX8"] == False and OrdemServico["CHECKBOX9"] == False:
    Criticas.AdicionaPendencia("Você deve informar se houve alteração no seu deslocamento.")
    
if OrdemServico["CHECKBOX10"] == False:
    Criticas.AdicionaPendencia("E necessário calcular a diferença do deslocamento.")
    
if OrdemServico["COMBOBOX_CONFIRMA_TREINAMENTO"] == False:
    Criticas.AdicionaPendencia("E necessário calcular o custo total do deslocamento.")
    
if OrdemServico["VALOR_DESPESAS"] < 0:
    Criticas.AdicionaPendencia("No campo, Valor de outras despesas R$, não é permitido o preenchimento de valores negativos. preencher com 0 caso não tenha.")
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Servico
#SCRIPT PARA LIMPAR OS DADOS DO FORMULARIO #######################
#Formulario["FAVORECIDO_DESLOCAMENTO"].Visivel = False
#Formulario["MATRICULA_DESLOCAMENTO"].Visivel = False
#Formulario["CARGO_DESLOCAMENTO"].Visivel = False
#Formulario["FUNCAO_DESLOCAMENTO"].Visivel = False
#Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = False
#Formulario["CELULAR"].Visivel = False
#Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False
#Formulario["SIM_NAO"].Visivel = False
#Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
#
#Formulario["TIPO_DESLOCAMENTO"].Visivel = False
#Formulario["CIDADE_ORIGEM"].Visivel = False
#Formulario["CIDADE_DESTINO"].Visivel = False
#Formulario["CIDADE_CLASSIFICACAO"].Visivel = False
#Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = False
#Formulario["PAIS"].Visivel = False
#Formulario["TIPO_DESTINO"].Visivel = False
#Formulario["SAIDA"].Visivel = False
#Formulario["RETORNO_DIA"].Visivel = False
#Formulario["SAIDA_HORA"].Visivel = False
#Formulario["RETORNO_HORA"].Visivel = False
#Formulario["DIAS_DE_TRA"].Visivel = False
#Formulario["TIPO_HOSPEDAGEM"].Visivel = False
#Formulario["QUANTIDADE_DIARIA"].Visivel = False
#Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
#Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
#Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
#Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
#Formulario["VALOR_DIARIA"].Visivel = False
#Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
#Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
#Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
#Formulario["COTACAO_DOLAR"].Visivel = False
#Formulario["DIARIA_COTACAO_REAL"].Visivel = False
#Formulario["NUMERO_NT"].Visivel = False
#Formulario["PARCELA_COMPLEMENTAR"].Visivel = False
#Formulario["TOTAL_COMPLEMENTAR"].Visivel = False
#Formulario["LISTA_INVIABILIDADE"].Visivel = False
#Formulario["OBJETIVO_VIAGEM"].Visivel = False
#Formulario["MEIO_LOCOMOCAO"].Visivel = False
#Formulario["VIAGEM_LONGA"].Visivel = False
#Formulario["SIM_NAO_REFEICAO"].Visivel = False
#Formulario["PREVISAO_DISTANCIA_KM"].Visivel = False
#Formulario["VALOR_DISTANCIA"].Visivel = False
#Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
#Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
#Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
#Formulario["VALOR_REF_REDUZIDA"].Visivel = False
#Formulario["VALOR_REF_INTEGRAL"].Visivel = False
#Formulario["DESCRICAO_DESPESAS"].Visivel = False
#Formulario["VALOR_DESPESAS"].Visivel = False
#Formulario["VALOR_TOTAL_ADIANTAMENTO"].Visivel = False
#Formulario["PAHL_HOSPEDAGENS"].Visivel = False
#Formulario["PAHL_LOCACOES"].Visivel = False
#Formulario["PAHL_PASSAGENS"].Visivel = False

Formulario["CIDADE_ORIGEM"].Habilitado = False
Formulario["CIDADE_DESTINO"].Habilitado = False
Formulario["SAIDA_HORA"].Habilitado = False
Formulario["TIPO_DESTINO"].Habilitado = False
Formulario["MEIO_LOCOMOCAO"].Habilitado = True
Formulario["TIPO_DESLOCAMENTO"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
Formulario["TIPO_HOSPEDAGEM"].Habilitado = False

#Limpa os valores da seleção SIM e Não quando carregar o formulario
Formulario["CHECKBOX9"].Habilitado = True
Formulario["CHECKBOX8"].Habilitado = True

Formulario["CHECKBOX8"].Valor = False
Formulario["CHECKBOX9"].Valor = False
Formulario["CHECKBOX10"].Valor = False
Formulario["COMBOBOX_CONFIRMA_TREINAMENTO"].Valor = False


#SQL PARA RECUPERAR O VALOR DO REPASSE DA SOLICITAÇÃO DE DESLOCAMENTO PAI##########################
os = OrdemServico.Numero.Split(".")
sqlDeslocamento = DB.ExecuteDataTable("Select o.NUMERO, csp.DESCRICAO, mp.DESCRICAO As MACRO_PROCESSO, pr.DESCRICAO As PROCESSO, csp.DESCRICAO As SUBPROCESSO, s.DESCRICAO As Servico, o.SITUACAO, p1.NOME As Cliente, p2.NOME As responsavel, o.DATA_HORA_CRIACAO, o.DATA_HORA_FIM_REAL, cped.VALOR_TOTAL_ADIANTAMENTO From ocorrencia o Inner Join pessoa p1 On p1.id_pessoa = o.ID_CLIENTE Inner Join pessoa p2 On p2.id_pessoa = o.ID_RESPONSAVEL Inner Join atividade a On a.id_atividade = o.ID_ATIVIDADE Inner Join ordem_servico os On os.id_ocorrencia = o.ID_OCORRENCIA Inner Join servico s On s.id_servico = os.ID_SERVICO Inner Join classe_sub_processo csp On csp.id_classe_sub_processo = o.ID_CLASSE_SUB_PROC Inner Join desenho_processo dp On dp.id_desenho_processo = o.ID_DESENHO_PROCESSO Inner Join processo pr On pr.id_processo = dp.ID_PROCESSO Inner Join macro_processo mp On mp.id_macro_processo = pr.ID_MACRO_PROCESSO Inner Join CP_ORDEM_SERVICO On o.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join CPE_DESLOCAMENTO cped on O.ID_OCORRENCIA = cped.ID_OCORRENCIA Where o.NUMERO = '"+os[0].ToString()+"'")

for deslocamento in sqlDeslocamento.Rows:
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = deslocamento["VALOR_TOTAL_ADIANTAMENTO"]
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = deslocamento["VALOR_TOTAL_ADIANTAMENTO"]

Formulario["CIDADE_DESTINO"].Visivel = True
Formulario["LABEL10"].Visivel = False
Formulario["CHECKBOX9"].Visivel = True
Formulario["CHECKBOX8"].Visivel = True
Formulario["LABEL2"].Visivel = True

#Script para "Houve alteração no Deslocamento"?    
if Formulario["CHECKBOX9"].Valor == True:
    Formulario["FAVORECIDO_DESLOCAMENTO"].Visivel = True
    Formulario["MATRICULA_DESLOCAMENTO"].Visivel = True
    Formulario["CARGO_DESLOCAMENTO"].Visivel = True
    Formulario["FUNCAO_DESLOCAMENTO"].Visivel = True
    Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = True
    Formulario["CELULAR"].Visivel = True
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
    Formulario["SIM_NAO"].Visivel = True
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True
    Formulario["CIDADE_DESTINO"].Visivel = True

    #Formulario["TIPO_DESLOCAMENTO"].Valor = ""
    #Formulario["CIDADE_ORIGEM"].Valor = ""
    #Formulario["CIDADE_DESTINO"].Valor = ""
    #Formulario["CIDADE_CLASSIFICACAO"].Valor = ""
    #Formulario["CIDADE_DESTINO_INTERNACIONAL"].Valor = ""
    #Formulario["PAIS"].Valor = ""
    #Formulario["TIPO_DESTINO"].Valor = ""
    Formulario["RETORNO_DIA"].Valor = None
    #Formulario["SAIDA_HORA"].Valor = ""
    Formulario["RETORNO_HORA"].Valor = ""
    Formulario["DIAS_DE_TRA"].Valor = ""
    Formulario["TIPO_HOSPEDAGEM"].Valor = ""
    Formulario["QUANTIDADE_DIARIA"].Valor = ""
    #Formulario["VALOR_DIARIA_DOLAR"].Valor = ""
    #Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = ""
    #Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = ""
    #Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = ""
    Formulario["VALOR_DIARIA"].Valor = ""
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = ""
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = ""
    Formulario["VALOR_TOTAL_DIARIA"].Valor = ""
    Formulario["COTACAO_DOLAR"].Valor = ""
    #Formulario["DIARIA_COTACAO_REAL"].Valor = ""
    #Formulario["NUMERO_NT"].Valor = ""
    Formulario["PARCELA_COMPLEMENTAR"].Valor = ""
    Formulario["TOTAL_COMPLEMENTAR"].Valor = ""
    #Formulario["MEIO_LOCOMOCAO"].Valor = ""
    Formulario["VIAGEM_LONGA"].Valor = ""
    Formulario["SIM_NAO_REFEICAO"].Valor = ""
    Formulario["PREVISAO_DISTANCIA_KM"].Valor = ""
    #Formulario["VALOR_DISTANCIA"].Valor = ""
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = ""
    Formulario["VALOR_TOTAL_REFEICAO"].Valor = ""
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = ""
    Formulario["VALOR_REF_REDUZIDA"].Valor = ""
    Formulario["VALOR_REF_INTEGRAL"].Valor = ""
    Formulario["DESCRICAO_DESPESAS"].Valor = ""
#    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = ""

#Formulario["QUANTIDADE_DIARIA"].Visivel = False
#Formulario["QUANTIDADE_DIARIA"].Habilitado = False
Formulario["VALOR_DIARIA"].Visivel = False
Formulario["VALOR_DIARIA"].Habilitado = False
#Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
Formulario["DIARIA_COTACAO_REAL"].Visivel = False
Formulario["DIARIA_COTACAO_REAL"].Habilitado = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False


#Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
#Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False  


Formulario["VALOR_REF_INTEGRAL"].Visivel = False
Formulario["VALOR_REF_INTEGRAL"].Habilitado = False
Formulario["VALOR_REF_REDUZIDA"].Visivel = False
Formulario["VALOR_REF_REDUZIDA"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = True
#Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = True
Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False        
Formulario["COTACAO_DOLAR"].Visivel = False
Formulario["COTACAO_DOLAR"].Habilitado = False  


#Formulario["VALOR_DISTANCIA"].Valor = "0"
#Formulario["VALOR_TOTAL_REFEICAO"].Valor = "0"
Formulario["QTD_REFEICAO_REDUZIDA"].Valor = "0"




#Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = "0"
#Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "0"
#Formulario["VALOR_DIARIA_DOLAR"].Valor = "0"
#Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "0"
Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False




Formulario["CARGO_DESLOCAMENTO"].Visivel = False
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = False
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = False
Formulario["CARGO_DESLOCAMENTO"].Habilitado = False
Formulario["FUNCAO_DESLOCAMENTO"].Habilitado = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Habilitado = False
Formulario["MATRICULA_DESLOCAMENTO"].Habilitado = False

    

Formulario["PREVISAO_DISTANCIA_KM"].Visivel = False
Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = False 
Formulario["VALOR_DISTANCIA"].Visivel = False
Formulario["VALOR_DISTANCIA"].Habilitado = False
#Formulario["VALOR_PASSAGEM"].Visivel = False
#Formulario["VALOR_PASSAGEM"].Habilitado = False
#Formulario["VALIDADE_PASSAGEM"].Visivel = False
#Formulario["VALIDADE_PASSAGEM"].Habilitado = False
#Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = False
#Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = False


#Formulario["QUANTIDADE_DIARIA"].Visivel = True
#Formulario["QUANTIDADE_DIARIA"].Habilitado = True
#Formulario["VALOR_DIARIA"].Visivel = False
#Formulario["VALOR_DIARIA"].Habilitado = False
#Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False

Formulario["CIDADE_DESTINO"].Visivel = True
Formulario["CIDADE_CLASSIFICACAO"].Visivel = True
Formulario["CIDADE_CLASSIFICACAO"].Habilitado = False
Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = False
Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = False
Formulario["PAIS"].Visivel = False
Formulario["PAIS"].Habilitado = False

#Dados das Reservas

#Formulario["PAH_MOTIVO_SOL"].Visivel = False
#Formulario["PAH_MOTIVO_SOL"].Habilitado = False 
#Formulario["PAH_LOCALIZADORES"].Visivel = False
#Formulario["PAH_LOCALIZADORES"].Habilitado = False
#Formulario["PAH_VOUCHER_HOSPEDAGEM"].Visivel = False
#Formulario["PAH_VOUCHER_HOSPEDAGEM"].Habilitado = False
#Formulario["RESERVA_DE_VOO"].Visivel = False
#Formulario["RESERVA_DE_VOO"].Habilitado = False
#Formulario["PAH_DATA_ENTRADA"].Visivel = False
#Formulario["PAH_DATA_ENTRADA"].Habilitado = False
#Formulario["PAH_DATA_SAIDA"].Visivel = False
#Formulario["PAH_DATA_SAIDA"].Habilitado = False 
#Formulario["PAH_LOCALIZADORES"].Visivel = False
#Formulario["PAH_LOCALIZADORES"].Habilitado = False
#Formulario["PAH_EVENTO_HOTEL"].Visivel = False
#Formulario["PAH_EVENTO_HOTEL"].Habilitado = False
#Formulario["PAH_HOTEL_EVENTO"].Visivel = False
#Formulario["PAH_HOTEL_EVENTO"].Habilitado = False
#Formulario["PAHL_VOUCHER_CARRO"].Visivel = False
#Formulario["PAHL_VOUCHER_CARRO"].Habilitado = False
#Formulario["PAHL_LOCACOES_CARRO"].Visivel = False
#Formulario["PAHL_LOCACOES_CARRO"].Habilitado = False 
###Formulario["DESCRICAO_OBRIG"].Visivel = False
###Formulario["DESCRICAO_OBRIG"].Habilitado = False
#Formulario["CSC_OBS"].Visivel = False
#Formulario["CSC_OBS"].Habilitado = False
#Formulario["RESERVA_DE_VOO"].Visivel = False
#Formulario["RESERVA_DE_VOO"].Habilitado = False
#Formulario["DATA_INICIO_AUX1"].Visivel = False
#Formulario["DATA_INICIO_AUX1"].Habilitado = False
#Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Visivel = False
#Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Habilitado = False


Formulario["SIM_NAO"].Visivel = False

Formulario["PARCELA_COMPLEMENTAR"].Visivel = True
Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False   
Formulario["TOTAL_COMPLEMENTAR"].Visivel = True
Formulario["TOTAL_COMPLEMENTAR"].Habilitado = False  

Formulario["VIAGEM_LONGA"].Visivel = False
Formulario["VIAGEM_LONGA"].Habilitado = False 

Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False 

Formulario["LABEL1"].Visivel = False
Formulario["LABEL1"].Habilitado = False
Formulario["NUMERO_NT"].Visivel = False
#Formulario["NUMERO_NT"].Habilitado = False

#Formulario["VALOR_EXTRA"].Habilitado = True    
#Formulario["VALOR_EXTRA"].Visivel = True

#LISTA DE PAÍSES

Formulario["PAIS"].Itens = "AFEGANISTÃO;ARMÊNIA;BANGLADESH;BELARUS;BENIN;BOLÍVIA;BURKINAFASSO;BUTÃO;CHILE; COMORES;REPÚBLICA POPULAR DEMOCRÁTICA DA CORÉIA;COSTA RICA;EL SALVADOR; EQUADOR;ESLOVÊNIA;FILIPINAS;GÂMBIA;GUIANA;GUINÉ BISSAU;GUINÉ;HONDURAS;INDONÉSIA;IRÃ;IRAQUE;LAOS;LÍBANO;MALÁSIA;MALDIVAS; MARROCOS;MONGÓLIA;MYANMAR;NAMÍBIA;NAURU;NEPAL;NICARÁGUA;PANAMÁ;PARAGUAI; REP. CENTRO AFRICANA;REPÚBLICA TOGOLESA;SALOMÃO;SAMOA;SERRA LEOA;SÍRIA;SOMÁLIA;SRI LANKA;SURINAME;TADJIQUISTÃO;TAILÂNDIA;TIMOR LESTE;TONGA;TUNÍSIA;TURCOMENISTÃO;TURQUIA;TUVALU;VIETNÃ;ZIMBÁBUE;ÁFRICA DO SUL;ALBÂNIA;ANDORA;ARGÉLIA;ARGENTINA;AUSTRÁLIA;BELIZE;BÓSNIA-HERZEGÓVINA;BURUNDI;CABO VERDE;CAMARÕES;CAMBOJA;CATAR;CHADE;CHINA;CHIPRE;COLÔMBIA;DOMINICA;EGITO;ERITRÉIA;ESTÔNIA;ETIÓPIA;GANA;GEÓRGIA;GUINÉ EQUATORIAL;HAITI;HUNGRIA;IEMEN;ILHAS MARSHALL;ÍNDIA;KIRIBATI;LESOTO;LÍBIA;MACEDÔNIA;MADAGASCAR;MALAUÍ;MICRONÉSIA;MOÇAMBIQUE;MOLDÁVIA;NÍGER;NIGÉRIA;NOVA ZELÂNDIA;PALAU;PAPUA NOVAGUINÉ;PAQUISTÃO;PERU;POLÔNIA;QUÊNIA;REPÚBLICA DOMINICANA;ROMÊNIA;RUANDA;SÃO TOMÉ E PRÍNCIPE;SENEGAL; SUDÃO;TANZÂNIA;URUGUAI;UZBEQUISTÃO;VENEZUELA;ANTÍGUA E BARBUDA;ARÁBIA SAUDITA;AZERBAIDJÃO;BAHAMAS;BAREINE;BOTSUANA;BRUNEI DARUSSALAM;BULGÁRIA;CANADÁ;CINGAPURA;CONGO;COSTA DO MARFIM;CUBA;DJIBUTI;EMIRADOS ÁRABES;FIJI;GABÃO;GUATEMALA;JAMAICA;JORDÂNIA;LETÔNIA;LIBÉRIA;LITUÂNIA;MALI;MALTA;MAURÍCIO;MAURITÂNIA;MÉXICO;REPÚBLICA DEMOCRÁTICA DO CONGO;REPÚBLICA TCHECA;RÚSSIA;SAN MARINO;SANTA LÚCIA;SÃO CRISTOVÃO E NÉVIS;SÃO VICENTE EGRANADINAS;TAIWAN;TRINIDAD E TOBAGO;UCRÂNIA;UGANDA;ZÂMBIA;ALEMANHA;ANGOLA;ÁUSTRIA;BARBADOS;BÉLGICA;CAZAQUISTÃO;CORÉIA DOSUL;CROÁCIA;DINAMARCA;ESPANHA;ESTADOS UNIDOS DA AMÉRICA;FINLÂNDIA;FRANÇA;GRANADA;GRÉCIA;HONG KONG;IRLANDA;ISLÂNDIA;ISRAEL;ITÁLIA;JAPÃO;KUAITE;LIECHTENSTEIN;LUXEMBURGO;MÔNACO;MONTENEGRO;NORUEGA;OMÃ;PEÍSES BAIXOS;PORTUGAL;REINO UNIDO;REPÚBLICA QUIRGUIZ;SEICHELES;SÉRVIA SUAZILÂNDIA;SUÉCIA;SUÍÇA;VANUATU"




#INICIO SCRIPT PARA FAVORECIDO DESLOCAMENTO###############################################
Formulario["FAVORECIDO_DESLOCAMENTO"].Habilitado = False

Formulario["CARGO_DESLOCAMENTO"].Visivel = True
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = True
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = True
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = True

Formulario["CARGO_DESLOCAMENTO"].Habilitado = False
Formulario["FUNCAO_DESLOCAMENTO"].Habilitado = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Habilitado = False
Formulario["MATRICULA_DESLOCAMENTO"].Habilitado = False

Formulario["CARGO_DESLOCAMENTO"].Valor = None
Formulario["FUNCAO_DESLOCAMENTO"].Valor = None
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = None
Formulario["MATRICULA_DESLOCAMENTO"].Valor = None

cargo = ""
funcao = ""
desc_colaborador = ""
matricula = ""

if Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != "" or Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["ORGAO_FAVORECIDO"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT SUBSTR(c.CARGO,INSTR(c.CARGO,'|')+1,LENGTH(c.CARGO)) AS CARGO1, c.FUNCAO_GRATIFICADA, c.DESC_COLABORADOR, c.MATRICULA, c.FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND C.NUMERO_SUBCR_NIVEL1 = O.SIGLA AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    #lista = Utils.ExecuteDataTable("SELECT SUBSTR(CARGO,INSTR(CARGO,'|')+1,LENGTH(CARGO)) AS CARGO1, FUNCAO_GRATIFICADA, DESC_COLABORADOR, MATRICULA, FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND LPAD(C.NUMERO_SUBCR_NIVEL1,5) = LPAD(O.SIGLA,5) AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    for linha in lista.Rows:
        cargo = linha["CARGO1"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()

    Formulario["CARGO_DESLOCAMENTO"].Valor = cargo.ToString()
    Formulario["FUNCAO_DESLOCAMENTO"].Valor = funcao.ToString()
    Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = desc_colaborador.ToString()
    Formulario["MATRICULA_DESLOCAMENTO"].Valor = matricula.ToString()

if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False
else:
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
    Formulario["ACOMPANHANDO_GRUPO_A"].Valor = "Não"
    
#FIM SCRIPT PARA FAVORECIDO DESLOCAMENTO###############################################


#INICIO SCRIPT PARA BLOCO 2 ####################################
Formulario['DIAS_DE_TRA'].Visivel = False

if Formulario['DIAS_DE_TRA'].Valor == 0 or Formulario['DIAS_DE_TRA'].Valor == '0' or Formulario['TIPO_HOSPEDAGEM'].Valor == 'Sem Hospedagem':

    Formulario['QUANTIDADE_DIARIA'].Habilitado = False
    Formulario['QUANTIDADE_DIARIA'].Valor = 0
    

if Formulario['PARCELA_COMPLEMENTAR'].Valor == 0 or Formulario['PARCELA_COMPLEMENTAR'].Valor == '':
    Formulario['PARCELA_COMPLEMENTAR'].Habilitado = False
    Formulario['PARCELA_COMPLEMENTAR'].Visivel = False
    
else:
    Formulario['PARCELA_COMPLEMENTAR'].Habilitado = True
    Formulario['PARCELA_COMPLEMENTAR'].Visivel = True

if Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Próprio":
    Formulario['VALOR_DISTANCIA'].Habilitado = True
    Formulario['VALOR_DISTANCIA'].Visivel = True    
    Formulario['PREVISAO_DISTANCIA_KM'].Habilitado = True
    Formulario['PREVISAO_DISTANCIA_KM'].Visivel = True
    
else:
    Formulario['VALOR_DISTANCIA'].Habilitado = False
    Formulario['VALOR_DISTANCIA'].Visivel = False    
    Formulario['PREVISAO_DISTANCIA_KM'].Habilitado = False
    Formulario['PREVISAO_DISTANCIA_KM'].Visivel = False
 
#################################    
#if Formulario['CSC_VALOR1_TOTAL'].Valor != 0 or Formulario['CSC_VALOR1_TOTAL'].Valor != '' or Formulario['CSC_VALOR1_TOTAL'].Valor != '0':
#    Formulario['CSC_VALOR1_TOTAL'].Habilitado = False
#    Formulario['CSC_VALOR1_TOTAL'].Visivel = True
#else:
#    Formulario['CSC_VALOR1_TOTAL'].Habilitado = False
#    Formulario['CSC_VALOR1_TOTAL'].Visivel = False
#       
##################################     
#if Formulario['CSC_VALOR1'].Valor != 0 or Formulario['CSC_VALOR1'].Valor != '' or Formulario['CSC_VALOR1'].Valor != '0':
#    Formulario['CSC_VALOR1'].Habilitado = False
#    Formulario['CSC_VALOR1'].Visivel = True
#else:
#    Formulario['CSC_VALOR1'].Habilitado = False
#    Formulario['CSC_VALOR1'].Visivel = False
    
#################################     
#if Formulario['CSC_VALOR2'].Valor != 0 or Formulario['CSC_VALOR2'].Valor != '' or Formulario['CSC_VALOR2'].Valor != '0':
#    Formulario['CSC_VALOR2'].Habilitado = False
#    Formulario['CSC_VALOR2'].Visivel = True
#else:
#    Formulario['CSC_VALOR2'].Habilitado = False
#    Formulario['CSC_VALOR2'].Visivel = False
       
#Formulario['MEIO_LOCOMOCAO'].Habilitado = False
Formulario['VALOR_TOTAL_REFEICAO'].Habilitado = False
Formulario['VALOR_TOTAL_REFEICAO'].Visivel = True
Formulario['CUSTO_TOT_DESLOC'].Habilitado = False
Formulario['CUSTO_TOT_DESLOC'].Visivel = False
Formulario['VALOR_TOT_PREST_CONTAS'].Habilitado = False
Formulario['VALOR_TOTAL_ADIANTAMENTO'].Habilitado = True
Formulario['VALOR_TOTAL_ADIANTAMENTO'].Visivel = True
Formulario['VALORTOTSEMCOMPROV'].Habilitado = False

#FIM SCRIPT PARA BLOCO 2 #######################################

Formulario["OBJETIVO_VIAGEM"].Habilitado = False
Formulario["SAIDA"].Habilitado = False
Formulario["VALOR_DESPESAS"].Habilitado = False
Formulario["LISTA_INVIABILIDADE"].Habilitado = False


#Formulario["NOME_PROJETO"].Habilitado = False    
#Formulario["NOME_PROJETO"].Visivel = False    
#Formulario["VALOR_EXTRA"].Habilitado = False    
#Formulario["VALOR_EXTRA"].Visivel = False
#Formulario["SIM_NAO4"].Habilitado = False    
#Formulario["SIM_NAO4"].Visivel = False

Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False

if OrdemServico["TIPO_DESLOCAMENTO"] == "Viagem a Serviço - Internacional":
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
    #Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
    Formulario["COTACAO_DOLAR"].Visivel = True
    #Formulario["COTACAO_DOLAR"].Habilitado = True  
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
    #Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = True
    #Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = True
    Formulario["PAIS"].Visivel = True
    #Formulario["PAIS"].Habilitado = True       
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
    Formulario["TIPO_HOSPEDAGEM"].Visivel = True
    Formulario["TIPO_HOSPEDAGEM"].Habilitado = False    
    Formulario["TIPO_HOSPEDAGEM"].Valor = "Avulsa"
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True    
    
    Formulario["CIDADE_DESTINO"].Visivel = False
    Formulario["CIDADE_DESTINO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["DIARIA_COTACAO_REAL"].Visivel = True
    #Formulario["DIARIA_COTACAO_REAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    
    Formulario["LABEL1"].Visivel = True
    Formulario["LABEL1"].Habilitado = True
    Formulario["NUMERO_NT"].Visivel =  True
    #Formulario["NUMERO_NT"].Habilitado = True
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Documentos da Prestação de Contas" classes: Documentos da Prestação de Contas — RequeridoInicial=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações do Deslocamento
  - LISTA_INVIABILIDADE "Lista de Motivos que inviabilizam a videoconferência" [DropDownList String → CPE_DESLOCAMENTO.LISTA_INVIABILIDADE] obrigatório
  - OBJETIVO_VIAGEM "Objetivo / Informações Adicionais:" [TextBox String → CPE_DESLOCAMENTO.OBJETIVO_VIAGEM] obrigatório
  - MEIO_LOCOMOCAO "Meio de locomoção principal" [DropDownList String → CPE_DESLOCAMENTO.MEIO_LOCOMOCAO] obrigatório
**MEIO_LOCOMOCAO.ScriptModificado**
```python
if Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Próprio":
    Formulario["PREVISAO_DISTANCIA_KM"].Visivel = True
    Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = True
    Formulario["VALOR_DISTANCIA"].Visivel = True
    Formulario["VALOR_DISTANCIA"].Habilitado = True
else:
    Formulario["PREVISAO_DISTANCIA_KM"].Visivel = False
    Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = False
    Formulario["VALOR_DISTANCIA"].Visivel = False
    Formulario["VALOR_DISTANCIA"].Habilitado = False
    
if (Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Próprio" or Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Locado" or Formulario["MEIO_LOCOMOCAO"].Valor == "Carro da Frota" or Formulario["MEIO_LOCOMOCAO"].Valor == "Barco") and Formulario ["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica":
    Formulario["VIAGEM_LONGA"].Visivel = True
    Formulario["VIAGEM_LONGA"].Habilitado = True
else:
    Formulario["VIAGEM_LONGA"].Visivel = False
    Formulario["VIAGEM_LONGA"].Habilitado = False 
    
    
    
##if Formulario["MEIO_LOCOMOCAO"].Valor == "Avião" or Formulario["MEIO_LOCOMOCAO"] == "Ônibus Interestadual":
##    Formulario["VALOR_PASSAGEM"].Visivel = True
##    Formulario["VALOR_PASSAGEM"].Habilitado = True
##    Formulario["VALIDADE_PASSAGEM"].Visivel = True
##    Formulario["VALIDADE_PASSAGEM"].Habilitado = True
##    Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = True
##    Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = True
##else:
##    Formulario["VALOR_PASSAGEM"].Visivel = False
##    Formulario["VALOR_PASSAGEM"].Habilitado = False
##    Formulario["VALIDADE_PASSAGEM"].Visivel = False
##    Formulario["VALIDADE_PASSAGEM"].Habilitado = False
##    Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = False
##    Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = False    
#    
    






##finais de semana um almoço e janta integral
##dias de semana uma refeição reduzida e uma integral
############# calculo dias
#import clr 
#import datetime
#import System.Text
# 
#
#
#zero = 0
#valorRefIntegral = 64.36
#valorRefReduzida = 18.39
#
#
#
#daysOffText = System.Text.StringBuilder()
#
#
###RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
#def isHoliday(day):
#    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
#    #feriados = 0
#    
#    for holiday in holidays.Rows:
#        if day == holiday["DATA"].Date:
#            #feriados += 2
#            return True
#    return False
#
#
#def countHolidays(firstDate, lastDate):
#    totalHolidays = 0
#    currentDay = firstDate
#
#    while currentDay <= lastDate:
#        if isHoliday(currentDay):
#            totalHolidays += 1
#        currentDay = currentDay.AddDays(1)
#
#    return totalHolidays
#
#    
#def workingDays(totalDays, firstDate):
#
#    totalWorkingDays = 0
#    totalDaysOff = 0
#    count = 0
#
#   
#    while count <= totalDays:
#        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
#        day = firstDate.Date.AddDays(count)
#        
#        
#        
#        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
#            totalDaysOff = totalDaysOff + 1
#            daysOffText.AppendLine(" dayOff: "+str(day))
#        
#        count = count + 1
#        totalWorkingDays = totalWorkingDays + 1
#    return totalWorkingDays - totalDaysOff
#   
#
#
#    
#def countSaturdays(firstDate, lastDate):
#    saturdays = 0
#    currentDay = firstDate
#    
#    while currentDay <= lastDate:
#        if (currentDay.DayOfWeek == DayOfWeek.Sunday or currentDay.DayOfWeek == DayOfWeek.Saturday):
#            saturdays += 2
#        currentDay = currentDay.AddDays(1)  # Avance para o próximo dia
#    
#    return saturdays
#
#    
#firstDate = Formulario["SAIDA"].Valor
#lastDate = Formulario["RETORNO_DIA"].Valor
#
#totalDays = (lastDate - firstDate).TotalDays
#count = 0
#
#
#
#
#
#totalWorkingDays = workingDays(totalDays,firstDate)
#holidaysCount = countHolidays(firstDate, lastDate)
#saturdays = countSaturdays(firstDate, lastDate) + holidaysCount * 2
#
#
##Quantidade de refeições Reduzias e integrais
#quantRed = totalWorkingDays
#quantInt = saturdays + totalWorkingDays 
#
#
#
#
#
#
##Atribuindo valor a variável
#saidaHora = Formulario["SAIDA_HORA"].Valor 
#retornoHora = Formulario["RETORNO_HORA"].Valor 
#
##Split de horário, separando hora de minuto
#hora = saidaHora.Split(':');     
#horaRetorno = retornoHora.Split(':');
#
##Atribuindo valor de horário e minuto de acordo com o índice da variável
#horarioSaida = hora[0]
#minutoSaida = hora[1]
#
#horarioRetorno = horaRetorno[0] 
#minutoRetorno = horaRetorno[1]
#
#
#
##SAIDA DIAS ÚTEIS
#
#
##1 maior q o 2
##if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) >= 13 and Convert.ToInt32(horarioSaida) < 21):
##    quantRed = quantRed - 1
##   
##if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) > 21):
##    quantInt = quantInt - 1
##   
##RETORNO DIAS ÚTEIS
##1 menor q o 2   
##if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 13:
##    quantRed = quantRed - 1
##    quantInt = quantInt - 1
##    
##if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 19 and Convert.ToInt32(horarioRetorno) > 13:
##    quantInt = quantInt - 1
##    #teste abaixo
##    quantRed = quantRed - 1
#
#
#
#
#
##DIAS UTEIS
#
#if workingDays(0,firstDate):
#    if (Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0)):
#        quantRed = quantRed - 1
#    if (Convert.ToInt32(horarioSaida) > 21) or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
#        quantInt = quantInt - 1
#if workingDays(0,lastDate):    
#    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantRed = quantRed - 1
#    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantInt = quantInt - 1
##Formulario.ExibeMensagem("hora:"+horarioRetorno.ToString()+" minuto:"+minutoRetorno.ToString())    
################################################################
#    
##SAÍDA FINAIS DE SEMANA E/OU FERIADOS
#
#if not  workingDays(0,firstDate):
#    if Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0):
#        quantInt = quantInt - 1
#    if Convert.ToInt32(horarioSaida) > 21 or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
#        quantInt = quantInt - 1
#if not  workingDays(0,lastDate):
#    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantInt = quantInt - 1
#    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantInt = quantInt - 1   
#
#
#if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA": 
#  
#    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = zero
#    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = zero
#    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
#    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
#    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
#    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
#    Formulario["VALOR_REF_REDUZIDA"].Visivel = False
#    Formulario["VALOR_REF_INTEGRAL"].Visivel = False
#    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
#    
#else:
#    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = quantRed
#    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = quantInt
#    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = True
#    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = True
#    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = True
#    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = True
#    Formulario["VALOR_REF_REDUZIDA"].Visivel = True
#    Formulario["VALOR_REF_INTEGRAL"].Visivel = True
#    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = True
#  
#    
#if quantRed > (totalWorkingDays):
#    mensagem = ("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + str(totalWorkingDays + 1) + " Verifique a Saída e o Retorno.")
#    Formulario.ExibeMensagem(mensagem)    
#    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
#    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
#    
#
############## calculo valor total
#
#refIntegral = Formulario["QTD_REFEICAO_INTEGRAL"].Valor * valorRefIntegral
#refReduzida = Formulario["QTD_REFEICAO_REDUZIDA"].Valor * valorRefReduzida
#valorTotalRefeicoes = refIntegral + refReduzida
#Formulario["VALOR_TOTAL_REFEICAO"].Valor  = valorTotalRefeicoes
#Formulario["VALOR_REF_REDUZIDA"].Valor = refReduzida
#Formulario["VALOR_REF_INTEGRAL"].Valor = refIntegral
#
#
#
#
#
#
```
  - VIAGEM_LONGA "Distância da Viagem de Carro (Programa Valor)" [DropDownList String → CPE_DESLOCAMENTO.VIAGEM_LONGA] obrigatório
  - PREVISAO_DISTANCIA_KM "Previsão de distancia em KM (Para recebimento de R$1,30 por KM)" [TextBox Decimal → CPE_DESLOCAMENTO.PREVISAO_DISTANCIA_KM] obrigatório
**PREVISAO_DISTANCIA_KM.ScriptModificado**
```python
import System


Formulario["VALOR_DISTANCIA"].Habilitado = False

valorTotal = 0

distancia = Formulario["PREVISAO_DISTANCIA_KM"].Valor
valorTotal = distancia * 1.30 


Formulario["VALOR_DISTANCIA"].Valor = valorTotal
#OrdemServico["VALOR_DISTANCIA"] = valorTotal
#
```
  - CHECKBOX8 "Não" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX8]
**CHECKBOX8.ScriptModificado**
```python
Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor = 0
Formulario["CHECKBOX10"].Valor = True
#Formulario["CHECKBOX9"].Visivel = False
#Formulario["CHECKBOX8"].Visivel = False
Formulario["CHECKBOX9"].Habilitado = False
Formulario["CHECKBOX8"].Habilitado = False

#Formulario["LABEL10"].Visivel = False
#Formulario["LABEL2"].Visivel = False

Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False

Formulario["SIM_NAO2"].Valor = "Não"
Formulario["SIM_NAO3"].Valor = "Não"

Formulario["SIM_NAO2"].Habilitado = False
Formulario["SIM_NAO3"].Habilitado = False

Formulario["VALOR_DOD"].Visivel = False
Formulario["VALORTOTALPB"].Visivel = False
```
  - CHECKBOX9 "Sim" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX9]
**CHECKBOX9.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["FAVORECIDO_DESLOCAMENTO"].Visivel = True
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = True
Formulario["CARGO_DESLOCAMENTO"].Visivel = True
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = True
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = True
Formulario["CELULAR"].Visivel = True
Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
Formulario["SIM_NAO"].Visivel = True
Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True

Formulario["VALOR_DESPESAS"].Valor = ""

Formulario["PARCELA_COMPLEMENTAR"].Habilitado = True

Formulario["TIPO_HOSPEDAGEM"].Habilitado = True

Formulario["VALOR_DESPESAS"].Habilitado = True

Formulario["SIM_NAO2"].Habilitado = True
Formulario["SIM_NAO3"].Habilitado = True

Formulario["TIPO_DESLOCAMENTO"].Visivel = True
Formulario["CIDADE_ORIGEM"].Visivel = True
Formulario["CIDADE_DESTINO"].Visivel = True
Formulario["CIDADE_CLASSIFICACAO"].Visivel = True
Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = True
Formulario["PAIS"].Visivel = True
Formulario["TIPO_DESTINO"].Visivel = True
Formulario["SAIDA"].Visivel = True
Formulario["RETORNO_DIA"].Visivel = True
Formulario["SAIDA_HORA"].Visivel = True
Formulario["RETORNO_HORA"].Visivel = True
Formulario["DIAS_DE_TRA"].Visivel = True
Formulario["TIPO_HOSPEDAGEM"].Visivel = True
Formulario["QUANTIDADE_DIARIA"].Visivel = True
Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = True
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
Formulario["VALOR_DIARIA"].Visivel = True
Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
Formulario["COTACAO_DOLAR"].Visivel = True
Formulario["DIARIA_COTACAO_REAL"].Visivel = True
#Formulario["NUMERO_NT"].Visivel = True
Formulario["PARCELA_COMPLEMENTAR"].Visivel = True
Formulario["TOTAL_COMPLEMENTAR"].Visivel = True
Formulario["LISTA_INVIABILIDADE"].Visivel = True
Formulario["MEIO_LOCOMOCAO"].Visivel = True
Formulario["VIAGEM_LONGA"].Visivel = True
Formulario["SIM_NAO_REFEICAO"].Visivel = True
Formulario["PREVISAO_DISTANCIA_KM"].Visivel = True
Formulario["VALOR_DISTANCIA"].Visivel = True
Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = True
Formulario["VALOR_TOTAL_REFEICAO"].Visivel = True
Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = True
Formulario["VALOR_REF_REDUZIDA"].Visivel = True
Formulario["VALOR_REF_INTEGRAL"].Visivel = True
Formulario["DESCRICAO_DESPESAS"].Visivel = True
Formulario["VALOR_DESPESAS"].Visivel = True
Formulario["VALOR_TOTAL_ADIANTAMENTO"].Visivel = True

#Formulario["MEIO_LOCOMOCAO"].Habilitado = True

#Formulario["TIPO_DESLOCAMENTO"].Valor = ""
#Formulario["CIDADE_CLASSIFICACAO"].Valor = ""
#Formulario["TIPO_DESTINO"].Valor = ""
Formulario["RETORNO_DIA"].Valor = None
#Formulario["SAIDA_HORA"].Valor = ""
Formulario["RETORNO_HORA"].Valor = ""
Formulario["DIAS_DE_TRA"].Valor = ""
Formulario["TIPO_HOSPEDAGEM"].Valor = ""
Formulario["QUANTIDADE_DIARIA"].Valor = ""
Formulario["VALOR_DIARIA_DOLAR"].Valor = ""
#Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = ""
#Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = ""
Formulario["VALOR_DIARIA"].Valor = ""
Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = ""
Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = ""
Formulario["VALOR_TOTAL_DIARIA"].Valor = ""
Formulario["COTACAO_DOLAR"].Valor = ""
#Formulario["DIARIA_COTACAO_REAL"].Valor = ""
#Formulario["NUMERO_NT"].Valor = ""
Formulario["PARCELA_COMPLEMENTAR"].Valor = ""
Formulario["TOTAL_COMPLEMENTAR"].Valor = ""
Formulario["MEIO_LOCOMOCAO"].Valor = ""
Formulario["VIAGEM_LONGA"].Valor = ""
Formulario["SIM_NAO_REFEICAO"].Valor = ""
Formulario["PREVISAO_DISTANCIA_KM"].Valor = ""
#Formulario["VALOR_DISTANCIA"].Valor = ""
Formulario["QTD_REFEICAO_REDUZIDA"].Valor = ""
Formulario["VALOR_TOTAL_REFEICAO"].Valor = ""
Formulario["QTD_REFEICAO_INTEGRAL"].Valor = ""
Formulario["VALOR_REF_REDUZIDA"].Valor = ""
Formulario["VALOR_REF_INTEGRAL"].Valor = ""
Formulario["DESCRICAO_DESPESAS"].Valor = ""

#SCRIPT PARA LIMPAR OS DADOS DO FORMULARIO #######################
Formulario["QUANTIDADE_DIARIA"].Visivel = False
Formulario["QUANTIDADE_DIARIA"].Habilitado = False
Formulario["VALOR_DIARIA"].Visivel = False
Formulario["VALOR_DIARIA"].Habilitado = False
#Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
#Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
#Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
#Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
#Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
Formulario["DIARIA_COTACAO_REAL"].Visivel = False
Formulario["DIARIA_COTACAO_REAL"].Habilitado = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False

Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False  


Formulario["VALOR_REF_INTEGRAL"].Visivel = False
Formulario["VALOR_REF_INTEGRAL"].Habilitado = False
Formulario["VALOR_REF_REDUZIDA"].Visivel = False
Formulario["VALOR_REF_REDUZIDA"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = True
#Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = True
Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
#Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False        
Formulario["COTACAO_DOLAR"].Visivel = False
Formulario["COTACAO_DOLAR"].Habilitado = False  


#Formulario["VALOR_DISTANCIA"].Valor = "0"
Formulario["VALOR_TOTAL_REFEICAO"].Valor = "0"
Formulario["QTD_REFEICAO_REDUZIDA"].Valor = "0"




Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = "0"
Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "0"
#Formulario["VALOR_DIARIA_DOLAR"].Valor = "0"
#Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "0"
Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False




Formulario["CARGO_DESLOCAMENTO"].Visivel = False
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = False
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = False
Formulario["CARGO_DESLOCAMENTO"].Habilitado = False
Formulario["FUNCAO_DESLOCAMENTO"].Habilitado = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Habilitado = False
Formulario["MATRICULA_DESLOCAMENTO"].Habilitado = False

    

Formulario["PREVISAO_DISTANCIA_KM"].Visivel = False
Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = False 
Formulario["VALOR_DISTANCIA"].Visivel = False
Formulario["VALOR_DISTANCIA"].Habilitado = False
#Formulario["VALOR_PASSAGEM"].Visivel = False
#Formulario["VALOR_PASSAGEM"].Habilitado = False
#Formulario["VALIDADE_PASSAGEM"].Visivel = False
#Formulario["VALIDADE_PASSAGEM"].Habilitado = False
#Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = False
#Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = False


#Formulario["QUANTIDADE_DIARIA"].Visivel = True
#Formulario["QUANTIDADE_DIARIA"].Habilitado = True
#Formulario["VALOR_DIARIA"].Visivel = False
#Formulario["VALOR_DIARIA"].Habilitado = False
#Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False

Formulario["CIDADE_DESTINO"].Visivel = True
Formulario["CIDADE_DESTINO"].Habilitado = False
#Formulario["CIDADE_CLASSIFICACAO"].Visivel = False
Formulario["CIDADE_CLASSIFICACAO"].Habilitado = False
Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = False
Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = False
Formulario["PAIS"].Visivel = False
Formulario["PAIS"].Habilitado = False


Formulario["SIM_NAO"].Visivel = False

Formulario["PARCELA_COMPLEMENTAR"].Visivel = True
Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False   
Formulario["TOTAL_COMPLEMENTAR"].Visivel = True
Formulario["TOTAL_COMPLEMENTAR"].Habilitado = False  

Formulario["VIAGEM_LONGA"].Visivel = False
Formulario["VIAGEM_LONGA"].Habilitado = False 

Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False 

Formulario["LABEL1"].Visivel = False
Formulario["LABEL1"].Habilitado = False
Formulario["NUMERO_NT"].Visivel = False
Formulario["NUMERO_NT"].Habilitado = False


#LISTA DE PAÍSES

Formulario["PAIS"].Itens = "AFEGANISTÃO;ARMÊNIA;BANGLADESH;BELARUS;BENIN;BOLÍVIA;BURKINAFASSO;BUTÃO;CHILE; COMORES;REPÚBLICA POPULAR DEMOCRÁTICA DA CORÉIA;COSTA RICA;EL SALVADOR; EQUADOR;ESLOVÊNIA;FILIPINAS;GÂMBIA;GUIANA;GUINÉ BISSAU;GUINÉ;HONDURAS;INDONÉSIA;IRÃ;IRAQUE;LAOS;LÍBANO;MALÁSIA;MALDIVAS; MARROCOS;MONGÓLIA;MYANMAR;NAMÍBIA;NAURU;NEPAL;NICARÁGUA;PANAMÁ;PARAGUAI; REP. CENTRO AFRICANA;REPÚBLICA TOGOLESA;SALOMÃO;SAMOA;SERRA LEOA;SÍRIA;SOMÁLIA;SRI LANKA;SURINAME;TADJIQUISTÃO;TAILÂNDIA;TIMOR LESTE;TONGA;TUNÍSIA;TURCOMENISTÃO;TURQUIA;TUVALU;VIETNÃ;ZIMBÁBUE;ÁFRICA DO SUL;ALBÂNIA;ANDORA;ARGÉLIA;ARGENTINA;AUSTRÁLIA;BELIZE;BÓSNIA-HERZEGÓVINA;BURUNDI;CABO VERDE;CAMARÕES;CAMBOJA;CATAR;CHADE;CHINA;CHIPRE;COLÔMBIA;DOMINICA;EGITO;ERITRÉIA;ESTÔNIA;ETIÓPIA;GANA;GEÓRGIA;GUINÉ EQUATORIAL;HAITI;HUNGRIA;IEMEN;ILHAS MARSHALL;ÍNDIA;KIRIBATI;LESOTO;LÍBIA;MACEDÔNIA;MADAGASCAR;MALAUÍ;MICRONÉSIA;MOÇAMBIQUE;MOLDÁVIA;NÍGER;NIGÉRIA;NOVA ZELÂNDIA;PALAU;PAPUA NOVAGUINÉ;PAQUISTÃO;PERU;POLÔNIA;QUÊNIA;REPÚBLICA DOMINICANA;ROMÊNIA;RUANDA;SÃO TOMÉ E PRÍNCIPE;SENEGAL; SUDÃO;TANZÂNIA;URUGUAI;UZBEQUISTÃO;VENEZUELA;ANTÍGUA E BARBUDA;ARÁBIA SAUDITA;AZERBAIDJÃO;BAHAMAS;BAREINE;BOTSUANA;BRUNEI DARUSSALAM;BULGÁRIA;CANADÁ;CINGAPURA;CONGO;COSTA DO MARFIM;CUBA;DJIBUTI;EMIRADOS ÁRABES;FIJI;GABÃO;GUATEMALA;JAMAICA;JORDÂNIA;LETÔNIA;LIBÉRIA;LITUÂNIA;MALI;MALTA;MAURÍCIO;MAURITÂNIA;MÉXICO;REPÚBLICA DEMOCRÁTICA DO CONGO;REPÚBLICA TCHECA;RÚSSIA;SAN MARINO;SANTA LÚCIA;SÃO CRISTOVÃO E NÉVIS;SÃO VICENTE EGRANADINAS;TAIWAN;TRINIDAD E TOBAGO;UCRÂNIA;UGANDA;ZÂMBIA;ALEMANHA;ANGOLA;ÁUSTRIA;BARBADOS;BÉLGICA;CAZAQUISTÃO;CORÉIA DOSUL;CROÁCIA;DINAMARCA;ESPANHA;ESTADOS UNIDOS DA AMÉRICA;FINLÂNDIA;FRANÇA;GRANADA;GRÉCIA;HONG KONG;IRLANDA;ISLÂNDIA;ISRAEL;ITÁLIA;JAPÃO;KUAITE;LIECHTENSTEIN;LUXEMBURGO;MÔNACO;MONTENEGRO;NORUEGA;OMÃ;PEÍSES BAIXOS;PORTUGAL;REINO UNIDO;REPÚBLICA QUIRGUIZ;SEICHELES;SÉRVIA SUAZILÂNDIA;SUÉCIA;SUÍÇA;VANUATU"




#INICIO SCRIPT PARA FAVORECIDO DESLOCAMENTO###############################################
Formulario["FAVORECIDO_DESLOCAMENTO"].Habilitado = False

Formulario["CARGO_DESLOCAMENTO"].Visivel = True
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = True
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = True
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = True

Formulario["CARGO_DESLOCAMENTO"].Habilitado = False
Formulario["FUNCAO_DESLOCAMENTO"].Habilitado = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Habilitado = False
Formulario["MATRICULA_DESLOCAMENTO"].Habilitado = False

Formulario["CARGO_DESLOCAMENTO"].Valor = None
Formulario["FUNCAO_DESLOCAMENTO"].Valor = None
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = None
Formulario["MATRICULA_DESLOCAMENTO"].Valor = None

cargo = ""
funcao = ""
desc_colaborador = ""
matricula = ""

if Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != "" or Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["ORGAO_FAVORECIDO"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT SUBSTR(c.CARGO,INSTR(c.CARGO,'|')+1,LENGTH(c.CARGO)) AS CARGO1, c.FUNCAO_GRATIFICADA, c.DESC_COLABORADOR, c.MATRICULA, c.FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND C.NUMERO_SUBCR_NIVEL1 = O.SIGLA AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    #lista = Utils.ExecuteDataTable("SELECT SUBSTR(CARGO,INSTR(CARGO,'|')+1,LENGTH(CARGO)) AS CARGO1, FUNCAO_GRATIFICADA, DESC_COLABORADOR, MATRICULA, FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND LPAD(C.NUMERO_SUBCR_NIVEL1,5) = LPAD(O.SIGLA,5) AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    for linha in lista.Rows:
        cargo = linha["CARGO1"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()

    Formulario["CARGO_DESLOCAMENTO"].Valor = cargo.ToString()
    Formulario["FUNCAO_DESLOCAMENTO"].Valor = funcao.ToString()
    Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = desc_colaborador.ToString()
    Formulario["MATRICULA_DESLOCAMENTO"].Valor = matricula.ToString()

if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False
else:
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
    Formulario["ACOMPANHANDO_GRUPO_A"].Valor = "Não"
    
#FIM SCRIPT PARA FAVORECIDO DESLOCAMENTO###############################################

Formulario["CHECKBOX8"].Valor = False
Formulario["CHECKBOX8"].Habilitado = False
Formulario["CHECKBOX9"].Habilitado = False
Formulario["LABEL10"].Visivel = True
#Formulario["LABEL2"].Visivel = False

if OrdemServico["TIPO_DESLOCAMENTO"] == "Viagem a Serviço - Internacional":
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
    #Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
    Formulario["COTACAO_DOLAR"].Visivel = True
    Formulario["COTACAO_DOLAR"].Habilitado = True  
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
    #Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = True
    #Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = True
    Formulario["PAIS"].Visivel = True
    #Formulario["PAIS"].Habilitado = True       
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
    Formulario["TIPO_HOSPEDAGEM"].Visivel = True
    Formulario["TIPO_HOSPEDAGEM"].Habilitado = False    
    Formulario["TIPO_HOSPEDAGEM"].Valor = "Avulsa"
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True    
    
    Formulario["CIDADE_DESTINO"].Visivel = False
    Formulario["CIDADE_DESTINO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["DIARIA_COTACAO_REAL"].Visivel = True
    #Formulario["DIARIA_COTACAO_REAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    
    Formulario["LABEL1"].Visivel = True
    Formulario["LABEL1"].Habilitado = True
    Formulario["NUMERO_NT"].Visivel =  True
    Formulario["NUMERO_NT"].Habilitado = True
```
  - FAVORECIDO_DESLOCAMENTO "Favorecido" [DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO] obrigatório
**FAVORECIDO_DESLOCAMENTO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["CARGO_DESLOCAMENTO"].Visivel = True
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = True
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = True
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = True



Formulario["CARGO_DESLOCAMENTO"].Habilitado = False
Formulario["FUNCAO_DESLOCAMENTO"].Habilitado = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Habilitado = False
Formulario["MATRICULA_DESLOCAMENTO"].Habilitado = False



Formulario["CARGO_DESLOCAMENTO"].Valor = None
Formulario["FUNCAO_DESLOCAMENTO"].Valor = None
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = None
Formulario["MATRICULA_DESLOCAMENTO"].Valor = None



cargo = ""
funcao = ""
desc_colaborador = ""
matricula = ""

if Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != "" or Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["ORGAO_FAVORECIDO"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT SUBSTR(c.CARGO,INSTR(c.CARGO,'|')+1,LENGTH(c.CARGO)) AS CARGO1, c.FUNCAO_GRATIFICADA, c.DESC_COLABORADOR, c.MATRICULA, c.FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND C.NUMERO_SUBCR_NIVEL1 = O.SIGLA AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    #lista = Utils.ExecuteDataTable("SELECT SUBSTR(CARGO,INSTR(CARGO,'|')+1,LENGTH(CARGO)) AS CARGO1, FUNCAO_GRATIFICADA, DESC_COLABORADOR, MATRICULA, FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND LPAD(C.NUMERO_SUBCR_NIVEL1,5) = LPAD(O.SIGLA,5) AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    for linha in lista.Rows:
        cargo = linha["CARGO1"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()

    Formulario["CARGO_DESLOCAMENTO"].Valor = cargo.ToString()
    Formulario["FUNCAO_DESLOCAMENTO"].Valor = funcao.ToString()
    Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = desc_colaborador.ToString()
    Formulario["MATRICULA_DESLOCAMENTO"].Valor = matricula.ToString()

    
        


if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False
else:
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
    Formulario["ACOMPANHANDO_GRUPO_A"].Valor = "Não"
```
  - MATRICULA_DESLOCAMENTO "Matrícula" [TextBox Integer → CPE_DESLOCAMENTO.MATRICULA_DESLOCAMENTO]
  - CARGO_DESLOCAMENTO "Cargo" [TextBox String → CPE_DESLOCAMENTO.CARGO_DESLOCAMENTO]
  - FUNCAO_DESLOCAMENTO "Função" [TextBox String → CPE_DESLOCAMENTO.FUNCAO_DESLOCAMENTO]
  - DESC_COLABORADOR_DESLOCAMENTO "Tipo de Colaborador" [TextBox String → CPE_DESLOCAMENTO.DESC_COLABORADOR_DESLOCAMENTO]
  - CELULAR "Celular do Favorecido" [TextBox String → CP_ORDEM_SERVICO.CELULAR] — Configuracao={"Mascara":"00000000000"}
  - ACOMPANHANDO_GRUPO_A "Estará acompanhando Presidente / Diretor / Conselheiro " [DropDownList String → CPE_DESLOCAMENTO.ACOMPANHANDO_GRUPO_A] obrigatório
**ACOMPANHANDO_GRUPO_A.ScriptModificado**
```python
if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True 
    Formulario["NUM_ABERTURA_CHAMADO"].Habilitado = True 
    Formulario["SIM_NAO"].Visivel = False
    Formulario["SIM_NAO"].Habilitado = False 
  

else:
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False 
    Formulario["SIM_NAO"].Visivel = True
    Formulario["SIM_NAO"].Habilitado = True
     
    
    
#    
#if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Não":
#    Formulario["SIM_NAO"].Visivel = True
#    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True 
#    Formulario["NUM_ABERTURA_CHAMADO"].Habilitado = True 
#
#else:
#     Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
#
```
  - DESCRICAO_DESPESAS "Descrição de outras despesas (Preencher com "NA" caso não tenha) " [TextBox String(1000) → CPE_DESLOCAMENTO.DESCRICAO_DESPESAS]
**DESCRICAO_DESPESAS.ScriptModificado**
```python
import System

diariaAvulsa = 0
valorDist = 0 



#valorTotalPrestContas = OrdemServico.GetCustom("VALOR_DESPESAS") + OrdemServico.GetCustom("VALOR_DISTANCIA") + OrdemServico.GetCustom("VALOR_TOTAL_DIARIA")
#valorTotSemPrestContas = refeições, diaria de hotel contratada/sem hospedagem e parcela complementar

if Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
    
    valorTotalAdiantamento = 0


    totalDiaria = 0
    ##valorAvicao = 0
    outrasDespesas = 0
    ##valorDistancia = 0
    #complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    totalDiaria = Convert.ToDecimal(Formulario["DIARIA_COTACAO_REAL"].Valor)
    ##valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    ##valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    #complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    ##valorTotalAdiantamento =  totalDiaria + outrasDespesas + valorDistancia 
    valorTotalAdiantamento = totalDiaria + outrasDespesas
    
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False

    ##OrdemServico["VALOR_UTILIZADO_DESLOCAMENTO"] = valorTotalAdiantamento

elif (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):

    valorTotalAdiantamento = 0
    valorTotalRefeicao = 0
    totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    valorTotalAdiantamento = valorTotalRefeicao + totalDiaria + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False
    
elif (Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    valorTotalAdiantamento = 0
    valorTotalRefeicao = 0
    #totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    #totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    valorTotalAdiantamento = valorTotalRefeicao + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False


    ##OrdemServico["VALOR_UTILIZADO_DESLOCAMENTO"] = valorTotalAdiantamento    
else:
    valorTotalAdiantamento = 0

    valorTotalRefeicao = 0
    #totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0
    
    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    #totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    
    valorTotalAdiantamento = valorTotalRefeicao + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False
```
  - VALOR_DESPESAS "Valor de outras despesas R$ (preencher com "0" caso não tenha)" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DESPESAS] obrigatório — Coluna=2
**VALOR_DESPESAS.ScriptModificado**
```python
import System

diariaAvulsa = 0
valorDist = 0 

Formulario["CHECKBOX10"].Valor = False
Formulario["COMBOBOX_CONFIRMA_TREINAMENTO"].Valor = False

#valorTotalPrestContas = OrdemServico.GetCustom("VALOR_DESPESAS") + OrdemServico.GetCustom("VALOR_DISTANCIA") + OrdemServico.GetCustom("VALOR_TOTAL_DIARIA")
#valorTotSemPrestContas = refeições, diaria de hotel contratada/sem hospedagem e parcela complementar

if Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
    
    valorTotalAdiantamento = 0


    totalDiaria = 0
    ##valorAvicao = 0
    outrasDespesas = 0
    ##valorDistancia = 0
    #complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    totalDiaria = Convert.ToDecimal(Formulario["DIARIA_COTACAO_REAL"].Valor)
    ##valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    ##valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    #complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    ##valorTotalAdiantamento =  totalDiaria + outrasDespesas + valorDistancia 
    valorTotalAdiantamento = totalDiaria + outrasDespesas
    
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False

    ##OrdemServico["VALOR_UTILIZADO_DESLOCAMENTO"] = valorTotalAdiantamento

#elif (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):

elif (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica") or (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):

    valorTotalAdiantamento = 0
    valorTotalRefeicao = 0
    totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    valorTotalAdiantamento = valorTotalRefeicao + totalDiaria + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False
    
elif (Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    valorTotalAdiantamento = 0
    valorTotalRefeicao = 0
    #totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    #totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    valorTotalAdiantamento = valorTotalRefeicao + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False


    ##OrdemServico["VALOR_UTILIZADO_DESLOCAMENTO"] = valorTotalAdiantamento    
else:
    valorTotalAdiantamento = 0

    valorTotalRefeicao = 0
    #totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0
    
    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    #totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    
    valorTotalAdiantamento = valorTotalRefeicao + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Habilitado = False
    #Esta faltando pegar valor de diaria e da parcela complementar para o valor total
    


 
#Valores a prestar conta 
    
#if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa":
#    
#    
#    diariaAvulsa = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#    
#    
#else:
#    diariaAvulsa = 0
#
#
#    
#if Formulario["VALOR_DISTANCIA"].Valor != 0:
#    valorDist = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
#
#else:
#    valorDist = 0 
#    
#outrasDespesas2 = Convert.ToDecimal(outrasDespesas)
#
#valorTotalPrestContas = outrasDespesas2 + diariaAvulsa + valorDist
#
#
#
#Formulario["VALOR_TOT_PREST_CONTAS"].Valor = Convert.ToDecimal(valorTotalPrestContas)
#
#
#
##Valores sem necessidade de prestação de contas
#
#refeicoes = 0
#hospeda = 0
#complementar = 0
#
#
#
#if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA":
#
#    refeicoes = 0
#
#else:
#    refeicoes = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
#    
#
#    
#if Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada":
#   hospeda = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#   
#elif Formulario["TIPO_HOSPEDAGEM"].Valor == "Sem Hospedagem":
#   hospeda = 0
#
#   
# 
#if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
#    complementar = 0
#else:
#    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
#    
#
#    
#totalSemPrestContas = complementar + hospeda + refeicoes
#
#Formulario["VALORTOTSEMCOMPROV"].Valor = Convert.ToDecimal(totalSemPrestContas)
















    #OrdemServico["VALOR_UTILIZADO_DESLOCAMENTO"] = valorTotalAdiantamento
```
  - VALOR_UTILIZADO_DESLOCAMENTO "Valor Utilizado" [TextBox Decimal → CPE_CSC.VALOR_UTILIZADO_DESLOCAMENTO]
  - VALOR_TOTAL_ADIANTAMENTO "Valor total do adiantamento R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_ADIANTAMENTO]
  - CHECKBOX10 "Marque este campo para calcular o valor da diferença do deslocamento. (Se você alterar algum preenchimento do formulario, desmarque e marque novamente este campo para recalcular o valor)." [CheckBox Boolean → CPE_PESSOAS.CHECKBOX10]
**CHECKBOX10.ScriptModificado**
```python
Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor = Formulario["VALOR_UTILIZADO_DESLOCAMENTO"].Valor - Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor

#if Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor < 0:
#    Formulario["SIM_NAO3"].Valor = "Sim"
#    Formulario["SIM_NAO3"].Habilitado = False
#    Formulario["STRING_ERP"].Visivel = True
#    Formulario["STRING_ERP"].Habilitado = True
#
OrdemServico.Salva()
```
  - VALOR_DIFERENCA_DESLOCAMENTO "Valor Diferença (Se o valor for negativo, necessário que o viajante realize a devolução para a BBTS)" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DIFERENCA_DESLOCAMENTO]
  - VALOR_DIARIA_DOLAR "Valor Diária US$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_DOLAR] obrigatório
**VALOR_DIARIA_DOLAR.ScriptModificado**
```python
if Convert.ToDecimal(Formulario["VALOR_DIARIA_DOLAR"].Valor) >= Convert.ToDecimal(Formulario["CAMPO_VALIDACAO_DOLAR"].Valor):
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = Formulario["CAMPO_VALIDACAO_DOLAR"].Valor
else:
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = Formulario["VALOR_DIARIA_DOLAR"].Valor
    
    
Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True

valorTotal1 = 0

quantDiaria = Convert.ToDecimal(Formulario["QUANTIDADE_DIARIA"].Valor)
valorDiaria = Convert.ToDecimal(Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor)

valorTotal1 = quantDiaria * valorDiaria 

Formulario["VALOR_TOTAL_DIARIA"].Valor =  valorTotal1 


#OrdemServico["VALOR_TOTAL_DIARIA"] = valorTotal1
```
  - CAMPO_VALIDACAO_DOLAR "Diária máxima autorizada US$ (TAB320-001)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DOLAR] obrigatório — Coluna=2
  - DIARIA_AUTORIZADO_INTERNACIONAL "Valor Diária Autorizado US$" [TextBox String → CPE_DESLOCAMENTO.DIARIA_AUTORIZADO_INTERNACIONAL] obrigatório — Coluna=3
  - LABEL10 "<h3><b>Preencha com os dados de deslocamento.</b></h3>" [Label String(700) → CPE_PDCI2019.LABEL10] obrigatório
  - LABEL2 "<h3 style="margin-bottom: -20px"><b>Houve alteração no deslocamento como data de estadia ou valores a receber?</b></h3>" [Label String(2000) → CP_ORDEM_SERVICO.LABEL2] obrigatório
  - SIM_NAO "Estará acompanhado Gerente Executivo / Gerente de Projeto I / Assesor Executivo / Superintendente?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
if Formulario["SIM_NAO"].Valor == "Sim":
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True
else:
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
```
  - NUM_ABERTURA_CHAMADO "N° da Abertura de Chamado do Deslocamento a Serviço de Quem Está Acompanhando" [TextBox String → CPE_DESLOCAMENTO.NUM_ABERTURA_CHAMADO] obrigatório
  - TIPO_DESLOCAMENTO "Tipo de Deslocamento" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESLOCAMENTO] obrigatório
**TIPO_DESLOCAMENTO.ScriptModificado**
```python
##Viagem internacional

if Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
    Formulario["COTACAO_DOLAR"].Visivel = True
    Formulario["COTACAO_DOLAR"].Habilitado = True  
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = True
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = True
    Formulario["PAIS"].Visivel = True
    Formulario["PAIS"].Habilitado = True       
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
    Formulario["TIPO_HOSPEDAGEM"].Visivel = True
    Formulario["TIPO_HOSPEDAGEM"].Habilitado = False    
    Formulario["TIPO_HOSPEDAGEM"].Valor = "Avulsa"
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True    
    
    Formulario["CIDADE_DESTINO"].Visivel = False
    Formulario["CIDADE_DESTINO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["DIARIA_COTACAO_REAL"].Visivel = True
    Formulario["DIARIA_COTACAO_REAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    
    Formulario["LABEL1"].Visivel = True
    Formulario["LABEL1"].Habilitado = True
    Formulario["NUMERO_NT"].Visivel =  True
    Formulario["NUMERO_NT"].Habilitado = True  
    
else:
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    Formulario["COTACAO_DOLAR"].Visivel = False
    Formulario["COTACAO_DOLAR"].Habilitado = False   
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = False
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = False
    Formulario["PAIS"].Visivel = False
    Formulario["PAIS"].Habilitado = False  
    Formulario["TIPO_HOSPEDAGEM"].Habilitado = True
    
    Formulario["CIDADE_DESTINO"].Visivel = True
    Formulario["CIDADE_DESTINO"].Habilitado = True
    Formulario["CIDADE_DESTINO"].Visivel = True
    Formulario["CIDADE_DESTINO"].Habilitado = True
    Formulario["CIDADE_CLASSIFICACAO"].Visivel = True
    Formulario["VALOR_DIARIA"].Visivel = True
    Formulario["VALOR_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
    Formulario["DIARIA_COTACAO_REAL"].Visivel = False
    Formulario["DIARIA_COTACAO_REAL"].Habilitado = False
    
    Formulario["LABEL1"].Visivel =  False
    Formulario["LABEL1"].Habilitado = False
    Formulario["NUMERO_NT"].Visivel =  False
    Formulario["NUMERO_NT"].Habilitado = False
    
    Formulario["VALOR_DIARIA"].Valor = ""
```
  - CIDADE_ORIGEM "Cidade de Origem" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_ORIGEM]
  - CIDADE_DESTINO "Cidade de Destino" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_DESTINO] — Coluna=2
**CIDADE_DESTINO.ScriptModificado**
```python
sqlConsultaCidadeDestino = DB.ExecuteDataTable("SELECT to_char(id_cidade) as id, c.descricao ||' - '|| c.id_estado as cidade FROM cidade_v c WHERE id_cidade = '"+Formulario["CIDADE_DESTINO"].Valor.ToString()+"'")

sqlConsultaClassificacao = DB.ExecuteDataTable("select DISTINCT CLASSIFICACAO, CIDADE || ' - ' || UF AS cidadeuf from Z_00143_CIDADES_CLASSIFICACOES where CIDADE || ' - ' || UF = '"+sqlConsultaCidadeDestino.Rows[0]["CIDADE"].ToString()+"'")

for classificacao in sqlConsultaClassificacao.Rows:
    Formulario["CIDADE_CLASSIFICACAO"].Valor = classificacao["CLASSIFICACAO"].ToString()
```
  - CIDADE_CLASSIFICACAO "Cidade Classificação" [TextBox String → CPE_CSC.CIDADE_CLASSIFICACAO]
  - CIDADE_DESTINO_INTERNACIONAL "Cidade de Destino (Internacional)" [TextBox String → CPE_DESLOCAMENTO.CIDADE_DESTINO_INTERNACIONAL] obrigatório — Coluna=2
  - PAIS "País de Destino" [DropDownList String → CPE_DESLOCAMENTO.PAIS] obrigatório — Coluna=3
**PAIS.ScriptModificado**
```python
  
        ################## grupo A
if Formulario["PAIS"].Valor == "AFEGANISTÃO" or Formulario["PAIS"].Valor == "ARMÊNIA" or Formulario["PAIS"].Valor == "BANGLADESH" or Formulario["PAIS"].Valor == "BELARUS" or Formulario["PAIS"].Valor == "BENIN" or Formulario["PAIS"].Valor == "BOLÍVIA" or Formulario["PAIS"].Valor == "BURKINAFASSO" or Formulario["PAIS"].Valor == "BUTÃO"  or Formulario["PAIS"].Valor == "CHILE" or Formulario["PAIS"].Valor == "COMORES" or Formulario["PAIS"].Valor == "REPÚBLICA POPULAR DEMOCRÁTICA DA CORÉIA" or Formulario["PAIS"].Valor == "COSTA RICA" or Formulario["PAIS"].Valor == "EL SALVADOR" or Formulario["PAIS"].Valor == "EQUADOR" or Formulario["PAIS"].Valor == "ESLOVÊNIA" or Formulario["PAIS"].Valor == "FILIPINAS" or Formulario["PAIS"].Valor == "GÂMBIA" or Formulario["PAIS"].Valor == "GUIANA" or Formulario["PAIS"].Valor == "GUINÉ BISSAU" or Formulario["PAIS"].Valor == "GUINÉ" or Formulario["PAIS"].Valor == "HONDURAS" or Formulario["PAIS"].Valor == "INDONÉSIA" or Formulario["PAIS"].Valor == "IRÃ" or Formulario["PAIS"].Valor == "IRAQUE" or Formulario["PAIS"].Valor == "LAOS" or Formulario["PAIS"].Valor == "LÍBANO" or Formulario["PAIS"].Valor == "MALÁSIA" or Formulario["PAIS"].Valor == "MALDIVAS" or Formulario["PAIS"].Valor == "MARROCOS" or Formulario["PAIS"].Valor == "MONGÓLIA" or Formulario["PAIS"].Valor == "NAMÍBIA" or Formulario["PAIS"].Valor == "MYANMAR" or Formulario["PAIS"].Valor == "NAURU" or Formulario["PAIS"].Valor == "NEPAL"or Formulario["PAIS"].Valor == "NICARÁGUA" or Formulario["PAIS"].Valor == "PANAMÁ" or Formulario["PAIS"].Valor == "PARAGUAI" or Formulario["PAIS"].Valor == " REP. CENTRO AFRICANA" or Formulario["PAIS"].Valor == "REPÚBLICA TOGOLESA" or Formulario["PAIS"].Valor == "SALOMÃO" or Formulario["PAIS"].Valor == "SAMOA" or Formulario["PAIS"].Valor == "SERRA LEOA" or Formulario["PAIS"].Valor == "SÍRIA" or Formulario["PAIS"].Valor == "SOMÁLIA" or Formulario["PAIS"].Valor == "SRI LANKA" or Formulario["PAIS"].Valor == "TURQUIA" or Formulario["PAIS"].Valor == "TADJIQUISTÃO" or Formulario["PAIS"].Valor == "TAILÂNDIA" or Formulario["PAIS"].Valor == "TIMOR LESTE" or Formulario["PAIS"].Valor == "TONGA" or Formulario["PAIS"].Valor == "TUNÍSIA" or Formulario["PAIS"].Valor == "TURCOMENISTÃO" or Formulario["PAIS"].Valor == "TUVALU" or Formulario["PAIS"].Valor == "VIETNÃ" or Formulario["PAIS"].Valor == "ZIMBÁBUE":
    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "220"
                        
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "200"
            
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "190"
            
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
          Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "180"
          
    else:
          Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "170"
            
        ###################### grupo B    
            
elif Formulario["PAIS"].Valor == "ÁFRICA DO SUL" or Formulario["PAIS"].Valor == "ALBÂNIA" or Formulario["PAIS"].Valor == "ANDORA" or Formulario["PAIS"].Valor == "ARGÉLIA" or Formulario["PAIS"].Valor == "ARGENTINA" or Formulario["PAIS"].Valor == "AUSTRÁLIA" or Formulario["PAIS"].Valor == "BELIZE" or Formulario["PAIS"].Valor == "BÓSNIA-HERZEGÓVINA"  or Formulario["PAIS"].Valor == "BURUNDI" or Formulario["PAIS"].Valor == " CABO VERDE" or Formulario["PAIS"].Valor == "CAMARÕES" or Formulario["PAIS"].Valor == "CAMBOJA" or Formulario["PAIS"].Valor == "CATAR" or Formulario["PAIS"].Valor == "CHADE" or Formulario["PAIS"].Valor == "CHINA" or Formulario["PAIS"].Valor == "CHIPRE" or Formulario["PAIS"].Valor == "COLÔMBIA" or Formulario["PAIS"].Valor == "DOMINICA" or Formulario["PAIS"].Valor == "EGITO" or Formulario["PAIS"].Valor == "ERITRÉIA" or Formulario["PAIS"].Valor == "ESTÔNIA" or Formulario["PAIS"].Valor == "ETIÓPIA" or Formulario["PAIS"].Valor == "GANA" or Formulario["PAIS"].Valor == "GEÓRGIA" or Formulario["PAIS"].Valor == "GUINÉ EQUATORIAL" or Formulario["PAIS"].Valor == "HAITI" or Formulario["PAIS"].Valor == "HUNGRIA" or Formulario["PAIS"].Valor == "IEMEN" or Formulario["PAIS"].Valor == " ILHAS MARSHALL" or Formulario["PAIS"].Valor == "ÍNDIA" or Formulario["PAIS"].Valor == "KIRIBATI" or Formulario["PAIS"].Valor == "LESOTO" or Formulario["PAIS"].Valor == "LÍBIA" or Formulario["PAIS"].Valor == "MACEDÔNIA"or Formulario["PAIS"].Valor == "MADAGASCAR" or Formulario["PAIS"].Valor == "MALAUÍ" or Formulario["PAIS"].Valor == "MICRONÉSIA" or Formulario["PAIS"].Valor == "MOÇAMBIQUE" or Formulario["PAIS"].Valor == "MOLDÁVIA" or Formulario["PAIS"].Valor == "NÍGER" or Formulario["PAIS"].Valor == "NIGÉRIA" or Formulario["PAIS"].Valor == "NOVA ZELÂNDIA" or Formulario["PAIS"].Valor == "PALAU" or Formulario["PAIS"].Valor == "PAPUA NOVA GUINÉ" or Formulario["PAIS"].Valor == "PAQUISTÃO" or Formulario["PAIS"].Valor == "PERU" or Formulario["PAIS"].Valor == "POLÔNIA" or Formulario["PAIS"].Valor == "QUÊNIA" or Formulario["PAIS"].Valor == "REPÚBLICA DOMINICANA" or Formulario["PAIS"].Valor == "ROMÊNIA" or Formulario["PAIS"].Valor == "RUANDA" or Formulario["PAIS"].Valor == " SÃO TOMÉ E PRÍNCIPE" or Formulario["PAIS"].Valor == "SENEGAL" or Formulario["PAIS"].Valor == "TANZÂNIA" or Formulario["PAIS"].Valor == "SUDÃO"  or Formulario["PAIS"].Valor == "URUGUAI" or Formulario["PAIS"].Valor == "UZBEQUISTÃO" or Formulario["PAIS"].Valor == "VENEZUELA":

    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "300"
                    
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "280"

    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "270"
                
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "260"
        
    else:
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "250"
                    
                    

            ################### grupo C

            
elif Formulario["PAIS"].Valor == "ANTÍGUA E BARBUDA" or Formulario["PAIS"].Valor == "ARÁBIA SAUDITA" or Formulario["PAIS"].Valor == "AZERBAIDJÃO" or Formulario["PAIS"].Valor == "BAHAMAS" or Formulario["PAIS"].Valor == "BAREINE" or Formulario["PAIS"].Valor == "BOTSUANA" or Formulario["PAIS"].Valor == "BRUNEI DARUSSALAM" or Formulario["PAIS"].Valor == "BULGÁRIA"  or Formulario["PAIS"].Valor == "CANADÁ" or Formulario["PAIS"].Valor == "CINGAPURA" or Formulario["PAIS"].Valor == "CONGO" or Formulario["PAIS"].Valor == "COSTA DO MARFIM" or Formulario["PAIS"].Valor == "CUBA" or Formulario["PAIS"].Valor == "DJIBUTI" or Formulario["PAIS"].Valor == "EMIRADOS ÁRABES" or Formulario["PAIS"].Valor == "FIJI" or Formulario["PAIS"].Valor == "GABÃO" or Formulario["PAIS"].Valor == "GUATEMALA" or Formulario["PAIS"].Valor == "REPÚBLICA DEMOCRÁTICA DO CONGO" or Formulario["PAIS"].Valor == "JAMAICA" or Formulario["PAIS"].Valor == "JORDÂNIA" or Formulario["PAIS"].Valor == "LETÔNIA" or Formulario["PAIS"].Valor == "LIBÉRIA" or Formulario["PAIS"].Valor == "GEÓRGIA" or Formulario["PAIS"].Valor == "GUINÉ EQUATORIAL" or Formulario["PAIS"].Valor == "HAITI" or Formulario["PAIS"].Valor == "MAURÍCIO" or Formulario["PAIS"].Valor == "MAURITÂNIA" or Formulario["PAIS"].Valor == "MÉXICO" or Formulario["PAIS"].Valor == "MALTA" or Formulario["PAIS"].Valor == " REPÚBLICA TCHECA" or Formulario["PAIS"].Valor == "RÚSSIA" or Formulario["PAIS"].Valor == "SAN MARINO" or Formulario["PAIS"].Valor == "SANTA LÚCIA"or Formulario["PAIS"].Valor == "SÃO CRISTOVÃO E NÉVIS" or Formulario["PAIS"].Valor == "SÃO VICENTE E GRANADINAS" or Formulario["PAIS"].Valor == "TAIWAN" or Formulario["PAIS"].Valor == "TRINIDAD E TOBAGO" or Formulario["PAIS"].Valor == "UCRÂNIA" or Formulario["PAIS"].Valor == "UGANDA" or Formulario["PAIS"].Valor == "ZÂMBIA":
    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "350"
                
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "330"
                    
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "320"
                
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "310"
    
    else:
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "300"     
                    
                
            #################### grupo D 
if Formulario["PAIS"].Valor == "ALEMANHA" or Formulario["PAIS"].Valor == "ANGOLA" or Formulario["PAIS"].Valor == "ÁUSTRIA" or Formulario["PAIS"].Valor == "BARBADOS" or Formulario["PAIS"].Valor == "BÉLGICA"or Formulario["PAIS"].Valor == "CAZAQUISTÃO" or Formulario["PAIS"].Valor == "CORÉIA DO SUL" or Formulario["PAIS"].Valor == "CROÁCIA"  or Formulario["PAIS"].Valor == "DINAMARCA" or Formulario["PAIS"].Valor == "ESPANHA" or Formulario["PAIS"].Valor == "ESTADOS UNIDOS DA AMÉRICA" or Formulario["PAIS"].Valor == "FINLÂNDIA" or Formulario["PAIS"].Valor == "FRANÇA" or Formulario["PAIS"].Valor == "GRANADA" or Formulario["PAIS"].Valor == "GRÉCIA HONG KONG" or Formulario["PAIS"].Valor == "IRLANDA" or Formulario["PAIS"].Valor == "ISLÂNDIA" or Formulario["PAIS"].Valor == "ISRAEL" or Formulario["PAIS"].Valor == "ITÁLIA" or Formulario["PAIS"].Valor == "JAPÃO" or Formulario["PAIS"].Valor == "KUAITE" or Formulario["PAIS"].Valor == "LIECHTENSTEIN" or Formulario["PAIS"].Valor == "LUXEMBURGO" or Formulario["PAIS"].Valor == "MÔNACO" or Formulario["PAIS"].Valor == "MONTENEGRO" or Formulario["PAIS"].Valor == "NORUEGA" or Formulario["PAIS"].Valor == "OMÃ" or Formulario["PAIS"].Valor == "PEÍSES BAIXOS" or Formulario["PAIS"].Valor == "PORTUGAL" or Formulario["PAIS"].Valor == "REINO UNIDO" or Formulario["PAIS"].Valor == "REPÚBLICA QUIRGUIZ" or Formulario["PAIS"].Valor == "SEICHELES" or Formulario["PAIS"].Valor == "SÉRVIA SUAZILÂNDIA" or Formulario["PAIS"].Valor == "SUÉCIA" or Formulario["PAIS"].Valor == "SUÍÇA" or Formulario["PAIS"].Valor == "VANUATU":
    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "460"
                
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "420"
            
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "390"
            
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "370"
                  
                  
    else:
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "350"
```
  - TIPO_DESTINO "Tipo da localidade de destino" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESTINO] obrigatório
  - SAIDA "Saída dia" [DatePicker DateTime → CPE_DESLOCAMENTO.SAIDA] obrigatório
  - RETORNO_DIA "Retorno dia" [DatePicker DateTime → CPE_DESLOCAMENTO.RETORNO_DIA] obrigatório — Coluna=3
  - SAIDA_HORA "Horário da Saída" [TextBox String → CPE_DESLOCAMENTO.SAIDA_HORA] obrigatório — Configuracao={"Mascara":"00:00"}
  - RETORNO_HORA "Horário do Retorno" [TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA] obrigatório — Coluna=3; Configuracao={"Mascara":"00:00"}
**RETORNO_HORA.ScriptModificado**
```python
import clr 
import datetime

data1 = ""
data2 = ""

data1 = Formulario["SAIDA"].Valor
data2 = Formulario["RETORNO_DIA"].Valor
 
delta = data2 - data1
diferenca = delta.Days

if diferenca == 0 or diferenca == '0':
    diferenca = 1


Formulario["DIAS_DE_TRA"].Valor = diferenca
Formulario["DIAS_DE_TRA"].Habilitado = False
```
  - DIAS_DE_TRA "Dias em Deslocamento" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA] obrigatório
  - TIPO_HOSPEDAGEM "Tipo de Hospedagem" [DropDownList String → CPE_DESLOCAMENTO.TIPO_HOSPEDAGEM] obrigatório
**TIPO_HOSPEDAGEM.ScriptModificado**
```python
Formulario["VALOR_DIARIA"].Valor = ""

if Formulario["TIPO_HOSPEDAGEM"].Valor == "Sem Hospedagem":
    Formulario["QUANTIDADE_DIARIA"].Visivel = False
    Formulario["QUANTIDADE_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    Formulario["PARCELA_COMPLEMENTAR"].Visivel = False
    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False
    Formulario["TOTAL_COMPLEMENTAR"].Visivel = False
    Formulario["TOTAL_COMPLEMENTAR"].Habilitado = False    
    Formulario["TOTAL_COMPLEMENTAR"].Valor = "0"   


##NOVO SCRIPT ADICIONADO PARA AVULSA SEM APRESENTAÇÃO DE NF    
if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa COM apresentação de NF" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA"].Visivel = True
    Formulario["VALOR_DIARIA"].Habilitado = True
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    #Formulario["PAHL_HOSPEDAGENS"].Visivel = True
    #Formulario["PAHL_HOSPEDAGENS"].Habilitado = True
    
    Formulario["QUANTIDADE_DIARIA"].Valor = ""

    
    
if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA"].Visivel = True
    Formulario["VALOR_DIARIA"].Habilitado = True
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    
    Formulario["QUANTIDADE_DIARIA"].Valor = ""
    

queryAdesaoDiariaAvulaSemApresentarNF = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, PESSOA.NOME From OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = CP_ORDEM_SERVICO.FAVORECIDO_COBRA Where OCORRENCIA.ASSUNTO = 'Adesão a diárias avulsas sem comprovação documental' And (OCORRENCIA.SITUACAO = 'FinalizadaSucesso' Or OCORRENCIA.SITUACAO = 'Aberto') and PESSOA.ID_PESSOA = '"+Formulario["FAVORECIDO_DESLOCAMENTO"].Valor+"'")

if queryAdesaoDiariaAvulaSemApresentarNF.Rows.Count == 0 and Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF":
    Formulario.ExibeMensagem("Parece que seu aceite, Adesão a diárias avulsas sem comprovação documental, não foi feito. O Aceite é necessário para este tipo de solicitação.")
    
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa":
    Formulario["QUANTIDADE_DIARIA"].Valor = ""
    Formulario["VALOR_DIARIA"].Valor = ""
    
#if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional"):
#    Formulario["QUANTIDADE_DIARIA"].Visivel = True
#    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA"].Visivel = True
#    Formulario["VALOR_DIARIA"].Habilitado = True
#    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
#    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
#    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False    
    

#if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional"):
#    Formulario["QUANTIDADE_DIARIA"].Visivel = False
#    Formulario["QUANTIDADE_DIARIA"].Habilitado = False
#    Formulario["VALOR_DIARIA"].Visivel = False
#    Formulario["VALOR_DIARIA"].Habilitado = False
#    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
#    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
#    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
```
  - QUANTIDADE_DIARIA "Quantidade de Diárias" [TextBox Integer → CPE_DESLOCAMENTO.QUANTIDADE_DIARIA]
**QUANTIDADE_DIARIA.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import OutputSubProcesso
def calculaDiaria():
    ############### SE O FAVORECIDO FOR DO GRUPO C MAS ESTARÁ ACOMPANHANDO O GRUPO B RECEBE O VALOR DO GRUPO B 
    
    if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
            Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
    
    elif Formulario["SIM_NAO"].Valor == "Sim" :
          if Formulario["CIDADE_DESTINO"].Valor == "3550308": # SAO PAULO 
                 Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "650"
                
          elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO E BRASILIA
            Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550"
            
          elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
              Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
          else: 
            Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
      
    else:     
            
        ############## SE FOR DO GRUPO A -  PRESIDENTE / DIRETOR / CONSELHEIRO NÃO TEM LIMITE   
        if Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "PRESIDENTE":
            Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
            
            
            
        ############## SE O FAVORECIDO FOR DO GRUPO B  ELE RECEBE REFERENTE A CIDADE     
        elif Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "GERENTE EXECUTIVO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE DE PROJETOS I" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "ASSESSOR EXEC DA PRESIDENCIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "SUPERINTENDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "SUPERINTENDENTE":
            if Formulario["CIDADE_DESTINO"].Valor == "3550308 ": # SAO PAULO 
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "650"
                    
            elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO OutputSubProcesso BRASILIA
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550"
                    
            elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or      Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
                      Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450" 
            else:
                Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
                  
                  
        ############## DEMAIS CARGOS
        elif Formulario["FUNCAO_DESLOCAMENTO"].Valor != "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "PRESIDENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE DE PROJETOS I" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "ASSESSOR EXEC DA PRESIDENCIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "SUPERINTENDENTE":
              
              if Formulario["CIDADE_DESTINO"].Valor == "3550308": # SAO PAULO 3550308 
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550" 
                    
              elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO ou BRASILIA
                        Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
                        
              elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or      Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
                          Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "370" 
                          
              else:
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "350"
                  

              
              
calculaDiaria()
     
############ VALOR FINAL DO ADIANTAMENTO EM DIARIAS      
diasViagem = Convert.ToInt32(Formulario["DIAS_DE_TRA"].Valor)
diasHospedagem = Convert.ToInt32(Formulario["QUANTIDADE_DIARIA"].Valor)



if diasHospedagem > diasViagem:
    mensagem = "Quantidade de Diária Excedida! Máximo Permitido: " + Formulario["DIAS_DE_TRA"].Valor + " Verifique a saída e o retorno"
    Formulario.ExibeMensagem(mensagem)      
    Formulario["VALOR_DIARIA"].Habilitado = False
else:
    Formulario["VALOR_DIARIA"].Habilitado = True   


#Valor parcela complementar    



if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":

    Formulario["PARCELA_COMPLEMENTAR"].Valor = "0"
    Formulario["PARCELA_COMPLEMENTAR"].Visivel = False
    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False    
    Formulario["TOTAL_COMPLEMENTAR"].Habilitado = False
    Formulario["TOTAL_COMPLEMENTAR"].Visivel = False
    Formulario["TOTAL_COMPLEMENTAR"].Valor = "0"
   
else:    
    Formulario["PARCELA_COMPLEMENTAR"].Valor = "19,74"
    Formulario["PARCELA_COMPLEMENTAR"].Visivel = True
    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False    
    
    pc = Formulario["PARCELA_COMPLEMENTAR"].Valor 
    qtd = Formulario["QUANTIDADE_DIARIA"].Valor
    total = 0

    total = pc * qtd
    
    Formulario["TOTAL_COMPLEMENTAR"].Valor = total
    Formulario["TOTAL_COMPLEMENTAR"].Visivel = True


#Define o valor para hospedagem do tipo avulsa
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" and Formulario["CIDADE_CLASSIFICACAO"].Valor == "A":
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = 230.00
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = 230.00
    
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" and Formulario["CIDADE_CLASSIFICACAO"].Valor == "B":
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = 250.00
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = 250.00

if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" and Formulario["CIDADE_CLASSIFICACAO"].Valor == "C":
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = 270.00
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = 270.00
    

#if (Formulario["TIPO_DESTINO"].Valor == "Interior") and (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa"):
#    Formulario["VALOR_DIARIA"].Valor = "350"
#    
#if (Formulario["TIPO_DESTINO"].Valor == "Capital") and (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa"):
#    Formulario["VALOR_DIARIA"].Valor = "500"
#
#import System.Text
#daysOffText = System.Text.StringBuilder()
#
# #RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
#def isHoliday(day):
#    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C  inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
#   
#    for holiday in holidays.Rows:
#        if day == holiday["DATA"].Date:
#            return True
#    return False
#   
#def workingDays(totalDays, firstDate):
#    
#    totalWorkingDays = 0
#    totalDaysOff = 0
#    count = 0
#   
#    while count <= totalDays:
#        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
#        day = firstDate.Date.AddDays(count)
#        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
#            totalDaysOff = totalDaysOff + 1
#            daysOffText.AppendLine(" dayOff: "+str(day))
#        
#        count = count + 1
#        totalWorkingDays = totalWorkingDays + 1
#    return totalWorkingDays - totalDaysOff
#   
#
#saida = Formulario["SAIDA"].Valor
#retorno  = Formulario["RETORNO_DIA"].Valor
#
#totalDias = (retorno - saida).TotalDays  
#count = 0
#
#totalDiasUteis = workingDays(totalDias,saida) 
#totalDiasNaoUteis = totalDias - totalDiasUteis
#
############### almoço e janta de ambos os dias
#quantReduzida = totalDiasUteis  
#quantIntegral = (totalDiasNaoUteis * 2) + totalDiasUteis
#
#
#

#Formulario["QTD_REFEICAO_REDUZIDA"].Valor = totalDiasUteis 
#Formulario["QTD_REFEICAO_INTEGRAL"].Valor = totalDiasNaoUteis
#
#
#Formulario["VALOR_REF_REDUZIDA"].Valor = totalDiasUteis * 18.39
#Formulario["VALOR_REF_INTEGRAL"].Valor = totalDiasNaoUteis *  64.36
#
#
#OrdemServico.AdicionaComentario("WorkingDays "+totalWorkingDays.ToString(),False)
#OrdemServico.AdicionaComentario(daysOffText.ToString(),False )

#OrdemServico["totalWorkingDays"] = totalWorkingDays
```
  - VALOR_DISTANCIA "Valor previsto para percorrer distância R$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DISTANCIA] obrigatório — Coluna=2
  - SIM_NAO_REFEICAO "O Empregado/Gestor terá direito a refeição complementar?" [DropDownList String → CPE_DESLOCAMENTO.SIM_NAO_REFEICAO] obrigatório
**SIM_NAO_REFEICAO.ScriptModificado**
```python
import clr 
import datetime
import System.Text
 


zero = 0
valorRefIntegral = 71
valorRefReduzida = 20.29



daysOffText = System.Text.StringBuilder()


##RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
def isHoliday(day):
    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
    #feriados = 0
    
    for holiday in holidays.Rows:
        if day == holiday["DATA"].Date:
            #feriados += 2
            return True
    return False


def countHolidays(firstDate, lastDate):
    totalHolidays = 0
    currentDay = firstDate

    while currentDay <= lastDate:
        if isHoliday(currentDay):
            totalHolidays += 1
        currentDay = currentDay.AddDays(1)

    return totalHolidays

    
def workingDays(totalDays, firstDate):

    totalWorkingDays = 0
    totalDaysOff = 0
    count = 0

   
    while count <= totalDays:
        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
        day = firstDate.Date.AddDays(count)
        
        
        
        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
            totalDaysOff = totalDaysOff + 1
            daysOffText.AppendLine(" dayOff: "+str(day))
        
        count = count + 1
        totalWorkingDays = totalWorkingDays + 1
    return totalWorkingDays - totalDaysOff
   


    
def countSaturdays(firstDate, lastDate):
    saturdays = 0
    currentDay = firstDate
    
    while currentDay <= lastDate:
        if (currentDay.DayOfWeek == DayOfWeek.Sunday or currentDay.DayOfWeek == DayOfWeek.Saturday):
            saturdays += 2
        currentDay = currentDay.AddDays(1)  # Avance para o próximo dia
    
    return saturdays

    
firstDate = Formulario["SAIDA"].Valor
lastDate = Formulario["RETORNO_DIA"].Valor

totalDays = (lastDate - firstDate).TotalDays
count = 0





totalWorkingDays = workingDays(totalDays,firstDate)
holidaysCount = countHolidays(firstDate, lastDate)
saturdays = countSaturdays(firstDate, lastDate) + holidaysCount * 2


#Quantidade de refeições Reduzias e integrais
quantRed = totalWorkingDays
quantInt = saturdays + totalWorkingDays 






#Atribuindo valor a variável
saidaHora = Formulario["SAIDA_HORA"].Valor 
retornoHora = Formulario["RETORNO_HORA"].Valor 

#Split de horário, separando hora de minuto
hora = saidaHora.Split(':');     
horaRetorno = retornoHora.Split(':');

#Atribuindo valor de horário e minuto de acordo com o índice da variável
horarioSaida = hora[0]
minutoSaida = hora[1]

horarioRetorno = horaRetorno[0] 
minutoRetorno = horaRetorno[1]



#SAIDA DIAS ÚTEIS


#1 maior q o 2
#if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) >= 13 and Convert.ToInt32(horarioSaida) < 21):
#    quantRed = quantRed - 1
#   
#if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) > 21):
#    quantInt = quantInt - 1
#   
#RETORNO DIAS ÚTEIS
#1 menor q o 2   
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 13:
#    quantRed = quantRed - 1
#    quantInt = quantInt - 1
#    
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 19 and Convert.ToInt32(horarioRetorno) > 13:
#    quantInt = quantInt - 1
#    #teste abaixo
#    quantRed = quantRed - 1





#DIAS UTEIS

if workingDays(0,firstDate):
    if (Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0)):
        quantRed = quantRed - 1
    if (Convert.ToInt32(horarioSaida) > 21) or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
        quantInt = quantInt - 1
if workingDays(0,lastDate):    
    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
        quantRed = quantRed - 1
    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
        quantInt = quantInt - 1
#Formulario.ExibeMensagem("hora:"+horarioRetorno.ToString()+" minuto:"+minutoRetorno.ToString())    
###############################################################
    
#SAÍDA FINAIS DE SEMANA E/OU FERIADOS

if not  workingDays(0,firstDate):
    if Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0):
        quantInt = quantInt - 1
    if Convert.ToInt32(horarioSaida) > 21 or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
        quantInt = quantInt - 1
if not  workingDays(0,lastDate):
    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
        quantInt = quantInt - 1
    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
        quantInt = quantInt - 1   


if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA": 
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = zero
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = zero
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["VALOR_REF_REDUZIDA"].Visivel = False
    Formulario["VALOR_REF_INTEGRAL"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
    Formulario["SIM_NAO_REFEICAO"].Visivel = False
    Formulario["SIM_NAO_REFEICAO"].Habilitado = False
else:
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = quantRed
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = quantInt
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = True
    Formulario["VALOR_REF_REDUZIDA"].Visivel = True
    Formulario["VALOR_REF_INTEGRAL"].Visivel = True
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = True
    Formulario["SIM_NAO_REFEICAO"].Visivel = True
    Formulario["SIM_NAO_REFEICAO"].Habilitado = True
  
    
if quantRed > (totalWorkingDays):
    mensagem = ("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + str(totalWorkingDays + 1) + " Verifique a Saída e o Retorno.")
    Formulario.ExibeMensagem(mensagem)    
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    

############# calculo valor total

refIntegral = Formulario["QTD_REFEICAO_INTEGRAL"].Valor * valorRefIntegral
refReduzida = Formulario["QTD_REFEICAO_REDUZIDA"].Valor * valorRefReduzida
valorTotalRefeicoes = refIntegral + refReduzida

if Formulario["SIM_NAO_REFEICAO"].Valor == "Sim":
    Formulario["VALOR_TOTAL_REFEICAO"].Valor  = valorTotalRefeicoes
    Formulario["VALOR_REF_REDUZIDA"].Valor = refReduzida
    Formulario["VALOR_REF_INTEGRAL"].Valor = refIntegral
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = True
    Formulario["VALOR_REF_REDUZIDA"].Visivel = True
    Formulario["VALOR_REF_INTEGRAL"].Visivel = True
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = True
else:
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = zero
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = zero
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["VALOR_REF_REDUZIDA"].Valor = zero
    Formulario["VALOR_REF_INTEGRAL"].Valor = zero
    Formulario["VALOR_TOTAL_REFEICAO"].Valor = zero  
    Formulario["VALOR_REF_REDUZIDA"].Visivel = False
    Formulario["VALOR_REF_INTEGRAL"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
```
  - VALOR_DIARIA "Valor da Diaria R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DIARIA] obrigatório
**VALOR_DIARIA.ScriptModificado**
```python
if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
         Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = Formulario["VALOR_DIARIA"].Valor
    



if Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "PRESIDENTE": 
     Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = Formulario["VALOR_DIARIA"].Valor


     
     
if Convert.ToDecimal(Formulario["VALOR_DIARIA"].Valor) >= Convert.ToDecimal(Formulario["CAMPO_VALIDACAO_DIARIA"].Valor):
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["CAMPO_VALIDACAO_DIARIA"].Valor
else:
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
    
    
Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True

valorTotal = 0

quantDiaria = Convert.ToDecimal(Formulario["QUANTIDADE_DIARIA"].Valor)
valorDiaria = Convert.ToDecimal(Formulario["VALOR_DIARIA_AUTORIZADO"].Valor)

valorTotal = quantDiaria * valorDiaria 

Formulario["VALOR_TOTAL_DIARIA"].Valor =  valorTotal 


OrdemServico["VALOR_TOTAL_DIARIA"] = valorTotal
```
  - VALOR_DIARIA_AUTORIZADO "Valor Diária Autorizado" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_AUTORIZADO] obrigatório — Coluna=2
  - CAMPO_VALIDACAO_DIARIA "Diária máxima autorizada R$ (TAB320-001)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DIARIA] obrigatório
  - VALOR_TOTAL_DIARIA "Valor Total Diária:" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_DIARIA]
  - LABEL1 "Cotação do Dólar Americano Conforme Aprovado na NT" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - COTACAO_DOLAR "Cotação do Dólar americano (USD) " [TextBox String → CPE_DESLOCAMENTO.COTACAO_DOLAR] obrigatório
**COTACAO_DOLAR.ScriptModificado**
```python
#import System
#
#valorTotal = 0
#
#
#valorTotal = Formulario["VALOR_TOTAL_DIARIA"].Valor * Convert.ToDecimal(Formulario["COTACAO_DOLAR"].Valor)
#
#
#Convert.ToDecimal(Formulario["DIARIA_COTACAO_REAL"].Valor) = valorTotal


valorTotal = 0
vtd = Formulario["VALOR_TOTAL_DIARIA"].Valor
cd = Convert.ToDecimal(Formulario["COTACAO_DOLAR"].Valor)

valorTotal = vtd * cd

Formulario["DIARIA_COTACAO_REAL"].Valor = valorTotal




#valorTotal = 0
#
#
#valorTotal = Formulario["VALOR_TOTAL_DIARIA"].Valor * (Formulario["COTACAO_DOLAR"].Valor)
#
#
#Formulario["DIARIA_COTACAO_REAL"].Valor = valorTotal
#

#diariaReal = ""
#cotacao = ""
#valorTotal = ""
#
#diariaReal = Convert.ToDouble(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#cotacao = Convert.ToDouble(Formulario["COTACAO_DOLAR"].Valor)
```
  - DIARIA_COTACAO_REAL "Diária em Real" [TextBox String → CPE_DESLOCAMENTO.DIARIA_COTACAO_REAL] obrigatório — Coluna=2
  - NUMERO_NT "Número da Nota Técnica" [TextBox String → CPE_CONTRATOS.NUMERO_NT] obrigatório — Configuracao={"Mascara":"0000/0000"}
  - PARCELA_COMPLEMENTAR "Parcela Complementar de hospedagem" [TextBox Decimal → CPE_DESLOCAMENTO.PARCELA_COMPLEMENTAR] obrigatório
  - TOTAL_COMPLEMENTAR "Total Parcela Complementar (Não é necessário prestar contas)" [TextBox Decimal → CPE_DESLOCAMENTO.TOTAL_COMPLEMENTAR] obrigatório
  - QTD_REFEICAO_REDUZIDA "Quantidade de refeições reduzidas" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_REDUZIDA] obrigatório
**QTD_REFEICAO_REDUZIDA.ScriptModificado**
```python
import calculos_deslocamento_v29
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.


import clr 
import datetime
import System.Text

Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    
qtdRef = qtdRefeicoes(Formulario["SAIDA"].Valor, Formulario["RETORNO_DIA"].Valor, Formulario["SAIDA_HORA"].Valor, Formulario["RETORNO_HORA"].Valor)


if Convert.ToInt32(qtdRef[0]['integral']) < Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor):
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = qtdRef[0]['integral']
    Formulario.ExibeMensagem("Quantidade de Refeições Integrais Excedida! Máximo permitido: " + qtdRef[0]['integral'].ToString() + " Verifique a Saída e o Retorno.")
if Convert.ToInt32(qtdRef[0]['reduzida']) < Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor):
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = qtdRef[0]['reduzida']
    Formulario.ExibeMensagem("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + qtdRef[0]['reduzida'].ToString() + " Verifique a Saída e o Retorno.")
    
valor = valorRefeicoes(Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor),Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor))

Formulario["VALOR_TOTAL_REFEICAO"].Valor = valor[0]['total']
Formulario["VALOR_REF_REDUZIDA"].Valor = valor[0]['reduzida']
Formulario["VALOR_REF_INTEGRAL"].Valor = valor[0]['integral']
```
  - VALOR_TOTAL_REFEICAO "Valor total previsto para refeições: R$" [TextBox String → CPE_ORDEM_SERVICO.VALOR_TOTAL_REFEICAO] obrigatório — Coluna=2
  - QTD_REFEICAO_INTEGRAL "Quantidade de Refeições Integrais" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_INTEGRAL] obrigatório
**QTD_REFEICAO_INTEGRAL.ScriptModificado**
```python
import calculos_deslocamento_v29
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.


import System
import clr 
import datetime
import System.Text

Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False

qtdRef = qtdRefeicoes(Formulario["SAIDA"].Valor, Formulario["RETORNO_DIA"].Valor, Formulario["SAIDA_HORA"].Valor, Formulario["RETORNO_HORA"].Valor)


if Convert.ToInt32(qtdRef[0]['integral']) < Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor):
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = qtdRef[0]['integral']
    Formulario.ExibeMensagem("Quantidade de Refeições Integrais Excedida! Máximo permitido: " + qtdRef[0]['integral'].ToString() + " Verifique a Saída e o Retorno.")
if Convert.ToInt32(qtdRef[0]['reduzida']) < Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor):
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = qtdRef[0]['reduzida']
    Formulario.ExibeMensagem("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + qtdRef[0]['reduzida'].ToString() + " Verifique a Saída e o Retorno.")
    
valor = valorRefeicoes(Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor),Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor))

Formulario["VALOR_TOTAL_REFEICAO"].Valor = valor[0]['total']
Formulario["VALOR_REF_REDUZIDA"].Valor = valor[0]['reduzida']
Formulario["VALOR_REF_INTEGRAL"].Valor = valor[0]['integral']
```
  - VALOR_REF_REDUZIDA "Valor Refeições Reduzidas" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_REDUZIDA] obrigatório
  - VALOR_REF_INTEGRAL "Valor refeições integrais" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_INTEGRAL]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Bloco 2
  - SIM_NAO2 "O funcionário/Gestor receberá um valor não previsto no pedido inicial do deslocamento?" [DropDownList String → CPE_CSC.SIM_NAO2] obrigatório
**SIM_NAO2.ScriptModificado**
```python
if Formulario["SIM_NAO2"].Valor == "Sim":    
#    Formulario["NOME_PROJETO"].Habilitado = True    
#    Formulario["NOME_PROJETO"].Visivel = True    
    Formulario["VALOR_DOD"].Habilitado = True    
    Formulario["VALOR_DOD"].Visivel = True
#    Formulario["VALOR_EXTRA"].Habilitado = True    
#    Formulario["VALOR_EXTRA"].Visivel = True  
    #Formulario["SIM_NAO4"].Habilitado = True    
    #Formulario["SIM_NAO4"].Visivel = True     
    
else:    

#    Formulario["NOME_PROJETO"].Habilitado = False    
#    Formulario["NOME_PROJETO"].Visivel = False    
    Formulario["VALOR_DOD"].Habilitado = False    
    Formulario["VALOR_DOD"].Visivel = False
#    Formulario["VALOR_EXTRA"].Habilitado = False    
#    Formulario["VALOR_EXTRA"].Visivel = False
    #Formulario["SIM_NAO4"].Habilitado = False    
    #Formulario["SIM_NAO4"].Visivel = False
    Formulario["VALOR_DOD"].Valor = 0
    
if Formulario["SIM_NAO2"].Valor == "Sim" and Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor != "": 
    Formulario["VALOR_DOD"].Valor = Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor
```
  - VALOR_DOD "Valor do reembolso:" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD] obrigatório
**VALOR_DOD.ScriptModificado**
```python
if Formulario["VALOR_DOD"].Valor >= 0:
    Formulario.ExibeMensagem("IMPORTANTE: Clique no botão SALVAR antes de cálcular o custo total da viagem.")
    OrdemServico.Salva
```
  - VALORTOTALPB "Valor de devolução:" [TextBox Decimal → CPE_PRJ_BB.VALORTOTALPB] obrigatório
**VALORTOTALPB.ScriptModificado**
```python
#if Formulario["VALORTOTALPB"].Valor >= 0:
    #Formulario.ExibeMensagem("IMPORTANTE: Clique no botão SALVAR antes de cálcular o custo total da viagem.")
    #OrdemServico.Salva
```
  - COMBOBOX_CONFIRMA_TREINAMENTO "Clique aqui para verificar o custo total da viagem" [CheckBox Boolean → CPE_PESSOAS.COMBOBOX_CONFIRMA_TREINAMENTO] obrigatório
**COMBOBOX_CONFIRMA_TREINAMENTO.ScriptModificado**
```python
zero = 0

if Formulario["SIM_NAO2"].Valor == "Sim":
    despesas = Convert.ToDecimal(Formulario["VALOR_DOD"].Valor)  
else:
    despesas = 0



valorDistCampo = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)

gastorNPrevi = Formulario["SIM_NAO2"].Valor
devolucao = Formulario["SIM_NAO3"].Valor
tipoHospeda = Formulario["TIPO_HOSPEDAGEM"].Valor
cargoDes = Formulario["CARGO_DESLOCAMENTO"].Valor
funcaoDes = Formulario["FUNCAO_DESLOCAMENTO"].Valor
tipoDeslocament = Formulario["TIPO_DESLOCAMENTO"].Valor
valorReembolso = Convert.ToDecimal(Formulario["VALOR_DOD"].Valor)
outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
diariaAvulsaSemPrestarContas = 0

#inicia a variavel valorTotalPrestContas
valorTotalPrestContas = 0

#Inicia a variavel totalSemPrestContas
totalSemPrestContas = 0
   

if gastorNPrevi == "Não":
    Formulario["VALORTOTSEMCOMPROV"].Valor = zero
    
    #novo - adiciona ao campo do formulario
    Formulario["VALORTOTSEMCOMPROV"].Valor = 0

if devolucao == "Não":
    Formulario["VALOR_TOT_PREST_CONTAS"].Valor = zero
    
    #novo - adiciona ao campo do formulario
    Formulario["VALOR_TOT_PREST_CONTAS"].Valor = 0


if tipoHospeda == "Avulsa":
    diariaAvulsa = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)  
else:
    diariaAvulsa = 0
    diariaAvulsaSemPrestarContas = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
 
     
if valorDistCampo != 0:
    valorDist = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)

else:
    valorDist = 0 
    

if Formulario["COMBOBOX_CONFIRMA_TREINAMENTO"].Valor == True:

    #Se for viagem nacional contabilizar outras despesas, diaria avulsa e valor distancia
    #valorTotalPrestContas = outrasDespesas + diariaAvulsa + valorDist + valorReembolso
    if OrdemServico["TIPO_DESLOCAMENTO"] != "Viagem a Serviço - Internacional":
        valorTotalPrestContas = outrasDespesas + diariaAvulsa + valorDist
        Formulario['VALOR_TOT_PREST_CONTAS'].Valor = valorTotalPrestContas
   
    #Se for viagem internacional contabilizar apenas outras despesas
    #valorTotalPrestContas = outrasDespesas
    if OrdemServico["TIPO_DESLOCAMENTO"] == "Viagem a Serviço - Internacional":
        valorTotalPrestContas = outrasDespesas
        Formulario['VALOR_TOT_PREST_CONTAS'].Valor = valorTotalPrestContas
    
    
#else:
 #   Formulario['VALOR_TOT_PREST_CONTAS'].Valor = 0
      


#Valores sem necessidade de prestação de contas

refeicoes = 0
hospeda = 0
complementar = 0
valorPassagens = Convert.ToDecimal(OrdemServico.GetCustom('CSC_VALOR1_TOTAL'))
valorCarro = Convert.ToDecimal(OrdemServico.GetCustom('CSC_VALOR2'))

if cargoDes == "PRESIDENTE" or cargoDes == "DIRETOR" or cargoDes == "CONSELHEIRO FISCAL" or cargoDes == "CONSELHEIRO DE ADMINISTRACAO" or cargoDes == "MEMBRO COMITE DE AUDITORIA" or funcaoDes == "PRESIDENTE" or  funcaoDes == "DIRETOR" or  funcaoDes == "CONSELHEIRO  FISCAL" or funcaoDes == "CONSELHEIRO DE ADMINISTRACAO" or funcaoDes == "MEMBRO COMITE DE AUDITORIA":
    refeicoes = 0
else:
    refeicoes = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)

#valor total da diária informada pelo Cesec após seleção no argo. CSC_VALOR1 = Valor total das diárias    
if tipoHospeda == "Contratada":
   hospeda = Convert.ToDecimal(OrdemServico.GetCustom("CSC_VALOR1"))
   
elif tipoHospeda == "Sem Hospedagem":
   hospeda = 0
   
 
if cargoDes == "PRESIDENTE" or cargoDes == "DIRETOR" or cargoDes == "MEMBRO COMITE DE AUDITORIA" or cargoDes == "CONSELHEIRO DE ADMINISTRACAO" or cargoDes == "CONSELHEIRO FISCAL" or funcaoDes == "PRESIDENTE" or  funcaoDes == "DIRETOR" or funcaoDes == "MEMBRO COMITE DE AUDITORIA" or  funcaoDes == "CONSELHEIRO DE ADMINISTRACAO" or funcaoDes == "CONSELHEIRO  FISCAL" or tipoDeslocament == "Viagem a Serviço - Internacional":
    complementar = 0
else:
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)

if OrdemServico["TIPO_DESLOCAMENTO"] != "Viagem a Serviço - Internacional":
    #VALOR TOTAL SEM NECESSIDADE DE PRESTAÇÃO DE CONTAS COM DOCUMENTAÇÃO
    #totalSemPrestContas = 0    
    if tipoHospeda == "Contratada": 
        #totalSemPrestContas = complementar + hospeda + refeicoes + valorPassagens + valorCarro + valorReembolso
        totalSemPrestContas = complementar + hospeda + refeicoes + valorPassagens + valorCarro
    #    Formulario['VALORTOTSEMCOMPROV'].Valor = totalSemPrestContas
        
    if tipoHospeda == "Avulsa" or tipoHospeda == "Sem Hospedagem":
        #totalSemPrestContas = complementar + hospeda + refeicoes + valorPassagens + valorCarro + valorReembolso
        #totalSemPrestContas = complementar + refeicoes + valorPassagens + valorCarro + valorReembolso
        totalSemPrestContas = complementar + refeicoes + valorPassagens + valorCarro
    #    Formulario['VALORTOTSEMCOMPROV'].Valor = totalSemPrestContas

    if tipoHospeda == "Avulsa SEM apresentação de NF":
        #totalSemPrestContas = complementar + hospeda + refeicoes + valorPassagens + valorCarro + valorReembolso
        #totalSemPrestContas = complementar + refeicoes + valorPassagens + valorCarro + valorReembolso
        totalSemPrestContas = complementar + refeicoes + valorPassagens + valorCarro + diariaAvulsaSemPrestarContas
    #    Formulario['VALORTOTSEMCOMPROV'].Valor = totalSemPrestContas     
        
    if totalSemPrestContas != 0:
        Formulario['VALORTOTSEMCOMPROV'].Valor = totalSemPrestContas
    #else:
    #    Formulario['VALORTOTSEMCOMPROV'].Valor = totalSemPrestContas
    
if OrdemServico["TIPO_DESLOCAMENTO"] == "Viagem a Serviço - Internacional":
    diariaCotacaoReal = Convert.ToDecimal(Formulario["DIARIA_COTACAO_REAL"].Valor)
    totalSemPrestContas = diariaCotacaoReal
    Formulario['VALORTOTSEMCOMPROV'].Valor = totalSemPrestContas

##########################################################################################################

    

Formulario['CUSTO_TOT_DESLOC'].Visivel = True    
Formulario["VALOR_TOT_PREST_CONTAS"].Visivel = True
Formulario["VALORTOTSEMCOMPROV"].Visivel = True


#######Custo total de deslocamento

#    custoTotalDeslocamento = 0    
#    valortotAdiant = Convert.ToDecimal(Formulario['VALOR_TOTAL_ADIANTAMENTO'].Valor)
#    valorDiariaDolar = Convert.ToDecimal(Formulario['VALOR_DIARIA_DOLAR'].Valor)
#    valorPassagens = Convert.ToDecimal(OrdemServico.GetCustom('CSC_VALOR1_TOTAL'))
#    valorDevolucao = Convert.ToDecimal(Formulario['VALORTOTALPB'].Valor)
#    ##valorReembolso = Convert.ToDecimal(OrdemServico.GetCustom('VALOR_EXTRA'))
#
#    if tipoHospeda == "Contratada" or tipoHospeda == "Sem Hospedagem": 
#        custoTotalDeslocamento = valortotAdiant + valorDiariaDolar + valorPassagens + despesas + valorCarro + hospeda - valorDevolucao
#        
#    if tipoHospeda == "Avulsa": 
#        custoTotalDeslocamento = valortotAdiant + valorDiariaDolar + valorPassagens + despesas + valorCarro - valorDevolucao
#        #Formulario["VALORTOTSEMCOMPROV"].Valor = custoTotalDeslocamento
#        #Formulario["VALOR_TOT_PREST_CONTAS"].Valor = valortotAdiant + valorDiariaDolar + valorPassagens + despesas + valorCarro
#        #Formulario["VALOR_TOT_PREST_CONTAS"].Valor = 0
#    Formulario['CUSTO_TOT_DESLOC'].Valor = custoTotalDeslocamento    

#if tipoHospeda == "Avulsa": 
    #custoTotalDeslocamento = valortotAdiant + valorDiariaDolar + valorPassagens + despesas + valorCarro - valorDevolucao
#Formulario['CUSTO_TOT_DESLOC'].Valor = custoTotalDeslocamento

custoTotalDeslocamento = 0   
valorDevolucao = Convert.ToDecimal(Formulario['VALORTOTALPB'].Valor)

if tipoHospeda == "Avulsa" or tipoHospeda == "Avulsa SEM apresentação de NF" or tipoHospeda == "Contratada" or tipoHospeda == "Sem Hospedagem":
    custoTotalDeslocamento = totalSemPrestContas + valorTotalPrestContas
    Formulario['CUSTO_TOT_DESLOC'].Valor = custoTotalDeslocamento
```
  - VALORTOTSEMCOMPROV "Valor total sem necessidade de comprovação documental" [TextBox Decimal → CPE_CSC.VALORTOTSEMCOMPROV]
  - SIM_NAO3 "Haverá necessidade de devolução de valor para a BBTS?" [DropDownList String → CPE_CSC.SIM_NAO3] obrigatório
**SIM_NAO3.ScriptModificado**
```python
if Formulario["SIM_NAO3"].Valor == "Sim":
    Formulario["STRING_ERP"].Habilitado = True
    Formulario["STRING_ERP"].Visivel = True
    Formulario["VALORTOTALPB"].Habilitado = True
    Formulario["VALORTOTALPB"].Visivel = True
else:
    Formulario["STRING_ERP"].Habilitado = False
    Formulario["STRING_ERP"].Visivel = False
    Formulario["VALORTOTALPB"].Habilitado = False
    Formulario["VALORTOTALPB"].Visivel = False
    
if Formulario["SIM_NAO3"].Valor == "Sim" and Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor != "" and Convert.ToDecimal(Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor) < 0: 
    Formulario["VALORTOTALPB"].Valor = Convert.ToDecimal(Formulario["VALOR_DIFERENCA_DESLOCAMENTO"].Valor) * -1
    Formulario["VALORTOTALPB"].Habilitado = False
    
OrdemServico.Salva()
```
  - STRING_ERP "Descrição dos valores a devolver" [TextBox String → CP_ORDEM_SERVICO.STRING_ERP] obrigatório
  - VALOR_TOT_PREST_CONTAS "Valor total a prestar contas com documentação (incluindo comprovante de devolução, se houver)" [TextBox Decimal → CPE_CSC.VALOR_TOT_PREST_CONTAS]
  - VALOR_TOTAL_ADIANTAMENTO "Valor total do adiantamento ao empregado" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_ADIANTAMENTO]
  - CUSTO_TOT_DESLOC "Custo total do deslocamento (descontado o valor de devolução)" [TextBox Decimal → CPE_HOMOLOGACAO.CUSTO_TOT_DESLOC] obrigatório

### [347984] EventoIntermediarioTimer ""
Config: TempoIntervalo=1440

### [347985] EventoIntermediarioMensagem "Prestação de Contas - Deslocamento"
Destinatário: Cliente e Favorecido Deslocamento (papel 1021)
ModeloComunicado: Prestação de Contas - Deslocamento
Corpo do comunicado: Prezado(a) OrdemServico.Customizado.FAVORECIDO_DESLOCAMENTO ,
Você realizou um deslocamento no dia OrdemServico.Customizado.SAIDA 
É necessário realizar sua prestação de contas. Para isso Link.Edicao Worklist , insira as informações e documentos referente ao deslocamento e clique em "Avançar".
Atenciosamente,
Central de Serviços

### [347986] Tarefa "Efetuar Pagamento"
Responsável: Responsável atual (papel 36)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
idFavorecido = Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_DESLOCAMENTO"))
#teste = '111094' 
#OrdemServico.SetCustom('MATRICULA_DESLOCAMENTO',teste.ToString)
favorecido = Pessoa.Carrega(idFavorecido)
nomeFavorecido = favorecido.Nome
#Utils.LogError("Pessoa: " + favorecido.ToString(), "DEBUG" + OrdemServico.Numero.ToString())

orgao = Orgao.Carrega(favorecido.OrgaoId)
#sigla = orgao.Sigla
#OrdemServico.SetCustom("SCR_TODOS_RH",sigla.ToString())
#
#
matricula = OrdemServico.GetCustom("MATRICULA_DESLOCAMENTO")
sigla = DB.ExecuteScalar ("SELECT SUBSTR(organizacao,1,10) as uor FROM cad_funcionario_v where matricula='" + matricula.ToString() + "'")

#Utils.LogError("Matricula: " + matricula.ToString(), "DEBUG" + OrdemServico.Numero.ToString())

#if OrdemServico.GetCustom("VALOR_TOTAL_REEMBOLSO").ToString() != None and OrdemServico.GetCustom("VALOR_TOTAL_REEMBOLSO").ToString() != '0' and OrdemServico.GetCustom("VALOR_TOTAL_REEMBOLSO").ToString() != '':
#    valorTotal = Convert.ToDecimal(OrdemServico.GetCustom("VALOR_TOTAL_REEMBOLSO").ToString())
#OrdemServico.AdicionaComentario('teste10', False)    
valorAdiantamento = 0
total_pestacao = 0
total_demaisDesp = 0
total_passag_contr = 0
total_hosp_contr = 0
total_carro_loc = 0
temReembolso='Não'
temDevolucao='Não'
fornecedor_passivo = '001.110001.3000001000.219399.000000.000.00000'

#Utils.LogError("Tem Reembolso: " + temReembolso.ToString(), "DEBUG" + OrdemServico.Numero.ToString())
#Utils.LogError("Tem Devolução: " + temDevolucao.ToString(), "DEBUG" + OrdemServico.Numero.ToString())

if (not String.IsNullOrEmpty(OrdemServico.GetCustom('VALOR_TOTAL_ADIANTAMENTO').ToString())) and OrdemServico["VALOR_TOTAL_ADIANTAMENTO"].ToString() != None and OrdemServico["VALOR_TOTAL_ADIANTAMENTO"].ToString() != '0' and OrdemServico["VALOR_TOTAL_ADIANTAMENTO"].ToString() != '':
    valorAdiantamento = OrdemServico["VALOR_TOTAL_ADIANTAMENTO"].ToString()

#Utils.LogError("valorAdiantamento: " + valorAdiantamento.ToString(), "DEBUG " + OrdemServico.Numero.ToString())

if (not String.IsNullOrEmpty(OrdemServico.GetCustom('VALOR_TOT_PREST_CONTAS').ToString())) and OrdemServico["VALOR_TOT_PREST_CONTAS"].ToString() != None and OrdemServico["VALOR_TOT_PREST_CONTAS"].ToString() != '0' and OrdemServico["VALOR_TOT_PREST_CONTAS"].ToString() != '':
        total_pestacao = OrdemServico["VALOR_TOT_PREST_CONTAS"].ToString()

#Utils.LogError("total_pestacao: " + total_pestacao.ToString(), "Debug " + OrdemServico.Numero.ToString())
    
if (not String.IsNullOrEmpty(OrdemServico.GetCustom('VALOR_DESPESAS').ToString())) and OrdemServico["VALOR_DESPESAS"].ToString() != None and OrdemServico["VALOR_DESPESAS"].ToString() != '0' and OrdemServico["VALOR_DESPESAS"].ToString() != '':
    total_demaisDesp = OrdemServico["VALOR_DESPESAS"].ToString()

#Utils.LogError("total_demaisDesp: " + total_demaisDesp.ToString(), "Debug " + OrdemServico.Numero.ToString())
##VALORES SERVIÇOS CONTRATADOS
#if (not String.IsNullOrEmpty(OrdemServico.GetCustom("CSC_VALOR1_TOTAL"))) and OrdemServico.GetCustom("CSC_VALOR1_TOTAL").ToString() != None:
if (OrdemServico.GetCustom("CSC_VALOR1_TOTAL")!= DBNull.Value):# and OrdemServico.GetCustom("CSC_VALOR1_TOTAL").ToString() != None:
    total_passag_contr = Convert.ToDecimal(OrdemServico.GetCustom('CSC_VALOR1_TOTAL'))
    
#Utils.LogError("total_passag_contr: " + total_passag_contr.ToString(), "Debug " + OrdemServico.Numero.ToString())

if (not String.IsNullOrEmpty(Convert.ToDecimal(OrdemServico.GetCustom('CSC_VALOR1')).ToString())) and Convert.ToDecimal(OrdemServico.GetCustom('CSC_VALOR1')).ToString() != '0':
    total_hosp_contr = Convert.ToDecimal(OrdemServico.GetCustom('CSC_VALOR1').ToString())

#Utils.LogError("total_hosp_contr: " + total_hosp_contr.ToString(), "Debug " + OrdemServico.Numero.ToString())
#if (not String.IsNullOrEmpty(OrdemServico.GetCustom("CSC_VALOR2").ToString())) and (OrdemServico.GetCustom('CSC_VALOR2').ToString()!= None):
if (OrdemServico.GetCustom("CSC_VALOR2") != DBNull.Value):# and (OrdemServico.GetCustom('CSC_VALOR2').ToString()!= None):

    total_carro_loc = Convert.ToDecimal(OrdemServico.GetCustom('CSC_VALOR2'))
    
#Utils.LogError("total_carro_loc: " + total_carro_loc.ToString(), "Debug " + OrdemServico.Numero.ToString())

if (not String.IsNullOrEmpty(OrdemServico.GetCustom("SIM_NAO2"))):
    temReembolso = OrdemServico.GetCustom("SIM_NAO2")

#Utils.LogError("temReembolso: " + temReembolso.ToString(), "Debug " + OrdemServico.Numero.ToString())

if (not String.IsNullOrEmpty(OrdemServico.GetCustom("SIM_NAO3"))):
    temDevolucao = OrdemServico.GetCustom("SIM_NAO3")
    
#Utils.LogError("temDevolucao: " + temDevolucao.ToString(), "Debug " + OrdemServico.Numero.ToString())
      
numero = OrdemServico.Numero.ToString()


qry = "SELECT MAX(INICIO_DATA_FUNCAO), EMPRESA, SUBSTR('"+sigla.ToString()+"', 1, 1) AS PREFIXO  FROM CAD_FUNCIONARIO_V WHERE DATA_DE_DEMISSAO IS NULL AND MATRICULA = '" + matricula.ToString() + "' GROUP BY EMPRESA"

#Utils.LogError("qry: " + qry.ToString(), "Debug " + OrdemServico.Numero.ToString())

lista = Utils.ExecuteDataTable(qry)
if (lista != None):
    for linha in lista.Rows:
        if (DBNull.Value.Equals(linha["EMPRESA"]) != True ):
            empresa = linha["EMPRESA"].ToString()
            OrdemServico.SetCustom("NUM_CHAVE",empresa.ToString())
            
        if (DBNull.Value.Equals(linha["PREFIXO"]) != True ):
            scr = linha["PREFIXO"].ToString()
            OrdemServico.SetCustom("NUM_ITEM",scr.ToString())  


filial = OrdemServico["NUM_CHAVE"].ToString()
inicio = OrdemServico["NUM_ITEM"].ToString()
uor = sigla
termo = '00 DDL'
if filial == '999994' and uor == '3000003204':
    filial ='410013'

    
#--- Prefixo da conta contábil (337 quando a UOR iniciar com 1 ou 2 e 343 quando iniciar com 3 ou 4)
if inicio == '1' or inicio == '2':
    prefixo = '337'
else:
    prefixo = '343'
nota = 'RDV'

############Quando o valor total do Adiantamento for IGUAL ao valor da Prestação de Contas
###if valorAdiantamento == total_pestacao:
if temReembolso=='Não' and temDevolucao == 'Não':
    rubrica = '90303'
    fornecedor = '001.110001.3000001000.114201.000000.000.00000'
    
    conta = "001."+ filial +"."+ uor +"."+ prefixo + rubrica +".000000.000.00000"
    OrdemServico.SetCustom("NUM_DOCU", conta)
    valor = DB.ExecuteScalar("select replace('"+ valorAdiantamento.ToString() + "',',','.') as valor from dual")
    valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '999999D99') as valor from dual")
    valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")
    
    SQLcontInterfaceGL = "SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND REFERENCE1 LIKE '%PREST_CONTAS_ADIANT_LOC%'"
    
    #Utils.LogError("SQLcontInterfaceGL_1: " + SQLcontInterfaceGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
        
    contInterfaceGL = DB.ExecuteScalar(SQLcontInterfaceGL.ToString())
    
    SQLcontGL = "SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND NAME LIKE '%PREST_CONTAS_ADIANT_LOC%'"
    
    #Utils.LogError("SQLcontGL_1: " + SQLcontGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
        
    contGL = DB.ExecuteScalar(SQLcontGL.ToString())
    
    valordecimal = Convert.ToDecimal(valorAdiantamento)

    #----- insert no GL
    #--- débito
    if contInterfaceGL.ToString()=='0' and contGL.ToString()=='0' and valor.ToString().Trim() != '.00' and valor.ToString() !='0' and valordecimal > 0:
        OrdemServico.AdicionaComentario("Procedure para débito GL_1: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC"+ numero +"','PREST_CONTAS_ADIANT_LOC"+ numero +"') ", False)
        
        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC"+ numero +"','PREST_CONTAS_ADIANT_LOC"+ numero +"') ")
        #--- crédito
        OrdemServico.AdicionaComentario("Procedure para Credito GL_1: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC"+ numero +"','PREST_CONTAS_ADIANT_LOC"+ numero +"') ", False)
        
        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC"+ numero +"','PREST_CONTAS_ADIANT_LOC"+ numero +"') ")
        
####FINAL Quando o valor total do Adiantamento for IGUAL ao valor da Prestação de Contas

#############Quando o valor total do Adiantamento for MAIOR do que o valor da Prestação de Contas
##if Convert.ToDecimal(valorAdiantamento) > Convert.ToDecimal(total_pestacao):
if temReembolso=='Não' and temDevolucao == 'Sim':
    #####Pelo registro contábil do valor total adiantado para o funcionário
    rubrica = '90303'
    fornecedor = '001.110001.3000001000.114201.000000.000.00000'
    conta = "001."+ filial +"."+ uor +"."+ prefixo + rubrica +".000000.000.00000"
    OrdemServico.SetCustom("NUM_DOCU", conta)
    valor = DB.ExecuteScalar("select replace('"+ valorAdiantamento.ToString() + "',',','.') as valor from dual")
    valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '999999D99') as valor from dual")
    valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")
    
    SQLcontInterfaceGL = "SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND REFERENCE1 LIKE '%PREST_CONTAS_ADIANT_LOC%'"
    
    Utils.LogError("SQLcontInterfaceGL_2: " + SQLcontInterfaceGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
        
    contInterfaceGL = DB.ExecuteScalar(SQLcontInterfaceGL.ToString())
    
    SQLcontGL = "SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND NAME LIKE '%PREST_CONTAS_ADIANT_LOC%'"
    
    Utils.LogError("SQLcontGL_2: " + SQLcontGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
    
        
    contGL = DB.ExecuteScalar(SQLcontGL.ToString())
    valordecimal = Convert.ToDecimal(valorAdiantamento)

    #----- insert no GL
    #--- débito
    if contInterfaceGL.ToString()=='0' and contGL.ToString()=='0' and valor.ToString() !='0' and valordecimal > 0:
        OrdemServico.AdicionaComentario("Procedure para débito GL_2.1: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC"+ numero +"','PREST_CONTAS_ADIANT_LOC"+ numero +"') ", False)
        
        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC"+ numero +"','PREST_CONTAS_ADIANT_LOC"+ numero +"') ")
        #--- crédito
        OrdemServico.AdicionaComentario("Procedure para Credito GL_2.1: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC"+ numero +"','PREST_CONTAS_ADIANT_LOC"+ numero +"') ", False)
        
        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC"+ numero +"','PREST_CONTAS_ADIANT_LOC"+ numero +"') ")
    
    
    ########Pelo registro contábil do valor a ser devolvido pelo funcionário
    
    valorDevolvido = OrdemServico.GetCustom('VALORTOTALPB')
    #Convert.ToDecimal(valorAdiantamento) - Convert.ToDecimal(total_pestacao)
    rubrica = '90303'
    fornecedor = '001.110001.3000001000.114201.000000.000.00000'
    
    conta = "001."+ filial +"."+ uor +"."+ prefixo + rubrica +".000000.000.00000"
    OrdemServico.SetCustom("NUM_DOCU", conta)
    valor = DB.ExecuteScalar("select replace('"+ valorDevolvido.ToString() + "',',','.') as valor from dual")
    valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '999999D99') as valor from dual")
    valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")
        
    SQLcontInterfaceGL = "SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND REFERENCE1 LIKE '%PREST_CONTAS_ADIANT_LOC_REST%'"
    
    #Utils.LogError("SQLcontInterfaceGL_2.2: " + SQLcontInterfaceGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
    
    contInterfaceGL = DB.ExecuteScalar(SQLcontInterfaceGL.ToString())
    
    SQLcontGL = "SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND NAME LIKE '%PREST_CONTAS_ADIANT_LOC_REST%'"
    
    #Utils.LogError("SQLcontGL_2.2: " + SQLcontGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
        
    contGL = DB.ExecuteScalar(SQLcontGL.ToString())
    valordecimal = Convert.ToDecimal(valorDevolvido)

    #----- insert no GL
    #--- débito
    if contInterfaceGL.ToString()=='0' and contGL.ToString()=='0' and valor.ToString() !='0' and valordecimal > 0:
        OrdemServico.AdicionaComentario("Procedure para débito GL_2.2: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC_REST"+ numero +"','PREST_CONTAS_ADIANT_LOC"+ numero +"') ", False)
        
        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC_REST"+ numero +"','PREST_CONTAS_ADIANT_LOC_REST"+ numero +"') ")
        #--- crédito
        OrdemServico.AdicionaComentario("Procedure para Credito GL_2.2: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC_REST"+ numero +"','PREST_CONTAS_ADIANT_LOC_REST"+ numero +"') ", False)
        
        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC_REST"+ numero +"','PREST_CONTAS_ADIANT_LOC_REST"+ numero +"') ")

        

########Quando o valor total do Adiantamento for MENOR do que o valor da Prestação de Contas        
#if Convert.ToDecimal(valorAdiantamento) < Convert.ToDecimal(total_pestacao):
if temReembolso=='Sim' and temDevolucao == 'Não':
    #####Pelo registro contábil do valor total adiantado para o funcionário
    rubrica = '90303'
    fornecedor = '001.110001.3000001000.114201.000000.000.00000'
    
    conta = "001."+ filial +"."+ uor +"."+ prefixo + rubrica +".000000.000.00000"
    OrdemServico.SetCustom("NUM_DOCU", conta)
    valor = DB.ExecuteScalar("select replace('"+ valorAdiantamento.ToString() + "',',','.') as valor from dual")
    valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '999999D99') as valor from dual")
    valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")
        
    SQLcontInterfaceGL = "SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND REFERENCE1 LIKE '%PREST_CONTAS_ADIANT_LOC%'"
    
    #Utils.LogError("contInterfaceGL_3.1: " + SQLcontInterfaceGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
    
    contInterfaceGL = DB.ExecuteScalar(SQLcontInterfaceGL.ToString())
        
    SQLcontGL = "SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND NAME LIKE '%PREST_CONTAS_ADIANT_LOC%'"
    
    #Utils.LogError("SQLcontGL_3.1: " + SQLcontGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
    
    contGL = DB.ExecuteScalar(SQLcontGL.ToString())
    valordecimal = Convert.ToDecimal(valorAdiantamento)
    
    #----- insert no GL
    #--- débito
    if contInterfaceGL.ToString()=='0' and contGL.ToString()=='0' and valor.ToString() !='0' and valordecimal > 0:
        OrdemServico.AdicionaComentario("Procedure para débito GL_3.1: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC"+ numero +"','PREST_CONTAS_ADIANT_LOC"+ numero +"') ", False)
        
        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC"+ numero +"','PREST_CONTAS_ADIANT_LOC"+ numero +"') ")
        #--- crédito
        OrdemServico.AdicionaComentario("Procedure para Credito GL_3.1: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC"+ numero +"','PREST_CONTAS_ADIANT_LOC"+ numero +"') ", False)
        
        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC"+ numero +"','PREST_CONTAS_ADIANT_LOC"+ numero +"') ")


        
    #####Pelo registro contábil do valor da diferença de locomoção a ser reembolsado para o funcionário
    #valorReembolso = Convert.ToDecimal(total_pestacao) - Convert.ToDecimal(valorAdiantamento)
    valorReembolso = OrdemServico.GetCustom("VALOR_DOD")
    rubrica = '90303'
    fornecedor = '001.110001.3000001000.219399.000000.000.00000'
    
    conta = "001."+ filial +"."+ uor +"."+ prefixo + rubrica +".000000.000.00000"
    OrdemServico.SetCustom("NUM_DOCU", conta)
    valor = DB.ExecuteScalar("select replace('"+ valorReembolso.ToString() + "',',','.') as valor from dual")
    valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '999999D99') as valor from dual")
    valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")
    
    SQLcontInterfaceGL = "SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND REFERENCE1 LIKE '%PREST_CONTAS_ADIANT_LOC_REEMBOLSO%'"
    
    #Utils.LogError("SQLcontInterfaceGL_3.2: " + SQLcontInterfaceGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
    
    contInterfaceGL = DB.ExecuteScalar(SQLcontInterfaceGL.ToString())
    
    SQLcontGL = "SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString()+"%'"
    
    #Utils.LogError("SQLcontGL: " + SQLcontGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
        
    contGL = DB.ExecuteScalar(SQLcontGL.ToString())
    valordecimal = Convert.ToDecimal(valorReembolso)
    
    
    #----- insert no GL
    #--- débito
    if contInterfaceGL.ToString()=='0' and contGL.ToString()=='0' and valor.ToString() !='0' and valordecimal > 0:
        
        OrdemServico.AdicionaComentario("Procedure para débito GL_4: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC_REEMBOLSO"+ numero +"','PREST_CONTAS_ADIANT_LOC_REEMBOLSO"+ numero +"') ", False)
        
        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC_REEMBOLSO"+ numero +"','PREST_CONTAS_ADIANT_LOC_REEMBOLSO"+ numero +"') ")
        #--- crédito
        OrdemServico.AdicionaComentario("Procedure para Credito GL_4: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC_REEMBOLSO"+ numero +"','PREST_CONTAS_ADIANT_LOC_REEMBOLSO"+ numero +"') ", False)
        
        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'PREST_CONTAS_ADIANT_LOC_REEMBOLSO"+ numero +"','PREST_CONTAS_ADIANT_LOC_REEMBOLSO"+ numero +"') ")
        
    #----- insert no AP
    
    SQLcontInterfaceGL = "SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND REFERENCE1 LIKE '%PREST_CONTAS_ADIANT_LOC_REEMBOLSO%'"
    
    #Utils.LogError("contInterfaceGL_4: " + SQLcontInterfaceGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
    
    contInterfaceGL = DB.ExecuteScalar(SQLcontInterfaceGL.ToString())
    
    SQLcontGL = "SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND NAME LIKE '%PREST_CONTAS_ADIANT_LOC_REEMBOLSO%'"
    
    #Utils.LogError("contInterfaceGL_4: " + SQLcontGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
        
    contGL = DB.ExecuteScalar(SQLcontGL.ToString())
    
    contInterfaceAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERIDAS from XXBBTSGATE.VW_BBTS_AP_INVOICES_INTERFACE where source LIKE '%SUPRAVIZIO%' AND invoice_num = '"+nota+""+OrdemServico.Numero.ToString() + "'")

    contAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERIDAS from AP_INVOICES_ALL where source LIKE '%SUPRAVIZIO%' AND invoice_num = '"+nota+""+OrdemServico.Numero.ToString() + "'")   
    #----- insert no AP
    if contInterfaceAP.ToString()=='0' and contAP.ToString()=='0' and valor.ToString() !='0' and valordecimal > 0:

        if (contInterfaceGL.ToString()>= '2' or contGL.ToString()>= '2'):

            OrdemServico.AdicionaComentario("Procedure AP_4: call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota.ToString() +""+ numero.ToString() + "', SYSDATE+1, '"+ matricula.ToString() +"', "+valor.ToString() +", '"+ fornecedor.ToString() +"', '"+ termo.ToString() +"','"+ fornecedor_passivo +"')", False)
            
            DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota.ToString() +""+ numero.ToString() + "', SYSDATE+1, '"+ matricula.ToString() +"', "+valor.ToString() +", '"+ fornecedor.ToString() +"', '"+ termo.ToString() +"','"+ fornecedor_passivo +"') ")



######PRESTRAÇÃO DE CONTAS LOCOMOÇÕES CONTRATADAS PELA VOETUR
if (total_passag_contr != None and total_passag_contr.ToString() != '0' and total_passag_contr.ToString() != '') or (total_hosp_contr != None and total_hosp_contr.ToString() != '0' and total_hosp_contr.ToString() != '') or (total_carro_loc != None and total_carro_loc.ToString() != '0' and total_carro_loc.ToString() != ''):
    nota = 'RDV'
    
    if total_passag_contr != None and total_passag_contr != '0' and total_passag_contr != '':
        rubrica = '90301'
        fornecedor = '001.110001.3000001000.21219902.000000.000.00000'
        
        conta = "001."+ filial +"."+ uor +"."+ prefixo + rubrica +".000000.000.00000"
        OrdemServico.SetCustom("NUM_DOCU", conta)
        valor = DB.ExecuteScalar("select replace('"+ total_passag_contr.ToString() + "',',','.') as valor from dual")
        valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '999999D99') as valor from dual")
        valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")
        
        SQLcontInterfaceGL = "SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND REFERENCE1 LIKE '%PASSAGEM_CONTRATADA%'"
        
        #Utils.LogError("SQLcontInterfaceGL_5: " + SQLcontInterfaceGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
        
        contInterfaceGL = DB.ExecuteScalar(SQLcontInterfaceGL.ToString())
        
        SQLcontGL = "SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND NAME LIKE '%PASSAGEM_CONTRATADA%'"
        
        #Utils.LogError("SQLcontGL_5: " + SQLcontGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
        
        contGL = DB.ExecuteScalar(SQLcontGL)
        valordecimal = Convert.ToDecimal(total_passag_contr)

        #----- insert no GL
        #--- débito
        if contInterfaceGL.ToString()=='0' and contGL.ToString()=='0' and valor.ToString().Trim() != '.00' and valor.ToString() !='0' and valordecimal > 0:
            OrdemServico.AdicionaComentario("Procedure para débito GL_5: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'PASSAGEM_CONTRATADA"+ numero +"','PASSAGEM_CONTRATADA"+ numero +"') ", False)
            
            DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'PASSAGEM_CONTRATADA"+ numero +"','PASSAGEM_CONTRATADA"+ numero +"') ")
            #--- crédito
            OrdemServico.AdicionaComentario("Procedure para Credito GL_5: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'PASSAGEM_CONTRATADA"+ numero +"','PASSAGEM_CONTRATADA"+ numero +"') ", False)
            DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'PASSAGEM_CONTRATADA"+ numero +"','PASSAGEM_CONTRATADA"+ numero +"') ")
        
    if total_hosp_contr != None and total_hosp_contr != '0' and total_hosp_contr != '':
        rubrica = '90302'
        fornecedor = '001.110001.3000001000.21219902.000000.000.00000'
        
        conta = "001."+ filial +"."+ uor +"."+ prefixo + rubrica +".000000.000.00000"
        OrdemServico.SetCustom("NUM_DOCU", conta)
        valor = DB.ExecuteScalar("select replace('"+ total_hosp_contr.ToString() + "',',','.') as valor from dual")
        valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '999999D99') as valor from dual")
        valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")
        
        SQLcontInterfaceGL = "SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND REFERENCE1 LIKE '%HOSPED_CONTRATADA%'"
        
        #Utils.LogError("SQLcontInterfaceGL_5.2: " + SQLcontInterfaceGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
            
        contInterfaceGL = DB.ExecuteScalar(SQLcontInterfaceGL.ToString())
        
        SQLcontGL = "SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND NAME LIKE '%HOSPED_CONTRATADA%'"
        
        #Utils.LogError("SQLcontGL_5.2: " + SQLcontGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
            
        contGL = DB.ExecuteScalar(SQLcontGL.ToString())
        valordecimal = Convert.ToDecimal(total_hosp_contr)

        #----- insert no GL
        #--- débito
        if contInterfaceGL.ToString()=='0' and contGL.ToString()=='0' and valor.ToString().Trim() != '.00' and valor.ToString() !='0' and valordecimal > 0:
            OrdemServico.AdicionaComentario("Procedure para débito GL_5.2: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'HOSPED_CONTRATADA"+ numero +"','HOSPED_CONTRATADA"+ numero +"') ", False)
            
            DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'HOSPED_CONTRATADA"+ numero +"','HOSPED_CONTRATADA"+ numero +"') ")
            #--- crédito
            OrdemServico.AdicionaComentario("Procedure para Credito GL_5.2: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'HOSPED_CONTRATADA"+ numero +"','HOSPED_CONTRATADA"+ numero +"') ", False)
            DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'HOSPED_CONTRATADA"+ numero +"','HOSPED_CONTRATADA"+ numero +"') ")
        
    if total_carro_loc != None and total_carro_loc != '0' and total_carro_loc != '':
        rubrica = '90306'
        fornecedor = '001.110001.3000001000.21219902.000000.000.00000'
        
        conta = "001."+ filial +"."+ uor +"."+ prefixo + rubrica +".000000.000.00000"
        OrdemServico.SetCustom("NUM_DOCU", conta)
        valor = DB.ExecuteScalar("select replace('"+ total_carro_loc.ToString() + "',',','.') as valor from dual")
        valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '999999D99') as valor from dual")
        valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")
            
        SQLcontInterfaceGL = "SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND REFERENCE1 LIKE '%CARRO_LOCADO%'"
        
        #Utils.LogError("SQLcontInterfaceGL_5.3: " + SQLcontInterfaceGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
        
        contInterfaceGL = DB.ExecuteScalar(SQLcontInterfaceGL.ToString())
        
        SQLcontGL = "SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND NAME LIKE '%CARRO_LOCADO%'"
        
        #Utils.LogError("SQLcontGL_5.3: " + SQLcontGL.ToString(), "Debug " + OrdemServico.Numero.ToString())
            
        contGL = DB.ExecuteScalar(SQLcontGL.ToString())
        valordecimal = Convert.ToDecimal(total_carro_loc)

        #----- insert no GL
        #--- débito
        if contInterfaceGL.ToString()=='0' and contGL.ToString()=='0' and valor.ToString().Trim() != '.00' and valor.ToString() !='0' and valordecimal > 0:
            OrdemServico.AdicionaComentario("Procedure para débito GL_5.3: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'CARRO_LOCADO"+ numero +"','CARRO_LOCADO"+ numero +"') ", False)
            
            DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'CARRO_LOCADO"+ numero +"','CARRO_LOCADO"+ numero +"') ")
            #--- crédito
            OrdemServico.AdicionaComentario("Procedure para Credito GL_5.3: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'CARRO_LOCADO"+ numero +"','CARRO_LOCADO"+ numero +"') ", False)
            DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'CARRO_LOCADO"+ numero +"','CARRO_LOCADO"+ numero +"') ")
######FIM PRESTRAÇÃO DE CONTAS LOCOMOÇÕES CONTRATADAS PELA VOETUR

OrdemServico.Salva()
AvancaProximaAtividade = True

        
######Quando do REEMBOLSO do valor da locomoção de DEMAIS DESPESAS realizado na Prestação de Contas 
#if total_demaisDesp.ToString() != '0':
#    rubrica = '90303'
#    fornecedor = '001.110001.3000001000.219399.000000.000.00000'
#    
#    conta = "001."+ filial +"."+ uor +"."+ prefixo + rubrica +".000000.000.00000"
#    OrdemServico.SetCustom("NUM_DOCU", conta)
#    valor = DB.ExecuteScalar("select replace('"+ total_demaisDesp.ToString() + "',',','.') as valor from dual")
#    valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '9999D99') as valor from dual")
#    valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")
#    
#    contInterfaceGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND REFERENCE1 LIKE '%PREST_CONTAS_LOC_DEMAIS_DESP%'")
#        
#    contGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND NAME LIKE '%PREST_CONTAS_LOC_DEMAIS_DESP%'")
#    
#    contInterfaceAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERIDAS from XXBBTSGATE.VW_BBTS_AP_INVOICES_INTERFACE where source LIKE '%SUPRAVIZIO%' AND invoice_num = '"+nota+""+OrdemServico.Numero.ToString() + "'")
#
#    contAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERIDAS from AP_INVOICES_ALL where source LIKE '%SUPRAVIZIO%' AND invoice_num = '"+nota+""+OrdemServico.Numero.ToString() + "'")
#    
#    
#    
#    #----- insert no GL
#    #--- débito
#    if contInterfaceGL.ToString()=='0' and contGL.ToString()=='0':
#        
#        OrdemServico.AdicionaComentario("Procedure para débito GL: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Lançamentos', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'PREST_CONTAS_LOC_DEMAIS_DESP"+ numero +"','PREST_CONTAS_LOC_DEMAIS_DESP"+ numero +"') ", False)
#        
#        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Lançamentos', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'PREST_CONTAS_LOC_DEMAIS_DESP"+ numero +"','PREST_CONTAS_LOC_DEMAIS_DESP"+ numero +"') ")
#        #--- crédito
#        OrdemServico.AdicionaComentario("Procedure para Credito GL: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Lançamentos', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'PREST_CONTAS_LOC_DEMAIS_DESP"+ numero +"','PREST_CONTAS_LOC_DEMAIS_DESP"+ numero +"') ", False)
#        
#        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Lançamentos', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'PREST_CONTAS_LOC_DEMAIS_DESP"+ numero +"','PREST_CONTAS_LOC_DEMAIS_DESP"+ numero +"') ")
#        
#    #----- insert no AP
#    contInterfaceGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND REFERENCE1 LIKE '%PREST_CONTAS_LOC_DEMAIS_DESP%'")
#        
#    contGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND NAME LIKE '%PREST_CONTAS_LOC_DEMAIS_DESP%'")
#
#    if contInterfaceAP.ToString() == '0' and contAP.ToString() == '0' and (contInterfaceGL.ToString()>= '2' or contGL.ToString()>= '2'):
#
#        OrdemServico.AdicionaComentario("Procedure AP: call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota.ToString() +""+ numero.ToString() + "', SYSDATE+1, '"+ matricula.ToString() +"', "+valor.ToString() +", '"+ fornecedor.ToString() +"', '"+ termo.ToString() +"')", False)
#        
#        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota.ToString() +""+ numero.ToString() + "', SYSDATE+1, '"+ matricula.ToString() +"', "+valor.ToString() +", '"+ fornecedor.ToString() +"', '"+ termo.ToString() +"') ")
```

### [347987] EventoIntermediarioTimer ""
Config: TempoIntervalo=1440

### [347988] EventoIntermediarioTimer ""
Config: TempoIntervalo=2880

### [347989] LinkInicial ""
Responsável: Cliente (papel 18)
Config: TipoMensagem=MensagemProcesso
**ScriptInicio**
```python
Formulario["VALOR_DESPESAS"].Habilitado = True
```
**ScriptFormCarregado**
```python
Formulario["NOME_PROJETO"].Habilitado = False
Formulario["NOME_PROJETO"].Visivel = False

Formulario["STRING_ERP"].Habilitado = False
Formulario["STRING_ERP"].Visivel = False

Formulario["VALOR_DOD"].Habilitado = False
Formulario["VALOR_DOD"].Visivel = False

Formulario["VALORTOTALPB"].Habilitado = False
Formulario["VALORTOTALPB"].Visivel = False

Formulario["VALOR_TOT_PREST_CONTAS"].Habilitado = False
Formulario["VALORTOTSEMCOMPROV"].Habilitado = False

Formulario["VALOR_TOT_PREST_CONTAS"].Visivel = False
Formulario["VALORTOTSEMCOMPROV"].Visivel = False

Formulario["VALOR_DESPESAS"].Habilitado = True

AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações do Deslocamento
  - VALOR_DIARIA "Valor da Diaria R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DIARIA]
**VALOR_DIARIA.ScriptModificado**
```python
#if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
#         Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = Formulario["VALOR_DIARIA"].Valor
#    
#
#
#
#if Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "PRESIDENTE": 
#     Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = Formulario["VALOR_DIARIA"].Valor
#
#
#     
#     
#if Convert.ToDecimal(Formulario["VALOR_DIARIA"].Valor) >= Convert.ToDecimal(Formulario["CAMPO_VALIDACAO_DIARIA"].Valor):
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["CAMPO_VALIDACAO_DIARIA"].Valor
#else:
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
#    
#    
#Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
#Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
#Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
#Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
#Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
#
#valorTotal = 0
#
#quantDiaria = Convert.ToDecimal(Formulario["QUANTIDADE_DIARIA"].Valor)
#valorDiaria = Convert.ToDecimal(Formulario["VALOR_DIARIA_AUTORIZADO"].Valor)
#
#valorTotal = quantDiaria * valorDiaria 
#
#Formulario["VALOR_TOTAL_DIARIA"].Valor =  valorTotal 
#
#
#OrdemServico["VALOR_TOTAL_DIARIA"] = valorTotal
#
```
  - TIPO_DESTINO "Tipo da localidade de destino" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESTINO] — Coluna=4
  - RETORNO_HORA "Horário do Retorno" [TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA] — Coluna=3; Configuracao={"Mascara":"00:00"}
**RETORNO_HORA.ScriptModificado**
```python
#import clr 
#import datetime
#
#data1 = ""
#data2 = ""
#
#data1 = Formulario["SAIDA"].Valor
#data2 = Formulario["RETORNO_DIA"].Valor
# 
#delta = data2 - data1
#diferenca = delta.Days
#
#Formulario["DIAS_DE_TRA"].Valor = diferenca
#Formulario["DIAS_DE_TRA"].Habilitado = False
#
```
  - DIAS_DE_TRA "Dias em Deslocamento" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA]
  - TIPO_HOSPEDAGEM "Tipo de Hospedagem" [DropDownList String → CPE_DESLOCAMENTO.TIPO_HOSPEDAGEM]
**TIPO_HOSPEDAGEM.ScriptModificado**
```python
#if Formulario["TIPO_HOSPEDAGEM"].Valor == "Sem Hospedagem":
#    Formulario["QUANTIDADE_DIARIA"].Visivel = False
#    Formulario["QUANTIDADE_DIARIA"].Habilitado = False
#    Formulario["VALOR_DIARIA"].Visivel = False
#    Formulario["VALOR_DIARIA"].Habilitado = False
#    Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
#    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
#    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
#    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
#    Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
#    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
#    Formulario["PARCELA_COMPLEMENTAR"].Visivel = False
#    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False
#    Formulario["TOTAL_COMPLEMENTAR"].Visivel = False
#    Formulario["TOTAL_COMPLEMENTAR"].Habilitado = False    
#    Formulario["TOTAL_COMPLEMENTAR"].Valor = "0" 
#    Formulario["PAHL_HOSPEDAGENS"].Visivel = False
#    Formulario["PAHL_HOSPEDAGENS"].Habilitado = False        
#    
#    
#if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
#    Formulario["QUANTIDADE_DIARIA"].Visivel = True
#    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA"].Visivel = True
#    Formulario["VALOR_DIARIA"].Habilitado = True
#    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
#    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
#    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
#    Formulario["PAHL_HOSPEDAGENS"].Visivel = True
#    Formulario["PAHL_HOSPEDAGENS"].Habilitado = True
#    
##if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional"):
##    Formulario["QUANTIDADE_DIARIA"].Visivel = True
##    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
##    Formulario["VALOR_DIARIA"].Visivel = True
##    Formulario["VALOR_DIARIA"].Habilitado = True
##    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
##    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
##    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
##    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
##    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
##    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
##    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
##    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
##    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
##    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
##    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
##    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False    
#    
#
##if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional"):
##    Formulario["QUANTIDADE_DIARIA"].Visivel = False
##    Formulario["QUANTIDADE_DIARIA"].Habilitado = False
##    Formulario["VALOR_DIARIA"].Visivel = False
##    Formulario["VALOR_DIARIA"].Habilitado = False
##    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
##    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
##    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
##    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
##    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
##    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
##    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
##    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
##    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
##    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
##    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = True
##    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
```
  - QUANTIDADE_DIARIA "Quantidade de Diárias" [TextBox Integer → CPE_DESLOCAMENTO.QUANTIDADE_DIARIA]
**QUANTIDADE_DIARIA.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import OutputSubProcesso
#
#def calculaDiaria():
#    ############### SE O FAVORECIDO FOR DO GRUPO C MAS ESTARÁ ACOMPANHANDO O GRUPO B RECEBE O VALOR DO GRUPO B 
#    
#    if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
#            Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
#    
#    elif Formulario["SIM_NAO"].Valor == "Sim" :
#          if Formulario["CIDADE_DESTINO"].Valor == "3550308": # SAO PAULO 
#                 Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "650"
#                
#          elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO E BRASILIA
#            Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550"
#            
#          elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
#              Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450" 
#      
#    else:     
#            
#        ############## SE FOR DO GRUPO A -  PRESIDENTE / DIRETOR / CONSELHEIRO NÃO TEM LIMITE   
#        if Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "PRESIDENTE":
#            Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
#            
#            
#            
#        ############## SE O FAVORECIDO FOR DO GRUPO B  ELE RECEBE REFERENTE A CIDADE     
#        elif Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "GERENTE EXECUTIVO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE DE PROJETOS I" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "ASSESSOR EXEC DA PRESIDENCIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "SUPERINTENDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "SUPERINTENDENTE":
#            if Formulario["CIDADE_DESTINO"].Valor == "3550308 ": # SAO PAULO 
#                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "650"
#                    
#            elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO OutputSubProcesso BRASILIA
#                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550"
#                    
#            elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or      Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
#                      Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450" 
#            else:
#                Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
#                  
#                  
#        ############## DEMAIS CARGOS
#        elif Formulario["FUNCAO_DESLOCAMENTO"].Valor != "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "PRESIDENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE DE PROJETOS I" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "ASSESSOR EXEC DA PRESIDENCIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "SUPERINTENDENTE":
#              
#              if Formulario["CIDADE_DESTINO"].Valor == "3550308": # SAO PAULO 3550308 
#                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550" 
#                    
#              elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO ou BRASILIA
#                        Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
#                        
#              elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or      Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
#                          Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "370" 
#                          
#              else:
#                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "350"
#                  
#
#              
#              
#calculaDiaria()
#     
############# VALOR FINAL DO ADIANTAMENTO EM DIARIAS      
#diasViagem = Convert.ToInt32(Formulario["DIAS_DE_TRA"].Valor)
#diasHospedagem = Convert.ToInt32(Formulario["QUANTIDADE_DIARIA"].Valor)
#
#
#
#if diasHospedagem > diasViagem:
#    mensagem = "Quantidade de Diária Excedida! Máximo Permitido: " + Formulario["DIAS_DE_TRA"].Valor + " Verifique a saída e o retorno"
#    Formulario.ExibeMensagem(mensagem)      
#    Formulario["VALOR_DIARIA"].Habilitado = False
#else:
#    Formulario["VALOR_DIARIA"].Habilitado = True   
#
#
##Valor parcela complementar    
#if Formulario["QUANTIDADE_DIARIA"] != "0":
#    Formulario["PARCELA_COMPLEMENTAR"].Valor = "17,90"
#    Formulario["PARCELA_COMPLEMENTAR"].Visivel = True
#    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False    
#    
#    pc = Formulario["PARCELA_COMPLEMENTAR"].Valor
#    qtd = Formulario["QUANTIDADE_DIARIA"].Valor
#    total = 0
#
#    total = pc * qtd
#
#    Formulario["TOTAL_COMPLEMENTAR"].Valor = total
#    Formulario["TOTAL_COMPLEMENTAR"].Visivel = True
#    
##if (Formulario["TIPO_DESTINO"].Valor == "Interior") and (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa"):
##    Formulario["VALOR_DIARIA"].Valor = "350"
##    
##if (Formulario["TIPO_DESTINO"].Valor == "Capital") and (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa"):
##    Formulario["VALOR_DIARIA"].Valor = "500"
##
##import System.Text
##daysOffText = System.Text.StringBuilder()
##
## #RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
##def isHoliday(day):
##    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C  inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
##   
##    for holiday in holidays.Rows:
##        if day == holiday["DATA"].Date:
##            return True
##    return False
##   
##def workingDays(totalDays, firstDate):
##    
##    totalWorkingDays = 0
##    totalDaysOff = 0
##    count = 0
##   
##    while count <= totalDays:
##        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
##        day = firstDate.Date.AddDays(count)
##        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
##            totalDaysOff = totalDaysOff + 1
##            daysOffText.AppendLine(" dayOff: "+str(day))
##        
##        count = count + 1
##        totalWorkingDays = totalWorkingDays + 1
##    return totalWorkingDays - totalDaysOff
##   
##
##saida = Formulario["SAIDA"].Valor
##retorno  = Formulario["RETORNO_DIA"].Valor
##
##totalDias = (retorno - saida).TotalDays  
##count = 0
##
##totalDiasUteis = workingDays(totalDias,saida) 
##totalDiasNaoUteis = totalDias - totalDiasUteis
##
################ almoço e janta de ambos os dias
##quantReduzida = totalDiasUteis  
##quantIntegral = (totalDiasNaoUteis * 2) + totalDiasUteis
##
##
##
#
##Formulario["QTD_REFEICAO_REDUZIDA"].Valor = totalDiasUteis 
##Formulario["QTD_REFEICAO_INTEGRAL"].Valor = totalDiasNaoUteis
##
##
##Formulario["VALOR_REF_REDUZIDA"].Valor = totalDiasUteis * 18.39
##Formulario["VALOR_REF_INTEGRAL"].Valor = totalDiasNaoUteis *  64.36
##
##
##OrdemServico.AdicionaComentario("WorkingDays "+totalWorkingDays.ToString(),False)
##OrdemServico.AdicionaComentario(daysOffText.ToString(),False )
#
##OrdemServico["totalWorkingDays"] = totalWorkingDays    
#    
#    
#    
#
```
  - VALOR_DIARIA_AUTORIZADO "Valor Diária Autorizado" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_AUTORIZADO] — Coluna=2
  - CAMPO_VALIDACAO_DIARIA "Diária máxima autorizada R$ (TAB320-001)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DIARIA]
  - VALOR_TOTAL_DIARIA "Valor Total Diária:" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_DIARIA]
  - ACOMPANHANDO_GRUPO_A "Estará acompanhando Presidente / Diretor / Conselheiro " [DropDownList String → CPE_DESLOCAMENTO.ACOMPANHANDO_GRUPO_A]
**ACOMPANHANDO_GRUPO_A.ScriptModificado**
```python
#if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
#    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True 
#    Formulario["NUM_ABERTURA_CHAMADO"].Habilitado = True 
#    Formulario["SIM_NAO"].Visivel = False
#    Formulario["SIM_NAO"].Habilitado = False 
#  
#
#else:
#    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False 
#    Formulario["SIM_NAO"].Visivel = True
#    Formulario["SIM_NAO"].Habilitado = True
     
    
    
#    
#if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Não":
#    Formulario["SIM_NAO"].Visivel = True
#    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True 
#    Formulario["NUM_ABERTURA_CHAMADO"].Habilitado = True 
#
#else:
#     Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
#
```
  - SIM_NAO "Estará acompanhado Gerente Executivo / Gerente de Projeto I / Assesor Executivo / Superintendente?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO]
**SIM_NAO.ScriptModificado**
```python
#if Formulario["SIM_NAO"].Valor == "Sim":
#    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True
#else:
#    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
```
  - VALOR_DIARIA_DOLAR "Valor Diária US$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_DOLAR]
**VALOR_DIARIA_DOLAR.ScriptModificado**
```python
#if Convert.ToDecimal(Formulario["VALOR_DIARIA_DOLAR"].Valor) >= Convert.ToDecimal(Formulario["CAMPO_VALIDACAO_DOLAR"].Valor):
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = Formulario["CAMPO_VALIDACAO_DOLAR"].Valor
#else:
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = Formulario["VALOR_DIARIA_DOLAR"].Valor
#    
#    
#Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
#Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
#Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
#Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
#Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
#
#valorTotal1 = 0
#
#quantDiaria = Convert.ToDecimal(Formulario["QUANTIDADE_DIARIA"].Valor)
#valorDiaria = Convert.ToDecimal(Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor)
#
#valorTotal1 = quantDiaria * valorDiaria 
#
#Formulario["VALOR_TOTAL_DIARIA"].Valor =  valorTotal1 


#OrdemServico["VALOR_TOTAL_DIARIA"] = valorTotal1
```
  - CAMPO_VALIDACAO_DOLAR "Diária máxima autorizada US$ (TAB320-001)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DOLAR] — Coluna=2
  - DIARIA_AUTORIZADO_INTERNACIONAL "Valor Diária Autorizado US$" [TextBox String → CPE_DESLOCAMENTO.DIARIA_AUTORIZADO_INTERNACIONAL] — Coluna=3
  - COTACAO_DOLAR "Cotação do Dólar americano (USD) " [TextBox String → CPE_DESLOCAMENTO.COTACAO_DOLAR]
**COTACAO_DOLAR.ScriptModificado**
```python
#import System
#
#valorTotal = 0
#
#
#valorTotal = Formulario["VALOR_TOTAL_DIARIA"].Valor * Convert.ToDecimal(Formulario["COTACAO_DOLAR"].Valor)
#
#
#Convert.ToDecimal(Formulario["DIARIA_COTACAO_REAL"].Valor) = valorTotal

#
#valorTotal = 0
#vtd = Formulario["VALOR_TOTAL_DIARIA"].Valor
#cd = Convert.ToDecimal(Formulario["COTACAO_DOLAR"].Valor)
#
#valorTotal = vtd * cd
#
#Formulario["DIARIA_COTACAO_REAL"].Valor = valorTotal
#



#valorTotal = 0
#
#
#valorTotal = Formulario["VALOR_TOTAL_DIARIA"].Valor * (Formulario["COTACAO_DOLAR"].Valor)
#
#
#Formulario["DIARIA_COTACAO_REAL"].Valor = valorTotal
#

#diariaReal = ""
#cotacao = ""
#valorTotal = ""
#
#diariaReal = Convert.ToDouble(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#cotacao = Convert.ToDouble(Formulario["COTACAO_DOLAR"].Valor)
```
  - DIARIA_COTACAO_REAL "Diária em Real" [TextBox String → CPE_DESLOCAMENTO.DIARIA_COTACAO_REAL] — Coluna=2
  - PARCELA_COMPLEMENTAR "Parcela Complementar de hospedagem" [TextBox Decimal → CPE_DESLOCAMENTO.PARCELA_COMPLEMENTAR]
  - TOTAL_COMPLEMENTAR "Total Parcela Complementar (Não é necessário prestar contas)" [TextBox Decimal → CPE_DESLOCAMENTO.TOTAL_COMPLEMENTAR]
  - SAIDA_HORA "Horário da Saída" [TextBox String → CPE_DESLOCAMENTO.SAIDA_HORA] — Configuracao={"Mascara":"00:00"}
  - LISTA_INVIABILIDADE "Lista de Motivos que inviabilizam a videoconferência" [DropDownList String → CPE_DESLOCAMENTO.LISTA_INVIABILIDADE]
  - OBJETIVO_VIAGEM "Objetivo / Informações Adicionais:" [TextBox String → CPE_DESLOCAMENTO.OBJETIVO_VIAGEM]
  - MEIO_LOCOMOCAO "Meio de locomoção principal" [DropDownList String → CPE_DESLOCAMENTO.MEIO_LOCOMOCAO]
**MEIO_LOCOMOCAO.ScriptModificado**
```python
#if Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Próprio":
#    Formulario["PREVISAO_DISTANCIA_KM"].Visivel = True
#    Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = True
#    Formulario["VALOR_DISTANCIA"].Visivel = True
#    Formulario["VALOR_DISTANCIA"].Habilitado = True
#else:
#    Formulario["PREVISAO_DISTANCIA_KM"].Visivel = False
#    Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = False
#    Formulario["VALOR_DISTANCIA"].Visivel = False
#    Formulario["VALOR_DISTANCIA"].Habilitado = False
    
    
    
##if Formulario["MEIO_LOCOMOCAO"].Valor == "Avião" or Formulario["MEIO_LOCOMOCAO"] == "Ônibus Interestadual":
##    Formulario["VALOR_PASSAGEM"].Visivel = True
##    Formulario["VALOR_PASSAGEM"].Habilitado = True
##    Formulario["VALIDADE_PASSAGEM"].Visivel = True
##    Formulario["VALIDADE_PASSAGEM"].Habilitado = True
##    Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = True
##    Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = True
##else:
##    Formulario["VALOR_PASSAGEM"].Visivel = False
##    Formulario["VALOR_PASSAGEM"].Habilitado = False
##    Formulario["VALIDADE_PASSAGEM"].Visivel = False
##    Formulario["VALIDADE_PASSAGEM"].Habilitado = False
##    Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = False
##    Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = False    
#    
    






##finais de semana um almoço e janta integral
##dias de semana uma refeição reduzida e uma integral
############# calculo dias
import clr 
import datetime
import System.Text
 

##finais de semana um almoço e janta integral
##dias de semana uma refeição reduzida e uma integral

valorRefIntegral = 64.36
valorRefReduzida = 18.39



daysOffText = System.Text.StringBuilder()


##RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
def isHoliday(day):
    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C  inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
    #feriados = 0
    
    for holiday in holidays.Rows:
        if day == holiday["DATA"].Date:
            #feriados += 2
            return True
    return False


def countHolidays(firstDate, lastDate):
    totalHolidays = 0
    currentDay = firstDate

    while currentDay <= lastDate:
        if isHoliday(currentDay):
            totalHolidays += 1
        currentDay = currentDay.AddDays(1)

    return totalHolidays

    
def workingDays(totalDays, firstDate):

    totalWorkingDays = 0
    totalDaysOff = 0
    count = 0

   
    while count <= totalDays:
        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
        day = firstDate.Date.AddDays(count)
        
        
        
        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
            totalDaysOff = totalDaysOff + 1
            daysOffText.AppendLine(" dayOff: "+str(day))
        
        count = count + 1
        totalWorkingDays = totalWorkingDays + 1
    return totalWorkingDays - totalDaysOff
   


    
def countSaturdays(firstDate, lastDate):
    saturdays = 0
    currentDay = firstDate
    
    while currentDay <= lastDate:
        if (currentDay.DayOfWeek == DayOfWeek.Sunday or currentDay.DayOfWeek == DayOfWeek.Saturday):
            saturdays += 2
        currentDay = currentDay.AddDays(1)  # Avance para o próximo dia
    
    return saturdays

    
firstDate = Formulario["SAIDA"].Valor
lastDate   = Formulario["RETORNO_DIA"].Valor

totalDays = (lastDate - firstDate).TotalDays
count = 0





totalWorkingDays = workingDays(totalDays,firstDate)
holidaysCount = countHolidays(firstDate, lastDate)
saturdays = countSaturdays(firstDate, lastDate) + holidaysCount * 2

quantRed = totalWorkingDays
quantInt = saturdays + totalWorkingDays 








saidaHora = Formulario["SAIDA_HORA"].Valor
retornoHora = Formulario["RETORNO_HORA"].Valor

hora = saidaHora.Split(':');
horaRetorno = retornoHora.Split(':');

horarioSaida = hora[0]
minutoSaida = hora[1]

horarioRetorno = horaRetorno[0] 
minutoRetorno = horaRetorno[1]



#SAIDA DIAS ÚTEIS


#1 maior q o 2
#if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) >= 13 and Convert.ToInt32(horarioSaida) < 21):
#    quantRed = quantRed - 1
#   
#if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) > 21):
#    quantInt = quantInt - 1
#   
#RETORNO DIAS ÚTEIS
#1 menor q o 2   
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 13:
#    quantRed = quantRed - 1
#    quantInt = quantInt - 1
#    
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 19 and Convert.ToInt32(horarioRetorno) > 13:
#    quantInt = quantInt - 1
#    #teste abaixo
#    quantRed = quantRed - 1





if workingDays(0,firstDate):
    if (Convert.ToInt32(horarioSaida) >= 13 and Convert.ToInt32(horarioSaida) < 21):
        quantRed = quantRed - 1
    if (Convert.ToInt32(horarioSaida) > 21):
        quantInt = quantInt - 1
        quantRed = quantRed - 1
    
    if (Convert.ToInt32(horarioRetorno) <= 13):
        quantRed = quantRed - 1
        quantInt = quantInt - 1
    if (Convert.ToInt32(horarioRetorno) <= 19 and Convert.ToInt32(horarioRetorno) > 13):
        quantInt = quantInt - 1
    
###############################################################
    
#SAÍDA FINAIS DE SEMANA E/OU FERIADOS

if not  workingDays(0,firstDate):
    if Convert.ToInt32(horarioSaida) > 13:
        quantInt = quantInt - 1
    if Convert.ToInt32(horarioSaida) > 21:
        quantInt = quantInt - 1
    if Convert.ToInt32(horarioRetorno) < 13:
        quantInt = quantInt - 2
    if Convert.ToInt32(horarioRetorno) < 19 and Convert.ToInt32(horarioRetorno) != 13:
        quantInt = quantInt - 1   


##Correção margem de erro do cálculo de refeições:
quantRed = quantRed - 1
quantInt = quantInt + 1
        
        
#str(Formulario["NUMERO_OC"].Valor) = str(quantRed)
#str(Formulario["NUMERO_DA_OC"].Valor) = str(quantInt)

Formulario["QTD_REFEICAO_REDUZIDA"].Valor = quantRed
Formulario["QTD_REFEICAO_INTEGRAL"].Valor = quantInt
  
##totalIntegrais = integrais + totalWorkingDays

##Formulario["QTD_REFEICAO_REDUZIDA"].Valor = totalWorkingDays
##Formulario["QTD_REFEICAO_INTEGRAL"].Valor = saturdays + totalWorkingDays



############## calculo valor total
 
refIntegral = Formulario["QTD_REFEICAO_INTEGRAL"].Valor * valorRefIntegral
refReduzida = Formulario["QTD_REFEICAO_REDUZIDA"].Valor * valorRefReduzida
valorTotalRefeicoes = refIntegral + refReduzida
Formulario["VALOR_TOTAL_REFEICAO"].Valor  = valorTotalRefeicoes
```
  - PREVISAO_DISTANCIA_KM "Previsão de distancia em KM" [TextBox Decimal → CPE_DESLOCAMENTO.PREVISAO_DISTANCIA_KM]
**PREVISAO_DISTANCIA_KM.ScriptModificado**
```python
#import System
#
#
#Formulario["VALOR_DISTANCIA"].Habilitado = False
#
#valorTotal = 0
#
#distancia = Formulario["PREVISAO_DISTANCIA_KM"].Valor
#valorTotal = distancia * 1.30 
#
#
#Formulario["VALOR_DISTANCIA"].Valor = valorTotal
##OrdemServico["VALOR_DISTANCIA"] = valorTotal
#
```
  - VALOR_DISTANCIA "Valor previsto para percorrer distância R$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DISTANCIA] — Coluna=2
  - QTD_REFEICAO_REDUZIDA "Quantidade de refeições reduzidas" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_REDUZIDA]
**QTD_REFEICAO_REDUZIDA.ScriptModificado**
```python
#import clr 
#import datetime
#import System.Text
#
#daysOffText = System.Text.StringBuilder()
#
#quantRefeicaoReduzida = Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor)
#quantRefeicaoIntegral = Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor)
#
#valorRefIntegral = 64.36
#valorRefReduzida = 18.39
#Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
#
#def isHoliday(day):
#    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C  inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
#   
#    for holiday in holidays.Rows:
#        if day == holiday["DATA"].Date:
#            return True
#    return False
#
#
#    
#def workingDays(totalDays, firstDate):
#
#    totalWorkingDays = 0
#    totalDaysOff = 0
#    count = 0
#
#   
#    while count <= totalDays:
#        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
#        day = firstDate.Date.AddDays(count)
#        
#        
#        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
#            totalDaysOff = totalDaysOff + 1
#            daysOffText.AppendLine(" dayOff: "+str(day))
#        
#        count = count + 1
#        totalWorkingDays = totalWorkingDays + 1
#    return totalWorkingDays - totalDaysOff
#
#
#    
#firstDate = Formulario["SAIDA"].Valor
#lastDate   = Formulario["RETORNO_DIA"].Valor
#
#totalDays = (lastDate - firstDate).TotalDays
#count = 0
#
#
#saidaHora = Formulario["SAIDA_HORA"].Valor
#retornoHora = Formulario["RETORNO_HORA"].Valor
#
#hora = saidaHora.Split(':');
#horaRetorno = retornoHora.Split(':');
#
#horarioSaida = saidaHora[0]
#minutoSaida = saidaHora[1]
#
#horarioRetorno = horaRetorno[0] 
#minutoRetorno = horaRetorno[1]
#
#
#
#
#totalWorkingDays = workingDays(totalDays,firstDate)
#
##SAIDA E RETORNO DIAS ÚTEIS
#
##SAIDA DIAS ÚTEIS
#if workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) >=13 and Convert.ToInt32(horarioSaida) < 21:
#    quantRefeicaoReduzida = quantRefeicaoReduzida - 1
#    totalWorkingDays = totalWorkingDays - 1
#   
#if workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) > 21:
#    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
#    quantRefeicaoReduzida = quantRefeicaoReduzida - 1
#    totalWorkingDays = totalWorkingDays - 1
#   
#    
##RETORNO DIAS ÚTEIS   
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 13:
#    quantRefeicaoReduzida = quantRefeicaoReduzida - 1
#    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
#    totalWorkingDays = totalWorkingDays - 1
#    
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) < 19 and Convert.ToInt32(horarioRetorno) > 13:
#    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
#     
################################################################
#    
##SAÍDA FINAIS DE SEMANA E/OU FERIADOS    
#if not  workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) > 13:
#    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
#    
#if not  workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) > 21:
#    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
#
#    
#    
##RETORNO FINAIS DE SEMANA E/OU FERIADOS    
#if not  workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) < 13:
#    quantRefeicaoIntegral = quantRefeicaoIntegral - 2
#
#if not  workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) < 19 and Convert.ToInt32(horarioRetorno) != 13:
#    quantRefeicaoIntegral = quantRefeicaoIntegral - 1 
#
#
#totalWorkingDays = totalWorkingDays - 2    
#    
#if quantRefeicaoReduzida > (totalWorkingDays - 1):
#    mensagem = ("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + str(totalWorkingDays + 1) + " Verifique a Saída e o Retorno.")
#    Formulario.ExibeMensagem(mensagem)    
#    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
#    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
#        
#else:
#    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = True
#    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = True
#    refIntegral = Formulario["QTD_REFEICAO_INTEGRAL"].Valor * valorRefIntegral
#    refReduzida = Formulario["QTD_REFEICAO_REDUZIDA"].Valor * valorRefReduzida
#    valorTotalRefeicoes = refIntegral + refReduzida
#    Formulario["VALOR_TOTAL_REFEICAO"].Valor  = valorTotalRefeicoes
#    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
#    
#    
#
#
##Formulario["QTD_REFEICAO_REDUZIDA"].Valor = totalWorkingDays
##Formulario["QTD_REFEICAO_INTEGRAL"].Valor = saturdays + totalWorkingDays
#    
#    
#    
#    
#    
#    
#
```
  - VALOR_TOTAL_REFEICAO "Valor total previsto para refeições: R$" [TextBox String → CPE_ORDEM_SERVICO.VALOR_TOTAL_REFEICAO] — Coluna=2
  - VALOR_REF_REDUZIDA "Valor Refeição Reduzida" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_REDUZIDA]
  - QTD_REFEICAO_INTEGRAL "Quantidade de Refeições Integrais" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_INTEGRAL]
**QTD_REFEICAO_INTEGRAL.ScriptModificado**
```python
#import System
#import clr 
#import datetime
#import System.Text
#  
#
#Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
#
##valorTotal = 0
#valorRefIntegral = 64.36
#valorRefReduzida = 18.39
#
#
#
##valorTotal = quantRefeicaoIntegral + quantRefeicaoReduzida
#
##Formulario["VALOR_TOTAL_REFEICAO"].Valor = valorTotal 
##OrdemServico["VALOR_TOTAL_REFEICAO"] = valorTotal
#
#
#
#
#quantRefeicaoReduzida = Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor)
#quantRefeicaoIntegral = Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor)
#
#
#daysOffText = System.Text.StringBuilder()
#
#
##RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
#def isHoliday(day):
#    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C  inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
#    #feriados = 0
#    
#    for holiday in holidays.Rows:
#        if day == holiday["DATA"].Date:
#            #feriados += 2
#            return True
#    return False
#
#
#def countHolidays(firstDate, lastDate):
#    totalHolidays = 0
#    currentDay = firstDate
#
#    while currentDay <= lastDate:
#        if isHoliday(currentDay):
#            totalHolidays += 1
#        currentDay = currentDay.AddDays(1)
#
#    return totalHolidays
#
#    
#def workingDays(totalDays, firstDate):
#
#    totalWorkingDays = 0
#    totalDaysOff = 0
#    count = 0
#
#   
#    while count <= totalDays:
#        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
#        day = firstDate.Date.AddDays(count)
#        
#        
#        
#        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
#            totalDaysOff = totalDaysOff + 1
#            daysOffText.AppendLine(" dayOff: "+str(day))
#        
#        count = count + 1
#        totalWorkingDays = totalWorkingDays + 1
#    return totalWorkingDays - totalDaysOff
#   
#
#
#    
#def countSaturdays(firstDate, lastDate):
#    saturdays = 0
#    currentDay = firstDate
#    
#    while currentDay <= lastDate:
#        if (currentDay.DayOfWeek == DayOfWeek.Sunday or currentDay.DayOfWeek == DayOfWeek.Saturday):
#            saturdays += 2
#        currentDay = currentDay.AddDays(1)  # Avance para o próximo dia
#    
#    return saturdays
#
#    
#firstDate = Formulario["SAIDA"].Valor
#lastDate   = Formulario["RETORNO_DIA"].Valor
#
#totalDays = (lastDate - firstDate).TotalDays
#count = 0
#
#
#
#totalWorkingDays = workingDays(totalDays,firstDate)
#totalREF = workingDays(totalDays,firstDate)
#holidaysCount = countHolidays(firstDate, lastDate)
#saturdays = countSaturdays(firstDate, lastDate) + holidaysCount * 2
#
#refIntPermitidas = totalWorkingDays + saturdays
#
#
#
#saidaHora = Formulario["SAIDA_HORA"].Valor
#retornoHora = Formulario["RETORNO_HORA"].Valor
#
#hora = saidaHora.Split(':');
#horaRetorno = retornoHora.Split(':');
#
#horarioSaida = saidaHora[0]
#minutoSaida = saidaHora[1]
#
#horarioRetorno = horaRetorno[0] 
#minutoRetorno = horaRetorno[1]
#
#
#
#refeicoesFeriados = totalWorkingDays + saturdays
#
#
#
##SAIDA DIAS ÚTEIS
#if workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) >= 13 and Convert.ToInt32(horarioSaida) < 21:
#    quantRefeicaoReduzida = quantRefeicaoReduzida - 1
#    totalREF = totalREF - 1
#   
#if workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) > 21:
#    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
#    refeicoesFeriados = refeicoesFeriados - 1
#    quantRefeicaoReduzida = quantRefeicaoReduzida - 1
#    totalREF = totalREF - 1
#   
##RETORNO DIAS ÚTEIS   
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 13:
#    quantRefeicaoReduzida = quantRefeicaoReduzida - 1
#    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
#    totalREF = totalREF - 1
#    refeicoesFeriados = refeicoesFeriados - 1
#    
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 19 and Convert.ToInt32(horarioRetorno) > 13:
#    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
#    refeicoesFeriados = refeicoesFeriados - 1
#     
################################################################
#    
##SAÍDA FINAIS DE SEMANA E/OU FERIADOS    
#if not  workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) > 13:
#    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
#    refeicoesFeriados = refeicoesFeriados - 1
#    
#if not  workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) > 21:
#    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
#    refeicoesFeriados = refeicoesFeriados - 1
#
#    
#    
##RETORNO FINAIS DE SEMANA E/OU FERIADOS    
#if not  workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) < 13:
#    quantRefeicaoIntegral = quantRefeicaoIntegral - 2
#    refeicoesFeriados = refeicoesFeriados - 2
#
#if not  workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) < 19 and Convert.ToInt32(horarioRetorno) != 13:
#    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
#    refeicoesFeriados = refeicoesFeriados - 1
#    
#          
#
#refeicoesFeriados = refeicoesFeriados + 1
#
#
#calcula = refeicoesFeriados - 1
#    
#
#    
#if quantRefeicaoIntegral >= (calcula - 1):
#    mensagem = ("Quantidade de Refeições Integrais Excedida! Máximo permitido: " + str(calcula) + " Verifique a Saída e o Retorno.")
#    Formulario.ExibeMensagem(mensagem)
#    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False 
#
#else:
#    refIntegral = Formulario["QTD_REFEICAO_INTEGRAL"].Valor * valorRefIntegral
#    refReduzida = Formulario["QTD_REFEICAO_REDUZIDA"].Valor * valorRefReduzida
#    valorTotalRefeicoes = refIntegral + refReduzida
#    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
#    Formulario["VALOR_TOTAL_REFEICAO"].Valor  = valorTotalRefeicoes        
#
#    
##adjusted by: Fernando Cajango Dias
# 
#
```
  - VALOR_REF_INTEGRAL "Valor Refeição Integral" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_INTEGRAL]
  - DESCRICAO_DESPESAS "Descrição de outras despesas (Preencher com "NA" caso não tenha) " [TextBox String(1000) → CPE_DESLOCAMENTO.DESCRICAO_DESPESAS]
  - VALOR_DESPESAS "Valor de outras despesas R$ (preencher com "0" caso não tenha)" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DESPESAS] — Coluna=2
**VALOR_DESPESAS.ScriptModificado**
```python
#import System
#Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False
#
#if Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
#    
#    valorTotalAdiantamento = 0
#
#
#    totalDiaria = 0
#    ##valorAvicao = 0
#    outrasDespesas = 0
#    ##valorDistancia = 0
#    complementar = 0
#
#    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
#    totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#    ##valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
#    ##valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
#    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
#    
#
#    ##valorTotalAdiantamento =  totalDiaria + outrasDespesas + valorDistancia 
#    valorTotalAdiantamento = totalDiaria + outrasDespesas + complementar
#    
#    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = valorTotalAdiantamento
#    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False
#
#    ##OrdemServico["VALOR_TOTAL_ADIANTAMENTO"] = valorTotalAdiantamento
#
#elif (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
#    valorTotalAdiantamento = 0
#
#    valorTotalRefeicao = 0
#    totalDiaria = 0
#    #valorAvicao = 0
#    outrasDespesas = 0
#    valorDistancia = 0
#    complementar = 0
#
#    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
#    totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
#    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
#    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
#    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
#    
#
#    valorTotalAdiantamento = valorTotalRefeicao + totalDiaria + outrasDespesas + valorDistancia + complementar
#
#    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = valorTotalAdiantamento
#    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False
#
#    ##OrdemServico["VALOR_TOTAL_ADIANTAMENTO"] = valorTotalAdiantamento    
#else:
#    valorTotalAdiantamento = 0
#
#    valorTotalRefeicao = 0
#    #totalDiaria = 0
#    #valorAvicao = 0
#    outrasDespesas = 0
#    valorDistancia = 0
#    complementar = 0
#    
#    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
#    #totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
#    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
#    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
#    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
#    
#    valorTotalAdiantamento = valorTotalRefeicao + outrasDespesas + valorDistancia + complementar
#
#    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = valorTotalAdiantamento
#    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False
#
#    #OrdemServico["VALOR_TOTAL_ADIANTAMENTO"] = valorTotalAdiantamento
```
  - VALOR_TOTAL_ADIANTAMENTO "Valor total do adiantamento R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_ADIANTAMENTO]
  - NUM_ABERTURA_CHAMADO "N° da Abertura de Chamado do Deslocamento a Serviço de Quem Está Acompanhando" [TextBox String → CPE_DESLOCAMENTO.NUM_ABERTURA_CHAMADO]
  - TIPO_DESLOCAMENTO "Tipo de Deslocamento" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESLOCAMENTO]
**TIPO_DESLOCAMENTO.ScriptModificado**
```python
##Viagem internacional
#
#if Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
#    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
#    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
#    Formulario["COTACAO_DOLAR"].Visivel = True
#    Formulario["COTACAO_DOLAR"].Habilitado = True  
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
#    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = True
#    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = True
#    Formulario["PAIS"].Visivel = True
#    Formulario["PAIS"].Habilitado = True       
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
#    Formulario["TIPO_HOSPEDAGEM"].Visivel = True
#    Formulario["TIPO_HOSPEDAGEM"].Habilitado = False    
#    Formulario["TIPO_HOSPEDAGEM"].Valor = "Avulsa"
#    Formulario["QUANTIDADE_DIARIA"].Visivel = True
#    Formulario["QUANTIDADE_DIARIA"].Habilitado = True    
#    Formulario["CIDADE_DESTINO"].Visivel = False
#    Formulario["CIDADE_DESTINO"].Habilitado = False
#    Formulario["VALOR_DIARIA"].Visivel = False
#    Formulario["VALOR_DIARIA"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
#    Formulario["VALOR_DIARIA"].Visivel = False
#    Formulario["VALOR_DIARIA"].Habilitado = False
#    Formulario["DIARIA_COTACAO_REAL"].Visivel = True
#    Formulario["DIARIA_COTACAO_REAL"].Habilitado = True
#    
#
#    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
#    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
#    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
#    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
#    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
#    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
#
#    
#    
#    
#
#    
#    
#else:
#
#
#    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
#    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
#    Formulario["COTACAO_DOLAR"].Visivel = False
#    Formulario["COTACAO_DOLAR"].Habilitado = False   
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
#    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = False
#    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = False
#    Formulario["PAIS"].Visivel = False
#    Formulario["PAIS"].Habilitado = False  
#
#    
#    Formulario["CIDADE_DESTINO"].Visivel = True
#    Formulario["CIDADE_DESTINO"].Habilitado = True
#    Formulario["CIDADE_DESTINO"].Visivel = True
#    Formulario["CIDADE_DESTINO"].Habilitado = True
#    Formulario["VALOR_DIARIA"].Visivel = True
#    Formulario["VALOR_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
#    Formulario["DIARIA_COTACAO_REAL"].Visivel = False
#    Formulario["DIARIA_COTACAO_REAL"].Habilitado = False
#
```
  - CIDADE_ORIGEM "Cidade de Origem" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_ORIGEM]
  - SIM_NAO_REFEICAO "O Empregado/Gestor terá direito a refeição complementar?" [DropDownList String → CPE_DESLOCAMENTO.SIM_NAO_REFEICAO] obrigatório
  - NUMERO_NT "Número da Nota Técnica" [TextBox String → CPE_CONTRATOS.NUMERO_NT]
  - Favorecido (nativo) obrigatório
  - FAVORECIDO_DESLOCAMENTO "Favorecido" [DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO]
**FAVORECIDO_DESLOCAMENTO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#Formulario["CARGO_DESLOCAMENTO"].Visivel = True
#Formulario["FUNCAO_DESLOCAMENTO"].Visivel = True
#Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = True
#Formulario["MATRICULA_DESLOCAMENTO"].Visivel = True
#
#
#
#Formulario["CARGO_DESLOCAMENTO"].Habilitado = False
#Formulario["FUNCAO_DESLOCAMENTO"].Habilitado = False
#Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Habilitado = False
#Formulario["MATRICULA_DESLOCAMENTO"].Habilitado = False
#
#
#
#Formulario["CARGO_DESLOCAMENTO"].Valor = None
#Formulario["FUNCAO_DESLOCAMENTO"].Valor = None
#Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = None
#Formulario["MATRICULA_DESLOCAMENTO"].Valor = None
#
#
#
#cargo = ""
#funcao = ""
#desc_colaborador = ""
#matricula = ""
#
#if Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != "" or Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != None:
#
#    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor)
#    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
#    if favorecidoCustom != None:
#        nomeFavorecido = favorecidoCustom.Nome
#        orgaoFavorecido = favorecidoCustom.OrgaoId
#    else:
#        nomeFavorecido = OrdemServico.Favorecido.Nome
#        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId
#
#    #Formulario["ORGAO_FAVORECIDO"].Valor = orgaoFavorecido
#    #Consulta o cargo e a função do Favorecido
#
#    lista = Utils.ExecuteDataTable("SELECT SUBSTR(c.CARGO,INSTR(c.CARGO,'|')+1,LENGTH(c.CARGO)) AS CARGO1, c.FUNCAO_GRATIFICADA, c.DESC_COLABORADOR, c.MATRICULA, c.FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND C.NUMERO_SUBCR_NIVEL1 = O.SIGLA AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )
#
#    #lista = Utils.ExecuteDataTable("SELECT SUBSTR(CARGO,INSTR(CARGO,'|')+1,LENGTH(CARGO)) AS CARGO1, FUNCAO_GRATIFICADA, DESC_COLABORADOR, MATRICULA, FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND LPAD(C.NUMERO_SUBCR_NIVEL1,5) = LPAD(O.SIGLA,5) AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )
#
#    for linha in lista.Rows:
#        cargo = linha["CARGO1"].ToString()
#        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
#            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
#        
#        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
#        matricula = linha["MATRICULA"].ToString()
#
#    Formulario["CARGO_DESLOCAMENTO"].Valor = cargo.ToString()
#    Formulario["FUNCAO_DESLOCAMENTO"].Valor = funcao.ToString()
#    Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = desc_colaborador.ToString()
#    Formulario["MATRICULA_DESLOCAMENTO"].Valor = matricula.ToString()
#
#    
#        
#
#
#if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
#    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False
#else:
#    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
#    
#
```
  - MATRICULA_DESLOCAMENTO "Matrícula" [TextBox Integer → CPE_DESLOCAMENTO.MATRICULA_DESLOCAMENTO]
  - CARGO_DESLOCAMENTO "Cargo" [TextBox String → CPE_DESLOCAMENTO.CARGO_DESLOCAMENTO]
  - FUNCAO_DESLOCAMENTO "Função" [TextBox String → CPE_DESLOCAMENTO.FUNCAO_DESLOCAMENTO]
  - DESC_COLABORADOR_DESLOCAMENTO "Tipo de Colaborador" [TextBox String → CPE_DESLOCAMENTO.DESC_COLABORADOR_DESLOCAMENTO]
  - CELULAR "Celular do Favorecido" [TextBox String → CP_ORDEM_SERVICO.CELULAR]
  - SAIDA "Saída dia" [DatePicker DateTime → CPE_DESLOCAMENTO.SAIDA]
  - RETORNO_DIA "Retorno dia" [DatePicker DateTime → CPE_DESLOCAMENTO.RETORNO_DIA] — Coluna=3
  - PAIS "País de Destino" [DropDownList String → CPE_DESLOCAMENTO.PAIS] — Coluna=3
**PAIS.ScriptModificado**
```python
#  
#        ################## grupo A
#if Formulario["PAIS"].Valor == "AFEGANISTÃO" or Formulario["PAIS"].Valor == "ARMÊNIA" or Formulario["PAIS"].Valor == "BANGLADESH" or Formulario["PAIS"].Valor == "BELARUS" or Formulario["PAIS"].Valor == "BENIN" or Formulario["PAIS"].Valor == "BOLÍVIA" or Formulario["PAIS"].Valor == "BURKINAFASSO" or Formulario["PAIS"].Valor == "BUTÃO"  or Formulario["PAIS"].Valor == "CHILE" or Formulario["PAIS"].Valor == "COMORES" or Formulario["PAIS"].Valor == "REPÚBLICA POPULAR DEMOCRÁTICA DA CORÉIA" or Formulario["PAIS"].Valor == "COSTA RICA" or Formulario["PAIS"].Valor == "EL SALVADOR" or Formulario["PAIS"].Valor == "EQUADOR" or Formulario["PAIS"].Valor == "ESLOVÊNIA" or Formulario["PAIS"].Valor == "FILIPINAS" or Formulario["PAIS"].Valor == "GÂMBIA" or Formulario["PAIS"].Valor == "GUIANA" or Formulario["PAIS"].Valor == "GUINÉ BISSAU" or Formulario["PAIS"].Valor == "GUINÉ" or Formulario["PAIS"].Valor == "HONDURAS" or Formulario["PAIS"].Valor == "INDONÉSIA" or Formulario["PAIS"].Valor == "IRÃ" or Formulario["PAIS"].Valor == "IRAQUE" or Formulario["PAIS"].Valor == "LAOS" or Formulario["PAIS"].Valor == "LÍBANO" or Formulario["PAIS"].Valor == "MALÁSIA" or Formulario["PAIS"].Valor == "MALDIVAS" or Formulario["PAIS"].Valor == "MARROCOS" or Formulario["PAIS"].Valor == "MONGÓLIA" or Formulario["PAIS"].Valor == "NAMÍBIA" or Formulario["PAIS"].Valor == "MYANMAR" or Formulario["PAIS"].Valor == "NAURU" or Formulario["PAIS"].Valor == "NEPAL"or Formulario["PAIS"].Valor == "NICARÁGUA" or Formulario["PAIS"].Valor == "PANAMÁ" or Formulario["PAIS"].Valor == "PARAGUAI" or Formulario["PAIS"].Valor == " REP. CENTRO AFRICANA" or Formulario["PAIS"].Valor == "REPÚBLICA TOGOLESA" or Formulario["PAIS"].Valor == "SALOMÃO" or Formulario["PAIS"].Valor == "SAMOA" or Formulario["PAIS"].Valor == "SERRA LEOA" or Formulario["PAIS"].Valor == "SÍRIA" or Formulario["PAIS"].Valor == "SOMÁLIA" or Formulario["PAIS"].Valor == "SRI LANKA" or Formulario["PAIS"].Valor == "TURQUIA" or Formulario["PAIS"].Valor == "TADJIQUISTÃO" or Formulario["PAIS"].Valor == "TAILÂNDIA" or Formulario["PAIS"].Valor == "TIMOR LESTE" or Formulario["PAIS"].Valor == "TONGA" or Formulario["PAIS"].Valor == "TUNÍSIA" or Formulario["PAIS"].Valor == "TURCOMENISTÃO" or Formulario["PAIS"].Valor == "TUVALU" or Formulario["PAIS"].Valor == "VIETNÃ" or Formulario["PAIS"].Valor == "ZIMBÁBUE":
#    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
#        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "220"
#                        
#    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
#            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "200"
#            
#    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
#            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "190"
#            
#    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
#          Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "180"
#          
#    else:
#          Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "170"
#            
#        ###################### grupo B    
#            
#elif Formulario["PAIS"].Valor == "ÁFRICA DO SUL" or Formulario["PAIS"].Valor == "ALBÂNIA" or Formulario["PAIS"].Valor == "ANDORA" or Formulario["PAIS"].Valor == "ARGÉLIA" or Formulario["PAIS"].Valor == "ARGENTINA" or Formulario["PAIS"].Valor == "AUSTRÁLIA" or Formulario["PAIS"].Valor == "BELIZE" or Formulario["PAIS"].Valor == "BÓSNIA-HERZEGÓVINA"  or Formulario["PAIS"].Valor == "BURUNDI" or Formulario["PAIS"].Valor == " CABO VERDE" or Formulario["PAIS"].Valor == "CAMARÕES" or Formulario["PAIS"].Valor == "CAMBOJA" or Formulario["PAIS"].Valor == "CATAR" or Formulario["PAIS"].Valor == "CHADE" or Formulario["PAIS"].Valor == "CHINA" or Formulario["PAIS"].Valor == "CHIPRE" or Formulario["PAIS"].Valor == "COLÔMBIA" or Formulario["PAIS"].Valor == "DOMINICA" or Formulario["PAIS"].Valor == "EGITO" or Formulario["PAIS"].Valor == "ERITRÉIA" or Formulario["PAIS"].Valor == "ESTÔNIA" or Formulario["PAIS"].Valor == "ETIÓPIA" or Formulario["PAIS"].Valor == "GANA" or Formulario["PAIS"].Valor == "GEÓRGIA" or Formulario["PAIS"].Valor == "GUINÉ EQUATORIAL" or Formulario["PAIS"].Valor == "HAITI" or Formulario["PAIS"].Valor == "HUNGRIA" or Formulario["PAIS"].Valor == "IEMEN" or Formulario["PAIS"].Valor == " ILHAS MARSHALL" or Formulario["PAIS"].Valor == "ÍNDIA" or Formulario["PAIS"].Valor == "KIRIBATI" or Formulario["PAIS"].Valor == "LESOTO" or Formulario["PAIS"].Valor == "LÍBIA" or Formulario["PAIS"].Valor == "MACEDÔNIA"or Formulario["PAIS"].Valor == "MADAGASCAR" or Formulario["PAIS"].Valor == "MALAUÍ" or Formulario["PAIS"].Valor == "MICRONÉSIA" or Formulario["PAIS"].Valor == "MOÇAMBIQUE" or Formulario["PAIS"].Valor == "MOLDÁVIA" or Formulario["PAIS"].Valor == "NÍGER" or Formulario["PAIS"].Valor == "NIGÉRIA" or Formulario["PAIS"].Valor == "NOVA ZELÂNDIA" or Formulario["PAIS"].Valor == "PALAU" or Formulario["PAIS"].Valor == "PAPUA NOVA GUINÉ" or Formulario["PAIS"].Valor == "PAQUISTÃO" or Formulario["PAIS"].Valor == "PERU" or Formulario["PAIS"].Valor == "POLÔNIA" or Formulario["PAIS"].Valor == "QUÊNIA" or Formulario["PAIS"].Valor == "REPÚBLICA DOMINICANA" or Formulario["PAIS"].Valor == "ROMÊNIA" or Formulario["PAIS"].Valor == "RUANDA" or Formulario["PAIS"].Valor == " SÃO TOMÉ E PRÍNCIPE" or Formulario["PAIS"].Valor == "SENEGAL" or Formulario["PAIS"].Valor == "TANZÂNIA" or Formulario["PAIS"].Valor == "SUDÃO"  or Formulario["PAIS"].Valor == "URUGUAI" or Formulario["PAIS"].Valor == "UZBEQUISTÃO" or Formulario["PAIS"].Valor == "VENEZUELA":
#
#    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
#        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "300"
#                    
#    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
#        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "280"
#
#    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
#        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "270"
#                
#    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
#        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "260"
#        
#    else:
#        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "250"
#                    
#                    
#
#            ################### grupo C
#
#            
#elif Formulario["PAIS"].Valor == "ANTÍGUA E BARBUDA" or Formulario["PAIS"].Valor == "ARÁBIA SAUDITA" or Formulario["PAIS"].Valor == "AZERBAIDJÃO" or Formulario["PAIS"].Valor == "BAHAMAS" or Formulario["PAIS"].Valor == "BAREINE" or Formulario["PAIS"].Valor == "BOTSUANA" or Formulario["PAIS"].Valor == "BRUNEI DARUSSALAM" or Formulario["PAIS"].Valor == "BULGÁRIA"  or Formulario["PAIS"].Valor == "CANADÁ" or Formulario["PAIS"].Valor == "CINGAPURA" or Formulario["PAIS"].Valor == "CONGO" or Formulario["PAIS"].Valor == "COSTA DO MARFIM" or Formulario["PAIS"].Valor == "CUBA" or Formulario["PAIS"].Valor == "DJIBUTI" or Formulario["PAIS"].Valor == "EMIRADOS ÁRABES" or Formulario["PAIS"].Valor == "FIJI" or Formulario["PAIS"].Valor == "GABÃO" or Formulario["PAIS"].Valor == "GUATEMALA" or Formulario["PAIS"].Valor == "REPÚBLICA DEMOCRÁTICA DO CONGO" or Formulario["PAIS"].Valor == "JAMAICA" or Formulario["PAIS"].Valor == "JORDÂNIA" or Formulario["PAIS"].Valor == "LETÔNIA" or Formulario["PAIS"].Valor == "LIBÉRIA" or Formulario["PAIS"].Valor == "GEÓRGIA" or Formulario["PAIS"].Valor == "GUINÉ EQUATORIAL" or Formulario["PAIS"].Valor == "HAITI" or Formulario["PAIS"].Valor == "MAURÍCIO" or Formulario["PAIS"].Valor == "MAURITÂNIA" or Formulario["PAIS"].Valor == "MÉXICO" or Formulario["PAIS"].Valor == "MALTA" or Formulario["PAIS"].Valor == " REPÚBLICA TCHECA" or Formulario["PAIS"].Valor == "RÚSSIA" or Formulario["PAIS"].Valor == "SAN MARINO" or Formulario["PAIS"].Valor == "SANTA LÚCIA"or Formulario["PAIS"].Valor == "SÃO CRISTOVÃO E NÉVIS" or Formulario["PAIS"].Valor == "SÃO VICENTE E GRANADINAS" or Formulario["PAIS"].Valor == "TAIWAN" or Formulario["PAIS"].Valor == "TRINIDAD E TOBAGO" or Formulario["PAIS"].Valor == "UCRÂNIA" or Formulario["PAIS"].Valor == "UGANDA" or Formulario["PAIS"].Valor == "ZÂMBIA":
#    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
#        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "350"
#                
#    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
#        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "330"
#                    
#    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
#        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "320"
#                
#    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
#        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "310"
#    
#    else:
#        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "300"     
#                    
#                
#            #################### grupo D 
#if Formulario["PAIS"].Valor == "ALEMANHA" or Formulario["PAIS"].Valor == "ANGOLA" or Formulario["PAIS"].Valor == "ÁUSTRIA" or Formulario["PAIS"].Valor == "BARBADOS" or Formulario["PAIS"].Valor == "BÉLGICA"or Formulario["PAIS"].Valor == "CAZAQUISTÃO" or Formulario["PAIS"].Valor == "CORÉIA DO SUL" or Formulario["PAIS"].Valor == "CROÁCIA"  or Formulario["PAIS"].Valor == "DINAMARCA" or Formulario["PAIS"].Valor == "ESPANHA" or Formulario["PAIS"].Valor == "ESTADOS UNIDOS DA AMÉRICA" or Formulario["PAIS"].Valor == "FINLÂNDIA" or Formulario["PAIS"].Valor == "FRANÇA" or Formulario["PAIS"].Valor == "GRANADA" or Formulario["PAIS"].Valor == "GRÉCIA HONG KONG" or Formulario["PAIS"].Valor == "IRLANDA" or Formulario["PAIS"].Valor == "ISLÂNDIA" or Formulario["PAIS"].Valor == "ISRAEL" or Formulario["PAIS"].Valor == "ITÁLIA" or Formulario["PAIS"].Valor == "JAPÃO" or Formulario["PAIS"].Valor == "KUAITE" or Formulario["PAIS"].Valor == "LIECHTENSTEIN" or Formulario["PAIS"].Valor == "LUXEMBURGO" or Formulario["PAIS"].Valor == "MÔNACO" or Formulario["PAIS"].Valor == "MONTENEGRO" or Formulario["PAIS"].Valor == "NORUEGA" or Formulario["PAIS"].Valor == "OMÃ" or Formulario["PAIS"].Valor == "PEÍSES BAIXOS" or Formulario["PAIS"].Valor == "PORTUGAL" or Formulario["PAIS"].Valor == "REINO UNIDO" or Formulario["PAIS"].Valor == "REPÚBLICA QUIRGUIZ" or Formulario["PAIS"].Valor == "SEICHELES" or Formulario["PAIS"].Valor == "SÉRVIA SUAZILÂNDIA" or Formulario["PAIS"].Valor == "SUÉCIA" or Formulario["PAIS"].Valor == "SUÍÇA" or Formulario["PAIS"].Valor == "VANUATU":
#    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
#        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "460"
#                
#    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
#            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "420"
#            
#    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
#            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "390"
#            
#    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
#            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "370"
#                  
#                  
#    else:
#            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "350"
#
```
  - CIDADE_DESTINO "Cidade de Destino" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_DESTINO] — Coluna=2
**CIDADE_DESTINO.ScriptModificado**
```python
sqlConsultaCidadeDestino = DB.ExecuteDataTable("SELECT to_char(id_cidade) as id, c.descricao ||' - '|| c.id_estado as cidade FROM cidade_v c WHERE id_cidade = '"+Formulario["CIDADE_DESTINO"].Valor.ToString()+"'")

sqlConsultaClassificacao = DB.ExecuteDataTable("select DISTINCT CLASSIFICACAO, CIDADE || ' - ' || UF AS cidadeuf from Z_00143_CIDADES_CLASSIFICACOES where CIDADE || ' - ' || UF = '"+sqlConsultaCidadeDestino.Rows[0]["CIDADE"].ToString()+"'")

for classificacao in sqlConsultaClassificacao.Rows:
    Formulario["CIDADE_CLASSIFICACAO"].Valor = classificacao["CLASSIFICACAO"].ToString()
```
  - CIDADE_CLASSIFICACAO "Cidade Classificação" [TextBox String → CPE_CSC.CIDADE_CLASSIFICACAO]
    - coluna CLASSIFICACAO obrigatório
    - coluna UF obrigatório
    - coluna CIDADE obrigatório
  - CIDADE_DESTINO_INTERNACIONAL "Cidade/País de Destino" [TextBox String → CPE_DESLOCAMENTO.CIDADE_DESTINO_INTERNACIONAL] — Coluna=2
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Localizador e Voucher - Solicitação
  - CSC_VALOR2 "Valor Total das Locações de Carro" [TextBox Decimal → CPE_CSC.CSC_VALOR2]
  - CSC_OBS1 "Observação" [Memo String(2000) → CPE_CSC.CSC_OBS1]
  - PAHL_NUM_ARGO "Número da OS Argo" [TextBox String → CPE_CSC.PAHL_NUM_ARGO]
  - PAHL_PASSAGENS "Passagens Aéreas" [CheckBox Boolean → CPE_CSC.PAHL_PASSAGENS]
  - PAHL_HOSPEDAGENS "Hospedagens" [CheckBox Boolean → CPE_CSC.PAHL_HOSPEDAGENS]
  - PAHL_LOCACOES "Locações" [CheckBox Boolean → CPE_CSC.PAHL_LOCACOES]
  - PAH_LOCALIZADORES "Localizador Aereo" [DataGrid RecordList → Z_00143_PAH_LOCALIZADORES.PAH_LOCALIZADORES] — FormaEdicaoWeb=JanelaPopup
    - coluna VALOR_TRECHO
    - coluna CIA_AEREA obrigatório
    - coluna LOCALIZADOR obrigatório
    - coluna SEQUENCIA obrigatório
  - CSC_DATA_INICIO "Data da Saída" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO]
  - CSC_DATA_FIM "Data do Retorno" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM]
  - CSC_VALOR1_TOTAL "Valor das Passagens" [TextBox Decimal → CPE_CSC.CSC_VALOR1_TOTAL]
  - PAH_VOUCHER_HOSPEDAGEM "Voucher de Hospedagem" [TextBox String → CPE_CSC.PAH_VOUCHER_HOSPEDAGEM]
  - CSC_VALOR1 "Valor Total das Diárias" [TextBox Decimal → CPE_CSC.CSC_VALOR1]
  - PAHL_VOUCHER_CARRO "Voucher de Locação de Carro" [TextBox String → CPE_CSC.PAHL_VOUCHER_CARRO]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Opções de Reserva
  - PAHL_LOCACOES "Locações de Carro" [CheckBox Boolean → CPE_CSC.PAHL_LOCACOES]
**PAHL_LOCACOES.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#camposVisiveis = None
#camposHabilitados = None
#vis = False
#hab = False
#
#pessoa = Pessoa.Carrega(Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
#if OrdemServico.Servico.Sigla == "DESLOCAMENTO":
#   # lista de campos a serem alteradas a visibilidade.
#   camposVisiveis = ["PAHL_LOCACOES_CARRO", "CSC_OBS"]
#   camposHabilitados = ["PAHL_LOCACOES_CARRO", "CSC_OBS"]
#   if Formulario["PAHL_LOCACOES"].Valor == True:
#      vis = True
#      hab = True
#
#   for controle in Formulario.Controles:
#       # preserva a visibilidade atual dos campos
#       visivel = Formulario[controle.Key].Visivel
#       habilitado = Formulario[controle.Key].Habilitado
#       valor = Formulario[controle.Key].Valor
#       for campo in camposVisiveis:
#           if controle.Key == campo:
#              visivel = vis
#              valor = None
#              break
#       Formulario[controle.Key].Visivel = visivel
#       
#       for campo in camposHabilitados:
#           if controle.Key == campo:
#              habilitado = hab
#              break
#       Formulario[controle.Key].Habilitado = habilitado
#       Formulario[controle.Key].Valor = valor
#       
#   #Formulario["PAH_MOTIVO_SOL"].Visivel = False
#   
#   #cargos = ["TECNICO", "TECNICO DE OPERACOES", "TECNICO ESPECIALISTA"]
#   
#   #if (Formulario["PAHL_PASSAGENS"].Valor == True or Formulario["PAHL_HOSPEDAGENS"].Valor == True or Formulario["PAHL_LOCACOES"].Valor == True) and cargos.Contains(pessoa["CARGO_FUNCIONAL"]):
#   Formulario["PAH_MOTIVO_SOL"].Visivel = True
#   Formulario["PAH_MOTIVO_SOL"].Habilitado = True
#   #else:
#   #   Formulario["PAH_MOTIVO_SOL"].Visivel = False
#   #   Formulario["PAH_MOTIVO_SOL"].Habilitado = False
#
```
  - PAHL_PASSAGENS "Reserva de Passagens Aéreas" [CheckBox Boolean → CPE_CSC.PAHL_PASSAGENS]
**PAHL_PASSAGENS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#camposVisiveis = None
#camposHabilitados = None
#vis = False
#hab = False
#
#pessoa = Pessoa.Carrega(Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
#if OrdemServico.Servico.Sigla == "DESLOCAMENTO":
#   # lista de campos a serem alteradas a visibilidade.
#   camposVisiveis = ["RESERVA_DE_VOO", "DESCRICAO_OBRIG", "CSC_OBS"]
#   camposHabilitados = ["RESERVA_DE_VOO", "DESCRICAO_OBRIG", "CSC_OBS"]
#   camposVisiveis = ["DESCRICAO_OBRIG", "CSC_OBS"]
#   camposHabilitados = ["DESCRICAO_OBRIG", "CSC_OBS"]
#   if Formulario["PAHL_PASSAGENS"].Valor == True:
#      vis = True
#      hab = True
#    
#
#   for controle in Formulario.Controles:
#       # preserva a visibilidade atual dos campos
#       visivel = Formulario[controle.Key].Visivel
#       habilitado = Formulario[controle.Key].Habilitado
#       valor = Formulario[controle.Key].Valor
#       for campo in camposVisiveis:
#           if controle.Key == campo:
#              visivel = vis
#              valor = None
#              break
#       Formulario[controle.Key].Visivel = visivel
#       
#       for campo in camposHabilitados:
#           if controle.Key == campo:
#              habilitado = hab
#              break
#       Formulario[controle.Key].Habilitado = habilitado
#       Formulario[controle.Key].Valor = valor
#       
#   cargos = ["TECNICO", "TECNICO DE OPERACOES", "TECNICO ESPECIALISTA"]

#if (Formulario["PAHL_PASSAGENS"].Valor == True) and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional"):
#    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Visivel = True
#    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Habilitado = True
#    Formulario["RESERVA_DE_VOO"].Visivel = False
#    Formulario["RESERVA_DE_VOO"].Habilitado = False
#    Formulario["DESCRICAO_OBRIG"].Visivel = True
#    Formulario["DESCRICAO_OBRIG"].Habilitado = True
#    Formulario["CSC_OBS"].Visivel = True
#    Formulario["CSC_OBS"].Habilitado = True
#elif (Formulario["PAHL_PASSAGENS"].Valor == True) and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
#    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Visivel = False
#    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Habilitado = False
#    Formulario["RESERVA_DE_VOO"].Visivel = True
#    Formulario["RESERVA_DE_VOO"].Habilitado = True    
#    Formulario["DESCRICAO_OBRIG"].Visivel = True
#    Formulario["DESCRICAO_OBRIG"].Habilitado = True
#    Formulario["CSC_OBS"].Visivel = True
#    Formulario["CSC_OBS"].Habilitado = True
#else:
#    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Visivel = False
#    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Habilitado = False
#    Formulario["RESERVA_DE_VOO"].Visivel = False
#    Formulario["RESERVA_DE_VOO"].Habilitado = False    
#    Formulario["DESCRICAO_OBRIG"].Visivel = False
#    Formulario["DESCRICAO_OBRIG"].Habilitado = False
#    Formulario["CSC_OBS"].Visivel = False
#    Formulario["CSC_OBS"].Habilitado = False
```
  - PAHL_HOSPEDAGENS "Reserva de Hospedagens" [CheckBox Boolean → CPE_CSC.PAHL_HOSPEDAGENS]
**PAHL_HOSPEDAGENS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#camposVisiveis = None
#camposHabilitados = None
#vis = False
#hab = False
#
#pessoa = Pessoa.Carrega(Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
#if OrdemServico.Servico.Sigla == "DESLOCAMENTO":
#   # lista de campos a serem alteradas a visibilidade.
#   camposVisiveis = ["PAH_DATA_ENTRADA", "PAH_DATA_SAIDA", "PAH_EVENTO_HOTEL", "DESCRICAO_OBRIG", "CSC_OBS"]
#   camposHabilitados = ["PAH_DATA_ENTRADA", "PAH_DATA_SAIDA", "PAH_EVENTO_HOTEL", "DESCRICAO_OBRIG", "CSC_OBS"]
#   if Formulario["PAHL_HOSPEDAGENS"].Valor == True:
#      vis = True
#      hab = True
#   for controle in Formulario.Controles:
#       # preserva a visibilidade atual dos campos
#       visivel = Formulario[controle.Key].Visivel
#       habilitado = Formulario[controle.Key].Habilitado
#       valor = Formulario[controle.Key].Valor
#       for campo in camposVisiveis:
#           if controle.Key == campo:
#              visivel = vis
#              valor = None
#              break
#       Formulario[controle.Key].Visivel = visivel
#       
#       for campo in camposHabilitados:
#           if controle.Key == campo:
#              habilitado = hab
#              break
#       Formulario[controle.Key].Habilitado = habilitado
#       Formulario[controle.Key].Valor = valor
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Solicitação de Reservas
  - PAHL_LOCACOES_CARRO "Locações de Carro" [DataGrid RecordList → Z_00143_PAHL_LOCACOES_CARRO.PAHL_LOCACOES_CARRO]
**PAHL_LOCACOES_CARRO.ScriptConfirmado**
```python
#if Registro["DATA_HORA_DEVOLUCAO"] < Registro["DATA_HORA_RETIRADA"]:
#   Formulario.ExibeMensagem("ATENÇÃO: Data/Hora da Devolução não pode ser menor que Data/Hora da Retirada!")
```
    - coluna CELULAR_FAVORECIDO obrigatório
    - coluna CARRO4X4 obrigatório
    - coluna DATA_HORA_RETIRADA obrigatório
    - coluna LOCAL_DEVOLUCAO obrigatório
    - coluna DATA_HORA_DEVOLUCAO obrigatório
**PAHL_LOCACOES_CARRO.DATA_HORA_DEVOLUCAO.ScriptModificado**
```python
#if FormularioRegistro["DATA_HORA_DEVOLUCAO"].Valor < FormularioRegistro["DATA_HORA_RETIRADA"].Valor:
#   Formulario.ExibeMensagem("Data/Hora da Devolução não pode ser menor que Data/Hora da Retirada!")
#   FormularioRegistro["DATA_HORA_DEVOLUCAO"].Valor = None
```
    - coluna CPF_FAVORECIDO obrigatório
    - coluna LOCAL_RETIRADA obrigatório
    - coluna VALOR_LOCACAO
  - DESCRICAO_OBRIG "Motivo da Viagem" [TextBox String(2000) → CP_ORDEM_SERVICO.DESCRICAO_OBRIG]
  - CSC_OBS "Observação" [Memo String(2000) → CPE_CSC.CSC_OBS]
  - DATA_INICIO_AUX1 "Data Início da Viagem" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_INICIO_AUX1]
  - PAH_MOTIVO_SOL "Motivo da Solicitação" [DropDownList String → CPE_CSC.PAH_MOTIVO_SOL]
  - PAH_LOCALIZADORES "Localizador Aereo" [DataGrid RecordList → Z_00143_PAH_LOCALIZADORES.PAH_LOCALIZADORES]
    - coluna SEQUENCIA obrigatório
    - coluna VALOR_TRECHO
    - coluna CIA_AEREA obrigatório
    - coluna LOCALIZADOR obrigatório
  - PAH_VOUCHER_HOSPEDAGEM "Voucher de Hospedagem" [TextBox String → CPE_CSC.PAH_VOUCHER_HOSPEDAGEM]
  - RESERVA_DE_VOO "Informações da Reserva de Voo - Nacional" [DataGrid RecordList → Z_00143_RESERVA_DE_VOO.RESERVA_DE_VOO]
    - coluna SEQUENCIA obrigatório
**RESERVA_DE_VOO.SEQUENCIA.ScriptModificado**
```python
rv = OrdemServico["RESERVA_DE_VOO"]

for seq in rv.Rows:
    if FormularioRegistro["SEQUENCIA"].Valor == seq["SEQUENCIA"]:
       Formulario.ExibeMensagem("A T E N Ç Ã O !!! \n Nº do Trecho já lançado!")
       FormularioRegistro["SEQUENCIA"].Valor = None
```
    - coluna ALT_EXC obrigatório
    - coluna QUANTIDADE_BAGAGENS obrigatório
    - coluna AEROPORTO_DESTINO obrigatório
    - coluna UF_ORIGEM obrigatório
    - coluna CIDADE_ORIGEM obrigatório
    - coluna TRECHO obrigatório
    - coluna ALT_OU_EXC
    - coluna HORA_ESTIMADA_VOO obrigatório
    - coluna DESPACHO_BAGAGENS obrigatório
**RESERVA_DE_VOO.DESPACHO_BAGAGENS.ScriptModificado**
```python
#Sim;Não
FormularioRegistro["QUANTIDADE_BAGAGENS"].Valor = None
FormularioRegistro["QUANTIDADE_BAGAGENS"].Habilitado = FormularioRegistro["DESPACHO_BAGAGENS"].Valor == "Sim"

if FormularioRegistro["DESPACHO_BAGAGENS"].Valor == "Não":
   FormularioRegistro["QUANTIDADE_BAGAGENS"].Valor = 0
```
    - coluna AEROPORTO_ORIGEM obrigatório
    - coluna UF_DESTINO obrigatório
    - coluna CIDADE_DESTINO obrigatório
    - coluna DATA_VOO obrigatório
  - RESERVA_DE_VOO_INTERNACIONAL "Informações para Reserva de Voo - Internacional" [DataGrid RecordList → Z_00143_RESERVA_DE_VOO_INTERNACIONAL.RESERVA_DE_VOO_INTERNACIONAL]
    - coluna SEQUENCIA obrigatório
    - coluna TRECHO obrigatório
    - coluna CIDADE_ORIGEM obrigatório
    - coluna AEROPORTO_ORIGEM obrigatório
    - coluna CIDADE_DESTINO obrigatório
    - coluna AEROPORTO_DESTINO obrigatório
    - coluna DATA_VOO obrigatório
    - coluna DESPACHO_BAGAGENS obrigatório
    - coluna QUANTIDADE_BAGAGENS obrigatório
    - coluna HORA_ESTIMADA_VOO obrigatório
  - PAH_DATA_ENTRADA "Data de Entrada no Hotel" [DatePicker DateTime → CPE_CSC.PAH_DATA_ENTRADA]
  - PAH_DATA_SAIDA "Data de Saída do Hotel" [DatePicker DateTime → CPE_CSC.PAH_DATA_SAIDA]
**PAH_DATA_SAIDA.ScriptModificado**
```python
#if Formulario["PAH_DATA_SAIDA"].Valor <= Formulario["PAH_DATA_ENTRADA"].Valor:
#   Formulario.ExibeMensagem("'Data de Saída do Hotel' deve ser maior que 'Data de Entrada no Hotel'!")
#   Formulario["PAH_DATA_SAIDA"].Valor = None
```
  - PAH_EVENTO_HOTEL "Evento no Hotel?" [DropDownList String → CPE_CSC.PAH_EVENTO_HOTEL]
**PAH_EVENTO_HOTEL.ScriptModificado**
```python
#Formulario["PAH_HOTEL_EVENTO"].Visivel = Formulario["PAH_EVENTO_HOTEL"].Valor == "Sim"
#Formulario["PAH_HOTEL_EVENTO"].Habilitado = Formulario["PAH_EVENTO_HOTEL"].Valor == "Sim"
#
```
  - PAH_HOTEL_EVENTO "Hotel do Evento" [TextBox String → CPE_CSC.PAH_HOTEL_EVENTO]
  - PAHL_VOUCHER_CARRO "Voucher de Locação de Carro" [TextBox String → CPE_CSC.PAHL_VOUCHER_CARRO]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados do Favorecido
  - MATRICULA_DESLOCAMENTO "Matrícula do Favorecido" [TextBox Integer → CPE_DESLOCAMENTO.MATRICULA_DESLOCAMENTO] obrigatório
  - CPF "CPF" [TextBox String(15) → CP_ORDEM_SERVICO.CPF]
  - FAVORECIDO_DESLOCAMENTO "Favorecido" [DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO]
**FAVORECIDO_DESLOCAMENTO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
#pessoa = Pessoa.Carrega(Convert.ToInt32(Formulario["FAVORECIDO_TODOS"].Valor))
#pessoa = Pessoa.Carrega("Id", Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
#orgao = Orgao.Carrega(pessoa.OrgaoId)
#
#OrdemServico.Favorecido = pessoa
#
#for controle in Formulario.Controles:
#    if controle.Key != "FAVORECIDO_DESLOCAMENTO":
#       Formulario[controle.Key].Visivel = False
#       Formulario[controle.Key].Valor = None
#
#Formulario["MATRICULA"].Valor = pessoa["MATRICULA"]
#Formulario["CPF"].Valor = pessoa["CPF"]
#Formulario["EMAIL_CLIENTE"].Valor = pessoa.Email #["EMAIL"]
#Formulario["TELEFONE_CLIENTE"].Valor = pessoa.Telefone #["TELEFONE"]
#Formulario["SCR_PRESTADOR"].Valor = orgao.Descricao
#Formulario["CELULAR"].Valor = None
# 
#Formulario["MATRICULA"].Visivel = True
#Formulario["CPF"].Visivel = True
#Formulario["EMAIL_CLIENTE"].Visivel = True
#Formulario["TELEFONE_CLIENTE"].Visivel = True
#Formulario["SCR_PRESTADOR"].Visivel = True
#Formulario["CELULAR"].Visivel = True
#
#Formulario["MATRICULA"].Habilitado = False
#Formulario["CPF"].Habilitado = False
#Formulario["EMAIL_CLIENTE"].Habilitado = False
#Formulario["TELEFONE_CLIENTE"].Habilitado = False
#Formulario["SCR_PRESTADOR"].Habilitado = False
#Formulario["CELULAR"].Habilitado = True
#
#Formulario["CSC_NUM_SISLOC"].Visivel = True
#Formulario["CSC_NUM_SISLOC"].Habilitado = True
```
  - SCR_PRESTADOR "UOR do Favorecido" [TextBox String → CP_ORDEM_SERVICO.SCR_PRESTADOR]
**SCR_PRESTADOR.ScriptModificado**
```python
#OrdemServico.SetCustom("SCR", Formulario["SCR_PRESTADOR"].Valor)
```
  - EMAIL_CLIENTE "E-mail do Favorecido" [TextBox String(200) → CP_ORDEM_SERVICO.EMAIL_CLIENTE]
  - TELEFONE_CLIENTE "Telefone do Favorecido" [TextBox String(300) → CP_ORDEM_SERVICO.TELEFONE_CLIENTE]
- Operação PR0001 Preencher Campos
  - NOME_PROJETO "Descrição das despesas Extras:" [TextBox String → CP_ORDEM_SERVICO.NOME_PROJETO]
  - VALOR_TOT_PREST_CONTAS "Valor total a prestar contas" [TextBox Decimal → CPE_CSC.VALOR_TOT_PREST_CONTAS]
  - VALOR_DOD "Valor do reembolso:" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD]
  - VALORTOTALPB "Valor de devolução:" [TextBox Decimal → CPE_PRJ_BB.VALORTOTALPB]
  - VALORTOTSEMCOMPROV "Valor total sem necessidade de comprovação" [TextBox Decimal → CPE_CSC.VALORTOTSEMCOMPROV]
  - STRING_ERP "Descrição dos valores a devolver" [TextBox String → CP_ORDEM_SERVICO.STRING_ERP]
- Associação de subprocesso: AssociacaoId=765; Nome=ADIR CORDEIRO DOS SANTOS FILHO; FraseAssociacao=Deslocamento a Serviço > Prestação de Contas

### [347990] EventoIntermediarioMensagem "Corrigir Prestação de Contas - Deslocamento "
Destinatário: Cliente e Favorecido Deslocamento (papel 1021)
ModeloComunicado: Cobrança Prestação de Contas - Deslocamento 
Corpo do comunicado: Prezado(a),
aguardamos sua prestação de contas referente ao deslocamento realizado no dia OrdemServico.Customizado.SAIDA .
Para realizar a prestação de contas, Link.Edicao Worklist .
Insiras as informações e documentos, salve e clique em avançar. 
Atenciosamente,
Central de Serviços

### [347991] EventoIntermediarioMensagem "Corrigir Prestação de Contas - Deslocamento"
Destinatário: Gerente Favorecido Deslocamento (papel 1020)
ModeloComunicado: Cobrança - Prestação de Contas - Deslocamento
Corpo do comunicado: Prezado(a) Gestor(a)
Informamos que OrdemServico.Customizado.FAVORECIDO_DESLOCAMENTO realizou um deslocamento no dia OrdemServico.Customizado.SAIDA e está pendente da prestação de contas. Pedimos por gentileza, solicitar a finalização da prestação de contas do deslocamento solicitado nesta ordem de Serviço.
Atenciosamente,
Central de Serviços

### [347992] Tarefa "Aprovar Prestação de contas
"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=APROVAR_PRESTACAO
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_DESLOCAMENTO")))
OrdemServico.Favorecido = favorecido
OrdemServico.IniciaAprovacao()
OrdemServico.Salva()
```
**ScriptFormCarregado**
```python
Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado=True
Formulario["VALOR_TOTAL_ADIANTAMENTO"].Visivel=True
```
- Operação PR0002 Aprovar
  - (aprovação) VALOR_REF_REDUZIDA "Valor refeições reduzidas" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_REDUZIDA] — PermiteModificarAprovado=true
  - (aprovação) VALOR_DOD "Valor do reembolso:" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD] — PermiteModificarAprovado=true
  - (aprovação) CSC_VALOR1_TOTAL "Valor das passagens aéreas" [TextBox Decimal → CPE_CSC.CSC_VALOR1_TOTAL] — PermiteModificarAprovado=true
  - (aprovação) PAHL_LOCACOES_CARRO "Locações de Carro" [DataGrid RecordList → Z_00143_PAHL_LOCACOES_CARRO.PAHL_LOCACOES_CARRO] — PermiteModificarAprovado=true
  - (aprovação) CSC_VALOR1 "Valor Diarias Hotel" [TextBox Decimal → CPE_CSC.CSC_VALOR1] — PermiteModificarAprovado=true
  - (aprovação) VALORTOTSEMCOMPROV "Valor total sem necessidade de comprovação" [TextBox Decimal → CPE_CSC.VALORTOTSEMCOMPROV] — PermiteModificarAprovado=true
  - (aprovação) STRING_ERP "Descrição dos valores a devolver" [TextBox String → CP_ORDEM_SERVICO.STRING_ERP] — PermiteModificarAprovado=true
  - (aprovação) VALOR_TOTAL_DIARIA "Valor máximo diaria hotel autorizado" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_DIARIA] — PermiteModificarAprovado=true
  - (aprovação) SIM_NAO2 "Houve gastos não previstos no deslocamento?" [DropDownList String → CPE_CSC.SIM_NAO2] — PermiteModificarAprovado=true
  - (aprovação) TOTAL_COMPLEMENTAR "Total Parcela Complementar (Não é necessário prestar contas)" [TextBox Decimal → CPE_DESLOCAMENTO.TOTAL_COMPLEMENTAR] — PermiteModificarAprovado=true
  - (aprovação) PAHL_VOUCHER_CARRO "Voucher de Locação de Carro" [TextBox String → CPE_CSC.PAHL_VOUCHER_CARRO] — PermiteModificarAprovado=true
  - (aprovação) CIDADE_DESTINO "Destino" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_DESTINO] — PermiteModificarAprovado=true
  - (aprovação) CSC_VALOR2 "Valor Total das Locações de Carro" [TextBox Decimal → CPE_CSC.CSC_VALOR2] — PermiteModificarAprovado=true
  - (aprovação) SAIDA "Saída" [DatePicker DateTime → CPE_DESLOCAMENTO.SAIDA] — PermiteModificarAprovado=true
  - (aprovação) VALOR_TOTAL_ADIANTAMENTO "Valor total do adiantamento ao empregado" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_ADIANTAMENTO] — PermiteModificarAprovado=true
  - (aprovação) VALORTOTALPB "Valor de devolução:" [TextBox Decimal → CPE_PRJ_BB.VALORTOTALPB] — PermiteModificarAprovado=true
  - (aprovação) QUANTIDADE_DIARIA "Quantidade de diarias" [TextBox Integer → CPE_DESLOCAMENTO.QUANTIDADE_DIARIA] — PermiteModificarAprovado=true
  - (aprovação) DESCRICAO_DESPESAS "Outras despesas" [TextBox String(1000) → CPE_DESLOCAMENTO.DESCRICAO_DESPESAS] — PermiteModificarAprovado=true
  - (aprovação) TIPO_HOSPEDAGEM "Tipo de hospedagem  " [DropDownList String → CPE_DESLOCAMENTO.TIPO_HOSPEDAGEM] — PermiteModificarAprovado=true
  - (aprovação) PREVISAO_DISTANCIA_KM "Previsao distancia km" [TextBox Decimal → CPE_DESLOCAMENTO.PREVISAO_DISTANCIA_KM] — PermiteModificarAprovado=true
  - (aprovação) FAVORECIDO_DESLOCAMENTO "Favorecido" [DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO]
  - (aprovação) CIDADE_ORIGEM "Origem" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_ORIGEM] — PermiteModificarAprovado=true
  - (aprovação) MEIO_LOCOMOCAO "Meio de locomoção" [DropDownList String → CPE_DESLOCAMENTO.MEIO_LOCOMOCAO] — PermiteModificarAprovado=true
  - (aprovação) QTD_REFEICAO_INTEGRAL "Quantidade refeições integrais" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_INTEGRAL] — PermiteModificarAprovado=true
  - (aprovação) VALOR_TOT_PREST_CONTAS "Valor total a prestar contas" [TextBox Decimal → CPE_CSC.VALOR_TOT_PREST_CONTAS] — PermiteModificarAprovado=true
  - (aprovação) PARCELA_COMPLEMENTAR "Parcela complementar  " [TextBox Decimal → CPE_DESLOCAMENTO.PARCELA_COMPLEMENTAR] — PermiteModificarAprovado=true
  - (aprovação) VALOR_DESPESAS "Valor de outras despesas" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DESPESAS] — PermiteModificarAprovado=true
  - (aprovação) CUSTO_TOT_DESLOC "Custo total do deslocamento" [TextBox Decimal → CPE_HOMOLOGACAO.CUSTO_TOT_DESLOC] — PermiteModificarAprovado=true
  - (aprovação) QTD_REFEICAO_REDUZIDA "Quantidade refeições reduzidas" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_REDUZIDA] — PermiteModificarAprovado=true
  - (aprovação) DIAS_DE_TRA "Dias de trabalho" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA] — PermiteModificarAprovado=true
  - (aprovação) RETORNO_DIA "Retorno " [DatePicker DateTime → CPE_DESLOCAMENTO.RETORNO_DIA] — PermiteModificarAprovado=true
  - (aprovação) PAH_VOUCHER_HOSPEDAGEM "Voucher Hospedagem" [TextBox String → CPE_CSC.PAH_VOUCHER_HOSPEDAGEM] — PermiteModificarAprovado=true
  - (aprovação) VALOR_DISTANCIA "Valor distância percorrida" [TextBox String → CPE_DESLOCAMENTO.VALOR_DISTANCIA] — PermiteModificarAprovado=true
  - (aprovação) VALOR_REF_INTEGRAL "Valor refeições integrais" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_INTEGRAL] — PermiteModificarAprovado=true
  - (aprovação) VALOR_TOTAL_REFEICAO "Valor total das refeições" [TextBox String → CPE_ORDEM_SERVICO.VALOR_TOTAL_REFEICAO] — PermiteModificarAprovado=true
  - (aprovação) OBJETIVO_VIAGEM "Objetivo viagem" [TextBox String → CPE_DESLOCAMENTO.OBJETIVO_VIAGEM] — PermiteModificarAprovado=true
  - (aprovação) NOME_PROJETO "Descrição das despesas Extras:" [TextBox String → CP_ORDEM_SERVICO.NOME_PROJETO] — PermiteModificarAprovado=true
  - item para aprovação ""
  - aprovador: Prestação de Contas Viagem e Hospedagem - Conforme NI006v.87 (Unico)
- Operação PR0001 Preencher Campos
  - VALOR_TOTAL_ADIANTAMENTO "Valor total do adiantamento R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_ADIANTAMENTO]
  - VALOR_TOT_PREST_CONTAS "Valor total a prestar contas" [TextBox Decimal → CPE_CSC.VALOR_TOT_PREST_CONTAS]
  - Favorecido (nativo)
  - FAVORECIDO_DESLOCAMENTO "Favorecido" [DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO] obrigatório
- Relatorios:
  - FormatoExportacao=PDF

### [347993] EventoIntermediarioMensagem "Cobrança - Prestação de Contas - Deslocamento"
Destinatário: Gerente Favorecido Deslocamento (papel 1020)
ModeloComunicado: Cobrança - Prestação de Contas - Deslocamento
Corpo do comunicado: Prezado(a) Gestor(a)
Informamos que OrdemServico.Customizado.FAVORECIDO_DESLOCAMENTO realizou um deslocamento no dia OrdemServico.Customizado.SAIDA e está pendente da prestação de contas. Pedimos por gentileza, solicitar a finalização da prestação de contas do deslocamento solicitado nesta ordem de Serviço.
Atenciosamente,
Central de Serviços

### [347995] Tarefa "Aguardar viagem"
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno

### [347994] EventoIntermediarioMensagem "Término de serviço"
Destinatário: Cliente e Favorecido Deslocamento (papel 1021)
ModeloComunicado: Término de serviço
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Em atendimento à Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto, comunico que foi realizado o término da atividade pelo Cesec.
Para mais detalhes sobre esta solicitação, clique no link a seguir ==> Link.Consulta.
 Complemento1 
Atenciosamente,
Central de Serviços

### [347996] EventoIntermediarioRegra ""
**Regra**
```python
OrdemServico["FUNCAO_DESLOCAMENTO"] != "GERENTE EXECUTIVO" and OrdemServico["RETORNO_DIA"] <= DateTime.Now
```

## Papéis usados
### papel 508: Fila CSC - Passagens Aéreas e Hospedagem
Tipo=RelacaoPessoas | pessoas: Fila CSC - Passagens Aéreas e Hospedagem
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 1021: Cliente e Favorecido Deslocamento
Tipo=Composto
- composto por: Cliente (PessoaOrdemServico)
- composto por: Favorecido Deslocamento (Script)
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```
### papel 1020: Gerente Favorecido Deslocamento
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_DESLOCAMENTO")))
gestor = favorecidoBBTec.ObtemChefia(False)

if favorecidoBBTec == gestor:
    gestor = gestor.Orgao.OrgaoPai.Gestor

Atores.Adiciona(gestor, "Gerente Favorecido Deslocamento")
```
### papel 461: Fila CSC - Pendente de Aprovação
Tipo=RelacaoPessoas | pessoas: Fila CSC - Pendente de Aprovação
### papel 1005: Prestação de Contas Viagem e Hospedagem - Conforme NI006v.87
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_DESLOCAMENTO")))
#favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.FavorecidoId))
cargoFavorecido = favorecido["CARGO_FUNCIONAL"]
orgaoFavorecido = favorecido.Orgao.Sigla

gestorPosicao = ""
if (cargoFavorecido == "PRESIDENTE" or cargoFavorecido == "DIRETOR" or cargoFavorecido == "ASSESSOR EXECUTIVO PRESIDENCIA" or cargoFavorecido == "MEMBRO COMITE DE AUDITORIA" or cargoFavorecido == "CONSELHEIRO DE ADMINISTRACAO" or cargoFavorecido == "CONSELHEIRO FISCAL") or (cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "3000009200" or orgaoFavorecido == "3000001330" or orgaoFavorecido == "3000009400" or orgaoFavorecido == "3000004052") or (cargoFavorecido == "GERENTE DE PROJETOS I" and orgaoFavorecido == "3000004051" or orgaoFavorecido == "3000004055"):
    uor = Orgao.Carrega("Sigla", "3000009430")
    gestor = uor.Gestor
    aprovador = gestor
#Disec aprovar viagem do Gerente Executivo Gesap
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "3000003402":
        uor = Orgao.Carrega("Sigla", "3000009430")
        gestor = uor.Gestor
        aprovador = gestor
#Dipli aprovar viagem do Gerente Executivo Gesuc
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "3000003401":
        uor = Orgao.Carrega("Sigla", "3000003410")
        gestor = uor.Gestor
        aprovador = gestor
#UNIBBTS aprovar viagem do Gerente Executivo Gepes
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "3000003200":
        uor = Orgao.Carrega("Sigla", "3000003260")
        gestor = uor.Gestor
        aprovador = gestor
#Dipav aprovar viagem do Gerente Executivo Gefic
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "3000003100":
        uor = Orgao.Carrega("Sigla", "3000009350")
        gestor = uor.Gestor
        aprovador = gestor
#Supot aprovar viagem do Gerente Executivo Geape
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "3000008810":
        uor = Orgao.Carrega("Sigla", "3000002050")
        gestor = uor.Gestor
        aprovador = gestor 
#Detic aprovar viagem do Gerente Executivo Getic
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "3000002026":
        uor = Orgao.Carrega("Sigla", "3000002023")
        gestor = uor.Gestor
        aprovador = gestor 
#Govit aprovar viagem do Gerente Executivo Geati
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "3000008800":
        uor = Orgao.Carrega("Sigla", "3000008406")
        gestor = uor.Gestor
        aprovador = gestor
#Difas aprovar viagem do Gerente Executivo Gesed
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "2000008422":
        uor = Orgao.Carrega("Sigla", "2000008260")
        gestor = uor.Gestor
        aprovador = gestor       
#Diarc aprovar viagem do Gerente Executivo Gecob
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "2000008100":
        uor = Orgao.Carrega("Sigla", "2000008110")
        gestor = uor.Gestor
        aprovador = gestor
#Diarb aprovar viagem do Gerente Executivo Gecor
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "2000008300":
        uor = Orgao.Carrega("Sigla", "2000008310")
        gestor = uor.Gestor
        aprovador = gestor       
#Dipre aprovar viagem do Gerente Executivo Gelop
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "2000004039":
        uor = Orgao.Carrega("Sigla", "2000004049")
        gestor = uor.Gestor
        aprovador = gestor              
#Dires aprovar viagem do Gerente Executivo Gered
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "2000004017":
        uor = Orgao.Carrega("Sigla", "2000004019")
        gestor = uor.Gestor
        aprovador = gestor
        
#Direm aprovar viagem do Gerente Executivo Gerel
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO")and orgaoFavorecido == "3000004060":
        uor = Orgao.Carrega("Sigla", "3000004045")
        gestor = uor.Gestor
        aprovador = gestor

#Dipeg aprovar viagem do Gerente Excutivo Gepin
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO")and orgaoFavorecido == "2000004069":
        uor = Orgao.Carrega("Sigla", "2000008253")
        gestor = uor.Gestor
        aprovador = gestor
      
#Dicre aprovar viagem do Gerente Executivo Gecor        
#elif cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "2000008300":
#        uor = Orgao.Carrega("Sigla", "2000008309")
#        gestor = uor.Gestor
#        aprovador = gestor
      
#Auditoria       
else:
    if (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO")and orgaoFavorecido == "4000001110":
        uor = Orgao.Carrega("Sigla", "4000001112")
        gestor = uor.Gestor
        aprovador = gestor
#Demais casos, gestor imediato aprova OS do seu subordinado        
    else:
        gestorid = favorecido.Orgao.GestorId
        gestor = favorecido.Orgao.Gestor
        if gestorid == favorecido.Id:
            gestor = favorecido.Orgao.OrgaoPai.Gestor
        aprovador = gestor



Atores.Adiciona(aprovador, "Alçadas de Aprovação por Posição Viagem e Hospedagem - Conforme NI006v.77")
```

## Campos customizados usados (definição global)

### PAHL_LOCACOES — Locações
CheckBox Boolean → CPE_CSC.PAHL_LOCACOES
Descrição: Locações de Carro

### PAHL_PASSAGENS — Passagens Aéreas
CheckBox Boolean → CPE_CSC.PAHL_PASSAGENS

### PAHL_HOSPEDAGENS — Hospedagens
CheckBox Boolean → CPE_CSC.PAHL_HOSPEDAGENS

### LISTA_DE_OS_ALTCANC_DESLOCAMENTO — OS's de Alteração e Cancelamento
DataGrid RecordList → Z_00143_LISTA_DE_OS_ALTCANC_DESLOCAMENTO.LISTA_DE_OS_ALTCANC_DESLOCAMENTO
Colunas do registro:
- OS "OS" [TextBox String]
- SOLICITACAO "Solicitação" [TextBox String]

### PAH_VOUCHER_HOSPEDAGEM — Voucher de Hospedagem
TextBox String → CPE_CSC.PAH_VOUCHER_HOSPEDAGEM

### PAHL_VOUCHER_CARRO — Voucher de Locação de Carro
TextBox String → CPE_CSC.PAHL_VOUCHER_CARRO

### PAHL_LOCACOES_CARRO — Locações de Carro
DataGrid RecordList → Z_00143_PAHL_LOCACOES_CARRO.PAHL_LOCACOES_CARRO
Colunas do registro:
- CARRO4X4 "4X4 ?" [CheckBox Boolean]
- LOCAL_RETIRADA "Local de Retirada" [TextBox String]
- DATA_HORA_RETIRADA "Data/Hora de Retirada" [DateTimePicker DateTime]
- LOCAL_DEVOLUCAO "Local de Devolução" [TextBox String]
- DATA_HORA_DEVOLUCAO "Data/Hora de Devolução" [DateTimePicker DateTime]
- VALOR_LOCACAO "Valor da Locação" [TextBox Decimal]

### PAHL_NUM_ARGO — Número da OS Argo
TextBox String → CPE_CSC.PAHL_NUM_ARGO

### CSC_VALOR1_TOTAL — Valor Total
TextBox Decimal → CPE_CSC.CSC_VALOR1_TOTAL

### CSC_VALOR1 — Valor
TextBox Decimal → CPE_CSC.CSC_VALOR1

### CSC_VALOR2 — Valor
TextBox Decimal → CPE_CSC.CSC_VALOR2

### TEXT_1 — TEXT_1
TextBox String(1000) → CPE_CSC.TEXT_1

### TEXT2 — TEXT2
TextBox String → CPE_CSC.TEXT2

### NUMERO_OC2 — Número da OC2
TextBox Integer → CPE_CONTRATOS.NUMERO_OC2

### DESCRICAO_DETALHADA — Descrição detalhada
Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA

### CHECKBOX1 — Checkbox1
CheckBox Boolean → CPE_PESSOAS.CHECKBOX1

### TEXT — TEXT
TextBox String(1000) → CPE_CSC.TEXT

### DIAS_DE_TRA — DIAS DE TRAB
TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA
Descrição: DIAS DE TRABALHO

### TIPO_HOSPEDAGEM — Tipo de Hospedagem
DropDownList String → CPE_DESLOCAMENTO.TIPO_HOSPEDAGEM
Itens: Contratada;Avulsa;Avulsa SEM apresentação de NF;Sem Hospedagem

### QUANTIDADE_DIARIA — Quantidade de Diárias
TextBox Integer → CPE_DESLOCAMENTO.QUANTIDADE_DIARIA

### VALOR_DIARIA_AUTORIZADO — Valor Diária Autorizado
TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_AUTORIZADO

### CAMPO_VALIDACAO_DIARIA — Campo de de validação
TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DIARIA

### VALOR_TOTAL_DIARIA — Valor total de diárias R$
TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_DIARIA

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### COTACAO_DOLAR — Cotação do Dólar americano (USD) 
TextBox String → CPE_DESLOCAMENTO.COTACAO_DOLAR

### DIARIA_COTACAO_REAL — Diária em Real
TextBox String → CPE_DESLOCAMENTO.DIARIA_COTACAO_REAL

### NUMERO_NT — Número da Nota Técnica
TextBox String → CPE_CONTRATOS.NUMERO_NT

### PARCELA_COMPLEMENTAR — Parcela Complementar de hospedagem
TextBox Decimal → CPE_DESLOCAMENTO.PARCELA_COMPLEMENTAR

### TOTAL_COMPLEMENTAR — Total Parcela Complementar (Não é necessário prestar contas)
TextBox Decimal → CPE_DESLOCAMENTO.TOTAL_COMPLEMENTAR
Descrição: Total Parcela Complementar

### PREVISAO_DISTANCIA_KM — Previsão de distancia em KM
TextBox Decimal → CPE_DESLOCAMENTO.PREVISAO_DISTANCIA_KM

### VALOR_DISTANCIA — Valor previsto para percorrer distância R$
TextBox String → CPE_DESLOCAMENTO.VALOR_DISTANCIA

### SIM_NAO_REFEICAO — Sim ou Não Refeição
DropDownList String → CPE_DESLOCAMENTO.SIM_NAO_REFEICAO
Itens: Sim;Não

### VALOR_REF_INTEGRAL — Valor Refeição Integral
TextBox String → CPE_DESLOCAMENTO.VALOR_REF_INTEGRAL

### DESCRICAO_DESPESAS — Descrição de outras despesas
TextBox String(1000) → CPE_DESLOCAMENTO.DESCRICAO_DESPESAS

### VALOR_DESPESAS — Valor de outras despesas R$
TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DESPESAS

### VALOR_UTILIZADO_DESLOCAMENTO — Valor Utilizado
TextBox Decimal → CPE_CSC.VALOR_UTILIZADO_DESLOCAMENTO

### VALOR_TOTAL_ADIANTAMENTO — Valor total do adiantamento R$
TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_ADIANTAMENTO

### CIDADE_DESTINO — Cidade de Destino
DropDownList String → CPE_DESLOCAMENTO.CIDADE_DESTINO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT to_char(id_cidade) as id, c.descricao as cidade FROM cidade_v c ORDER BY c.descricao")
```

### CIDADE_CLASSIFICACAO — Cidade Classificação
TextBox String → CPE_CSC.CIDADE_CLASSIFICACAO

### CIDADE_DESTINO_INTERNACIONAL — Cidade/País de Destino
TextBox String → CPE_DESLOCAMENTO.CIDADE_DESTINO_INTERNACIONAL

### PAIS — País
DropDownList String → CPE_DESLOCAMENTO.PAIS
**LookupScript**
```python
#
```

### TIPO_DESTINO — Tipo da localidade de destino
DropDownList String → CPE_DESLOCAMENTO.TIPO_DESTINO
Itens: Capital;Interior

### SAIDA — Saída dia
DatePicker DateTime → CPE_DESLOCAMENTO.SAIDA

### RETORNO_DIA — Retorno dia
DatePicker DateTime → CPE_DESLOCAMENTO.RETORNO_DIA

### SAIDA_HORA — Horário da Saída
TextBox String → CPE_DESLOCAMENTO.SAIDA_HORA

### RETORNO_HORA — Horário do Retorno
TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA

### CHECKBOX10 — Checkbox10
CheckBox Boolean → CPE_PESSOAS.CHECKBOX10

### LISTA_INVIABILIDADE — Lista de Motivos que inviabilizam a videoconferência
DropDownList String → CPE_DESLOCAMENTO.LISTA_INVIABILIDADE
Itens: 0 - Atendimento Técnico;
1 - Auditoria;
2 - Vistoria;
3 - Fiscalização de execução de contrato;
4 - Licitação presencial;
5 - Audiência;
6 - Convocação gerencial;
7 - Saída para compras de material;
8 - Serviços Administrativos (banco, cartório, prefeitura);
9 - Reunião presencial (cliente, fornecedor);
10 - Indisponibilidade de sistema de vídeo conferencia;
11 - Processo interno de seleção;
12 - Contigência;
13 - Plantão;
14 - Manutenção do veículo;
15 - Transferência de Funcionário;
16 - Participação em Projeto

### OBJETIVO_VIAGEM — Objetivo / Informações Adicionais:
TextBox String → CPE_DESLOCAMENTO.OBJETIVO_VIAGEM

### MEIO_LOCOMOCAO — Meio de locomoção principal
DropDownList String → CPE_DESLOCAMENTO.MEIO_LOCOMOCAO
Itens: Avião;Barco;Carro Locado;Carro Próprio;Carro da Frota;Carro por Aplicativo;Metrô;Taxi;Trem;Ônibus Interestadual;Ônibus Intermunicipal;Ônibus Municipal

### VIAGEM_LONGA — Viagem de Longa Distância
DropDownList String → CPE_DESLOCAMENTO.VIAGEM_LONGA
Itens: Até 399km;A partir de 400km

### VALOR_DIFERENCA_DESLOCAMENTO — Valor Diferença
TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DIFERENCA_DESLOCAMENTO

### QTD_REFEICAO_REDUZIDA — Quantidade de refeições reduzidas
TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_REDUZIDA

### VALOR_TOTAL_REFEICAO — Valor total previsto para refeições: R$
TextBox String → CPE_ORDEM_SERVICO.VALOR_TOTAL_REFEICAO

### QTD_REFEICAO_INTEGRAL — Quantidade de Refeições Integrais
TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_INTEGRAL

### VALOR_REF_REDUZIDA — Valor Refeição Reduzida
TextBox String → CPE_DESLOCAMENTO.VALOR_REF_REDUZIDA

### LABEL2 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL2
Descrição: Texto informativo

### CHECKBOX8 — Checkbox8
CheckBox Boolean → CPE_PESSOAS.CHECKBOX8

### CHECKBOX9 — Checkbox9
CheckBox Boolean → CPE_PESSOAS.CHECKBOX9
Descrição: Checkbo9

### LABEL10 — LABEL10
Label String(700) → CPE_PDCI2019.LABEL10

### FAVORECIDO_DESLOCAMENTO — Favorecido
DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### MATRICULA_DESLOCAMENTO — Matrícula
TextBox Integer → CPE_DESLOCAMENTO.MATRICULA_DESLOCAMENTO

### CARGO_DESLOCAMENTO — Cargo
TextBox String → CPE_DESLOCAMENTO.CARGO_DESLOCAMENTO

### FUNCAO_DESLOCAMENTO — Função
TextBox String → CPE_DESLOCAMENTO.FUNCAO_DESLOCAMENTO

### DESC_COLABORADOR_DESLOCAMENTO — Tipo de Colaborador
TextBox String → CPE_DESLOCAMENTO.DESC_COLABORADOR_DESLOCAMENTO

### CELULAR — Celular
TextBox String → CP_ORDEM_SERVICO.CELULAR

### ACOMPANHANDO_GRUPO_A — Estará acompanhando Presidente / Direto / Conselheiro 
DropDownList String → CPE_DESLOCAMENTO.ACOMPANHANDO_GRUPO_A
Itens: Sim;Não

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### NUM_ABERTURA_CHAMADO — N° da Abertura de Chamado do Deslocamento a Serviço de Quem Está Acompanhando
TextBox String → CPE_DESLOCAMENTO.NUM_ABERTURA_CHAMADO

### TIPO_DESLOCAMENTO — Tipo de Deslocamento
DropDownList String → CPE_DESLOCAMENTO.TIPO_DESLOCAMENTO
Itens: Viagem a Serviço - Nacional;Viagem a Serviço - Internacional;Viagem - Assistência Técnica;Treinamento - Assistência Técnica

### CIDADE_ORIGEM — Cidade de Origem
DropDownList String → CPE_DESLOCAMENTO.CIDADE_ORIGEM
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT to_char(id_cidade) as id, c.descricao as cidade FROM cidade_v c ORDER BY c.descricao")
```

### VALOR_DIARIA_DOLAR — Valor Diária US$
TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_DOLAR

### CAMPO_VALIDACAO_DOLAR — Campo de Validação Dolar
TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DOLAR

### DIARIA_AUTORIZADO_INTERNACIONAL — Valor Diária Autorizado US$
TextBox String → CPE_DESLOCAMENTO.DIARIA_AUTORIZADO_INTERNACIONAL

### VALOR_DIARIA — Valor da Diaria R$
TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DIARIA

### SIM_NAO2 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO2
Itens: Sim;Não

### VALOR_DOD — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD
Descrição: Valor do orçamento

### SIM_NAO3 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO3
Descrição: Informe
Itens: Sim;Não

### STRING_ERP — Linha Extra do Comunicado ERP
TextBox String → CP_ORDEM_SERVICO.STRING_ERP
Descrição: Linha Extra do Comunicado "Envio de Senha Geral do Sistema Corporativo" do Serviço ERP

### VALORTOTALPB — Valor Total
TextBox Decimal → CPE_PRJ_BB.VALORTOTALPB

### VALOR_TOT_PREST_CONTAS — Valor total a prestar contas
TextBox Decimal → CPE_CSC.VALOR_TOT_PREST_CONTAS

### CUSTO_TOT_DESLOC — Custo total do deslocamento
TextBox Decimal → CPE_HOMOLOGACAO.CUSTO_TOT_DESLOC

### COMBOBOX_CONFIRMA_TREINAMENTO — Confirmo que o reembolso a ser solicitado se refere a Treinamento Externo por Reembolso
CheckBox Boolean → CPE_PESSOAS.COMBOBOX_CONFIRMA_TREINAMENTO
Descrição: Combobox Confirma Treinamento

### VALORTOTSEMCOMPROV — Valor total sem necessidade de comprovação
TextBox Decimal → CPE_CSC.VALORTOTSEMCOMPROV

### CSC_OBS1 — Observação/Detalhamento
Memo String(2000) → CPE_CSC.CSC_OBS1
Descrição: Observação

### PAH_LOCALIZADORES — Localizador Aereo
DataGrid RecordList → Z_00143_PAH_LOCALIZADORES.PAH_LOCALIZADORES
Colunas do registro:
- VALOR_TRECHO "Valor do trecho" [TextBox Decimal]
- SEQUENCIA "Sequência" [DropDownList Integer] itens: 1;2;3;4;5;6;7;8;9
- CIA_AEREA "Companhia Aerea" [DropDownList String] itens: Azul;Gol;Latam;Passaredo
- LOCALIZADOR "Localizador" [TextBox String]

### CSC_DATA_INICIO — Data Início
DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO

### CSC_DATA_FIM — Data Fim
DatePicker DateTime → CPE_CSC.CSC_DATA_FIM

### DESCRICAO_OBRIG — Descrição obrigatória
TextBox String(2000) → CP_ORDEM_SERVICO.DESCRICAO_OBRIG
Descrição: Breve descrição

### CSC_OBS — Observação
Memo String(2000) → CPE_CSC.CSC_OBS

### DATA_INICIO_AUX1 — Início Auxiliar
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_INICIO_AUX1
Descrição: Data de Início Auxiliiar

### PAH_MOTIVO_SOL — Motivo da Solicitação
DropDownList String → CPE_CSC.PAH_MOTIVO_SOL
Descrição: Tipo de Solicitação de Reserva
Itens: Atendimento técnico;Eventos / Treinamentos;Transferência de Funcionário;Convocação Gerencial;Outros

### RESERVA_DE_VOO — Informações para Reserva de Voo
DataGrid RecordList → Z_00143_RESERVA_DE_VOO.RESERVA_DE_VOO
Descrição: Reserva de Voo
Colunas do registro:
- TRECHO "Trecho" [DropDownList String] itens: Ida;Volta
- SEQUENCIA "Nº do Trecho" [DropDownList Integer] itens: 1;2;3;4;5;6;7;8;9
- CIDADE_ORIGEM "Cidade Origem" [DropDownList String]
**CIDADE_ORIGEM.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT to_char(id_cidade) as id, c.descricao as cidade FROM cidade_v c ORDER BY c.descricao")
```
- AEROPORTO_DESTINO "Aeroporto de Destino" [TextBox String]
- DESPACHO_BAGAGENS "Despacho de Bagagens?" [DropDownList String] itens: Sim;Não
- QUANTIDADE_BAGAGENS "Quantidade de Bagagens" [TextBox Integer]
- AEROPORTO_ORIGEM "Aeroporto de Origem" [TextBox String]
- CIDADE_DESTINO "Cidade de Destino" [DropDownList String]
**CIDADE_DESTINO.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT to_char(id_cidade) as id, c.descricao as cidade FROM cidade_v c ORDER BY c.descricao")
```
- DATA_VOO "Data do Voo" [DatePicker DateTime]
- HORA_ESTIMADA_VOO "Horário Estimado para Voo" [TextBox String]

### RESERVA_DE_VOO_INTERNACIONAL — Informações para Reserva de Voo Internacional
DataGrid RecordList → Z_00143_RESERVA_DE_VOO_INTERNACIONAL.RESERVA_DE_VOO_INTERNACIONAL
Descrição: Reserva de Voo
Colunas do registro:
- SEQUENCIA "Nº do Trecho" [DropDownList Integer] itens: 1;2;3;4;5;6;7;8;9
- TRECHO "Trecho" [DropDownList String] itens: Ida;Volta
- CIDADE_ORIGEM "Cidade Origem" [TextBox String]
- AEROPORTO_ORIGEM "Aeroporto de Origem" [TextBox String]
- CIDADE_DESTINO "Cidade de Destino" [TextBox String]
- AEROPORTO_DESTINO "Aeroporto de Destino" [TextBox String]
- DATA_VOO "Data do Voo" [DatePicker DateTime]
- HORA_ESTIMADA_VOO "Horário Estimado para Voo" [TextBox String]
- DESPACHO_BAGAGENS "Despacho de Bagagens?" [DropDownList String] itens: Sim;Não
- QUANTIDADE_BAGAGENS "Quantidade de Bagagens" [TextBox Integer]

### PAH_DATA_ENTRADA — Data de Entrada
DatePicker DateTime → CPE_CSC.PAH_DATA_ENTRADA

### PAH_DATA_SAIDA — Data de Saída
DatePicker DateTime → CPE_CSC.PAH_DATA_SAIDA

### PAH_EVENTO_HOTEL — Evento no Hotel?
DropDownList String → CPE_CSC.PAH_EVENTO_HOTEL
Descrição: Evento será Realizado no Hotel?
Itens: Sim;Não

### PAH_HOTEL_EVENTO — Hotel do Evento
TextBox String → CPE_CSC.PAH_HOTEL_EVENTO
Descrição: Hotel onde será realizado o evento

### CPF — CPF
TextBox String(15) → CP_ORDEM_SERVICO.CPF

### SCR_PRESTADOR — UOR
TextBox String → CP_ORDEM_SERVICO.SCR_PRESTADOR
Descrição: UOR onde está lotado o prestador de serviço

### EMAIL_CLIENTE — Email do Cliente
TextBox String(200) → CP_ORDEM_SERVICO.EMAIL_CLIENTE

### TELEFONE_CLIENTE — Ramal do Cliente
TextBox String(300) → CP_ORDEM_SERVICO.TELEFONE_CLIENTE

### NOME_PROJETO — Nome do Projeto
TextBox String → CP_ORDEM_SERVICO.NOME_PROJETO

## Biblioteca de scripts referenciada
apiOrdsSV, calculos_deslocamento_v29, teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
