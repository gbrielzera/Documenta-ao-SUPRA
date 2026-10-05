# Fluxo: Fale com a V360 (FALEV360) — versão 27
Caminho: Fluxos > Suprimentos - Contratos Versão 27 Fale com a V360
XML: `XMLs para teste/Suprimentos_-_Contratos_Versão_27_Fale_com_a_V360.xml` | Supravizio 19.1.1 | SubProcessoId 21004 | DesenhoProcessoId 2867 | ProcessoId 151
Órgão dono: 3000003140 - DIVISAO DE GESTAO DE CONTRATOS COM FORNECEDORES | Responsável: MONICA GUIZZARDI VAILLANT
Classe do subprocesso: Objetivo=Fale com a V360; DescricaoCliente=Fale com a V360; CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Divergência entre a nota fiscal e a ordem de compra (DIVERGENCIANFOC); Divergência entre a nota fiscal e os tributos da base (DIVERGENCIANFTB); Medição não localizada (MEDLOCALIZA); Pendências no instrumento de Medição. (PENDENCIAMEDICAO); Erro na consulta de autenticidade (ERROCONAUTEN); Outros (OUTROS); Ingresso de Nota Fiscal (INGRESSONF); Compras Diretas (COMPRASDIRETASV360); Contas Concessionárias (CONTASCONCESSIONARIAS); Faturas de Aluguéis e condomínio (FATURAAC); Nota Técnica (NOTATECNICAV360); PDPEP (PDPEP); Acesso a V360 (ACESSOAV360)

## Grafo do fluxo
- [335012] EventoFinal "" {Responsável atual} → (fim)
- [335013] EventoFinal "" {Responsável atual} → (fim)
- [335014] EventoIntermediarioMensagem "Ordem de serviço finalizada" → [335013] 
- [335015] Tarefa "Analisar solicitação" {Fila DICOF} → [335026] Informar Solução
- [335016] Tarefa "Analisar solicitação" {Fila Disec} → [335024] Informar Solução
- [335017] Tarefa "Verificar Solicitação Com Aprovação." {Fila Cesec - V360} → [G76028] Informe o responsável por sanar a dúvida do client
- [335018] EventoIntermediarioMensagem "Aviso Sobre Abertura de Ordem de Serviço" → [335016] Analisar solicitação
- [335019] EventoInicial "" {Cliente} → [335020] Aviso sobre Abertura de Chamado
- [335020] EventoIntermediarioMensagem "Aviso sobre Abertura de Chamado" → [G76027] É solicitação de Acesso ao V360?
- [335021] EventoIntermediarioMensagem "Aviso Sobre Abertura de Ordem de Serviço" → [335015] Analisar solicitação
- [335022] EventoIntermediarioMensagem "Ordem de serviço finalizada" → [335025] 
- [335023] Tarefa "Informar Solução" {Responsável atual} → [335014] Ordem de serviço finalizada
- [335024] Tarefa "Informar Solução" {Responsável atual} → [335027] Ordem de serviço finalizada
- [335025] EventoFinal "" {Responsável atual} → (fim)
- [335026] Tarefa "Informar Solução" {Responsável atual} → [335022] Ordem de serviço finalizada
- [335027] EventoIntermediarioMensagem "Ordem de serviço finalizada" → [335012] 
- [335028] Tarefa "Verificar Solicitação" {Fila Cesec - V360} → [G76028] Informe o responsável por sanar a dúvida do client
- [G76027] Gateway "É solicitação de Acesso ao V360?" → «Sim» [335017] Verificar Solicitação Com Aprovação. | «Não» [335028] Verificar Solicitação
- [G76028] Gateway "Informe o responsável por sanar a dúvida do cliente" → «Cesec Cont» [335023] Informar Solução | «Gesuc/Dicof» [335021] Aviso Sobre Abertura de Ordem de Serviço | «Gesap/Disec» [335018] Aviso Sobre Abertura de Ordem de Serviço

## Gateways
### [G76027] É solicitação de Acesso ao V360? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == 'ACESSOAV360'
```
- alternativa → [335017] Verificar Solicitação Com Aprovação.: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [335028] Verificar Solicitação: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
### [G76028] Informe o responsável por sanar a dúvida do cliente (EventBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("VERIFICASOLIC")
```
- alternativa → [335023] Informar Solução: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Cesec Cont
**ValorComparacaoDecision**
```python
1
```
- alternativa → [335021] Aviso Sobre Abertura de Ordem de Serviço: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Gesuc/Dicof
**ValorComparacaoDecision**
```python
2
```
- alternativa → [335018] Aviso Sobre Abertura de Ordem de Serviço: SequenciaAvaliacao=2; OperadorDecision=Equal; ReferenciaDecision=Gesap/Disec
**ValorComparacaoDecision**
```python
3
```

## Atividades

### [335012] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [335013] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [335014] EventoIntermediarioMensagem "Ordem de serviço finalizada"
Destinatário: Cliente (papel 18)
ModeloComunicado: Fale com a V360
Corpo do comunicado: Prezado(a),
A Ordem de Serviço nº OrdemServico.Numero sobre o Assunto: OrdemServico.Assunto foi atendido com sucesso!
Solução informada: 
OrdemServico.Customizado.OBS24 
Para maiores informações:
Link.Consulta .
Caso ainda tenha dúvidas, abra um novo Fale com a V360 referenciando esta ordem de serviço.
Atenciosamente,
Central de Serviços

### [335015] Tarefa "Analisar solicitação"
Responsável: Fila DICOF (papel 1145)
Config: ConfirmaResponsabilidade=true

### [335016] Tarefa "Analisar solicitação"
Responsável: Fila Disec (papel 790)
Config: ConfirmaResponsabilidade=true

### [335017] Tarefa "Verificar Solicitação Com Aprovação."
Responsável: Fila Cesec - V360 (papel 1268)
Config: Codigo=VERIFICASOLIC; ConfirmaResponsabilidade=true
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- Operação PR0002 Aprovar
  - (aprovação) SIM_NAO "Aprovado?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO]
  - aprovador: Gestor do Cliente (Unico)

### [335018] EventoIntermediarioMensagem "Aviso Sobre Abertura de Ordem de Serviço"
Config: ListaDestinatarios=bruno.prado@bbts.com.br; AnexarTodosDocumentos=true
ModeloComunicado: Aviso de abertura de chamado
Corpo do comunicado: Prezado(a),
Foi aberta a ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [335019] EventoInicial ""
Responsável: Cliente (papel 18)
TipoSolicitacao: 30.04. Suprimentos Corporativos, Licitações e Contratos - Recebimento de de documentos para pagamento de Fornecedores
**ScriptInicio**
```python
s = OrdemServico.Servico.ClasseServicoId
if s == 291:
    OrdemServico.CancelaAprovacao('VERIFICASOLIC')
```
**ScriptFormCarregado**
```python
Formulario["COMBOBOX1"].Itens = "Sim;Não"
Formulario["CURSO"].Visivel = False
Formulario["CURSO"].Habilitado = False

if Formulario["COMBOBOX1"].Valor == "Sim":
    Formulario["CURSO"].Habilitado = True
    Formulario["CURSO"].Visivel = True
    
if Formulario["COMBOBOX1"].Valor == "Não":
    Formulario["CURSO"].Habilitado = False
    Formulario["CURSO"].Visivel = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos
  - COMBOBOX1 "Esse chamado esta relacionado a algum outro chamado aberto?" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
**COMBOBOX1.ScriptModificado**
```python
Formulario["COMBOBOX1"].Itens = "Sim;Não"
Formulario["CURSO"].Visivel = False
Formulario["CURSO"].Habilitado = False

if Formulario["COMBOBOX1"].Valor == "Sim":
    Formulario["CURSO"].Habilitado = True
    Formulario["CURSO"].Visivel = True
    
if Formulario["COMBOBOX1"].Valor == "Não":
    Formulario["CURSO"].Habilitado = False
    Formulario["CURSO"].Visivel = False
```
  - CURSO "Número do chamado (caso haja mais de um chamado, separe-os por ponto e vírgula):" [TextBox String → CP_ORDEM_SERVICO.CURSO]
  - ID_MEDICAO "ID de medição" [TextBox String → CPE_CONTRATOS02.ID_MEDICAO]
  - ID_DOCUMENTOS_FISCAIS "ID de documentos fiscais" [TextBox String → CPE_CONTRATOS02.ID_DOCUMENTOS_FISCAIS]
  - DescricaoDetalhada (nativo) obrigatório

### [335020] EventoIntermediarioMensagem "Aviso sobre Abertura de Chamado"
Config: ListaDestinatarios=ivanilson.dias@bbts.com.br
ModeloComunicado: Aviso de abertura de chamado
Corpo do comunicado: Prezado(a),
Foi aberta a ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [335021] EventoIntermediarioMensagem "Aviso Sobre Abertura de Ordem de Serviço"
Config: ListaDestinatarios=contratos@bbts.com.br;alineladislau.silva@bbts.com.br; AnexarTodosDocumentos=true
ModeloComunicado: Aviso de abertura de chamado
Corpo do comunicado: Prezado(a),
Foi aberta a ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [335022] EventoIntermediarioMensagem "Ordem de serviço finalizada"
Destinatário: Cliente (papel 18)
ModeloComunicado: Fale com a V360
Corpo do comunicado: Prezado(a),
A Ordem de Serviço nº OrdemServico.Numero sobre o Assunto: OrdemServico.Assunto foi atendido com sucesso!
Solução informada: 
OrdemServico.Customizado.OBS24 
Para maiores informações:
Link.Consulta .
Caso ainda tenha dúvidas, abra um novo Fale com a V360 referenciando esta ordem de serviço.
Atenciosamente,
Central de Serviços

### [335023] Tarefa "Informar Solução"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - OBS24 "Informar Solução" [Memo String(2000) → CPE_CSC.OBS24] obrigatório

### [335024] Tarefa "Informar Solução"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - OBS24 "Informar Solução" [Memo String(2000) → CPE_CSC.OBS24] obrigatório

### [335025] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [335026] Tarefa "Informar Solução"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - OBS24 "Informar Solução" [Memo String(2000) → CPE_CSC.OBS24] obrigatório

### [335027] EventoIntermediarioMensagem "Ordem de serviço finalizada"
Destinatário: Cliente (papel 18)
ModeloComunicado: Fale com a V360
Corpo do comunicado: Prezado(a),
A Ordem de Serviço nº OrdemServico.Numero sobre o Assunto: OrdemServico.Assunto foi atendido com sucesso!
Solução informada: 
OrdemServico.Customizado.OBS24 
Para maiores informações:
Link.Consulta .
Caso ainda tenha dúvidas, abra um novo Fale com a V360 referenciando esta ordem de serviço.
Atenciosamente,
Central de Serviços

### [335028] Tarefa "Verificar Solicitação"
Responsável: Fila Cesec - V360 (papel 1268)

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
### papel 1145: Fila DICOF
Tipo=RelacaoPessoas | pessoas: Fila Gestão de Contratos
### papel 790: Fila Disec
Tipo=RelacaoPessoas | pessoas: Fila - Disec
### papel 1268: Fila Cesec - V360
Tipo=RelacaoPessoas | pessoas: Fila Cesec - V360
### papel 753: Gestor do Cliente
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.Cliente.Orgao.GestorId.ToString() == OrdemServico.ClienteId.ToString():
    Atores.Add(OrdemServico.Cliente.Orgao.OrgaoPai.Gestor)
else:
    Atores.Add(OrdemServico.Cliente.ObtemChefia(False))
```

## Campos customizados usados (definição global)

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### COMBOBOX1 — Chamado Aberto?
DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1

### CURSO — Curso
TextBox String → CP_ORDEM_SERVICO.CURSO

### ID_MEDICAO — ID_MEDICAO
TextBox String → CPE_CONTRATOS02.ID_MEDICAO

### ID_DOCUMENTOS_FISCAIS — ID_DOCUMENTOS_FISCAIS
TextBox String → CPE_CONTRATOS02.ID_DOCUMENTOS_FISCAIS

### OBS24 — Observação24
Memo String(2000) → CPE_CSC.OBS24

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
