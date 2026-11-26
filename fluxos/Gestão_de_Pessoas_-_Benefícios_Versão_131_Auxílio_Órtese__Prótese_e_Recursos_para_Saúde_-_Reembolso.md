# Fluxo: Auxílio Órtese, Prótese e Recursos para Saúde - Reembolso (AUXPCDRBS) — versão 131
Caminho: Fluxos > Gestão de Pessoas - Benefícios Versão 131 Auxílio Órtese, Prótese e Recursos para Saúde - Reembolso
XML: `XMLs para teste/Gestão_de_Pessoas_-_Benefícios_Versão_131_Auxílio_Órtese,_Prótese_e_Recursos_para_Saúde_-_Reembolso.xml` | Supravizio 19.1.1 | SubProcessoId 29028 | DesenhoProcessoId 2776 | ProcessoId 105
Órgão dono: 3000003210 - DIVISAO DE BENEFICIOS E MOVIMENTACOES DE PESSOAL | Responsável: PALOMA SABINE AMADO ROSA VARGAS
Classe do subprocesso: Objetivo=Auxílio Órtese, Prótese e Recursos para Saúde - Reembolso; DescricaoCliente=Auxílio Órtese, Prótese e Recursos para Saúde - Reembolso; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Auxílio órtese, Prótese e Recursos para Saúde - Reembolso; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Auxílio Órtese e Prótese (APARELHOAUDITIVO)

## Grafo do fluxo
- [442209] EventoIntermediarioMensagem "Devolulção para Ajustes" → [442214] Corrigir Informações do Anexo
- [442210] FimCancelamento "" → (fim)
- [442211] Tarefa "Informar Motivo da Reprovação" {Responsável atual} → [442209] Devolulção para Ajustes
- [442212] Tarefa "Verificar Solicitação
" {Fila CSC - Benefícios} → [G95664] Dados OK?
- [442213] EventoIntermediarioMensagem "Resposta Solicitação Reprovada" → [442210] 
- [442214] Tarefa "Corrigir Informações do Anexo" {Cliente} → [442216]  | [442212] Verificar Solicitação

- [442215] EventoInicial "" → [442212] Verificar Solicitação

- [442216] EventoIntermediarioTimer "" → [442213] Resposta Solicitação Reprovada
- [442217] EventoFinal "" {Responsável atual} → (fim)
- [442218] EventoIntermediarioMensagem "Término de serviço" → [442217] 
- [442219] Tarefa "Liberar Pagamento na Conta do Empregado" {Fila CSC - Benefícios} → [442218] Término de serviço
- [442220] Tarefa "Verificar Reprovação" {Fila CSC - Benefícios} → [G95666] Devolver Para O  Demandante?
- [442221] Tarefa "Aprovar Solicitação" {Responsável atual} → [G95665] Aprovou?

- [442222] EventoIntermediarioMensagem "Verificar Reprovação" → [442220] Verificar Reprovação
- [G95664] Gateway "Dados OK?" → «Não» [442211] Informar Motivo da Reprovação | «Sim» [442221] Aprovar Solicitação
- [G95665] Gateway "Aprovou?
" → «Reprovado» [442222] Verificar Reprovação | «Aprovado» [442219] Liberar Pagamento na Conta do Empregado
- [G95666] Gateway "Devolver Para O  Demandante?" → «Não» [442221] Aprovar Solicitação | «Sim» [442214] Corrigir Informações do Anexo

## Gateways
### [G95664] Dados OK? (EventBasedExclusiveDecision)
- alternativa → [442211] Informar Motivo da Reprovação: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
- alternativa → [442221] Aprovar Solicitação: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
### [G95665] Aprovou?
 (DataBasedExclusiveDecision)
Codigo=A
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("AS")
```
- alternativa → [442222] Verificar Reprovação: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
- alternativa → [442219] Liberar Pagamento na Conta do Empregado: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
### [G95666] Devolver Para O  Demandante? (EventBasedExclusiveDecision)
Codigo=DEVOLVER
- alternativa → [442221] Aprovar Solicitação: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
- alternativa → [442214] Corrigir Informações do Anexo: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1

## Atividades

### [442209] EventoIntermediarioMensagem "Devolulção para Ajustes"
Destinatário: Cliente (papel 18)
ModeloComunicado: CSC Gestão de Pessoas - Benefícios - Devolução para ajustes
Corpo do comunicado: OrdemServico.Cliente.Nome,
A Ordem de Serviço número OrdemServico.Numero - Reembolso OrdemServico.Servico foi enviada pelo Cesec para sua responsabilidade para ajustes e/ou correções.
Motivos da devolução: OrdemServico.Customizado.RESPOSTA_REPROVACAO_REEMBOLSO
Após ajustes, clique no botão avançar na interface Workspace para o Cesec continuar com o reembolso.
IMPORTANTE: Caso esse(s) ajuste(s) não seja(m) realizado(s) dentro do prazo de 10 (dez) dias corridos, a Ordem de Serviço será FINALIZADA automaticamente.
Para ajustá-la, acesse a aplicação Supravizio e consulte a solicitação via tela Workspace através do link abaixo:
Edição Cliente Worklist: Link.Edicao Worklist 
Edição Cliente: Link.E…

### [442210] FimCancelamento ""

### [442211] Tarefa "Informar Motivo da Reprovação"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Anexo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - Justificativa (nativo) "Justificativa da devolução" obrigatório

### [442212] Tarefa "Verificar Solicitação
"
Responsável: Fila CSC - Benefícios (papel 524)
Config: ConfirmaResponsabilidade=true
- Operação PR0001 Preencher Campos
  - FAVORECIDO_TODOS "Nome do Beneficiário" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
  - SIM_NAO "O empregado favorecido está afastado?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
if Formulario["SIM_NAO"].Valor != None:
    Formulario["COMBOBOX"].Habilitado = True
    
if Formulario["Valor"].Valor != None:
    if Formulario["VALOR"].Valor >= 20000:
        Formulario["VALOR_TOTAL"].Valor = 20000
    elif Formulario["SIM_NAO"].Valor == "Sim":
        Formulario["VALOR_TOTAL"].Valor = 0.9 * Formulario["VALOR"].Valor
    else:
        Formulario["VALOR_TOTAL"].Valor = Formulario["VALOR"].Valor
    Formulario["VALOR_AUTORIZADO"].Valor = 0.01 * Formulario["VALOR_TOTAL"].Valor
```
  - COMBOBOX "Tipo de Equipamento" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
**COMBOBOX.ScriptModificado**
```python
if Formulario["COMBOBOX"].Valor != None:
    Formulario["TEXT"].Habilitado = True
```
  - TEXT "Nome do Equipamento (ex: muleta, cadeira de rodas ...)" [TextBox String(1000) → CPE_CSC.TEXT] obrigatório
**TEXT.ScriptModificado**
```python
if Formulario["TEXT"].Valor != None:
    Formulario["VALOR"].Habilitado = True
```
  - VALOR "Valor do Equipamento" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
**VALOR.ScriptModificado**
```python
ben = Convert.ToDecimal(Formulario["VALOR"].Valor)

if Formulario["VALOR"].Valor != None:
    Formulario["VALOR_REEMBOLSO"].Valor = ben * 0.9
```
  - VALOR_REEMBOLSO "Valor do Reembolso" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO] obrigatório

### [442213] EventoIntermediarioMensagem "Resposta Solicitação Reprovada"
Destinatário: Cliente e Favorecido Cobra (papel 312)
ModeloComunicado: Resposta da Solicitação de Reembolso - Reprovação
Corpo do comunicado: Prezado(a),
Por não atendimento a NI 102 a sua solitação de Número OrdemServico.Numero - Reembolso OrdemServico.Servico foi indeferida pelo motivo abaixo: 
OrdemServico.Customizado.RESPOSTA_REPROVACAO_REEMBOLSO 
Para mais detalhes sobre esta solicitação Link.Consulta.
Atenciosamente
Central de Serviços

### [442214] Tarefa "Corrigir Informações do Anexo"
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
- Operação PR0004 Associar Itens Configuração
  - anexo "Comprovante de pagamento (Nota Fiscal/Cupom Fiscal)" classes: Comprovante de pagamento — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Laudo Médico Específico Comprovando Necessidade de Aparelho Auditivo" classes: Laudo Médico — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "FQ110-001" classes: Anexo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - COMBOBOX "Tipo de Equipamento" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
**COMBOBOX.ScriptModificado**
```python
if Formulario["COMBOBOX"].Valor != None:
    Formulario["TEXT"].Habilitado = True
```
  - TEXT "Nome do Equipamento (ex: muleta, cadeira de rodas ...)" [TextBox String(1000) → CPE_CSC.TEXT] obrigatório
**TEXT.ScriptModificado**
```python
if Formulario["TEXT"].Valor != None:
    Formulario["VALOR"].Habilitado = True
```
  - VALOR "Valor do Equipamento" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
**VALOR.ScriptModificado**
```python
ben = Convert.ToDecimal(Formulario["VALOR"].Valor)

if Formulario["VALOR"].Valor != None:
    Formulario["VALOR_REEMBOLSO"].Valor = ben * 0.9
```
  - VALOR_REEMBOLSO "Valor do Reembolso" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO] obrigatório
  - FAVORECIDO_TODOS "Nome do Beneficiário" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
  - SIM_NAO "O empregado favorecido está afastado?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
if Formulario["SIM_NAO"].Valor != None:
    Formulario["COMBOBOX"].Habilitado = True
    
if Formulario["Valor"].Valor != None:
    if Formulario["VALOR"].Valor >= 20000:
        Formulario["VALOR_TOTAL"].Valor = 20000
    elif Formulario["SIM_NAO"].Valor == "Sim":
        Formulario["VALOR_TOTAL"].Valor = 0.9 * Formulario["VALOR"].Valor
    else:
        Formulario["VALOR_TOTAL"].Valor = Formulario["VALOR"].Valor
    Formulario["VALOR_AUTORIZADO"].Valor = 0.01 * Formulario["VALOR_TOTAL"].Valor
```

### [442215] EventoInicial ""
Config: Configuracao={"ServicoIniciador":"APARELHOAUDITIVO"}
TipoSolicitacao: 20.01. Gestão de Pessoas - Benefícios
**ScriptValidacao**
```python
#anos_carencia = 1
#data_limite_5anos = DateTime.Now.AddYears(-5)
#
## 1) Regra de carência (última solicitação do mesmo tipo)
#sql_ultima = "select max(os.DATA_HORA_FIM_REAL) as ULTIMA from OCORRENCIA os inner join CP_ORDEM_SERVICO cp on os.ID_OCORRENCIA = cp.ID_OCORRENCIA where cp.FAVORECIDO_TODOS = '" + OrdemServico.GetCustom("FAVORECIDO_TODOS").ToString() + "' and UPPER(os.SITUACAO) not in ('CANCELADO', 'CANCELADA', 'REPROVADO', 'REPROVADA') and (os.ASSUNTO = 'Auxílio Órtese, Prótese e Recursos para Saúde - Adiantamento' or os.ASSUNTO = 'Auxílio Órtese, Prótese e Recursos para Saúde - Reembolso')"
#
#ultima_data = DB.ExecuteScalar(sql_ultima)
#
#carencia_ok = True
#
#if ultima_data != None and ultima_data != DBNull.Value:
#    limite = Convert.ToDateTime(ultima_data).AddYears(anos_carencia)
#
#    if DateTime.Now < limite:
#        carencia_ok = False
#        Criticas.AdicionaPendencia(
#            "Este benefício já foi solicitado em "
#            + Convert.ToDateTime(ultima_data).ToString("dd/MM/yyyy")
#            + ". Novas solicitações só podem ser feitas a partir de "
#            + limite.ToString("dd/MM/yyyy")
#            + "."
#        )
#
## 2) Regra de teto de valor (janela de 5 anos)
#if carencia_ok:
#
#    valor_solicitado = OrdemServico.GetCustom("VALOR_REEMBOLSO")
#
#    sql_soma = "select sum(cpe.VALOR_REEMBOLSO) as TOTAL from OCORRENCIA os inner join CP_ORDEM_SERVICO cp on os.ID_OCORRENCIA = cp.ID_OCORRENCIA inner join CPE_PESSOAS cpe on os.ID_OCORRENCIA = cpe.ID_OCORRENCIA where cp.FAVORECIDO_TODOS = '" + OrdemServico.GetCustom("FAVORECIDO_TODOS").ToString() + "' and UPPER(os.SITUACAO) not in ('CANCELADO', 'CANCELADA', 'REPROVADO', 'REPROVADA') and (os.ASSUNTO = 'Auxílio Órtese, Prótese e Recursos para Saúde - Adiantamento' or os.ASSUNTO = 'Auxílio Órtese, Prótese e Recursos para Saúde - Reembolso') and os.DATA_HORA_FIM_REAL >= to_date('" + data_limite_5anos.ToString("yyyy-MM-dd") + "','yyyy-mm-dd')"
#    total_gasto = DB.ExecuteScalar(sql_soma)
#
#    if total_gasto == None or total_gasto == DBNull.Value:
#        total_gasto = 0
#
#    if (Convert.ToDecimal(total_gasto) + Convert.ToDecimal(valor_solicitado)) > 20000:
#        Criticas.AdicionaPendencia(
#            "O total solicitado para este auxílio nos últimos 5 anos (R$ "
#            + Convert.ToDecimal(total_gasto).ToString("N2")
#            + ") somado a este pedido ultrapassa o limite de R$ 20.000,00."
#        )
```
**ScriptFormCarregado**
```python
Formulario["COMBOBOX"].Habilitado = False
Formulario["COMBOBOX"].Itens = 'Órtese;Prótese;Recurso para Saúde'
Formulario["TEXT"].Habilitado = False
Formulario["VALOR"].Habilitado = False
Formulario["VALOR_REEMBOLSO"].Habilitado = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Laudo Médico Específico Comprovando Necessidade" classes: Laudo Médico — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=FQ110-001
  - anexo "FQ110-001" classes: Anexo — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Comprovante de pagamento (Nota Fiscal/Cupom Fiscal)" classes: Comprovante de pagamento — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - FAVORECIDO_TODOS "Nome do Beneficiário" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
  - SIM_NAO "O empregado favorecido está afastado?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
if Formulario["SIM_NAO"].Valor != None:
    Formulario["COMBOBOX"].Habilitado = True
    
if Formulario["Valor"].Valor != None:
    if Formulario["VALOR"].Valor >= 20000:
        Formulario["VALOR_TOTAL"].Valor = 20000
    elif Formulario["SIM_NAO"].Valor == "Sim":
        Formulario["VALOR_TOTAL"].Valor = 0.9 * Formulario["VALOR"].Valor
    else:
        Formulario["VALOR_TOTAL"].Valor = Formulario["VALOR"].Valor
    Formulario["VALOR_AUTORIZADO"].Valor = 0.01 * Formulario["VALOR_TOTAL"].Valor
```
  - COMBOBOX "Tipo de Equipamento" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
**COMBOBOX.ScriptModificado**
```python
if Formulario["COMBOBOX"].Valor != None:
    Formulario["TEXT"].Habilitado = True
```
  - TEXT "Nome do Equipamento (ex: muleta, cadeira de rodas ...)" [TextBox String(1000) → CPE_CSC.TEXT] obrigatório
**TEXT.ScriptModificado**
```python
if Formulario["TEXT"].Valor != None:
    Formulario["VALOR"].Habilitado = True
```
  - VALOR "Valor do Equipamento" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
**VALOR.ScriptModificado**
```python
ben = Convert.ToDecimal(Formulario["VALOR"].Valor)

if Formulario["VALOR"].Valor != None:
    Formulario["VALOR_REEMBOLSO"].Valor = ben * 0.9
```
  - VALOR_REEMBOLSO "Valor do Reembolso" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO] obrigatório

### [442216] EventoIntermediarioTimer ""
Config: TempoIntervalo=14400; MaximoExecucao=1

### [442217] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [442218] EventoIntermediarioMensagem "Término de serviço"
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de serviço
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Em atendimento à Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto, comunico que foi realizado o término da atividade pelo Cesec.
Para mais detalhes sobre esta solicitação, clique no link a seguir ==> Link.Consulta.
 Complemento1 
Atenciosamente,
Central de Serviços

### [442219] Tarefa "Liberar Pagamento na Conta do Empregado"
Responsável: Fila CSC - Benefícios (papel 524)
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
valor = DB.ExecuteScalar("select replace('"+ OrdemServico.GetCustom("VALOR_REEMBOLSO").ToString() + "',',','.') as valor from dual")
valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '999999D99') as valor from dual")
valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")

pessoa = Pessoa.Carrega(OrdemServico.FavorecidoId)

contInterfaceAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERT from XXBBTSGATE.VW_BBTS_AP_INVOICES_INTERFACE where source LIKE '%SUPRAVIZIO%' AND invoice_num = 'PCD"+OrdemServico.Numero.ToString() + "'")

contAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERT from AP_INVOICES_ALL where source LIKE '%SUPRAVIZIO%' AND invoice_num = 'PCD"+OrdemServico.Numero.ToString() + "'")

if contInterfaceAP.ToString()=='0' and contAP.ToString()=='0':
    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('PCD"+ OrdemServico.Numero.ToString() + "', SYSDATE+1, '"+ pessoa["MATRICULA"].ToString() +"', "+valor.ToString() +", '001.110001.3000003204.34310512','00 DDL','001.110001.3000001000.219340') ")

#sql = " call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('RV"+ OrdemServico.Numero.ToString() + "', SYSDATE+1, '"+ OrdemServico.GetCustom("MATRICULA").ToString() +"', "+OrdemServico.GetCustom("VALOR_REEMBOLSO").ToString() +", '001.110001.3000003204.34310508') "

#OrdemServico.AdicionaComentario(sql.ToString(), False)

AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos
  - Justificativa (nativo) obrigatório

### [442220] Tarefa "Verificar Reprovação"
Responsável: Fila CSC - Benefícios (papel 524)
Config: ConfirmaResponsabilidade=true

### [442221] Tarefa "Aprovar Solicitação"
Responsável: Responsável atual (papel 36)
Config: Codigo=AS
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovação do Gestor; MinimoAprovadores=1; ReenvioEmailAprovacao=12
  - (aprovação) Favorecido (nativo) "Nome do Beneficiário"
  - (aprovação) DescricaoDetalhada (nativo)
  - (aprovação) VALOR_REEMBOLSO "Valor do Reembolso" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO] — PermiteModificarAprovado=true
  - (aprovação) VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] — PermiteModificarAprovado=true
  - aprovador: Cesec-PEAD Marina (Unico)
  - aprovador: Gerente Cesec PES (Unico)

### [442222] EventoIntermediarioMensagem "Verificar Reprovação"
Destinatário: Cliente (papel 18)
ModeloComunicado: Verificar Reprovação
Corpo do comunicado: Prezado(a),
A solicitação não foi aprovada. Por gentileza verificar a reprovação. 
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
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```
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
### papel 312: Cliente e Favorecido Cobra
Tipo=Composto
- composto por: Favorecido Cobra (Script)
- composto por: Cliente (PessoaOrdemServico)
### papel 881: Cesec-PEAD Marina
Tipo=RelacaoPessoas | pessoas: MARINA DE MELO RIBEIRO MATSUI
### papel 1031: Gerente Cesec PES
Tipo=RelacaoOrgaos

## Campos customizados usados (definição global)

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX
Itens: Órtese;Órtese Dentária; Prótese;Recurso para Saúde

### TEXT — TEXT
TextBox String(1000) → CPE_CSC.TEXT

### VALOR — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR
Descrição: Informe

### VALOR_REEMBOLSO — Valor do Reembolso
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO
