# Fluxo: Precificação e Orçamento (PREORC) — versão 10
Caminho: Fluxos > Gestão de Custos Versão 10 Precificação e Orçamento
XML: `XMLs para teste/Gestão_de_Custos_Versão_10_Precificação_e_Orçamento.xml` | Supravizio 19.1.1 | SubProcessoId 20807 | DesenhoProcessoId 2922 | ProcessoId 76
Órgão dono: 3000009350 - DIVISAO DE PRECIFICAO E AVALIACAO DE NEGOCIOS | Responsável: PRISCILA SARAIVA VALENTIM BUARQUE
Classe do subprocesso: Objetivo=Precificação e Orçamento; DescricaoCliente=Precificação e Orçamento; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadoresGrupoEnvolvido; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Precificação e Orçamento (PRECORC)

## Grafo do fluxo
- [331432] Tarefa "Validar Planilha Rascunho" {Precificação} → [G75337] Precificação é Válida?
- [331433] Tarefa "Revisão de Modelagem" {Cliente} → [331419] Definir Cronograma da Precificação
- [331421] Tarefa "Preencher Planilha Rascunho de Preços" {Precificação} → [331424] Aviso de Encaminhamento de chamado
- [331422] Tarefa "Analisar Modelagem" {Precificação} → [G75336] Modelagem Suficiente ?
- [331423] EventoIntermediarioMensagem "Aviso de Encaminhamento de chamado" → [331422] Analisar Modelagem
- [331424] EventoIntermediarioMensagem "Aviso de Encaminhamento de chamado" → [331432] Validar Planilha Rascunho
- [331425] EventoIntermediarioMensagem "Aviso de Encaminhamento de chamado" → [331421] Preencher Planilha Rascunho de Preços
- [331426] EventoIntermediarioMensagem "Aviso de Encaminhamento de chamado" → [331427] Anexar Planilha de Preços (Versão Final)
- [331427] Tarefa "Anexar Planilha de Preços (Versão Final)" {Precificação} → [331708] Aviso de Encerramento de chamado
- [331428] EventoIntermediarioMensagem "Aviso de Encaminhamento de chamado" → [331419] Definir Cronograma da Precificação
- [331429] EventoInicial "Precificação e Orçamento" {Cliente} → [331428] Aviso de Encaminhamento de chamado
- [331419] Tarefa "Definir Cronograma da Precificação" {Precificação - Coordenadores} → [331423] Aviso de Encaminhamento de chamado
- [331420] EventoFinal "" {Precificação} → (fim)
- [331708] EventoIntermediarioMensagem "Aviso de Encerramento de chamado" → [331420] 
- [331729] LinkInicial "" {Precificação - Coordenadores} → [331428] Aviso de Encaminhamento de chamado
- [331730] LinkInicial "Contratação Unificada" {Precificação - Coordenadores} → [331428] Aviso de Encaminhamento de chamado
- [G75336] Gateway "Modelagem Suficiente ?" → «Sim» [331421] Preencher Planilha Rascunho de Preços | «Não» [331433] Revisão de Modelagem
- [G75337] Gateway "Precificação é Válida?" → «Não» [331425] Aviso de Encaminhamento de chamado | «Sim» [331426] Aviso de Encaminhamento de chamado

## Gateways
### [G75336] Modelagem Suficiente ? (EventBasedExclusiveDecision)
Codigo=PO_GW_DOCUMENTACAO
- alternativa → [331421] Preencher Planilha Rascunho de Preços: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
- alternativa → [331433] Revisão de Modelagem: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
### [G75337] Precificação é Válida? (EventBasedExclusiveDecision)
Codigo=PO_GW_GRATIFICACAO
- alternativa → [331425] Aviso de Encaminhamento de chamado: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0; MotivoObrigatorio=true
- alternativa → [331426] Aviso de Encaminhamento de chamado: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1

## Atividades

### [331432] Tarefa "Validar Planilha Rascunho"
Responsável: Precificação (papel 394)
Config: Codigo=PO_VALIDAR
**ScriptInicio**
```python
import PrecifObtemCronogramaAtividade
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

# responsável pela atividade
if (OrdemServico.Atividade.Codigo != None):
    cronograma = PrecifObtemCronogramaAtividade(OrdemServico.Id, OrdemServico.Atividade.Codigo)

if cronograma != None:
    OrdemServico.ResponsavelId = Convert.ToInt32(cronograma["RESPONSAVEL_ATIVIDADE"])
    OrdemServico.Salva()
```
**ScriptFormCarregado**
```python
import PrecifObtemCronogramaAtividade
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

if (OrdemServico.Atividade.Codigo != None):
    cronograma = PrecifObtemCronogramaAtividade(OrdemServico.Id, OrdemServico.Atividade.Codigo)

if (DBNull.Value.Equals(cronograma["DATA_INICIO_ATIVIDADE"]) != True ):
    Formulario["DATA_ATIVIDADE"].Valor = cronograma["DATA_INICIO_ATIVIDADE"]
    Formulario["DATA_ATIVIDADE"].Habilitado = False

if (DBNull.Value.Equals(cronograma["DATA_INICIO_ATIVIDADE"]) != True ):
    Formulario["DATA_VENCIMENTO"].Valor = cronograma["DATA_FIM_ATIVIDADE"]
    Formulario["DATA_VENCIMENTO"].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - DATA_ATIVIDADE "Data início programada para atividade" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ATIVIDADE]
  - DATA_VENCIMENTO "Data fim programada para atividade" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO]

### [331433] Tarefa "Revisão de Modelagem"
Responsável: Cliente (papel 18)
Config: Codigo=PO_REV
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
- Operação PR0004 Associar Itens Configuração
  - anexo "Consolidação Técnica" classes: Consolidação Técnica — RequeridoInicial=true; PermiteMultiplosItens=true; IncluirPaginaAssinatura=true
  - anexo "Outros Documentos" classes: Arquivo — PermiteMultiplosItens=true; IncluirPaginaAssinatura=true

### [331421] Tarefa "Preencher Planilha Rascunho de Preços"
Responsável: Precificação (papel 394)
Config: Codigo=PO_RASCUNHO
**ScriptInicio**
```python
import PrecifObtemCronogramaAtividade
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

# responsável pela atividade
if (OrdemServico.Atividade.Codigo != None):
    cronograma = PrecifObtemCronogramaAtividade(OrdemServico.Id, OrdemServico.Atividade.Codigo)
    
if cronograma != None:
    OrdemServico.ResponsavelId = Convert.ToInt32(cronograma["RESPONSAVEL_ATIVIDADE"])
    OrdemServico.Salva()
```
**ScriptFormCarregado**
```python
import PrecifObtemCronogramaAtividade
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

if (OrdemServico.Atividade.Codigo != None):
    cronograma = PrecifObtemCronogramaAtividade(OrdemServico.Id, OrdemServico.Atividade.Codigo)

if (DBNull.Value.Equals(cronograma["DATA_INICIO_ATIVIDADE"]) != True ):
    Formulario["DATA_ATIVIDADE"].Valor = cronograma["DATA_INICIO_ATIVIDADE"]
    Formulario["DATA_ATIVIDADE"].Habilitado = False
    
if (DBNull.Value.Equals(cronograma["DATA_FIM_ATIVIDADE"]) != True ):
    Formulario["DATA_VENCIMENTO"].Valor = cronograma["DATA_FIM_ATIVIDADE"]
    Formulario["DATA_VENCIMENTO"].Habilitado = False
```
- Operação PR0004 Associar Itens Configuração: Nome=PLANILHA_RASCUNHO
  - anexo "Planilha Rascunho de Preço" classes: Planilha Rascunho de Preço — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos
  - DATA_ATIVIDADE "Data início programada para atividade" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ATIVIDADE]
  - DATA_VENCIMENTO "Data fim programada para atividade" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO]

### [331422] Tarefa "Analisar Modelagem"
Responsável: Precificação (papel 394)
Config: Codigo=PO_ANALISAR; PermissaoRestritaPapel=true
**ScriptInicio**
```python
import PrecifObtemCronogramaAtividade
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

#responsável pela atividade
cronograma = PrecifObtemCronogramaAtividade(OrdemServico.Id, OrdemServico.Atividade.Codigo)
if cronograma != None:
    OrdemServico.ResponsavelId = Convert.ToInt32(cronograma["RESPONSAVEL_ATIVIDADE"])
    OrdemServico.Salva()
```
**ScriptFormCarregado**
```python
import PrecifObtemCronogramaAtividade
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

cronograma = PrecifObtemCronogramaAtividade(OrdemServico.Id, OrdemServico.Atividade.Codigo)

if (DBNull.Value.Equals(cronograma["DATA_INICIO_ATIVIDADE"]) != True ):
    Formulario["DATA_ATIVIDADE"].Valor = Convert.ToDateTime(cronograma["DATA_INICIO_ATIVIDADE"])
    Formulario["DATA_ATIVIDADE"].Habilitado = False
    
if (DBNull.Value.Equals(cronograma["DATA_FIM_ATIVIDADE"]) != True ):
    Formulario["DATA_VENCIMENTO"].Valor = cronograma["DATA_FIM_ATIVIDADE"].ToString()
    Formulario["DATA_VENCIMENTO"].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - DATA_ATIVIDADE "Data início programada para atividade" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ATIVIDADE]
  - DATA_VENCIMENTO "Data fim programada para atividade" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO]

### [331423] EventoIntermediarioMensagem "Aviso de Encaminhamento de chamado"
Destinatário: Precificação (papel 394)
Config: Codigo=PO_AVISO_ANALISAR; EnviaMensagemIndividual=true
ModeloComunicado: Aviso sobre encaminhamento
Corpo do comunicado: OrdemServico.Cliente.Nome,
Foi encaminhado o chamado interno OrdemServico.Numero - OrdemServico.Assunto.
Acesse a aplicação Supravizio e consulte a solicitação via tela Workspace.
Atenciosamente, 
Central de Serviços

### [331424] EventoIntermediarioMensagem "Aviso de Encaminhamento de chamado"
Destinatário: Precificação (papel 394)
Config: Codigo=PO_AVISO_VALIDAR
ModeloComunicado: Aviso sobre encaminhamento
Corpo do comunicado: OrdemServico.Cliente.Nome,
Foi encaminhado o chamado interno OrdemServico.Numero - OrdemServico.Assunto.
Acesse a aplicação Supravizio e consulte a solicitação via tela Workspace.
Atenciosamente, 
Central de Serviços

### [331425] EventoIntermediarioMensagem "Aviso de Encaminhamento de chamado"
Destinatário: Precificação (papel 394)
Config: Codigo=PO_AVISO_RASCUNHO; EnviaMensagemIndividual=true
ModeloComunicado: Aviso sobre encaminhamento
Corpo do comunicado: OrdemServico.Cliente.Nome,
Foi encaminhado o chamado interno OrdemServico.Numero - OrdemServico.Assunto.
Acesse a aplicação Supravizio e consulte a solicitação via tela Workspace.
Atenciosamente, 
Central de Serviços

### [331426] EventoIntermediarioMensagem "Aviso de Encaminhamento de chamado"
Destinatário: Precificação (papel 394)
Config: Codigo=PO_AVISO_PREENCHER; EnviaMensagemIndividual=true
ModeloComunicado: Aviso sobre encaminhamento
Corpo do comunicado: OrdemServico.Cliente.Nome,
Foi encaminhado o chamado interno OrdemServico.Numero - OrdemServico.Assunto.
Acesse a aplicação Supravizio e consulte a solicitação via tela Workspace.
Atenciosamente, 
Central de Serviços

### [331427] Tarefa "Anexar Planilha de Preços (Versão Final)"
Responsável: Precificação (papel 394)
Config: Codigo=PO_PLANILHA
**ScriptInicio**
```python
import PrecifObtemCronogramaAtividade
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

# responsável pela atividade
if (OrdemServico.Atividade.Codigo != None):
    cronograma = PrecifObtemCronogramaAtividade(OrdemServico.Id, OrdemServico.Atividade.Codigo)

if cronograma != None:
    OrdemServico.ResponsavelId = Convert.ToInt32(cronograma["RESPONSAVEL_ATIVIDADE"])
    OrdemServico.Salva()
```
**ScriptFormCarregado**
```python
import PrecifObtemCronogramaAtividade
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

if (OrdemServico.Atividade.Codigo != None):
    cronograma = PrecifObtemCronogramaAtividade(OrdemServico.Id, OrdemServico.Atividade.Codigo)
    
if (DBNull.Value.Equals(cronograma["DATA_INICIO_ATIVIDADE"]) != True ):
    Formulario["DATA_ATIVIDADE"].Valor = cronograma["DATA_INICIO_ATIVIDADE"]
    Formulario["DATA_ATIVIDADE"].Habilitado = False

if (DBNull.Value.Equals(cronograma["DATA_FIM_ATIVIDADE"]) != True ):
    Formulario["DATA_VENCIMENTO"].Valor = cronograma["DATA_FIM_ATIVIDADE"]
    Formulario["DATA_VENCIMENTO"].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - DATA_ATIVIDADE "Data início programada" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ATIVIDADE]
  - DATA_VENCIMENTO "Data fim programada" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO]
- Operação PR0004 Associar Itens Configuração: Nome=PLANILHA_VALIDADA
  - anexo "Planilha de Preço (versão final)" classes: Planilha de preço (versão final) — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [331428] EventoIntermediarioMensagem "Aviso de Encaminhamento de chamado"
Config: Codigo=PO_AVISO_COORD; ListaDestinatarios=aluis.souza@bbts.com.br;dipav@bbts.com.br
ModeloComunicado: Aviso sobre encaminhamento
Corpo do comunicado: OrdemServico.Cliente.Nome,
Foi encaminhado o chamado interno OrdemServico.Numero - OrdemServico.Assunto.
Acesse a aplicação Supravizio e consulte a solicitação via tela Workspace.
Atenciosamente, 
Central de Serviços

### [331429] EventoInicial "Precificação e Orçamento"
Responsável: Cliente (papel 18)
Config: Codigo=PO_INI_MANUAL
TipoSolicitacao: Precificação e Orçamento
- Operação PR0004 Associar Itens Configuração
  - anexo "Outros Documentos" classes: Arquivo — PermiteMultiplosItens=true; IncluirPaginaAssinatura=true
  - anexo "Consolidação Técnica" classes: Consolidação Técnica — RequeridoInicial=true; PermiteMultiplosItens=true; IncluirPaginaAssinatura=true

### [331419] Tarefa "Definir Cronograma da Precificação"
Responsável: Precificação - Coordenadores (papel 395)
Config: Codigo=PO_CRONO; UnidadeANO=Minutos; ConfirmaResponsabilidade=true; PermiteCancelamentoAA=true
**ScriptInicio**
```python
qry = "SELECT count(*) as qtd FROM Z_00143_PRECIF_CRONOGRAMA WHERE ID_OCORRENCIA  = " + OrdemServico.Id.ToString()
lista = DB.ExecuteDataTable(qry)
for linha in lista.Rows:
    if linha["QTD"] == 0:
        qry  = "INSERT ALL "
        qry += "INTO Z_00143_PRECIF_CRONOGRAMA (CODIGO_ATIVIDADE, SEQUENCIA, ID_OCORRENCIA) VALUES ('PO_ANALISAR', 1," + OrdemServico.Id.ToString() + ") "
        qry += "INTO Z_00143_PRECIF_CRONOGRAMA (CODIGO_ATIVIDADE, SEQUENCIA, ID_OCORRENCIA) VALUES ('PO_RASCUNHO', 2," + OrdemServico.Id.ToString() + ") "
        qry += "INTO Z_00143_PRECIF_CRONOGRAMA (CODIGO_ATIVIDADE, SEQUENCIA, ID_OCORRENCIA) VALUES ('PO_VALIDAR', 3," +  OrdemServico.Id.ToString() + ") "
        qry += "INTO Z_00143_PRECIF_CRONOGRAMA (CODIGO_ATIVIDADE, SEQUENCIA, ID_OCORRENCIA) VALUES ('PO_PLANILHA', 4," +  OrdemServico.Id.ToString() + ") "
        qry += "SELECT * FROM dual"

        DB.ExecuteNonQuery(qry)
```
**ScriptValidacao**
```python
from Venki.Supravizio.Processo.Custom import Atividade
#if OrdemServico.Atividade.Codigo == 'PO_CRONO':
responsavelPreencher = None 
responsavelValidar = None 

lista = OrdemServico.GetCustom("PRECIF_CRONOGRAMA")
if lista != None and lista.Rows.Count > 0 :
    totalDias = 0
    lista = OrdemServico.GetCustom("PRECIF_CRONOGRAMA")
    dtFimAnt = None
    falhou = False
    if OrdemServico.GetCustom("PRECIF_DATA_INICIO") != None and OrdemServico.GetCustom("PRECIF_DATA_FIM") != None:
        if Convert.ToDateTime(OrdemServico.GetCustom("PRECIF_DATA_FIM")) < Convert.ToDateTime(OrdemServico.GetCustom("PRECIF_DATA_INICIO")):
            falhou = True
            Criticas.AdicionaPendencia("Data Fim (" + OrdemServico.GetCustom("PRECIF_DATA_INICIO").Date.ToString() + ") da Precificação não pode ser MENOR que data Início da Precificação (" + OrdemServico.GetCustom("PRECIF_DATA_FIM").Date.ToString() + ").")
        if falhou == False:
            for linha in lista.Rows:
                if falhou == False:
                    if DBNull.Value.Equals(linha["DATA_INICIO_ATIVIDADE"]) == True:
                        falhou = True
                    else:
                        if  Convert.ToDateTime(linha["DATA_INICIO_ATIVIDADE"]) < Convert.ToDateTime(OrdemServico.GetCustom("PRECIF_DATA_INICIO")):
                            falhou = True
                            Criticas.AdicionaPendencia("Data Início (" + linha["DATA_INICIO_ATIVIDADE"].Date.ToString() + "), no 'Cronograma', não pode ser MENOR que data 'Início da Precificação'(" + OrdemServico.GetCustom("PRECIF_DATA_INICIO").Date.ToString() + ") no 'Formulário'.")
                        else:
                            if Convert.ToDateTime(linha["DATA_INICIO_ATIVIDADE"]) > Convert.ToDateTime(OrdemServico.GetCustom("PRECIF_DATA_FIM")):
                                falhou = True
                                Criticas.AdicionaPendencia("Data Início (" + linha["DATA_INICIO_ATIVIDADE"].Date.ToString() + ") no 'Cronograma' não pode ser MAIOR que 'Fim da Precificação'(" + OrdemServico.GetCustom("PRECIF_DATA_FIM").Date.ToString() + ") no 'Formulário'.")
                        
                if falhou == False :
                    if DBNull.Value.Equals(linha["DATA_FIM_ATIVIDADE"].Date.ToString()) == True:
                        falhou = False
                    else:
                        if Convert.ToDateTime(linha["DATA_FIM_ATIVIDADE"]) < Convert.ToDateTime(OrdemServico.GetCustom("PRECIF_DATA_INICIO")):
                            falhou = True
                            Criticas.AdicionaPendencia("Data Fim (" + linha["DATA_FIM_ATIVIDADE"].Date.ToString() + "), no 'Cronograma', não pode ser MENOR que Data 'Início' (" + OrdemServico.GetCustom("PRECIF_DATA_INICIO").Date.ToString() + ") no 'Formulario'.")
                        else:
                            if Convert.ToDateTime(linha["DATA_FIM_ATIVIDADE"]) > Convert.ToDateTime(OrdemServico.GetCustom("PRECIF_DATA_FIM")):
                                falhou = True
                                Criticas.AdicionaPendencia("Data Fim (" + linha["DATA_FIM_ATIVIDADE"].Date.ToString() + "), no 'Cronograma', não pode ser MAIOR que 'Fim da Precificação'(" + OrdemServico.GetCustom("PRECIF_DATA_FIM").Date.ToString() + ") no 'Formulario'.")
            
#                if falhou == False:
#                    if linha["DIAS_ATIVIDADE"] <= 0:
#                        falhou = True
#                        Criticas.AdicionaPendencia("Dias da Atividade (" + linha["DIAS_ATIVIDADE"].ToString() + "), no 'Cronograma', deve ser MAIOR que Zero.")
#                    else:
#                        totalDias = totalDias + Convert.ToInt32(linha["DIAS_ATIVIDADE"])                        

                if falhou == False :
                    if  dtFimAnt == None and linha["DATA_INICIO_ATIVIDADE"].Date <= dtFimAnt:
                        falhou = True
                        Criticas.AdicionaPendencia("Revise datas do Cronograma. Data Início (" + linha["DATA_INICIO_ATIVIDADE"].Date.ToString() + ") tem que ser MAIOR que a Data Fim (" + dtFimAnt.ToString() + ") da atividade anterior.")
                    else:
                        dtFimAnt = linha["DATA_FIM_ATIVIDADE"].Date
                    
                if falhou == False:
                    if linha["CODIGO_ATIVIDADE"] == "PO_RASCUNHO":
                        responsavelPreencher = linha["RESPONSAVEL_ATIVIDADE"]
                        #Criticas.AdicionaPendencia("Preencher: " + responsavelPreencher.ToString())
                    if linha["CODIGO_ATIVIDADE"] == "PO_VALIDAR":
                        responsavelValidar = linha["RESPONSAVEL_ATIVIDADE"]
                        #Criticas.AdicionaPendencia("Validar: " + responsavelValidar.ToString())

            if responsavelPreencher != None and responsavelValidar != None and responsavelPreencher == responsavelValidar:
                Criticas.AdicionaPendencia("Responsável pelo Preenchimento tem que ser diferente do Responsável pela Validação!")
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Período para precificação
  - PRECIF_DATA_INICIO "Data Início da Precificação" [DatePicker DateTime → CP_ORDEM_SERVICO.PRECIF_DATA_INICIO] obrigatório
  - PRECIF_DATA_FIM "Data Término da Precificação" [DatePicker DateTime → CP_ORDEM_SERVICO.PRECIF_DATA_FIM] obrigatório
  - PRECIF_CRONOGRAMA "Cronograma das Atividades da Precificação" [DataGrid RecordList → Z_00143_PRECIF_CRONOGRAMA.PRECIF_CRONOGRAMA] obrigatório
    - coluna DIAS_ATIVIDADE obrigatório
**PRECIF_CRONOGRAMA.DIAS_ATIVIDADE.ScriptModificado**
```python
if FormularioRegistro["DATA_INICIO_ATIVIDADE"].Valor != "" and FormularioRegistro["DATA_INICIO_ATIVIDADE"].Valor != None and FormularioRegistro["DIAS_ATIVIDADE"].Valor != "" and FormularioRegistro["DIAS_ATIVIDADE"].Valor != None and FormularioRegistro["DIAS_ATIVIDADE"].Valor > 0:

    dias = Convert.ToInt32(FormularioRegistro["DIAS_ATIVIDADE"].Valor)

    dataFim = FormularioRegistro["DATA_INICIO_ATIVIDADE"].Valor.Date

    #conta dias uteis
    item  = 1
    while item < dias :
        if (dataFim.DayOfWeek == DayOfWeek.Sunday):
            dataFim = dataFim.AddDays(1)
        else:
            if (dataFim.DayOfWeek == DayOfWeek.Saturday):
                dataFim = dataFim.AddDays(2)
        dataFim = dataFim.AddDays(1)
        item += 1

    if (dataFim.DayOfWeek == DayOfWeek.Sunday):
        dataFim = dataFim.AddDays(1)
    else:
        if (dataFim.DayOfWeek == DayOfWeek.Saturday):
            dataFim = dataFim.AddDays(2)

    FormularioRegistro["DATA_FIM_ATIVIDADE"].Valor = dataFim
```
    - coluna DATA_INICIO_ATIVIDADE obrigatório
**PRECIF_CRONOGRAMA.DATA_INICIO_ATIVIDADE.ScriptModificado**
```python
if FormularioRegistro["DATA_INICIO_ATIVIDADE"].Valor != "" and FormularioRegistro["DATA_INICIO_ATIVIDADE"].Valor != None and FormularioRegistro["DIAS_ATIVIDADE"].Valor != "" and FormularioRegistro["DIAS_ATIVIDADE"].Valor != None and FormularioRegistro["DIAS_ATIVIDADE"].Valor > 0:

    dias = Convert.ToInt32(FormularioRegistro["DIAS_ATIVIDADE"].Valor)

    dataFim = FormularioRegistro["DATA_INICIO_ATIVIDADE"].Valor.Date

    #conta dias uteis
    item  = 1
    while item < dias :
        if (dataFim.DayOfWeek == DayOfWeek.Sunday):
            dataFim = dataFim.AddDays(1)
        else:
            if (dataFim.DayOfWeek == DayOfWeek.Saturday):
                dataFim = dataFim.AddDays(2)
        dataFim = dataFim.AddDays(1)
        item += 1

    if (dataFim.DayOfWeek == DayOfWeek.Sunday):
        dataFim = dataFim.AddDays(1)
    else:
        if (dataFim.DayOfWeek == DayOfWeek.Saturday):
            dataFim = dataFim.AddDays(2)

    FormularioRegistro["DATA_FIM_ATIVIDADE"].Valor = dataFim
```
    - coluna DATA_FIM_ATIVIDADE
    - coluna RESPONSAVEL2 obrigatório
    - coluna SEQUENCIA
    - coluna CODIGO_ATIVIDADE
    - coluna TIPO_ATIVIDADE obrigatório
    - coluna RESPONSAVEL_ATIVIDADE obrigatório

### [331420] EventoFinal ""
Responsável: Precificação (papel 394)
Config: Codigo=PO_SUCESSO
ClassePesquisaSatisfacao: Pesquisa de Satisfação - Financeira

### [331708] EventoIntermediarioMensagem "Aviso de Encerramento de chamado"
Destinatário: Cliente (papel 18)
Config: Codigo=PO_AVISO_FINALIZACAO
ModeloComunicado: Aviso de encerramento de chamado. (Precificação)
Corpo do comunicado: Prezado(a),
Em atendimento à Ordem de Serviço nº OrdemServico.Numero - Precificação e Orçamento, informamos que a mesma foi recebida e tratada.
Para mais detalhes sobre esta solicitação Link.Consulta .
Atenciosamente,
Central de Serviços

### [331729] LinkInicial ""
Responsável: Precificação - Coordenadores (papel 395)
Config: Codigo=PO_INI_NN; TipoMensagem=MensagemProcesso
- Operação PR0004 Associar Itens Configuração
  - anexo "Consolidação Técnica" classes: Consolidação Técnica — RequeridoInicial=true
- Associação de subprocesso: AssociacaoId=80; Nome=MARCELO CAVALCANTE DE OLIVEIRA LIMA; FraseAssociacao=Portal Negócios - Precificação

### [331730] LinkInicial "Contratação Unificada"
Responsável: Precificação - Coordenadores (papel 395)
Config: TipoMensagem=MensagemProcesso
- Operação PR0004 Associar Itens Configuração
  - anexo "Arquivo para Precificação" classes: Arquivo para Precificação — RequeridoInicial=true
  - anexo "Consolidação Técnica" classes: Consolidação Técnica — RequeridoInicial=true
- Associação de subprocesso: AssociacaoId=131; Nome=GUSTAVO PACHECO LUSTOSA; FraseAssociacao=Contratação Unificada - Precificação
- Associação de subprocesso: AssociacaoId=146; Nome=GUSTAVO PACHECO LUSTOSA; FraseAssociacao=Viabilidade de Negócio - Precificação
- Associação de subprocesso: AssociacaoId=161; Nome=GUSTAVO PACHECO LUSTOSA; FraseAssociacao=Contratação Unificada - Atualizar Planilha

## Papéis usados
### papel 394: Precificação
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
precificador = OrdemServico.ResponsavelId
pessoa = Pessoa.Carrega(Convert.ToInt32(precificador));
#Utils.LogInformation(pessoa.Nome, "log")
if (pessoa != None):
    Atores.Adiciona(pessoa, "Precificador");
```
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 395: Precificação - Coordenadores
Tipo=RelacaoGrupos

## Campos customizados usados (definição global)

### DATA_ATIVIDADE — Data da atividade
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ATIVIDADE

### DATA_VENCIMENTO — Data do Vencimento
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO

### PRECIF_DATA_INICIO — Data Início da Precificação
DatePicker DateTime → CP_ORDEM_SERVICO.PRECIF_DATA_INICIO

### PRECIF_DATA_FIM — Data Término da Precificação
DatePicker DateTime → CP_ORDEM_SERVICO.PRECIF_DATA_FIM

### PRECIF_CRONOGRAMA — Cronograma da Precificação
DataGrid RecordList → Z_00143_PRECIF_CRONOGRAMA.PRECIF_CRONOGRAMA
Colunas do registro:
- DATA_INICIO_ATIVIDADE "Data Início" [DatePicker DateTime]
- DATA_FIM_ATIVIDADE "Data Témino" [DatePicker DateTime]
- RESPONSAVEL_ATIVIDADE "Responsável" [DropDownList String]
**RESPONSAVEL_ATIVIDADE.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) , to_char(p.nome || ' (' || p.usuario_rede || ')') AS nome FROM CAD_FUNCIONARIO_V F INNER JOIN PESSOA P ON (F.NOME = P.NOME AND P.ATIVO = 'Sim') INNER JOIN ORGAO O ON (O.ID_ORGAO = P.ID_ORGAO AND O.SIGLA IN ( '3000009350', '3000009351', '3000009352')) WHERE f.status_matricula = 'Ativo' ORDER BY nome")
```
- DIAS_ATIVIDADE "Dias Úteis" [TextBox Integer]
- CODIGO_ATIVIDADE "Atividade" [DropDownList String]
**CODIGO_ATIVIDADE.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT AT.CODIGO, AT.DESCRICAO FROM SUB_PROCESSO SP INNER JOIN OCORRENCIA OC ON OC.ID_SUB_PROCESSO = sp.ID_SUB_PROCESSO INNER JOIN ATIVIDADE AT ON AT.ID_SUB_PROCESSO = SP.ID_SUB_PROCESSO LEFT JOIN execucao_atividade EA ON ea.id_atividade = aT.id_atividade and oc.id_ocorrencia = ea.id_ocorrencia WHERE AT.CODIGO IN ('PO_ANALISAR', 'PO_RASCUNHO', 'PO_VALIDAR', 'PO_PLANILHA') AND DESCRICAO IS NOT NULL AND OC.NUMERO = '" + OrdemServico.Numero.ToString() + "' ORDER BY DESCRICAO")
```
- SEQUENCIA "Sequência" [TextBox Integer]

## Biblioteca de scripts referenciada
PrecifObtemCronogramaAtividade, teste
(fonte em catalogo/biblioteca/<Nome>.py)
