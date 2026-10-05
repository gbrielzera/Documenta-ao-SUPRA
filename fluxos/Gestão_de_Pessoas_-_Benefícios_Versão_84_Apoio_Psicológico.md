# Fluxo: Apoio Psicológico (APOIOPSICOLOGICO) — versão 84
Caminho: Fluxos > Gestão de Pessoas - Benefícios Versão 84 Apoio Psicológico
XML: `XMLs para teste/Gestão_de_Pessoas_-_Benefícios_Versão_84_Apoio_Psicológico.xml` | Supravizio 19.1.1 | SubProcessoId 20100 | DesenhoProcessoId 2818 | ProcessoId 105
Órgão dono: 3000003210 - DIVISAO DE BENEFICIOS E MOVIMENTACOES DE PESSOAL | Responsável: PALOMA SABINE AMADO ROSA
Classe do subprocesso: CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorResponsavel; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Cancelar Agendamento Apoio Psicológico (CANCELARPSICO); Agendamento Apoio Psicológico (AGENDAMENTOPSICO)

## Grafo do fluxo
- [322019] Tarefa "Remover da agenda de consulta por falta de confirmação do cliente." {Fila CSC - Benefícios} → [322035] Atendido com sucesso
- [322020] EventoIntermediarioTimer "Aguarda 72 horas para cliente confirmar a consulta" → [322028] Preenche resposta de não confirmação do cliente.
- [322021] EventoIntermediarioMensagem "Prioridade" → [G73569] Qual a solicitação?
- [322022] Tarefa "Informar nova data disponível para o cliente" {Fila CSC - Benefícios} → [322037] Notificar data disponivel para consulta
- [322023] EventoFinal "Sucesso" {Responsável atual} → (fim)
- [322024] EventoIntermediarioMensagem "E-mail de confirmação de agendamento e orientações gerais --- " → [322036] Sucesso
- [322025] EventoIntermediarioMensagem "Notifica abertura de chamado" → [322027] Informar a data disponível para o cliente
- [322026] LinkInicial "Agendamento Apoio Psicológico" → [322025] Notifica abertura de chamado
- [322027] Tarefa "Informar a data disponível para o cliente" {Fila CSC - Benefícios} → [322037] Notificar data disponivel para consulta
- [322028] Tarefa "Preenche resposta de não confirmação do cliente." {Fila CSC - Benefícios} → [322019] Remover da agenda de consulta por falta de confirm
- [322029] EventoIntermediarioMensagem "Atendido com sucesso" → [322023] Sucesso
- [322030] Tarefa "Informar o de acordo a data disponível para consulta." {Cliente} → [322020] Aguarda 72 horas para cliente confirmar a consulta | [322038] Notifica email a cada 12 horas | [G73571] De acordo?
- [322031] Tarefa "Enviar confirmação de data e horário disponível." {Responsável atual} → [322024] E-mail de confirmação de agendamento e orientações
- [322032] EventoInicial "Início" {Cliente} → [G73570] Está relacionado ao PMI 2025?
- [322033] EventoFinal "Sucesso" {Responsável atual} → (fim)
- [322034] Tarefa "Cancelar agendamento." {Fila CSC - Benefícios} → [322029] Atendido com sucesso
- [322035] EventoIntermediarioMensagem "Atendido com sucesso" → [322033] Sucesso
- [322036] EventoFinal "Sucesso" {Responsável atual} → (fim)
- [322037] EventoIntermediarioMensagem "Notificar data disponivel para consulta" → [322030] Informar o de acordo a data disponível para consul
- [322038] EventoIntermediarioTimer "Notifica email a cada 12 horas" → [322037] Notificar data disponivel para consulta
- [G73569] Gateway "Qual a solicitação?" → «Cancelar» [322034] Cancelar agendamento. | «Agendar» [322027] Informar a data disponível para o cliente
- [G73570] Gateway "Está relacionado ao PMI 2025?" → «Sim» [322021] Prioridade | «Não» [G73569] Qual a solicitação?
- [G73571] Gateway "De acordo?" → «Sim» [322031] Enviar confirmação de data e horário disponível. | «Não» [322022] Informar nova data disponível para o cliente

## Gateways
### [G73569] Qual a solicitação? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla
```
- alternativa → [322034] Cancelar agendamento.: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Cancelar
**ValorComparacaoDecision**
```python
"CANCELARPSICO"
```
- alternativa → [322027] Informar a data disponível para o cliente: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Agendar
**ValorComparacaoDecision**
```python
"AGENDAMENTOPSICO"
```
### [G73570] Está relacionado ao PMI 2025? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["SIM_NAO12"]
```
- alternativa → [322021] Prioridade: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
"Sim"
```
- alternativa → [G73569] Qual a solicitação?: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
"Não"
```
### [G73571] De acordo? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["DE_ACORDO_DATA_PSICO"]
```
- alternativa → [322031] Enviar confirmação de data e horário disponível.: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
"Sim, estou de acordo com a data e horário informado"
```
- alternativa → [322022] Informar nova data disponível para o cliente: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
"Não, solicito outra data e horário"
```

## Atividades

### [322019] Tarefa "Remover da agenda de consulta por falta de confirmação do cliente."
Responsável: Fila CSC - Benefícios (papel 524)

### [322020] EventoIntermediarioTimer "Aguarda 72 horas para cliente confirmar a consulta"
Config: TempoIntervalo=4200

### [322021] EventoIntermediarioMensagem "Prioridade"
Destinatário: Fila CSC - Benefícios (papel 524)
ModeloComunicado: Chamado Prioritário
Corpo do comunicado: Prezado(a),
 Informo que foi aberto o chamado de número OrdemServico.Numero , referente ao fluxo OrdemServico.Assunto . Este chamado está vinculado ao PMI 2025 e, portanto, possui prioridade em relação aos demais chamados que não estão relacionados a esse programa.
 Atenciosamente,
 Central de Serviços

### [322022] Tarefa "Informar nova data disponível para o cliente"
Responsável: Fila CSC - Benefícios (papel 524)
Config: ConfirmaResponsabilidade=true
- Operação PR0001 Preencher Campos
  - AGENDAMENTO_DATA_HORA_PSICO "Agendamento de Data e Hora " [DataGrid RecordList → Z_00143_AGENDAMENTO_DATA_HORA_PSICO.AGENDAMENTO_DATA_HORA_PSICO] obrigatório — QtdColunasFormulario=1
    - coluna DATA obrigatório
    - coluna HORA obrigatório

### [322023] EventoFinal "Sucesso"
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [322024] EventoIntermediarioMensagem "E-mail de confirmação de agendamento e orientações gerais --- "
Destinatário: Cliente (papel 18)
ModeloComunicado: Chamado atendido com sucesso - Apoio nutricional
Corpo do comunicado: Prezado,
A Ordem de Serviço nº OrdemServico.Numero sobre o Assunto: Apoio Nutricional
Para maiores informações Link.Consulta .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
#consultaLista = DB.ExecuteDataTable("select agendamento.DATA, agendamento.HORA from Z_00143_AGENDAMENTO_DATA_HORA_PSICO agendamento where ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
#
#respostaVerificacao = ""
#
#for agendamento in consultaLista.Rows:
#    respostaVerificacao = respostaVerificacao+"<tr><td>"+agendamento["DATA"].ToString("dd/MM/yyyy")+"</td>"+"<td>"+agendamento["HORA"].ToString()+"</td></tr>"
#    
#    
#Mensagem.Complemento1 = "<table><tr><th>Data</th><th>Hora</th></tr>"+respostaVerificacao+"</table>"
```

### [322025] EventoIntermediarioMensagem "Notifica abertura de chamado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Aviso de abertura de chamado
Corpo do comunicado: Prezado(a),
Foi aberta a ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [322026] LinkInicial "Agendamento Apoio Psicológico"
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - FAVORECIDO_TODOS "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
**FAVORECIDO_TODOS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario["FAVORECIDO_TODOS"].Valor != "" and Formulario["FAVORECIDO_TODOS"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_TODOS"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        orgaoFavorecido = favorecidoCustom.OrgaoId
        Formulario["SCR_PRESTADOR"].Valor = favorecidoCustom.Orgao.Descricao.ToString()
        Formulario["MATRICULA"].Valor = favorecidoCustom["MATRICULA"].ToString()
```
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA] obrigatório
  - TELEFONE_ATUALIZADO "Nº Telefone - WhatsApp" [TextBox String → CPE_CSC.TELEFONE_ATUALIZADO]
  - DescricaoDetalhada (nativo) "Escreva os dias e horários de preferência." obrigatório
  - OPCOES_ATENDIMENTO "Selecione um canal de atendimento" [DropDownList String → CPE_CSC.OPCOES_ATENDIMENTO] obrigatório
**OPCOES_ATENDIMENTO.ScriptModificado**
```python
if Formulario["OPCOES_ATENDIMENTO"].Valor == "WhatsApp":
    Formulario["TELEFONE_ATUALIZADO"].Visivel = True
    
if Formulario["OPCOES_ATENDIMENTO"].Valor != "WhatsApp":
    Formulario["TELEFONE_ATUALIZADO"].Visivel = False
```
- Associação de subprocesso: AssociacaoId=566; FraseAssociacao=Chatbot ->  Agendamento Apoio Psicológico; Nome=CHATBOTAGENDPSICO

### [322027] Tarefa "Informar a data disponível para o cliente"
Responsável: Fila CSC - Benefícios (papel 524)
Config: ConfirmaResponsabilidade=true
- Operação PR0001 Preencher Campos
  - AGENDAMENTO_DATA_HORA_PSICO "Agendamento de Data e Hora " [DataGrid RecordList → Z_00143_AGENDAMENTO_DATA_HORA_PSICO.AGENDAMENTO_DATA_HORA_PSICO] obrigatório — QtdColunasFormulario=1
    - coluna DATA obrigatório
    - coluna HORA obrigatório

### [322028] Tarefa "Preenche resposta de não confirmação do cliente."
Responsável: Fila CSC - Benefícios (papel 524)
Config: ConfirmaResponsabilidade=true
**ScriptInicio**
```python
OrdemServico["DE_ACORDO_DATA_PSICO"] = "Consulta não confirmada pelo cliente"

AvancaProximaAtividade = True
```
**ScriptFormCarregado**
```python
Formulario["DE_ACORDO_DATA_PSICO"].Itens = "Consulta não confirmada pelo cliente"
```
- Operação PR0001 Preencher Campos
  - DE_ACORDO_DATA_PSICO "De acordo a data de consulta - Agendamento Apoio Psicológico" [DropDownList String → CPE_CSC.DE_ACORDO_DATA_PSICO] obrigatório
**DE_ACORDO_DATA_PSICO.ScriptModificado**
```python
if Formulario["DE_ACORDO_DATA_PSICO"].Valor == "Sim, estou de acordo com a data e horário informado":
    Formulario["DESCRICAODETALHADA"].Visivel = False
    Formulario["DESCRICAODETALHADA"].Habilitado = False
    
if Formulario["DE_ACORDO_DATA_PSICO"].Valor == "Não, solicito outra data e horário":
    Formulario["DESCRICAODETALHADA"].Visivel = True
    Formulario["DESCRICAODETALHADA"].Habilitado = True
```
  - DescricaoDetalhada (nativo) "Observação com dias e horários de sua preferência." obrigatório

### [322029] EventoIntermediarioMensagem "Atendido com sucesso"
Destinatário: Cliente (papel 18)
ModeloComunicado: Chamado atendido com sucesso - Apoio nutricional
Corpo do comunicado: Prezado,
A Ordem de Serviço nº OrdemServico.Numero sobre o Assunto: Apoio Nutricional
Para maiores informações Link.Consulta .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = "Seu agendamento ao Apoio psicológico referente a data " + OrdemServico["DATA_PARA_CANCELAMENTO"].ToString() + " foi cancelada como solicitado."
```

### [322030] Tarefa "Informar o de acordo a data disponível para consulta."
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
**ScriptFormCarregado**
```python
Formulario["DESCRICAODETALHADA"].Valor = ""
Formulario["DESCRICAODETALHADA"].Visivel = False
Formulario["DESCRICAODETALHADA"].Habilitado = False
Formulario["DE_ACORDO_DATA_PSICO"].Valor = ""
```
- Operação PR0001 Preencher Campos
  - DE_ACORDO_DATA_PSICO "De acordo a data de consulta - Agendamento Apoio Psicológico" [DropDownList String → CPE_CSC.DE_ACORDO_DATA_PSICO] obrigatório
**DE_ACORDO_DATA_PSICO.ScriptModificado**
```python
if Formulario["DE_ACORDO_DATA_PSICO"].Valor == "Sim, estou de acordo com a data e horário informado":
    Formulario["DESCRICAODETALHADA"].Visivel = False
    Formulario["DESCRICAODETALHADA"].Habilitado = False
    
if Formulario["DE_ACORDO_DATA_PSICO"].Valor == "Não, solicito outra data e horário":
    Formulario["DESCRICAODETALHADA"].Visivel = True
    Formulario["DESCRICAODETALHADA"].Habilitado = True
```
  - DescricaoDetalhada (nativo) "Observação com dias e horários de sua preferência." obrigatório
  - AGENDAMENTO_DATA_HORA_PSICO "Agendamento de Data e Hora " [DataGrid RecordList → Z_00143_AGENDAMENTO_DATA_HORA_PSICO.AGENDAMENTO_DATA_HORA_PSICO] obrigatório
    - coluna DATA obrigatório
    - coluna HORA obrigatório

### [322031] Tarefa "Enviar confirmação de data e horário disponível."
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - AGENDAMENTO_DATA_HORA_PSICO "Data disponível para consulta" [DataGrid RecordList → Z_00143_AGENDAMENTO_DATA_HORA_PSICO.AGENDAMENTO_DATA_HORA_PSICO] obrigatório
    - coluna DATA obrigatório
    - coluna HORA obrigatório

### [322032] EventoInicial "Início"
Responsável: Cliente (papel 18)
TipoSolicitacao: 20.01. Gestão de Pessoas - Benefícios
**ScriptValidacao**
```python
if OrdemServico["OPCOES_ATENDIMENTO"] == "WhatsApp" and OrdemServico["TELEFONE_ATUALIZADO"] == "":
    Criticas.AdicionaPendencia("Para consultas via WhatsApp o telefone é obrigatório.")
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Processo.Custom import Gateway
Formulario["TELEFONE_ATUALIZADO"].Visivel = False
Formulario["DATA_PARA_CANCELAMENTO"].Visivel=False
Formulario["DATA_PARA_CANCELAMENTO"].Habilitado=False

Formulario['SIM_NAO1'].Itens = 'Sim;Não'
Formulario['SIM_NAO2'].Itens = 'Liliane dos Santos;Luiz Henrique'

#Formulario['SIM_NAO2'].Habilitado =  False
#Formulario['SIM_NAO2'].Visivel =  False

Formulario["SIM_NAO12"].Habilitado = False

Formulario['GRAU_PARENTE'].Habilitado =  False
Formulario['GRAU_PARENTE'].Visivel =  False
    

if OrdemServico.Servico.Sigla == "CANCELARPSICO":
    Formulario["DATA_PARA_CANCELAMENTO"].Visivel=True
    Formulario["DATA_PARA_CANCELAMENTO"].Habilitado=True

    Formulario["LABEL1"].Visivel=False
    Formulario["LABEL2"].Visivel=False
    Formulario["OPCOES_ATENDIMENTO"].Visivel=False
    Formulario["TELEFONE_ATUALIZADO"].Visivel=False
    Formulario["DESCRICAODETALHADA"].Visivel=False
    
    Formulario["LABEL1"].Habilitado=False
    Formulario["LABEL2"].Habilitado=False
    Formulario["OPCOES_ATENDIMENTO"].Habilitado=False
    Formulario["TELEFONE_ATUALIZADO"].Habilitado=False
    Formulario["DESCRICAODETALHADA"].Habilitado=False
    
# Desativa a parte do PMI 2025 caso tenha finalizado os 3 meses determinados
#ATENÇÃO!!! EM CASO DE ABERTURA DE CHAMADO PARA ESTA ALTERAÇÃO, LEMBRAR DE REMOVER O Gateway

#datainicio = "01/06/2025 10:59:59"
#datafim = "30/09/2025 23:59:59"
#if OrdemServico.DataHoraCriacao.ToString() > datainicio and OrdemServico.##DataHoraCriacao.ToString() < datafim:
#    Formulario["SIM_NAO12"].Habilitado = True
#    Formulario["SIM_NAO12"].Visivel = True
#else:
#    Formulario["SIM_NAO12"].Habilitado = False
#    Formulario["SIM_NAO12"].Visivel = True
#    Formulario["SIM_NAO12"].Valor = "Não"

#Recomendação ao Solicitante
Formulario["LABEL4"].Valor = '<html><head><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><link rel="icon" type="image/x-icon" href=""><style>.forma {text-shadow: 2px 2px #e9f507;}</style></head><body><div class="forma"><justify><font color="#1f05b3" size="3"><p><font size="6"><i class="fa fa-cogs fa-fw"></i></font>&nbsp;&nbsp;<b>Informações necessárias para o atendimento da Ordem de Serviço.</div></b></p><b>Caro solicitante,</b><br>Informe detalhadamente os dados necessários nos campos abaixo para a solicitação pretendida.</font></justify><br><br></body></html>'

#Label Acesso doc
Formulario["LABEL5"].Valor = '<a href="https://bbts.docnix.com.br/bbts/corporate/index.html#/maxdoc/link/documento/1707" target="_blank"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><i class="fa fa-download" style="font-size:36px"></i>&nbsp;<b>Acessar PRO192-001</b></a><br><br>'
```
- Operação PR0001 Preencher Campos
  - LABEL5 "Texto Informativo" [Label String(1024) → CPE_ORDEM_SERVICO.LABEL5] obrigatório
  - LABEL2 "<div style="color: red"><b>*Os atendimentos são realizados no periodo matutino e vespertino.</b></div>" [Label String(2000) → CP_ORDEM_SERVICO.LABEL2] obrigatório
  - LABEL1 "<div style="color: red"><b>É permitido a solicitação para funcionários Cedidos BBTS, Cedidos BB, Afastados e Estagiários. </b></div>" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - LABEL3 "<div style="color: red"><b>*Acompanhe seu e-mail. Você receberá a solicitação de confirmação da consulta em breve.</b></div>" [Label String(1024) → CP_ORDEM_SERVICO.LABEL3] obrigatório
  - LABEL107 "<p style="color: red; font-weight: bold;">*Os chamados relacionados ao PMI 2025 terão prioridade em relação aos demais.</p>" [Label String(1000) → CPE_CONTRATOS.LABEL107] obrigatório
  - FAVORECIDO_TODOS "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
**FAVORECIDO_TODOS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
import peopleSoft
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

if Formulario["FAVORECIDO_TODOS"].Valor != "" and Formulario["FAVORECIDO_TODOS"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_TODOS"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        orgaoFavorecido = favorecidoCustom.OrgaoId
        Formulario["SCR_PRESTADOR"].Valor = favorecidoCustom.Orgao.Descricao.ToString()
        Formulario["MATRICULA"].Valor = favorecidoCustom["MATRICULA"].ToString()
        
# --- PMI

matricula = Formulario["MATRICULA"].Valor.ToString()
pmi = consultaPMI(matricula)

if pmi == 'Y':
    Formulario["SIM_NAO12"].Valor = "Sim"
    Formulario["SIM_NAO12"].Habilitado = False
elif pmi == 'N':
    Formulario["SIM_NAO12"].Valor = "Não"
    Formulario["SIM_NAO12"].Habilitado = False
else:
    Formulario["SIM_NAO12"].Valor = "Não"
    Formulario["SIM_NAO12"].Habilitado = False
```
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA] obrigatório
  - SCR_PRESTADOR "UOR" [TextBox String → CP_ORDEM_SERVICO.SCR_PRESTADOR] obrigatório
  - OPCOES_ATENDIMENTO "Selecione um canal de atendimento" [DropDownList String → CPE_CSC.OPCOES_ATENDIMENTO] obrigatório
**OPCOES_ATENDIMENTO.ScriptModificado**
```python
if Formulario["OPCOES_ATENDIMENTO"].Valor == "WhatsApp":
    Formulario["TELEFONE_ATUALIZADO"].Visivel = True
    
if Formulario["OPCOES_ATENDIMENTO"].Valor != "WhatsApp":
    Formulario["TELEFONE_ATUALIZADO"].Visivel = False
```
  - TELEFONE_ATUALIZADO "Nº Telefone - WhatsApp" [TextBox String → CPE_CSC.TELEFONE_ATUALIZADO]
  - DATA_PARA_CANCELAMENTO "Data para cancelamento" [DateTimePicker DateTime → CPE_CSC.DATA_PARA_CANCELAMENTO] obrigatório
  - LABEL4 "LABEL4" [Label String(1024) → CPE_PDCI2019.LABEL4] obrigatório
  - SIM_NAO1 "Primeira consulta?" [DropDownList String → CPE_CSC.SIM_NAO1] obrigatório
**SIM_NAO1.ScriptModificado**
```python
if Formulario['SIM_NAO1'].Valor == 'Não':
    Formulario["SIM_NAO12"].Habilitado = False
    Formulario['SIM_NAO2'].Visivel =  True
    
else:
    Formulario['SIM_NAO2'].Habilitado =  True
    Formulario['SIM_NAO2'].Visivel =  False
    
# Desativa a parte do PMI 2025 caso tenha finalizado os 3 meses determinados
#datainicio = "01/05/2025 10:59:59"
#datafim = "30/09/2025 23:59:59"
#if OrdemServico.DataHoraCriacao.ToString() > datainicio and OrdemServico.DataHoraCriacao.ToString() < datafim:
#    Formulario["SIM_NAO12"].Habilitado = True
#    Formulario["SIM_NAO12"].Visivel = True
#else:
#    Formulario["SIM_NAO12"].Habilitado = False
#    Formulario["SIM_NAO12"].Visivel = True
#    Formulario["SIM_NAO12"].Valor = "Não"
```
  - SIM_NAO2 "Com qual psicóloga você faz acompanhamento?" [DropDownList String → CPE_CSC.SIM_NAO2] obrigatório
  - SIM_NAO12 "Empregado PMI" [DropDownList String → CPE_CONTRATOS.SIM_NAO12] obrigatório
**SIM_NAO12.ScriptModificado**
```python
Formulario["GRAU_PARENTE"].Visivel = False
Formulario["GRAU_PARENTE"].Habilitado = False
Formulario["SIM_NAO12"].Habilitado = False



if Formulario["SIM_NAO12"].Valor == "Sim":
    Formulario["GRAU_PARENTE"].Visivel = True
    Formulario["GRAU_PARENTE"].Habilitado = True
    Formulario["SIM_NAO12"].Habilitado = False

else:
    Formulario["GRAU_PARENTE"].Visivel = False
    Formulario["GRAU_PARENTE"].Habilitado = False
    Formulario["SIM_NAO12"].Habilitado = False
```
  - GRAU_PARENTE "Dados dos parentes que residem com o funcionário" [DataGrid RecordList → Z_00143_GRAU_PARENTE.GRAU_PARENTE] obrigatório — QtdColunasFormulario=1
    - coluna PARENTE_NOME obrigatório
    - coluna PARENTE_GRAUS obrigatório
  - DescricaoDetalhada (nativo) "Escreva os dias e horários de preferência." obrigatório

### [322033] EventoFinal "Sucesso"
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [322034] Tarefa "Cancelar agendamento."
Responsável: Fila CSC - Benefícios (papel 524)
Config: ConfirmaResponsabilidade=true

### [322035] EventoIntermediarioMensagem "Atendido com sucesso"
Destinatário: Cliente (papel 18)
ModeloComunicado: Chamado atendido com sucesso - Apoio nutricional
Corpo do comunicado: Prezado,
A Ordem de Serviço nº OrdemServico.Numero sobre o Assunto: Apoio Nutricional
Para maiores informações Link.Consulta .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = "Devido a não confirmação do Agendamento ao Apoio psicológico, por parte do favorecido "+ OrdemServico.Cliente.Nome +", não haverá consulta."
```

### [322036] EventoFinal "Sucesso"
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [322037] EventoIntermediarioMensagem "Notificar data disponivel para consulta"
Destinatário: Cliente (papel 18)
ModeloComunicado: Data disponivel para consulta - Agendamento Apoio Psicológico
Corpo do comunicado: Prezado(a),
Segue Data(s) e horário(s) agendados Complemento1 
Gentileza avaliar e confirmar sua participação pelo link abaixo.
 Link.Edicao 
Atenciosamente
Central de Serviços
**ScriptEvento**
```python
consultaLista = DB.ExecuteDataTable("select agendamento.DATA, agendamento.HORA from Z_00143_AGENDAMENTO_DATA_HORA_PSICO agendamento where ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")

respostaVerificacao = ""

for agendamento in consultaLista.Rows:
    respostaVerificacao = respostaVerificacao+"<tr><td>"+agendamento["DATA"].ToString("dd/MM/yyyy")+"</td>"+"<td>"+agendamento["HORA"].ToString()+"</td></tr>"
    
    
Mensagem.Complemento1 = "<table><tr><th>Data</th><th>Hora</th></tr>"+respostaVerificacao+"</table>"
```

### [322038] EventoIntermediarioTimer "Notifica email a cada 12 horas"
Config: TempoIntervalo=720

## Papéis usados
### papel 524: Fila CSC - Benefícios
Tipo=RelacaoPessoas | pessoas: Fila CSC - Benefícios
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
pessoa = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))
atores = OrdemServico.ObtemAtoresProcesso('Fila CSC - Benefícios')
for ator in atores:
    if ator != pessoa:
        Atores.Adiciona(ator)
```
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```

## Campos customizados usados (definição global)

### AGENDAMENTO_DATA_HORA_PSICO — Agendamento de Data e Hora 
DataGrid RecordList → Z_00143_AGENDAMENTO_DATA_HORA_PSICO.AGENDAMENTO_DATA_HORA_PSICO
Colunas do registro:
- DATA "Data" [DatePicker DateTime]
- HORA "Hora" [TextBox String]

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### MATRICULA — Matrícula
TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA

### TELEFONE_ATUALIZADO — Telefone2
TextBox String → CPE_CSC.TELEFONE_ATUALIZADO

### OPCOES_ATENDIMENTO — Selecione um canal de atendimento
DropDownList String → CPE_CSC.OPCOES_ATENDIMENTO
Itens: Teams;WhatsApp;Presencial (Exclusivo para empregados em Brasília)

### DE_ACORDO_DATA_PSICO — De acordo a data de consulta - Agendamento Apoio Psicológico
DropDownList String → CPE_CSC.DE_ACORDO_DATA_PSICO
Itens: Sim, estou de acordo com a data e horário informado;Não, solicito outra data e horário

### LABEL5 — Texto Informativo
Label String(1024) → CPE_ORDEM_SERVICO.LABEL5

### LABEL2 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL2
Descrição: Texto informativo

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### LABEL3 — Texto Informativo
Label String(1024) → CP_ORDEM_SERVICO.LABEL3

### LABEL107 — LABEL107
Label String(1000) → CPE_CONTRATOS.LABEL107

### SCR_PRESTADOR — UOR
TextBox String → CP_ORDEM_SERVICO.SCR_PRESTADOR
Descrição: UOR onde está lotado o prestador de serviço

### DATA_PARA_CANCELAMENTO — Data para cancelamento
DateTimePicker DateTime → CPE_CSC.DATA_PARA_CANCELAMENTO

### LABEL4 — LABEL4
Label String(1024) → CPE_PDCI2019.LABEL4

### SIM_NAO1 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO1
Itens: Sim;Não

### SIM_NAO2 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO2
Itens: Sim;Não

### SIM_NAO12 — Sim ou Não
DropDownList String → CPE_CONTRATOS.SIM_NAO12
Itens: Sim;
Não

### GRAU_PARENTE — Dados dos parentes que residem com o funcionário
DataGrid RecordList → Z_00143_GRAU_PARENTE.GRAU_PARENTE
Descrição: GRAU_PARENTE
Colunas do registro:
- PARENTE_NOME "Nome do(a) Parente" [TextBox String]
- PARENTE_GRAUS "Grau do(a) Parente" [DropDownList String] itens: 1º grau; 2º grau; 3º grau; 4º grau

## Biblioteca de scripts referenciada
peopleSoft, teste
(fonte em catalogo/biblioteca/<Nome>.py)
