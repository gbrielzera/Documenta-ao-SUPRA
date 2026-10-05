# Fluxo: Reembolso (CSCREEMBOLSO) — versão 90
Caminho: Fluxos > Gestão de Pessoas - Benefícios Versão 90 Reembolso
XML: `XMLs para teste/Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml` | Supravizio 19.1.1 | SubProcessoId 22565 | DesenhoProcessoId 3055 | ProcessoId 105
Órgão dono: 3000003210 - DIVISAO DE BENEFICIOS E MOVIMENTACOES DE PESSOAL | Responsável: PALOMA SABINE AMADO ROSA VARGAS
Classe do subprocesso: Objetivo=Reembolso; DescricaoCliente=Reembolso; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Reembolso; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Reembolso Auxílio PCD Terapias - Consultas Avulsas (Particulares) (RPCDCONSULTAS); Reembolso Auxílio PCD Terapias - Planos de Saúde (Modalidade Reembolso BBTS)  (RPCDTERAPIAS); Creche ou Auxílio Babá (CRECHECOLABORADOR); Pré-escola ou Auxílio Babá (13 até 83 meses) (PREESCOLACOLABORADOR); Auxílio para Filho com Deficiência (ESCOLA); Auxílio Odontológico (AUXODONTOLOGICO); Medicamento (MEDICAMENTOCOLABORADOR); Ótico (OTICOCOLABORADOR)

## Grafo do fluxo
- [360745] LinkInicial "Reembolso Creche" → [360762] Aviso de abertura de chamado
- [360764] EventoIntermediarioMensagem "Solicitação de Reembolso" → [360757] Preencher Informações
- [360746] LinkInicial "Reembolso Auxílio para Filho com Deficiência" → [360762] Aviso de abertura de chamado
- [360761] LinkInicial "Reembolso Odontológico" → [360762] Aviso de abertura de chamado
- [360762] EventoIntermediarioMensagem "Aviso de abertura de chamado" → [360757] Preencher Informações
- [360763] Tarefa "Aprovação do Gestor" {Fila CSC - Pendente de Aprovação} → [G81070] Aprovada?
- [360765] EventoIntermediarioMensagem "Aviso de aprovação" → [360749] Inserir dados no ERP
- [360744] Tarefa "Verificar Nota Fiscal
" {Fila CSC - Benefícios} → [G81067] Solicitação aprovada?
- [360747] Tarefa "Informar Motivo da Reprovação" {Responsável atual da atividade} → [360756] Devolução para ajustes
- [360748] LinkInicial "Reembolso Ótico" → [360762] Aviso de abertura de chamado
- [360749] Tarefa "Inserir dados no ERP" {Responsável atual da atividade} → [G81066] Cadastro de Dependente?
- [360750] Tarefa "Calcular reembolso" {Fila CSC - Benefícios} → [360744] Verificar Nota Fiscal

- [360751] EventoIntermediarioTimer "Tempo para correção" → [360754] Resposta Solicitação Reprovada
- [360752] EventoIntermediarioMensagem "Resposta Solicitação Aprovada" → [360759] Finalizada Sucesso
- [360753] EventoIntermediarioMensagem "Aviso para aprovação" → [360763] Aprovação do Gestor
- [360754] EventoIntermediarioMensagem "Resposta Solicitação Reprovada" → [360770] Finalizada Não realizado
- [360755] EventoIntermediarioMensagem "Enviar Atualização de dependentes" → [360752] Resposta Solicitação Aprovada
- [360756] EventoIntermediarioMensagem "Devolução para ajustes" → [360767] Corrigir informações e/ou anexos
- [360757] Tarefa "Preencher Informações" {Fila CSC - Benefícios} → [360750] Calcular reembolso
- [360758] EventoFinal "" → (fim)
- [360759] EventoFinal "Finalizada Sucesso" {Favorecido Todos} → (fim)
- [360760] EventoInicial "Solicitação de reembolso" {Fila CSC - Benefícios} → [360764] Solicitação de Reembolso
- [360766] EventoIntermediarioMensagem "Notificar cliente reprovado" → [360758] 
- [360767] Tarefa "Corrigir informações e/ou anexos" {Cliente} → [360750] Calcular reembolso | [360751] Tempo para correção
- [360768] LinkInicial "Reembolso Medicamento" → [360762] Aviso de abertura de chamado
- [360769] LinkInicial "Reembolso Pré-Escola" → [360762] Aviso de abertura de chamado
- [360770] EventoFinal "Finalizada Não realizado" {Sistema} → (fim)
- [G81066] Gateway "Cadastro de Dependente?" → «Sim» [360752] Resposta Solicitação Aprovada | «Não» [360755] Enviar Atualização de dependentes
- [G81067] Gateway "Solicitação aprovada?" → «Não» [360747] Informar Motivo da Reprovação | «Sim» [G81068] OS referente a Reembolso Medicamento?
- [G81068] Gateway "OS referente a Reembolso Medicamento?" → «Sim» [G81069] Valor do Reembolso é maior que 500,00 ? | «Não» [360749] Inserir dados no ERP
- [G81069] Gateway "Valor do Reembolso é maior que 500,00 ?" → «Sim» [360753] Aviso para aprovação | «Não» [360749] Inserir dados no ERP
- [G81070] Gateway "Aprovada?" → «Aprovado» [360765] Aviso de aprovação | «Reprovado» [360766] Notificar cliente reprovado

## Gateways
### [G81066] Cadastro de Dependente? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.GetCustom("OPCAO_DE_CONFIRMACAO")
```
- alternativa → [360752] Resposta Solicitação Aprovada: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [360755] Enviar Atualização de dependentes: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G81067] Solicitação aprovada? (EventBasedExclusiveDecision)
Referencia=Considerando a análise da documentação e da nota fiscal apresentada pelo solicitante do reembolso, defina se a solicitação está aprovada ou não.; Codigo=APROVACAO
- alternativa → [360747] Informar Motivo da Reprovação: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
- alternativa → [G81068] OS referente a Reembolso Medicamento?: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
### [G81068] OS referente a Reembolso Medicamento? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR"
```
- alternativa → [G81069] Valor do Reembolso é maior que 500,00 ?: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [360749] Inserir dados no ERP: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G81069] Valor do Reembolso é maior que 500,00 ? (DataBasedExclusiveDecision)
Referencia=Atenção solucionador!
Valor de Reembolso maior que R$ 500,00 , solicitar aprovação do Gestor.
**ExpressaoComparacaoDecision**
```python
OrdemServico.GetCustom('VALOR_REEMBOLSO') >= 500
```
- alternativa → [360753] Aviso para aprovação: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [360749] Inserir dados no ERP: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G81070] Aprovada? (DataBasedExclusiveDecision)
Codigo=APROV_GESTOR_GTW
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROV_GESTOR")
```
- alternativa → [360765] Aviso de aprovação: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [360766] Notificar cliente reprovado: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [360745] LinkInicial "Reembolso Creche"
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - DATA_PAGAMENTO "Data de pagamento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_PAGAMENTO] obrigatório
  - FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - COMBOBOX1 "Tipo de Benefício" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
  - NOME "Nome" [TextBox String → CP_ORDEM_SERVICO.NOME] obrigatório
  - OPCAO_DE_CONFIRMACAO "Dependente não cadastrado" [CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO]
  - REEMBOLSO_DECLARACAO "Declaro que não recebo de outra instituição, reembolso creche/pré-escola para este dependente." [CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO] obrigatório
  - REEMBOLSO_DECLARACAO_ESCOLA "Declaro que não recebo de outra instituição, reembolso escola para este dependente." [CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO_ESCOLA] obrigatório
  - VALOR_MENSALIDADE "Valor da mensalidade" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_MENSALIDADE] obrigatório
- Associação de subprocesso: AssociacaoId=349; FraseAssociacao=Reembolso Creche Chatbot -> Reembolso Creche; Nome=REEMBOLSOCRECHE

### [360764] EventoIntermediarioMensagem "Solicitação de Reembolso"
Destinatário: Fila CSC - Benefícios (papel 524)
Config: ListaDestinatarios=reembolsos.fopag@bbts.com.br
ModeloComunicado: Solicitação de Reembolso - Informação
Corpo do comunicado: Prezado(a) , 
O Solicitante OrdemServico.Cliente.Nome registrou a Ordem de Serviço nº OrdemServico.Numero solicitando o serviço de Reembolso OrdemServico.Servico. 
Prazo para atendimento de OrdemServico.TempoSLA.
Atenciosamente,
Central de Serviços

### [360746] LinkInicial "Reembolso Auxílio para Filho com Deficiência"
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - COMBOBOX1 "Tipo de Benefício" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
  - DATA_PAGAMENTO "Data de pagamento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_PAGAMENTO] obrigatório
  - NOME "Nome" [TextBox String → CP_ORDEM_SERVICO.NOME] obrigatório
  - OPCAO_DE_CONFIRMACAO "Dependente não cadastrado" [CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO]
  - REEMBOLSO_DECLARACAO "Declaro que não recebo de outra instituição, reembolso creche/pré-escola para este dependente." [CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO] obrigatório
  - REEMBOLSO_DECLARACAO_ESCOLA "Declaro que não recebo de outra instituição, reembolso escola para este dependente." [CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO_ESCOLA] obrigatório
  - VALOR_MENSALIDADE "Valor da mensalidade" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_MENSALIDADE] obrigatório
  - FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
- Associação de subprocesso: AssociacaoId=557; FraseAssociacao=Chatbot Reembolso Auxílio para Filho com Deficiência -> Reembolso; Nome=AUXFILHOCOMDEF

### [360761] LinkInicial "Reembolso Odontológico"
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - NOMEDEPENDENTE "Nome do dependente" [TextBox String → CPE_CSC.NOMEDEPENDENTE]
  - DATA_DOCUMENTO "Data do documento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_DOCUMENTO]
  - aSSUNTO
  - FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
  - LISTA_TRATAMENTO "LISTA_TRATAMENTO" [DataGrid RecordList → Z_00143_LISTA_TRATAMENTO.LISTA_TRATAMENTO]
    - coluna VALOR_PAGO obrigatório
    - coluna TRATAMENTO obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna VALOR_FINAL
    - coluna VALOR_TRATAMENTO obrigatório
  - NUM_NOTA_FISCAL "ID da Nota Fiscal" [TextBox Integer → CP_ORDEM_SERVICO.NUM_NOTA_FISCAL]
  - SERVICO_SELECIONADO "Serviço Selecionado" [TextBox String → CP_ORDEM_SERVICO.SERVICO_SELECIONADO]
- Associação de subprocesso: AssociacaoId=351; FraseAssociacao=Reembolso Odontológico Chatbot -> Reembolso Odontológico; Nome=REEMBOLSOODONTOLOGICOCHATBOT

### [360762] EventoIntermediarioMensagem "Aviso de abertura de chamado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Aviso de abertura de chamado
Corpo do comunicado: Prezado(a),
Foi aberta a ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [360763] Tarefa "Aprovação do Gestor"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=APROV_GESTOR
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovação do Gestor; MinimoAprovadores=1; ReprovarImediato=true; ReenvioEmailAprovacao=12; RotuloBotaoAprovar=Aprovar
  - (aprovação) DescricaoDetalhada (nativo)
  - aprovador: Cesec-PEAD Marina (Unico)
  - aprovador: Gerente Cesec PES (Unico)

### [360765] EventoIntermediarioMensagem "Aviso de aprovação"
Destinatário: Responsável atual (papel 36)
ModeloComunicado: Aviso de aprovação
Corpo do comunicado: Prezado(a),
O chamado interno OrdemServico.Numero - OrdemServico.Assunto foi aprovado.
Para mais detalhes sobre esta solicitação : Link.Consulta .
Atenciosamente
Central de Serviços

### [360744] Tarefa "Verificar Nota Fiscal
"
Referência: Instruções
 Verificar se o item da nota fiscal está de acordo com o receituário
Verificar se o valor a ser reembolsado está correto
 ATENÇÃO:
Caso altere algum valor na lista, recalcule (MANUALMENTE) o valor do reembolso.
Responsável: Fila CSC - Benefícios (papel 524)
Config: Regra=80; GrupoANO=G80%
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
pessoa = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))
OrdemServico["MATRICULA"] = pessoa["MATRICULA"].ToString()
```
**ScriptFim**
```python
OrdemServico["RESPONSAVEL_ATUAL"] = OrdemServico.ResponsavelId
OrdemServico["FAVORECIDO_TODOS"] = OrdemServico.ResponsavelId
```
**ScriptValidacao**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if String.IsNullOrEmpty(OrdemServico["MATRICULA"].ToString()):
   pessoa = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))
   OrdemServico["MATRICULA"] = pessoa["MATRICULA"]
   OrdemServico.Salva()
#
#Criticas.AdicionaAviso(OrdemServico["FAVORECIDO_COBRA"].ToString())
pessoa = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))
resp=OrdemServico.ResponsavelId
if pessoa.Id.ToString() == resp.ToString():
    Criticas.AdicionaPendencia("Não é permitido o Favorecido atender o próprio chamado.")
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
pessoa = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))
Formulario["FAVORECIDO_TODOS"].Valor = OrdemServico.ResponsavelId
Formulario["MATRICULA"].Valor = pessoa["MATRICULA"].ToString()
#Formulario.ExibeMensagem(pessoa["MATRICULA"].ToString())
#matricula = pessoa["MATRICULA"].ToString()
#OrdemServico.SetCustom("MATRICULA",matricula.ToString())
#Formulario.ExibeMensagem(OrdemServico["MATRICULA"].ToString())
#OrdemServico.Salva()

#Bloqueia a alteração do Favorecido
Formulario['FAVORECIDO_COBRA'].Habilitado = False

Formulario["PARCELAS_PID"].Habilitado = False
Formulario["PARCELAS_PID"].Visivel = False
Formulario["QUANTIDADE"].Habilitado = False

#Formulario["REEMBOLSO_DECLARACAO_MED"].Visivel = True
#Formulario["NOME"].Visivel = False
#Formulario["NOME"].Habilitado = False
#Formulario["REEMBOLSO_DECLARACAO_ESCOLA"].Habilitado = False
#Formulario["REEMBOLSO_DECLARACAO_ESCOLA"].Visivel = False
Formulario["DATA_DOCUMENTO"].Visivel = False
Formulario["DATA_DOCUMENTO"].Habilitado = False

Formulario["LISTA_TRATAMENTO"].Visivel = False

#--- Nome do dependente
#if (Formulario["OPCAO_DE_CONFIRMACAO"].Valor == True) :
#    Formulario["NOME"].Visivel = True
#    Formulario["NOME"].Habilitado = True

#--- Medicamento
if OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR":
    Formulario["LISTA_MEDICAMENTOS"].Habilitado = True
    Formulario["LISTA_MEDICAMENTOS"].Visivel = True
    #Formulario["DEP_FAVORECIDO_COBRA"].Visivel = False


#--- Escola/Creche/Pré-escola/Ótico
#if OrdemServico.Servico.Sigla == "ESCOLA" or OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR" or OrdemServico.Servico.Sigla == "CRECHECOLABORADOR" or OrdemServico.Servico.Sigla == "OTICOCOLABORADOR":
    #Formulario["DEP_FAVORECIDO_COBRA"].Visivel = True
    #Formulario["REEMBOLSO_DECLARACAO_MED"].Visivel = False
    #if OrdemServico.Servico.Sigla == "ESCOLA":
#        Formulario["REEMBOLSO_DECLARACAO_ESCOLA"].Habilitado = True
#        Formulario["REEMBOLSO_DECLARACAO_ESCOLA"].Visivel = True

#--- Odontológico
if OrdemServico.Servico.Sigla == "AUXODONTOLOGICO":
    #Formulario["NUM_NOTA_FISCAL"].Visivel = True
    #Formulario["NUM_NOTA_FISCAL"].Habilitado = True
    #Formulario["REEMBOLSO_DECLARACAO_MED"].Visivel = False
    Formulario["LISTA_TRATAMENTO"].Visivel = True
    Formulario["LISTA_TRATAMENTO"].Habilitado = False
    Formulario["DATA_PAGAMENTO"].Visivel = False
    Formulario["DATA_PAGAMENTO"].Habilitado = False
    Formulario["DATA_DOCUMENTO"].Visivel = True
    Formulario["DATA_DOCUMENTO"].Habilitado = True
    
if OrdemServico.Servico.Sigla == "OTICOCOLABORADOR":
    Formulario["LISTA_REEMBOLSO_OTICO"].Habilitado = False
    Formulario["LISTA_REEMBOLSO_OTICO"].Visivel = True
```
- Operação PR0001 Preencher Campos
  - FAVORECIDO_COBRA "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - QUANTIDADE "Parcelas Reembolso" [TextBox Integer → CP_ORDEM_SERVICO.QUANTIDADE] obrigatório
  - FAVORECIDO_TODOS "Responsável inícial" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
  - LISTA_MEDICAMENTOS "Lista de Medicamentos" [DataGrid RecordList → Z_00143_LISTA_MEDICAMENTOS.LISTA_MEDICAMENTOS] obrigatório
**LISTA_MEDICAMENTOS.ScriptModificado**
```python
FormularioRegistro["CNPJ"].Visivel = True
FormularioRegistro["CNPJ"].Habilitado = True
dt = OrdemServico.GetCustom("LISTA_NF")
itensCNPJ=''
itensNF=''
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ,CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = 636750")
#itensNF=DB.ExecuteDataTable("SELECT NUMERO_NF FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
contCNPJ=0
contNF=0
regdr=0
#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCNPJ=0
    igualNF=0
    regdr2=0
    
    for dr2 in dt.Rows:
        if (dr["CNPJ"]== dr2["CNPJ"]):
            if (regdr<=regdr2 and igualCNPJ==0):
                igualCNPJ=0
            else:
                igualCNPJ=1
        if (dr["NUMERO_NF"]== dr2["NUMERO_NF"]):
            if (regdr<=regdr2 and igualNF==0):
                igualNF=0
            else:
                igualNF=1
        regdr2=regdr2+1
    if (igualCNPJ<=0):
        if (contCNPJ==0):
            itensCNPJ=dr["CNPJ"]
            #itensCNPJ=dt.Rows.Count.ToString()
            contCNPJ=1
        else:
            itensCNPJ = itensCNPJ+';'+dr["CNPJ"]
    if (igualNF<=0):
        if (contNF==0):
            itensNF=dr["NUMERO_NF"]
            contNF=1
        else:
            itensNF = itensNF+';'+dr["NUMERO_NF"]
    regdr=regdr+1
FormularioRegistro["CNPJ"].Itens = itensCNPJ
FormularioRegistro["NUM_NOTA_FISCAL"].Itens = itensNF
```
    - coluna VALOR_MEDICAMENTO obrigatório
    - coluna CNPJ obrigatório
    - coluna TIPO obrigatório
    - coluna DEPENDENTE
    - coluna NUM_NOTA_FISCAL obrigatório
    - coluna NOME_MEDICAMENTO obrigatório
    - coluna DATA_RECEITA obrigatório
  - PARCELAS_PID "Parcelas Reembolso" [DropDownList Integer → CP_ORDEM_SERVICO.PARCELAS_PID]
  - VALOR_TOTAL_REEMBOLSO "Valor Total" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_TOTAL_REEMBOLSO] obrigatório
  - LISTA_REEMBOLSO_OTICO "Dados do Reembolso Ótico" [DataGrid RecordList → Z_00143_LISTA_REEMBOLSO_OTICO.LISTA_REEMBOLSO_OTICO]
    - coluna NOTA_FISCAL obrigatório
    - coluna NOME_DEPENDENTE
    - coluna TIPO_REEMBOLSO obrigatório
    - coluna DATA_RECEITA obrigatório
  - VALOR_REEMBOLSO "Valor do Reembolso" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO] obrigatório
  - LISTA_NF "ListaNF(informar COO apenas se não houver NF). Máximo de 3 Notas Fiscais" [DataGrid RecordList → Z_00143_LISTA_NF.LISTA_NF] — QtdColunasFormulario=1; PosicaoRotulo=Topo
    - coluna NUMERO_NF obrigatório
    - coluna CNPJ obrigatório
  - LISTA_TRATAMENTO "Lista de Tratamento Odontológico" [DataGrid RecordList → Z_00143_LISTA_TRATAMENTO.LISTA_TRATAMENTO]
    - coluna QUANTIDADE obrigatório
    - coluna TRATAMENTO obrigatório
    - coluna VALOR_TRATAMENTO obrigatório
    - coluna VALOR_PAGO obrigatório
    - coluna VALOR_FINAL
  - DATA_DOCUMENTO "Data do Orçamento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_DOCUMENTO]
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA]
  - VALOR_NOTA_FISCAL "Número do COO (Nota Fiscal)" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_NOTA_FISCAL] obrigatório
  - VALOR_MENSALIDADE "Valor da mensalidade" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_MENSALIDADE] obrigatório
  - DATA_PAGAMENTO "Data mês referência" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_PAGAMENTO]

### [360747] Tarefa "Informar Motivo da Reprovação"
Referência: Durante a verificação da Nota Fiscal, foi informado que a solicitação não deve ser aprovada visto que os documentos e nota(s) fiscal(is) não estão de acordo com o previsto no normativo. 
Informe o motivo da não aprovação com as orientações para que o solicitante corrija ou altere os dados da solicitação.
Responsável: Responsável atual da atividade (papel 340)
**ScriptFormCarregado**
```python
Formulario['RESPOSTA_REPROVACAO_REEMBOLSO'].Valor=OrdemServico.ObtemMotivoGateway("APROVACAO").ToString()
```
- Operação PR0001 Preencher Campos
  - RESPOSTA_REPROVACAO_REEMBOLSO "Justificativa da devolução:" [Memo String(2000) → CP_ORDEM_SERVICO.RESPOSTA_REPROVACAO_REEMBOLSO] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Anexo — RequeridoInicial=true

### [360748] LinkInicial "Reembolso Ótico"
Config: TipoMensagem=MensagemProcesso
- Associação de subprocesso: AssociacaoId=327; FraseAssociacao=Chatbot Reembolso Òtico -> Reembolso; Nome=CHATBOTREEMBOLSOOTICO

### [360749] Tarefa "Inserir dados no ERP"
Referência: Insira os dados no ERP conforme normativo
Responsável: Responsável atual da atividade (papel 340)
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
idFavorecido = Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA"))
favorecido = Pessoa.Carrega(idFavorecido)
nomeFavorecido = favorecido.Nome
orgao = Orgao.Carrega(favorecido.OrgaoId)
#sigla = orgao.Sigla
matricula = OrdemServico["MATRICULA"].ToString()
sigla = DB.ExecuteScalar ("SELECT SUBSTR(organizacao,1,10) as uor FROM cad_funcionario_v where matricula='" + matricula.ToString() + "'")
OrdemServico.SetCustom("SIGLA_SCR",sigla.ToString())
valorTotal = Convert.ToDecimal(OrdemServico["VALOR_TOTAL_REEMBOLSO"])
valor = OrdemServico["VALOR_REEMBOLSO"].ToString()
numero = OrdemServico.Numero.ToString()
fornecedor = '001.110001.3000001000.219340.000000.000.00000'


qry = "SELECT MAX(INICIO_DATA_FUNCAO), EMPRESA, SUBSTR('"+sigla.ToString()+"', 1, 1) AS PREFIXO  FROM CAD_FUNCIONARIO_V WHERE MATRICULA = '" + matricula.ToString() + "' GROUP BY EMPRESA"

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
#uor = OrdemServico["SIGLA_SCR"].ToString()
uor=DB.ExecuteScalar("select substr(organizacao,1,10) as uor from cad_funcionario_v where matricula='"+matricula.ToString()+"'")

termo = '00 DDL'

if OrdemServico.Servico.Sigla == "RPCDTERAPIAS":
    nota = 'RPDP'
    rubrica = '10512'
    
if OrdemServico.Servico.Sigla == "RPCDCONSULTAS":
    nota = 'RPDC'
    rubrica = '10512'
    
if OrdemServico.Servico.Sigla == "RPCDAVRUNIMED":
    nota = 'RPCU'
    rubrica = '10512'
    
if OrdemServico.Servico.Sigla == "RPCDAVRPARTICULARES":
    nota = 'RPCP'
    rubrica = '10512'
    
if OrdemServico.Servico.Sigla == "RPCDAVRCONJ":
    nota = 'RPCJ'
    rubrica = '10512'

if OrdemServico.Servico.Sigla == "CRECHECOLABORADOR":
    nota = 'RCRE'
    rubrica = '10516'

if OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR":
    nota = 'RPRE'
    rubrica = '10516'
    
if OrdemServico.Servico.Sigla == "ESCOLA":
    nota = 'RESC'
    rubrica = '10516'

if OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR":
    nota = 'RMED'
    rubrica = '10508'

if OrdemServico.Servico.Sigla == "OTICOCOLABORADOR":
    nota = 'ROTI'
    rubrica = '10507'

if OrdemServico.Servico.Sigla == "AUXODONTOLOGICO":
    nota = 'RODO'
    rubrica = '10504'
    
    if Convert.ToDecimal(valor) >= Convert.ToDecimal(OrdemServico["VALOR"]):
        termo = '00/30/60 DDL'
    #if valorTotal >= Convert.ToDecimal(OrdemServico["VALOR"]):
    #    termo = '00/30/60 DDL'
    
#--- Prefixo da conta contábil (337 quando a UOR iniciar com 1 ou 2 e 343 quando iniciar com 3 ou 4)
if inicio == '1' or inicio == '2':
    prefixo = '337'
else:
    prefixo = '343'
    
#--- Conta contábil (001.filial.uor.prefixo+rubrica)
conta = "001."+ filial +"."+ uor +"."+ prefixo + rubrica +".000000.000.00000"
OrdemServico.SetCustom("NUM_DOCU", conta)

#OrdemServico.AdicionaComentario('Conta contábil de débito no GL: '+ conta, False)
valor = DB.ExecuteScalar("select replace('"+ OrdemServico.GetCustom("VALOR_REEMBOLSO").ToString() + "',',','.') as valor from dual")
valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '99999D99') as valor from dual")
valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")

contInterfaceAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERIDAS from XXBBTSGATE.VW_BBTS_AP_INVOICES_INTERFACE where source LIKE '%SUPRAVIZIO%' AND invoice_num = '"+nota+""+OrdemServico.Numero.ToString() + "'")
    
contInterfaceGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")

contAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERIDAS from AP_INVOICES_ALL where source LIKE '%SUPRAVIZIO%' AND invoice_num = '"+nota+""+OrdemServico.Numero.ToString() + "'")
    
contGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")

#----- insert no GL PÀRA CONTABILIZAÇÃO (CONTABIL)

#--- débito
if contInterfaceGL.ToString()=='0' and contGL.ToString()=='0':
    OrdemServico.AdicionaComentario("Procedure para débito GL: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Lançamentos', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ", False)
    
    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Lançamentos', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ")
    
#--- crédito
    OrdemServico.AdicionaComentario("Procedure para débito GL: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Lançamentos', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ", False)
    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Lançamentos', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ")

#----- insert no AP (PARA PAGAMENTO)
contInterfaceGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")

contGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")

if contInterfaceAP.ToString()=='0' and contAP.ToString()=='0' and (contInterfaceGL.ToString()== '2' or contGL.ToString()== '2'):
    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota +""+ numero + "', SYSDATE+1, '"+ matricula +"', "+valor.ToString() +", '"+ fornecedor +"', '"+ termo +"', '"+ fornecedor +"') ")

    OrdemServico.AdicionaComentario("Procedure AP: call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota +""+ numero + "', SYSDATE+1, '"+ matricula +"', "+valor.ToString() +", '"+ fornecedor +"', '"+ termo +"','"+ fornecedor +"')", False)

OrdemServico.Salva()
AvancaProximaAtividade = True
```
**ScriptFim**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
#idFavorecido = Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA"))
#favorecido = Pessoa.Carrega(idFavorecido)
#nomeFavorecido = favorecido.Nome
#orgao = Orgao.Carrega(favorecido.OrgaoId)
#sigla = orgao.Sigla
#OrdemServico.SetCustom("SIGLA_SCR",sigla.ToString())
#
#matricula = OrdemServico["MATRICULA"].ToString()
#valorTotal = Convert.ToDecimal(OrdemServico["VALOR_TOTAL_REEMBOLSO"])
#valor = OrdemServico["VALOR_REEMBOLSO"].ToString()
#numero = OrdemServico.Numero.ToString()
#fornecedor = '001.110001.3000001000.219340.000000.000.00000'
#
#filial = OrdemServico["NUM_CHAVE"].ToString()
#inicio = OrdemServico["NUM_ITEM"].ToString()
#uor = sigla.ToString()
#termo = '00 DDL'
#
#if OrdemServico.Servico.Sigla == "RPCDTERAPIAS":
#    nota = 'RPDP'
#    rubrica = '10512'
#    
#if OrdemServico.Servico.Sigla == "RPCDCONSULTAS":
#    nota = 'RPDC'
#    rubrica = '10512'
#    
#if OrdemServico.Servico.Sigla == "RPCDAVRUNIMED":
#    nota = 'RPCU'
#    rubrica = '10512'
#    
#if OrdemServico.Servico.Sigla == "RPCDAVRPARTICULARES":
#    nota = 'RPCP'
#    rubrica = '10512'
#    
#if OrdemServico.Servico.Sigla == "RPCDAVRCONJ":
#    nota = 'RPCJ'
#    rubrica = '10512'
#
#if OrdemServico.Servico.Sigla == "CRECHECOLABORADOR":
#    nota = 'RCRE'
#    rubrica = '10516'
#
#if OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR":
#    nota = 'RPRE'
#    rubrica = '10516'
#    
#if OrdemServico.Servico.Sigla == "ESCOLA":
#    nota = 'RESC'
#    rubrica = '10516'
#
#if OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR":
#    nota = 'RMED'
#    rubrica = '10508'
#
#if OrdemServico.Servico.Sigla == "OTICOCOLABORADOR":
#    nota = 'ROTI'
#    rubrica = '10507'
#
#if OrdemServico.Servico.Sigla == "AUXODONTOLOGICO":
#    nota = 'RODO'
#    rubrica = '10504'
#    
#    if Convert.ToDecimal(valor) >= Convert.ToDecimal(OrdemServico["VALOR"]):
#        termo = '00/30/60 DDL'
#    #if valorTotal >= Convert.ToDecimal(OrdemServico["VALOR"]):
#    #    termo = '00/30/60 DDL'
#    
##--- Prefixo da conta contábil (337 quando a UOR iniciar com 1 ou 2 e 343 quando iniciar com 3 ou 4)
#if inicio == '1' or inicio == '2':
#    prefixo = '337'
#else:
#    prefixo = '343'
#    
##--- Conta contábil (001.filial.uor.prefixo+rubrica)
#conta = "001."+ filial +"."+ uor +"."+ prefixo + rubrica +".000000.000.00000"
#OrdemServico.SetCustom("NUM_DOCU", conta)
#
#OrdemServico.AdicionaComentario('Conta contábil de débito no GL: '+ conta, False)
#valor = DB.ExecuteScalar("select replace('"+ OrdemServico.GetCustom("VALOR_REEMBOLSO").ToString() + "',',','.') as valor from dual")
#valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '99999D99') as valor from dual")
#valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")
#
#contInterfaceAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERIDAS from XXBBTSGATE.VW_BBTS_AP_INVOICES_INTERFACE where source LIKE '%SUPRAVIZIO%' AND invoice_num = '"+nota+""+OrdemServico.Numero.ToString() + "'")
#    
#contInterfaceGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")
#
#contAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERIDAS from AP_INVOICES_ALL where source LIKE '%SUPRAVIZIO%' AND invoice_num = '"+nota+""+OrdemServico.Numero.ToString() + "'")
#    
#contGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")
#
#
##----- insert no GL
##--- débito
#if contInterfaceGL.ToString()=='0' and contGL.ToString()=='0':
#
#    OrdemServico.AdicionaComentario("Procedure para débito GL: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Lançamentos', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ", False)
#
#
#    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Lançamentos', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ")
#    #--- crédito
#    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Lançamentos', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ")
#
##----- insert no AP
#contInterfaceGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")
#
#contGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")
#
#if contInterfaceAP.ToString()=='0' and contAP.ToString()=='0' and (contInterfaceGL.ToString()>= '2' or contGL.ToString()>= '2'):
#    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota +""+ numero + "', SYSDATE+1, '"+ matricula +"', "+valor.ToString() +", '"+ fornecedor +"', '"+ termo +"') ")
#
#
##OrdemServico.AdicionaComentario("Procedure para débito GL: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Lançamentos', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"')", False)
##OrdemServico.AdicionaComentario("Procedure para crédito GL: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Lançamentos', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"')", False)
##OrdemServico.AdicionaComentario("Procedure AP: call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota +""+ numero + "', SYSDATE+1, '"+ matricula +"', "+valor.ToString() +", '"+ fornecedor +"', '"+ termo +"')", False)
#
#OrdemServico.Salva()
#
```
**ScriptValidacao**
```python
if OrdemServico.Servico.Sigla == "RPCDTERAPIAS":
    nota = 'RPDP'
    rubrica = '10512'
    
if OrdemServico.Servico.Sigla == "RPCDCONSULTAS":
    nota = 'RPDC'
    rubrica = '10512'
    
if OrdemServico.Servico.Sigla == "RPCDAVRUNIMED":
    nota = 'RPCU'
    rubrica = '10512'
    
if OrdemServico.Servico.Sigla == "RPCDAVRPARTICULARES":
    nota = 'RPCP'
    rubrica = '10512'
    
if OrdemServico.Servico.Sigla == "RPCDAVRCONJ":
    nota = 'RPCJ'
    rubrica = '10512'
    
if OrdemServico.Servico.Sigla == "CRECHECOLABORADOR":
    nota = 'RCRE'
    rubrica = '10516'

if OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR":
    nota = 'RPRE'
    rubrica = '10516'
    
if OrdemServico.Servico.Sigla == "ESCOLA":
    nota = 'RESC'
    rubrica = '10516'

if OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR":
    nota = 'RMED'
    rubrica = '10508'

if OrdemServico.Servico.Sigla == "OTICOCOLABORADOR":
    nota = 'ROTI'
    rubrica = '10507'

if OrdemServico.Servico.Sigla == "AUXODONTOLOGICO":
    nota = 'RODO'
    rubrica = '10504'
    

contInterfaceAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERIDAS from XXBBTSGATE.VW_BBTS_AP_INVOICES_INTERFACE where source LIKE '%SUPRAVIZIO%' AND invoice_num = '"+nota+""+OrdemServico.Numero.ToString() + "'")

contAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERIDAS from AP_INVOICES_ALL where source LIKE '%SUPRAVIZIO%' AND invoice_num = '"+nota+""+OrdemServico.Numero.ToString() + "'")
    
if contInterfaceAP.ToString()=='0':
    if contAP.ToString()=='0':
        Criticas.AdicionaPendencia("Não inseriu no AP")
    

contGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")
    
contInterfaceGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")

if contInterfaceGL.ToString()=='0':
    if contGL.ToString()=='0':
        Criticas.AdicionaPendencia("Não inseriu no GL")
```

### [360750] Tarefa "Calcular reembolso"
Referência: Atenção!
Verificar se o Valor do Reembolso está correto, comparando os valores lançados no sistema e os valores da nota em anexo.
Responsável: Fila CSC - Benefícios (papel 524)
Config: Regra=80; GrupoANO=G80%
**ScriptInicio**
```python
#--- Seleção de valores
OrdemServico.SetCustom("QUANTIDADE","1")
tratamento_tabela = 0
valor_tabela = 0
salario = 0
valorFixo = 0
porcentagem = 0
valor = 0
medicamento = 0
tratamento = 0
reembolso = 0
valorPMI = 0
matricula = OrdemServico.GetCustom("MATRICULA").ToString()
numero = OrdemServico.Numero.ToString()
servico = OrdemServico.Servico.Sigla.ToString()

#--- Seleção do salário do favorecido
lista = Utils.ExecuteDataTable(" SELECT REPLACE(TO_CHAR(PROPOSTA_SALARIAL),',','.') AS SALARIO FROM CAD_FUNCIONARIO_V WHERE ROWNUM = 1 AND MATRICULA = '"+ matricula +"' ")


#for linha in lista.Rows:
#    salario = linha["SALARIO"]

for linha in lista.Rows:
    if linha["SALARIO"] != DBNull.Value:
        salario = linha["SALARIO"]
    else:
        salario = 0


#--- Seleção de valores do reembolso

#--- Seleção de valores do reembolso
if (OrdemServico.Servico.Sigla == "CRECHECOLABORADOR") or (OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR") or (OrdemServico.Servico.Sigla == "ESCOLA"):

    lista = Utils.ExecuteDataTable(" SELECT NVL(RE.VALOR,0)  AS VALOR, NVL(RE.PORCENTAGEM,0) AS PORCENTAGEM, CP.DATA_PAGAMENTO, RE.DT_INICIO_VIG, RE.DT_FIM_VIG FROM TB_CAD_REEMBOLSO RE INNER JOIN SERVICO SE ON RE.SIGLA_SERVICO = SE.SIGLA INNER JOIN ORDEM_SERVICO OS ON SE.ID_SERVICO = OS.ID_SERVICO INNER JOIN OCORRENCIA OC ON OC.ID_OCORRENCIA = OS.ID_OCORRENCIA INNER JOIN CP_ORDEM_SERVICO CP ON OC.ID_OCORRENCIA = CP.ID_OCORRENCIA WHERE RE.SIGLA_SERVICO = '"+ servico +"' AND FAIXA_DE <= "+ salario.ToString() +" AND FAIXA_ATE >= "+ salario.ToString() +" AND OC.NUMERO = '"+ numero +"' AND CP.DATA_PAGAMENTO BETWEEN RE.DT_INICIO_VIG AND NVL(RE.DT_FIM_VIG, ADD_MONTHS(sysdate,12)) ")
else:

    lista = Utils.ExecuteDataTable(" SELECT NVL(RE.VALOR,0) AS VALOR, NVL(RE.PORCENTAGEM,0) AS PORCENTAGEM FROM TB_CAD_REEMBOLSO RE INNER JOIN SERVICO SE ON RE.SIGLA_SERVICO = SE.SIGLA INNER JOIN ORDEM_SERVICO OS ON SE.ID_SERVICO = OS.ID_SERVICO INNER JOIN OCORRENCIA OC ON OC.ID_OCORRENCIA = OS.ID_OCORRENCIA WHERE RE.SIGLA_SERVICO = '"+ servico +"' AND FAIXA_DE <= "+ salario.ToString() +" AND FAIXA_ATE >= "+ salario.ToString() +" AND OC.NUMERO = '"+ numero +"' AND RE.ATIVO = 'S' ")


for linha in lista.Rows:
    valorFixo = Convert.ToDecimal(linha["VALOR"])
    porcentagem = Convert.ToDecimal(linha["PORCENTAGEM"])
    if OrdemServico.GetCustom("SIM_NAO204") == "Sim":
        valorPMI = valorFixo * 2

#--- Salário mínimo / Salário Minimo no PMI é *2
if OrdemServico.GetCustom("SIM_NAO204") == "Sim":
    OrdemServico.SetCustom("VALOR", valorPMI)
else:
    OrdemServico.SetCustom("VALOR",valorFixo)


#---------- MEDICAMENTOS

#--- Calcular valor do reembolso
if (OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR"):
    #--- Verificando se o empregado faz parte do PMI 2025
    if OrdemServico.GetCustom("SIM_NAO204") == "Sim":
        listaMedicamentos = OrdemServico.GetCustom("LISTA_MEDICAMENTOS")
        if (listaMedicamentos != None):
            for listaMedicamentos in listaMedicamentos.Rows:
    #            medicamento = listaMedicamentos["VALOR_MEDICAMENTO"]
                if listaMedicamentos["VALOR_MEDICAMENTO"] != DBNull.Value:
                    medicamento = Convert.ToDecimal(listaMedicamentos["VALOR_MEDICAMENTO"])
                else:
                    medicamento = 0

                valor = valor + medicamento

            OrdemServico.SetCustom("VALOR_TOTAL_REEMBOLSO",valor)
            reembolso = (valor * porcentagem * 1.5)/100
            OrdemServico.SetCustom("VALOR_REEMBOLSO",reembolso)
    else:
        listaMedicamentos = OrdemServico.GetCustom("LISTA_MEDICAMENTOS")
        if (listaMedicamentos != None):
            for listaMedicamentos in listaMedicamentos.Rows:
    #            medicamento = listaMedicamentos["VALOR_MEDICAMENTO"]
                if listaMedicamentos["VALOR_MEDICAMENTO"] != DBNull.Value:
                    medicamento = Convert.ToDecimal(listaMedicamentos["VALOR_MEDICAMENTO"])
                else:
                    medicamento = 0

                valor = valor + medicamento

            OrdemServico.SetCustom("VALOR_TOTAL_REEMBOLSO",valor)
            reembolso = (valor * porcentagem)/100
            OrdemServico.SetCustom("VALOR_REEMBOLSO",reembolso)


#---------- ÓTICO

#--- Calcular valor do reembolso
if (OrdemServico.Servico.Sigla == "OTICOCOLABORADOR"):
    valor = OrdemServico.GetCustom("VALOR_NOTA_FISCAL")
    OrdemServico.SetCustom("VALOR_TOTAL_REEMBOLSO",valor)
    valor = (valor * porcentagem)/100
    
    #--- Só pode reembolsar o valor máximo (salário minimo)
    if (valor > valorFixo):
        valor = valorFixo
    OrdemServico.SetCustom("VALOR_REEMBOLSO",valor)


#---------- CRECHE E PRÉ-ESCOLA

#--- Cálculo reembolso
if (OrdemServico.Servico.Sigla == "CRECHECOLABORADOR") or (OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR"):
    #--- Verificando se o empregado faz parte do PMI 2025
    if OrdemServico.GetCustom("SIM_NAO204") == "Sim":
        reembolso = OrdemServico.GetCustom("VALOR_MENSALIDADE")
        OrdemServico.SetCustom("VALOR_TOTAL_REEMBOLSO",reembolso) 
        if (reembolso >= valorPMI):
            OrdemServico.SetCustom("VALOR_REEMBOLSO", valorPMI)
        else:
            OrdemServico.SetCustom("VALOR_REEMBOLSO", reembolso)
    else:
        reembolso = OrdemServico.GetCustom("VALOR_MENSALIDADE")
        OrdemServico.SetCustom("VALOR_TOTAL_REEMBOLSO",reembolso) 
        if (reembolso >= valorFixo):
            OrdemServico.SetCustom("VALOR_REEMBOLSO", valorFixo)
        else:
            OrdemServico.SetCustom("VALOR_REEMBOLSO", reembolso)
        
#--- Escola (Reembolso) 
if (OrdemServico.Servico.Sigla == "ESCOLA"):        
    reembolso = OrdemServico.GetCustom("VALOR_MENSALIDADE")
    OrdemServico.SetCustom("VALOR_TOTAL_REEMBOLSO",reembolso) 
    if (reembolso >= valorFixo):
        OrdemServico.SetCustom("VALOR_REEMBOLSO", valorFixo)
    else:
        OrdemServico.SetCustom("VALOR_REEMBOLSO", reembolso)



#---------- ODONTOLÓGICO

#--- Calcular valor do reembolso
if (OrdemServico.Servico.Sigla == "AUXODONTOLOGICO"):
    listaTratamento = OrdemServico.GetCustom("LISTA_TRATAMENTO")
    if (listaTratamento != None):
#        for lista in listaTratamento.Rows:
#            tratamento = lista["VALOR_PAGO"] * lista["QUANTIDADE"]
#            tratamento_tabela = lista["VALOR_TRATAMENTO"]* lista["QUANTIDADE"]
#            valor = valor + tratamento
#            valor_tabela = valor_tabela + tratamento_tabela
#
#        OrdemServico.SetCustom("VALOR_TOTAL_REEMBOLSO",valor)
#        reembolso = valor
#        
#        if valor > valor_tabela:
#            OrdemServico.SetCustom("VALOR_REEMBOLSO",valor_tabela)
#        else:
#            OrdemServico.SetCustom("VALOR_REEMBOLSO",valor)
#      
#        if ((valor >= valorFixo) and (valor_tabela >= valorFixo)) and (valorFixo >= 1):
#            OrdemServico.SetCustom("QUANTIDADE","3")
#            reembolso = reembolso/3

        valor_reembolsavel = 0     
        for lista in listaTratamento.Rows:
            tratamento = (lista["VALOR_PAGO"] / 2 ) * lista["QUANTIDADE"]
            tratamento_tabela = lista["VALOR_TRATAMENTO"] * lista["QUANTIDADE"]
            valor += (lista["VALOR_PAGO"] * lista["QUANTIDADE"])
            #valor_tabela = valor_tabela + tratamento_tabela
            
            if (lista["VALOR_PAGO"] / 2) >= lista["VALOR_TRATAMENTO"]:
                valor_reembolsavel += tratamento_tabela
            else:
                valor_reembolsavel += tratamento


        OrdemServico.SetCustom("VALOR_TOTAL_REEMBOLSO",valor)
        reembolso = valor_reembolsavel
        
        OrdemServico.SetCustom("VALOR_REEMBOLSO",valor_reembolsavel)
      
        if (valor_reembolsavel >= valorFixo and valorFixo >= 1):
            OrdemServico.SetCustom("QUANTIDADE","3")
            OrdemServico.SetCustom("VALOR", valorFixo)
            valor_reembolsavel = valor_reembolsavel/3  

AvancaProximaAtividade = True
OrdemServico.Salva()
```
**ScriptValidacao**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#pessoa = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))
#resp=OrdemServico.ResponsavelId
#if pessoa.Id.ToString()==resp.ToString():
# Criticas.AdicionaPendencia("Não é permitido o Favorecido atender o próprio chamado.")
```
**ScriptFormCarregado**
```python
Formulario["VALOR"].Visivel = False
```
- Operação PR0001 Preencher Campos
  - SIM_NAO204 "Empregado PMI" [DropDownList String → CPE_CONTRATOS02.SIM_NAO204] obrigatório
  - VALOR_TOTAL_REEMBOLSO "Valor Total" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_TOTAL_REEMBOLSO] obrigatório
  - PARCELAS_PID "Parcelas Reembolso" [DropDownList Integer → CP_ORDEM_SERVICO.PARCELAS_PID]
  - QUANTIDADE "Parcelas Reembolso" [TextBox Integer → CP_ORDEM_SERVICO.QUANTIDADE] obrigatório
  - VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - VALOR_REEMBOLSO "Valor do Reembolso" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO] obrigatório

### [360751] EventoIntermediarioTimer "Tempo para correção"
Config: TempoIntervalo=14400; MaximoExecucao=1
**ScriptEvento**
```python
OrdemServico.AvancaAtividade()
```

### [360752] EventoIntermediarioMensagem "Resposta Solicitação Aprovada"
Destinatário: Cliente (papel 18)
ModeloComunicado: Resposta da Solicitação de Reembolso - Aprovação
Corpo do comunicado: Prezado(a) , 
Complemento2, a solicitação de Número OrdemServico.Numero - Reembolso OrdemServico.Servico foi deferida e o valor a ser reembolsado será de Complemento1. 
Foi um prazer lhe atender.
Para continuar evoluindo com o nosso atendimento, gostaríamos de saber sua opinião. É bem rápido, leva menos de 1 minuto.
Para acessar nosso formulário da pesquisa de satisfação, clique nesse link Link.Pesquisa .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.GetCustom("VALOR_REEMBOLSO").ToString() +" reais."
Mensagem.Complemento2 = "Conforme NI 102 "

if ((OrdemServico.Servico.Sigla == "CRECHECOLABORADOR") or (OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR") or (OrdemServico.Servico.Sigla == "ESCOLA")) :
    Mensagem.Complemento2 = "Conforme NI 162 "
    
if (OrdemServico.Servico.Sigla == "AUXODONTOLOGICO"):
    Mensagem.Complemento2 = "Conforme NI 165 "

if (OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR"):
    Mensagem.Complemento2 = "Conforme NI 102 "
    
if (OrdemServico.Servico.Sigla == "OTICOCOLABORADOR"):
    Mensagem.Complemento2 = "Conforme NI 164 "

if (OrdemServico.GetCustom("QUANTIDADE") >= 2) :
    Mensagem.Complemento1 = OrdemServico.GetCustom("VALOR_REEMBOLSO").ToString() +" reais, este valor será parcelado em "+ OrdemServico.GetCustom("QUANTIDADE").ToString() + " parcelas iguais."
```

### [360753] EventoIntermediarioMensagem "Aviso para aprovação"
Destinatário: Gerente Cesec PES (papel 1310)
ModeloComunicado: Comunicado - Pendencia de Aprovação
Corpo do comunicado: Prezado(a),
O chamado interno OrdemServico.Numero - OrdemServico.Assunto.
Comunicamos que a atividade OrdemServico.Atividade está pendente de aprovação.

### [360754] EventoIntermediarioMensagem "Resposta Solicitação Reprovada"
Destinatário: Cliente e Favorecido Cobra (papel 312)
ModeloComunicado: Resposta da Solicitação de Reembolso - Reprovação
Corpo do comunicado: Prezado(a),
Por não atendimento a NI 102 a sua solitação de Número OrdemServico.Numero - Reembolso OrdemServico.Servico foi indeferida pelo motivo abaixo: 
OrdemServico.Customizado.RESPOSTA_REPROVACAO_REEMBOLSO 
Para mais detalhes sobre esta solicitação Link.Consulta.
Atenciosamente
Central de Serviços

### [360755] EventoIntermediarioMensagem "Enviar Atualização de dependentes"
Config: ListaDestinatarios=atualizacaocadastral@bbtecno.com.br; AnexarTodosDocumentos=true
ModeloComunicado: Solicitação Cadastro de Dependentes
Corpo do comunicado: Prezado(a), 
OrdemServico.Cliente.Nome abriu o chamado OrdemServico.Numero está solicitando o cadastro de dependentes, segue anexo o comprovante de dependência:
 Complemento1 
Atenciosamente,
Central de Serviços
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=1685; ClasseConfiguracao=Nota Fiscal
  - ClasseConfiguracaoId=1692; ClasseConfiguracao=Comprovação de dependência
  - ClasseConfiguracaoId=1693; ClasseConfiguracao=Receituário
  - ClasseConfiguracaoId=1694; ClasseConfiguracao=Comprovante de Pagamento Depósito
  - ClasseConfiguracaoId=1695; ClasseConfiguracao=Boleto Bancário
  - ClasseConfiguracaoId=2169; ClasseConfiguracao=Orçamento

### [360756] EventoIntermediarioMensagem "Devolução para ajustes"
Destinatário: Cliente e Responsavel Atual (papel 544)
Config: ListaDestinatarios=disec@bbts.com.br
ModeloComunicado: CSC Gestão de Pessoas - Benefícios - Devolução para ajustes
Corpo do comunicado: OrdemServico.Cliente.Nome,
A Ordem de Serviço número OrdemServico.Numero - Reembolso OrdemServico.Servico foi enviada pelo Cesec para sua responsabilidade para ajustes e/ou correções.
Motivos da devolução: OrdemServico.Customizado.RESPOSTA_REPROVACAO_REEMBOLSO
Após ajustes, clique no botão avançar na interface Workspace para o Cesec continuar com o reembolso.
IMPORTANTE: Caso esse(s) ajuste(s) não seja(m) realizado(s) dentro do prazo de 10 (dez) dias corridos, a Ordem de Serviço será FINALIZADA automaticamente.
Para ajustá-la, acesse a aplicação Supravizio e consulte a solicitação via tela Workspace através do link abaixo:
Edição Cliente Worklist: Link.Edicao Worklist 
Edição Cliente: Link.E…
**ScriptEvento**
```python
#.Assunto = "Comunicado de devolução para ajustes"
#Mensagem.Complemento1 = "A solicitação de número "+OrdemServico.NumeroSistema.ToString()+" - Reembolso "+OrdemServico.Servico.ToString()+" foi devolvida para sua caixa para a efetivação de ajuste(s) na(s) informação(ões) conforme lista abaixo, caso esse(s) ajuste(s) não seja(m) realizado(s) dentro do prazo de 10 (dez) dias corridos, o chamado será finalizado automaticamente.</br></br>Ajustes: "+OrdemServico.GetCustom('RESPOSTA_REPROVACAO_REEMBOLSO')+".</br>Acesse a aplicação Supravizio e consulte a solicitação via tela Workspace.</br> <a href='http://santacruz.bbts.com.br/Supravizio'> http://santacruz.bbts.com.br/Supravizio/</a></br> Ou </br> <a href='http://santacruz.bbtecno.com.br/Supravizio'> http://santacruz.bbtecno.com.br/Supravizio/</a></br></br>Atenciosamente,</br>Cesec/Disec"
```
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=2223; ClasseConfiguracao=Anexo

### [360757] Tarefa "Preencher Informações"
Responsável: Fila CSC - Benefícios (papel 524)
Config: Regra=80; GrupoANO=G80%
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
##PGESV###

idFavorecido = Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA"))
favorecido = Pessoa.Carrega(idFavorecido)
nomeFavorecido = favorecido.Nome
orgao = Orgao.Carrega(favorecido.OrgaoId)
sigla = orgao.Sigla
matricula = None
cpf = None


OrdemServico["CPF"] = favorecido["CPF"]
OrdemServico["MATRICULA"] = favorecido["MATRICULA"]
OrdemServico.SetCustom("SIGLA_SCR",sigla.ToString())


qry = "SELECT MAX(INICIO_DATA_FUNCAO), EMPRESA, SUBSTR('"+sigla.ToString()+"', 1, 1) AS PREFIXO  FROM CAD_FUNCIONARIO_V WHERE DATA_DE_DEMISSAO IS NULL AND MATRICULA = '" + favorecido["MATRICULA"] + "' GROUP BY EMPRESA"

lista = Utils.ExecuteDataTable(qry)
if (lista != None):
    for linha in lista.Rows:
        if (DBNull.Value.Equals(linha["EMPRESA"]) != True ):
            empresa = linha["EMPRESA"].ToString()
            OrdemServico.SetCustom("NUM_CHAVE",empresa.ToString())
            
        if (DBNull.Value.Equals(linha["PREFIXO"]) != True ):
            scr = linha["PREFIXO"].ToString()
            OrdemServico.SetCustom("NUM_ITEM",scr.ToString())        
        
            
    OrdemServico.Salva()
    AvancaProximaAtividade = True            

    

#OrdemServico.SetCustom("SIGLA_SCR",sigla.ToString())
#
#qry = "SELECT MAX(INICIO_DATA_FUNCAO), MATRICULA, CPF, EMPRESA, SUBSTR(NUMERO_SUBCR_NIVEL1, 1, 1) as PREFIXO FROM CAD_FUNCIONARIO_V WHERE DATA_DE_DEMISSAO IS NULL AND NOME = '" + nomeFavorecido + "' AND NUMERO_SUBCR_NIVEL1 = '" + sigla.ToString() + "' GROUP BY MATRICULA, CPF, EMPRESA, NUMERO_SUBCR_NIVEL1"
#
##qry = "SELECT MAX(INICIO_DATA_FUNCAO), MATRICULA, CPF FROM CAD_FUNCIONARIO_V WHERE DATA_DE_DEMISSAO IS NULL AND NOME = '" + nomeFavorecido + "' AND LPAD(NUMERO_SUBCR_NIVEL1,5) = LPAD('" + sigla.ToString() + "',5) GROUP BY MATRICULA, CPF"
#
#lista = Utils.ExecuteDataTable(qry)
#if (lista != None):
#    for linha in lista.Rows:
#        if (DBNull.Value.Equals(linha["CPF"]) != True ):
#            cpf = linha["CPF"].ToString()
#            OrdemServico.SetCustom("CPF",cpf.ToString())
#        
#        if (DBNull.Value.Equals(linha["MATRICULA"]) != True ):
#            matricula = linha["MATRICULA"].ToString()
#            OrdemServico.SetCustom("MATRICULA",matricula.ToString())
#            
#        if (DBNull.Value.Equals(linha["EMPRESA"]) != True ):
#            empresa = linha["EMPRESA"].ToString()
#            OrdemServico.SetCustom("NUM_CHAVE",empresa.ToString())    
#            
#        if (DBNull.Value.Equals(linha["PREFIXO"]) != True ):
#            scr = linha["PREFIXO"].ToString()
#            OrdemServico.SetCustom("NUM_ITEM",scr.ToString())    
#
#            
##    if (matricula != None and cpf != None) or (matricula != "" and cpf != ""):    
##        OrdemServico.SetCustom("CPF",cpf.ToString())
##        OrdemServico.SetCustom("MATRICULA",matricula.ToString())
#
#    OrdemServico.Salva()
#    AvancaProximaAtividade = True
```
**ScriptValidacao**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#pessoa = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))
#resp=OrdemServico.ResponsavelId
#if pessoa.Id.ToString()==resp.ToString():
# Criticas.AdicionaPendencia("Não é permitido o Favorecido atender o próprio chamado.")
```
**ScriptFormCarregado**
```python
Formulario["MATRICULA"].Visivel = True
```
- Operação PR0001 Preencher Campos
  - CPF "CPF" [TextBox String(15) → CP_ORDEM_SERVICO.CPF] obrigatório
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA] obrigatório

### [360758] EventoFinal ""
Config: TipoFinalizacao=NaoRealizado

### [360759] EventoFinal "Finalizada Sucesso"
Responsável: Favorecido Todos (papel 385)
Config: Codigo=EVENTOFINAL
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ocorrencia
#idOs = OrdemServico.Id

ocorrencia = Ocorrencia.Carrega(Convert.ToInt32(OrdemServico.Id))

ocorrencia.FinalizadorId = Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_TODOS"))
#ocorrenciaOS.Finalizador = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_TODOS")))

Ocorrencia.Salva(ocorrencia)

#OrdemServico.Salva()
```
**ScriptFim**
```python
OrdemServico.FinalizadorId = Convert.ToInt32(OrdemServico.ResponsavelId)
```
**ScriptValidacao**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if String.IsNullOrEmpty(OrdemServico["MATRICULA"].ToString()):
   pessoa = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))
   OrdemServico["MATRICULA"] = pessoa["MATRICULA"]
   OrdemServico.Salva()
```

### [360760] EventoInicial "Solicitação de reembolso"
Referência: Preencha as informações da solicitação do serviço no formulário.
Responsável: Fila CSC - Benefícios (papel 524)
Config: Codigo=EVENTO_INICIAL
TipoSolicitacao: 20.01. Gestão de Pessoas - Benefícios
**ScriptValidacao**
```python
from Venki.Supravizio.Processo.Custom import Evento
import validaCNPJ
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.
#mes=11
mes=OrdemServico.DataHoraCriacao.AddMonths(-2).Month
#Atendendo a OS 311519 para liberar por um período determinado a abertura de chamado até o mês de janeiro do ano anterior 
if (Convert.ToDateTime("16/02/2017") >= DateTime.Now):
        mes=1
        
numero = "0"
if (OrdemServico.Numero.ToString()!= ""):
    numero = OrdemServico.Numero.ToString()
favorecidoCobra = OrdemServico.GetCustom("FAVORECIDO_COBRA").ToString()

if OrdemServico.GetCustom("DEP_FAVORECIDO_COBRA").ToString()=='':
    OrdemServico.SetCustom("DEP_FAVORECIDO_COBRA",'99999')

#---------- VERIFICA A EDICAO DOS CAMPOS DE DEPENDENTES
#if (OrdemServico.GetCustom("OPCAO_DE_CONFIRMACAO") == True) and ((OrdemServico.GetCustom("NOME").ToString() == "") and (OrdemServico.GetCustom("DEP_FAVORECIDO_COBRA").ToString() == "" and OrdemServico.GetCustom("DEP_FAVORECIDO_COBRA").ToString() == 1)) :
#    Criticas.AdicionaPendencia("O campo Nome do Dependente é obrigatório.") 
#
if (OrdemServico.GetCustom("DEP_FAVORECIDO_COBRA").ToString() != "" and OrdemServico.GetCustom("DEP_FAVORECIDO_COBRA").ToString() != None and OrdemServico.GetCustom("DEP_FAVORECIDO_COBRA").ToString() != '99999'):
    dependenteCobra = OrdemServico.GetCustom("DEP_FAVORECIDO_COBRA").ToString()
   
else:
    
    if ((OrdemServico.GetCustom("NOME").ToString() != "") and (OrdemServico.GetCustom("OPCAO_DE_CONFIRMACAO") == True)):
        dependenteCobra = OrdemServico.GetCustom("NOME").ToString()
        
    else: 
        dependenteCobra = "IS NULL"
if ((OrdemServico.PossuiItem("CD") == False) and (OrdemServico.GetCustom("OPCAO_DE_CONFIRMACAO") == True)):
        Criticas.AdicionaPendencia("Não foi associado um(a) 'Comprovação de dependência'")
            
#---------- MEDICAMENTO

#--- Verifica se foi marcado o campo de declaração do medicamento para fins não estéticos
if ((OrdemServico.GetCustom("REEMBOLSO_DECLARACAO_MED")  == False) and (OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR")) :
    Criticas.AdicionaPendencia("A declaração da finalidade do medicamento é um campo obrigatório")

#--- Verifica se existe alguma medicamento comum
if (OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR"):
    listaMedicamentos = OrdemServico.GetCustom("LISTA_MEDICAMENTOS")
    listaNF = OrdemServico.GetCustom("LISTA_NF")
    #if (listaNF == None or listaMedicamentos == None):
    if (listaNF.Rows.Count == 0 or listaMedicamentos.Rows.Count == 0):    
        Criticas.AdicionaPendencia("Lista de NF(COO) e Lista de Medicamentos são obrigatórios!")
    else:
        cont = 0
        for linha in listaMedicamentos.Rows:
            cont += 0
            existeNF = 0
            existeCNPJ = 0
            for linhaNF in listaNF.Rows:
                if (linha["CNPJ"]==linhaNF["CNPJ"] and linha["NUM_NOTA_FISCAL"]==linhaNF["NUMERO_NF"]):
                    existeCNPJ = 1
                    existeNF = 1
                #if (linha["NUM_NOTA_FISCAL"]==linhaNF["NUMERO_NF"]):
            if (existeCNPJ == 0 or existeNF == 0):
                Criticas.AdicionaPendencia("NF ou CNPJ do medicamento "+linha["NOME_MEDICAMENTO"]+" não consta no campo Lista de NF(COO)")
            if (linha["TIPO"] == "Comum") and (Convert.ToDateTime(linha["DATA_RECEITA"]).AddDays(180).Date < DateTime.Now.Date) and (OrdemServico.Atividade.Codigo == "EVENTO_INICIAL"):
                #Criticas.AdicionaPendencia("Data da Receita não pode ser anterior a 100 dias.")
                Criticas.AdicionaPendencia("Data da Receita referente ao medicamento '"+linha["NOME_MEDICAMENTO"]+"' não pode ser anterior a " + Convert.ToString(DateTime.Now.AddDays(-180).Date))

            if (linha["TIPO"] == "Contínuo") and (Convert.ToDateTime(linha["DATA_RECEITA"]).AddDays(365).Date < DateTime.Now.Date) and (OrdemServico.Atividade.Codigo == "EVENTO_INICIAL"):
                #Criticas.AdicionaPendencia("Data da Receita não pode ser anterior a 220 dias.")
                Criticas.AdicionaPendencia("Data da Receita referente ao medicamento '"+linha["NOME_MEDICAMENTO"]+"' não pode ser anterior a " + Convert.ToString(DateTime.Now.AddDays(-365).Date))
                
            # Critica CNPJ
            resultado = validaCNPJ(linha["CNPJ"])
            if  resultado != "ok":
                Criticas.AdicionaPendencia("Linha: " + cont.ToString() + ". CNPJ " + resultado + " Inválido")
            if  String.IsNullOrEmpty(linha["NUM_NOTA_FISCAL"].ToString()):
                Criticas.AdicionaPendencia("Linha: " + cont.ToString() + ". Número da nota fiscal Inválido")
                resultado = "Erro"
            if  resultado == "ok" :
                # Verifica se já existe O.S. para a nota fiscal
                qry = "SELECT count(LM.NUM_NOTA_FISCAL) CONTADOR FROM OCORRENCIA OC INNER JOIN ORDEM_SERVICO OS ON OC.ID_OCORRENCIA = OS.ID_OCORRENCIA INNER JOIN SERVICO SE ON OS.ID_SERVICO = SE.ID_SERVICO INNER JOIN Z_00143_LISTA_MEDICAMENTOS LM ON LM.ID_OCORRENCIA = OC.ID_OCORRENCIA WHERE SE.SIGLA = '" + OrdemServico.Servico.Sigla + "' AND OC.NUMERO <> '" + numero + "' AND LM.NUM_NOTA_FISCAL = '" + linha["NUM_NOTA_FISCAL"] + "' AND OC.SITUACAO <> 'Cancelada' AND OC.SITUACAO <> 'FinalizadaNaoRealizada' AND LM.CNPJ = '" + linha["CNPJ"]+ "' group by LM.NUM_NOTA_FISCAL "
                lista = Utils.ExecuteDataTable(qry)
                
                ###Criticas.AdicionaPendencia(qry)
                
                numeroRegistro = 0
                for registro in lista.Rows:
                    numeroRegistro = registro["CONTADOR"]

                if (numeroRegistro >= 1):
                    Criticas.AdicionaPendencia("Linha: " + cont.ToString() + ". Já existe O.S. para o documento Fiscal número " + linha["NUM_NOTA_FISCAL"] + " do CNPJ " + linha["CNPJ"] + " - Solicite orientações abrindo um chamado no Fale com a Gepes, no menu acima .")

#---------- ÓTICO
if (OrdemServico.Servico.Sigla == "OTICOCOLABORADOR"):
    
#--- Verifica se já existe outro chamado aberto
    #--- Verifica se existe outro chamado aberto para o Cliente
    depend= " AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"')"
    if (dependenteCobra == "IS NULL"):
        depend= " AND (CPOS.DEP_FAVORECIDO_COBRA "+ dependenteCobra +" AND CPOS.NOME "+ dependenteCobra +")"
    lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O INNER JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) INNER JOIN PESSOA F ON (CPOS.FAVORECIDO_COBRA = to_char(F.ID_PESSOA)) WHERE S.ID_SERVICO = '"+ OrdemServico.ServicoId.ToString() +"' AND O.SITUACAO = 'Aberto' AND O.NUMERO <> '"+ numero +"' AND to_char(F.ID_PESSOA) = '"+ favorecidoCobra +"' "+ depend) 
    numeroRegistro = 0
    for linha in lista.Rows:
        numeroRegistro = linha["CONTADOR"]

    if (numeroRegistro >= 1):
        Criticas.AdicionaPendencia("Já existe um chamado aberto! Aguarde a verificação do Cesec para abrir outro") 
    else:

        #--- Verifica tempo para solicitação de material ótico
        consulta = Utils.ExecuteDataTable(" select * from (SELECT distinct ROUND((SYSDATE - OC.DATA_HORA_CRIACAO),0) as DIAS, Z.TIPO_REEMBOLSO, OC.DATA_HORA_CRIACAO FROM OCORRENCIA OC INNER JOIN ORDEM_SERVICO OS ON (OC.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO SE ON (OS.ID_SERVICO = SE.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (CPOS.ID_OCORRENCIA = OC.ID_OCORRENCIA) INNER JOIN PESSOA PE ON (CPOS.FAVORECIDO_COBRA = PE.ID_PESSOA) inner join cp_pessoa cpp on cpp.id_pessoa = pe.id_pessoa INNER JOIN CAD_FUNCIONARIO_V CA ON (CA.matricula = cpp.matricula) LEFT JOIN DEPENDENTES_BENEFICIOS_V DEP ON (DEP.MATRICULA = CA.MATRICULA and CPOS.DEP_FAVORECIDO_COBRA = DEP.NOME_DEPENDENTE) INNER JOIN Z_00143_LISTA_REEMBOLSO_OTICO Z ON (Z.ID_OCORRENCIA = OC.ID_OCORRENCIA) WHERE SE.ID_SERVICO = '"+ OrdemServico.ServicoId.ToString() +"' AND PE.ID_PESSOA = '"+ favorecidoCobra +"' AND OC.SITUACAO = 'FinalizadaSucesso' " + depend +" ORDER BY OC.DATA_HORA_CRIACAO DESC) where dias < 365")
        
        dia = 0 
        tipoJaPedido = ""
        listaOtico = OrdemServico.GetCustom("LISTA_REEMBOLSO_OTICO")
        
        
        # verifica itens permitidos na lista
        
        for linhaOtico in listaOtico.Rows:
            if (linhaOtico["DATA_RECEITA"] == "" or linhaOtico["DATA_RECEITA"] == None) :
                Criticas.AdicionaPendencia("Campo 'Data da Receita' é Obrigatório")
            else:
                dt = linhaOtico["DATA_RECEITA"].AddDays(365)
                if (dt < OrdemServico.DataHoraCriacao) :
                    Criticas.AdicionaPendencia("A data da receita é inferior a 365 dias da abertura da OS")

            for linha in consulta.Rows:
                erro = ""
                dia = linha["DIAS"].ToString() 
                tipoJaPedido = linha["TIPO_REEMBOLSO"].ToString() 
                if (tipoJaPedido == "Lente de Contato" or tipoJaPedido == "Armação/Lente"):
                    erro = "Já foi concedido Reembolso Ótico no último ano, não sendo permitido novo pedido neste período, para este titular ou dependente."
                elif (linhaOtico["TIPO_REEMBOLSO"] == tipoJaPedido):
                    erro = "O Reembolso Ótico para '" + tipoJaPedido + "' é concedido apenas uma vez por ano, um para o titular e um para cada dependente."
                elif (tipoJaPedido == "Armação" and linhaOtico["TIPO_REEMBOLSO"] != "Lente"):
                    erro = "Reembolso Ótico somente permitido para 'Lente', pois já foi concedido reembolso para 'Armação' no último ano, para este titular ou dependente."
                elif (tipoJaPedido == "Lente" and linhaOtico["TIPO_REEMBOLSO"] != "Armação"):
                    erro = "Reembolso Ótico somente permitido para 'Armação', pois já foi concedido reembolso para 'Lente' no último ano, para este titular ou dependente."
                if erro != "":
                    Criticas.AdicionaPendencia(erro)
                    break

#---------- ESCOLA(AUXÍLIO PARA FILHO COM DEFICIÊNCIA)

#--- Verifica se já possui chamado aberto

if (OrdemServico.Servico.Sigla == "ESCOLA"):
    if OrdemServico.GetCustom("DATA_PAGAMENTO") == "" or OrdemServico.GetCustom("DATA_PAGAMENTO") == None :
        Criticas.AdicionaPendencia("Campo 'Data mês referência' é Obrigatório")
    else:    
        if OrdemServico.GetCustom("DATA_PAGAMENTO")!= "":
            lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O INNER JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) INNER JOIN PESSOA F ON (CPOS.FAVORECIDO_COBRA = to_char(F.ID_PESSOA)) WHERE S.ID_SERVICO = '" + OrdemServico.ServicoId.ToString() + "' AND O.SITUACAO = 'Aberto' AND O.NUMERO <> '"+ numero +"' AND to_char(F.ID_PESSOA) = '"+ favorecidoCobra +"' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') ") 
            numeroRegistro = 0
            for linha in lista.Rows:
                numeroRegistro = linha["CONTADOR"]

            if (numeroRegistro >= 1):
                Criticas.AdicionaPendencia("Já existe um chamado aberto! Aguarde a verificação do Cesec para abrir outro") 
            else:
                lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) WHERE S.SIGLA = 'ESCOLA' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+ OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') AND O.SITUACAO = 'FinalizadaSucesso' ")
                numeroRegistro = 0
                for linha in lista.Rows:
                    numeroRegistro = linha["CONTADOR"]

                if (numeroRegistro > 0):
                    Criticas.AdicionaPendencia("Apenas um Auxílio para Filho(a) com Deficiência deve ser solicitado por mês")
                    
        else:
            Criticas.AdicionaPendencia("O campo Data mês referência é obrigatório") 
        if OrdemServico.GetCustom("REEMBOLSO_DECLARACAO_ESCOLA") == False:
            Criticas.AdicionaPendencia("A declaração de que não recebo reembolso escolar de outra intituição é um campo obrigatório")
    #if ((OrdemServico.GetCustom("DATA_PAGAMENTO").AddYears(1).Year < OrdemServico.DataHoraCriacao.Year) or ((OrdemServico.GetCustom("DATA_PAGAMENTO").AddYears(1).Year == OrdemServico.DataHoraCriacao.Year)and (OrdemServico.GetCustom("DATA_PAGAMENTO").Month < mes))or ((OrdemServico.GetCustom("DATA_PAGAMENTO").Year == OrdemServico.DataHoraCriacao.Year)and (OrdemServico.GetCustom("DATA_PAGAMENTO").AddMonths(-2).Month < mes)):
    #alteração para validação de data Ordem de serviço #357501 - Rosângela
    if ( Convert.ToDateTime("01" + "/" + OrdemServico["DATA_PAGAMENTO"].ToString("MM/yyyy")) < Convert.ToDateTime("01" + "/" + DateTime.AddMonths(DateTime.Now, -2).ToString("MM/yyyy")) ):
        Criticas.AdicionaPendencia("A 'Data mês referência' não pode ser anterior a "+DateTime.AddMonths(DateTime.Now, -2).ToString("MM/yyyy"))
        

#---------- CRECHE

#--- Verifica se já possui chamado aberto

if (OrdemServico.Servico.Sigla == "CRECHECOLABORADOR"):
    if OrdemServico.GetCustom("DATA_PAGAMENTO") == "" or OrdemServico.GetCustom("DATA_PAGAMENTO") == None :
        Criticas.AdicionaPendencia("Campo 'Data mês referência' é Obrigatório")
    else:    
        lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O INNER JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) INNER JOIN PESSOA F ON (CPOS.FAVORECIDO_COBRA = to_char(F.ID_PESSOA)) WHERE S.ID_SERVICO = '" + OrdemServico.ServicoId.ToString() + "' AND O.SITUACAO = 'Aberto' AND O.NUMERO <> '"+ numero +"' AND to_char(F.ID_PESSOA) = '"+ favorecidoCobra +"' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+ OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') ") 
        numeroRegistro = 0
        for linha in lista.Rows:
            numeroRegistro = linha["CONTADOR"]

        if (numeroRegistro >= 1):
            Criticas.AdicionaPendencia("Já existe um chamado aberto! Aguarde a verificação do Cesec para abrir outro") 
        else:
            lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) WHERE S.SIGLA = 'CRECHECOLABORADOR' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+ OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') AND O.SITUACAO = 'FinalizadaSucesso' ") 
            numeroRegistro = 0
            for linha in lista.Rows:
                numeroRegistro = linha["CONTADOR"]

            if (numeroRegistro > 0):
                Criticas.AdicionaPendencia("Apenas um Auxílio Creche deve ser solicitado por mês")
    #if (OrdemServico.GetCustom("DATA_PAGAMENTO").AddYears(1).Year < OrdemServico.DataHoraCriacao.Year) or ((OrdemServico.GetCustom("DATA_PAGAMENTO").AddYears(1).Year == OrdemServico.DataHoraCriacao.Year)and (OrdemServico.GetCustom("DATA_PAGAMENTO").Month < mes))or ((OrdemServico.GetCustom("DATA_PAGAMENTO").Year == OrdemServico.DataHoraCriacao.Year)and (OrdemServico.GetCustom("DATA_PAGAMENTO").AddMonths(-2).Month < mes)):
    #alteração para validação de data Ordem de serviço #357501 - Rosângela
    if ( Convert.ToDateTime("01" + "/" + OrdemServico["DATA_PAGAMENTO"].ToString("MM/yyyy")) < Convert.ToDateTime("01" + "/" + DateTime.AddMonths(DateTime.Now, -2).ToString("MM/yyyy")) ):
        Criticas.AdicionaPendencia("A 'Data mês referência' não pode ser anterior a "+DateTime.AddMonths(DateTime.Now, -2).ToString("MM/yyyy"))
        
#---------- PRE-ESCOLA

#--- Verifica se já possui chamado aberto

if (OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR"):  
    if OrdemServico.GetCustom("DATA_PAGAMENTO") == "" or OrdemServico.GetCustom("DATA_PAGAMENTO") == None :
        Criticas.AdicionaPendencia("Campo 'Data mês referência' é Obrigatório")
    else:    
        lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O INNER JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) INNER JOIN PESSOA F ON (CPOS.FAVORECIDO_COBRA = to_char(F.ID_PESSOA)) WHERE S.ID_SERVICO = '" + OrdemServico.ServicoId.ToString() + "' AND O.SITUACAO = 'Aberto' AND O.NUMERO <> '"+ numero +"' AND to_char(F.ID_PESSOA) = '"+ favorecidoCobra +"' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') ") 
        numeroRegistro = 0
        for linha in lista.Rows:
            numeroRegistro = linha["CONTADOR"]

        if (numeroRegistro >= 1):
            Criticas.AdicionaPendencia("Já existe um chamado aberto! Aguarde a verificação do Cesec para abrir outro") 
            
        else:
            if OrdemServico["OPCAO_DE_CONFIRMACAO"] == True:
                lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) JOIN PESSOA F ON (CPOS.FAVORECIDO_COBRA = to_char(F.ID_PESSOA)) WHERE S.SIGLA = 'PREESCOLACOLABORADOR' AND to_char(F.ID_PESSOA) = '"+ favorecidoCobra +"' AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+ OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') AND O.SITUACAO = 'FinalizadaSucesso' ")
                numeroRegistro = 0
                for linha in lista.Rows:
                    numeroRegistro = linha["CONTADOR"]
                
            else:
                lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) WHERE S.SIGLA = 'PREESCOLACOLABORADOR' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+ OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') AND O.SITUACAO = 'FinalizadaSucesso' ")
                numeroRegistro = 0
                for linha in lista.Rows:
                    numeroRegistro = linha["CONTADOR"]
            
        #else:
        #    lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) WHERE S.SIGLA = 'PREESCOLACOLABORADOR' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+ OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') AND O.SITUACAO = 'FinalizadaSucesso' ")
        #    numeroRegistro = 0
        #    for linha in lista.Rows:
        #        numeroRegistro = linha["CONTADOR"]
            
            if (numeroRegistro > 0):
                #Criticas.AdicionaPendencia(dependenteCobra.ToString())
                Criticas.AdicionaPendencia("Apenas um Auxílio Pré-Escola deve ser solicitado por mês")
                
    #if (OrdemServico.GetCustom("DATA_PAGAMENTO").AddYears(1).Year < OrdemServico.DataHoraCriacao.Year) or ((OrdemServico.GetCustom("DATA_PAGAMENTO").AddYears(1).Year == OrdemServico.DataHoraCriacao.Year)and (OrdemServico.GetCustom("DATA_PAGAMENTO").Month < mes))or ((OrdemServico.GetCustom("DATA_PAGAMENTO").Year == OrdemServico.DataHoraCriacao.Year)and (OrdemServico.GetCustom("DATA_PAGAMENTO").AddMonths(-2).Month < mes)):
    #alteração para validação de data Ordem de serviço #357501 - Rosângela
    if ( Convert.ToDateTime("01" + "/" + OrdemServico["DATA_PAGAMENTO"].ToString("MM/yyyy")) < Convert.ToDateTime("01" + "/" + DateTime.AddMonths(DateTime.Now, -2).ToString("MM/yyyy")) ):
        Criticas.AdicionaPendencia("A 'Data mês referência' não pode ser anterior a "+DateTime.AddMonths(DateTime.Now, -2).ToString("MM/yyyy"))


#---------- CRECHE E PRE-ESCOLA

#--- Verifica se foi marcado o campo de declaração de reembolso de outra instituição
if ((OrdemServico.GetCustom("REEMBOLSO_DECLARACAO")  == False) and ((OrdemServico.Servico.Sigla == "CRECHECOLABORADOR") or (OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR"))) :
    Criticas.AdicionaPendencia("A declaração de 'Declaro que não estou solicitando o auxílio babá, auxílio creche, auxílio pré escola ou auxílio filho com deficiência para o mesmo dependente na mesma competência.' é obrigatório")
if ((OrdemServico.GetCustom("REEMBOLSO_DECLARACAO_ESCOLA")  == False) and ((OrdemServico.Servico.Sigla == "CRECHECOLABORADOR") or (OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR"))) :
    Criticas.AdicionaPendencia("A declaração de 'Declaro não receber este benefício em outra instituição' é obrigatório")

#--- Campo Dependente obrigatório para Auxílio Creche e Pré-Escola

if ((OrdemServico.Servico.Sigla == "CRECHECOLABORADOR") or (OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR") or (OrdemServico.Servico.Sigla == "ESCOLA"))  and (OrdemServico.GetCustom("NOME") == "" and (OrdemServico.GetCustom("DEP_FAVORECIDO_COBRA") == 1 or OrdemServico.GetCustom("DEP_FAVORECIDO_COBRA") == "")):
    Criticas.AdicionaPendencia("Campo Dependente é Obrigatório!")



#---------- ODONTOLÓGICO

if (OrdemServico.Servico.Sigla == "AUXODONTOLOGICO"):
    if (OrdemServico.GetCustom("DEMANDA_PROC")  == False):
        Criticas.AdicionaPendencia("Por favor, declare não estar solicitando o mesmo tratamento dentro de 6 meses.")
    
    if OrdemServico.GetCustom("DATA_DOCUMENTO") == "" or OrdemServico.GetCustom("DATA_DOCUMENTO") == None :
        Criticas.AdicionaPendencia("Campo 'Data do Orçamento' é Obrigatório")
    else:
        dias = OrdemServico.GetCustom("DATA_DOCUMENTO").AddDays(61)
        if dias < OrdemServico.DataHoraCriacao :
            Criticas.AdicionaPendencia("A data do orçamento é superior a 60 dias da abertura da OS")
            
    #--- Verifica se existe outro chamado aberto para o Cliente

    depend= " AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"')"
    if (dependenteCobra == "is NULL"):
        depend= " AND (CPOS.DEP_FAVORECIDO_COBRA "+ dependenteCobra +" AND CPOS.NOME "+ dependenteCobra +")"
    
    lista = Utils.ExecuteDataTable("SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O INNER JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) INNER JOIN PESSOA F ON (to_char(CPOS.FAVORECIDO_COBRA) = to_char(F.ID_PESSOA)) WHERE S.ID_SERVICO = '"+ OrdemServico.ServicoId.ToString() +"' AND O.SITUACAO = 'Aberto' AND O.NUMERO <> '"+ numero +"' AND to_char(F.ID_PESSOA) = '"+ favorecidoCobra +"'"+ depend)
    numeroRegistro = 0
    for linha in lista.Rows:
        numeroRegistro = linha["CONTADOR"]

    if (numeroRegistro >= 1):
        Criticas.AdicionaPendencia("Já existe um chamado aberto! Aguarde a verificação do Cesec para abrir outro") 
    else:
        #--- Verifica tempo para solicitação de auxilio odontológico

        depend= " AND (CP.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CP.NOME = '"+ dependenteCobra +"')"
        if (dependenteCobra == "is NULL"):
            depend= " AND (CP.DEP_FAVORECIDO_COBRA "+ dependenteCobra +" AND CP.NOME "+ dependenteCobra +")"
    
        #consulta = Utils.ExecuteDataTable(" SELECT distinct ROUND((SYSDATE - OC.DATA_HORA_CRIACAO),0) as DIAS, OC.DATA_HORA_CRIACAO FROM OCORRENCIA OC INNER JOIN ORDEM_SERVICO OS ON (OC.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO SE ON (OS.ID_SERVICO = SE.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CP ON (CP.ID_OCORRENCIA = OC.ID_OCORRENCIA) INNER JOIN PESSOA PE ON (CP.FAVORECIDO_COBRA = PE.ID_PESSOA) INNER JOIN CAD_FUNCIONARIO_V CA ON (CA.NOME = PE.NOME) LEFT JOIN DEPENDENTES_BENEFICIOS_V DEP ON (DEP.MATRICULA = CA.MATRICULA and CP.DEP_FAVORECIDO_COBRA = DEP.NOME_DEPENDENTE) WHERE SE.ID_SERVICO = '"+ OrdemServico.ServicoId.ToString() +"' AND ROWNUM = 1 AND PE.ID_PESSOA = '"+ favorecidoCobra +"' AND OC.SITUACAO = 'FinalizadaSucesso'"+ depend +" ORDER BY OC.DATA_HORA_CRIACAO DESC ")
        
        
        
        #consulta = Utils.ExecuteDataTable(" SELECT distinct ROUND((SYSDATE - OC.DATA_HORA_CRIACAO),0) as DIAS, OC.DATA_HORA_CRIACAO FROM OCORRENCIA OC INNER JOIN ORDEM_SERVICO OS ON (OC.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO SE ON (OS.ID_SERVICO = SE.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CP ON (CP.ID_OCORRENCIA = OC.ID_OCORRENCIA) INNER JOIN PESSOA PE ON (CP.FAVORECIDO_COBRA = to_char(PE.ID_PESSOA)) inner join cp_pessoa cpp on cpp.id_pessoa = pe.id_pessoa INNER JOIN CAD_FUNCIONARIO_V CA ON (CA.matricula = cpp.matricula) WHERE SE.ID_SERVICO = '"+ OrdemServico.ServicoId.ToString() +"' AND ROWNUM = 1 AND PE.ID_PESSOA = '"+ favorecidoCobra +"' AND OC.SITUACAO = 'FinalizadaSucesso'"+ depend +" ORDER BY OC.DATA_HORA_CRIACAO DESC ")
        #dia = 0 
        #for linha in consulta.Rows: 
        #    dia = linha["DIAS"].ToString() 
        #    
        #    if (Convert.ToInt32(dia) < 180): 
        #        Criticas.AdicionaPendencia("Beneficiário já recebeu reembolso odontológico em menos de seis meses.")
        
        
# ============================================================
# REGRA DE CARENCIA POR TIPO DE MEDICAMENTO
#
# Grid: LISTA_MEDICAMENTOS
# Tabela fisica: Z_00143_LISTA_MEDICAMENTOS
#
# Regras:
#
# 1. Medicamentos a base de canabidiol:
#    carencia fixa de 1 mes.
#
# 2. Increnoativos:
#    QUANTIDADE 1 = carencia de 1 mes;
#    QUANTIDADE 2 = carencia de 2 meses;
#    QUANTIDADE 3 = carencia de 3 meses.
#
# 3. Formula infantil:
#    carencia fixa de 1 mes.
# ============================================================

def TextoCarenciaMedicamento(valor):
    try:
        if valor is None:
            return ""

        if valor == DBNull.Value:
            return ""

        texto = Convert.ToString(
            valor
        )

        if texto is None:
            return ""

        return texto.Trim()

    except:
        return ""


def NormalizarCarenciaMedicamento(valor):
    try:
        texto = TextoCarenciaMedicamento(
            valor
        ).ToUpper()

        while texto.Contains("  "):
            texto = texto.Replace(
                "  ",
                " "
            )

        return texto

    except:
        return ""


def SqlCarenciaMedicamento(valor):
    try:
        return TextoCarenciaMedicamento(
            valor
        ).Replace(
            "'",
            "''"
        )

    except:
        return ""


def ObterConfiguracaoCarencia(tipoMedicamento):
    tipoNormalizado = NormalizarCarenciaMedicamento(
        tipoMedicamento
    )

    if tipoNormalizado == "":
        return None


    # --------------------------------------------------------
    # CANABIDIOL
    # --------------------------------------------------------

    if (
        tipoNormalizado.Contains("CANABIDIOL")
    ):

        return {
            "CODIGO": "CANABIDIOL",
            "DESCRICAO": (
                "Medicamentos à base de canabidiol"
            ),
            "FILTRO_SQL": (
                "UPPER(TRIM(LM.TIPO)) "
                "LIKE '%CANABIDIOL%'"
            ),
            "QUANTIDADE_VARIAVEL": False
        }


    # --------------------------------------------------------
    # INCRENOATIVOS
    #
    # O diagnóstico confirmou que o texto salvo começa com:
    # Increnoativos: Ozempic, Mounjaro...
    # --------------------------------------------------------

    if (
        tipoNormalizado.Contains("INCRENOATIVO") or
        tipoNormalizado.Contains("INCRETINICO") or
        tipoNormalizado.Contains("INCRETÍNICO") or
        tipoNormalizado.Contains("OZEMPIC") or
        tipoNormalizado.Contains("MOUNJARO")
    ):

        return {
            "CODIGO": "INCRENOATIVOS",
            "DESCRICAO": (
                "Medicamentos incretínicos, como "
                "Ozempic e Mounjaro"
            ),
            "FILTRO_SQL": (
                "("
                "UPPER(TRIM(LM.TIPO)) "
                "LIKE '%INCRENOATIVO%' "
                "OR UPPER(TRIM(LM.TIPO)) "
                "LIKE '%INCRETINICO%' "
                "OR UPPER(TRIM(LM.TIPO)) "
                "LIKE '%OZEMPIC%' "
                "OR UPPER(TRIM(LM.TIPO)) "
                "LIKE '%MOUNJARO%'"
                ")"
            ),
            "QUANTIDADE_VARIAVEL": True
        }


    # --------------------------------------------------------
    # FORMULA INFANTIL
    # --------------------------------------------------------

    if (
        tipoNormalizado.Contains("FORMULA INFANTIL") or
        tipoNormalizado.Contains("FÓRMULA INFANTIL")
    ):

        return {
            "CODIGO": "FORMULA_INFANTIL",
            "DESCRICAO": "Fórmula infantil",
            "FILTRO_SQL": (
                "("
                "UPPER(TRIM(LM.TIPO)) "
                "LIKE '%FORMULA INFANTIL%' "
                "OR UPPER(TRIM(LM.TIPO)) "
                "LIKE '%FÓRMULA INFANTIL%'"
                ")"
            ),
            "QUANTIDADE_VARIAVEL": False
        }


    return None


# ============================================================
# EXECUTA SOMENTE NO SERVICO DE MEDICAMENTOS
# ============================================================

if OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR":

    listaMedicamentosCarencia = None

    try:
        listaMedicamentosCarencia = OrdemServico.GetCustom(
            "LISTA_MEDICAMENTOS"
        )

    except:
        listaMedicamentosCarencia = None


    if listaMedicamentosCarencia is not None:

        favorecidoCarencia = TextoCarenciaMedicamento(
            OrdemServico.GetCustom(
                "FAVORECIDO_COBRA"
            )
        )

        numeroOsCarencia = TextoCarenciaMedicamento(
            OrdemServico.Numero
        )

        servicoIdCarencia = TextoCarenciaMedicamento(
            OrdemServico.ServicoId
        )


        # ====================================================
        # IDENTIFICA OS TIPOS LIMITADOS DA GRID ATUAL
        #
        # O dicionario evita validar duas vezes quando houver
        # mais de uma linha do mesmo tipo na mesma solicitacao.
        # ====================================================

        tiposAtuaisCarencia = {}


        for linhaAtualCarencia in (
            listaMedicamentosCarencia.Rows
        ):

            tipoAtualCarencia = ""
            quantidadeAtualCarencia = ""


            try:
                tipoAtualCarencia = TextoCarenciaMedicamento(
                    linhaAtualCarencia["TIPO"]
                )

            except:
                tipoAtualCarencia = ""


            try:
                quantidadeAtualCarencia = (
                    TextoCarenciaMedicamento(
                        linhaAtualCarencia["QUANTIDADE"]
                    )
                )

            except:
                quantidadeAtualCarencia = ""


            configuracaoAtualCarencia = (
                ObterConfiguracaoCarencia(
                    tipoAtualCarencia
                )
            )


            if configuracaoAtualCarencia is None:
                continue


            codigoTipoAtual = configuracaoAtualCarencia[
                "CODIGO"
            ]


            # ------------------------------------------------
            # VALIDA A QUANTIDADE INFORMADA NA OS ATUAL
            # PARA OS MEDICAMENTOS INCRENOATIVOS
            # ------------------------------------------------

            if configuracaoAtualCarencia[
                "QUANTIDADE_VARIAVEL"
            ]:

                if quantidadeAtualCarencia not in [
                    "1",
                    "2",
                    "3"
                ]:

                    Criticas.AdicionaPendencia(
                        (
                            "Para medicamentos incretínicos, "
                            "como Ozempic e Mounjaro, o campo "
                            "Quantidade deve ser preenchido "
                            "com 1, 2 ou 3."
                        )
                    )


            if codigoTipoAtual not in tiposAtuaisCarencia:

                tiposAtuaisCarencia[
                    codigoTipoAtual
                ] = configuracaoAtualCarencia


        # ====================================================
        # VALIDA AS SOLICITACOES ANTERIORES
        # ====================================================

        if len(tiposAtuaisCarencia) > 0:

            if favorecidoCarencia == "":

                Criticas.AdicionaPendencia(
                    "Selecione o funcionário antes de continuar."
                )

            else:

                favorecidoCarenciaSql = SqlCarenciaMedicamento(
                    favorecidoCarencia
                )


                # ------------------------------------------------
                # EXCLUI A OS ATUAL SOMENTE SE ELA TIVER NUMERO
                #
                # No Evento Inicial, o numero ainda pode estar
                # vazio. No Oracle, '' equivale a NULL.
                # ------------------------------------------------

                filtroOsAtualCarencia = ""

                if numeroOsCarencia != "":

                    filtroOsAtualCarencia = (
                        "AND O.NUMERO <> '" +
                        SqlCarenciaMedicamento(
                            numeroOsCarencia
                        ) +
                        "' "
                    )


                for codigoTipoCarencia in tiposAtuaisCarencia:

                    configuracaoCarencia = (
                        tiposAtuaisCarencia[
                            codigoTipoCarencia
                        ]
                    )

                    descricaoTipoCarencia = (
                        configuracaoCarencia[
                            "DESCRICAO"
                        ]
                    )

                    filtroTipoCarencia = (
                        configuracaoCarencia[
                            "FILTRO_SQL"
                        ]
                    )

                    quantidadeVariavelCarencia = (
                        configuracaoCarencia[
                            "QUANTIDADE_VARIAVEL"
                        ]
                    )


                    # ============================================
                    # DEFINE O NUMERO DE MESES DE CARENCIA
                    #
                    # Para incretínicos, utiliza QUANTIDADE da
                    # solicitacao anterior.
                    #
                    # Para os demais tipos, utiliza 1 mes.
                    # ============================================

                    if quantidadeVariavelCarencia:

                        mesesCarenciaSql = (
                            "CASE "
                            "WHEN TRIM(LM.QUANTIDADE) = '1' "
                            "THEN 1 "
                            "WHEN TRIM(LM.QUANTIDADE) = '2' "
                            "THEN 2 "
                            "WHEN TRIM(LM.QUANTIDADE) = '3' "
                            "THEN 3 "
                            "ELSE 1 "
                            "END"
                        )

                    else:

                        mesesCarenciaSql = "1"


                    # ============================================
                    # CONSULTA AS SOLICITACOES QUE AINDA ESTAO
                    # DENTRO DO PERIODO DE CARENCIA
                    #
                    # A consulta retorna individualmente os
                    # registros ainda bloqueantes.
                    # ============================================

                    sqlValidacaoCarencia = (
                        "SELECT * FROM ("

                        "SELECT "
                        "O.ID_OCORRENCIA, "
                        "O.NUMERO AS NUMERO_OS, "
                        "O.DATA_HORA_CRIACAO AS DATA_OS, "
                        "O.SITUACAO, "
                        "LM.TIPO, "
                        "TRIM(LM.QUANTIDADE) AS QUANTIDADE, "

                        + mesesCarenciaSql +

                        " AS MESES_CARENCIA, "

                        "ADD_MONTHS("
                        "O.DATA_HORA_CRIACAO, "

                        + mesesCarenciaSql +

                        ") AS DATA_LIBERACAO "

                        "FROM OCORRENCIA O "

                        "INNER JOIN ORDEM_SERVICO OS "
                        "ON OS.ID_OCORRENCIA = "
                        "O.ID_OCORRENCIA "

                        "INNER JOIN CP_ORDEM_SERVICO CPOS "
                        "ON CPOS.ID_OCORRENCIA = "
                        "O.ID_OCORRENCIA "

                        "INNER JOIN "
                        "Z_00143_LISTA_MEDICAMENTOS LM "
                        "ON LM.ID_OCORRENCIA = "
                        "O.ID_OCORRENCIA "

                        "WHERE OS.ID_SERVICO = "

                        + servicoIdCarencia +

                        " "

                        "AND TO_CHAR("
                        "CPOS.FAVORECIDO_COBRA"
                        ") = '"

                        + favorecidoCarenciaSql +

                        "' "

                        + filtroOsAtualCarencia +

                        "AND UPPER(TRIM(O.SITUACAO)) "
                        "NOT IN ("
                        "'CANCELADO', "
                        "'CANCELADA', "
                        "'REPROVADO', "
                        "'REPROVADA', "
                        "'FINALIZADANAOREALIZADA'"
                        ") "

                        "AND "

                        + filtroTipoCarencia +

                        " "

                        "AND SYSDATE < "
                        "ADD_MONTHS("
                        "O.DATA_HORA_CRIACAO, "

                        + mesesCarenciaSql +

                        ") "

                        "ORDER BY "
                        "O.DATA_HORA_CRIACAO DESC"

                        ") "

                        "WHERE ROWNUM = 1"
                    )


                    try:
                        dadosCarencia = Utils.ExecuteDataTable(
                            sqlValidacaoCarencia
                        )

                        if dadosCarencia.Rows.Count > 0:

                            registroCarencia = (
                                dadosCarencia.Rows[0]
                            )

                            numeroOsAnteriorCarencia = (
                                TextoCarenciaMedicamento(
                                    registroCarencia[
                                        "NUMERO_OS"
                                    ]
                                )
                            )

                            quantidadeAnteriorCarencia = (
                                TextoCarenciaMedicamento(
                                    registroCarencia[
                                        "QUANTIDADE"
                                    ]
                                )
                            )

                            mesesCarencia = 1

                            try:
                                mesesCarencia = Convert.ToInt32(
                                    registroCarencia[
                                        "MESES_CARENCIA"
                                    ]
                                )

                            except:
                                mesesCarencia = 1


                            dataSolicitacaoCarencia = None
                            dataLiberacaoCarencia = None


                            try:
                                dataSolicitacaoCarencia = (
                                    registroCarencia[
                                        "DATA_OS"
                                    ]
                                )

                            except:
                                dataSolicitacaoCarencia = None


                            try:
                                dataLiberacaoCarencia = (
                                    registroCarencia[
                                        "DATA_LIBERACAO"
                                    ]
                                )

                            except:
                                dataLiberacaoCarencia = None


                            # ====================================
                            # MONTA A MENSAGEM
                            # ====================================

                            mensagemCarencia = (
                                "Já existe uma solicitação de " +
                                descricaoTipoCarencia +
                                " dentro do período de carência."
                            )


                            if numeroOsAnteriorCarencia != "":

                                mensagemCarencia += (
                                    " OS encontrada: " +
                                    numeroOsAnteriorCarencia +
                                    "."
                                )


                            if (
                                dataSolicitacaoCarencia is not None and
                                dataSolicitacaoCarencia != DBNull.Value
                            ):

                                try:
                                    mensagemCarencia += (
                                        " Data da solicitação: " +
                                        Convert.ToDateTime(
                                            dataSolicitacaoCarencia
                                        ).ToString(
                                            "dd/MM/yyyy"
                                        ) +
                                        "."
                                    )

                                except:
                                    pass


                            if quantidadeVariavelCarencia:

                                mensagemCarencia += (
                                    " Quantidade informada na "
                                    "solicitação anterior: " +
                                    quantidadeAnteriorCarencia +
                                    "."
                                )


                            mensagemCarencia += (
                                " Período de carência: " +
                                Convert.ToString(
                                    mesesCarencia
                                )
                            )


                            if mesesCarencia == 1:

                                mensagemCarencia += " mês."

                            else:

                                mensagemCarencia += " meses."


                            if (
                                dataLiberacaoCarencia is not None and
                                dataLiberacaoCarencia != DBNull.Value
                            ):

                                try:
                                    mensagemCarencia += (
                                        " Uma nova solicitação "
                                        "poderá ser realizada "
                                        "a partir de " +
                                        Convert.ToDateTime(
                                            dataLiberacaoCarencia
                                        ).ToString(
                                            "dd/MM/yyyy"
                                        ) +
                                        "."
                                    )

                                except:
                                    pass


                            Criticas.AdicionaPendencia(
                                mensagemCarencia
                            )


                    except Exception as exCarencia:

                        Criticas.AdicionaPendencia(
                            (
                                "Não foi possível validar a carência "
                                "para {0}. Detalhes: {1}"
                            ).format(
                                descricaoTipoCarencia,
                                TextoCarenciaMedicamento(
                                    exCarencia
                                )
                            )
                        )
```
**ScriptFormCarregado**
```python
OrdemServico.Assunto = OrdemServico.Servico.Descricao
Formulario["REEMBOLSO_DECLARACAO_MED"].Visivel = True
Formulario["NOME"].Visivel = False
Formulario["NOME"].Habilitado = False
Formulario["SIM_NAO204"].Visivel = False
Formulario["SIM_NAO204"].Habilitado = False
Formulario["MATRICULA"].Visivel = False
Formulario["MATRICULA"].Habilitado = False
Formulario["REEMBOLSO_DECLARACAO_ESCOLA"].Habilitado = False
Formulario["REEMBOLSO_DECLARACAO_ESCOLA"].Visivel = False
Formulario["DATA_DOCUMENTO"].Visivel = False
Formulario["DATA_DOCUMENTO"].Habilitado = False
Formulario["LISTA_NF"].Habilitado = False
Formulario["LISTA_NF"].Visivel = False
Formulario["COMBOBOX1"].Visivel = False
Formulario["COMBOBOX1"].Habilitado = False
Formulario["LISTAPCD_TERAPIAS"].Visivel = False
Formulario["LISTAPCD_TERAPIAS"].Habilitado = False
Formulario["LISTAPCD_COO"].Visivel = False
Formulario["LISTAPCD_COO"].Habilitado = False
Formulario["DEMANDA_PROC"].Visivel = False
Formulario["DEMANDA_PROC"].Habilitado = False
Formulario["DEMANDA_PROC"].Valor = False
Formulario["COUNT_10"].Visivel = False
Formulario["COUNT_10"].Habilitado = False
Formulario["LISTA_TRATAMENTO"].Visivel = False
Formulario["SIM_NAO204"].Habilitado = False


#Formulario["FAVORECIDO_COBRA"].Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")

Formulario["LABEL2"].Valor = '<table><br>___________________________________________________________________________________________________<br><br><b><font color="red">Informe o número da Nota Fiscal (sem pontos ou traços), seguindo estes critérios de prioridade:</font></b><br>1º - nº da NF; caso não tenha ;<br>2º - nº do cupom; caso não tenha;<br>3º - nº COO; caso não tenha;<br>4º - nº do extrato;<br>5º - nº SAT<br>___________________________________________________________________________________________________<br><br></table>'

#--- Nome do dependente
if (Formulario["OPCAO_DE_CONFIRMACAO"].Valor == True) :
    Formulario["NOME"].Visivel = True
    Formulario["NOME"].Habilitado = True

#--- PCD Terapias - Plano e saúde Modalidade Reembolso
if OrdemServico.Servico.Sigla == "RPCDCONSULTAS" or OrdemServico.Servico.Sigla == "RPCDAVRPARTICULARES" or OrdemServico.Servico.Sigla == "RPCDAVRUNIMED":
    Formulario["LISTA_NF"].Habilitado = True
    Formulario["LISTA_NF"].Visivel = True
    Formulario["LISTAPCD_TERAPIAS"].Visivel = True
    Formulario["LISTAPCD_TERAPIAS"].Habilitado = True
    Formulario["DEP_FAVORECIDO_COBRA"].Visivel = False
    Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = False
    Formulario["REEMBOLSO_DECLARACAO_MED"].Visivel = False
    Formulario["DEMANDA_PROC"].Visivel = False
    Formulario["DEMANDA_PROC"].Habilitado = False
    
#--- PCD Terapias - Consultas Avulsas
if OrdemServico.Servico.Sigla == "RPCDTERAPIAS" or OrdemServico.Servico.Sigla == "RPCDAVRCONJ":
    Formulario["LISTAPCD_COO"].Visivel = True
    Formulario["LISTAPCD_COO"].Habilitado = True
    Formulario["DEP_FAVORECIDO_COBRA"].Visivel = False
    Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = False
    Formulario["REEMBOLSO_DECLARACAO_MED"].Visivel = False
    Formulario["DEMANDA_PROC"].Visivel = False
    Formulario["DEMANDA_PROC"].Habilitado = False

#--- Medicamento
if OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR":
    Formulario["LISTA_NF"].Habilitado = True
    Formulario["LISTA_NF"].Visivel = True
    Formulario["DEMANDA_PROC"].Visivel = False
    Formulario["DEMANDA_PROC"].Habilitado = False
    Formulario["DEP_FAVORECIDO_COBRA"].Visivel = False
    Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = False
    Formulario["SIM_NAO204"].Visivel = True
    Formulario["SIM_NAO204"].Habilitado = False

#--- Escola/Creche/Pré-escola/Ótico
if OrdemServico.Servico.Sigla == "ESCOLA" or OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR" or OrdemServico.Servico.Sigla == "CRECHECOLABORADOR" or OrdemServico.Servico.Sigla == "OTICOCOLABORADOR":
    Formulario["DEMANDA_PROC"].Visivel = False
    Formulario["DEMANDA_PROC"].Habilitado = False
    Formulario["FAVORECIDO_COBRA"].Valor = None
    Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = False
    Formulario["DEP_FAVORECIDO_COBRA"].Visivel = True
    Formulario["DEP_FAVORECIDO_COBRA"].Valor = None
    Formulario["REEMBOLSO_DECLARACAO_MED"].Visivel = False
    Formulario["REEMBOLSO_DECLARACAO_ESCOLA"].Visivel = True
    Formulario["REEMBOLSO_DECLARACAO_ESCOLA"].Habilitado = True    
    if OrdemServico.Servico.Sigla == "ESCOLA":
        Formulario["REEMBOLSO_DECLARACAO_ESCOLA"].Habilitado = True
        Formulario["REEMBOLSO_DECLARACAO_ESCOLA"].Visivel = True
    Formulario["OPCAO_DE_CONFIRMACAO"].Visivel = True
    Formulario["OPCAO_DE_CONFIRMACAO"].Habilitado = True
    
        
if OrdemServico.Servico.Sigla == "ESCOLA":
    Formulario["COMBOBOX1"].Visivel = True
    Formulario["COMBOBOX1"].Habilitado = True
    Formulario["COMBOBOX1"].Itens = "Auxílio Educacional;Auxílio Babá"
    Formulario["DEMANDA_PROC"].Visivel = False
    Formulario["DEMANDA_PROC"].Habilitado = False

if OrdemServico.Servico.Sigla == "CRECHECOLABORADOR":
    Formulario["COMBOBOX1"].Visivel = True
    Formulario["COMBOBOX1"].Habilitado = True
    Formulario["COMBOBOX1"].Itens = "Auxílio Creche;Auxílio Babá"
    Formulario["DEMANDA_PROC"].Visivel = False
    Formulario["DEMANDA_PROC"].Habilitado = False 
    Formulario["SIM_NAO204"].Visivel = True
    Formulario["SIM_NAO204"].Habilitado = False   
 
if OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR":
    Formulario["COMBOBOX1"].Visivel = True
    Formulario["COMBOBOX1"].Habilitado = True
    Formulario["COMBOBOX1"].Itens = "Auxílio Pré-Escola;Auxílio Babá"   
    Formulario["DEMANDA_PROC"].Visivel = False
    Formulario["DEMANDA_PROC"].Habilitado = False
    Formulario["SIM_NAO204"].Visivel = True
    Formulario["SIM_NAO204"].Habilitado = False
    
       
    
#--- Odontológico
if OrdemServico.Servico.Sigla == "AUXODONTOLOGICO":
    Formulario["NUM_NOTA_FISCAL"].Visivel = True
    Formulario["NUM_NOTA_FISCAL"].Habilitado = True
    Formulario["REEMBOLSO_DECLARACAO_MED"].Visivel = False
    Formulario["DATA_PAGAMENTO"].Visivel = False
    Formulario["DATA_PAGAMENTO"].Habilitado = False
    Formulario["DATA_DOCUMENTO"].Visivel = True
    Formulario["DATA_DOCUMENTO"].Habilitado = True
    Formulario["DEMANDA_PROC"].Visivel = True
    Formulario["DEMANDA_PROC"].Habilitado = True
    Formulario["LISTA_TRATAMENTO"].Visivel = True
    
Formulario["OPCAO_DE_CONFIRMACAO"].Visivel = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Pedido médico com a indicação das terapias - Relatório da clínica, constando a quantidade de sessões mensais de terapias e a descrição do tipo de terapia realizada." classes: Relatório Terapia — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Demonstrativo de Desconto de Cooparticipação" classes: Demonstrativo de Desconto de Cooparticipação — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações para preenchimento
  - COMBOBOX1 "Tipo de Benefício" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
  - DEMANDA_PROC "Declaro que não estou solicitando em período inferior 6 meses o benefício para o mesmo tratamento ou elemento. " [CheckBox Boolean → CP_ORDEM_SERVICO.DEMANDA_PROC] obrigatório
  - FAVORECIDO_COBRA "Empregado/Funcionário:" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
**FAVORECIDO_COBRA.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
import peopleSoft
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

#--- Matricula
if Formulario["FAVORECIDO_COBRA"].Valor != "" and Formulario["FAVORECIDO_COBRA"].Valor != None:
 
    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_COBRA"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        orgaoFavorecido = favorecidoCustom.OrgaoId
        Formulario["MATRICULA"].Valor = favorecidoCustom["MATRICULA"].ToString()
        

# --- PMI

matricula = Formulario["MATRICULA"].Valor.ToString()
pmi = consultaPMI(matricula)

if pmi == 'Y':
    Formulario["SIM_NAO204"].Valor = "Sim"
    Formulario["SIM_NAO204"].Habilitado = False
elif pmi == 'N':
    Formulario["SIM_NAO204"].Valor = "Não"
    Formulario["SIM_NAO204"].Habilitado = False
else:
    Formulario["SIM_NAO204"].Valor = "Não"
    Formulario["SIM_NAO204"].Habilitado = False
 
if Controle.Valor != None:
    favorecido = Pessoa.Carrega(Convert.ToInt32(Controle.Valor))
 
idFavorecido = favorecido.Id

# bloquear abertura de chamado para os cargos relacionados abaixo
cargos = ["CONSULTOR", "ESTAGIARIO", "JOVEM APRENDIZ", "MENOR APRENDIZ", "PRESTADOR DE SERVIÇO", "SISTEMA"]
if Controle.Valor != None:
    favorecido = Pessoa.Carrega(Convert.ToInt32(Controle.Valor))
    cargo = favorecido.Cargo.ToString()
    if cargos.Contains(cargo):
       Formulario.ExibeMensagem("Reembolso não permitido para o cargo '" + cargo + "'")
       Formulario["FAVORECIDO_COBRA"].Valor = ""

OrdemServico.SetCustom("FAVORECIDO_COBRA",Controle.Valor)
idFavorecido = OrdemServico["FAVORECIDO_COBRA"]

#--- Medicamento
if (OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR"):
    Formulario["LISTA_MEDICAMENTOS"].Habilitado = True
    Formulario["LISTA_MEDICAMENTOS"].Visivel = True  
    Formulario["LISTA_NF"].Habilitado = False
    Formulario["LISTA_NF"].Visivel = False
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["MATRICULA"].Visivel = True
        Formulario["MATRICULA"].Habilitado = True
        Formulario["LISTA_NF"].Habilitado = True
        Formulario["LISTA_NF"].Visivel = True
        Formulario["LISTA_MEDICAMENTOS"].Habilitado = True
        Formulario["LISTA_MEDICAMENTOS"].Visivel = True
        dt = OrdemServico.GetCustom("LISTA_NF")
        if (dt.Rows.Count == 0):
            Formulario["LISTA_MEDICAMENTOS"].Habilitado = True
            Formulario["LISTA_MEDICAMENTOS"].Visivel = True    
    else:
        Formulario["LISTA_MEDICAMENTOS"].Habilitado = True
        Formulario["LISTA_MEDICAMENTOS"].Visivel = True
    Formulario["LISTA_MEDICAMENTOS"].Valor = None
    Formulario["LISTA_NF"].Valor = None


#--- Ótico
if (OrdemServico.Servico.Sigla == "OTICOCOLABORADOR"):
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["DEP_FAVORECIDO_COBRA"].Itens = DB.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE, DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +"  AND dep.beneficio = 'MATERIAL OTICO - REEMBOLSO' ORDER BY DEP.NOME_DEPENDENTE ")
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = True
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = True
        Formulario["COUNT_10"].Visivel = True
        Formulario["COUNT_10"].Habilitado = True
    else:
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = False
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = False
    #Formulario["DEP_FAVORECIDO_COBRA"].Valor = None


#--- Creche
if (OrdemServico.Servico.Sigla == "CRECHECOLABORADOR"):
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["DEP_FAVORECIDO_COBRA"].Valor = None
        Formulario["DEP_FAVORECIDO_COBRA"].Itens = DB.ExecuteDataTable("SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +"  AND dep.beneficio = 'REEMBOLSO DE CRECHE' ORDER BY DEP.NOME_DEPENDENTE")
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = True
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = True
    else:
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = False
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = False
    Formulario["DEP_FAVORECIDO_COBRA"].Valor = None


#--- Pré-escola
if (OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR"):
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["DEP_FAVORECIDO_COBRA"].Valor = None
        Formulario["DEP_FAVORECIDO_COBRA"].Itens = DB.ExecuteDataTable("SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +"  AND dep.beneficio = 'AUX PRE-ESCOLA' ORDER BY DEP.NOME_DEPENDENTE")
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = True
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = True
    else:
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = False
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = False
    Formulario["DEP_FAVORECIDO_COBRA"].Valor = None

#--- ODONTOLOGICO
if (OrdemServico.Servico.Sigla == "AUXODONTOLOGICO"):
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["DEP_FAVORECIDO_COBRA"].Itens = DB.ExecuteDataTable("SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +"  AND dep.beneficio = 'ASSIST ODONTOLOGICA - REEMBOLSO' ORDER BY DEP.NOME_DEPENDENTE")
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = True
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = True
    else:
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = False
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = False
    Formulario["DEP_FAVORECIDO_COBRA"].Valor = None

#--- Escola
if (OrdemServico.Servico.Sigla == "ESCOLA"):
    if Formulario["FAVORECIDO_COBRA"].Valor != None:
        Formulario["DEP_FAVORECIDO_COBRA"].Valor = None
        Formulario["DEP_FAVORECIDO_COBRA"].Itens = DB.ExecuteDataTable("SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +" AND dep.beneficio = 'AUXILIO ESCOLA' ORDER BY DEP.NOME_DEPENDENTE")
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = True
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = True
    else:
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = False
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = False
    Formulario["DEP_FAVORECIDO_COBRA"].Valor = None
```
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA] obrigatório
  - DEP_FAVORECIDO_COBRA "Nome do Dependente" [DropDownList String → CP_ORDEM_SERVICO.DEP_FAVORECIDO_COBRA]
  - SIM_NAO204 "Empregado PMI" [DropDownList String → CPE_CONTRATOS02.SIM_NAO204] obrigatório
  - LABEL2 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL2]
  - LISTA_NF "Incluir no máximo 3 Notas Fiscais" [DataGrid RecordList → Z_00143_LISTA_NF.LISTA_NF] — QtdColunasFormulario=1; LarguraJanelaPopup=400; PosicaoRotulo=Topo
**LISTA_NF.ScriptModificado**
```python
dt = OrdemServico.GetCustom("LISTA_NF")
if (dt.Rows.Count>=3):
    if OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR":
        FormularioRegistro["CNPJ"].Habilitado=False
        FormularioRegistro["NUMERO_NF"].Habilitado=False
        Formulario["LISTA_MEDICAMENTOS"].Habilitado = True
        Formulario["LISTA_MEDICAMENTOS"].Visivel = True
    if OrdemServico.Servico.Sigla == "RPCDCONSULTAS"  or OrdemServico.Servico.Sigla == "RPCDAVRPARTICULARES" or OrdemServico.Servico.Sigla == "RPCDAVRUNIMED":
        FormularioRegistro["CNPJ"].Habilitado=False
        FormularioRegistro["NUMERO_NF"].Habilitado=False
        Formulario["LISTA_PCD_TERAPIA"].Visivel = True
        Formulario["LISTA_PCD_TERAPIA"].Habilitado = True
    if OrdemServico.Servico.Sigla == "RPCDTERAPIAS":
        FormularioRegistro["CNPJ"].Habilitado=False
        FormularioRegistro["NUMERO_NF"].Habilitado=False
        Formulario["LISTA_PCD_TERAPIA"].Visivel = True
        Formulario["LISTA_PCD_TERAPIA"].Habilitado = True
```
**LISTA_NF.ScriptConfirmado**
```python
import validaCNPJ
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.
if OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR":
    Formulario["LISTA_MEDICAMENTOS"].Habilitado = False
    Formulario["LISTA_MEDICAMENTOS"].Visivel = False  
    Formulario["LISTA_NF"].Habilitado = False
    Formulario["LISTA_NF"].Visivel = False

    numero = "0"
    if (OrdemServico.Numero.ToString()!= ""):
        numero = OrdemServico.Numero.ToString()
    listaNF = OrdemServico.GetCustom("LISTA_NF")
    for linhaNF in listaNF.Rows:
        # Critica CNPJ
        resultado = validaCNPJ(linhaNF["CNPJ"])
        if  resultado != "ok":
            Formulario.ExibeMensagem("CNPJ " + resultado + " Inválido")
        if  String.IsNullOrEmpty(linhaNF["NUMERO_NF"].ToString()):
            Formulario.ExibeMensagem("Número da nota fiscal Inválido")
            resultado = "Erro"
        if  resultado == "ok" :
            # Verifica se já existe O.S. para a nota fiscal
            qry = "SELECT count(LM.NUM_NOTA_FISCAL) CONTADOR FROM OCORRENCIA OC INNER JOIN ORDEM_SERVICO OS ON OC.ID_OCORRENCIA = OS.ID_OCORRENCIA INNER JOIN SERVICO SE ON OS.ID_SERVICO = SE.ID_SERVICO INNER JOIN Z_00143_LISTA_MEDICAMENTOS LM ON LM.ID_OCORRENCIA = OC.ID_OCORRENCIA WHERE SE.SIGLA = '" + OrdemServico.Servico.Sigla + "' AND OC.NUMERO <> '" + numero + "' AND LM.NUM_NOTA_FISCAL = '" + linhaNF["NUMERO_NF"] + "' AND OC.SITUACAO <> 'Cancelada' AND OC.SITUACAO <> 'FinalizadaNaoRealizada' AND LM.CNPJ = '" + linhaNF["CNPJ"]+ "' group by LM.NUM_NOTA_FISCAL "
            lista = Utils.ExecuteDataTable(qry)
            
            ###Criticas.AdicionaPendencia(qry)
            
            numeroRegistro = 0
            for registro in lista.Rows:
                numeroRegistro = registro["CONTADOR"]

            if (numeroRegistro >= 1):
                Formulario.ExibeMensagem("Já existe O.S. para o documento Fiscal número " + linhaNF["NUMERO_NF"] + " do CNPJ " + linhaNF["CNPJ"] + "." )

    resultado = validaCNPJ(FormularioRegistro["CNPJ"].Valor)
    if  resultado != "ok":
        Formulario.ExibeMensagem("CNPJ " + resultado + " Inválido")
        Cancela=True
    if  String.IsNullOrEmpty(FormularioRegistro["NUMERO_NF"].Valor):
        Formulario.ExibeMensagem("Número da nota fiscal Inválido")
        resultado = "Erro"
        Cancela=True
    if  resultado == "ok" :
        # Verifica se já existe O.S. para a nota fiscal
        qry = "SELECT count(LM.NUM_NOTA_FISCAL) CONTADOR FROM OCORRENCIA OC INNER JOIN ORDEM_SERVICO OS ON OC.ID_OCORRENCIA = OS.ID_OCORRENCIA INNER JOIN SERVICO SE ON OS.ID_SERVICO = SE.ID_SERVICO INNER JOIN Z_00143_LISTA_MEDICAMENTOS LM ON LM.ID_OCORRENCIA = OC.ID_OCORRENCIA WHERE SE.SIGLA = '" + OrdemServico.Servico.Sigla + "' AND OC.NUMERO <> '" + numero + "' AND LM.NUM_NOTA_FISCAL = '" + FormularioRegistro["NUMERO_NF"].Valor.ToString() + "' AND OC.SITUACAO <> 'Cancelada' AND OC.SITUACAO <> 'FinalizadaNaoRealizada' AND LM.CNPJ = '" +FormularioRegistro["CNPJ"].Valor.ToString() + "' group by LM.NUM_NOTA_FISCAL "
        lista = Utils.ExecuteDataTable(qry)
        
        ###Criticas.AdicionaPendencia(qry)
        
        numeroRegistro = 0
        for registro in lista.Rows:
            numeroRegistro = registro["CONTADOR"]

        if (numeroRegistro >= 1):
            Formulario.ExibeMensagem("Já existe O.S. para o documento Fiscal número " + FormularioRegistro["NUMERO_NF"].Valor.ToString() + " do CNPJ " + FormularioRegistro["CNPJ"].Valor.ToString() + "." )
            Cancela=True



    #--- Medicamento
    if (OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR"):
        if (Formulario["FAVORECIDO_COBRA"].Valor != None):
            Formulario["LISTA_NF"].Habilitado = True
            Formulario["LISTA_NF"].Visivel = True

            #dt = Formulario("LISTA_NF")
            if (String.IsNullOrEmpty(FormularioRegistro["CNPJ"].Valor)):
                Formulario["LISTA_MEDICAMENTOS"].Habilitado = False
                Formulario["LISTA_MEDICAMENTOS"].Visivel = False
            else:
                Formulario["LISTA_MEDICAMENTOS"].Habilitado = True
                Formulario["LISTA_MEDICAMENTOS"].Visivel = True    
        else:
            Formulario["LISTA_MEDICAMENTOS"].Habilitado = False
            Formulario["LISTA_MEDICAMENTOS"].Visivel = False
        Formulario["LISTA_MEDICAMENTOS"].Valor = None
        Formulario["LISTA_NF"].Valor = None
        
        dt = OrdemServico.GetCustom("LISTA_NF")
        if (dt.Rows.Count>=3):
            Cancela=True
```
    - coluna NUMERO_NF obrigatório
    - coluna CNPJ obrigatório
  - LISTA_MEDICAMENTOS "Lista de Medicamentos" [DataGrid RecordList → Z_00143_LISTA_MEDICAMENTOS.LISTA_MEDICAMENTOS] obrigatório — QtdColunasFormulario=3; PosicaoRotulo=Topo
**LISTA_MEDICAMENTOS.ScriptModificado**
```python
FormularioRegistro["CNPJ"].Visivel = True
FormularioRegistro["CNPJ"].Habilitado = True
dt = OrdemServico.GetCustom("LISTA_NF")
itensCNPJ=''
itensNF=''
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ,CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = 636750")
#itensNF=DB.ExecuteDataTable("SELECT NUMERO_NF FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
contCNPJ=0
contNF=0
regdr=0
#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCNPJ=0
    igualNF=0
    regdr2=0
    
    for dr2 in dt.Rows:
        if (dr["CNPJ"]== dr2["CNPJ"]):
            if (regdr<=regdr2 and igualCNPJ==0):
                igualCNPJ=0
            else:
                igualCNPJ=1
        if (dr["NUMERO_NF"]== dr2["NUMERO_NF"]):
            if (regdr<=regdr2 and igualNF==0):
                igualNF=0
            else:
                igualNF=1
        regdr2=regdr2+1
    if (igualCNPJ<=0):
        if (contCNPJ==0):
            itensCNPJ=dr["CNPJ"]
            #itensCNPJ=dt.Rows.Count.ToString()
            contCNPJ=1
        else:
            itensCNPJ = itensCNPJ+';'+dr["CNPJ"]
    if (igualNF<=0):
        if (contNF==0):
            itensNF=dr["NUMERO_NF"]
            contNF=1
        else:
            itensNF = itensNF+';'+dr["NUMERO_NF"]
    regdr=regdr+1
FormularioRegistro["CNPJ"].Itens = itensCNPJ
FormularioRegistro["NUM_NOTA_FISCAL"].Itens = itensNF
```
    - coluna QUANTIDADE
    - coluna CNPJ obrigatório
**LISTA_MEDICAMENTOS.CNPJ.ScriptModificado**
```python
dt = OrdemServico.GetCustom("LISTA_NF")
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ,CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = 636750")
#itensNF=DB.ExecuteDataTable("SELECT NUMERO_NF FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
itensNF=''

cont=0
##if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    #if (cont==0):
    #    itensCNPJ=dr["CNPJ"]
    #else:
    #    itensCNPJ = itensCNPJ+';'+dr["CNPJ"]
    if (FormularioRegistro["CNPJ"].Valor == dr["CNPJ"]):
        if (cont==0):
            itensNF=dr["NUMERO_NF"]
        else:
            itensNF = itensNF+';'+dr["NUMERO_NF"]
        cont=1
#FormularioRegistro["CNPJ"].Itens = itensCNPJ
FormularioRegistro["NUM_NOTA_FISCAL"].Itens = itensNF
```
    - coluna DEPENDENTE
    - coluna VALOR_MEDICAMENTO obrigatório
    - coluna NUM_NOTA_FISCAL obrigatório
**LISTA_MEDICAMENTOS.NUM_NOTA_FISCAL.ScriptModificado**
```python
dt = OrdemServico.GetCustom("LISTA_NF")
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ,CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = 636750")
#itensNF = DB.ExecuteDataTable("SELECT NUMERO_NF FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
#itensCNPJ=None
itensCNPJ = ''
cont=0
##if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    if (FormularioRegistro["NUM_NOTA_FISCAL"].Valor == dr["NUMERO_NF"]):
        if (cont==0):
            itensCNPJ=dr["CNPJ"]
        else:
            itensCNPJ = itensCNPJ+';'+dr["CNPJ"]
    #if (cont==0):
    #    itensNF=dr["NUMERO_NF"]
    #else:
    #    itensNF = itensNF+';'+dr["NUMERO_NF"]
        cont=1
FormularioRegistro["CNPJ"].Itens = itensCNPJ
#FormularioRegistro["NUM_NOTA_FISCAL"].Itens = itensNF
```
    - coluna TIPO obrigatório
**LISTA_MEDICAMENTOS.TIPO.ScriptModificado**
```python
if FormularioRegistro['TIPO'].Valor == 'Increnoativos: Ozempic, Mounjaro, entre outros, vide NI103':
    FormularioRegistro['QUANTIDADE'].Visivel = True
else:
    FormularioRegistro['QUANTIDADE'].Visivel = False
```
    - coluna DATA_RECEITA obrigatório
    - coluna NOME_MEDICAMENTO obrigatório
  - LISTAPCD_TERAPIAS "Auxilio PCD" [DataGrid RecordList → Z_00143_LISTAPCD_TERAPIAS.LISTAPCD_TERAPIAS] obrigatório
    - coluna VALOR obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna DATA obrigatório
    - coluna CNPJ obrigatório
    - coluna DEPENDENTE
    - coluna TERAPIA obrigatório
    - coluna NUM_NOTA_FISCAL obrigatório
  - LISTAPCD_COO "Auxilio PCD Cooparticipação " [DataGrid RecordList → Z_00143_LISTAPCD_COO.LISTAPCD_COO] obrigatório
    - coluna DATA_RELATORIO obrigatório
    - coluna CNPJ obrigatório
    - coluna DEPENDENTES
    - coluna QUANTIDADE obrigatório
    - coluna TERAPIA obrigatório
    - coluna VALOR_COO obrigatório
  - LISTA_REEMBOLSO_OTICO "Dados do Reembolso Ótico" [DataGrid RecordList → Z_00143_LISTA_REEMBOLSO_OTICO.LISTA_REEMBOLSO_OTICO] obrigatório — QtdColunasFormulario=1; LarguraJanelaPopup=120
    - coluna NOME_DEPENDENTE
    - coluna DATA_RECEITA obrigatório
    - coluna NOTA_FISCAL obrigatório
    - coluna TIPO_REEMBOLSO obrigatório
  - COUNT_10 "Quantidade de Pares de Lente" [DropDownList Integer → CPE_PESSOAS.COUNT_10] obrigatório
  - VALOR_NOTA_FISCAL "Valor da Nota Fiscal" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_NOTA_FISCAL] obrigatório
  - DATA_PAGAMENTO "Data mês referência" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_PAGAMENTO]
  - DATA_DOCUMENTO "Data do registro de atendimento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_DOCUMENTO] obrigatório
  - NUM_NOTA_FISCAL "Número do COO (Nota Fiscal)" [TextBox Integer → CP_ORDEM_SERVICO.NUM_NOTA_FISCAL] obrigatório
  - VALOR_MENSALIDADE "Valor da mensalidade" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_MENSALIDADE] obrigatório
  - REEMBOLSO_DECLARACAO "Declaro que não estou solicitando o auxílio babá, auxílio creche, auxílio  pré escola ou auxílio filho com deficiência para o mesmo dependente na mesma competência." [CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO] obrigatório
  - OPCAO_DE_CONFIRMACAO "Dependente não cadastrado" [CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO]
**OPCAO_DE_CONFIRMACAO.ScriptModificado**
```python
Formulario["NOME"].Visivel = False
Formulario["NOME"].Habilitado = False
Formulario["NOME"].Valor = ""

if (Formulario["OPCAO_DE_CONFIRMACAO"].Valor == True) :
    Formulario["NOME"].Visivel = True
    Formulario["NOME"].Habilitado = True
    Formulario.ExibeMensagem("Favor anexar o arquivo 'Comprovação de dependência'")
```
  - NOME "Nome Completo do Dependente" [TextBox String → CP_ORDEM_SERVICO.NOME]
  - REEMBOLSO_DECLARACAO_MED "

Declaro que o reembolso solicitado não se refere a medicamentos com finalidade de tratamentos estéticos e/ou cosméticos." [CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO_MED]
  - REEMBOLSO_DECLARACAO_ESCOLA "Declaro não receber este benefício em outra instituição" [CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO_ESCOLA]
  - LISTA_TRATAMENTO "LISTA_TRATAMENTO" [DataGrid RecordList → Z_00143_LISTA_TRATAMENTO.LISTA_TRATAMENTO] obrigatório — FormaEdicaoWeb=JanelaPopup; LarguraJanelaPopup=400
    - coluna VALOR_PAGO obrigatório
    - coluna VALOR_FINAL
    - coluna VALOR_TRATAMENTO
    - coluna VALORPAGO obrigatório
    - coluna TRATAMENTO obrigatório
**LISTA_TRATAMENTO.TRATAMENTO.ScriptModificado**
```python
consulta = Utils.ExecuteDataTable("select NVL(SS.VALOR,0) as VALOR from TB_CAD_SUBSERVICO SS WHERE SS.ID_CAD_SUBSERVICO='"+FormularioRegistro["TRATAMENTO"].Valor+"'")
for valor in consulta.Rows: 
    FormularioRegistro["VALOR_TRATAMENTO"].Valor = valor["VALOR"]
```
    - coluna QUANTIDADE obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=COMPROVACAO_DE_DEPENDENCIA
  - anexo "Comprovação de dependência, somente em casos de dependente não cadastrado." classes: Comprovação de dependência — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=ARQUIVOS OBRIGATORIOS
  - anexo "Boleto Bancário" classes: Boleto Bancário — ProduzidoTermino=true
  - anexo "" classes: Comprovante de vínculo empregatício - Babá — RequeridoInicial=true
  - anexo "Receituário" classes: Receituário — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "NF" classes: Nota Fiscal — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "Anexar Orçamento" classes: Orçamento — RequeridoInicial=true
  - anexo "Comprovante de pagamento" classes: Comprovante de Pagamento Depósito — ProduzidoTermino=true
- Operação PR0004 Associar Itens Configuração: Nome=RECEITUARIO OPCIONAL
  - anexo "Receituário" classes: Receituário — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração: Nome=LAUDO_MEDICO
  - anexo "Laudo Médico (Necessário para produtos não classificados como medicamento pela Anvisa, porém aceitos pelas diretrizes NI102)." classes: Laudo Médico — RequeridoInicial=true; PermiteMultiplosItens=true

### [360766] EventoIntermediarioMensagem "Notificar cliente reprovado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Aviso sobre Reprovação - Reembolso
Corpo do comunicado: Prezado(a), 
O chamado OrdemServico.Numero foi cancelada pois o gestor não aprovou a documentação.
Para mais detalhes sobre esta solicitação Link.Consulta 
Motivo: Complemento1
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoReprovacao("APROV_GESTOR")
```

### [360767] Tarefa "Corrigir informações e/ou anexos"
Referência: ...
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
**ScriptValidacao**
```python
import validaCNPJ
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.
mes=12

#Atendendo a OS 311519 para liberar por um período determinado a abertura de chamado até o mês de janeiro do ano anterior 
if (Convert.ToDateTime("16/02/2017") >= DateTime.Now):
        mes=1
        
numero = "0"
if (OrdemServico.Numero.ToString()!= ""):
    numero = OrdemServico.Numero.ToString()
favorecidoCobra = OrdemServico.GetCustom("FAVORECIDO_COBRA").ToString()

#---------- VERIFICA A EDICAO DOS CAMPOS DE DEPENDENTES

if (OrdemServico.GetCustom("OPCAO_DE_CONFIRMACAO") == True) and ((OrdemServico.GetCustom("NOME") == "") and (OrdemServico.GetCustom("DEP_FAVORECIDO_COBRA") == "")) :
    Criticas.AdicionaPendencia("O campo Nome do Dependente é obrigatório.") 

if (OrdemServico.GetCustom("DEP_FAVORECIDO_COBRA") != ""):
    dependenteCobra = OrdemServico.GetCustom("DEP_FAVORECIDO_COBRA").ToString()
else:
    if ((OrdemServico.GetCustom("NOME") != "") and (OrdemServico.GetCustom("OPCAO_DE_CONFIRMACAO") == True)):
        dependenteCobra = OrdemServico.GetCustom("NOME").ToString()
    else: 
        dependenteCobra = "is NULL"
if ((OrdemServico.PossuiItem("CD") == False) and (OrdemServico.GetCustom("OPCAO_DE_CONFIRMACAO") == True)):
        Criticas.AdicionaPendencia("Não foi associado um(a) 'Comprovação de dependência'")


#---------- MEDICAMENTO

#--- Verifica se foi marcado o campo de declaração do medicamento para fins não estéticos
if ((OrdemServico.GetCustom("REEMBOLSO_DECLARACAO_MED")  == False) and (OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR")) :
    Criticas.AdicionaPendencia("A declaração da finalidade do medicamento é um campo obrigatório")

#--- Verifica se existe alguma medicamento comum
if (OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR"):
    listaMedicamentos = OrdemServico.GetCustom("LISTA_MEDICAMENTOS")
    listaNF = OrdemServico.GetCustom("LISTA_NF")
    #if (listaNF == None or listaMedicamentos == None):
    if (listaNF.Rows.Count == 0 or listaMedicamentos.Rows.Count == 0):    
        Criticas.AdicionaPendencia("Lista de NF(COO) e Lista de Medicamentos são obrigatórios!")
    else:
        cont = 0
        for linha in listaMedicamentos.Rows:
            cont += 1
            existeNF = 0
            existeCNPJ = 0
            for linhaNF in listaNF.Rows:
                if (linha["CNPJ"]==linhaNF["CNPJ"] and linha["NUM_NOTA_FISCAL"]==linhaNF["NUMERO_NF"]):
                    existeCNPJ = 1
                    existeNF = 1
                #if (linha["NUM_NOTA_FISCAL"]==linhaNF["NUMERO_NF"]):
            if (existeCNPJ == 0 or existeNF == 0):
                Criticas.AdicionaPendencia("NF ou CNPJ do medicamento "+linha["NOME_MEDICAMENTO"]+" não consta no campo Lista de NF(COO)")
                
            if (linha["TIPO"] == "Comum") and (Convert.ToDateTime(linha["DATA_RECEITA"]).AddDays(120).Date < DateTime.Now.Date) and (OrdemServico.Atividade.Codigo == "EVENTO_INICIAL"):
                #Criticas.AdicionaPendencia("Data da Receita não pode ser anterior a 100 dias.")
                Criticas.AdicionaPendencia("Data da Receita referente ao medicamento '"+linha["NOME_MEDICAMENTO"]+"' não pode ser anterior a " + Convert.ToString(DateTime.Now.AddDays(-120).Date))

            if (linha["TIPO"] == "Contínuo") and (Convert.ToDateTime(linha["DATA_RECEITA"]).AddDays(360).Date < DateTime.Now.Date) and (OrdemServico.Atividade.Codigo == "EVENTO_INICIAL"):
                #Criticas.AdicionaPendencia("Data da Receita não pode ser anterior a 220 dias.")
                Criticas.AdicionaPendencia("Data da Receita referente ao medicamento '"+linha["NOME_MEDICAMENTO"]+"' não pode ser anterior a " + Convert.ToString(DateTime.Now.AddDays(-360).Date))
                
            # Critica CNPJ
            resultado = validaCNPJ(linha["CNPJ"])
            if  resultado != "ok":
                Criticas.AdicionaPendencia("Linha: " + cont.ToString() + ". CNPJ " + resultado + " Inválido")
            if  String.IsNullOrEmpty(linha["NUM_NOTA_FISCAL"].ToString()):
                Criticas.AdicionaPendencia("Linha: " + cont.ToString() + ". Número da nota fiscal Inválido")
                resultado = "Erro"
            if  resultado == "ok" :
                # Verifica se já existe O.S. para a nota fiscal
                qry = "SELECT count(LM.NUM_NOTA_FISCAL) CONTADOR FROM OCORRENCIA OC INNER JOIN ORDEM_SERVICO OS ON OC.ID_OCORRENCIA = OS.ID_OCORRENCIA INNER JOIN SERVICO SE ON OS.ID_SERVICO = SE.ID_SERVICO INNER JOIN Z_00143_LISTA_MEDICAMENTOS LM ON LM.ID_OCORRENCIA = OC.ID_OCORRENCIA WHERE SE.SIGLA = '" + OrdemServico.Servico.Sigla + "' AND OC.NUMERO <> '" + numero + "' AND LM.NUM_NOTA_FISCAL = '" + linha["NUM_NOTA_FISCAL"] + "' AND OC.SITUACAO <> 'Cancelada' AND OC.SITUACAO <> 'FinalizadaNaoRealizada' AND LM.CNPJ = '" + linha["CNPJ"]+ "' group by LM.NUM_NOTA_FISCAL "
                lista = Utils.ExecuteDataTable(qry)
                
                ###Criticas.AdicionaPendencia(qry)
                
                numeroRegistro = 0
                for registro in lista.Rows:
                    numeroRegistro = registro["CONTADOR"]

                if (numeroRegistro >= 1):
                    Criticas.AdicionaPendencia("Linha: " + cont.ToString() + ". Já existe O.S. para o documento Fiscal número " + linha["NUM_NOTA_FISCAL"] + " do CNPJ " + linha["CNPJ"] + "." )

#---------- ÓTICO
if (OrdemServico.Servico.Sigla == "OTICOCOLABORADOR"):
    
#--- Verifica se já existe outro chamado aberto
    #--- Verifica se existe outro chamado aberto para o Cliente
    depend= " AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"')"
    if (dependenteCobra == "is NULL"):
        depend= " AND (CPOS.DEP_FAVORECIDO_COBRA "+ dependenteCobra +" AND CPOS.NOME "+ dependenteCobra +")"
    lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O INNER JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) INNER JOIN PESSOA F ON (CPOS.FAVORECIDO_COBRA = F.ID_PESSOA) WHERE S.ID_SERVICO = '"+ OrdemServico.ServicoId.ToString() +"' AND O.SITUACAO = 'Aberto' AND O.NUMERO <> '"+ numero +"' AND CPOS.FAVORECIDO_COBRA = '"+ favorecidoCobra +"' "+ depend) 
    
    for linha in lista.Rows:
        numeroRegistro = linha["CONTADOR"]

    if (numeroRegistro >= 1):
        Criticas.AdicionaPendencia("Já existe um chamado aberto! Aguarde análise da equipe da GGP para abrir outro") 
    else:

        #--- Verifica tempo para solicitação de material ótico
        consulta = Utils.ExecuteDataTable(" select * from (SELECT distinct ROUND((SYSDATE - OC.DATA_HORA_CRIACAO),0) as DIAS, Z.TIPO_REEMBOLSO, OC.DATA_HORA_CRIACAO FROM OCORRENCIA OC INNER JOIN ORDEM_SERVICO OS ON (OC.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO SE ON (OS.ID_SERVICO = SE.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (CPOS.ID_OCORRENCIA = OC.ID_OCORRENCIA) INNER JOIN PESSOA PE ON (CPOS.FAVORECIDO_COBRA = PE.ID_PESSOA) INNER JOIN CAD_FUNCIONARIO_V CA ON (CA.NOME = PE.NOME) LEFT JOIN DEPENDENTES_BENEFICIOS_V DEP ON (DEP.MATRICULA = CA.MATRICULA and CPOS.DEP_FAVORECIDO_COBRA = DEP.NOME_DEPENDENTE) INNER JOIN Z_00143_LISTA_REEMBOLSO_OTICO Z ON (Z.ID_OCORRENCIA = OC.ID_OCORRENCIA) WHERE SE.ID_SERVICO = '"+ OrdemServico.ServicoId.ToString() +"' AND CPOS.FAVORECIDO_COBRA = '"+ favorecidoCobra +"' AND OC.SITUACAO = 'FinalizadaSucesso' " + depend +" ORDER BY OC.DATA_HORA_CRIACAO DESC) where dias < 365")
        
        dia = 0 
        tipoJaPedido = ""
        listaOtico = OrdemServico.GetCustom("LISTA_REEMBOLSO_OTICO")
        # verifica itens permitidos na lista
        
        for linhaOtico in listaOtico.Rows:
            if (linhaOtico["DATA_RECEITA"] == "" or linhaOtico["DATA_RECEITA"] == None) :
                Criticas.AdicionaPendencia("Campo 'Data da Receita' é Obrigatório")
            else:
                dt = linhaOtico["DATA_RECEITA"].AddDays(365)
                if (dt < OrdemServico.DataHoraCriacao) :
                    Criticas.AdicionaPendencia("A data da receita é inferior a 365 dias da abertura da OS")

            for linha in consulta.Rows:
                erro = ""
                dia = linha["DIAS"].ToString() 
                tipoJaPedido = linha["TIPO_REEMBOLSO"].ToString() 
                if (tipoJaPedido == "Lente de Contato" or tipoJaPedido == "Armação/Lente"):
                    erro = "Já foi concedido Reembolso Ótico no último ano, não sendo permitido novo pedido neste período, para este titular ou dependente."
                elif (linhaOtico["TIPO_REEMBOLSO"] == tipoJaPedido):
                    erro = "O Reembolso Ótico para '" + tipoJaPedido + "' é concedido apenas uma vez por ano, um para o titular e um para cada dependente."
                elif (tipoJaPedido == "Armação" and linhaOtico["TIPO_REEMBOLSO"] != "Lente"):
                    erro = "Reembolso Ótico somente permitido para 'Lente', pois já foi concedido reembolso para 'Armação' no último ano, para este titular ou dependente."
                elif (tipoJaPedido == "Lente" and linhaOtico["TIPO_REEMBOLSO"] != "Armação"):
                    erro = "Reembolso Ótico somente permitido para 'Armação', pois já foi concedido reembolso para 'Lente' no último ano, para este titular ou dependente."
                if erro != "":
                    Criticas.AdicionaPendencia(erro)
                    break

#---------- ESCOLA

#--- Verifica se já possui chamado aberto

if (OrdemServico.Servico.Sigla == "ESCOLA"):
    if OrdemServico.GetCustom("DATA_PAGAMENTO") == "" or OrdemServico.GetCustom("DATA_PAGAMENTO") == None :
        Criticas.AdicionaPendencia("Campo 'Data mês referência' é Obrigatório")
    else:    
        if OrdemServico.GetCustom("DATA_PAGAMENTO")!= "":
            lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O INNER JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) INNER JOIN PESSOA F ON (CPOS.FAVORECIDO_COBRA = F.ID_PESSOA) WHERE S.ID_SERVICO = '" + OrdemServico.ServicoId.ToString() + "' AND O.SITUACAO = 'Aberto' AND O.NUMERO <> '"+ numero +"' AND F.ID_PESSOA = '"+ favorecidoCobra +"' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') ") 

            for linha in lista.Rows:
                numeroRegistro = linha["CONTADOR"]

            if (numeroRegistro >= 1):
                Criticas.AdicionaPendencia("Já existe um chamado aberto! Aguarde análise da equipe da GGP para abrir outro") 
            else:
                lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) WHERE S.SIGLA = 'ESCOLA' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+ OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') AND O.SITUACAO = 'FinalizadaSucesso' ")

                for linha in lista.Rows:
                    numeroRegistro = linha["CONTADOR"]

                if (numeroRegistro > 0):
                    Criticas.AdicionaPendencia("Apenas um Auxílio Escola deve ser solicitado por mês")
        else:
            Criticas.AdicionaPendencia("O campo Data mês referência é obrigatório") 
        if OrdemServico.GetCustom("REEMBOLSO_DECLARACAO_ESCOLA") == False:
            Criticas.AdicionaPendencia("A declaração de que não recebo reembolso escolar de outra intituição é um campo obrigatório")
    if (OrdemServico.GetCustom("DATA_PAGAMENTO").AddYears(1).Year < OrdemServico.DataHoraCriacao.Year) or ((OrdemServico.GetCustom("DATA_PAGAMENTO").AddYears(1).Year == OrdemServico.DataHoraCriacao.Year)and (OrdemServico.GetCustom("DATA_PAGAMENTO").Month < mes)):
        Criticas.AdicionaPendencia("A 'Data mês referência' não pode ser anterior a "+mes.ToString()+"/"+ OrdemServico.DataHoraCriacao.AddYears(-1).Year.ToString())
        

#---------- CRECHE

#--- Verifica se já possui chamado aberto

if (OrdemServico.Servico.Sigla == "CRECHECOLABORADOR"):
    if OrdemServico.GetCustom("DATA_PAGAMENTO") == "" or OrdemServico.GetCustom("DATA_PAGAMENTO") == None :
        Criticas.AdicionaPendencia("Campo 'Data mês referência' é Obrigatório")
    else:    
        lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O INNER JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) INNER JOIN PESSOA F ON (CPOS.FAVORECIDO_COBRA = F.ID_PESSOA) WHERE S.ID_SERVICO = '" + OrdemServico.ServicoId.ToString() + "' AND O.SITUACAO = 'Aberto' AND O.NUMERO <> '"+ numero +"' AND F.ID_PESSOA = '"+ favorecidoCobra +"' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+ OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') ") 
        
        for linha in lista.Rows:
            numeroRegistro = linha["CONTADOR"]

        if (numeroRegistro >= 1):
            Criticas.AdicionaPendencia("Já existe um chamado aberto! Aguarde análise da equipe da GGP para abrir outro") 
        else:
            lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) WHERE S.SIGLA = 'CRECHECOLABORADOR' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+ OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') AND O.SITUACAO = 'FinalizadaSucesso' ") 

            for linha in lista.Rows:
                numeroRegistro = linha["CONTADOR"]

            if (numeroRegistro > 0):
                Criticas.AdicionaPendencia("Apenas um Auxílio Creche deve ser solicitado por mês")
    if (OrdemServico.GetCustom("DATA_PAGAMENTO").AddYears(1).Year < OrdemServico.DataHoraCriacao.Year) or ((OrdemServico.GetCustom("DATA_PAGAMENTO").AddYears(1).Year == OrdemServico.DataHoraCriacao.Year)and (OrdemServico.GetCustom("DATA_PAGAMENTO").Month < mes)):
        Criticas.AdicionaPendencia("A 'Data mês referência' não pode ser anterior a "+mes.ToString()+"/"+ OrdemServico.DataHoraCriacao.AddYears(-1).Year.ToString())
        

#---------- PRE-ESCOLA

#--- Verifica se já possui chamado aberto

#if (OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR"):  
#    if OrdemServico.GetCustom("DATA_PAGAMENTO") == "" or OrdemServico.GetCustom("DATA_PAGAMENTO") == None :
#        Criticas.AdicionaPendencia("Campo 'Data mês referência' é Obrigatório")
#    else:    
#        lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O INNER JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) INNER JOIN PESSOA F ON (CPOS.FAVORECIDO_COBRA = F.ID_PESSOA) WHERE S.ID_SERVICO = '" + OrdemServico.ServicoId.ToString() + "' AND O.SITUACAO = 'Aberto' AND O.NUMERO <> '"+ numero +"' AND F.ID_PESSOA = '"+ favorecidoCobra +"' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') ") 
#
#        for linha in lista.Rows:
#            numeroRegistro = linha["CONTADOR"]
#
#        if (numeroRegistro >= 1):
#            Criticas.AdicionaPendencia("Já existe um chamado aberto! Aguarde análise da equipe da GGP para abrir outro") 
#        else:
#            lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) WHERE S.SIGLA = 'PREESCOLACOLABORADOR' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+ OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') AND O.SITUACAO = 'FinalizadaSucesso' ")
#
#            for linha in lista.Rows:
#                numeroRegistro = linha["CONTADOR"]
#
#            if (numeroRegistro > 0):
#                Criticas.AdicionaPendencia("Apenas um Auxílio Pré-Escola deve ser solicitado por mês")
#    if (OrdemServico.GetCustom("DATA_PAGAMENTO").AddYears(1).Year < OrdemServico.DataHoraCriacao.Year) or ((OrdemServico.GetCustom("DATA_PAGAMENTO").AddYears(1).Year == OrdemServico.DataHoraCriacao.Year)and (OrdemServico.GetCustom("DATA_PAGAMENTO").Month < mes)):
#        Criticas.AdicionaPendencia("A 'Data mês referência' não pode ser anterior a "+mes.ToString()+"/"+ OrdemServico.DataHoraCriacao.AddYears(-1).Year.ToString())
#        
#        
if (OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR"):  
    if OrdemServico.GetCustom("DATA_PAGAMENTO") == "" or OrdemServico.GetCustom("DATA_PAGAMENTO") == None :
        Criticas.AdicionaPendencia("Campo 'Data mês referência' é Obrigatório")
    else:    
        lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O INNER JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) INNER JOIN PESSOA F ON (CPOS.FAVORECIDO_COBRA = to_char(F.ID_PESSOA)) WHERE S.ID_SERVICO = '" + OrdemServico.ServicoId.ToString() + "' AND O.SITUACAO = 'Aberto' AND O.NUMERO <> '"+ numero +"' AND to_char(F.ID_PESSOA) = '"+ favorecidoCobra +"' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') ") 
        numeroRegistro = 0
        for linha in lista.Rows:
            numeroRegistro = linha["CONTADOR"]

        if (numeroRegistro >= 1):
            Criticas.AdicionaPendencia("Já existe um chamado aberto! Aguarde a verificação do Cesec para abrir outro") 
            
        else:
            if OrdemServico["OPCAO_DE_CONFIRMACAO"] == True:
                lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) JOIN PESSOA F ON (CPOS.FAVORECIDO_COBRA = to_char(F.ID_PESSOA)) WHERE S.SIGLA = 'PREESCOLACOLABORADOR' AND to_char(F.ID_PESSOA) = '"+ favorecidoCobra +"' AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+ OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') AND O.SITUACAO = 'FinalizadaSucesso' ")
                numeroRegistro = 0
                for linha in lista.Rows:
                    numeroRegistro = linha["CONTADOR"]
                
            else:
                lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) WHERE S.SIGLA = 'PREESCOLACOLABORADOR' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+ OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') AND O.SITUACAO = 'FinalizadaSucesso' ")
                numeroRegistro = 0
                for linha in lista.Rows:
                    numeroRegistro = linha["CONTADOR"]
            
        #else:
        #    lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) WHERE S.SIGLA = 'PREESCOLACOLABORADOR' AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"') AND TO_CHAR(CPOS.DATA_PAGAMENTO, 'MM/YYYY') = TO_CHAR(TO_DATE('"+ OrdemServico.GetCustom("DATA_PAGAMENTO").ToString() +"','DD/MM/YYYY HH24:MI:SS'),'MM/YYYY') AND O.SITUACAO = 'FinalizadaSucesso' ")
        #    numeroRegistro = 0
        #    for linha in lista.Rows:
        #        numeroRegistro = linha["CONTADOR"]
            
#            if (numeroRegistro > 0):
#                #Criticas.AdicionaPendencia(dependenteCobra.ToString())
#                Criticas.AdicionaPendencia("Apenas um Auxílio Pré-Escola deve ser solicitado por mês")        
#
        
        
        
        
#---------- CRECHE E PRE-ESCOLA

#--- Verifica se foi marcado o campo de declaração de reembolso de outra instituição
if ((OrdemServico.GetCustom("REEMBOLSO_DECLARACAO") == False) and ((OrdemServico.Servico.Sigla == "CRECHECOLABORADOR") or (OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR"))) :
    Criticas.AdicionaPendencia("A declaração de não recebimento de reembolso por outra instituição é campo obrigatório")

#--- Campo Dependente obrigatório para Auxílio Creche e Pré-Escola

if ((OrdemServico.Servico.Sigla == "CRECHECOLABORADOR") or (OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR") or (OrdemServico.Servico.Sigla == "ESCOLA")) and OrdemServico.GetCustom("DEP_FAVORECIDO_COBRA") == "" and (OrdemServico.GetCustom("NOME") == ""):
    Criticas.AdicionaPendencia("Campo Dependente é Obrigatório")


#---------- ODONTOLÓGICO


if (OrdemServico.Servico.Sigla == "AUXODONTOLOGICO"):
    if OrdemServico.GetCustom("DATA_DOCUMENTO") == "" or OrdemServico.GetCustom("DATA_DOCUMENTO") == None :
        Criticas.AdicionaPendencia("Campo 'Data do Orçamento' é Obrigatório")
    else:
        dias = OrdemServico.GetCustom("DATA_DOCUMENTO").AddDays(60)
        if dias < OrdemServico.DataHoraCriacao :
            Criticas.AdicionaPendencia("A data do orçamento é superior a 60 dias da abertura da OS")
            
    #--- Verifica se existe outro chamado aberto para o Cliente

    depend= " AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"')"
    if (dependenteCobra == "is NULL"):
        depend= " AND (CPOS.DEP_FAVORECIDO_COBRA "+ dependenteCobra +" AND CPOS.NOME "+ dependenteCobra +")"
    
    lista = Utils.ExecuteDataTable("SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O INNER JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) INNER JOIN PESSOA F ON (CPOS.FAVORECIDO_COBRA = F.ID_PESSOA) WHERE S.ID_SERVICO = '"+ OrdemServico.ServicoId.ToString() +"' AND O.SITUACAO = 'Aberto' AND O.NUMERO <> '"+ numero +"' AND F.ID_PESSOA = '"+ favorecidoCobra +"'"+ depend)

    for linha in lista.Rows:
        numeroRegistro = linha["CONTADOR"]

    if (numeroRegistro >= 1):
        Criticas.AdicionaPendencia("Já existe um chamado aberto! Aguarde análise da equipe da GGP para abrir outro") 
    else:
        #--- Verifica tempo para solicitação de auxilio odontológico

        depend= " AND (CP.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CP.NOME = '"+ dependenteCobra +"')"
        if (dependenteCobra == "is NULL"):
            depend= " AND (CP.DEP_FAVORECIDO_COBRA "+ dependenteCobra +" AND CP.NOME "+ dependenteCobra +")"
    
        #consulta = Utils.ExecuteDataTable(" SELECT distinct ROUND((SYSDATE - OC.DATA_HORA_CRIACAO),0) as DIAS, OC.DATA_HORA_CRIACAO FROM OCORRENCIA OC INNER JOIN ORDEM_SERVICO OS ON (OC.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO SE ON (OS.ID_SERVICO = SE.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CP ON (CP.ID_OCORRENCIA = OC.ID_OCORRENCIA) INNER JOIN PESSOA PE ON (CP.FAVORECIDO_COBRA = PE.ID_PESSOA) INNER JOIN CAD_FUNCIONARIO_V CA ON (CA.NOME = PE.NOME) LEFT JOIN DEPENDENTES_BENEFICIOS_V DEP ON (DEP.MATRICULA = CA.MATRICULA and CP.DEP_FAVORECIDO_COBRA = DEP.NOME_DEPENDENTE) WHERE SE.ID_SERVICO = '"+ OrdemServico.ServicoId.ToString() +"' AND ROWNUM = 1 AND PE.ID_PESSOA = '"+ favorecidoCobra +"' AND OC.SITUACAO = 'FinalizadaSucesso'"+ depend +" ORDER BY OC.DATA_HORA_CRIACAO DESC ")
        consulta = Utils.ExecuteDataTable(" SELECT distinct ROUND((SYSDATE - OC.DATA_HORA_CRIACAO),0) as DIAS, OC.DATA_HORA_CRIACAO FROM OCORRENCIA OC INNER JOIN ORDEM_SERVICO OS ON (OC.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO SE ON (OS.ID_SERVICO = SE.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CP ON (CP.ID_OCORRENCIA = OC.ID_OCORRENCIA) INNER JOIN PESSOA PE ON (CP.FAVORECIDO_COBRA = PE.ID_PESSOA) INNER JOIN CAD_FUNCIONARIO_V CA ON (CA.NOME = PE.NOME) WHERE SE.ID_SERVICO = '"+ OrdemServico.ServicoId.ToString() +"' AND ROWNUM = 1 AND PE.ID_PESSOA = '"+ favorecidoCobra +"' AND OC.SITUACAO = 'FinalizadaSucesso'"+ depend +" ORDER BY OC.DATA_HORA_CRIACAO DESC ")
        dia = 0 
        for linha in consulta.Rows: 
            dia = linha["DIAS"].ToString() 
            
            if (Convert.ToInt32(dia) < 180): 
                Criticas.AdicionaPendencia("Beneficiário já recebeu reembolso odontológico em menos de seis meses.")


                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                #---------- ODONTOLÓGICO
#Convert.ToDateTime(linha["DATA_RECEITA"]).AddDays(120).Date < DateTime.Now.Date)
#
#if (OrdemServico.Servico.Sigla == "AUXODONTOLOGICO"):
#
#
#    if OrdemServico.GetCustom("DATA_DOCUMENTO") == "" or OrdemServico.GetCustom("DATA_DOCUMENTO") == None :
#        Criticas.AdicionaPendencia("Campo 'Data do Orçamento' é Obrigatório")
#    #else:
#    #    dias = OrdemServico.GetCustom("DATA_DOCUMENTO").AddDays(60)
#    #    if dias < OrdemServico.DataHoraCriacao :
#    #        Criticas.AdicionaPendencia("A data do orçamento é superior a 60 dias da abertura da OS")
#    
#    elif (Convert.ToDateTime("DATA_DOCUMENTO").AddDays(60).Date) < (OrdemServico.DataHoraCriacao):
#        #Criticas.AdicionaPendencia("Data da Receita não pode ser anterior a 60 dias.")
#        Criticas.AdicionaPendencia("A data do orçamento é superior a 60 dias da abertura da OS")
#            
#    #--- Verifica se existe outro chamado aberto para o Cliente
#
#    depend= " AND (CPOS.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CPOS.NOME = '"+ dependenteCobra +"')"
#    if (dependenteCobra == "is NULL"):
#        depend= " AND (CPOS.DEP_FAVORECIDO_COBRA "+ dependenteCobra +" AND CPOS.NOME "+ dependenteCobra +")"
#    
#    lista = Utils.ExecuteDataTable("SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O INNER JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) INNER JOIN PESSOA F ON (CPOS.FAVORECIDO_COBRA = F.ID_PESSOA) WHERE S.ID_SERVICO = '"+ OrdemServico.ServicoId.ToString() +"' AND O.SITUACAO = 'Aberto' AND O.NUMERO <> '"+ numero +"' AND F.ID_PESSOA = '"+ favorecidoCobra +"'"+ depend)
#
#    for linha in lista.Rows:
#        numeroRegistro = linha["CONTADOR"]
#
#    if (numeroRegistro >= 1):
#        Criticas.AdicionaPendencia("Já existe um chamado aberto! Aguarde análise da equipe da GGP para abrir outro") 
#    else:
#        #--- Verifica tempo para solicitação de auxilio odontológico
#
#        depend= " AND (CP.DEP_FAVORECIDO_COBRA = '"+ dependenteCobra +"' OR CP.NOME = '"+ dependenteCobra +"')"
#        if (dependenteCobra == "is NULL"):
#            depend= " AND (CP.DEP_FAVORECIDO_COBRA "+ dependenteCobra +" AND CP.NOME "+ dependenteCobra +")"
#    
#        #consulta = Utils.ExecuteDataTable(" SELECT distinct ROUND((SYSDATE - OC.DATA_HORA_CRIACAO),0) as DIAS, OC.DATA_HORA_CRIACAO FROM OCORRENCIA OC INNER JOIN ORDEM_SERVICO OS ON (OC.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO SE ON (OS.ID_SERVICO = SE.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CP ON (CP.ID_OCORRENCIA = OC.ID_OCORRENCIA) INNER JOIN PESSOA PE ON (CP.FAVORECIDO_COBRA = PE.ID_PESSOA) INNER JOIN CAD_FUNCIONARIO_V CA ON (CA.NOME = PE.NOME) LEFT JOIN DEPENDENTES_BENEFICIOS_V DEP ON (DEP.MATRICULA = CA.MATRICULA and CP.DEP_FAVORECIDO_COBRA = DEP.NOME_DEPENDENTE) WHERE SE.ID_SERVICO = '"+ OrdemServico.ServicoId.ToString() +"' AND ROWNUM = 1 AND PE.ID_PESSOA = '"+ favorecidoCobra +"' AND OC.SITUACAO = 'FinalizadaSucesso'"+ depend +" ORDER BY OC.DATA_HORA_CRIACAO DESC ")
#        consulta = Utils.ExecuteDataTable(" SELECT distinct ROUND((SYSDATE - OC.DATA_HORA_CRIACAO),0) as DIAS, OC.DATA_HORA_CRIACAO FROM OCORRENCIA OC INNER JOIN ORDEM_SERVICO OS ON (OC.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO SE ON (OS.ID_SERVICO = SE.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CP ON (CP.ID_OCORRENCIA = OC.ID_OCORRENCIA) INNER JOIN PESSOA PE ON (CP.FAVORECIDO_COBRA = PE.ID_PESSOA) INNER JOIN CAD_FUNCIONARIO_V CA ON (CA.NOME = PE.NOME) WHERE SE.ID_SERVICO = '"+ OrdemServico.ServicoId.ToString() +"' AND ROWNUM = 1 AND PE.ID_PESSOA = '"+ favorecidoCobra +"' AND OC.SITUACAO = 'FinalizadaSucesso'"+ depend +" ORDER BY OC.DATA_HORA_CRIACAO DESC ")
#        dia = 0 
#        for linha in consulta.Rows: 
#            dia = linha["DIAS"].ToString() 
#            
#            if (Convert.ToInt32(dia) < 180): 
#                Criticas.AdicionaPendencia("Beneficiário já recebeu reembolso odontológico em menos de seis meses.")
```
**ScriptFormCarregado**
```python
idFavorecido = OrdemServico.GetCustom("FAVORECIDO_COBRA")
Formulario["REEMBOLSO_DECLARACAO_MED"].Visivel = True
Formulario["NOME"].Visivel = False
Formulario["NOME"].Habilitado = False
Formulario["REEMBOLSO_DECLARACAO_ESCOLA"].Habilitado = False
Formulario["REEMBOLSO_DECLARACAO_ESCOLA"].Visivel = False
Formulario["DATA_DOCUMENTO"].Visivel = False
Formulario["DATA_DOCUMENTO"].Habilitado = False
Formulario["LISTA_NF"].Habilitado = False
Formulario["LISTA_NF"].Visivel = False
Formulario["LISTA_TRATAMENTO"].Visivel = False

#Bloqueia a alteração do Favorecido
Formulario['FAVORECIDO_COBRA'].Habilitado = False


#--- Nome do dependente
if (Formulario["OPCAO_DE_CONFIRMACAO"].Valor == True) :
    Formulario["NOME"].Visivel = True
    Formulario["NOME"].Habilitado = True

#--- Medicamento
if OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR":
    Formulario["LISTA_NF"].Habilitado = True
    Formulario["LISTA_NF"].Visivel = True
    Formulario["LABEL1"].Valor = '<table><br>___________________________________________________________________________________________________<br><b><font color="red">Se for corrigir a nota fiscal, vai ser preciso apagar o medicamento e inserir novamente!</font></b><br>___________________________________________________________________________________________________<br><br></table>'
    if Formulario["FAVORECIDO_COBRA"].Valor == None:
        Formulario["LISTA_MEDICAMENTOS"].Habilitado = False
        Formulario["LISTA_MEDICAMENTOS"].Visivel = False
        Formulario["LISTA_NF"].Habilitado = False
        Formulario["LISTA_NF"].Visivel = False
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = False

#--- Escola/Creche/Pré-escola/Ótico
if OrdemServico.Servico.Sigla == "ESCOLA" or OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR" or OrdemServico.Servico.Sigla == "CRECHECOLABORADOR" or OrdemServico.Servico.Sigla == "OTICOCOLABORADOR":
    Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = True
    Formulario["DEP_FAVORECIDO_COBRA"].Visivel = True
    Formulario["REEMBOLSO_DECLARACAO_MED"].Visivel = False
    if OrdemServico.Servico.Sigla == "ESCOLA":
        Formulario["REEMBOLSO_DECLARACAO_ESCOLA"].Habilitado = True
        Formulario["REEMBOLSO_DECLARACAO_ESCOLA"].Visivel = True

#--- Odontológico
if OrdemServico.Servico.Sigla == "AUXODONTOLOGICO":
    Formulario["NUM_NOTA_FISCAL"].Visivel = True
    Formulario["NUM_NOTA_FISCAL"].Habilitado = True
    Formulario["REEMBOLSO_DECLARACAO_MED"].Visivel = False
    Formulario["DATA_PAGAMENTO"].Visivel = False
    Formulario["DATA_PAGAMENTO"].Habilitado = False
    Formulario["DATA_DOCUMENTO"].Visivel = True
    Formulario["DATA_DOCUMENTO"].Habilitado = True
    Formulario["LISTA_TRATAMENTO"].Visivel = True
    Formulario["LISTA_TRATAMENTO"].Habilitado = True
    
if OrdemServico.Servico.Sigla == "OTICOCOLABORADOR":
    Formulario["LISTA_REEMBOLSO_OTICO"].Habilitado = True
    Formulario["LISTA_REEMBOLSO_OTICO"].Visivel = True
    

#--- Medicamento
if (OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR"):
    Formulario["LISTA_MEDICAMENTOS"].Habilitado = False
    Formulario["LISTA_MEDICAMENTOS"].Visivel = False  
    Formulario["LISTA_NF"].Habilitado = False
    Formulario["LISTA_NF"].Visivel = False
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["LISTA_NF"].Habilitado = True
        Formulario["LISTA_NF"].Visivel = True
        Formulario["LISTA_MEDICAMENTOS"].Habilitado = True
        Formulario["LISTA_MEDICAMENTOS"].Visivel = True
        dt = OrdemServico.GetCustom("LISTA_NF")
        if (dt.Rows.Count == 0):
            Formulario["LISTA_MEDICAMENTOS"].Habilitado = False
            Formulario["LISTA_MEDICAMENTOS"].Visivel = False    
    else:
        Formulario["LISTA_MEDICAMENTOS"].Habilitado = False
        Formulario["LISTA_MEDICAMENTOS"].Visivel = False
    Formulario["LISTA_MEDICAMENTOS"].Valor = None
    Formulario["LISTA_NF"].Valor = None


#--- Ótico
if (OrdemServico.Servico.Sigla == "OTICOCOLABORADOR"):
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["DEP_FAVORECIDO_COBRA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +"  AND dep.beneficio = 'MATERIAL OTICO - REEMBOLSO' ORDER BY DEP.NOME_DEPENDENTE ")



#--- Creche
if (OrdemServico.Servico.Sigla == "CRECHECOLABORADOR"):
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["DEP_FAVORECIDO_COBRA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +"  AND dep.beneficio = 'REEMBOLSO DE CRECHE' ORDER BY DEP.NOME_DEPENDENTE ")



#--- Pré-escola
if (OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR"):
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["DEP_FAVORECIDO_COBRA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +"  AND dep.beneficio = 'AUX PRE-ESCOLA' ORDER BY DEP.NOME_DEPENDENTE ")


#--- ODONTOLOGICO
if (OrdemServico.Servico.Sigla == "AUXODONTOLOGICO"):
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["DEP_FAVORECIDO_COBRA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +"  AND dep.beneficio = 'ASSIST ODONTOLOGICA - REEMBOLSO' ORDER BY DEP.NOME_DEPENDENTE ")


#--- Escola
if (OrdemServico.Servico.Sigla == "ESCOLA"):
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["DEP_FAVORECIDO_COBRA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +" AND dep.beneficio = 'AUXILIO ESCOLA' ORDER BY DEP.NOME_DEPENDENTE ")
```
- Operação PR0001 Preencher Campos
  - LISTA_TRATAMENTO "Lista de Tratamento Odontológico" [DataGrid RecordList → Z_00143_LISTA_TRATAMENTO.LISTA_TRATAMENTO]
    - coluna VALOR_PAGO obrigatório
    - coluna TRATAMENTO obrigatório
**LISTA_TRATAMENTO.TRATAMENTO.ScriptModificado**
```python
consulta = Utils.ExecuteDataTable("select NVL(SS.VALOR,0) as VALOR from TB_CAD_SUBSERVICO SS WHERE SS.ID_CAD_SUBSERVICO='"+FormularioRegistro["TRATAMENTO"].Valor+"'")
for valor in consulta.Rows:	
	FormularioRegistro["VALOR_TRATAMENTO"].Valor = valor["VALOR"]
```
    - coluna VALOR_TRATAMENTO
    - coluna QUANTIDADE obrigatório
    - coluna VALOR_FINAL
  - REEMBOLSO_DECLARACAO_ESCOLA "Declaro que não recebo de outra instituição, reembolso escola para este dependente." [CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO_ESCOLA]
  - DEP_FAVORECIDO_COBRA "Dependente" [DropDownList String → CP_ORDEM_SERVICO.DEP_FAVORECIDO_COBRA]
  - FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
**FAVORECIDO_COBRA.ScriptModificado**
```python
OrdemServico.SetCustom("FAVORECIDO_COBRA",Controle.Valor)
idFavorecido = OrdemServico.GetCustom("FAVORECIDO_COBRA")


#--- Medicamento
if (OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR"):
    Formulario["LISTA_MEDICAMENTOS"].Habilitado = False
    Formulario["LISTA_MEDICAMENTOS"].Visivel = False  
    Formulario["LISTA_NF"].Habilitado = False
    Formulario["LISTA_NF"].Visivel = False
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["LISTA_NF"].Habilitado = True
        Formulario["LISTA_NF"].Visivel = True
        Formulario["LISTA_MEDICAMENTOS"].Habilitado = True
        Formulario["LISTA_MEDICAMENTOS"].Visivel = True
        dt = OrdemServico.GetCustom("LISTA_NF")
        if (dt.Rows.Count == 0):
            Formulario["LISTA_MEDICAMENTOS"].Habilitado = False
            Formulario["LISTA_MEDICAMENTOS"].Visivel = False    
    else:
        Formulario["LISTA_MEDICAMENTOS"].Habilitado = False
        Formulario["LISTA_MEDICAMENTOS"].Visivel = False
    Formulario["LISTA_MEDICAMENTOS"].Valor = None
    Formulario["LISTA_NF"].Valor = None


#--- Ótico
if (OrdemServico.Servico.Sigla == "OTICOCOLABORADOR"):
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["DEP_FAVORECIDO_COBRA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +"  AND dep.beneficio = 'MATERIAL OTICO - REEMBOLSO' ORDER BY DEP.NOME_DEPENDENTE ")
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = True
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = True
    else:
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = False
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = False
    Formulario["DEP_FAVORECIDO_COBRA"].Valor = None


#--- Creche
if (OrdemServico.Servico.Sigla == "CRECHECOLABORADOR"):
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["DEP_FAVORECIDO_COBRA"].Valor = None
        Formulario["DEP_FAVORECIDO_COBRA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +"  AND dep.beneficio = 'REEMBOLSO DE CRECHE' ORDER BY DEP.NOME_DEPENDENTE ")
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = True
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = True
    else:
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = False
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = False
    Formulario["DEP_FAVORECIDO_COBRA"].Valor = None


#--- Pré-escola
if (OrdemServico.Servico.Sigla == "PREESCOLACOLABORADOR"):
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["DEP_FAVORECIDO_COBRA"].Valor = None
        Formulario["DEP_FAVORECIDO_COBRA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +"  AND dep.beneficio = 'AUX PRE-ESCOLA' ORDER BY DEP.NOME_DEPENDENTE ")
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = True
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = True
    else:
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = False
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = False
    Formulario["DEP_FAVORECIDO_COBRA"].Valor = None

#--- ODONTOLOGICO
if (OrdemServico.Servico.Sigla == "AUXODONTOLOGICO"):
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["DEP_FAVORECIDO_COBRA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +"  AND dep.beneficio = 'ASSIST ODONTOLOGICA - REEMBOLSO' ORDER BY DEP.NOME_DEPENDENTE ")
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = True
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = True
    else:
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = False
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = False
    Formulario["DEP_FAVORECIDO_COBRA"].Valor = None

#--- Escola
if (OrdemServico.Servico.Sigla == "ESCOLA"):
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["DEP_FAVORECIDO_COBRA"].Valor = None
        Formulario["DEP_FAVORECIDO_COBRA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +" AND dep.beneficio = 'AUXILIO ESCOLA' ORDER BY DEP.NOME_DEPENDENTE ")
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = True
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = True
    else:
        Formulario["DEP_FAVORECIDO_COBRA"].Habilitado = False
        Formulario["DEP_FAVORECIDO_COBRA"].Visivel = False
    Formulario["DEP_FAVORECIDO_COBRA"].Valor = None
```
  - LISTA_NF "Lista NF(informar COO apenas se não houver NF). Máximo de 3 Notas Fiscais" [DataGrid RecordList → Z_00143_LISTA_NF.LISTA_NF] — QtdColunasFormulario=1; PosicaoRotulo=Topo
**LISTA_NF.ScriptModificado**
```python
dt = OrdemServico.GetCustom("LISTA_NF")
if (dt.Rows.Count>=3):
    FormularioRegistro["CNPJ"].Habilitado=False
    FormularioRegistro["NUMERO_NF"].Habilitado=False
    Formulario["LISTA_MEDICAMENTOS"].Habilitado = True
    Formulario["LISTA_MEDICAMENTOS"].Visivel = True
```
**LISTA_NF.ScriptConfirmado**
```python
import validaCNPJ
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.
Formulario["LISTA_MEDICAMENTOS"].Habilitado = False
Formulario["LISTA_MEDICAMENTOS"].Visivel = False  
Formulario["LISTA_NF"].Habilitado = False
Formulario["LISTA_NF"].Visivel = False

numero = "0"
if (OrdemServico.Numero.ToString()!= ""):
    numero = OrdemServico.Numero.ToString()
listaNF = OrdemServico.GetCustom("LISTA_NF")
for linhaNF in listaNF.Rows:
    # Critica CNPJ
    resultado = validaCNPJ(linhaNF["CNPJ"])
    if  resultado != "ok":
        Formulario.ExibeMensagem("CNPJ " + resultado + " Inválido")
    if  String.IsNullOrEmpty(linhaNF["NUMERO_NF"].ToString()):
        Formulario.ExibeMensagem("Número da nota fiscal Inválido")
        resultado = "Erro"
    if  resultado == "ok" :
        # Verifica se já existe O.S. para a nota fiscal
        qry = "SELECT count(LM.NUM_NOTA_FISCAL) CONTADOR FROM OCORRENCIA OC INNER JOIN ORDEM_SERVICO OS ON OC.ID_OCORRENCIA = OS.ID_OCORRENCIA INNER JOIN SERVICO SE ON OS.ID_SERVICO = SE.ID_SERVICO INNER JOIN Z_00143_LISTA_MEDICAMENTOS LM ON LM.ID_OCORRENCIA = OC.ID_OCORRENCIA WHERE SE.SIGLA = '" + OrdemServico.Servico.Sigla + "' AND OC.NUMERO <> '" + numero + "' AND LM.NUM_NOTA_FISCAL = '" + linhaNF["NUMERO_NF"] + "' AND OC.SITUACAO <> 'Cancelada' AND OC.SITUACAO <> 'FinalizadaNaoRealizada' AND LM.CNPJ = '" + linhaNF["CNPJ"]+ "' group by LM.NUM_NOTA_FISCAL "
        lista = Utils.ExecuteDataTable(qry)
        
        ###Criticas.AdicionaPendencia(qry)
        
        numeroRegistro = 0
        for registro in lista.Rows:
            numeroRegistro = registro["CONTADOR"]

        if (numeroRegistro >= 1):
            Formulario.ExibeMensagem("Já existe O.S. para o documento Fiscal número " + linhaNF["NUMERO_NF"] + " do CNPJ " + linhaNF["CNPJ"] + "." )

resultado = validaCNPJ(FormularioRegistro["CNPJ"].Valor)
if  resultado != "ok":
    Formulario.ExibeMensagem("CNPJ " + resultado + " Inválido")
    Cancela=True
if  String.IsNullOrEmpty(FormularioRegistro["NUMERO_NF"].Valor):
    Formulario.ExibeMensagem("Número da nota fiscal Inválido")
    resultado = "Erro"
    Cancela=True
if  resultado == "ok" :
    # Verifica se já existe O.S. para a nota fiscal
    qry = "SELECT count(LM.NUM_NOTA_FISCAL) CONTADOR FROM OCORRENCIA OC INNER JOIN ORDEM_SERVICO OS ON OC.ID_OCORRENCIA = OS.ID_OCORRENCIA INNER JOIN SERVICO SE ON OS.ID_SERVICO = SE.ID_SERVICO INNER JOIN Z_00143_LISTA_MEDICAMENTOS LM ON LM.ID_OCORRENCIA = OC.ID_OCORRENCIA WHERE SE.SIGLA = '" + OrdemServico.Servico.Sigla + "' AND OC.NUMERO <> '" + numero + "' AND LM.NUM_NOTA_FISCAL = '" + FormularioRegistro["NUMERO_NF"].Valor.ToString() + "' AND OC.SITUACAO <> 'Cancelada' AND OC.SITUACAO <> 'FinalizadaNaoRealizada' AND LM.CNPJ = '" +FormularioRegistro["CNPJ"].Valor.ToString() + "' group by LM.NUM_NOTA_FISCAL "
    lista = Utils.ExecuteDataTable(qry)
    
    ###Criticas.AdicionaPendencia(qry)
    
    numeroRegistro = 0
    for registro in lista.Rows:
        numeroRegistro = registro["CONTADOR"]

    if (numeroRegistro >= 1):
        Formulario.ExibeMensagem("Já existe O.S. para o documento Fiscal número " + FormularioRegistro["NUMERO_NF"].Valor.ToString() + " do CNPJ " + FormularioRegistro["CNPJ"].Valor.ToString() + "." )
        Cancela=True



#--- Medicamento
if (OrdemServico.Servico.Sigla == "MEDICAMENTOCOLABORADOR"):
    if (Formulario["FAVORECIDO_COBRA"].Valor != None):
        Formulario["LISTA_NF"].Habilitado = True
        Formulario["LISTA_NF"].Visivel = True

        #dt = Formulario("LISTA_NF")
        if (String.IsNullOrEmpty(FormularioRegistro["CNPJ"].Valor)):
            Formulario["LISTA_MEDICAMENTOS"].Habilitado = False
            Formulario["LISTA_MEDICAMENTOS"].Visivel = False
        else:
            Formulario["LISTA_MEDICAMENTOS"].Habilitado = True
            Formulario["LISTA_MEDICAMENTOS"].Visivel = True    
    else:
        Formulario["LISTA_MEDICAMENTOS"].Habilitado = False
        Formulario["LISTA_MEDICAMENTOS"].Visivel = False
    Formulario["LISTA_MEDICAMENTOS"].Valor = None
    Formulario["LISTA_NF"].Valor = None
    
    dt = OrdemServico.GetCustom("LISTA_NF")
    if (dt.Rows.Count>=3):
        Cancela=True
```
    - coluna CNPJ obrigatório
    - coluna NUMERO_NF obrigatório
  - LISTA_REEMBOLSO_OTICO "Dados do Reembolso Ótico" [DataGrid RecordList → Z_00143_LISTA_REEMBOLSO_OTICO.LISTA_REEMBOLSO_OTICO] obrigatório — QtdColunasFormulario=1
    - coluna TIPO_REEMBOLSO obrigatório
    - coluna NOME_DEPENDENTE
    - coluna NOTA_FISCAL obrigatório
    - coluna DATA_RECEITA obrigatório
  - VALOR_NOTA_FISCAL "Valor da Nota Fiscal" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_NOTA_FISCAL] obrigatório
  - NUM_NOTA_FISCAL "Número do COO (Nota Fiscal)" [TextBox Integer → CP_ORDEM_SERVICO.NUM_NOTA_FISCAL] obrigatório
  - VALOR_MENSALIDADE "Valor da mensalidade" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_MENSALIDADE] obrigatório
  - LISTA_MEDICAMENTOS "Lista de Medicamentos" [DataGrid RecordList → Z_00143_LISTA_MEDICAMENTOS.LISTA_MEDICAMENTOS] obrigatório — QtdColunasFormulario=3
**LISTA_MEDICAMENTOS.ScriptModificado**
```python
FormularioRegistro["CNPJ"].Visivel = True
FormularioRegistro["CNPJ"].Habilitado = True
dt = OrdemServico.GetCustom("LISTA_NF")
itensCNPJ=''
itensNF=''
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ,CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = 636750")
#itensNF=DB.ExecuteDataTable("SELECT NUMERO_NF FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
contCNPJ=0
contNF=0
regdr=0
#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCNPJ=0
    igualNF=0
    regdr2=0
    
    for dr2 in dt.Rows:
        if (dr["CNPJ"]== dr2["CNPJ"]):
            if (regdr<=regdr2 and igualCNPJ==0):
                igualCNPJ=0
            else:
                igualCNPJ=1
        if (dr["NUMERO_NF"]== dr2["NUMERO_NF"]):
            if (regdr<=regdr2 and igualNF==0):
                igualNF=0
            else:
                igualNF=1
        regdr2=regdr2+1
    if (igualCNPJ<=0):
        if (contCNPJ==0):
            itensCNPJ=dr["CNPJ"]
            #itensCNPJ=dt.Rows.Count.ToString()
            contCNPJ=1
        else:
            itensCNPJ = itensCNPJ+';'+dr["CNPJ"]
    if (igualNF<=0):
        if (contNF==0):
            itensNF=dr["NUMERO_NF"]
            contNF=1
        else:
            itensNF = itensNF+';'+dr["NUMERO_NF"]
    regdr=regdr+1
FormularioRegistro["CNPJ"].Itens = itensCNPJ
FormularioRegistro["NUM_NOTA_FISCAL"].Itens = itensNF
```
    - coluna CNPJ obrigatório
**LISTA_MEDICAMENTOS.CNPJ.ScriptModificado**
```python
FormularioRegistro["CNPJ"].Visivel = True
FormularioRegistro["CNPJ"].Habilitado = True
dt = OrdemServico.GetCustom("LISTA_NF")
itensCNPJ=''
itensNF=''
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ,CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = 636750")
#itensNF=DB.ExecuteDataTable("SELECT NUMERO_NF FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
contCNPJ=0
contNF=0
regdr=0
#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCNPJ=0
    igualNF=0
    regdr2=0
    
    for dr2 in dt.Rows:
        if (dr["CNPJ"]== dr2["CNPJ"]):
            if (regdr<=regdr2 and igualCNPJ==0):
                igualCNPJ=0
            else:
                igualCNPJ=1
        if (dr["NUMERO_NF"]== dr2["NUMERO_NF"]):
            if (regdr<=regdr2 and igualNF==0):
                igualNF=0
            else:
                igualNF=1
        regdr2=regdr2+1
    if (igualCNPJ<=0):
        if (contCNPJ==0):
            itensCNPJ=dr["CNPJ"]
            #itensCNPJ=dt.Rows.Count.ToString()
            contCNPJ=1
        else:
            itensCNPJ = itensCNPJ+';'+dr["CNPJ"]
    if (igualNF<=0):
        if (contNF==0):
            itensNF=dr["NUMERO_NF"]
            contNF=1
        else:
            itensNF = itensNF+';'+dr["NUMERO_NF"]
    regdr=regdr+1
FormularioRegistro["CNPJ"].Itens = itensCNPJ
FormularioRegistro["NUM_NOTA_FISCAL"].Itens = itensNF
```
    - coluna NUM_NOTA_FISCAL obrigatório
**LISTA_MEDICAMENTOS.NUM_NOTA_FISCAL.ScriptModificado**
```python
dt = OrdemServico.GetCustom("LISTA_NF")
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ,CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = 636750")
#itensNF = DB.ExecuteDataTable("SELECT NUMERO_NF FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
#itensCNPJ=None
itensCNPJ = ''
cont=0
##if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    if (FormularioRegistro["NUM_NOTA_FISCAL"].Valor == dr["NUMERO_NF"]):
        if (cont==0):
            itensCNPJ=dr["CNPJ"]
        else:
            itensCNPJ = itensCNPJ+';'+dr["CNPJ"]
    #if (cont==0):
    #    itensNF=dr["NUMERO_NF"]
    #else:
    #    itensNF = itensNF+';'+dr["NUMERO_NF"]
        cont=1
FormularioRegistro["CNPJ"].Itens = itensCNPJ
#FormularioRegistro["NUM_NOTA_FISCAL"].Itens = itensNF
```
    - coluna DATA_RECEITA obrigatório
    - coluna VALOR_MEDICAMENTO obrigatório
    - coluna NOME_MEDICAMENTO obrigatório
    - coluna TIPO obrigatório
    - coluna DEPENDENTE
  - REEMBOLSO_DECLARACAO "Declaro que não recebo de outra instituição, reembolso creche/pré-escola para este dependente." [CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO] obrigatório
  - DATA_PAGAMENTO "Data mês referência" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_PAGAMENTO]
  - DATA_DOCUMENTO "Data do Orçamento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_DOCUMENTO]
  - OPCAO_DE_CONFIRMACAO "Dependente não cadastrado" [CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO]
**OPCAO_DE_CONFIRMACAO.ScriptModificado**
```python
Formulario["NOME"].Visivel = False
Formulario["NOME"].Habilitado = False
Formulario["NOME"].Valor = ""

if (Formulario["OPCAO_DE_CONFIRMACAO"].Valor == True) :
    Formulario["NOME"].Visivel = True
    Formulario["NOME"].Habilitado = True
    Formulario.ExibeMensagem("Favor anexar o arquivo 'Comprovação de dependência'")
```
  - NOME "Nome Completo do Dependente" [TextBox String → CP_ORDEM_SERVICO.NOME]
  - LABEL1 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - REEMBOLSO_DECLARACAO_MED "

Declaro que o reembolso solicitado não se refere a medicamentos com finalidade de tratamentos estéticos e/ou cosméticos." [CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO_MED]
- Operação PR0004 Associar Itens Configuração: Nome=COMPROVACAO_DE_DEPENDENCI
  - anexo "Comprovação de dependência, somente em casos de dependente não cadastrado." classes: Comprovação de dependência — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=ARQUIVOS OBRIGATORIOS ANEXO
  - anexo "Comprovante de pagamento" classes: Comprovante de Pagamento Depósito — ProduzidoTermino=true
  - anexo "Anexar Orçamento" classes: Orçamento — RequeridoInicial=true
  - anexo "Boleto Bancário" classes: Boleto Bancário — ProduzidoTermino=true
  - anexo "Receituário" classes: Receituário — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "NF" classes: Nota Fiscal — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Anexo — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=RECEITUARIO OPCIONAL ANEXO
  - anexo "Receituário" classes: Receituário — RequeridoInicial=true; PermiteMultiplosItens=true
- Acoes:
  - Acao=Categorizar; Percentual=50; CodigoGrupoANO=6e7d5991-6031-4343-9cb5-896776dd7d7f; CategoriaId=4; Categoria=Alta

### [360768] LinkInicial "Reembolso Medicamento"
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - Assunto (nativo) obrigatório
  - LISTA_NF "Lista de NF(COO)" [DataGrid RecordList → Z_00143_LISTA_NF.LISTA_NF] obrigatório
    - coluna CNPJ obrigatório
    - coluna NUMERO_NF obrigatório
  - LISTA_MEDICAMENTOS "Lista de Medicamentos" [DataGrid RecordList → Z_00143_LISTA_MEDICAMENTOS.LISTA_MEDICAMENTOS] obrigatório
**LISTA_MEDICAMENTOS.ScriptModificado**
```python
FormularioRegistro["CNPJ"].Visivel = True
FormularioRegistro["CNPJ"].Habilitado = True
dt = OrdemServico.GetCustom("LISTA_NF")
itensCNPJ=''
itensNF=''
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
#itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ,CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = 636750")
#itensNF=DB.ExecuteDataTable("SELECT NUMERO_NF FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
contCNPJ=0
contNF=0
regdr=0
#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCNPJ=0
    igualNF=0
    regdr2=0
    
    for dr2 in dt.Rows:
        if (dr["CNPJ"]== dr2["CNPJ"]):
            if (regdr<=regdr2 and igualCNPJ==0):
                igualCNPJ=0
            else:
                igualCNPJ=1
        if (dr["NUMERO_NF"]== dr2["NUMERO_NF"]):
            if (regdr<=regdr2 and igualNF==0):
                igualNF=0
            else:
                igualNF=1
        regdr2=regdr2+1
    if (igualCNPJ<=0):
        if (contCNPJ==0):
            itensCNPJ=dr["CNPJ"]
            #itensCNPJ=dt.Rows.Count.ToString()
            contCNPJ=1
        else:
            itensCNPJ = itensCNPJ+';'+dr["CNPJ"]
    if (igualNF<=0):
        if (contNF==0):
            itensNF=dr["NUMERO_NF"]
            contNF=1
        else:
            itensNF = itensNF+';'+dr["NUMERO_NF"]
    regdr=regdr+1
FormularioRegistro["CNPJ"].Itens = itensCNPJ
FormularioRegistro["NUM_NOTA_FISCAL"].Itens = itensNF
```
    - coluna DATA_RECEITA obrigatório
    - coluna NUM_NOTA_FISCAL obrigatório
    - coluna DEPENDENTE
    - coluna NOME_MEDICAMENTO obrigatório
    - coluna CNPJ obrigatório
    - coluna VALOR_MEDICAMENTO obrigatório
    - coluna TIPO obrigatório
  - REEMBOLSO_DECLARACAO_MED "

Declaro que o reembolso solicitado não se refere a medicamentos com finalidade de tratamentos estéticos e/ou cosméticos." [CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO_MED] obrigatório
  - FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA]
  - OPCAO_DE_CONFIRMACAO "Dependente não cadastrado" [CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO]
  - NOME "Nome Completo do Dependente" [TextBox String → CP_ORDEM_SERVICO.NOME]
- Associação de subprocesso: AssociacaoId=324; FraseAssociacao=Chatbot -> Reembolso Medicamento; Nome=CHATBOTREEMBOLSOMEDICAMENTO

### [360769] LinkInicial "Reembolso Pré-Escola"
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - COMBOBOX1 "Tipo de Benefício" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
  - DATA_PAGAMENTO "Data de pagamento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_PAGAMENTO] obrigatório
  - FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - NOME "Nome" [TextBox String → CP_ORDEM_SERVICO.NOME] obrigatório
  - OPCAO_DE_CONFIRMACAO "Dependente não cadastrado" [CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO]
  - REEMBOLSO_DECLARACAO "Declaro que não recebo de outra instituição, reembolso creche/pré-escola para este dependente." [CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO] obrigatório
  - REEMBOLSO_DECLARACAO_ESCOLA "Declaro que não recebo de outra instituição, reembolso escola para este dependente." [CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO_ESCOLA] obrigatório
  - VALOR_MENSALIDADE "Valor da mensalidade" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_MENSALIDADE] obrigatório
- Associação de subprocesso: AssociacaoId=326; FraseAssociacao=Chat Bot Reembolso Pré-escola -> Reembolso; Nome=CHATBOTREEMBOLSOPREESCOLA

### [360770] EventoFinal "Finalizada Não realizado"
Responsável: Sistema (papel 1)
Config: TipoFinalizacao=NaoRealizado
**ScriptValidacao**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if String.IsNullOrEmpty(OrdemServico["MATRICULA"].ToString()):
   pessoa = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))
   OrdemServico["MATRICULA"] = pessoa["MATRICULA"]
   OrdemServico.Salva()
```

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
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 461: Fila CSC - Pendente de Aprovação
Tipo=RelacaoPessoas | pessoas: Fila CSC - Pendente de Aprovação
### papel 941: Cesec-PEAD Marina
Tipo=RelacaoPessoas | pessoas: MARINA DE MELO RIBEIRO MATSUI
### papel 1310: Gerente Cesec PES
Tipo=RelacaoOrgaos
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```
### papel 340: Responsável atual da atividade
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Customizado.OrdemServico.RESPONSAVEL_ATUAL
### papel 312: Cliente e Favorecido Cobra
Tipo=Composto
- composto por: Favorecido Cobra (Script)
- composto por: Cliente (PessoaOrdemServico)
### papel 544: Cliente e Responsavel Atual
Tipo=Composto
- composto por: Cliente (PessoaOrdemServico)
- composto por: Responsável atual (PessoaOrdemServico)
### papel 385: Favorecido Todos
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.GetCustom("FAVORECIDO_TODOS"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_TODOS")))

    if favorecido != None:
        Atores.Adiciona(favorecido, "Favorecido")
```
### papel 1: Sistema
Tipo=RelacaoPessoas | pessoas: Sistema

## Campos customizados usados (definição global)

### DATA_PAGAMENTO — Data de pagamento
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_PAGAMENTO
Descrição: Data do pagamento

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### COMBOBOX1 — Chamado Aberto?
DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1

### NOME — Nome
TextBox String → CP_ORDEM_SERVICO.NOME

### OPCAO_DE_CONFIRMACAO — Campo confirma uma afirmação
CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO
Descrição: Campo genérico para confirmação de uma afirmação

### REEMBOLSO_DECLARACAO — Declaro que não recebo de outra instituição, reembolso creche/pré-escola para este dependente.
CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO

### REEMBOLSO_DECLARACAO_ESCOLA — Declaro que não recebo de outra instituição, reembolso escola para este dependente.
CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO_ESCOLA

### VALOR_MENSALIDADE — Valor da mensalidade
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_MENSALIDADE

### NOMEDEPENDENTE — Nome do dependente
TextBox String → CPE_CSC.NOMEDEPENDENTE
Descrição: Nome dependente

### DATA_DOCUMENTO — Data do documento
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_DOCUMENTO
Descrição: Data de aprovação ou criação do documento

### LISTA_TRATAMENTO — LISTA_TRATAMENTO
DataGrid RecordList → Z_00143_LISTA_TRATAMENTO.LISTA_TRATAMENTO
Descrição: Lista de tratamentos odontológicos
Colunas do registro:
- VALOR_FINAL "Valor Final" [TextBox String]
- VALOR_PAGO "Valor Unitário Pago" [TextBox Decimal]
- TRATAMENTO "Tratamento" [DropDownList String]
**TRATAMENTO.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT to_char(S.ID_CAD_SUBSERVICO), S.DESC_SUBSERVICO FROM TB_REEMBOLSO_SUBSERVICO RS INNER JOIN TB_CAD_REEMBOLSO R ON R.ATIVO='S' AND R.ID_CAD_REEMBOLSO=RS.ID_CAD_REEMBOLSO INNER JOIN TB_CAD_SUBSERVICO S ON S.ATIVO='S' AND S.ID_CAD_SUBSERVICO=RS.ID_CAD_SUBSERVICO WHERE R.SIGLA_SERVICO='AUXODONTOLOGICO'")
```
- VALOR_TRATAMENTO "Valor tratamento(Limite referente a 50% do Valor Unitário Pago)" [TextBox Decimal]
- QUANTIDADE "Quantidade" [TextBox Integer]

### NUM_NOTA_FISCAL — ID da Nota Fiscal
TextBox Integer → CP_ORDEM_SERVICO.NUM_NOTA_FISCAL

### SERVICO_SELECIONADO — Serviço Selecionado
TextBox String → CP_ORDEM_SERVICO.SERVICO_SELECIONADO

### QUANTIDADE — Quantidade
TextBox Integer → CP_ORDEM_SERVICO.QUANTIDADE

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### LISTA_MEDICAMENTOS — Lista de Medicamentos
DataGrid RecordList → Z_00143_LISTA_MEDICAMENTOS.LISTA_MEDICAMENTOS
Colunas do registro:
- CNPJ "CNPJ (da NF)" [DropDownList String]
**CNPJ.LookupScript**
```python
#Itens=''
```
- NOME_MEDICAMENTO "Nome do Medicamento" [TextBox DateTime]
- VALOR_MEDICAMENTO "Valor" [TextBox Decimal]
- TIPO "Tipo" [DropDownList String] itens: Comum;Contínuo;Medicamentos a base de canabidiol;Medicamentos que atuam como agentes metabólicos - vide NI103;Increnoativos: Ozempic, Mounjaro, entre outros, vide NI103;Formula Infantil - vide NI103
- NUM_NOTA_FISCAL "Número do COO (Nota Fiscal)" [DropDownList String]
**NUM_NOTA_FISCAL.LookupScript**
```python
#Itens = DB.ExecuteDataTable("SELECT CNPJ,NUMERO_NF FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = 636750")
#DB.ExecuteDataTable("SELECT NUMERO_NF FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())

#dt = OrdemServico.GetCustom("LISTA_NF")
##itensNF = DB.ExecuteDataTable("SELECT NUMERO_NF FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = "+OrdemServico.Id.ToString())
##itensCNPJ = DB.ExecuteDataTable("SELECT CNPJ,CNPJ FROM Z_00143_LISTA_NF WHERE ID_OCORRENCIA = 636750")
#itensNF=''
##cont=0
##if (itensNF.Rows.Count==0):
#if (dt.Rows.Count==0):
#    for dr in dt.Rows:
#        if (cont==0):
#            itensNF=dr["NUMERO_NF"]
#        else:
#            itensNF = itensNF+';'+dr["NUMERO_NF"]
#        cont=1
#Itens = ''
```
- DATA_RECEITA "Data da Receita" [DateTimePicker DateTime]
- DEPENDENTE "Dependentes" [DropDownList String]
**DEPENDENTE.LookupScript**
```python
idFavorecido = OrdemServico.GetCustom("FAVORECIDO_COBRA")

#if idFavorecido != None:
#    Itens = DB.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +"  AND dep.beneficio = 'REEMBOLSO FARMACIA' ORDER BY DEP.NOME_DEPENDENTE ")
    

if OrdemServico.GetCustom("FAVORECIDO_COBRA").ToString() != "":
    Itens = DB.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ OrdemServico.GetCustom("FAVORECIDO_COBRA").ToString() +" and dep.nome_dependente <> ' ' AND dep.beneficio = 'REEMBOLSO FARMACIA' ORDER BY DEP.NOME_DEPENDENTE ")
```
- QUANTIDADE "Quantidade de Caixas" [DropDownList String] itens: 1;2;3

### PARCELAS_PID — Número de parcelas
DropDownList Integer → CP_ORDEM_SERVICO.PARCELAS_PID
Itens: 1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36

### VALOR_TOTAL_REEMBOLSO — Valor Total
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_TOTAL_REEMBOLSO

### LISTA_REEMBOLSO_OTICO — Dados do Reembolso Ótico
DataGrid RecordList → Z_00143_LISTA_REEMBOLSO_OTICO.LISTA_REEMBOLSO_OTICO
Colunas do registro:
- TIPO_REEMBOLSO "Tipo" [DropDownList String] itens: Armação;Lente;Armação/Lente;Lente de Contato
- NOTA_FISCAL "Número do COO (Nota Fiscal)" [TextBox String]
- DATA_RECEITA "Data da Receita" [DatePicker DateTime]

### VALOR_REEMBOLSO — Valor do Reembolso
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO

### LISTA_NF — Lista de NF(COO)
DataGrid RecordList → Z_00143_LISTA_NF.LISTA_NF
Colunas do registro:
- CNPJ "CNPJ (Somente os Números)" [TextBox String]
- NUMERO_NF "Número da NF ou número do COO - sempre informar os zeros a esquerda" [TextBox String]

### MATRICULA — Matrícula
TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA

### VALOR_NOTA_FISCAL — Valor da Nota Fiscal
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_NOTA_FISCAL

### RESPOSTA_REPROVACAO_REEMBOLSO — Justificativa da Reprovação
Memo String(2000) → CP_ORDEM_SERVICO.RESPOSTA_REPROVACAO_REEMBOLSO

### SIM_NAO204 — Sim ou Não
DropDownList String → CPE_CONTRATOS02.SIM_NAO204
Itens: Sim;Não

### VALOR — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR
Descrição: Informe

### CPF — CPF
TextBox String(15) → CP_ORDEM_SERVICO.CPF

### DEMANDA_PROC — Processo
CheckBox Boolean → CP_ORDEM_SERVICO.DEMANDA_PROC

### DEP_FAVORECIDO_COBRA — Dependente
DropDownList String → CP_ORDEM_SERVICO.DEP_FAVORECIDO_COBRA
Descrição: Dependente do Favorecido Cobra
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT DEP.NOME_DEPENDENTE, DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP ORDER BY DEP.NOME_DEPENDENTE")
```

### LABEL2 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL2
Descrição: Texto informativo

### LISTAPCD_TERAPIAS — Auxilio PCD
DataGrid RecordList → Z_00143_LISTAPCD_TERAPIAS.LISTAPCD_TERAPIAS
Colunas do registro:
- TERAPIA "Terapia" [TextBox String]
- VALOR "Valor Unitario" [TextBox Decimal]
- QUANTIDADE "Quantidade" [TextBox Integer]
- DATA "Data Relátorio" [DatePicker DateTime]
- NUM_NOTA_FISCAL "Número do COO (Nota Fiscal)" [DropDownList String]
**NUM_NOTA_FISCAL.LookupScript**
```python
lista = []
for item in OrdemServico.GetCustom("LISTA_NF").Rows:
    lista.append(item["NUMERO_NF"])
Itens = lista
```
- CNPJ "CNPJ" [DropDownList String]
**CNPJ.LookupScript**
```python
lista = []
for item in OrdemServico.GetCustom("LISTA_NF").Rows:
    lista.append(item["CNPJ"])
Itens = lista
```
- DEPENDENTE "Dependentes" [DropDownList String]
**DEPENDENTE.LookupScript**
```python
idFavorecido = OrdemServico.GetCustom("FAVORECIDO_COBRA")

#if idFavorecido != None:
#    Itens = DB.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +"  AND dep.beneficio = 'REEMBOLSO FARMACIA' ORDER BY DEP.NOME_DEPENDENTE ")
    

if OrdemServico.GetCustom("FAVORECIDO_COBRA").ToString() != "":
    Itens = DB.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ OrdemServico.GetCustom("FAVORECIDO_COBRA").ToString() +" and dep.nome_dependente <> ' ' AND dep.beneficio = 'REEMBOLSO FARMACIA' ORDER BY DEP.NOME_DEPENDENTE ")
```

### LISTAPCD_COO — Auxilio PCD Cooparticipação 
DataGrid RecordList → Z_00143_LISTAPCD_COO.LISTAPCD_COO
Colunas do registro:
- TERAPIA "Terapia" [TextBox String]
- VALOR_COO "Valor Unitário da Coparticipação" [TextBox Decimal]
- QUANTIDADE "Quantidade" [TextBox String]
- DATA_RELATORIO "Data relátorio" [DatePicker DateTime]
- CNPJ "CNPJ/CPF" [TextBox String]
- DEPENDENTES "Dependente" [DropDownList String]
**DEPENDENTES.LookupScript**
```python
idFavorecido = OrdemServico.GetCustom("FAVORECIDO_COBRA")

#if idFavorecido != None:
#    Itens = DB.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ idFavorecido.ToString() +"  AND dep.beneficio = 'REEMBOLSO FARMACIA' ORDER BY DEP.NOME_DEPENDENTE ")
    

if OrdemServico.GetCustom("FAVORECIDO_COBRA").ToString() != "":
    Itens = DB.ExecuteDataTable(" SELECT DISTINCT DEP.NOME_DEPENDENTE FROM DEPENDENTES_BENEFICIOS_V DEP INNER JOIN CAD_FUNCIONARIO_V FU ON DEP.MATRICULA = FU.MATRICULA INNER JOIN PESSOA PE ON PE.NOME = FU.NOME WHERE pe.ID_PESSOA = "+ OrdemServico.GetCustom("FAVORECIDO_COBRA").ToString() +" and dep.nome_dependente <> ' ' AND dep.beneficio = 'REEMBOLSO FARMACIA' ORDER BY DEP.NOME_DEPENDENTE ")
```

### COUNT_10 — Count to 12
DropDownList Integer → CPE_PESSOAS.COUNT_10
Itens: 1;2;3;4;5;6;7;8;9;10;11;12

### REEMBOLSO_DECLARACAO_MED — 

Declaro que o reembolso solicitado não se refere a medicamentos com finalidade de tratamentos estéticos e/ou cosméticos.
CheckBox Boolean → CP_ORDEM_SERVICO.REEMBOLSO_DECLARACAO_MED
Descrição: 

*Declaro que o reembolso solicitado não se refere a medicamentos com finalidade de tratamentos estéticos e/ou cosméticos.

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

## Biblioteca de scripts referenciada
peopleSoft, teste, validaCNPJ
(fonte em catalogo/biblioteca/<Nome>.py)
