# Fluxo: Auxílio Órtese, Prótese e Recursos para Saúde (AUXPCD) — versão 93
Caminho: Fluxos > Gestão de Pessoas - Benefícios Versão 93 Auxílio Órtese, Prótese e Recursos para Saúde
XML: `XMLs para teste/Gestão_de_Pessoas_-_Benefícios_Versão_93_Auxílio_Órtese,_Prótese_e_Recursos_para_Saúde.xml` | Supravizio 19.1.1 | SubProcessoId 23418 | DesenhoProcessoId 3125 | ProcessoId 105
Órgão dono: 3000003210 - DIVISAO DE BENEFICIOS E MOVIMENTACOES DE PESSOAL | Responsável: PALOMA SABINE AMADO ROSA VARGAS
Classe do subprocesso: Objetivo=Auxílio Órtese, Prótese e Recursos para Saúde; DescricaoCliente=Auxílio Órtese, Prótese e Recursos para Saúde; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Auxílio de Aparelho Auditivo.; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Auxílio Órtese, Prótese e Recursos para Saúde (APARELHOAUDITIVO)

## Grafo do fluxo
- [377996] SubProcesso "Gerar comprovante de pagamento" {Responsável atual} → [373900] Liberar Pagamento na Conta do Empregado
- [373900] Tarefa "Liberar Pagamento na Conta do Empregado" {Fila CSC - Benefícios} → [373919] Crédito Enviado
- [373901] Tarefa "Solicitar Envio da Nota Fiscal em até 30 dias" {Fila CSC - Benefícios} → [373918]  | [373907]  | [G83596] Enviou?
- [373902] EventoIntermediarioMensagem "Verificar Reprovação" → [373920] Verificar Reprovação
- [373903] EventoFinal "" {Responsável atual} → (fim)
- [373904] EventoIntermediarioMensagem "Comunicado de Desconto do Crédito" → [373906] Atividade
- [373905] EventoIntermediarioMensagem "Cobrança da Nota Fiscal" → [373901] Solicitar Envio da Nota Fiscal em até 30 dias
- [373906] Tarefa "Atividade" {Responsável atual} → [373917] Resposta Solicitação Reprovada
- [373907] EventoIntermediarioTimer "" → [373904] Comunicado de Desconto do Crédito
- [373908] LinkInicial "Chatbot" → [373913] Verificar Solicitação

- [373909] Tarefa "Informar Motivo da Reprovação" {Responsável atual} → [373910] Devolução para Ajustes
- [373910] EventoIntermediarioMensagem "Devolução para Ajustes" → [373915] Corrigir Informações do Anexo
- [373911] FimCancelamento "" → (fim)
- [373912] EventoIntermediarioMensagem "Resposta Solicitação Reprovada" → [373911] 
- [373913] Tarefa "Verificar Solicitação
" {Fila CSC - Benefícios} → [G83595] Dados OK?
- [373914] EventoInicial "" → [373913] Verificar Solicitação

- [373915] Tarefa "Corrigir Informações do Anexo" {Cliente} → [373916]  | [373913] Verificar Solicitação

- [373916] EventoIntermediarioTimer "" → [373912] Resposta Solicitação Reprovada
- [373917] EventoIntermediarioMensagem "Resposta Solicitação Reprovada" → [373923] 
- [373918] EventoIntermediarioTimer "" → [373905] Cobrança da Nota Fiscal
- [373919] EventoIntermediarioMensagem "Crédito Enviado" → [373901] Solicitar Envio da Nota Fiscal em até 30 dias
- [373920] Tarefa "Verificar Reprovação" {Fila CSC - Benefícios} → [G83597] Devolver Para O  Demandante?
- [373921] EventoIntermediarioMensagem "Chamado atendido com sucesso" → [373903] 
- [373922] Tarefa "Aprovar Solicitação" {Responsável atual} → [G83594] Aprovou?

- [373923] FimCancelamento "" → (fim)
- [G83594] Gateway "Aprovou?
" → «Aprovado» [377996] Gerar comprovante de pagamento | «Reprovado» [373902] Verificar Reprovação
- [G83595] Gateway "Dados OK?" → «Não» [373909] Informar Motivo da Reprovação | «Sim» [373922] Aprovar Solicitação
- [G83596] Gateway "Enviou?" → «Sim» [373921] Chamado atendido com sucesso | «Não» [373906] Atividade
- [G83597] Gateway "Devolver Para O  Demandante?" → «Não» [373922] Aprovar Solicitação | «Sim» [373915] Corrigir Informações do Anexo

## Gateways
### [G83594] Aprovou?
 (DataBasedExclusiveDecision)
Codigo=A
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("AS")
```
- alternativa → [377996] Gerar comprovante de pagamento: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Aprovado
**ValorComparacaoDecision**
```python
True
```
- alternativa → [373902] Verificar Reprovação: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Reprovado
**ValorComparacaoDecision**
```python
False
```
### [G83595] Dados OK? (EventBasedExclusiveDecision)
- alternativa → [373909] Informar Motivo da Reprovação: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não
- alternativa → [373922] Aprovar Solicitação: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim
### [G83596] Enviou? (EventBasedExclusiveDecision)
Codigo=ENVIOU
- alternativa → [373921] Chamado atendido com sucesso: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
- alternativa → [373906] Atividade: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não; RotuloMotivo=Não
### [G83597] Devolver Para O  Demandante? (EventBasedExclusiveDecision)
Codigo=DEVOLVER
- alternativa → [373922] Aprovar Solicitação: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não
- alternativa → [373915] Corrigir Informações do Anexo: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim

## Atividades

### [377996] SubProcesso "Gerar comprovante de pagamento"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1696
**ScriptInicio**
```python
sub = OrdemServico.IniciaSubProcesso(OrdemServico.Atividade)
servico = OrdemServico.Servico.Sigla
sub.Servico.Sigla = servico
sub.Assunto = 'Gerar comprovante de pagamento - Auxílio Órtese, Prótese e Recursos para Saúde.'
sub.Salva()
sub.AvancaAtividade()
```
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
  - CustomPropertyId=1032; CustomProperty=COMBOBOX
  - CustomPropertyId=510; CustomProperty=FAVORECIDO_TODOS
  - CustomPropertyId=773; CustomProperty=PARCELAS_PID
  - CustomPropertyId=1002; CustomProperty=SIM_NAO
  - CustomPropertyId=5068; CustomProperty=TEXT
  - CustomPropertyId=709; CustomProperty=VALOR
  - CustomPropertyId=4987; CustomProperty=VALOR_AUTORIZADO
  - CustomPropertyId=2171; CustomProperty=VALOR_LIMITE_ATUAL
  - CustomPropertyId=774; CustomProperty=VALOR_PRESTACAO
  - CustomPropertyId=390; CustomProperty=VALOR_TOTAL_REEMBOLSO
- Associação: Ativo=true; FraseAssociacao=Aux. Órtese, Prótese e Recursos -> Comprovantes; FraseInversaAssociacao=Comprovantes -> Aux. Órtese, Prótese e Recursos; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=COMPROVANTEPCD; SeparadorSequencial=. | fonte: Auxílio Órtese, Prótese e Recursos para Saúde → alvo: Comprovantes de Valores Pagos a Fornecedores

### [373900] Tarefa "Liberar Pagamento na Conta do Empregado"
Responsável: Fila CSC - Benefícios (papel 524)
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
valor = DB.ExecuteScalar("select replace('"+ OrdemServico.GetCustom("VALOR").ToString() + "',',','.') as valor from dual")
valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '999999D99') as valor from dual")
valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")

pessoa = Pessoa.Carrega(OrdemServico.FavorecidoId)

contInterfaceAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERT from XXBBTSGATE.VW_BBTS_AP_INVOICES_INTERFACE where source LIKE '%SUPRAVIZIO%' AND invoice_num = 'PCD"+OrdemServico.Numero.ToString() + "'")

contAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERT from AP_INVOICES_ALL where source LIKE '%SUPRAVIZIO%' AND invoice_num = 'PCD"+OrdemServico.Numero.ToString() + "'")

if contInterfaceAP.ToString()=='0' and contAP.ToString()=='0':
    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('PCD"+ OrdemServico.Numero.ToString() + "', SYSDATE+1, '"+ pessoa["MATRICULA"].ToString() +"', "+valor.ToString() +", '001.110001.3000003204.34310512','00 DDL','001.110001.3000001000.219340') ")

#sql = " call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('RV"+ OrdemServico.Numero.ToString() + "', SYSDATE+1, '"+ OrdemServico.GetCustom("MATRICULA").ToString() +"', "+OrdemServico.GetCustom("VALOR").ToString() +", '001.110001.3000003204.34310508') "

#OrdemServico.AdicionaComentario(sql.ToString(), False)

AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos
  - Justificativa (nativo) obrigatório

### [373901] Tarefa "Solicitar Envio da Nota Fiscal em até 30 dias"
Responsável: Fila CSC - Benefícios (papel 524)
Config: ConfirmaResponsabilidade=true

### [373902] EventoIntermediarioMensagem "Verificar Reprovação"
Destinatário: Cliente (papel 18)
ModeloComunicado: Verificar Reprovação
Corpo do comunicado: Prezado(a),
A solicitação não foi aprovada. Por gentileza verificar a reprovação. 
Atenciosamente,
Central de Serviços

### [373903] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [373904] EventoIntermediarioMensagem "Comunicado de Desconto do Crédito"
Config: ListaDestinatarios=admempregado@bbts.com.br; cesecgyn.fopag@bbts.com.br; saude@bbts.com.br
ModeloComunicado: Comunicado de Desconto do Crédito
Corpo do comunicado: Prezados(as),
Informamos que o empregado OrdemServico.Customizado.NOME não enviou a nota fiscal comprovando o a compra do aparelho auditivo referente a solicitação realizada na Ordem de Serviço OrdemServico.Customizado.NUMERO_OS .
Pedimos por gentileza, para realizar o desconto na conta do empregado.
Atenciosamente,
Central de Serviços

### [373905] EventoIntermediarioMensagem "Cobrança da Nota Fiscal"
Destinatário: Cliente (papel 18)
ModeloComunicado: Cobrança da Nota Fiscal
Corpo do comunicado: Prezado(a),
Ainda não recebemos a nota fiscal eletrônica comprovando a aquisição do aparelho auditivo. Solicitamos o envio o mais rápido possível.
Conforme regulamento, o não envio da nota acarretará na cobrança integral do valor do equipamento na conta do empregado.
Atenciosamente,
Central de Serviços

### [373906] Tarefa "Atividade"
Responsável: Responsável atual (papel 36)

### [373907] EventoIntermediarioTimer ""
Config: TempoIntervalo=43200

### [373908] LinkInicial "Chatbot"
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - VALOR "Valor do Equipamento" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - VALOR_REEMBOLSO "Valor do Benefício" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO] obrigatório
  - FAVORECIDO_TODOS "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
**FAVORECIDO_TODOS.ScriptModificado**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```
  - SERVICO_SELECIONADO "Serviço Selecionado" [TextBox String → CP_ORDEM_SERVICO.SERVICO_SELECIONADO] obrigatório
- Associação de subprocesso: AssociacaoId=1427; Nome=ADIR CORDEIRO DOS SANTOS FILHO; FraseAssociacao=Chatbot->Fale com a Diges

### [373909] Tarefa "Informar Motivo da Reprovação"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Anexo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - Justificativa (nativo) "Justificativa da devolução" obrigatório

### [373910] EventoIntermediarioMensagem "Devolução para Ajustes"
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

### [373911] FimCancelamento ""

### [373912] EventoIntermediarioMensagem "Resposta Solicitação Reprovada"
Destinatário: Cliente e Favorecido Cobra (papel 312)
ModeloComunicado: Resposta da Solicitação de Reembolso - Reprovação
Corpo do comunicado: Prezado(a),
Por não atendimento a NI 102 a sua solitação de Número OrdemServico.Numero - Reembolso OrdemServico.Servico foi indeferida pelo motivo abaixo: 
OrdemServico.Customizado.RESPOSTA_REPROVACAO_REEMBOLSO 
Para mais detalhes sobre esta solicitação Link.Consulta.
Atenciosamente
Central de Serviços

### [373913] Tarefa "Verificar Solicitação
"
Responsável: Fila CSC - Benefícios (papel 524)

### [373914] EventoInicial ""
TipoSolicitacao: 20.01. Gestão de Pessoas - Benefícios
**ScriptValidacao**
```python
anosCarencia = 1
dataLimite5Anos = DateTime.Now.AddYears(-5)

# 1) Regra de carência (última solicitação do mesmo tipo)
sqlUltima = ("select max(os.DATA_HORA_FIM_REAL) as ULTIMA from OCORRENCIA os INNER JOIN CP_ORDEM_SERVICO cp on os.ID_OCORRENCIA = cp.ID_OCORRENCIA where cp.FAVORECIDO_TODOS = '" + OrdemServico.GetCustom("FAVORECIDO_TODOS").ToString() + "' and UPPER(os.SITUACAO) not in ('CANCELADO', 'CANCELADA', 'REPROVADO', 'REPROVADA') and (os.ASSUNTO = 'Auxílio Órtese, Prótese e Recursos para Saúde - Adiantamento' or os.ASSUNTO = 'Auxílio Órtese, Prótese e Recursos para Saúde - Reembolso')")

ultimaData = DB.ExecuteScalar(sqlUltima)

carenciaOk = True
if ultimaData != None and ultimaData != DBNull.Value:
    limite = Convert.ToDateTime(ultimaData).AddYears(anosCarencia)
    if DateTime.Now < limite:
        carenciaOk = False
        Criticas.AdicionaPendencia("Este benefício já foi solicitado em " + Convert.ToDateTime(ultimaData).ToString("dd/MM/yyyy") + ". Novas solicitações só podem ser feitas a partir de " + limite.ToString("dd/MM/yyyy") + ".")


# 2) Regra de teto de valor (janela de 5 anos)
if carenciaOk:
    valorSolicitado = OrdemServico.GetCustom("VALOR")

    sqlSoma = ("select sum(cp.VALOR) as TOTAL from OCORRENCIA os inner join CP_ORDEM_SERVICO cp on os.ID_OCORRENCIA = cp.ID_OCORRENCIA where cp.FAVORECIDO_TODOS = '" + OrdemServico.GetCustom("FAVORECIDO_TODOS").ToString() + "' and UPPER(os.SITUACAO) not in ('CANCELADO', 'CANCELADA', 'REPROVADO', 'REPROVADA') and (os.ASSUNTO = 'Auxílio Órtese, Prótese e Recursos para Saúde - Adiantamento' or os.ASSUNTO = 'Auxílio Órtese, Prótese e Recursos para Saúde - Reembolso') and os.DATA_HORA_FIM_REAL >= to_date('" + dataLimite5Anos.ToString("yyyy-MM-dd") + "','yyyy-mm-dd')")

    totalGasto = DB.ExecuteScalar(sqlSoma)
    if totalGasto == None or totalGasto == DBNull.Value:
        totalGasto = 0

    if (Convert.ToDecimal(totalGasto) + Convert.ToDecimal(valorSolicitado)) > 20000:
        Criticas.AdicionaPendencia("O total solicitado para este auxílio nos últimos 5 anos (R$ " + Convert.ToDecimal(totalGasto).ToString("N2") + ") somado a este pedido ultrapassa o limite de R$ 20.000,00.")
```
**ScriptFormCarregado**
```python
Formulario["COMBOBOX"].Habilitado = False
Formulario["SIM_NAO"].Habilitado = False
Formulario["COMBOBOX"].Itens = 'Órtese;Prótese;Recurso para Saúde'
Formulario["VALOR_LIMITE_ATUAL"].Habilitado = False
Formulario["PARCELAS_PID"].Habilitado = False
Formulario["TEXT"].Habilitado = False
Formulario["VALOR"].Habilitado = False
Formulario["VALOR_PRESTACAO"].Habilitado = False
Formulario["VALOR_TOTAL_REEMBOLSO"].Habilitado = False
Formulario["VALOR_AUTORIZADO"].Habilitado = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Laudo Médico Específico Comprovando Necessidade" classes: Laudo Médico — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Cotação do Valor do Aparelho" classes: Cotação do Valor do Aparelho — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=FQ110-001
  - anexo "FQ110-001" classes: Anexo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - COMBOBOX "Tipo de Equipamento" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
**COMBOBOX.ScriptModificado**
```python
Formulario["TEXT"].Habilitado = True
```
  - FAVORECIDO_TODOS "Nome do Beneficiário" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
**FAVORECIDO_TODOS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
import apisLG
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

diaFechamentoFolha = 10  # dia do fechamento

colaborador = Pessoa.Carrega(Int32.Parse(Formulario["FAVORECIDO_TODOS"].Valor))
matriculaColaborador = DB.ExecuteScalar("SELECT matricula FROM cp_pessoa WHERE id_pessoa='"+str(colaborador.Id)+"'")

hoje = DateTime.Now

if hoje.Day < diaFechamentoFolha:
    # folha do mês passado ainda não fechou, usa 2 meses atrás
    dataRef = hoje.AddMonths(-2)
else:
    # folha já fechou, usa mês passado normalmente
    dataRef = hoje.AddMonths(-1)

ano = dataRef.Year
mes = dataRef.Month

margemConsignavel = consultaMargemConsignavel(str(matriculaColaborador), str(ano), str(mes))

Formulario["VALOR_LIMITE_ATUAL"].Valor = margemConsignavel.ToString()
Formulario["SIM_NAO"].Habilitado = True
```
  - SIM_NAO "O empregado favorecido está afastado?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
maxAdiantamento = 20000
 
# Limpando formato da margem consignável para comparação decimal
margemConsignavel = Formulario["VALOR_LIMITE_ATUAL"].Valor
margemConsignavel = margemConsignavel.replace("R$", "").strip()
margemConsignavel = margemConsignavel.replace(".", "")
margemConsignavel = Convert.ToDecimal(margemConsignavel)
    
if Formulario["VALOR_TOTAL_REEMBOLSO"].Valor != None:

    # Valor Adiantado equivale a 90% do Valor do Equipamento caso beneficiário esteja afastado. Caso contrário, equivale ao valor integral. Em ambos as alternativas, o Valor Adiantado é limitado pela variável "maxAdiantamento".
    if Formulario["SIM_NAO"].Valor == "Sim":
        valorTotalTeorico = 0.9 * Formulario["VALOR_TOTAL_REEMBOLSO"].Valor
    else:
        valorTotalTeorico = Formulario["VALOR_TOTAL_REEMBOLSO"].Valor
        
    if valorTotalTeorico >= maxAdiantamento:
        Formulario["VALOR"].Valor = maxAdiantamento
    else:
        Formulario["VALOR"].Valor = valorTotalTeorico
        
    # Valor a Ser Parcelado é 10% do Valor Adiantado
    Formulario["VALOR_AUTORIZADO"].Valor = 0.1 * Formulario["VALOR"].Valor

    if (Formulario["PARCELAS_PID"].Valor != None):
        valorParcela = Formulario["VALOR_AUTORIZADO"].Valor / Formulario["PARCELAS_PID"].Valor
        valorParcela = round(valorParcela,2)

        if (margemConsignavel != None) and (valorParcela > margemConsignavel):
            divisao = Formulario["VALOR_AUTORIZADO"].Valor / margemConsignavel
            parcelasNecessarias = int(divisao)
            if divisao > parcelasNecessarias:
                parcelasNecessarias += 1

            parcela = min(parcelasNecessarias, 36)
            valorParcela = Formulario["VALOR_AUTORIZADO"].Valor / parcela
            valorParcela = round(valorParcela,2)

            Formulario["PARCELAS_PID"].Valor = parcela

        Formulario["VALOR_PRESTACAO"].Valor = valorParcela
        
        
Formulario["COMBOBOX"].Habilitado = True
```
  - TEXT "Nome do equipamento (ex: muleta, cadeira de rodas ...)" [TextBox String(1000) → CPE_CSC.TEXT] obrigatório
**TEXT.ScriptModificado**
```python
Formulario["VALOR_TOTAL_REEMBOLSO"].Habilitado = True
```
  - VALOR_PRESTACAO "Valor da prestação" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_PRESTACAO] obrigatório
  - VALOR_TOTAL_REEMBOLSO "Valor do Equipamento" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_TOTAL_REEMBOLSO] obrigatório
**VALOR_TOTAL_REEMBOLSO.ScriptModificado**
```python
maxAdiantamento = 20000
 
# Limpando formato da margem consignável para comparação decimal
margemConsignavel = Formulario["VALOR_LIMITE_ATUAL"].Valor
margemConsignavel = margemConsignavel.replace("R$", "").strip()
margemConsignavel = margemConsignavel.replace(".", "")
margemConsignavel = Convert.ToDecimal(margemConsignavel)
    
# Valor Adiantado equivale a 90% do Valor do Equipamento caso beneficiário esteja afastado. Caso contrário, equivale ao valor integral. Em ambos as alternativas, o Valor Adiantado é limitado pela variável "maxAdiantamento".
if Formulario["SIM_NAO"].Valor == "Sim":
    valorTotalTeorico = 0.9 * Formulario["VALOR_TOTAL_REEMBOLSO"].Valor
else:
    valorTotalTeorico = Formulario["VALOR_TOTAL_REEMBOLSO"].Valor
        
if valorTotalTeorico >= maxAdiantamento:
    Formulario["VALOR"].Valor = maxAdiantamento
else:
    Formulario["VALOR"].Valor = valorTotalTeorico
        
# Valor a Ser Parcelado é 10% do Valor Adiantado
Formulario["VALOR_AUTORIZADO"].Valor = 0.1 * Formulario["VALOR"].Valor

if (Formulario["PARCELAS_PID"].Valor != None):
    valorParcela = Formulario["VALOR_AUTORIZADO"].Valor / Formulario["PARCELAS_PID"].Valor
    valorParcela = round(valorParcela,2)

    if (margemConsignavel != None) and (valorParcela > margemConsignavel):
        divisao = Formulario["VALOR_AUTORIZADO"].Valor / margemConsignavel
        parcelasNecessarias = int(divisao)
        if divisao > parcelasNecessarias:
            parcelasNecessarias += 1

        parcela = min(parcelasNecessarias, 36)
        valorParcela = Formulario["VALOR_AUTORIZADO"].Valor / parcela
        valorParcela = round(valorParcela,2)

        Formulario["PARCELAS_PID"].Valor = parcela

    Formulario["VALOR_PRESTACAO"].Valor = valorParcela
    

Formulario["PARCELAS_PID"].Habilitado = True
```
  - VALOR "Valor Adiantado" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - VALOR_AUTORIZADO "Valor a ser Parcelado (10% do valor adiantado)" [TextBox Decimal → CPE_MOVIMENTACAO_PESSOA.VALOR_AUTORIZADO] obrigatório
  - VALOR_LIMITE_ATUAL "Margem Consignável (valor máximo da prestação)" [TextBox String → CPE_TIP_SOL01.VALOR_LIMITE_ATUAL] obrigatório
  - PARCELAS_PID "Número de parcelas" [DropDownList Integer → CP_ORDEM_SERVICO.PARCELAS_PID] obrigatório
**PARCELAS_PID.ScriptModificado**
```python
valor = Formulario["VALOR_AUTORIZADO"].Valor
parcela = Convert.ToInt32(Formulario["PARCELAS_PID"].Valor)

# Limpando formato da margem consignável para comparação decimal
margemConsignavel = Formulario["VALOR_LIMITE_ATUAL"].Valor
margemConsignavel = margemConsignavel.replace("R$", "").strip()
margemConsignavel = margemConsignavel.replace(".", "")
margemConsignavel = Convert.ToDecimal(margemConsignavel)

Formulario["VALOR_PRESTACAO"].Valor = 0

if (valor != None) and (Formulario["PARCELAS_PID"].Valor != None):
    valorParcela = round(valor / parcela, 2)

    if (margemConsignavel != None) and (valorParcela > margemConsignavel):
        divisao = valor / margemConsignavel
        parcelasNecessarias = int(divisao)
        if divisao > parcelasNecessarias:
            parcelasNecessarias += 1

        parcela = min(parcelasNecessarias, 36)
        valorParcela = round(valor / parcela, 2)

        Formulario["PARCELAS_PID"].Valor = parcela

    Formulario["VALOR_PRESTACAO"].Valor = valorParcela
```

### [373915] Tarefa "Corrigir Informações do Anexo"
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
- Operação PR0004 Associar Itens Configuração
  - anexo "Laudo Médico Específico Comprovando Necessidade de Aparelho Auditivo" classes: Laudo Médico — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Cotação do Valor do Aparelho — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "FQ110-001" classes: Anexo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - FAVORECIDO_TODOS "Nome do Beneficiário" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
**FAVORECIDO_TODOS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
import apisLG
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

diaFechamentoFolha = 10  # dia do fechamento

colaborador = Pessoa.Carrega(Int32.Parse(Formulario["FAVORECIDO_TODOS"].Valor))
matriculaColaborador = DB.ExecuteScalar("SELECT matricula FROM cp_pessoa WHERE id_pessoa='"+str(colaborador.Id)+"'")

hoje = DateTime.Now

if hoje.Day < diaFechamentoFolha:
    # folha do mês passado ainda não fechou, usa 2 meses atrás
    dataRef = hoje.AddMonths(-2)
else:
    # folha já fechou, usa mês passado normalmente
    dataRef = hoje.AddMonths(-1)

ano = dataRef.Year
mes = dataRef.Month

margemConsignavel = consultaMargemConsignavel(str(matriculaColaborador), str(ano), str(mes))

Formulario["VALOR_LIMITE_ATUAL"].Valor = margemConsignavel.ToString()
Formulario["SIM_NAO"].Habilitado = True
```
  - VALOR "Valor Adiantado" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - VALOR_AUTORIZADO "Valor a ser Parcelado (10% do valor adiantado)" [TextBox Decimal → CPE_MOVIMENTACAO_PESSOA.VALOR_AUTORIZADO] obrigatório
  - VALOR_LIMITE_ATUAL "Margem Consignável (valor máximo da prestação)" [TextBox String → CPE_TIP_SOL01.VALOR_LIMITE_ATUAL] obrigatório
  - VALOR_PRESTACAO "Valor da prestação" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_PRESTACAO] obrigatório
  - SIM_NAO "O empregado favorecido está afastado?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
maxAdiantamento = 20000
 
# Limpando formato da margem consignável para comparação decimal
margemConsignavel = Formulario["VALOR_LIMITE_ATUAL"].Valor
margemConsignavel = margemConsignavel.replace("R$", "").strip()
margemConsignavel = margemConsignavel.replace(".", "")
margemConsignavel = Convert.ToDecimal(margemConsignavel)
    
if Formulario["VALOR_TOTAL_REEMBOLSO"].Valor != None:

    # Valor Adiantado equivale a 90% do Valor do Equipamento caso beneficiário esteja afastado. Caso contrário, equivale ao valor integral. Em ambos as alternativas, o Valor Adiantado é limitado pela variável "maxAdiantamento".
    if Formulario["SIM_NAO"].Valor == "Sim":
        valorTotalTeorico = 0.9 * Formulario["VALOR_TOTAL_REEMBOLSO"].Valor
    else:
        valorTotalTeorico = Formulario["VALOR_TOTAL_REEMBOLSO"].Valor
        
    if valorTotalTeorico >= maxAdiantamento:
        Formulario["VALOR"].Valor = maxAdiantamento
    else:
        Formulario["VALOR"].Valor = valorTotalTeorico
        
    # Valor a Ser Parcelado é 10% do Valor Adiantado
    Formulario["VALOR_AUTORIZADO"].Valor = 0.1 * Formulario["VALOR"].Valor

    if (Formulario["PARCELAS_PID"].Valor != None):
        valorParcela = Formulario["VALOR_AUTORIZADO"].Valor / Formulario["PARCELAS_PID"].Valor
        valorParcela = round(valorParcela,2)

        if (margemConsignavel != None) and (valorParcela > margemConsignavel):
            divisao = Formulario["VALOR_AUTORIZADO"].Valor / margemConsignavel
            parcelasNecessarias = int(divisao)
            if divisao > parcelasNecessarias:
                parcelasNecessarias += 1

            parcela = min(parcelasNecessarias, 36)
            valorParcela = Formulario["VALOR_AUTORIZADO"].Valor / parcela
            valorParcela = round(valorParcela,2)

            Formulario["PARCELAS_PID"].Valor = parcela

        Formulario["VALOR_PRESTACAO"].Valor = valorParcela
        
        
Formulario["COMBOBOX"].Habilitado = True
```
  - COMBOBOX "Tipo de Equipamento" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
**COMBOBOX.ScriptModificado**
```python
Formulario["TEXT"].Habilitado = True
```
  - TEXT "Nome do equipamento (ex: muleta, cadeira de rodas ...)" [TextBox String(1000) → CPE_CSC.TEXT] obrigatório
**TEXT.ScriptModificado**
```python
Formulario["VALOR_TOTAL_REEMBOLSO"].Habilitado = True
```
  - VALOR_TOTAL_REEMBOLSO "Valor do Equipamento" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_TOTAL_REEMBOLSO] obrigatório
**VALOR_TOTAL_REEMBOLSO.ScriptModificado**
```python
maxAdiantamento = 20000
 
# Limpando formato da margem consignável para comparação decimal
margemConsignavel = Formulario["VALOR_LIMITE_ATUAL"].Valor
margemConsignavel = margemConsignavel.replace("R$", "").strip()
margemConsignavel = margemConsignavel.replace(".", "")
margemConsignavel = Convert.ToDecimal(margemConsignavel)
    
# Valor Adiantado equivale a 90% do Valor do Equipamento caso beneficiário esteja afastado. Caso contrário, equivale ao valor integral. Em ambos as alternativas, o Valor Adiantado é limitado pela variável "maxAdiantamento".
if Formulario["SIM_NAO"].Valor == "Sim":
    valorTotalTeorico = 0.9 * Formulario["VALOR_TOTAL_REEMBOLSO"].Valor
else:
    valorTotalTeorico = Formulario["VALOR_TOTAL_REEMBOLSO"].Valor
        
if valorTotalTeorico >= maxAdiantamento:
    Formulario["VALOR"].Valor = maxAdiantamento
else:
    Formulario["VALOR"].Valor = valorTotalTeorico
        
# Valor a Ser Parcelado é 10% do Valor Adiantado
Formulario["VALOR_AUTORIZADO"].Valor = 0.1 * Formulario["VALOR"].Valor

if (Formulario["PARCELAS_PID"].Valor != None):
    valorParcela = Formulario["VALOR_AUTORIZADO"].Valor / Formulario["PARCELAS_PID"].Valor
    valorParcela = round(valorParcela,2)

    if (margemConsignavel != None) and (valorParcela > margemConsignavel):
        divisao = Formulario["VALOR_AUTORIZADO"].Valor / margemConsignavel
        parcelasNecessarias = int(divisao)
        if divisao > parcelasNecessarias:
            parcelasNecessarias += 1

        parcela = min(parcelasNecessarias, 36)
        valorParcela = Formulario["VALOR_AUTORIZADO"].Valor / parcela
        valorParcela = round(valorParcela,2)

        Formulario["PARCELAS_PID"].Valor = parcela

    Formulario["VALOR_PRESTACAO"].Valor = valorParcela
    

Formulario["PARCELAS_PID"].Habilitado = True
```
  - PARCELAS_PID "Número de parcelas" [DropDownList Integer → CP_ORDEM_SERVICO.PARCELAS_PID] obrigatório
**PARCELAS_PID.ScriptModificado**
```python
valor = Formulario["VALOR_AUTORIZADO"].Valor
parcela = Convert.ToInt32(Formulario["PARCELAS_PID"].Valor)

# Limpando formato da margem consignável para comparação decimal
margemConsignavel = Formulario["VALOR_LIMITE_ATUAL"].Valor
margemConsignavel = margemConsignavel.replace("R$", "").strip()
margemConsignavel = margemConsignavel.replace(".", "")
margemConsignavel = Convert.ToDecimal(margemConsignavel)

Formulario["VALOR_PRESTACAO"].Valor = 0

if (valor != None) and (Formulario["PARCELAS_PID"].Valor != None):
    valorParcela = round(valor / parcela, 2)

    if (margemConsignavel != None) and (valorParcela > margemConsignavel):
        divisao = valor / margemConsignavel
        parcelasNecessarias = int(divisao)
        if divisao > parcelasNecessarias:
            parcelasNecessarias += 1

        parcela = min(parcelasNecessarias, 36)
        valorParcela = round(valor / parcela, 2)

        Formulario["PARCELAS_PID"].Valor = parcela

    Formulario["VALOR_PRESTACAO"].Valor = valorParcela
```

### [373916] EventoIntermediarioTimer ""
Config: TempoIntervalo=14400; MaximoExecucao=1

### [373917] EventoIntermediarioMensagem "Resposta Solicitação Reprovada"
Destinatário: Cliente e Favorecido Cobra (papel 312)
ModeloComunicado: Resposta da Solicitação de Reembolso - Reprovação
Corpo do comunicado: Prezado(a),
Por não atendimento a NI 102 a sua solitação de Número OrdemServico.Numero - Reembolso OrdemServico.Servico foi indeferida pelo motivo abaixo: 
OrdemServico.Customizado.RESPOSTA_REPROVACAO_REEMBOLSO 
Para mais detalhes sobre esta solicitação Link.Consulta.
Atenciosamente
Central de Serviços

### [373918] EventoIntermediarioTimer ""
Config: TempoIntervalo=4320

### [373919] EventoIntermediarioMensagem "Crédito Enviado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Comunicado de Crédito do Auxílio Aparelho Auditivo
Corpo do comunicado: Prezado(a),
Informamos que será realizado o crédito no valor de OrdemServico.Customizado.VALOR referente a aquisição de Auxílio Órtese, Prótese e Recursos para Saúde em até 5 dias uteis.
Solicitamos o envio da nota fiscal eletrônica em até 30 dias, respondendo a este e-mail sem alterar o assunto e o destinatário.
Atenciosamente,
Central de Serviços

### [373920] Tarefa "Verificar Reprovação"
Responsável: Fila CSC - Benefícios (papel 524)

### [373921] EventoIntermediarioMensagem "Chamado atendido com sucesso"
Destinatário: Cliente (papel 18)
ModeloComunicado: Chamado atendido com sucesso
Corpo do comunicado: Prezado,
A Ordem de Serviço nº OrdemServico.Numero sobre o Assunto: OrdemServico.Assunto foi atendido com sucesso!
 Complemento1 
Para maiores informações Link.Consulta .
Atenciosamente,
Central de Serviços

### [373922] Tarefa "Aprovar Solicitação"
Responsável: Responsável atual (papel 36)
Config: Codigo=AS
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovação do Gestor; MinimoAprovadores=1; ReenvioEmailAprovacao=12
  - (aprovação) DescricaoDetalhada (nativo)
  - (aprovação) VALOR_REEMBOLSO "Valor do Reembolso" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO] — PermiteModificarAprovado=true
  - (aprovação) Favorecido (nativo) "Nome do Beneficiário"
  - (aprovação) VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] — PermiteModificarAprovado=true
  - aprovador: Gerente Cesec PES (Unico)
  - aprovador: Cesec-PEAD Marina (Unico)

### [373923] FimCancelamento ""

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
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 312: Cliente e Favorecido Cobra
Tipo=Composto
- composto por: Favorecido Cobra (Script)
- composto por: Cliente (PessoaOrdemServico)
### papel 1310: Gerente Cesec PES
Tipo=RelacaoOrgaos
### papel 941: Cesec-PEAD Marina
Tipo=RelacaoPessoas | pessoas: MARINA DE MELO RIBEIRO MATSUI

## Campos customizados usados (definição global)

### VALOR — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR
Descrição: Informe

### VALOR_REEMBOLSO — Valor do Reembolso
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### SERVICO_SELECIONADO — Serviço Selecionado
TextBox String → CP_ORDEM_SERVICO.SERVICO_SELECIONADO

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX
Itens: Órtese;Órtese Dentária; Prótese;Recurso para Saúde

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### TEXT — TEXT
TextBox String(1000) → CPE_CSC.TEXT

### VALOR_PRESTACAO — Valor da prestação
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_PRESTACAO

### VALOR_TOTAL_REEMBOLSO — Valor Total
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_TOTAL_REEMBOLSO

### VALOR_AUTORIZADO — Valor Autorizado
TextBox Decimal → CPE_MOVIMENTACAO_PESSOA.VALOR_AUTORIZADO

### VALOR_LIMITE_ATUAL — Valor do limite atual (R$)
TextBox String → CPE_TIP_SOL01.VALOR_LIMITE_ATUAL
Descrição: Valor do limite atual (R$):

### PARCELAS_PID — Número de parcelas
DropDownList Integer → CP_ORDEM_SERVICO.PARCELAS_PID
Itens: 1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36

## Biblioteca de scripts referenciada
apisLG, teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
