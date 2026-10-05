# Fluxo: Contratação de Jovem Aprendiz (CONJOV) — versão 68
Caminho: Fluxos > Ascensão Profissional e Movimentação de Pessoas Versão 68 Contratação de Jovem Aprendiz
XML: `XMLs para teste/Ascensão_Profissional_e_Movimentação_de_Pessoas_Versão_68_Contratação_de_Jovem_Aprendiz.xml` | Supravizio 19.1.1 | SubProcessoId 19889 | DesenhoProcessoId 2804 | ProcessoId 58
Órgão dono: 3000003210 - DIVISAO DE BENEFICIOS E MOVIMENTACOES DE PESSOAL | Responsável: PALOMA SABINE AMADO ROSA
Classe do subprocesso: Objetivo=Contratação de Jovem Aprendiz; DescricaoCliente=Contratação de Jovem Aprendiz; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Contratação de Jovem Aprendiz; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Gestão de Pessoas - Jovem Aprendiz - Contratação (CSCJACONTRESC)

## Grafo do fluxo
- [317753] Tarefa "Aguardar e Analisar a documentaçao do Jovem Aprendiz" {Responsável atual} → [G72756] Documentação ok?
- [325304] EventoIntermediarioMensagem "Aviso Atividade sem resposta" → [317778] Aguardando recebimento das FQs
- [325307] EventoIntermediarioTimer "" → [325308] Aviso Atividade sem resposta
- [325308] EventoIntermediarioMensagem "Aviso Atividade sem resposta" → [317782] Jovem em curso (Pausa 10 dias úteis)
- [317757] EventoIntermediarioTimer "" → [317771] Envio para RENAPSI
- [317758] EventoIntermediarioTimer "Aguardando retorno" → (fim)
- [317759] FimCancelamento "Chamado Finalizado" → (fim)
- [317754] Tarefa "RENAPSI informa ao jovem aprendiz a data prevista" {Responsável atual} → [317781] Realizar entrevista
- [317755] EventoIntermediarioMensagem "Informar a RENAPSI" → [317752] Aguardar a resposta da RENAPSI
- [317756] EventoIntermediarioTimer "" → [317772] Aviso de cobrança
- [317764] Tarefa "Enviar currículo escolhido para a entrevista - empresa terceirizada" {Responsável atual} → [G72751] Gerente escolheu?
- [317761] EventoInicial "Contratação de Jovem Aprendiz" {Movimentação de Pessoal} → [317760] Conferir e Aprovar Solicitação
- [317762] Tarefa "Comunicar a empresa terceirizada" {Responsável atual} → [G72753] Vai prosseguir?
- [317760] Tarefa "Conferir e Aprovar Solicitação" {Fila CSC - Movimentação Pessoal} → [324971] Tempo de aprovação (2 dias) | [G72750] CESEC aprova?
- [317765] EventoFinal "" {Responsável atual} → (fim)
- [317767] EventoFinal "" {Responsável atual} → (fim)
- [317768] EventoIntermediarioMensagem "Término de serviço" → [317759] Chamado Finalizado
- [317763] Tarefa "Confirmar com cliente comparecimento do jovem aprendiz na unidade" {Responsável atual} → [G72749] Compareceu a Posse?
- [317769] Tarefa "Enviar documentação para empresa terceirizada" {Responsável atual} → [317773] Aviso de candidato já selecionado
- [317779] EventoIntermediarioMensagem "Reprovação do chamado" → [324981] Ajustar planilha
- [317770] Tarefa "Finalizando chamado" {Fila CSC - Movimentação Pessoal} → [317768] Término de serviço
- [317771] EventoIntermediarioMensagem "Envio para RENAPSI" → [317775] Seleção de currículo
- [317777] Tarefa "ENVIAR A DOCUMENTAÇÃO PARA EMPRESA terceirizada" {Responsável atual} → [317783] Aviso de candidato não selecionado
- [317778] Tarefa "Aguardando recebimento das FQs" {Responsável atual} → [324976] Aguardar recebimento das FQs (10 dias) | [324977] Abertura da Solicitação do crachá | [325303] 
- [317782] Tarefa "Jovem em curso (Pausa 10 dias úteis)" {Responsável atual} → [317763] Confirmar com cliente comparecimento do jovem apre | [317758] Aguardando retorno | [325307] 
- [317783] EventoIntermediarioMensagem "Aviso de candidato não selecionado" → [317775] Seleção de currículo
- [317772] EventoIntermediarioMensagem "Aviso de cobrança" → [317786] Aguardar retorno do gestor
- [317773] EventoIntermediarioMensagem "Aviso de candidato já selecionado" → [317754] RENAPSI informa ao jovem aprendiz a data prevista
- [317774] EventoIntermediarioMensagem "Informação sobre data da posse + dias de curso do Jovem Aprendiz" → [317782] Jovem em curso (Pausa 10 dias úteis)
- [317775] Tarefa "Seleção de currículo" {Responsável atual} → [317757]  | [317790] Enviar currículo para gerentes
- [317784] Tarefa "Quais os documentos pendentes?" {Responsável atual} → [317789] Arrumar informações (RENAPSI)
- [317785] Tarefa "Convocar Jovem Aprendiz Para Posse" {Responsável atual} → [317774] Informação sobre data da posse + dias de curso do 
- [317786] Tarefa "Aguardar retorno do gestor" {Responsável atual} → [317756]  | [317764] Enviar currículo escolhido para a entrevista - emp
- [317788] Tarefa "Cadastrar colaborador no people" {Fila CSC - Movimentação Pessoal} → [317785] Convocar Jovem Aprendiz Para Posse
- [317789] EventoIntermediarioMensagem "Arrumar informações (RENAPSI)" → [317788] Cadastrar colaborador no people
- [317790] EventoIntermediarioMensagem "Enviar currículo para gerentes" → [317786] Aguardar retorno do gestor
- [324971] EventoIntermediarioTimer "Tempo de aprovação (2 dias)" → (fim)
- [324973] EventoIntermediarioTimer "Aguardando resposta (2 semanas)" → [317755] Informar a RENAPSI
- [317781] Tarefa "Realizar entrevista" {Responsável atual} → [G72755] Aprovado?
- [324976] EventoIntermediarioTimer "Aguardar recebimento das FQs (10 dias)" → [324977] Abertura da Solicitação do crachá
- [324977] Tarefa "Abertura da Solicitação do crachá" {Responsável atual} → [317770] Finalizando chamado
- [324982] EventoIntermediarioTimer "2 dias para ajustar a planilha" → (fim)
- [324983] Tarefa "Motivo não comparecimento" {Responsável atual} → [324985] Aguardar resposta do cliente (4 dias) | [G74136] Motivo plausível?
- [324985] EventoIntermediarioTimer "Aguardar resposta do cliente (4 dias)" → (fim)
- [324986] Tarefa "Número do chamado - Comunicar admissão" {Responsável atual} → [317778] Aguardando recebimento das FQs | [324987] 4 dias para comunicar admissão | [325301] 
- [324987] EventoIntermediarioTimer "4 dias para comunicar admissão" → [317778] Aguardando recebimento das FQs
- [324981] Tarefa "Ajustar planilha" {Responsável atual} → [324982] 2 dias para ajustar a planilha | [G74134] Planilha foi revisada?
- [317752] Tarefa "Aguardar a resposta da RENAPSI" {Responsável atual} → [317753] Aguardar e Analisar a documentaçao do Jovem Aprend | [324973] Aguardando resposta (2 semanas)
- [325301] EventoIntermediarioTimer "" → [325302] Aviso Atividade sem resposta
- [325302] EventoIntermediarioMensagem "Aviso Atividade sem resposta" → [324986] Número do chamado - Comunicar admissão
- [325303] EventoIntermediarioTimer "" → [325304] Aviso Atividade sem resposta
- [G72752] Gateway "Candidato já selecionado?" → «Sim» [317769] Enviar documentação para empresa terceirizada | «Não» [317777] ENVIAR A DOCUMENTAÇÃO PARA EMPRESA terceirizada
- [G72753] Gateway "Vai prosseguir?" → «Sim» [317778] Aguardando recebimento das FQs | «Não» [324983] Motivo não comparecimento
- [G72755] Gateway "Aprovado?" → «Sim» [317755] Informar a RENAPSI | «Não» [317777] ENVIAR A DOCUMENTAÇÃO PARA EMPRESA terceirizada
- [G74136] Gateway "Motivo plausível?" → «Sim» [317763] Confirmar com cliente comparecimento do jovem apre | «Não» [317767] 
- [G72756] Gateway "Documentação ok?" → «Não» [317784] Quais os documentos pendentes? | «Sim» [317788] Cadastrar colaborador no people
- [G74134] Gateway "Planilha foi revisada?" → «Não» [317765]  | «Sim» [317760] Conferir e Aprovar Solicitação
- [G72749] Gateway "Compareceu a Posse?" → «Não» [317762] Comunicar a empresa terceirizada | «Sim» [324986] Número do chamado - Comunicar admissão
- [G72750] Gateway "CESEC aprova?" → «Sim» [G72752] Candidato já selecionado? | «Não» [317779] Reprovação do chamado
- [G72751] Gateway "Gerente escolheu?" → «Não» [317777] ENVIAR A DOCUMENTAÇÃO PARA EMPRESA terceirizada | «Sim» [317754] RENAPSI informa ao jovem aprendiz a data prevista

## Gateways
### [G72752] Candidato já selecionado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["SIM_NAO"] == "Sim"
```
- alternativa → [317769] Enviar documentação para empresa terceirizada: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [317777] ENVIAR A DOCUMENTAÇÃO PARA EMPRESA terceirizada: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G72753] Vai prosseguir? (EventBasedExclusiveDecision)
- alternativa → [317778] Aguardando recebimento das FQs: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
- alternativa → [324983] Motivo não comparecimento: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=2
### [G72755] Aprovado? (EventBasedExclusiveDecision)
- alternativa → [317755] Informar a RENAPSI: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [317777] ENVIAR A DOCUMENTAÇÃO PARA EMPRESA terceirizada: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
### [G74136] Motivo plausível? (EventBasedExclusiveDecision)
- alternativa → [317763] Confirmar com cliente comparecimento do jovem apre: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [317767] : OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
### [G72756] Documentação ok? (EventBasedExclusiveDecision)
- alternativa → [317784] Quais os documentos pendentes?: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
- alternativa → [317788] Cadastrar colaborador no people: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
### [G74134] Planilha foi revisada? (EventBasedExclusiveDecision)
- alternativa → [317765] : OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
- alternativa → [317760] Conferir e Aprovar Solicitação: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
### [G72749] Compareceu a Posse? (EventBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.GetCustom("POSSE")
```
- alternativa → [317762] Comunicar a empresa terceirizada: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=3
- alternativa → [324986] Número do chamado - Comunicar admissão: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=4
### [G72750] CESEC aprova? (EventBasedExclusiveDecision)
Codigo=APROVA_MOVI
- alternativa → [G72752] Candidato já selecionado?: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1; RotuloMotivo=Sim
- alternativa → [317779] Reprovação do chamado: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0; RotuloMotivo=Não; MotivoObrigatorio=true; PublicarRespostaAA=true
### [G72751] Gerente escolheu? (EventBasedExclusiveDecision)
Codigo=GERENTEESCOLEU
- alternativa → [317777] ENVIAR A DOCUMENTAÇÃO PARA EMPRESA terceirizada: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
- alternativa → [317754] RENAPSI informa ao jovem aprendiz a data prevista: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1

## Atividades

### [317753] Tarefa "Aguardar e Analisar a documentaçao do Jovem Aprendiz"
Responsável: Responsável atual (papel 36)
Config: UnidadeANO=Minutos
MotivoInterrupcaoSLA: Aguardando aprovação

### [325304] EventoIntermediarioMensagem "Aviso Atividade sem resposta"
Destinatário: Responsável atual (papel 36)
ModeloComunicado: Atividade sem resposta
Corpo do comunicado: Predazo(a), lembre-se de avançar a atividade 
OrdemServico.Atividade. Atenciosamente,Equipe Contratação Jovem Aprendiz.

### [325307] EventoIntermediarioTimer ""
Config: TempoIntervalo=2880

### [325308] EventoIntermediarioMensagem "Aviso Atividade sem resposta"
Destinatário: Responsável atual (papel 36)
ModeloComunicado: Atividade sem resposta
Corpo do comunicado: Predazo(a), lembre-se de avançar a atividade 
OrdemServico.Atividade. Atenciosamente,Equipe Contratação Jovem Aprendiz.

### [317757] EventoIntermediarioTimer ""
Config: TempoIntervalo=14400

### [317758] EventoIntermediarioTimer "Aguardando retorno"
Config: TempoIntervalo=14400

### [317759] FimCancelamento "Chamado Finalizado"

### [317754] Tarefa "RENAPSI informa ao jovem aprendiz a data prevista"
Responsável: Responsável atual (papel 36)
MotivoInterrupcaoSLA: Aguardando ação de intervenientes externos

### [317755] EventoIntermediarioMensagem "Informar a RENAPSI"
Destinatário: Responsável atual (papel 36)
ModeloComunicado: Alerta sobre o envio de comunicado
Corpo do comunicado: Prezado(a),
Fase de envio do comunicado referente à Ordem de Serviço (OS) OrdemServico.Numero 
Agradecemos pela atenção!
Para obter mais informações e enviar o comunicado: Link.Consulta 
Atenciosamente,
Central de Serviços

### [317756] EventoIntermediarioTimer ""
Config: TempoIntervalo=7200

### [317764] Tarefa "Enviar currículo escolhido para a entrevista - empresa terceirizada"
Responsável: Responsável atual (papel 36)
Config: Codigo=GERENTEESCOLHEU

### [317761] EventoInicial "Contratação de Jovem Aprendiz"
Responsável: Movimentação de Pessoal (papel 230)
TipoSolicitacao: 18.01. Gestão de Pessoas - Ascensão e Movimentação de Pessoas
**ScriptFim**
```python
#lista = Utils.ExecuteDataTable("SELECT DISTINCT PESSOA.NOME_ABREVIADO AS NOME_COMPLETO FROM ORGAO LEFT OUTER JOIN PESSOA ON ORGAO.ID_GESTOR = PESSOA.ID_PESSOA WHERE ROWNUM = 1 AND ORGAO.ID_ORGAO = '"+OrdemServico.GetCustom("SCR_MOVI").ToString()+"' AND ORGAO.ATIVO like 'Sim'")

#for linha in lista.Rows:
#   gestor = linha["NOME_COMPLETO"].ToString()
    
#OrdemServico.SetCustom("RESPONSAVEL_MOV",OrdemServico.GetCustom("NOME_GESTORES"))
```
**ScriptValidacao**
```python
from Venki.Supravizio.Processo.Custom import Evento
if OrdemServico.Atividade.Tipo == "EventoInicial":
    if (OrdemServico.GetCustom("FAVORECIDO_TODOS") == ""):
        Criticas.AdicionaPendencia("Campo Gestor para aprovação não foi preenchido !")
```
**ScriptFormCarregado**
```python
#----- Visível
Formulario["FAVORECIDO_TODOS"].Visivel = False
#Formulario["CNPJ"].Visivel = False
#Formulario["ENDERECO_FORNECEDOR"].Visivel = False

#----- Habilitado
#Formulario["ENDERECO_FORNECEDOR"].Habilitado = False
#Formulario["CNPJ"].Habilitado = False

#Formulario["SCR_TODOS_RH"].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - LABEL100 "<b style="color:black">Para acessar a planilha de Perfil de Vaga <a href="https://bbtecno.sharepoint.com/:x:/t/Gepes/ETdBWi5dyMpLjQx-tpEFjP4Bm2PAbGkLkLjXAIQ-VKdrQQ?e=rmAf1N">clique aqui</a></b>" [Label String(500) → CPE_CONTRATOS.LABEL100]
- Operação PR0001 Preencher Campos
  - SCR_TODOS_RH "UOR Movimentação" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH] obrigatório
**SCR_TODOS_RH.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["FAVORECIDO_TODOS"].Habilitado = True
Formulario["FAVORECIDO_TODOS"].Visivel = True
Formulario["FAVORECIDO_TODOS"].Valor = None

lotacao = ""
dotacao = ""
idgestor = ""
nomegestor = ""


if Formulario["SCR_TODOS_RH"].Valor != None and Formulario["SCR_TODOS_RH"].Valor != "":

    scr = Formulario["SCR_TODOS_RH"].Valor
   
    if (scr != ""):
         
        #Consulta o gestor do órgão

        lista = Utils.ExecuteDataTable(" SELECT DISTINCT ID_GESTOR FROM ORGAO where '"+scr.ToString()+"' = SIGLA AND ATIVO = 'Sim' ")

        for linha in lista.Rows:
            idgestor = Convert.ToInt32(linha["ID_GESTOR"])

        if (idgestor != ""):
            pessoa = Pessoa.Carrega(idgestor)
            nomegestor = pessoa.Nome
            Formulario["FAVORECIDO_TODOS"].Valor = idgestor
            Formulario["FAVORECIDO_TODOS"].Habilitado = False
```
  - SEXO_CONTRA "Sexo" [DropDownList String → CP_ORDEM_SERVICO.SEXO_CONTRA] obrigatório
  - FAVORECIDO_TODOS "Gestor para aprovação da movimentação" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
  - FAIXA_ETARIA "Faixa Etária" [DropDownList String → CPE_CSC.FAIXA_ETARIA] obrigatório
  - ATIVIDADES "Atividades a serem desenvolvidas (listar pelo menos 3 atividades)" [Memo String(2000) → CP_ORDEM_SERVICO.ATIVIDADES] obrigatório
  - REQUISITOS "Requisitos desejáveis (listar pelo menos 2 requisitos)" [Memo String(2000) → CP_ORDEM_SERVICO.REQUISITOS] obrigatório
  - HORARIO_JOVEM_APRENDIZ "Horário do Jovem Aprendiz (deverá cumprir 4 horas diárias)" [DropDownList String → CPE_CSC.HORARIO_JOVEM_APRENDIZ] obrigatório
  - DescricaoDetalhada (nativo) "Observação"
  - LOCAL DE ATUACAO "Local de atuação" [DropDownList String → CPE_HOMOLOGACAO.LOCAL_DE_ATUACAO] obrigatório
  - FAVORECIDO_MONITOR "Supervisor/Orientador do Jovem Aprendiz" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_MONITOR] obrigatório
**FAVORECIDO_MONITOR.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
monitor = Formulario["FAVORECIDO_MONITOR"].Valor
cargo = Pessoa.Carrega("Cargo", monitor)
OrdemServico.SetCustom("CARGO", cargo)
```
- Operação PR0004 Associar Itens Configuração: Nome=ANEXO DE DOCUMENTO
  - anexo "Anexe a planilha de Perfil de Vagas preenchida" classes: Arquivo — ProduzidoTermino=true; IncluirPaginaAssinatura=true

### [317762] Tarefa "Comunicar a empresa terceirizada"
Responsável: Responsável atual (papel 36)

### [317760] Tarefa "Conferir e Aprovar Solicitação"
Responsável: Fila CSC - Movimentação Pessoal (papel 510)
Config: Codigo=SOLICITACAO
MotivoInterrupcaoSLA: Aguardando aprovação
**ScriptInicio**
```python
###PGESV###

orgao = OrdemServico.GetCustom("SCR_TODOS_RH")
descricao = ""
OrdemServico.SetCustom("DESCRICAO_ORGAO",orgao.ToString())


#Consulta a descrição do órgão destino
lista = Utils.ExecuteDataTable("SELECT distinct SCR, SCR || ' - ' || SUBSTR(SCR_DESCRICAO, INSTR(SCR_DESCRICAO,'-')+1) AS NOME FROM COB_GL_CENTRO where SCR is not null AND ENABLED_FLAG = 'Y' AND SCR like '%"+ OrdemServico.GetCustom("SCR_TODOS_RH").ToString() +"%'")

#lista = Utils.ExecuteDataTable("SELECT distinct lpad(SCR, 5, '0') AS SCR,lpad(SCR, 5, '0') || ' - ' || SUBSTR(SCR_DESCRICAO, INSTR(SCR_DESCRICAO,'-')+1) AS NOME FROM COB_GL_CENTRO where SCR is not null AND ENABLED_FLAG = 'Y' AND SCR like '%"+ OrdemServico.GetCustom("SCR_TODOS_RH").ToString() +"%'")

for linha in lista.Rows:
    
    descricao = linha["NOME"].ToString()
    

if descricao !="" and descricao!=None:
    OrdemServico.SetCustom("DESCRICAO_ORGAO",descricao)
```
- Operação PR0001 Preencher Campos
  - OBS_ACOMPA "Acompanhamento da Solicitação" [Memo String → CP_ORDEM_SERVICO.OBS_ACOMPA]

### [317765] EventoFinal ""
Responsável: Responsável atual (papel 36)
Config: TipoFinalizacao=NaoRealizado

### [317767] EventoFinal ""
Responsável: Responsável atual (papel 36)

### [317768] EventoIntermediarioMensagem "Término de serviço"
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de serviço
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Em atendimento à Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto, comunico que foi realizado o término da atividade pelo Cesec.
Para mais detalhes sobre esta solicitação, clique no link a seguir ==> Link.Consulta.
 Complemento1 
Atenciosamente,
Central de Serviços

### [317763] Tarefa "Confirmar com cliente comparecimento do jovem aprendiz na unidade"
Responsável: Responsável atual (papel 36)

### [317769] Tarefa "Enviar documentação para empresa terceirizada"
Responsável: Responsável atual (papel 36)

### [317779] EventoIntermediarioMensagem "Reprovação do chamado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Aviso de reprovação de chamados
Corpo do comunicado: Prezado(a) OrdemServico.Cliente.Nome ,
A Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto não foi aprovada.
 Complemento1 
Para obter mais detalhes sobre a solicitação e a reprovação, CLIQUE no link =>> Link.Consulta 
Central de Serviços

### [317770] Tarefa "Finalizando chamado"
Responsável: Fila CSC - Movimentação Pessoal (papel 510)
Config: UnidadeANO=Minutos
- Operação PR0001 Preencher Campos
  - OBS_ACOMPA "Acompanhamento da Solicitação" [Memo String → CP_ORDEM_SERVICO.OBS_ACOMPA]

### [317771] EventoIntermediarioMensagem "Envio para RENAPSI"
Destinatário: Responsável atual (papel 36)
ModeloComunicado: Alerta sobre o envio de comunicado
Corpo do comunicado: Prezado(a),
Fase de envio do comunicado referente à Ordem de Serviço (OS) OrdemServico.Numero 
Agradecemos pela atenção!
Para obter mais informações e enviar o comunicado: Link.Consulta 
Atenciosamente,
Central de Serviços

### [317777] Tarefa "ENVIAR A DOCUMENTAÇÃO PARA EMPRESA terceirizada"
Responsável: Responsável atual (papel 36)

### [317778] Tarefa "Aguardando recebimento das FQs"
Responsável: Responsável atual (papel 36)
MotivoInterrupcaoSLA: Aguardando retorno de documentação

### [317782] Tarefa "Jovem em curso (Pausa 10 dias úteis)"
Responsável: Responsável atual (papel 36)
MotivoInterrupcaoSLA: Aguardando ação de intervenientes externos

### [317783] EventoIntermediarioMensagem "Aviso de candidato não selecionado"
Destinatário: Responsável atual (papel 36)
ModeloComunicado: Alerta sobre o envio de comunicado
Corpo do comunicado: Prezado(a),
Fase de envio do comunicado referente à Ordem de Serviço (OS) OrdemServico.Numero 
Agradecemos pela atenção!
Para obter mais informações e enviar o comunicado: Link.Consulta 
Atenciosamente,
Central de Serviços

### [317772] EventoIntermediarioMensagem "Aviso de cobrança"
Destinatário: Gerente Executivo do Responsável atual (papel 370)
ModeloComunicado: Cobrança de retorno
Corpo do comunicado: Prezado(a),
A ordem de serviço OrdemServico.Numero aguarda seu retorno para prosseguir com o atendimento.
Atenciosamente,
Central de Serviços

### [317773] EventoIntermediarioMensagem "Aviso de candidato já selecionado"
Destinatário: Reembolso (papel 196)
Config: ListaDestinatarios=admempregado@bbts.com.br;movimentacaopessoal@bbts.com.br;jovemaprendiz_estagiario@bbts.com.br; NomeRemetente=CENTRAL DE SERVIÇOS - CONTRATAÇÂO DE JOVEM APRENDIZ
ModeloComunicado: Aviso de candidato selecionado
Corpo do comunicado: Prezado(a),
Um candidato já foi selecionado.
Atenciosamente,
CENTRAL DE SERVIÇOS

### [317774] EventoIntermediarioMensagem "Informação sobre data da posse + dias de curso do Jovem Aprendiz"
Destinatário: Gestor do Responsável (papel 350)
ModeloComunicado: Data de posse de jovem aprendiz
Corpo do comunicado: Prezado(a)s,
Informamos que o jovem aprendiz OrdemServico.Customizado.NOME foi cadastrado. 
 Atenciosamente,
Central de Serviços

### [317775] Tarefa "Seleção de currículo"
Responsável: Responsável atual (papel 36)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno

### [317784] Tarefa "Quais os documentos pendentes?"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informe os documentos pendentes
  - PENDENCIA "Documentos pendentes" [TextBox String → CPE_FINANCEIRO.PENDENCIA] obrigatório

### [317785] Tarefa "Convocar Jovem Aprendiz Para Posse"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Convocação jovem apendiz
  - MP_DT_FIM_SUBST "Data de Admissão BBTS (Início de contrato)" [DatePicker DateTime → CPE_MOVIMENTACAO_PESSOA.MP_DT_FIM_SUBST] obrigatório
  - HORA_ENTRADA "Horário do almoço" [TextBox String(80) → CP_ORDEM_SERVICO.HORA_ENTRADA] obrigatório
  - POSSE "Posse" [DropDownList String → CP_ORDEM_SERVICO.POSSE] obrigatório
  - Justificativa (nativo) "Dados do selecionado" obrigatório
    - coluna NUMERO_SERIE_PATRI obrigatório
    - coluna DESCRICAO_PATRIMONIO obrigatório
    - coluna CONDICAO_USO obrigatório
    - coluna NUMERO_PATRIMONIO obrigatório
  - OBS_ACOMPA "Acompanhamento da Solicitação" [Memo String → CP_ORDEM_SERVICO.OBS_ACOMPA]
  - MP_EST_DT_VIGENCIA "Data de Admissão Renapsi (Início de contrato)" [DatePicker DateTime → CPE_MOVIMENTACAO_PESSOA.MP_EST_DT_VIGENCIA] obrigatório

### [317786] Tarefa "Aguardar retorno do gestor"
Responsável: Responsável atual (papel 36)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno

### [317788] Tarefa "Cadastrar colaborador no people"
Responsável: Fila CSC - Movimentação Pessoal (papel 510)
Config: ConfirmaResponsabilidade=true
**ScriptFormCarregado**
```python
Formulario["NUM_VERSAO"].Visivel=True
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informe a data de posse
  - DATA_POSSE "Data da Posse" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_POSSE] obrigatório
- Operação PR0001 Preencher Campos
  - MP_EST_SINDICATO "Sindicato" [TextBox String → CPE_MOVIMENTACAO_PESSOA.MP_EST_SINDICATO] obrigatório
  - MP_EST_DT_VIGENCIA "Vigência do Contrato Renapsi" [DatePicker DateTime → CPE_MOVIMENTACAO_PESSOA.MP_EST_DT_VIGENCIA] obrigatório
  - MP_DT_FIM_SUBST "Vigência do Contrato BBTS" [DatePicker DateTime → CPE_MOVIMENTACAO_PESSOA.MP_DT_FIM_SUBST] obrigatório
  - MP_EST_NOME "Nome" [TextBox String → CPE_MOVIMENTACAO_PESSOA.MP_EST_NOME] obrigatório
  - MP_EST_MATRICULA "Matrícula" [TextBox String → CPE_MOVIMENTACAO_PESSOA.MP_EST_MATRICULA] obrigatório
  - MP_EST_DT_INICIO "Data Início do Contrato" [DatePicker DateTime → CPE_MOVIMENTACAO_PESSOA.MP_EST_DT_INICIO] obrigatório
  - MP_EST_CARGO "Cargo" [TextBox String → CPE_MOVIMENTACAO_PESSOA.MP_EST_CARGO] obrigatório
  - MP_EST_PLANO_SAL "Plano Salarial" [TextBox String → CPE_MOVIMENTACAO_PESSOA.MP_EST_PLANO_SAL] obrigatório
  - MP_EST_FAIXA "Faixa" [TextBox String → CPE_MOVIMENTACAO_PESSOA.MP_EST_FAIXA] obrigatório
  - MP_EST_GESTOR_POSICAO "Reportar-se posição" [TextBox String → CPE_MOVIMENTACAO_PESSOA.MP_EST_GESTOR_POSICAO] obrigatório
- Operação PR0001 Preencher Campos
  - NUM_VERSAO "Número da posição" [TextBox Integer → CP_ORDEM_SERVICO.NUM_VERSAO] obrigatório

### [317789] EventoIntermediarioMensagem "Arrumar informações (RENAPSI)"
Destinatário: Responsável atual (papel 36)
ModeloComunicado: Ajuste de Documentação
Corpo do comunicado: Prezado(a)s,
Após análise da documentação enviada, verificamos a ausência de alguns documentos e a necessidade de ajustes nas informações fornecidas. A fim de garantir o andamento correto do processo, solicitamos que as devidas correções sejam efetuadas e os documentos atualizados sejam reenviados o mais breve possível.
Documentos:
 OrdemServico.Customizado.PENDENCIA 
Atenciosamente,
Central de Serviços

### [317790] EventoIntermediarioMensagem "Enviar currículo para gerentes"
Destinatário: Responsável atual (papel 36)
ModeloComunicado: Alerta sobre o envio de comunicado
Corpo do comunicado: Prezado(a),
Fase de envio do comunicado referente à Ordem de Serviço (OS) OrdemServico.Numero 
Agradecemos pela atenção!
Para obter mais informações e enviar o comunicado: Link.Consulta 
Atenciosamente,
Central de Serviços

### [324971] EventoIntermediarioTimer "Tempo de aprovação (2 dias)"
Config: TempoIntervalo=2880

### [324973] EventoIntermediarioTimer "Aguardando resposta (2 semanas)"
Config: TempoIntervalo=20160

### [317781] Tarefa "Realizar entrevista"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Data da entrevista dos currículos selecionados
  - DATA_ATIVIDADE "Data da atividade" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ATIVIDADE] obrigatório

### [324976] EventoIntermediarioTimer "Aguardar recebimento das FQs (10 dias)"
Config: TempoIntervalo=14400

### [324977] Tarefa "Abertura da Solicitação do crachá"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - NÚMERO DO CHAMADO "Número do crachá" [TextBox Integer → CP_ORDEM_SERVICO.NUMERO_DO_CHAMADO] obrigatório
    - coluna NUMERO obrigatório
    - coluna NUMERONF obrigatório

### [324982] EventoIntermediarioTimer "2 dias para ajustar a planilha"
Config: TempoIntervalo=2880

### [324983] Tarefa "Motivo não comparecimento"
Responsável: Responsável atual (papel 36)
Config: Codigo=MOTIVO
MotivoInterrupcaoSLA: Aguardando ação de intervenientes externos
- Operação PR0001 Preencher Campos
  - DESCRICAO_DETALHADA "Motivo não comparecimento" [Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório

### [324985] EventoIntermediarioTimer "Aguardar resposta do cliente (4 dias)"
Config: TempoIntervalo=5760

### [324986] Tarefa "Número do chamado - Comunicar admissão"
Responsável: Responsável atual (papel 36)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- Operação PR0001 Preencher Campos
  - NUM_ITEM "Número do Chamado" [TextBox String(30) → CP_ORDEM_SERVICO.NUM_ITEM] obrigatório

### [324987] EventoIntermediarioTimer "4 dias para comunicar admissão"
Config: TempoIntervalo=5760

### [324981] Tarefa "Ajustar planilha"
Responsável: Responsável atual (papel 36)
Config: Codigo=PLANILHA
MotivoInterrupcaoSLA: Aguardando ação de intervenientes externos

### [317752] Tarefa "Aguardar a resposta da RENAPSI"
Responsável: Responsável atual (papel 36)
MotivoInterrupcaoSLA: Aguardando ação de intervenientes externos

### [325301] EventoIntermediarioTimer ""
Config: TempoIntervalo=1440

### [325302] EventoIntermediarioMensagem "Aviso Atividade sem resposta"
Destinatário: Responsável atual (papel 36)
ModeloComunicado: Atividade sem resposta
Corpo do comunicado: Predazo(a), lembre-se de avançar a atividade 
OrdemServico.Atividade. Atenciosamente,Equipe Contratação Jovem Aprendiz.

### [325303] EventoIntermediarioTimer ""
Config: TempoIntervalo=2880

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
### papel 230: Movimentação de Pessoal
Tipo=RelacaoGrupos
### papel 510: Fila CSC - Movimentação Pessoal
Tipo=RelacaoPessoas | pessoas: Fila CSC - Movimentação Pessoal
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 370: Gerente Executivo do Responsável atual
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Processo.Custom import Ator
gestor = OrdemServico.Responsavel.Orgao.Gestor

#Variável de Controle do Loop infinito
countLoop = 0;


#Loop da busca do Gerente Executivo do Favorecido
while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência" ))  and countLoop <8 ):
	gestor = gestor.Orgao.OrgaoPai.Gestor
	idgestor = gestor.Id
	
	if (gestor.Orgao.OrgaoPai == None or gestor.Orgao.OrgaoPai == DBNull.Value):
		break	

	countLoop = countLoop + 1

if (countLoop >= 8):
	Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")

Atores.Adiciona(gestor, "Gerente Executivo de" + OrdemServico.Responsavel.ToString())
```
### papel 196: Reembolso
Tipo=RelacaoGrupos
### papel 350: Gestor do Responsável
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
gestor = OrdemServico.Responsavel.ObtemChefia(False)

# se for um diretor ou presidente (mudar os identificadores e relacionar todos)
if gestor.Id == 4458 or gestor.Id == 4459 or gestor.Id == 4460 or gestor.Id == 4461 or gestor.Id == 3805 or gestor.Id == 5313 or gestor.Id == 5457 or gestor.Id == 5903 or gestor.Id == 13787:
    gestor = Pessoa.Carrega(1194)

Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Responsavel.ToString())
```

## Campos customizados usados (definição global)

### LABEL100 — Label100
Label String(500) → CPE_CONTRATOS.LABEL100

### SCR_TODOS_RH — UOR Movimentação
DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH
Descrição: SCR Movimentação
**LookupScript**
```python
###PGESV###
Itens = DB.ExecuteDataTable("SELECT to_char(SCR) as SCR, NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO");
```

### SEXO_CONTRA — Sexo
DropDownList String → CP_ORDEM_SERVICO.SEXO_CONTRA
Itens: Feminino;Masculino;Indiferente

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### FAIXA_ETARIA — Faixa Etária
DropDownList String → CPE_CSC.FAIXA_ETARIA
Itens: 14 a 16;17 a 20;21 a 24

### ATIVIDADES — Atividades
Memo String(2000) → CP_ORDEM_SERVICO.ATIVIDADES

### REQUISITOS — Requisitos desejáveis
Memo String(2000) → CP_ORDEM_SERVICO.REQUISITOS

### HORARIO_JOVEM_APRENDIZ — Horário do Jovem Aprendiz
DropDownList String → CPE_CSC.HORARIO_JOVEM_APRENDIZ
Itens: Matutino;Vespertino

### LOCAL DE ATUACAO — LOCAL DE ATUACAO
DropDownList String → CPE_HOMOLOGACAO.LOCAL_DE_ATUACAO
Itens: MACEIO;MANAUS;SALVADOR - AV. LUIS VIANA;SALVADOR - RUA MARQUES;FORTALEZA;BRASILIA - 716 NORTE;BRASILIA - MATRIZ;BRASILIA - PARQUE TECNOLOGICO;BRASILIA - SAUN QD 5;VITORIA;GOIANIA;SÃO LUIZ;BELO HORIZONTE;UBERLANDIA;CAMPO GRANDE;CUIABA;BELEM;JOAO PESSOA;RECIFE;TERESINA;CASCAVEL;CURITIBA - PRAÇA TIRADENTES;CURITIBA - RUA AMINTAS;LONDRINA;PIRAI;RIO DE JANEIRO - Estrada dos bandeirantes 10875;RIO DE JANEIRO - Estrada dos bandeirantes 13843;RIO DE JANEIRO - AV. REPUBLICA DO CHILE;RIO DE JANEIRO - CARIOCA;RIO DE JANEIRO - JACAREPAGUA;	RIO DE JANEIRO - TELEPORTO;NATAL;PORTO VELHO;PASSO FUNDO;PORTO ALE…

### FAVORECIDO_MONITOR — Monitor
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_MONITOR
Descrição: Para pesquisa rápida faça:
1 - Clique na seta à direita do campo para abrir a relação de nomes;
2 - Com a lista ABERTA, pressione as teclas Ctrl + F (no IE aparece uma caixa de texto na parte superior esquerda e no Chrome na parte superior direita);
3 -  Digite o nome (ou parte dele) a ser pesquisado (serão marcados todas ocorrências que correspondam ao texto digitado);
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as id_pessoa, p.nome FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cpp on cpp.matricula = f.matricula inner join pessoa p on p.id_pessoa = cpp.id_pessoa WHERE f.status_matricula = 'Ativo' AND p.ativo = 'Sim' order by p.nome")
```

### OBS_ACOMPA — Acompanhamento da Solicitação
Memo String → CP_ORDEM_SERVICO.OBS_ACOMPA

### PENDENCIA — Pendência
TextBox String → CPE_FINANCEIRO.PENDENCIA

### MP_DT_FIM_SUBST — Data Fim Substituição
DatePicker DateTime → CPE_MOVIMENTACAO_PESSOA.MP_DT_FIM_SUBST

### HORA_ENTRADA — Hora Entrada
TextBox String(80) → CP_ORDEM_SERVICO.HORA_ENTRADA

### POSSE — Posse
DropDownList String → CP_ORDEM_SERVICO.POSSE
Itens: Compareceu;Compareceu e pediu postergação;Não compareceu;Compareceu e desistiu da posse

### MP_EST_DT_VIGENCIA — Vigência
DatePicker DateTime → CPE_MOVIMENTACAO_PESSOA.MP_EST_DT_VIGENCIA

### DATA_POSSE — Data da Posse
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_POSSE

### MP_EST_SINDICATO — Sindicato
TextBox String → CPE_MOVIMENTACAO_PESSOA.MP_EST_SINDICATO

### MP_EST_NOME — Nome
TextBox String → CPE_MOVIMENTACAO_PESSOA.MP_EST_NOME

### MP_EST_MATRICULA — Matrícula
TextBox String → CPE_MOVIMENTACAO_PESSOA.MP_EST_MATRICULA

### MP_EST_DT_INICIO — Data Início do Contrato
DatePicker DateTime → CPE_MOVIMENTACAO_PESSOA.MP_EST_DT_INICIO

### MP_EST_CARGO — Cargo
TextBox String → CPE_MOVIMENTACAO_PESSOA.MP_EST_CARGO

### MP_EST_PLANO_SAL — Plano Salarial
TextBox String → CPE_MOVIMENTACAO_PESSOA.MP_EST_PLANO_SAL

### MP_EST_FAIXA — Faixa
TextBox String → CPE_MOVIMENTACAO_PESSOA.MP_EST_FAIXA

### MP_EST_GESTOR_POSICAO — Reportar-se posição
TextBox String → CPE_MOVIMENTACAO_PESSOA.MP_EST_GESTOR_POSICAO

### NUM_VERSAO — Número da Posição
TextBox Integer → CP_ORDEM_SERVICO.NUM_VERSAO

### DATA_ATIVIDADE — Data da atividade
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ATIVIDADE

### NÚMERO DO CHAMADO — Número do Chamado
TextBox Integer → CP_ORDEM_SERVICO.NUMERO_DO_CHAMADO
Descrição: Número do Chamado no Sistema CHAMA.

### DESCRICAO_DETALHADA — Descrição detalhada
Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA

### NUM_ITEM — Número do Ítem
TextBox String(30) → CP_ORDEM_SERVICO.NUM_ITEM

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
