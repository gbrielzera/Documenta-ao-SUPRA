# Fluxo: Esteira de Processos - Time Desenvolvimento e Automação da Gesap (TIMEDEVCSC) — versão 14
Caminho: Fluxos > Administração - Alteração e Criação de Subprocessos e Relatórios Versão 14 Esteira de Processos - Time Desenvolvimento e Automação da Gesap
XML: `XMLs para teste/Administração_-_Alteração_e_Criação_de_Subprocessos_e_Relatórios_Versão_14_Esteira_de_Processos_-_Time_Desenvolvimento_e_Automação_da_Gesap.xml` | Supravizio 19.1.1 | SubProcessoId 21080 | DesenhoProcessoId 2948 | ProcessoId 423
Órgão dono: 3000009430 - DIVISAO DE GERENCIAMENTO DOS SERVICOS COMPARTILHADOS | Responsável: LUCAS DA SILVA DURAO OLIVEIRA
Classe do subprocesso: Objetivo=Esteira de Processos - Time Desenvolvimento CSC; DescricaoCliente=Esteira de Processos - Time Desenvolvimento e Automação da Gesap; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Esteira de Processos - Time Desenvolvimento e Automação da Gesap (TIMEDESENVCSC)

## Grafo do fluxo
- [341088] LinkInicial "" {Cliente} → [336115] Aviso de Abertura de OS
- [339739] EventoIntermediarioMensagem "Ajuste de informações" → [339738] Ajustar a demanda
- [339738] Tarefa "Ajustar a demanda" {Cliente} → [336111] Verificar e direcionar solicitação.
- [336108] Tarefa "Homologar a solução junto ao cliente" {Responsável atual} → [G76205] Aprovado pelo cliente?
- [336109] Tarefa "Desenvolver a solicitação" {Responsável atual} → [336108] Homologar a solução junto ao cliente
- [336110] Tarefa "Levantar requisito e mapear solicitaçãos junto ao cliente." {Favorecido Cobra} → [336109] Desenvolver a solicitação
- [336111] Tarefa "Verificar e direcionar solicitação." {Gestor Time Desenvolvimento Gesap} → [G76898] A solicitação precisa de ajustes?
- [336112] EventoIntermediarioMensagem "Aviso de Processo Finalizado" → [336113] 
- [336113] EventoFinal "" → (fim)
- [336115] EventoIntermediarioMensagem "Aviso de Abertura de OS" → [336111] Verificar e direcionar solicitação.
- [336114] EventoInicial "" {Cliente} → [336115] Aviso de Abertura de OS
- [G76205] Gateway "Aprovado pelo cliente?" → «Não» [336109] Desenvolver a solicitação | «Sim» [336112] Aviso de Processo Finalizado
- [G76898] Gateway "A solicitação precisa de ajustes?" → «Não» [336110] Levantar requisito e mapear solicitaçãos junto ao  | «Sim» [339739] Ajuste de informações

## Gateways
### [G76205] Aprovado pelo cliente? (EventBasedExclusiveDecision)
- alternativa → [336109] Desenvolver a solicitação: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não; RotuloMotivo=Não (Precisa de ajuste)
- alternativa → [336112] Aviso de Processo Finalizado: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim; RotuloMotivo=Sim
### [G76898] A solicitação precisa de ajustes? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico['SIM_NAO10'] == "Sim"
```
- alternativa → [336110] Levantar requisito e mapear solicitaçãos junto ao : SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [339739] Ajuste de informações: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```

## Atividades

### [341088] LinkInicial ""
Responsável: Cliente (papel 18)
Config: TipoMensagem=MensagemProcesso
**ScriptInicio**
```python
AvancaProximaAtividade = True
OrdemServico.AdicionaComentario(OrdemServico.Servico.Sigla.ToString() ,False)
OrdemServico.AdicionaComentario(OrdemServico.Responsavel.ToString() ,False)
```
**ScriptFormCarregado**
```python
Formulario['LABEL10'].Valor = '<br><br><div style="display: flex; align-items: center; text-align: center;"><span style="flex: 1; border-bottom: 1px solid blue; margin-right: .25em; margin: 0 5%;"></span> <span style="font-size: 16px; color: red; margin: 0 15px; font-weight: 800;"> DETALHAMENTO DA SOLICITAÇÃO </span>  <span style="flex: 1; border-bottom: 1px solid blue; margin-left: .25em; margin: 0 5%;"></span></div><br><br>'

#Formulario['COMBOBOX_II'].Visivel = False
#Formulario['COMBOBOX_II'].Habilitado = False
#
#Formulario['COMBOBOX_I'].Itens = 'Automação; Dados; Desenvolvimento; Fluxos (Cesec)'
#Formulario['COMBOBOX_I'].Valor = 'Fluxos (Cesec)'
#Formulario['COMBOBOX_II'].Valor = 'Criação/Alteração de Fluxos no Supravizio'
#
#if Formulario['SIM_NAO'].Valor != 'Sim':
#    Formulario['JUSTIFICATIVA5'].Visivel = False
#

if Formulario['JUSTIFICATIVA5'].Valor == '':
    Formulario['JUSTIFICATIVA5'].Valor = 'Não necessário'

Formulario['COMBOBOX_I'].Habilitado = False
Formulario['COMBOBOX_II'].Habilitado = False
Formulario['SIM_NAO'].Habilitado = False
Formulario['JUSTIFICATIVA5'].Habilitado = False
Formulario['CAMINHO_SUBPROCESSO'].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - LABEL10 "LABEL10" [Label String(700) → CPE_PDCI2019.LABEL10]
  - SIM_NAO "A solicitação impacta nas operações do Cesec?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO]
  - COMBOBOX_I "Qual a categoria da solicitação?" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_I]
  - COMBOBOX_II "Tipo de Solicitação" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_II]
  - CAMINHO_SUBPROCESSO "Caminho do Subprocesso" [Memo String → CPE_ORDEM_SERVICO.CAMINHO_SUBPROCESSO] obrigatório
  - JUSTIFICATIVA5 "Justificativa DISEC" [Memo String → CPE_CONTRATOS02.JUSTIFICATIVA5]
- Associação de subprocesso: AssociacaoId=1633; Nome=LUCAS DA SILVA DURAO OLIVEIRA; FraseAssociacao=Disec --> Time desenvolvimento Gesap

### [339739] EventoIntermediarioMensagem "Ajuste de informações"
Destinatário: Cliente (papel 18)
ModeloComunicado: Ajuste de informações GESAP
Corpo do comunicado: Prezado(a),
Informamos que o chamado foi devolvido para ajustes conforme mensagem abaixo.
 OrdemServico.Customizado.DESCRICAO_RESUMIDA 
Para maiores informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [339738] Tarefa "Ajustar a demanda"
Responsável: Cliente (papel 18)
**ScriptFormCarregado**
```python
lista = [ "COMBOBOX_I", "COMBOBOX_II", "DESCRICAO_DETALHADA" ]

Formulario['COMBOBOX_I'].Itens = 'Automação; Dados; Desenvolvimento'
Formulario['DESCRICAO_RESUMIDA'].Habilitado = False

for item in lista:
    Formulario[item].Habilitado = True
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexos (Se necessário)" classes: Arquivo — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos
  - DESCRICAO_RESUMIDA "Explique o que precisa ser alterado" [Memo String(200) → CPE_BOOTCAMP.DESCRICAO_RESUMIDA] obrigatório
  - COMBOBOX_I "Qual a categoria da solicitação?" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_I] obrigatório
**COMBOBOX_I.ScriptModificado**
```python
if Formulario['COMBOBOX_I'].Valor == "Dados":
    Formulario['COMBOBOX_II'].Itens = "Criação; Alteração; Manutenção de um processo já existente"

elif Formulario['COMBOBOX_I'].Valor == "Automação":
    Formulario['COMBOBOX_II'].Itens = 'Criação; Alteração; Manutenção de um processo já existente'
    
elif Formulario['COMBOBOX_I'].Valor == "Desenvolvimento":
    Formulario['COMBOBOX_II'].Itens = 'Criação; Alteração; Manutenção de um processo já existente'
    
else:
    Formulario['COMBOBOX_II'].Valor == "Não encontrado..."
    

    
Formulario['COMBOBOX_II'].Visivel = True
Formulario['COMBOBOX_II'].Habilitado = True
```
  - COMBOBOX_II "Tipo de Solicitação" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_II] obrigatório — Coluna=2
  - LABEL10 "LABEL10" [Label String(700) → CPE_PDCI2019.LABEL10] obrigatório
  - DESCRICAO_DETALHADA "Descreva DETALHADAMENTE sua demanda" [Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório

### [336108] Tarefa "Homologar a solução junto ao cliente"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - OBS11 "Anotações da reunião (Não obrigatório)" [Memo String(2000) → CPE_CSC.OBS11]

### [336109] Tarefa "Desenvolver a solicitação"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - OBS11 "Observações (Não Obrigatório):" [Memo String(2000) → CPE_CSC.OBS11]

### [336110] Tarefa "Levantar requisito e mapear solicitaçãos junto ao cliente."
Responsável: Favorecido Cobra (papel 277)
- Operação PR0001 Preencher Campos
  - DATA1 "Data início do desenvolvimento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA1] obrigatório
  - COMPLEXIDADE "Complexidade" [DropDownList String → CP_ORDEM_SERVICO.COMPLEXIDADE] obrigatório — Coluna=2
  - OBS11 "Observação do Desenvolvedor (Não obrigatório)" [Memo String(2000) → CPE_CSC.OBS11]

### [336111] Tarefa "Verificar e direcionar solicitação."
Responsável: Gestor Time Desenvolvimento Gesap (papel 1452)
**ScriptInicio**
```python
OrdemServico.AdicionaComentario(OrdemServico.Servico.Sigla, False)
```
**ScriptFormCarregado**
```python
campos1 = ['COMBOBOX_I', 'COMBOBOX_II']
campos = ['COMBOBOX_I', 'COMBOBOX_II', 'DESCRICAO_DETALHADA', 'SIM_NAO', "JUSTIFICATIVA5", "DESCRICAO_RESUMIDA"]

if OrdemServico.Servico.Sigla == "TIMEDESENVCSC":
    for i in campos1:
        Formulario[i].Visivel = False

else:
    # Fluxo original
    Formulario["SIM_NAO"].Visivel = False
    Formulario["JUSTIFICATIVA5"].Visivel = False
    Formulario["DESCRICAO_RESUMIDA"].Visivel = False
    for i in campos:
        Formulario[i].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - FAVORECIDO_COBRA "Atribuir a qual funcionário" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - DESCRICAO_RESUMIDA "Explique o que precisa ser alterado pelo cliente" [Memo String(200) → CPE_BOOTCAMP.DESCRICAO_RESUMIDA] obrigatório
    - coluna AGENCIA obrigatório
    - coluna CONTA_CORR obrigatório
    - coluna TIPO_CHAVE obrigatório
    - coluna CHAVE_PIX obrigatório
    - coluna BANCO obrigatório
- Operação PR0001 Preencher Campos
  - COMBOBOX_I "Qual a categoria da solicitação?" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_I] obrigatório
**COMBOBOX_I.ScriptModificado**
```python
if Formulario['COMBOBOX_I'].Valor == "Dados":
    Formulario['COMBOBOX_II'].Itens = "Criação; Alteração; Manutenção de um processo já existente"

elif Formulario['COMBOBOX_I'].Valor == "Automação":
    Formulario['COMBOBOX_II'].Itens = 'Criação; Alteração; Manutenção de um processo já existente'
    
elif Formulario['COMBOBOX_I'].Valor == "Desenvolvimento":
    Formulario['COMBOBOX_II'].Itens = 'Criação; Alteração; Manutenção de um processo já existente'
    
else:
    Formulario['COMBOBOX_II'].Valor == "Não encontrado..."
    

    
Formulario['COMBOBOX_II'].Visivel = True
Formulario['COMBOBOX_II'].Habilitado = True
```
  - COMBOBOX_II "Tipo de Solicitação" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_II] obrigatório — Coluna=2
  - SIM_NAO10 "A solicitação precisa de Ajustes por parte do Cliente?" [DropDownList String → CPE_CSC.SIM_NAO10] obrigatório — Coluna=3
**SIM_NAO10.ScriptModificado**
```python
if Formulario['SIM_NAO10'].Valor == "Sim":
    Formulario['DESCRICAO_RESUMIDA'].Visivel = True
    Formulario['DESCRICAO_RESUMIDA'].Habilitado = True
else:
    Formulario['DESCRICAO_RESUMIDA'].Visivel = False
    Formulario['DESCRICAO_RESUMIDA'].Habilitado = False
```
  - SIM_NAO "A solicitação impacta nas operações do Cesec?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório — Coluna=3
  - LABEL10 "LABEL10" [Label String(700) → CPE_PDCI2019.LABEL10] obrigatório
  - DESCRICAO_DETALHADA "Descreva DETALHADAMENTE sua demanda" [Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório
  - JUSTIFICATIVA5 "Justificativa da Disec" [Memo String → CPE_CONTRATOS02.JUSTIFICATIVA5] obrigatório

### [336112] EventoIntermediarioMensagem "Aviso de Processo Finalizado"
Destinatário: Gestor Time Desenvolvimento Gesap (papel 1452)
ModeloComunicado: Aviso de Finalização de Chamado
Corpo do comunicado: Prezado(a),
Foi finalizado a ordem de serviço n°: OrdemServico.Numero referente ao Serviço OrdemServico.Assunto.
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [336113] EventoFinal ""

### [336115] EventoIntermediarioMensagem "Aviso de Abertura de OS"
Destinatário: Gestor Time Desenvolvimento Gesap (papel 1452)
ModeloComunicado: Abertura de Chamado - Time dev Gesap
Corpo do comunicado: Prezado,
Foi aberta a Ordem de Serviço nº OrdemServico.Numero referente ao assunto: OrdemServico.SubProcesso .
Descrição Detalhada da Solicitação:
 OrdemServico.Customizado.DESCRICAO_DETALHADA 
==============================================
Para maiores informações Link.Workspace 
Atenciosamente,
Central de Serviços

### [336114] EventoInicial ""
Responsável: Cliente (papel 18)
Config: Configuracao={"ServicoIniciador":"TIMEDESENVCSC"}
TipoSolicitacao: 00.03. Administração e Patrimônio - Criação/Alteração de Subprocessos e Relatórios na Central de Serviços
**ScriptValidacao**
```python
if len(OrdemServico.GetCustom('DESCRICAO_DETALHADA')) < 150:
    Criticas.AdicionaPendencia('Por favor, detalhe mais a sua solicitação.\n Quanto mais detalhada ela for, mais rápido será o desenvolvimento da solução.\n(Mínimo 150 caracteres)')
```
**ScriptFormCarregado**
```python
Formulario['LABEL1'].Valor = "<div style='display: flex; justify-content: center; align-items: center;'><div style='display: flex; align-items: center; width: 100%; background: linear-gradient(90deg, blue, rgb(2, 0, 18)); border-radius: 16px; padding: 2%;'><br><p style='flex: 1; text-align: center; color: yellow; font-weight: 600; font-size: 16px; font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif; margin: 0;'>-- ATENÇÃO -- <br><br>A solicitação desse fluxo é exclusivo da GESAP para melhoria de processos internos (Fora do Supravizio).<br>Para solicitações sobre Criação / Melhoria de Fluxos / Relatórios do Supravizio, por favor, volte um passo e selecione esse serviço:   <br><br> <strong style='color: azure; font-size: 18px;'>--> Criação/Alteração de Subprocessos e Relatórios na Central de Serviços</strong> <br></p></div></div><br><br>"

Formulario['LABEL10'].Valor = '<br><br><div style="display: flex; align-items: center; text-align: center;"><span style="flex: 1; border-bottom: 1px solid blue; margin-right: .25em; margin: 0 5%;"></span> <span style="font-size: 16px; color: red; margin: 0 15px; font-weight: 800;"> DETALHAMENTO DA SOLICITAÇÃO </span>  <span style="flex: 1; border-bottom: 1px solid blue; margin-left: .25em; margin: 0 5%;"></span></div><br><br>'

Formulario['COMBOBOX_II'].Visivel = False
Formulario['COMBOBOX_II'].Habilitado = False

Formulario['COMBOBOX_I'].Itens = 'Automação; Dados; Desenvolvimento'
```
- Operação PR0001 Preencher Campos
  - LABEL1 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - COMBOBOX_I "Qual a categoria da solicitação?" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_I] obrigatório
**COMBOBOX_I.ScriptModificado**
```python
if Formulario['COMBOBOX_I'].Valor == "Dados":
    Formulario['COMBOBOX_II'].Itens = "Criação; Alteração; Manutenção de um processo já existente"

elif Formulario['COMBOBOX_I'].Valor == "Automação":
    Formulario['COMBOBOX_II'].Itens = 'Criação; Alteração; Manutenção de um processo já existente'
    
elif Formulario['COMBOBOX_I'].Valor == "Desenvolvimento":
    Formulario['COMBOBOX_II'].Itens = 'Criação; Alteração; Manutenção de um processo já existente'
    
else:
    Formulario['COMBOBOX_II'].Valor == "Não encontrado..."
    

    
Formulario['COMBOBOX_II'].Visivel = True
Formulario['COMBOBOX_II'].Habilitado = True
```
  - COMBOBOX_II "Tipo de Solicitação" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_II] obrigatório — Coluna=2
  - LABEL10 "LABEL10" [Label String(700) → CPE_PDCI2019.LABEL10] obrigatório
  - DESCRICAO_DETALHADA "Descreva DETALHADAMENTE sua demanda" [Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexos (Se necessário)" classes: Arquivo — RequeridoInicial=true; PermiteMultiplosItens=true; IncluirPaginaAssinatura=true
- ClientesAutorizados:
  - PapelProcessoId=66791; PapelAutorizado=Time Desenvolvimento GESAP

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
### papel 277: Favorecido Cobra
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.GetCustom("FAVORECIDO_COBRA"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))

    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```
### papel 1452: Gestor Time Desenvolvimento Gesap
Tipo=RelacaoPessoas | pessoas: LUCAS DA SILVA DURAO OLIVEIRA

## Campos customizados usados (definição global)

### LABEL10 — LABEL10
Label String(700) → CPE_PDCI2019.LABEL10

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### COMBOBOX_I — COMBOBOX_I
DropDownList String → CPE_BOOTCAMP.COMBOBOX_I

### COMBOBOX_II — COMBOBOX_II
DropDownList String → CPE_BOOTCAMP.COMBOBOX_II

### CAMINHO_SUBPROCESSO — Caminho do Subprocesso
Memo String → CPE_ORDEM_SERVICO.CAMINHO_SUBPROCESSO

### JUSTIFICATIVA5 — Justificativa5
Memo String → CPE_CONTRATOS02.JUSTIFICATIVA5

### DESCRICAO_RESUMIDA — Informar UOR de destino/Nome do Gestor/Função
Memo String(200) → CPE_BOOTCAMP.DESCRICAO_RESUMIDA
Descrição: Informar UOR

### DESCRICAO_DETALHADA — Descrição detalhada
Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA

### OBS11 — Observação11
Memo String(2000) → CPE_CSC.OBS11

### DATA1 — Data
DatePicker DateTime → CP_ORDEM_SERVICO.DATA1

### COMPLEXIDADE — Complexidade
DropDownList String → CP_ORDEM_SERVICO.COMPLEXIDADE
Itens: Baixa;Média;Alta

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### SIM_NAO10 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO10
Itens: Sim;Não

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
