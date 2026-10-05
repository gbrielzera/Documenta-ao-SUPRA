# Fluxo: Auxílio Órtese, Prótese e Recursos para Saúde - Reembolso (AUXPCDRBS) — versão 88
Caminho: Fluxos > Gestão de Pessoas - Benefícios Versão 88 Auxílio Órtese, Prótese e Recursos para Saúde - Reembolso
XML: `XMLs para teste/Gestão_de_Pessoas_-_Benefícios_Versão_88_Auxílio_Órtese,_Prótese_e_Recursos_para_Saúde_-_Reembolso.xml` | Supravizio 19.1.1 | SubProcessoId 22221 | DesenhoProcessoId 3036 | ProcessoId 105
Órgão dono: 3000003210 - DIVISAO DE BENEFICIOS E MOVIMENTACOES DE PESSOAL | Responsável: PALOMA SABINE AMADO ROSA VARGAS
Classe do subprocesso: Objetivo=Auxílio Órtese, Prótese e Recursos para Saúde - Reembolso; DescricaoCliente=Auxílio Órtese, Prótese e Recursos para Saúde - Reembolso; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Auxílio de Aparelho Auditivo (APARELHOAUDITIVO)

## Grafo do fluxo
- [353653] EventoIntermediarioMensagem "Devolulção para Ajustes" → [353659] Corrigir Informações do Anexo
- [353654] FimCancelamento "" → (fim)
- [353655] Tarefa "Informar Motivo da Reprovação" {Responsável atual} → [353653] Devolulção para Ajustes
- [353657] Tarefa "Verificar Solicitação
" {Fila CSC - Benefícios} → [G79759] Dados OK?
- [353658] EventoIntermediarioMensagem "Resposta Solicitação Reprovada" → [353654] 
- [353659] Tarefa "Corrigir Informações do Anexo" {Cliente} → [353663]  | [353657] Verificar Solicitação

- [353661] EventoInicial "" → [353657] Verificar Solicitação

- [353663] EventoIntermediarioTimer "" → [353658] Resposta Solicitação Reprovada
- [353664] EventoFinal "" {Responsável atual} → (fim)
- [353665] EventoIntermediarioMensagem "Término de serviço" → [353664] 
- [353666] Tarefa "Liberar Pagamento na Conta do Empregado" {Fila CSC - Benefícios} → [353665] Término de serviço
- [G79759] Gateway "Dados OK?" → «Não» [353655] Informar Motivo da Reprovação | «Sim» [353666] Liberar Pagamento na Conta do Empregado

## Gateways
### [G79759] Dados OK? (EventBasedExclusiveDecision)
- alternativa → [353655] Informar Motivo da Reprovação: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
- alternativa → [353666] Liberar Pagamento na Conta do Empregado: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1; RotuloMotivo=Sim

## Atividades

### [353653] EventoIntermediarioMensagem "Devolulção para Ajustes"
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

### [353654] FimCancelamento ""

### [353655] Tarefa "Informar Motivo da Reprovação"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Anexo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - Justificativa (nativo) "Justificativa da devolução" obrigatório

### [353657] Tarefa "Verificar Solicitação
"
Responsável: Fila CSC - Benefícios (papel 524)
- Operação PR0001 Preencher Campos
  - FAVORECIDO_TODOS "Nome do Beneficiário" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
  - VALOR "Valor do Equipamento" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
**VALOR.ScriptModificado**
```python
Formulario["VALOR_REEMBOLSO"].Visivel = True
Formulario["VALOR_REEMBOLSO"].Valor = Controle.Valor 
if Controle.Valor >= 20000:
    Formulario["VALOR_REEMBOLSO"].Valor = 20000
```
  - VALOR_REEMBOLSO "Valor do Reembolso" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO] obrigatório

### [353658] EventoIntermediarioMensagem "Resposta Solicitação Reprovada"
Destinatário: Cliente e Favorecido Cobra (papel 312)
ModeloComunicado: Resposta da Solicitação de Reembolso - Reprovação
Corpo do comunicado: Prezado(a),
Por não atendimento a NI 102 a sua solitação de Número OrdemServico.Numero - Reembolso OrdemServico.Servico foi indeferida pelo motivo abaixo: 
OrdemServico.Customizado.RESPOSTA_REPROVACAO_REEMBOLSO 
Para mais detalhes sobre esta solicitação Link.Consulta.
Atenciosamente
Central de Serviços

### [353659] Tarefa "Corrigir Informações do Anexo"
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
- Operação PR0004 Associar Itens Configuração
  - anexo "Comprovante de pagamento (Nota Fiscal/Cupom Fiscal)" classes: Comprovante de pagamento — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - FAVORECIDO_TODOS "Nome do Beneficiário" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
  - VALOR "Valor do Equipamento" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - VALOR_REEMBOLSO "Valor do Reembolso" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO] obrigatório
  - DescricaoDetalhada (nativo) obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Laudo Médico Específico Comprovando Necessidade de Aparelho Auditivo" classes: Laudo Médico — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "FQ110-001" classes: Anexo — RequeridoInicial=true

### [353661] EventoInicial ""
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
- Operação PR0004 Associar Itens Configuração
  - anexo "Comprovante de pagamento (Nota Fiscal/Cupom Fiscal)" classes: Comprovante de pagamento — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Laudo Médico Específico Comprovando Necessidade" classes: Laudo Médico — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=FQ110-001
  - anexo "FQ110-001" classes: Anexo — RequeridoInicial=true

### [353663] EventoIntermediarioTimer ""
Config: TempoIntervalo=14400; MaximoExecucao=1

### [353664] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [353665] EventoIntermediarioMensagem "Término de serviço"
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de serviço
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Em atendimento à Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto, comunico que foi realizado o término da atividade pelo Cesec.
Para mais detalhes sobre esta solicitação, clique no link a seguir ==> Link.Consulta.
 Complemento1 
Atenciosamente,
Central de Serviços

### [353666] Tarefa "Liberar Pagamento na Conta do Empregado"
Responsável: Fila CSC - Benefícios (papel 524)
**ScriptInicio**
```python
import clr
import System

clr.AddReference("Supravizio.Custom")

from System import Convert, DBNull


def Texto(valor):
    try:
        if valor is None or valor == DBNull.Value:
            return ""

        texto = Convert.ToString(valor)

        if texto is None:
            return ""

        return texto.Trim()

    except:
        return ""


# ============================================================
# TRATA O VALOR DO REEMBOLSO
# ============================================================

valorBruto = Texto(
    OrdemServico.GetCustom(
        "VALOR_REEMBOLSO"
    )
)

if valorBruto == "":
    raise Exception(
        "O campo VALOR_REEMBOLSO não foi preenchido."
    )


valor = DB.ExecuteScalar(
    (
        "SELECT REPLACE('{0}', ',', '.') "
        "FROM DUAL"
    ).format(
        valorBruto.Replace("'", "''")
    )
)

valor = DB.ExecuteScalar(
    (
        "SELECT TO_CHAR({0}, '999999D99') "
        "FROM DUAL"
    ).format(
        Texto(valor)
    )
)

valor = DB.ExecuteScalar(
    (
        "SELECT REPLACE('{0}', ',', '.') "
        "FROM DUAL"
    ).format(
        Texto(valor).Replace("'", "''")
    )
)

valor = Texto(valor)

# ============================================================
# RECUPERA A MATRÍCULA DO EMPREGADO SELECIONADO
# ============================================================

idPessoaTexto = Texto(
    OrdemServico.GetCustom(
        "FAVORECIDO_TODOS"
    )
)

if idPessoaTexto == "":
    raise Exception(
        "Nenhum empregado foi selecionado no campo FAVORECIDO_TODOS."
    )


try:
    idPessoa = Convert.ToInt32(
        idPessoaTexto
    )

except:
    raise Exception(
        (
            "O campo FAVORECIDO_TODOS retornou um "
            "identificador inválido: {0}."
        ).format(
            idPessoaTexto
        )
    )


nomePessoa = DB.ExecuteScalar(
    (
        "SELECT P.NOME "
        "FROM PESSOA P "
        "WHERE P.ID_PESSOA = {0} "
        "AND ROWNUM = 1"
    ).format(
        idPessoa
    )
)

nomePessoa = Texto(
    nomePessoa
)


matricula = DB.ExecuteScalar(
    (
        "SELECT CP.MATRICULA "
        "FROM CP_PESSOA CP "
        "WHERE CP.ID_PESSOA = {0} "
        "AND CP.MATRICULA IS NOT NULL "
        "AND TRIM(CP.MATRICULA) IS NOT NULL "
        "AND ROWNUM = 1"
    ).format(
        idPessoa
    )
)

matricula = Texto(
    matricula
)


if matricula == "":
    raise Exception(
        (
            "Não foi encontrada matrícula para a pessoa "
            "selecionada em FAVORECIDO_TODOS. "
            "ID_PESSOA: {0}; nome: {1}."
        ).format(
            idPessoa,
            nomePessoa
        )
    )


#OrdemServico.AdicionaComentario(
#    (
#        "Diagnóstico da integração AP: "
#        "ID_PESSOA selecionado={0}; "
#        "nome={1}; "
#        "matrícula enviada={2}; "
#        "FavorecidoId nativo da OS={3}."
#    ).format(
#        idPessoa,
#        nomePessoa,
#        matricula,
#        Texto(OrdemServico.FavorecidoId)
#    ),
#    False
#)


# ============================================================
# MONTA O NÚMERO DA INTERFACE AP
# ============================================================

numeroInvoice = (
    "PCD" +
    OrdemServico.Numero.ToString()
)


# ============================================================
# VERIFICA DUPLICIDADE
# ============================================================

contInterfaceAP = DB.ExecuteScalar(
    (
        "SELECT COUNT(1) "
        "FROM XXBBTSGATE.VW_BBTS_AP_INVOICES_INTERFACE "
        "WHERE SOURCE LIKE '%SUPRAVIZIO%' "
        "AND INVOICE_NUM = '{0}'"
    ).format(
        numeroInvoice
    )
)


contAP = DB.ExecuteScalar(
    (
        "SELECT COUNT(1) "
        "FROM AP_INVOICES_ALL "
        "WHERE SOURCE LIKE '%SUPRAVIZIO%' "
        "AND INVOICE_NUM = '{0}'"
    ).format(
        numeroInvoice
    )
)


# ============================================================
# CHAMA A PROCEDURE
# ============================================================

if (
    Texto(contInterfaceAP) == "0" and
    Texto(contAP) == "0"
):

    sqlProcedure = (
        "CALL XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE "
        "('{0}', SYSDATE + 1, '{1}', {2}, "
        "'001.110001.3000003210.34310512')"
    ).format(
        numeroInvoice,
        matricula.Replace("'", "''"),
        valor
    )

    # Diagnóstico temporário.
    #OrdemServico.AdicionaComentario(
    #    (
    #        "Integração AP: ID_PESSOA={0}; "
    #        "MATRÍCULA={1}; "
    #        "VALOR={2}; "
    #        "INVOICE={3}."
    #    ).format(
    #        idPessoa,
    #        matricula,
    #        valor,
    #        numeroInvoice
    #    ),
    #    False
    #)

    DB.ExecuteNonQuery(
        sqlProcedure
    )


AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos
  - Justificativa (nativo) obrigatório

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

## Campos customizados usados (definição global)

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### VALOR — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR
Descrição: Informe

### VALOR_REEMBOLSO — Valor do Reembolso
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX
Itens: Órtese;Órtese Dentária; Prótese;Recurso para Saúde

### TEXT — TEXT
TextBox String(1000) → CPE_CSC.TEXT

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
