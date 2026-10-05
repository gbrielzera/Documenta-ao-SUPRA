# Fluxo: Transferência de Bens Patrimoniais (TRANSBENSPATRIMONIAIS) — versão 38
Caminho: Fluxos > Administração - Bens Patrimoniais Versão 38 Transferência de Bens Patrimoniais
XML: `XMLs para teste/Administração_-_Bens_Patrimoniais_Versão_38_Transferência_de_Bens_Patrimoniais.xml` | Supravizio 19.1.1 | SubProcessoId 22356 | DesenhoProcessoId 3043 | ProcessoId 93
Órgão dono: 3000003150 - DIVISAO DE ENGENHARIA E GESTAO DE ESTABELECIMENTOS | Responsável: DAIANY NEVES ROSA
Classe do subprocesso: Objetivo=Transferência de Bens Patrimoniais; DescricaoCliente=Transferência de Bens Patrimoniais; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Transferência de Bens Patrimoniais; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Transferência de Bens Patrimoniais Entre Diferentes UORs (TRANSBENSPATRIMONIAIS); Transferência de Bens Patrimoniais Entre Empregados da Mesma UOR (TRANSFBENFUNCMSMUOR)

## Grafo do fluxo
- [358064] Tarefa "Atualizar dados no ERP/FA" {Responsável atual} → [358068] Execução da atualização | [358070] 
- [358065] EventoIntermediarioMensagem "Reprovação de Chamado" → [358069] 
- [358066] Tarefa "Aprovar Transferência do Órgão Destino" {Fila CSC - Pendente de Aprovação} → [G80568] Gestor Órgão Destinatário aprova movimentação?
- [358067] EventoIntermediarioMensagem "Reprovação de Chamado" → [358072] 
- [358068] EventoIntermediarioTimer "Execução da atualização" → [358064] Atualizar dados no ERP/FA
- [358069] EventoFinal "" → (fim)
- [358070] EventoFinal "" → (fim)
- [358071] Tarefa "Solicitar Aprovação do Gestor da UOR
" {Fila CSC - Pendente de Aprovação} → [G80565] Aprovou?

- [358072] EventoFinal "" → (fim)
- [358073] EventoInicial "Transferência de Bens Patrimoniais" → [G80566] Qual o serviço?

- [358076] Tarefa "Aguardar encerramento da conciliação para avançar esta tarefa." {Fila CSC - Bens Patrimoniais} → [358064] Atualizar dados no ERP/FA
- [358077] EventoIntermediarioMensagem "Reprovação de Chamado" → [358072] 
- [358074] Tarefa "Preencher informações" {Fila CSC - Bens Patrimoniais} → [358075] Aprovar transferência do Órgão Emitente
- [358075] Tarefa "Aprovar transferência do Órgão Emitente" {Fila CSC - Pendente de Aprovação} → [G80567] Gestor Órgão Emitente aprova movimentação?
- [G80565] Gateway "Aprovou?
" → «Reprovado» [358065] Reprovação de Chamado | «Aprovado» [358076] Aguardar encerramento da conciliação para avançar 
- [G80566] Gateway "Qual o serviço?
" → «Transferência de Bens entre Empregados da mesma UOR» [358071] Solicitar Aprovação do Gestor da UOR
 | «Transferência de Bens entre diferentes UORs» [358074] Preencher informações
- [G80567] Gateway "Gestor Órgão Emitente aprova movimentação?" → «Sim» [358066] Aprovar Transferência do Órgão Destino | «Não» [358067] Reprovação de Chamado
- [G80568] Gateway "Gestor Órgão Destinatário aprova movimentação?" → «Não» [358077] Reprovação de Chamado | «Sim» [358076] Aguardar encerramento da conciliação para avançar 

## Gateways
### [G80565] Aprovou?
 (DataBasedExclusiveDecision)
Codigo=APROVA
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("DEASDA")
```
- alternativa → [358065] Reprovação de Chamado: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
- alternativa → [358076] Aguardar encerramento da conciliação para avançar : OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
### [G80566] Qual o serviço?
 (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla
```
- alternativa → [358071] Solicitar Aprovação do Gestor da UOR
: OperadorDecision=Equal; ReferenciaDecision=Transferência de Bens entre Empregados da mesma UOR; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
"TRANSFBENFUNCMSMUOR"
```
- alternativa → [358074] Preencher informações: OperadorDecision=Equal; ReferenciaDecision=Transferência de Bens entre diferentes UORs; SequenciaAvaliacao=0; RotuloMotivo=Transferência entre funcionários da mesma UOR
**ValorComparacaoDecision**
```python
"TRANSBENSPATRIMONIAIS"
```
### [G80567] Gestor Órgão Emitente aprova movimentação? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROV_EMITENTE")
```
- alternativa → [358066] Aprovar Transferência do Órgão Destino: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [358067] Reprovação de Chamado: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G80568] Gestor Órgão Destinatário aprova movimentação? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROV_DESTINO")
```
- alternativa → [358077] Reprovação de Chamado: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
- alternativa → [358076] Aguardar encerramento da conciliação para avançar : OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```

## Atividades

### [358064] Tarefa "Atualizar dados no ERP/FA"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=251; Codigo=INTEGRA_ERP; PassaTodosItens=true
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
**ScriptInicio**
```python
sql1="select log.bem, log.mensagem from XXBBTSGATE.TB_BBTS_LOG_INTEGRA_SV_ERP log WHERE log.CHAMADO ='"+OrdemServico.Numero.ToString()+"' and log.TRANSF_BEM_ID in ( select max(log2.TRANSF_BEM_ID) from XXBBTSGATE.TB_BBTS_LOG_INTEGRA_SV_ERP log2 WHERE log2.CHAMADO =log.CHAMADO group by log2.CHAMADO, log2.BEM)"
lista = DB.ExecuteDataTable(sql1)
for linha in lista.Rows:
    sql2="UPDATE Z_00143_DADOS_BEM_INV_COM_ETI set PROCESSADO = '"+linha['MENSAGEM'].ToString()+"' where id_ocorrencia ='"+OrdemServico.Id.ToString()+"' and NUM_PATRIM='"+linha['BEM'].ToString()+"'"
    DB.ExecuteNonQuery(sql2)


sql3 = "select count(1) from Z_00143_DADOS_BEM_INV_COM_ETI where (PROCESSADO != 'Bem transferido' or PROCESSADO is null) and id_ocorrencia ='"+OrdemServico.Id.ToString()+"'"
result = DB.ExecuteScalar(sql3)
if result.ToString() == '0':
    AvancaProximaAtividade=True
else:
    AvancaProximaAtividade=False
```
**ScriptFormCarregado**
```python
sql1="select log.bem, log.mensagem from XXBBTSGATE.TB_BBTS_LOG_INTEGRA_SV_ERP log WHERE log.CHAMADO ='"+OrdemServico.Numero.ToString()+"' and log.TRANSF_BEM_ID in ( select max(log2.TRANSF_BEM_ID) from XXBBTSGATE.TB_BBTS_LOG_INTEGRA_SV_ERP log2 WHERE log2.CHAMADO =log.CHAMADO group by log2.CHAMADO, log2.BEM)"
lista = DB.ExecuteDataTable(sql1)
for linha in lista.Rows:
    sql2="UPDATE Z_00143_DADOS_BEM_INV_COM_ETI set PROCESSADO = '"+linha['MENSAGEM'].ToString()+"' where id_ocorrencia ='"+OrdemServico.Id.ToString()+"' and NUM_PATRIM='"+linha['BEM'].ToString()+"'"
    DB.ExecuteNonQuery(sql2)
    #Formulario.ExibeMensagem(linha['MENSAGEM'])
```
- Operação PR0001 Preencher Campos
  - DADOS_BEM_INV_COM_ETI "Dados do Bem" [DataGrid RecordList → Z_00143_DADOS_BEM_INV_COM_ETI.DADOS_BEM_INV_COM_ETI] obrigatório
    - coluna DESCRICAO_PATRIMONIO obrigatório
    - coluna NUMERO_SERIE_PATRI
    - coluna CONDICAO_USO obrigatório
    - coluna PROCESSADO
    - coluna CATEGORIA_ATIVO obrigatório
    - coluna DISPONIBILIDADE
    - coluna CONDICAO_DE_USO
    - coluna NUM_PATRIM obrigatório
    - coluna VALOR_RESIDUAL obrigatório
    - coluna RESPONSAVEL
    - coluna LOCAL_ATIVO obrigatório
    - coluna FILIAL obrigatório
    - coluna PLANTA obrigatório
    - coluna DETALHE obrigatório
    - coluna AGENCIA obrigatório
- ValoresInputs:
  - CustomPropertyId=1697; CustomProperty=LABEL10
  - CustomPropertyId=1066; CustomProperty=LABEL2
  - CustomPropertyId=338; CustomProperty=DADOS_BEM_INV_COM_ETI
  - CustomPropertyId=3119; CustomProperty=DADOS_DO_BEM
  - CustomPropertyId=331; CustomProperty=GESTOR_PATRIMONIALEMI
  - CustomPropertyId=334; CustomProperty=GESTOR_PATRIMONIAL
  - CustomPropertyId=346; CustomProperty=MUDANCA_ESTABELECIMENTO
  - PropertyId=1223; Property=DescricaoDetalhada
  - CustomPropertyId=571; CustomProperty=SCR
  - CustomPropertyId=242; CustomProperty=SCR1
  - CustomPropertyId=1134; CustomProperty=UNIDADE_NEGOCIO
  - CustomPropertyId=1055; CustomProperty=ENDERECO_FORNECEDOR
  - CustomPropertyId=1074; CustomProperty=COMBOBOX1
  - CustomPropertyId=550; CustomProperty=FAVORECIDO_COBRA
  - CustomPropertyId=510; CustomProperty=FAVORECIDO_TODOS
  - CustomPropertyId=578; CustomProperty=SCR_TODOS_RH
  - PropertyId=1295; Property=Servico
- Associação: Ativo=true; FraseAssociacao=Transferência de Bens Patrimoniais -> Atualizar dados manualmente no ERP; FraseInversaAssociacao=Atualizar dados manualmente no ERP -> Transferência de Bens Patrimoniais; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=ATUALIZAR_DADOS_ERP; SeparadorSequencial=. | fonte: Transferência de Bens Patrimoniais → alvo: Atualizar dados manualmente no ERP

### [358065] EventoIntermediarioMensagem "Reprovação de Chamado"
Destinatário: Cliente (papel 18)
Config: Temporalidade=60
ModeloComunicado: Aviso de reprovação de chamados
Corpo do comunicado: Prezado(a) OrdemServico.Cliente.Nome ,
A Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto não foi aprovada.
 Complemento1 
Para obter mais detalhes sobre a solicitação e a reprovação, CLIQUE no link =>> Link.Consulta 
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoReprovacao("DEASDA")
```

### [358066] Tarefa "Aprovar Transferência do Órgão Destino"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=APROV_DESTINO
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovação pelo Órgão Destinatário; ReenvioEmailAprovacao=3; RotuloBotaoAprovar=Transferência concluída; RotuloBotaoReprovar=Não concluída
  - (aprovação) SCR1 "UOR do Órgão Destinatário" [DropDownList Integer → CP_ORDEM_SERVICO.SCR1]
  - (aprovação) SCR "UOR do Órgão Emitente" [DropDownList Integer → CP_ORDEM_SERVICO.SCR]
  - (aprovação) DADOS_BEM_INV_COM_ETI "Dados do Bem" [DataGrid RecordList → Z_00143_DADOS_BEM_INV_COM_ETI.DADOS_BEM_INV_COM_ETI] — PermiteModificarAprovado=true
  - (aprovação) GESTOR_PATRIMONIAL "Gestor Patrimonial do Órgão Destinatário" [DropDownList String → CP_ORDEM_SERVICO.GESTOR_PATRIMONIAL] — PermiteModificarAprovado=true
  - (aprovação) DescricaoDetalhada (nativo) "Observações"
  - (aprovação) MUDANCA_ESTABELECIMENTO "Mudança de Estabelecimento" [DropDownList String → CP_ORDEM_SERVICO.MUDANCA_ESTABELECIMENTO]
  - (aprovação) DADOS_BEM_INCLUSAO "Dados do Bem" [DataGrid RecordList → Z_00143_DADOS_BEM_INCLUSAO.DADOS_BEM_INCLUSAO] — PermiteModificarAprovado=true
  - (aprovação) GESTOR_PATRIMONIALEMI "Gestor Patrimonial do Órgão Emitente" [DropDownList String → CP_ORDEM_SERVICO.GESTOR_PATRIMONIALEMI] — PermiteModificarAprovado=true
  - item para aprovação "Nota Fiscal de Transferência"
  - aprovador: Gestor Patrimonial Órgão Destinatário (Unico)

### [358067] EventoIntermediarioMensagem "Reprovação de Chamado"
Destinatário: Cliente (papel 18)
Config: Temporalidade=60
ModeloComunicado: Aviso de reprovação de chamados
Corpo do comunicado: Prezado(a) OrdemServico.Cliente.Nome ,
A Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto não foi aprovada.
 Complemento1 
Para obter mais detalhes sobre a solicitação e a reprovação, CLIQUE no link =>> Link.Consulta 
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoReprovacao("APROV_EMITENTE")
```

### [358068] EventoIntermediarioTimer "Execução da atualização"
Config: TempoIntervalo=1; MaximoExecucao=3

### [358069] EventoFinal ""
Config: TipoFinalizacao=NaoRealizado

### [358070] EventoFinal ""
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [358071] Tarefa "Solicitar Aprovação do Gestor da UOR
"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=DEASDA
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
- Operação PR0002 Aprovar: ReenvioEmailAprovacao=24
  - (aprovação) FAVORECIDO_COBRA "Nome do Funcionário Destinatário" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
  - (aprovação) DADOS_BEM_INV_COM_ETI "Dados do Bem" [DataGrid RecordList → Z_00143_DADOS_BEM_INV_COM_ETI.DADOS_BEM_INV_COM_ETI]
  - (aprovação) SCR_TODOS_RH "UOR Movimentação" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH]
  - (aprovação) DADOS_BEM "Observações (mencionar o estado de conservação e funcionamento do bem)" [DataGrid RecordList → Z_00143_DADOS_BEM.DADOS_BEM]
  - (aprovação) FAVORECIDO_TODOS "Nome do Funcionário Emitente" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
  - aprovador: Gerente SCR_TODOS_RH (Unico)

### [358072] EventoFinal ""
Config: TipoFinalizacao=NaoRealizado

### [358073] EventoInicial "Transferência de Bens Patrimoniais"
TipoSolicitacao: 03.03. Administração e Patrimônio - Gestão de Bens
**ScriptValidacao**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
#if OrdemServico.GetCustom("SCR1") != None:
#    uor = Orgao.Carrega(Convert.ToInt32(OrdemServico.GetCustom("SCR1")))
#else:
#    uor = Orgao.Carrega(Convert.ToInt32(OrdemServico.GetCustom("SCR_TODOS_RH")))
    
scr = ""
cont = 0
if OrdemServico.GetCustom("MUDANCA_ESTABELECIMENTO")=="Sim":
    for itemOcorrencia in OrdemServico.ItensAnexados:
        if itemOcorrencia.ToString().find("Nota Fiscal de Transferência:")==0:
            cont=1
else:
    cont=1
if cont==0:
    Criticas.AdicionaPendencia('Não foi associado um(a) Nota Fiscal de Transferência')
    
idScr = OrdemServico.GetCustom("SCR")
if idScr != None:
    scr = Orgao.Carrega(idScr)
    pessoa = scr.GestorId
    if (pessoa != None):
        OrdemServico.SetCustom("GESTOR_PATRIMONIALEMI",idScr.ToString() + ' --> ' + Convert.ToString(scr.GestorId))
        nome = Pessoa.Carrega("Nome", pessoa)
        OrdemServico.SetCustom("RESPONSAVEL_MOV",nome) #Convert.ToString(scr.GestorId))
        OrdemServico.Salva
        
idScr = OrdemServico.GetCustom("SCR1")
if idScr != None:
    scr = Orgao.Carrega(idScr)
    pessoa = scr.GestorId
    if (pessoa != None):
        OrdemServico.SetCustom("GESTOR_PATRIMONIAL",idScr.ToString() + ' --> ' + Convert.ToString(scr.GestorId))
        OrdemServico.Salva
        
#Verifica se a tabela dados do bem quem item sem preencher
tabela = OrdemServico.GetCustom("DADOS_BEM_INV_COM_ETI")
nulo=0
ePatrimonio = 0
listaPatrimonio = ''
for linha in tabela.Rows:
    nf = linha["NUMERO_SERIE_PATRI"].ToString()
    descricao = linha["DESCRICAO_PATRIMONIO"].ToString()
    responsavel = linha["RESPONSAVEL"].ToString()
    categoria = linha["CATEGORIA_ATIVO"].ToString()
    valor_residual = linha["VALOR_RESIDUAL"].ToString()
    local = linha["LOCAL_ATIVO"].ToString()
    filial = linha["FILIAL"].ToString()
    planta = linha["PLANTA"].ToString()
    detalhe = linha["DETALHE"].ToString()
    agencia = linha["AGENCIA"].ToString()
    condicao = linha["CONDICAO_USO"].ToString()
    patrimonio = linha["NUM_PATRIM"].ToString()
    if String.IsNullOrEmpty(nf) or String.IsNullOrEmpty(descricao) or (String.IsNullOrEmpty(responsavel) and OrdemServico.Servico.Sigla == "TRANSFBENFUNCMSMUOR") or String.IsNullOrEmpty(categoria) or String.IsNullOrEmpty(valor_residual) or String.IsNullOrEmpty(local) or String.IsNullOrEmpty(filial) or String.IsNullOrEmpty(planta) or String.IsNullOrEmpty(detalhe) or String.IsNullOrEmpty(agencia) or String.IsNullOrEmpty(condicao) or String.IsNullOrEmpty(patrimonio):
        nulo = 1
        
    lista = Utils.ExecuteDataTable(" SELECT numero_serie FROM XXBBTSGATE.VW_BBTS_SV_FA_DADOS_DO_BEM WHERE numero_etiqueta = '"+ patrimonio.ToString() +"' ")
    if lista.Rows.Count == 0 :
        ePatrimonio = 1
        listaPatrimonio = patrimonio.ToString()+'-'+listaPatrimonio
        
    #pre_fix_conta = DB.ExecuteScalar("SELECT LPAD(conta,3,'0') pref_conta FROM XXBBTSGATE.VW_BBTS_SV_FA_DADOS_DO_BEM WHERE numero_etiqueta = '"+linha['NUM_PATRIM'].ToString()+"'")
    #pre_padrao = DB.ExecuteScalar("select ATTRIBUTE2 from xxbbtsgate.vw_bbts_ind_flex_values where FLEX_VALUE = '"+uor.Sigla.ToString()+"'")
    #
    #if pre_fix_conta.ToString()!= pre_padrao.ToString():
    #    Criticas.AdicionaPendencia("Não é possível tranferir o Patrimônio: "+linha['NUM_PATRIM'].ToString()+", devido a contra atribuida a ele não ser compativel com a Uor de destino selecionada.")
    
if nulo == 1:
    Criticas.AdicionaPendencia("A tabela 'Dados do Bem' tem itens sem informação.")
if ePatrimonio == 1:
    Criticas.AdicionaPendencia('O patrimônio '+ listaPatrimonio.ToString()+' não existe no nosso sistema!')
    
#Consulta se este patrimonio já esta em alguma OS em atendimento.
listaPatimonioDadosBemEti = OrdemServico.GetCustom("DADOS_BEM_INV_COM_ETI")

if OrdemServico.Numero == "":
    for item in listaPatimonioDadosBemEti.Rows:
        consultaOSPatrimonioDadosBemEti = DB.ExecuteDataTable("select Z_00143_DADOS_BEM_INV_COM_ETI.ID_OCORRENCIA, Z_00143_DADOS_BEM_INV_COM_ETI.NUM_PATRIM, OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.NUMERO from Z_00143_DADOS_BEM_INV_COM_ETI INNER JOIN OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = Z_00143_DADOS_BEM_INV_COM_ETI.ID_OCORRENCIA where Z_00143_DADOS_BEM_INV_COM_ETI.NUM_PATRIM = '"+item["NUM_PATRIM"].ToString()+"' and OCORRENCIA.SITUACAO = 'Aberto'")

        for patrimonio in consultaOSPatrimonioDadosBemEti.Rows:
            Criticas.AdicionaPendencia("Já existe uma solicitação aberta em atendimento para o patrimonio "+item["NUM_PATRIM"].ToString()+" - OS:"+patrimonio["NUMERO"].ToString())
```
**ScriptFormCarregado**
```python
Formulario['CAMINHO'].Habilitado = False
Formulario['CAMINHO'].Valor = 'Central de TI > Para Você > Estação de Trabalho > Requisição de Equipamento.'
Formulario["GESTOR_PATRIMONIALEMI"].Visivel = False
#Formulario["GESTOR_PATRIMONIAL"].Visivel = False
Formulario["ENDERECO_FORNECEDOR"].Visivel = False
Formulario["COMBOBOX1"].Visivel = False

if (OrdemServico.Servico.Sigla == "TRANSFBENFUNCMSMUOR"):
    Formulario["FAVORECIDO_COBRA"].Visivel = True
    Formulario["FAVORECIDO_COBRA"].Habilitado = True 
    Formulario["FAVORECIDO_TODOS"].Visivel = True
    Formulario["FAVORECIDO_TODOS"].Habilitado = True
    Formulario["SCR_TODOS_RH"].Visivel = True
    Formulario["SCR_TODOS_RH"].Habilitado = True
    Formulario["COMBOBOX1"].Visivel = False
    Formulario["COMBOBOX1"].Habilitado = False
    Formulario["ENDERECO_FORNECEDOR"].Visivel = False
    Formulario["ENDERECO_FORNECEDOR"].Habilitado = False
    Formulario["GESTOR_PATRIMONIAL"].Visivel = False
    Formulario["GESTOR_PATRIMONIAL"].Habilitado = False
    Formulario["MUDANCA_ESTABELECIMENTO"].Visivel = False
    Formulario["MUDANCA_ESTABELECIMENTO"].Habilitado = False
    Formulario["UNIDADE_NEGOCIO"].Visivel = False
    Formulario["UNIDADE_NEGOCIO"].Habilitado = False   
    

if (OrdemServico.Servico.Sigla == "TRANSBENSPATRIMONIAIS"):
    Formulario["FAVORECIDO_COBRA"].Visivel = False
    Formulario["FAVORECIDO_COBRA"].Habilitado = False 
    Formulario["FAVORECIDO_TODOS"].Visivel = False
    Formulario["FAVORECIDO_TODOS"].Habilitado = False
    Formulario["SCR_TODOS_RH"].Visivel = False
    Formulario["SCR_TODOS_RH"].Habilitado = False
    Formulario["COMBOBOX1"].Visivel = True  
    Formulario["COMBOBOX1"].Habilitado = True
    Formulario["ENDERECO_FORNECEDOR"].Visivel = True
    Formulario["ENDERECO_FORNECEDOR"].Habilitado = True
    Formulario["MUDANCA_ESTABELECIMENTO"].Visivel = True
    Formulario["MUDANCA_ESTABELECIMENTO"].Habilitado = True
    Formulario["UNIDADE_NEGOCIO"].Visivel = True
    Formulario["UNIDADE_NEGOCIO"].Habilitado = True
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Arquivos Extras (Opcionais)" classes: Arquivo 02 — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - LABEL11 "Para baixar o Arquivo para importação dos Bens Patrimoniais <a href="https://bbtecno.sharepoint.com/:x:/g/Gepes%20-%20Diret%20-%20Cesec/ESdn8jpqjPFAg00f4Scd9e0B3FSPWQxEwWRAUIB2poIwqA"> Clique aqui.</A>" [Label String(700) → CPE_PDCI2019.LABEL11] obrigatório
  - OPCAO_DE_CONFIRMACAO "Importar arquivo" [CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO] obrigatório
**OPCAO_DE_CONFIRMACAO.ScriptModificado**
```python
if Controle.Valor == True:

    if OrdemServico.PossuiItem("ARQUIVO"):
        import clr
        import System
        #import System.Data.OleDb
        clr.AddReference("System.Data")
        from System.Data import DataSet
        from System.Data.OleDb import OleDbConnection, OleDbDataAdapter, OleDbCommand

        #site de referencia para dll: https://www.microsoft.com/en-us/download/details.aspx?id=13255
        def readExcel(nomesCampos, nomeGrid):
            _olecon = None
            _oleCmd = None;
            _Consulta = None;

            repositorio = Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM");
            anexo = OrdemServico.ObtemItem("ARQUIVO");
            _Arquivo = repositorio + "\\" + anexo.Localizacao;
            _StringConexao = String.Format("Provider=Microsoft.ACE.OLEDB.12.0;Data Source={0};Extended Properties='Excel 12.0 Xml;HDR=YES;ReadOnly=False';", _Arquivo);

            conexao = OleDbConnection(_StringConexao)
            adapter = OleDbDataAdapter('select * from [TRANSFERENCIA$]', conexao);

            ds =  DataSet();

            conexao.Open();
            adapter.Fill(ds);
            for linha in ds.Tables[0].Rows:
                #OrdemServico.AdicionaLinhaRegistro(nomeGrid, nomesCampos, [linha["Etiqueta"],linha["COMENTÁRIOS (Atribuições)"]])
                
                #------------------------
                
                descricao = ""
                nf = ""
                patrimonio = linha["Etiqueta"].ToString()
                condicaoUso = linha["CONDICAO_USO"].ToString()
                lista = Utils.ExecuteDataTable(" SELECT numero_serie, descricao_bem,CATEGORIA, MATRICULA, MATRICULA ||' - '|| NOME AS RESPONSAVEL, FILIAL_PLANTA||'.'||PLANTA||'.'||DETALHE||'.'||AGENCIA AS LOCAL, FILIAL_PLANTA, PLANTA, DETALHE, AGENCIA,replace(to_char(VALOR_LIQUIDO, '999999.99'),'.',',') as VALOR_LIQUIDO FROM XXBBTSGATE.VW_BBTS_SV_FA_DADOS_DO_BEM WHERE numero_etiqueta = '"+ patrimonio.ToString() +"' ")
                if lista.Rows.Count == 0 :
                    Formulario.ExibeMensagem('Este número de patrimônio '+ patrimonio.ToString()+' não existe no nosso sistema!')
                    nf = None
                    descricao = None
                    matricula = None
                    categoria = None
                    valor_residual = None
                    local = linha["FILIAL"].ToString()+'.'+linha["PLANTA"].ToString()+'.'+linha["DETALHE"].ToString()+'.'+linha["AGENCIAS"].ToString()
                    filial = linha["FILIAL"].ToString()
                    planta = linha["PLANTA"].ToString()
                    detalhe = linha["DETALHE"].ToString()
                    agencia = linha["AGENCIAS"].ToString()
                    OrdemServico.AdicionaLinhaRegistro(nomeGrid, nomesCampos, [agencia,categoria,condicaoUso,descricao,detalhe,filial,local,patrimonio,nf,planta,matricula,valor_residual])
                    
                else:
                    for linhaBD in lista.Rows:
                        nf = linhaBD["NUMERO_SERIE"].ToString()
                        descricao = linhaBD["descricao_bem"].ToString()
                        matricula = linhaBD["MATRICULA"].ToString()
                        categoria = linhaBD["CATEGORIA"].ToString()
                        valor_residual = linhaBD["VALOR_LIQUIDO"].ToString()
                        local = linhaBD["FILIAL_PLANTA"].ToString()+'.'+linhaBD["PLANTA"].ToString()+'.'+linhaBD["DETALHE"].ToString()+'.'+linhaBD["AGENCIA"].ToString()
                        #filial = linha["FILIAL"].ToString()
                        filial = linhaBD["FILIAL_PLANTA"].ToString()
                        planta = linhaBD["PLANTA"].ToString()
                        detalhe = linhaBD["DETALHE"].ToString()
                        agencia = linhaBD["AGENCIA"].ToString()

                    OrdemServico.AdicionaLinhaRegistro(nomeGrid, nomesCampos, [agencia,categoria,condicaoUso,descricao,detalhe,filial,local,patrimonio,nf,planta,matricula,valor_residual])
                        
                    #if nf != "" and nf != None:
                    #    FormularioRegistro["NUMERO_SERIE_PATRI"].Habilitado = False
                    
                
                
                
                #-------------------------
            conexao.Close();
        readExcel(['AGENCIA','CATEGORIA_ATIVO','CONDICAO_USO','DESCRICAO_PATRIMONIO','DETALHE','FILIAL','LOCAL_ATIVO','NUM_PATRIM','NUMERO_SERIE_PATRI','PLANTA','RESPONSAVEL','VALOR_RESIDUAL'], 'DADOS_BEM_INV_COM_ETI')
    else:
        Formulario.ExibeMensagem("Não tem Arquivo anexado para importação dos bens patrimoniais.")
        Formulario["OPCAO_DE_CONFIRMACAO"].Valor = False
```
  - CAMINHO "Caminho para emissão do TRUG" [TextBox String → CPE_CSC.CAMINHO]
  - DADOS_BEM_INV_COM_ETI "Dados do Bem" [DataGrid RecordList → Z_00143_DADOS_BEM_INV_COM_ETI.DADOS_BEM_INV_COM_ETI] obrigatório
**DADOS_BEM_INV_COM_ETI.ScriptConfirmado**
```python
if (OrdemServico.Servico.Sigla == "TRANSFBENFUNCMSMUOR"):
    if ( Registro["RESPONSAVEL"] == None):
        Formulario.ExibeMensagem("O campo responsável é obrigatório")
        Cancela = True
```
    - coluna LOCAL_ATIVO obrigatório
    - coluna CONDICAO_DE_USO
    - coluna AGENCIAS obrigatório
**DADOS_BEM_INV_COM_ETI.AGENCIAS.ScriptModificado**
```python
filial=''
planta=''
detalhe=''
agencias=''

if FormularioRegistro["FILIAL"].Valor != None:
    filial=FormularioRegistro["FILIAL"].Valor.ToString()
if FormularioRegistro["PLANTA"] != None:
    planta=FormularioRegistro["PLANTA"].Valor.ToString()
if FormularioRegistro["DETALHE"].Valor != None:
    detalhe=FormularioRegistro["DETALHE"].Valor.ToString()
if FormularioRegistro["AGENCIAS"].Valor != None:
    agencias=FormularioRegistro["AGENCIAS"].Valor.ToString()

FormularioRegistro["LOCAL_DO_ATIVO"].Valor = filial+'.'+planta+'.'+detalhe+'.'+agencias
```
    - coluna NOTA_FISCAL obrigatório
    - coluna RC_COMPRAS obrigatório
    - coluna NUM_PATRIM obrigatório
**DADOS_BEM_INV_COM_ETI.NUM_PATRIM.ScriptModificado**
```python
if FormularioRegistro["NUM_PATRIM"].Valor != None and FormularioRegistro["NUM_PATRIM"].Valor != "":

    descricao = ""
    nf = ""
    patrominio = FormularioRegistro["NUM_PATRIM"].Valor
    lista = Utils.ExecuteDataTable(" SELECT numero_serie, descricao_bem,CATEGORIA, MATRICULA, MATRICULA ||' - '|| NOME AS RESPONSAVEL, FILIAL_PLANTA||'.'||PLANTA||'.'||DETALHE||'.'||AGENCIA AS LOCAL, FILIAL_PLANTA, PLANTA, DETALHE, AGENCIA,replace(to_char(VALOR_LIQUIDO, '999999.99'),'.',',') as VALOR_LIQUIDO FROM XXBBTSGATE.VW_BBTS_SV_FA_DADOS_DO_BEM WHERE numero_etiqueta = '"+ patrominio.ToString() +"' ")
    if lista.Rows.Count == 0 :
        Formulario.ExibeMensagem('Este número de patrimônio não existe no nosso sistema!')
        FormularioRegistro["DESCRICAO_PATRIMONIO"].Valor = ''
        FormularioRegistro["NUMERO_SERIE_PATRI"].Valor = None
        FormularioRegistro["RESPONSAVEL"].Valor = None
        FormularioRegistro["CATEGORIA_ATIVO"].Valor = None
        FormularioRegistro["VALOR_RESIDUAL"].Valor = None
        FormularioRegistro["LOCAL_ATIVO"].Valor = None
        FormularioRegistro["FILIAL"].Valor = None
        FormularioRegistro["PLANTA"].Valor = None
        FormularioRegistro["DETALHE"].Valor = None
        FormularioRegistro["AGENCIA"].Valor = None
        
    else:
        for linha in lista.Rows:
            nf = linha["NUMERO_SERIE"].ToString()
            descricao = linha["DESCRICAO_BEM"].ToString()
            matricula = linha["MATRICULA"].ToString()
            categoria = linha["CATEGORIA"].ToString()
            valor_residual = linha["VALOR_LIQUIDO"].ToString()
            local = linha["LOCAL"].ToString()
            filial = linha["FILIAL_PLANTA"].ToString()
            planta = linha["PLANTA"].ToString()
            detalhe = linha["DETALHE"].ToString()
            agencia = linha["AGENCIA"].ToString()

        FormularioRegistro["DESCRICAO_PATRIMONIO"].Valor = descricao
        FormularioRegistro["NUMERO_SERIE_PATRI"].Valor = nf
        FormularioRegistro["RESPONSAVEL"].Valor = matricula
        FormularioRegistro["CATEGORIA_ATIVO"].Valor = categoria
        FormularioRegistro["VALOR_RESIDUAL"].Valor = valor_residual
        FormularioRegistro["LOCAL_ATIVO"].Valor = local
        FormularioRegistro["FILIAL"].Valor = filial
        FormularioRegistro["PLANTA"].Valor = planta
        FormularioRegistro["DETALHE"].Valor = detalhe
        FormularioRegistro["AGENCIA"].Valor = agencia
        FormularioRegistro["DESCRICAO_PATRIMONIO"].Habilitado = False
            
        if nf != "" and nf != None:
            FormularioRegistro["NUMERO_SERIE_PATRI"].Habilitado = False
```
    - coluna RESPONSAVEL
    - coluna FILIAL obrigatório
**DADOS_BEM_INV_COM_ETI.FILIAL.ScriptModificado**
```python
if String.IsNullOrEmpty(FormularioRegistro["FILIAL"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["PLANTA"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["DETALHE"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["AGENCIA"].Valor)==False:
    FormularioRegistro["LOCAL_ATIVO"].Valor = FormularioRegistro["FILIAL"].Valor+'.'+FormularioRegistro["PLANTA"].Valor+'.'+FormularioRegistro["DETALHE"].Valor+'.'+FormularioRegistro["AGENCIA"].Valor
```
    - coluna LOCAL_DO_ATIVO obrigatório
    - coluna PROCESSADO
    - coluna DESCRICAO_PATRIMONIO obrigatório
    - coluna NUMERO_SERIE_PATRI
    - coluna CONDICAO_USO obrigatório
    - coluna DISPONIBILIDADE
    - coluna PATRIMONIO obrigatório
**DADOS_BEM_INV_COM_ETI.PATRIMONIO.ScriptModificado**
```python
if FormularioRegistro["PATRIMONIO"].Valor != None and FormularioRegistro["PATRIMONIO"].Valor != "":

    descricao = ""
    nf = ""
    patrominio = FormularioRegistro["PATRIMONIO"].Valor
    lista = Utils.ExecuteDataTable(" SELECT numero_serie, descricao_bem FROM XXBBTSGATE.VW_BBTS_SV_FA WHERE numero_bem = '"+ patrominio.ToString() +"' ")

    for linha in lista.Rows:
        nf = linha["NUMERO_SERIE"].ToString()
        descricao = linha["DESCRICAO_BEM"].ToString()

    FormularioRegistro["DESCRICAO_PATRIMONIO"].Valor = descricao
    FormularioRegistro["NUMERO_SERIE_PATRI"].Valor = nf
    FormularioRegistro["DESCRICAO_PATRIMONIO"].Habilitado = False
        
    if nf != "" and nf != None:
        FormularioRegistro["NUMERO_SERIE_PATRI"].Habilitado = False
```
    - coluna VALOR_RESIDUAL obrigatório
    - coluna DETALHE obrigatório
**DADOS_BEM_INV_COM_ETI.DETALHE.ScriptModificado**
```python
if String.IsNullOrEmpty(FormularioRegistro["FILIAL"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["PLANTA"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["DETALHE"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["AGENCIA"].Valor)==False:
    FormularioRegistro["LOCAL_ATIVO"].Valor = FormularioRegistro["FILIAL"].Valor+'.'+FormularioRegistro["PLANTA"].Valor+'.'+FormularioRegistro["DETALHE"].Valor+'.'+FormularioRegistro["AGENCIA"].Valoragencias
```
    - coluna AGENCIA obrigatório
**DADOS_BEM_INV_COM_ETI.AGENCIA.ScriptModificado**
```python
if String.IsNullOrEmpty(FormularioRegistro["FILIAL"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["PLANTA"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["DETALHE"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["AGENCIA"].Valor)==False:
    FormularioRegistro["LOCAL_ATIVO"].Valor = FormularioRegistro["FILIAL"].Valor+'.'+FormularioRegistro["PLANTA"].Valor+'.'+FormularioRegistro["DETALHE"].Valor+'.'+FormularioRegistro["AGENCIA"].Valor
```
    - coluna CATEGORIA_ATIVO obrigatório
    - coluna CATEGORIA_DO_ATIVO obrigatório
    - coluna PLANTA obrigatório
**DADOS_BEM_INV_COM_ETI.PLANTA.ScriptModificado**
```python
if String.IsNullOrEmpty(FormularioRegistro["FILIAL"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["PLANTA"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["DETALHE"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["AGENCIA"].Valor)==False:
    FormularioRegistro["LOCAL_ATIVO"].Valor = FormularioRegistro["FILIAL"].Valor+'.'+FormularioRegistro["PLANTA"].Valor+'.'+FormularioRegistro["DETALHE"].Valor+'.'+FormularioRegistro["AGENCIA"].Valor
```
    - coluna ETIQUETA obrigatório
  - GESTOR_PATRIMONIALEMI "Órgão Emitente" [DropDownList String → CP_ORDEM_SERVICO.GESTOR_PATRIMONIALEMI]
  - GESTOR_PATRIMONIAL "Gestor Patrimonial do Órgão Destinatário" [DropDownList String → CP_ORDEM_SERVICO.GESTOR_PATRIMONIAL] obrigatório
  - MUDANCA_ESTABELECIMENTO "Mudança de Estabelecimento" [DropDownList String → CP_ORDEM_SERVICO.MUDANCA_ESTABELECIMENTO] obrigatório
  - DescricaoDetalhada (nativo) "Observações (mencionar o estado de conservação e funcionamento do bem)" obrigatório
  - SCR "UOR de Origem" [DropDownList Integer → CP_ORDEM_SERVICO.SCR] obrigatório
  - SCR1 "UOR de Destino" [DropDownList Integer → CP_ORDEM_SERVICO.SCR1] obrigatório
**SCR1.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
#lista = Formulario['DADOS_BEM_INV_COM_ETI'].Valor
#uor = Orgao.Carrega(Convert.ToInt32(Controle.Valor))
#pre_fix_conta = 0
#pre_padrao=0
#for linha in lista.Rows:
#    pre_fix_conta = DB.ExecuteScalar("SELECT LPAD(conta,3,'0') pref_conta FROM XXBBTSGATE.VW_BBTS_SV_FA_DADOS_DO_BEM WHERE numero_etiqueta = '"+linha['NUM_PATRIM'].ToString()+"'")
#    pre_padrao = DB.ExecuteScalar("select ATTRIBUTE2 from xxbbtsgate.vw_bbts_ind_flex_values where FLEX_VALUE = '"+uor.Sigla.ToString()+"'")
#    if pre_fix_conta.ToString()!= pre_padrao.ToString():
#        Formulario.ExibeMensagem("Não é possível tranferir o Patrimônio: "+linha['NUM_PATRIM'].ToString()+", devido a contra atribuida a ele não ser compativel com a Uor de destino selecionada.")
#
```
  - UNIDADE_NEGOCIO "Unidade de Negócio" [DropDownList String → CP_ORDEM_SERVICO.UNIDADE_NEGOCIO] obrigatório
**UNIDADE_NEGOCIO.ScriptModificado**
```python
if Formulario["UNIDADE_NEGOCIO"].Valor != None:

    unidade = Formulario["UNIDADE_NEGOCIO"].Valor

    Formulario["ENDERECO_FORNECEDOR"].Valor = DB.ExecuteScalar(" SELECT ADDRESS1||', '||NUM1||', '||REPLACE(ADDRESS2 ||', ',' , ','')||ADDRESS4||' - '||CITY||' - '||STATE||' / CEP:'||POSTAL AS ENDERECO FROM PS_ESTAB_TBL WHERE EFF_STATUS='A' AND ESTABID = '"+ unidade.ToString() +"' ")

    Formulario["COMBOBOX1"].Itens = DB.ExecuteDataTable(" SELECT DISTINCT fa.location_id, fa.descricao_planta || ' - ' || fa.descricao_detalhe FROM XXBBTSGATE.VW_BBTS_SV_FA fa WHERE fa.filial_planta = '"+ unidade.ToString() +"' ")
    
    Formulario["ENDERECO_FORNECEDOR"].Visivel = True
    Formulario["COMBOBOX1"].Visivel = True

else:
    Formulario["ENDERECO_FORNECEDOR"].Visivel = False
    Formulario["ENDERECO_FORNECEDOR"].Habilitado = False
    Formulario["COMBOBOX1"].Visivel = False
```
  - ENDERECO_FORNECEDOR "Endereço" [TextBox String(300) → CP_ORDEM_SERVICO.ENDERECO_FORNECEDOR] obrigatório
  - COMBOBOX1 "Localização" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - FAVORECIDO_COBRA "Nome do Funcionário Destinatário" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - FAVORECIDO_TODOS "Nome do Funcionário Emitente" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
  - SCR_TODOS_RH "UOR dos Colaboradores" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH] obrigatório
**SCR_TODOS_RH.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
#lista = Formulario['DADOS_BEM_INV_COM_ETI'].Valor
#uor = Orgao.Carrega(Convert.ToInt32(Controle.Valor))
#pre_fix_conta = 0
#pre_padrao=0
#for linha in lista.Rows:
#    pre_fix_conta = DB.ExecuteScalar("SELECT LPAD(conta,3,'0') pref_conta FROM XXBBTSGATE.VW_BBTS_SV_FA_DADOS_DO_BEM WHERE numero_etiqueta = '"+linha['NUM_PATRIM'].ToString()+"'")
#    pre_padrao = DB.ExecuteScalar("select ATTRIBUTE2 from xxbbtsgate.vw_bbts_ind_flex_values where FLEX_VALUE = '"+uor.Sigla.ToString()+"'")
#    if pre_fix_conta.ToString()!= pre_padrao.ToString():
#        Formulario.ExibeMensagem("Não é possível tranferir o Patrimônio: "+linha['NUM_PATRIM'].ToString()+", devido a contra atribuida a ele não ser compativel com a Uor de destino selecionada.")
```
  - DADOS_DO_BEM "Dados do Bem" [DataGrid RecordList → Z_00143_DADOS_DO_BEM.DADOS_DO_BEM]
**DADOS_DO_BEM.ScriptConfirmado**
```python
if (OrdemServico.Servico.Sigla == "TRANSFBENFUNCMSMUOR"):
    if ( Registro["RESPONSAVEL"] == None):
        Formulario.ExibeMensagem("O campo responsável é obrigatório")
        Cancela = True
```
    - coluna AGENCIA obrigatório
**DADOS_DO_BEM.AGENCIA.ScriptModificado**
```python
if String.IsNullOrEmpty(FormularioRegistro["FILIAL"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["PLANTA"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["DETALHE"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["AGENCIA"].Valor)==False:
    FormularioRegistro["LOCAL_ATIVO"].Valor = FormularioRegistro["FILIAL"].Valor+'.'+FormularioRegistro["PLANTA"].Valor+'.'+FormularioRegistro["DETALHE"].Valor+'.'+FormularioRegistro["AGENCIA"].Valor
```
    - coluna FILIAL obrigatório
**DADOS_DO_BEM.FILIAL.ScriptModificado**
```python
if String.IsNullOrEmpty(FormularioRegistro["FILIAL"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["PLANTA"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["DETALHE"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["AGENCIA"].Valor)==False:
    FormularioRegistro["LOCAL_ATIVO"].Valor = FormularioRegistro["FILIAL"].Valor+'.'+FormularioRegistro["PLANTA"].Valor+'.'+FormularioRegistro["DETALHE"].Valor+'.'+FormularioRegistro["AGENCIA"].Valor
```
    - coluna NUMERO_SERIE_PATRI obrigatório
    - coluna NUM_PATRIM obrigatório
**DADOS_DO_BEM.NUM_PATRIM.ScriptModificado**
```python
if FormularioRegistro["NUM_PATRIM"].Valor != None and FormularioRegistro["NUM_PATRIM"].Valor != "":

    descricao = ""
    nf = ""
    patrominio = FormularioRegistro["NUM_PATRIM"].Valor
    lista = Utils.ExecuteDataTable(" SELECT numero_serie, descricao_bem,CATEGORIA, MATRICULA, MATRICULA ||' - '|| NOME AS RESPONSAVEL, FILIAL_PLANTA||'.'||PLANTA||'.'||DETALHE||'.'||AGENCIA AS LOCAL, FILIAL_PLANTA, PLANTA, DETALHE, AGENCIA,replace(to_char(VALOR_LIQUIDO, '999999.99'),'.',',') as VALOR_LIQUIDO FROM XXBBTSGATE.VW_BBTS_SV_FA_DADOS_DO_BEM WHERE numero_etiqueta = '"+ patrominio.ToString() +"' ")
    if lista.Rows.Count == 0 :
        Formulario.ExibeMensagem('Este número de patrimônio não existe no nosso sistema!')
        FormularioRegistro["DESCRICAO_PATRIMONIO"].Valor = ''
        FormularioRegistro["NUMERO_SERIE_PATRI"].Valor = None
        FormularioRegistro["RESPONSAVEL"].Valor = None
        FormularioRegistro["CATEGORIA_ATIVO"].Valor = None
        FormularioRegistro["VALOR_RESIDUAL"].Valor = None
        FormularioRegistro["LOCAL_ATIVO"].Valor = None
        FormularioRegistro["FILIAL"].Valor = None
        FormularioRegistro["PLANTA"].Valor = None
        FormularioRegistro["DETALHE"].Valor = None
        FormularioRegistro["AGENCIA"].Valor = None
        
    else:
        for linha in lista.Rows:
            nf = linha["NUMERO_SERIE"].ToString()
            descricao = linha["DESCRICAO_BEM"].ToString()
            matricula = linha["MATRICULA"].ToString()
            categoria = linha["CATEGORIA"].ToString()
            valor_residual = linha["VALOR_LIQUIDO"].ToString()
            local = linha["LOCAL"].ToString()
            filial = linha["FILIAL_PLANTA"].ToString()
            planta = linha["PLANTA"].ToString()
            detalhe = linha["DETALHE"].ToString()
            agencia = linha["AGENCIA"].ToString()

        FormularioRegistro["DESCRICAO_PATRIMONIO"].Valor = descricao
        FormularioRegistro["NUMERO_SERIE_PATRI"].Valor = nf
        FormularioRegistro["RESPONSAVEL"].Valor = matricula
        FormularioRegistro["CATEGORIA_ATIVO"].Valor = categoria
        FormularioRegistro["VALOR_RESIDUAL"].Valor = valor_residual
        FormularioRegistro["LOCAL_ATIVO"].Valor = local
        FormularioRegistro["FILIAL"].Valor = filial
        FormularioRegistro["PLANTA"].Valor = planta
        FormularioRegistro["DETALHE"].Valor = detalhe
        FormularioRegistro["AGENCIA"].Valor = agencia
        FormularioRegistro["DESCRICAO_PATRIMONIO"].Habilitado = False
            
        if nf != "" and nf != None:
            FormularioRegistro["NUMERO_SERIE_PATRI"].Habilitado = False
```
    - coluna PROCESSADO
    - coluna DESCRICAO_PATRIMONIO obrigatório
    - coluna CONDICAO_USO obrigatório
    - coluna RESPONSAVEL
    - coluna CATEGORIA_ATIVO obrigatório
    - coluna VALOR_RESIDUAL obrigatório
    - coluna LOCAL_ATIVO obrigatório
    - coluna DETALHE obrigatório
**DADOS_DO_BEM.DETALHE.ScriptModificado**
```python
if String.IsNullOrEmpty(FormularioRegistro["FILIAL"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["PLANTA"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["DETALHE"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["AGENCIA"].Valor)==False:
    FormularioRegistro["LOCAL_ATIVO"].Valor = FormularioRegistro["FILIAL"].Valor+'.'+FormularioRegistro["PLANTA"].Valor+'.'+FormularioRegistro["DETALHE"].Valor+'.'+FormularioRegistro["AGENCIA"].Valor
```
    - coluna PLANTA obrigatório
**DADOS_DO_BEM.PLANTA.ScriptModificado**
```python
if String.IsNullOrEmpty(FormularioRegistro["FILIAL"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["PLANTA"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["DETALHE"].Valor)==False and String.IsNullOrEmpty(FormularioRegistro["AGENCIA"].Valor)==False:
    FormularioRegistro["LOCAL_ATIVO"].Valor = FormularioRegistro["FILIAL"].Valor+'.'+FormularioRegistro["PLANTA"].Valor+'.'+FormularioRegistro["DETALHE"].Valor+'.'+FormularioRegistro["AGENCIA"].Valor
```
- Operação PR0004 Associar Itens Configuração: Nome=NOTA_FISCAL
  - anexo "Nota Fiscal de Transferência" classes: Nota Fiscal de Transferência — ProduzidoTermino=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Arquivo para importação dos Bens Patrimoniais - Utilizar a planilha de upload disponibilizada no Link. Campos obrigatórios: Etiqueta e Condições de Uso." classes: Arquivo — RequeridoInicial=true

### [358076] Tarefa "Aguardar encerramento da conciliação para avançar esta tarefa."
Responsável: Fila CSC - Bens Patrimoniais (papel 488)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno

### [358077] EventoIntermediarioMensagem "Reprovação de Chamado"
Destinatário: Cliente (papel 18)
Config: Temporalidade=60
ModeloComunicado: Aviso de reprovação de chamados
Corpo do comunicado: Prezado(a) OrdemServico.Cliente.Nome ,
A Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto não foi aprovada.
 Complemento1 
Para obter mais detalhes sobre a solicitação e a reprovação, CLIQUE no link =>> Link.Consulta 
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoReprovacao("APROV_DESTINO")
```

### [358074] Tarefa "Preencher informações"
Responsável: Fila CSC - Bens Patrimoniais (papel 488)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
#----- Seleção de dados P_MATRICULA e P_UOR
#destino = OrdemServico.GetCustom("RESPONSAVEL")
matricula = 0
uor = ""

idScr = OrdemServico.GetCustom("SCR1")
if idScr != None:
    scr = Orgao.Carrega(idScr)
    pessoa = scr.GestorId
    destino = Convert.ToString(scr.GestorId)



lista = Utils.ExecuteDataTable(" SELECT distinct cpp.matricula, org.sigla FROM cp_pessoa cpp inner join orgao org on cpp.id_pessoa = org.id_gestor where cpp.id_pessoa = "+ destino +" ")

for linha in lista.Rows:
    matricula = linha["MATRICULA"]
    uor = linha["SIGLA"]

OrdemServico.SetCustom("MATRICULA", matricula)
OrdemServico.SetCustom("SIGLA_SCR", uor)


AvancaProximaAtividade = True
```

### [358075] Tarefa "Aprovar transferência do Órgão Emitente"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=APROV_EMITENTE
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovação pelo Órgão Emitente; UtilizaIdentidadeSolicitante=true; ReenvioEmailAprovacao=24
  - (aprovação) SCR1 "UOR do Órgão Destinatário" [DropDownList Integer → CP_ORDEM_SERVICO.SCR1]
  - (aprovação) GESTOR_PATRIMONIAL "Gestor Patrimonial do Órgão Destinatário" [DropDownList String → CP_ORDEM_SERVICO.GESTOR_PATRIMONIAL] — PermiteModificarAprovado=true
  - (aprovação) GESTOR_PATRIMONIALEMI "Gestor Patrimonial do Órgão Emitente" [DropDownList String → CP_ORDEM_SERVICO.GESTOR_PATRIMONIALEMI] — PermiteModificarAprovado=true
  - (aprovação) DADOS_BEM_INCLUSAO "Dados do Bem" [DataGrid RecordList → Z_00143_DADOS_BEM_INCLUSAO.DADOS_BEM_INCLUSAO] — PermiteModificarAprovado=true
  - (aprovação) DADOS_BEM_INV_COM_ETI "Dados do Bem" [DataGrid RecordList → Z_00143_DADOS_BEM_INV_COM_ETI.DADOS_BEM_INV_COM_ETI] — PermiteModificarAprovado=true
  - (aprovação) MUDANCA_ESTABELECIMENTO "Mudança de Estabelecimento" [DropDownList String → CP_ORDEM_SERVICO.MUDANCA_ESTABELECIMENTO]
  - (aprovação) SCR "UOR do Órgão Emitente" [DropDownList Integer → CP_ORDEM_SERVICO.SCR]
  - (aprovação) DescricaoDetalhada (nativo) "Observações" — PermiteModificarAprovado=true
  - item para aprovação "Nota Fiscal de Transferência"
  - aprovador: Gestor Patrimonial Órgão Emitente (Unico)

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
### papel 179: Gestor Patrimonial Órgão Destinatário
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
#s = OrdemServico.GetCustom("GESTOR_PATRIMONIAL").ToString()
#idPessoa = Convert.ToString(s[s.find("-->")+4:len(s)]) 
#Utils.LogError(idPessoa, "erro")
#pessoa = Pessoa.Carrega(Convert.ToInt32(idPessoa));
#Utils.LogInformation(pessoa.Nome, "log")
#if (pessoa != None):
#    Atores.Adiciona(pessoa, "Gestor Selecionado");

idScr = Convert.ToInt32(OrdemServico.GetCustom("SCR1"))

scr = Orgao.Carrega(idScr)
if (scr != None):
    pessoa = scr.Gestor
    if (pessoa != None):
        Atores.Adiciona(pessoa)
#else:
#    Atores.Adiciona(OrdemServico.Cliente)
```
### papel 584: Gerente SCR_TODOS_RH
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Processo.Custom import Ator
id = DB.ExecuteScalar("select id_orgao from orgao where sigla = '"+ OrdemServico["SCR_TODOS_RH"].ToString() +"'")

idScr = Convert.ToInt32(id)
scr = Orgao.Carrega(idScr)
if (scr != None):
    pessoa = scr.Gestor
    if (pessoa != None):
        Atores.Adiciona(pessoa)
```
### papel 488: Fila CSC - Bens Patrimoniais
Tipo=RelacaoPessoas | pessoas: Fila CSC - Bens Patrimoniais
### papel 172: Gestor Patrimonial Órgão Emitente
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
#s = OrdemServico.GetCustom("GESTOR_PATRIMONIALEMI").ToString()
#idPessoa = Convert.ToString(s[s.find("-->")+4:len(s)])
#Utils.LogError(idPessoa, "erro")
#pessoa = Pessoa.Carrega(Convert.ToInt32(idPessoa));
#Utils.LogInformation(pessoa.Nome, "log")
#if (pessoa != None):
#    Atores.Adiciona(pessoa, "Gestor Selecionado");

idScr = Convert.ToInt32(OrdemServico.GetCustom("SCR"))

scr = Orgao.Carrega(idScr)
if (scr != None):
    pessoa = scr.Gestor
    if (pessoa != None):
        Atores.Adiciona(pessoa)
```

## Campos customizados usados (definição global)

### DADOS_BEM_INV_COM_ETI — Dados do Bem
DataGrid RecordList → Z_00143_DADOS_BEM_INV_COM_ETI.DADOS_BEM_INV_COM_ETI
Colunas do registro:
- DESCRICAO_PATRIMONIO "Descrição" [TextBox String]
- NUMERO_SERIE_PATRI "Número de Série" [TextBox String]
- CONDICAO_USO "Estado do Equipamento" [DropDownList String] itens:  ;Material Ocioso;Material Antieconômico;Material Recuperável;Material Irrecuperável;Material Produtivo
- NUM_PATRIM "Número de Patrimônio" [TextBox String]
- CATEGORIA_ATIVO "Categoria do Ativo" [TextBox String]
- VALOR_RESIDUAL "Valor Residual" [TextBox String]
- RESPONSAVEL "Responsável" [DropDownList String]
**RESPONSAVEL.LookupScript**
```python
Itens = Utils.ExecuteDataTable("select matricula as id, matricula||' - '|| nome as descricao from cad_funcionario_v order by nome, matricula")
```
- LOCAL_ATIVO "Local do Ativo" [TextBox String]
- FILIAL "Local - Filial" [TextBox String]
- PLANTA "Local -  Planta" [TextBox String]
- DETALHE "Local - Detalhe" [TextBox String]
- AGENCIA "Local - Agência" [TextBox String]
- PROCESSADO "Processado" [TextBox String]

### SCR1 — Novo SCR
DropDownList Integer → CP_ORDEM_SERVICO.SCR1

### SCR — UOR
DropDownList Integer → CP_ORDEM_SERVICO.SCR
Descrição: SCR

### GESTOR_PATRIMONIAL — Gestor Patrimonial do Órgão Destinatário
DropDownList String → CP_ORDEM_SERVICO.GESTOR_PATRIMONIAL
**LookupScript**
```python
Itens = DB.ExecuteDataTable("select orgao.id_orgao || ' --> ' || pessoa.id_pessoa as id, orgao.descricao || ' --> ' || pessoa.nome as gestor_patrimonial from orgao, pessoa where (orgao.id_gestor = pessoa.id_pessoa) order by orgao.descricao")
```

### MUDANCA_ESTABELECIMENTO — Mudança de Estabelecimento
DropDownList String → CP_ORDEM_SERVICO.MUDANCA_ESTABELECIMENTO
Itens: Sim;Não

### DADOS_BEM_INCLUSAO — Dados do Bem
DataGrid RecordList → Z_00143_DADOS_BEM_INCLUSAO.DADOS_BEM_INCLUSAO
Colunas do registro:
- DESCRICAO_PATRIMONIO "Descrição" [TextBox String]
- NUMERO_SERIE_PATRI "Número de Série" [TextBox String]
- CONDICAO_USO "Condição de Uso" [DropDownList String] itens:  ;Material Ocioso;Material Antieconômico;Material Recuperável;Material Irrecuperável;Material Produtivo
- RC_COMPRAS "Num. Requisição de Compras" [TextBox String]
- NOTA_FISCAL "Número Nota Fiscal" [TextBox String]
- PATRIMONIO "Núm. de Patrimônio" [TextBox String]

### GESTOR_PATRIMONIALEMI — Gestor Patrimonial do Órgão Emitente
DropDownList String → CP_ORDEM_SERVICO.GESTOR_PATRIMONIALEMI
**LookupScript**
```python
Itens = DB.ExecuteDataTable("select orgao.id_orgao || ' --> ' || pessoa.id_pessoa as id, orgao.descricao || ' --> ' || pessoa.nome as gestor_patrimonial from orgao, pessoa where (orgao.id_gestor = pessoa.id_pessoa) order by orgao.descricao")
```

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### SCR_TODOS_RH — UOR Movimentação
DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH
Descrição: SCR Movimentação
**LookupScript**
```python
###PGESV###
Itens = DB.ExecuteDataTable("SELECT to_char(SCR) as SCR, NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO");
```

### DADOS_BEM — Dados do Bem
DataGrid RecordList → Z_00143_DADOS_BEM.DADOS_BEM
Colunas do registro:
- NUMERO_PATRIMONIO "N° Patrimônio" [TextBox Integer]
- NUMERO_SERIE_PATRI "Número de Série" [TextBox Integer]
- DESCRICAO_PATRIMONIO "Descrição" [TextBox String]
- CONDICAO_USO "Condição de Uso" [DropDownList String] itens:  ;Material Ocioso;Material Antieconômico;Material Recuperável;Material Irrecuperável;Material Produtivo

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### LABEL11 — LABEL11
Label String(700) → CPE_PDCI2019.LABEL11

### OPCAO_DE_CONFIRMACAO — Campo confirma uma afirmação
CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO
Descrição: Campo genérico para confirmação de uma afirmação

### CAMINHO — CAMINHO
TextBox String → CPE_CSC.CAMINHO

### UNIDADE_NEGOCIO — Unidade de Negócio
DropDownList String → CP_ORDEM_SERVICO.UNIDADE_NEGOCIO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT TO_CHAR(E.ESTABID) AS ID, E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE)")

#ValorCorrente = "SELECT DISTINCT E.ESTABID, E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE)"

#sqlValor = "SELECT DISTINCT E.ESTABID, E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE) AND E.ESTABID = "+ValorCorrente
# 
#sqlEntrada = "SELECT DISTINCT E.ESTABID, E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE) AND UPPER(E.DESCR) like UPPER('%"+EntradaUsuario+"%')"
#
#sqlOrder = " order by DESCR asc"
# 
#if not String.IsNullOrEmpty(ValorCorrente) and not String.IsNullOrEmpty(EntradaUsuario):
#
#   Itens = DB.ExecuteDataTable("(" + sqlValor + ") UNION (" + sqlEntrada + " ) " + sqlOrder)
# 
#elif String.IsNullOrEmpty(EntradaUsuario) and String.IsNullOrEmpty(ValorCorrente):
# 
#   Itens = DB.ExecuteDataTable( sqlEntrada + sqlOrder)
#   #None
# 
#elif String.IsNullOrEmpty(EntradaUsuario):
#   
#   Itens = DB.ExecuteDataTable( sqlValor + sqlOrder)
# 
#else:
#   
#   Itens = DB.ExecuteDataTable( sqlEntrada + sqlOrder)
```

### ENDERECO_FORNECEDOR — Endereço
TextBox String(300) → CP_ORDEM_SERVICO.ENDERECO_FORNECEDOR

### COMBOBOX1 — Chamado Aberto?
DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1

### DADOS_DO_BEM — Dados do Bem
DataGrid RecordList → Z_00143_DADOS_DO_BEM.DADOS_DO_BEM
Colunas do registro:
- VALOR_RESIDUAL "Valor Residual" [TextBox String]
- LOCAL_ATIVO "Local do Ativo" [TextBox String]
- RESPONSAVEL "Responsável" [DropDownList String]
**RESPONSAVEL.LookupScript**
```python
Itens = Utils.ExecuteDataTable("select matricula as id, matricula||' - '|| nome as descricao from cad_funcionario_v order by nome, matricula")
```
- FILIAL "Local - Filial" [TextBox String]
- PLANTA "Local -  Planta" [TextBox String]
- DETALHE "Local - Detalhe" [TextBox String]
- AGENCIA "Local - Agência" [TextBox String]
- PROCESSADO "Processado" [TextBox String]
- NUM_PATRIM "Número de Patrimônio" [TextBox String]
- DESCRICAO_PATRIMONIO "Descrição" [TextBox String]
- NUMERO_SERIE_PATRI "Número de Série" [TextBox String]
- CONDICAO_USO "Estado do Equipamento" [DropDownList String] itens:  ;Material Ocioso;Material Antieconômico;Material Recuperável;Material Irrecuperável;Material Produtivo
- CATEGORIA_ATIVO "Categoria do Ativo" [TextBox String]

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
