# Fluxo: Fale com a V360 (FALEV360) — versão 1
Caminho: Fluxos > ativação teste Versão 1 Fale com a V360
XML: `XMLs para teste/ativação_teste_Versão_1_Fale_com_a_V360.xml` | Supravizio 19.1.1 | SubProcessoId 20976 | DesenhoProcessoId 2940 | ProcessoId 768
Órgão dono: 3000003140 - DIVISAO DE GESTAO DE CONTRATOS COM FORNECEDORES | Responsável: MONICA GUIZZARDI VAILLANT
Classe do subprocesso: Objetivo=Fale com a V360; DescricaoCliente=Fale com a V360; CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Divergência entre a nota fiscal e a ordem de compra (DIVERGENCIANFOC); Divergência entre a nota fiscal e os tributos da base (DIVERGENCIANFTB); Medição não localizada (MEDLOCALIZA); Pendências no instrumento de Medição. (PENDENCIAMEDICAO); Erro na consulta de autenticidade (ERROCONAUTEN); Outros (OUTROS); Ingresso de Nota Fiscal (INGRESSONF); Compras Diretas (COMPRASDIRETASV360); Contas Concessionárias (CONTASCONCESSIONARIAS); Faturas de Aluguéis e condomínio (FATURAAC); Nota Técnica (NOTATECNICAV360); PDPEP (PDPEP); Acesso a V360 (ACESSOAV360)

## Grafo do fluxo
- [334583] EventoFinal "" {Responsável atual} → (fim)
- [334584] EventoFinal "" {Responsável atual} → (fim)
- [334585] EventoIntermediarioMensagem "Ordem de serviço finalizada" → [334584] 
- [334586] Tarefa "Analisar solicitação" {Fila DICOF} → [334590] Informar Solução
- [334587] Tarefa "Analisar solicitação" {Fila Disec} → [334588] Informar Solução
- [334592] Tarefa "Verificar Solicitação Com Aprovação." {Fila Cesec - V360} → [G75962] Informe o responsável por sanar a dúvida do client
- [334593] EventoIntermediarioMensagem "Aviso Sobre Abertura de Ordem de Serviço" → [334587] Analisar solicitação
- [334594] EventoInicial "" {Cliente} → [334595] Aviso sobre Abertura de Chamado
- [334595] EventoIntermediarioMensagem "Aviso sobre Abertura de Chamado" → [G75964] É solicitação de Acesso ao V360?
- [334596] EventoIntermediarioMensagem "Aviso Sobre Abertura de Ordem de Serviço" → [334586] Analisar solicitação
- [334597] EventoIntermediarioMensagem "Ordem de serviço finalizada" → [334589] 
- [334598] Tarefa "Informar Solução" {Responsável atual} → [334585] Ordem de serviço finalizada
- [334588] Tarefa "Informar Solução" {Responsável atual} → [334591] Ordem de serviço finalizada
- [334589] EventoFinal "" {Responsável atual} → (fim)
- [334590] Tarefa "Informar Solução" {Responsável atual} → [334597] Ordem de serviço finalizada
- [334591] EventoIntermediarioMensagem "Ordem de serviço finalizada" → [334583] 
- [334609] Tarefa "Verificar Solicitação" {Fila Cesec - V360} → [G75962] Informe o responsável por sanar a dúvida do client
- [G75964] Gateway "É solicitação de Acesso ao V360?" → «Não» [334609] Verificar Solicitação | «Sim» [334592] Verificar Solicitação Com Aprovação.
- [G75962] Gateway "Informe o responsável por sanar a dúvida do cliente" → «Cesec Cont» [334598] Informar Solução | «Gesuc/Dicof» [334596] Aviso Sobre Abertura de Ordem de Serviço | «Gesap/Disec» [334593] Aviso Sobre Abertura de Ordem de Serviço

## Gateways
### [G75964] É solicitação de Acesso ao V360? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == 'ACESSOAV360'
```
- alternativa → [334609] Verificar Solicitação: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
- alternativa → [334592] Verificar Solicitação Com Aprovação.: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
### [G75962] Informe o responsável por sanar a dúvida do cliente (EventBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("VERIFICASOLIC")
```
- alternativa → [334598] Informar Solução: OperadorDecision=Equal; ReferenciaDecision=Cesec Cont; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
1
```
- alternativa → [334596] Aviso Sobre Abertura de Ordem de Serviço: OperadorDecision=Equal; ReferenciaDecision=Gesuc/Dicof; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
2
```
- alternativa → [334593] Aviso Sobre Abertura de Ordem de Serviço: OperadorDecision=Equal; ReferenciaDecision=Gesap/Disec; SequenciaAvaliacao=2
**ValorComparacaoDecision**
```python
3
```

## Atividades

### [334583] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [334584] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [334585] EventoIntermediarioMensagem "Ordem de serviço finalizada"
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

### [334586] Tarefa "Analisar solicitação"
Responsável: Fila DICOF (papel 1145)
Config: ConfirmaResponsabilidade=true

### [334587] Tarefa "Analisar solicitação"
Responsável: Fila Disec (papel 790)
Config: ConfirmaResponsabilidade=true

### [334592] Tarefa "Verificar Solicitação Com Aprovação."
Responsável: Fila Cesec - V360 (papel 1268)
Config: Codigo=VERIFICASOLIC; ConfirmaResponsabilidade=true
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- Operação PR0002 Aprovar
  - aprovador: Gestor do Cliente (Unico)

### [334593] EventoIntermediarioMensagem "Aviso Sobre Abertura de Ordem de Serviço"
Config: ListaDestinatarios=bruno.prado@bbts.com.br; AnexarTodosDocumentos=true
ModeloComunicado: Aviso de abertura de chamado
Corpo do comunicado: Prezado(a),
Foi aberta a ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [334594] EventoInicial ""
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

### [334595] EventoIntermediarioMensagem "Aviso sobre Abertura de Chamado"
Config: ListaDestinatarios=ivanilson.dias@bbts.com.br
ModeloComunicado: Aviso de abertura de chamado
Corpo do comunicado: Prezado(a),
Foi aberta a ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [334596] EventoIntermediarioMensagem "Aviso Sobre Abertura de Ordem de Serviço"
Config: ListaDestinatarios=contratos@bbts.com.br;alineladislau.silva@bbts.com.br; AnexarTodosDocumentos=true
ModeloComunicado: Aviso de abertura de chamado
Corpo do comunicado: Prezado(a),
Foi aberta a ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [334597] EventoIntermediarioMensagem "Ordem de serviço finalizada"
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

### [334598] Tarefa "Informar Solução"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - OBS24 "Informar Solução" [Memo String(2000) → CPE_CSC.OBS24] obrigatório

### [334588] Tarefa "Informar Solução"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - OBS24 "Informar Solução" [Memo String(2000) → CPE_CSC.OBS24] obrigatório

### [334589] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [334590] Tarefa "Informar Solução"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - OBS24 "Informar Solução" [Memo String(2000) → CPE_CSC.OBS24] obrigatório

### [334591] EventoIntermediarioMensagem "Ordem de serviço finalizada"
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

### [334609] Tarefa "Verificar Solicitação"
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
Tipo=RelacaoPessoas
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
