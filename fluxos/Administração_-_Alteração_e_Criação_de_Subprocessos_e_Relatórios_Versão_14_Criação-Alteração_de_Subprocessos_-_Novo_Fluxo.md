# Fluxo: Criação/Alteração de Subprocessos - Novo Fluxo (SUBPROCESSOS) — versão 14
Caminho: Fluxos > Administração - Alteração e Criação de Subprocessos e Relatórios Versão 14 Criação-Alteração de Subprocessos - Novo Fluxo
XML: `XMLs para teste/Administração_-_Alteração_e_Criação_de_Subprocessos_e_Relatórios_Versão_14_Criação-Alteração_de_Subprocessos_-_Novo_Fluxo.xml` | Supravizio 19.1.1 | SubProcessoId 21085 | DesenhoProcessoId 2948 | ProcessoId 423
Órgão dono: 3000009430 - DIVISAO DE GERENCIAMENTO DOS SERVICOS COMPARTILHADOS | Responsável: ADIR CORDEIRO DOS SANTOS FILHO T
Classe do subprocesso: Objetivo=Criação/Alteração de Subprocessos e Relatórios na Central de Serviços; DescricaoCliente=Criação/Alteração de Subprocessos e Relatórios na Central de Serviços; CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Criação/Alteração de Subprocessos e Relatórios na Central de Serviços; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Solicitar confecção de relatórios da Central de Serviços (RELATORIOS); Criação de novos subprocessos (SUBPROCESSOS); Solicitar alteração de subprocessos  (ALTERARSUB); Indisponibilidade, falhas ou erros (INDISFALHASOUERROS)

## Grafo do fluxo
- [336321] EventoFinal "" → (fim)
- [336322] EventoIntermediarioMensagem "Aviso de Cancelamento de Chamado" → [336321] 
- [336143] EventoFinal "" → (fim)
- [336144] SubProcesso "" {Gestor Time Desenvolvimento Gesap} → [336143] 
- [336146] LinkInicial "" → [336156] Verificar e direcionar solicitação.
- [336149] Tarefa "Indicar o responsável" {Responsável atual} → [336157] Aviso sobre abertura de ordem de serviço
- [336150] EventoFinal "" {Responsável atual} → (fim)
- [336156] Tarefa "Verificar e direcionar solicitação." {Fila Disec} → [G76235] Mandar pro time de desenvolvimento ou cancelar
- [336157] EventoIntermediarioMensagem "Aviso sobre abertura de ordem de serviço" → [336159] Confeccionar Relatório
- [336158] EventoIntermediarioMensagem "Confecção de Relatórios" → [336150] 
- [336159] Tarefa "Confeccionar Relatório" {Favorecido Cobra} → [336162] Confecção de Relatórios
- [336160] Tarefa "Analisar solicitação" {Fila Disec} → [336149] Indicar o responsável
- [336162] EventoIntermediarioMensagem "Confecção de Relatórios" → [336158] Confecção de Relatórios
- [336163] EventoInicial "" {Cliente} → [G76213] Enviar a solicitação para o Time de Desenvolviment
- [341102] LinkInicial "" → [336144] 
- [G76213] Gateway "Enviar a solicitação para o Time de Desenvolvimento?" → «Não» [336144]  | «Sim» [G76215] Qual o serviço?
- [G76215] Gateway "Qual o serviço?" → «Relatórios» [336160] Analisar solicitação | «SubProcessos» [336156] Verificar e direcionar solicitação.
- [G76235] Gateway "Mandar pro time de desenvolvimento ou cancelar" → «Sim» [336144]  | «Cancelar» [336322] Aviso de Cancelamento de Chamado

## Gateways
### [G76213] Enviar a solicitação para o Time de Desenvolvimento? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico['SIM_NAO'] == 'Sim'
```
- alternativa → [336144] : SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [G76215] Qual o serviço?: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
### [G76215] Qual o serviço? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == "RELATORIOS"
```
- alternativa → [336160] Analisar solicitação: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Relatórios
**ValorComparacaoDecision**
```python
True
```
- alternativa → [336156] Verificar e direcionar solicitação.: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=SubProcessos
**ValorComparacaoDecision**
```python
False
```
### [G76235] Mandar pro time de desenvolvimento ou cancelar (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["SIM_NAO_100"] == 'Mandar para o time de Desenvolvimento'
```
- alternativa → [336144] : SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [336322] Aviso de Cancelamento de Chamado: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Cancelar
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [336321] EventoFinal ""
Config: TipoFinalizacao=NaoRealizado

### [336322] EventoIntermediarioMensagem "Aviso de Cancelamento de Chamado"
Destinatário: Cliente e Gerente Posição (papel 631)
ModeloComunicado: Chamado cancelado - Solicitação de Fluxos
Corpo do comunicado: Prezado(a),
O chamado OrdemServico.Numero - OrdemServico.Assunto foi cancelado. Verifique o motivo abaixo:
Motivo: OrdemServico.Customizado.JUSTIFICATIVA 
Para mais informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [336143] EventoFinal ""

### [336144] SubProcesso ""
Responsável: Gestor Time Desenvolvimento Gesap (papel 1452)
Config: AssociacaoId=1633; PassaTodosItens=true
- ValoresInputs:
  - PropertyId=1295; Property=Servico
  - CustomPropertyId=3872; CustomProperty=COMBOBOX_I
  - CustomPropertyId=3873; CustomProperty=COMBOBOX_II
  - CustomPropertyId=1002; CustomProperty=SIM_NAO
  - CustomPropertyId=1697; CustomProperty=LABEL10
  - CustomPropertyId=2164; CustomProperty=DESCRICAO_DETALHADA
  - CustomPropertyId=4580; CustomProperty=JUSTIFICATIVA5
- Associação: Ativo=true; FraseAssociacao=Disec --> Time desenvolvimento Gesap; FraseInversaAssociacao=Time desenvolvimento Gesap -> Disec; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=ENVIARPARATIMEDEV | fonte: Criação/Alteração de Subprocessos - Novo Fluxo → alvo: Esteira de Processos - Time Desenvolvimento e Automação da Gesap

### [336146] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - SUBPROCESSO_ATIVO "Selecione o Subprocesso: " [TextBox String → CPE_ORDEM_SERVICO.SUBPROCESSO_ATIVO] obrigatório
  - CAMINHO_SUBPROCESSO "Caminho do Subprocesso (Ex: 00 - Centro de Serviços Compartilhados -> 12.18. Serviços de TI - Telefonia Móvel -> 12.18. Serviços de TI - Telefonia Móvel -> Bloqueio)" [Memo String → CPE_ORDEM_SERVICO.CAMINHO_SUBPROCESSO] obrigatório
  - CSC_DATA_INICIO "Data Início" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO]
  - CSC_DATA_FIM "Data Fim" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM]
  - DescricaoDetalhada (nativo) obrigatório
  - Justificativa (nativo) "Justificativa: " obrigatório
- Associação de subprocesso: AssociacaoId=1566; Nome=ADIR CORDEIRO DOS SANTOS FILHO; FraseAssociacao=Entrada de Novas demandas --> Criação/Alteração

### [336149] Tarefa "Indicar o responsável"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - FAVORECIDO_COBRA "Indique o responsável para confecção do relatório" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório

### [336150] EventoFinal ""
Responsável: Responsável atual (papel 36)

### [336156] Tarefa "Verificar e direcionar solicitação."
Responsável: Fila Disec (papel 790)
**ScriptFormCarregado**
```python
Formulario['SIM_NAO_100'].Itens = 'Mandar para o time de Desenvolvimento; Cancelar (Informe o motivo)'
Formulario['JUSTIFICATIVA'].Visivel = False

campos = ['CAMINHO_SUBPROCESSO', 'SUBPROCESSO_ATIVO', "DESCRICAO_DETALHADA"]

for i in campos:
    Formulario[i].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - SUBPROCESSO_ATIVO "Selecione o Subprocesso: " [TextBox String → CPE_ORDEM_SERVICO.SUBPROCESSO_ATIVO] obrigatório
  - CAMINHO_SUBPROCESSO "Caminho do Subprocesso (Ex: 00 - Centro de Serviços Compartilhados -> 12.18. Serviços de TI - Telefonia Móvel -> 12.18. Serviços de TI - Telefonia Móvel -> Bloqueio)" [Memo String → CPE_ORDEM_SERVICO.CAMINHO_SUBPROCESSO] obrigatório
- Operação PR0001 Preencher Campos
  - SIM_NAO "A solicitação impacta nas operações do Cesec?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório — Coluna=3
  - LABEL10 "LABEL10" [Label String(700) → CPE_PDCI2019.LABEL10] obrigatório
  - DESCRICAO_DETALHADA "Descreva DETALHADAMENTE sua demanda" [Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório
- Operação PR0001 Preencher Campos
  - JUSTIFICATIVA "Justificativa do cancelamento" [Memo String(1999) → CPE_CSC.JUSTIFICATIVA] obrigatório
  - SIM_NAO_100 "Mandar para o time de desenvolvimento ou cancelar?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO_100] obrigatório
**SIM_NAO_100.ScriptModificado**
```python
if Formulario['SIM_NAO_100'].Valor == "Cancelar (Informe o motivo)":
    Formulario['JUSTIFICATIVA'].Visivel = True
    Formulario['JUSTIFICATIVA5'].Visivel = False
else:
    Formulario['JUSTIFICATIVA'].Visivel = False
    Formulario['JUSTIFICATIVA5'].Visivel = True
```
  - JUSTIFICATIVA5 "Justificativa da decisão de mandar para o Time de desenvolvimento" [Memo String → CPE_CONTRATOS02.JUSTIFICATIVA5] obrigatório

### [336157] EventoIntermediarioMensagem "Aviso sobre abertura de ordem de serviço"
Destinatário: Favorecido Cobra (papel 277)
ModeloComunicado: Aviso sobre Abertura de Chamado
Corpo do comunicado: Prezados(as),
Foi aberta a Ordem de Serviço nº OrdemServico.Numero referente ao assunto: OrdemServico.SubProcesso .
Descrição Detalhada:
OrdemServico.DescricaoDetalhada 
 OrdemServico.Customizado.DESCRICAO_OBRIG 
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [336158] EventoIntermediarioMensagem "Confecção de Relatórios"
Destinatário: Cliente (papel 18)
ModeloComunicado: Relatórios Disec
Corpo do comunicado: Segue em anexo, o relatório solicitado nesta OS.
Atenciosamente,
Central de Serviços.

### [336159] Tarefa "Confeccionar Relatório"
Responsável: Favorecido Cobra (papel 277)
- Operação PR0004 Associar Itens Configuração
  - anexo "Relatório" classes: Arquivo — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos
  - OBS10 "Observação (Não obrigatório)" [Memo String(2000) → CPE_CSC.OBS10]
  - OBS21 "Código" [Memo String(4000) → CPE_CSC.OBS21] obrigatório

### [336160] Tarefa "Analisar solicitação"
Responsável: Fila Disec (papel 790)
Config: ConfirmaResponsabilidade=true

### [336162] EventoIntermediarioMensagem "Confecção de Relatórios"
Destinatário: Cliente e Favorecido Cobra (papel 312)
Config: Configuracao={"ImpressaoImprimirAtividades":true, "ImpressaoImprimirAprov":false, "ImpressaoImprimirComent":true, "AnexaRelatorioImpressao":false}
ModeloComunicado: Confecção de Relatórios 2
Corpo do comunicado: Prezado(a) 
 OrdemServico.Cliente.Nome ,
Segue o relatório solicitado na ordem de serviço OrdemServico.Numero.
Atenciosamente,
Central de Serviços
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=1655; ClasseConfiguracao=Arquivo

### [336163] EventoInicial ""
Responsável: Cliente (papel 18)
TipoSolicitacao: 00.03. Administração e Patrimônio - Criação/Alteração de Subprocessos e Relatórios na Central de Serviços
**ScriptValidacao**
```python
if len(OrdemServico.GetCustom('DESCRICAO_DETALHADA')) < 150:
    Criticas.AdicionaPendencia('Por favor,\n Conte com mais detalhes a sua solicitação. (No mínimo 100 caracteres)')
```
**ScriptFormCarregado**
```python
if (OrdemServico.Servico.Sigla == "RELATORIOS"):
    Formulario['CAMPOS'].Habilitado = True
    Formulario['CAMPOS'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
else:
    Formulario['CAMPOS'].Habilitado = False
    Formulario['CAMPOS'].Visivel = False
    Formulario['CSC_DATA_INICIO'].Visivel = False
    Formulario['CSC_DATA_INICIO'].Habilitado = False
    Formulario['CSC_DATA_FIM'].Visivel = False
    Formulario['CSC_DATA_FIM'].Habilitado = False
    
    
    
if (OrdemServico.Servico.Sigla == "ALTERARSUB") or (OrdemServico.Servico.Sigla == "RELATORIOS"):
    Formulario['SUBPROCESSO_ATIVO'].Habilitado = True
    Formulario['SUBPROCESSO_ATIVO'].Visivel = True
    Formulario['SUBPROCESSO_SUPRAVIZIO'].Habilitado = False
    Formulario['SUBPROCESSO_SUPRAVIZIO'].Visivel = False
else:
    Formulario['SUBPROCESSO_ATIVO'].Habilitado = False
    Formulario['SUBPROCESSO_ATIVO'].Visivel = False
    Formulario['SUBPROCESSO_SUPRAVIZIO'].Habilitado = True
    Formulario['SUBPROCESSO_SUPRAVIZIO'].Visivel = True

    
    
if String.IsNullOrEmpty(Formulario['CAMPOS'].Valor):
    Formulario['CAMPOS'].Valor = "Ex: Ordem de Serviços, cliente, responsável, abertura, finalização, situação."

Formulario['LABEL10'].Valor = '<br><br><div style="display: flex; align-items: center; text-align: center;"><span style="flex: 1; border-bottom: 1px solid blue; margin-right: .25em; margin: 0 5%;"></span> <span style="font-size: 16px; color: red; margin: 0 15px; font-weight: 800;"> DETALHAMENTO DA SOLICITAÇÃO </span>  <span style="flex: 1; border-bottom: 1px solid blue; margin-left: .25em; margin: 0 5%;"></span></div><br><br>'

Formulario['COMBOBOX_I'].Habilitado = False
Formulario['COMBOBOX_I'].Valor = 'Fluxos (Cesec)'
Formulario['COMBOBOX_II'].Habilitado = False
Formulario['COMBOBOX_II'].Valor = 'Criação/Alteração de Fluxos no Supravizio'
```
- Operação PR0001 Preencher Campos
  - SUBPROCESSO_ATIVO "Selecione o Subprocesso: " [TextBox String → CPE_ORDEM_SERVICO.SUBPROCESSO_ATIVO] obrigatório
  - SUBPROCESSO_SUPRAVIZIO "Subprocesso (Para uma busca mais rápida, digite o nome do Subprocesso)" [TextBox String → CPE_CSC.SUBPROCESSO_SUPRAVIZIO] obrigatório
  - CAMINHO_SUBPROCESSO "Caminho do Subprocesso (Ex: 00 - Centro de Serviços Compartilhados -> 12.18. Serviços de TI - Telefonia Móvel -> 12.18. Serviços de TI - Telefonia Móvel -> Bloqueio)" [Memo String → CPE_ORDEM_SERVICO.CAMINHO_SUBPROCESSO] obrigatório
  - CAMPOS "Campos desejados no Relatório" [Memo String → CPE_ORDEM_SERVICO.CAMPOS] obrigatório
  - CSC_DATA_INICIO "Data Início" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO]
  - CSC_DATA_FIM "Data Fim" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM]
- Operação PR0004 Associar Itens Configuração
  - anexo "Desenho do Fluxo " classes: Arquivo — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Procedimento Operacional (POP)" classes: Arquivo 01 — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos
  - SIM_NAO "A solicitação impacta nas operações do Cesec?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório — Coluna=3
  - COMBOBOX_I "
Qual a categoria da solicitação?" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_I] obrigatório — Coluna=3
  - COMBOBOX_II "Tipo de Solicitação" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_II] — Coluna=3
  - LABEL10 "LABEL10" [Label String(700) → CPE_PDCI2019.LABEL10] obrigatório
  - DESCRICAO_DETALHADA "Descreva DETALHADAMENTE sua demanda" [Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório

### [341102] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Associação de subprocesso: AssociacaoId=1041; Nome=ADIR CORDEIRO DOS SANTOS FILHO; FraseAssociacao=Gestão da Qualidade -> Criação de Subprocesso

## Papéis usados
### papel 631: Cliente e Gerente Posição
Tipo=Composto
- composto por: Gerente Posição do Cliente (Script)
- composto por: Cliente (PessoaOrdemServico)
### papel 1452: Gestor Time Desenvolvimento Gesap
Tipo=RelacaoPessoas | pessoas: LUCAS DA SILVA DURAO OLIVEIRA
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```
### papel 790: Fila Disec
Tipo=RelacaoPessoas | pessoas: BRUNO DA SILVA RAMOS, BRUNO DA SILVA RAMOS_ 
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

## Campos customizados usados (definição global)

### SUBPROCESSO_ATIVO — Subprocesso
TextBox String → CPE_ORDEM_SERVICO.SUBPROCESSO_ATIVO
**LookupScript**
```python
#Itens = DB.ExecuteDataTable ("Select CLASSE_SUB_PROCESSO.DESCRICAO From CLASSE_SUB_PROCESSO Where CLASSE_SUB_PROCESSO.ATIVO = 'Sim' Order By CLASSE_SUB_PROCESSO.DESCRICAO_CLIENTE")
```

### CAMINHO_SUBPROCESSO — Caminho do Subprocesso
Memo String → CPE_ORDEM_SERVICO.CAMINHO_SUBPROCESSO

### CSC_DATA_INICIO — Data Início
DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO

### CSC_DATA_FIM — Data Fim
DatePicker DateTime → CPE_CSC.CSC_DATA_FIM

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### LABEL10 — LABEL10
Label String(700) → CPE_PDCI2019.LABEL10

### DESCRICAO_DETALHADA — Descrição detalhada
Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA

### JUSTIFICATIVA — Justificativa
Memo String(1999) → CPE_CSC.JUSTIFICATIVA

### SIM_NAO_100 — Sim ou Não
DropDownList String → CPE_CONTRATOS02.SIM_NAO_100
Itens: Sim;Não

### JUSTIFICATIVA5 — Justificativa5
Memo String → CPE_CONTRATOS02.JUSTIFICATIVA5

### OBS10 — Observação10
Memo String(2000) → CPE_CSC.OBS10

### OBS21 — Observação21
Memo String(4000) → CPE_CSC.OBS21

### SUBPROCESSO_SUPRAVIZIO — Selecione o Subprocesso
TextBox String → CPE_CSC.SUBPROCESSO_SUPRAVIZIO

### CAMPOS — Campos
Memo String → CPE_ORDEM_SERVICO.CAMPOS

### COMBOBOX_I — COMBOBOX_I
DropDownList String → CPE_BOOTCAMP.COMBOBOX_I

### COMBOBOX_II — COMBOBOX_II
DropDownList String → CPE_BOOTCAMP.COMBOBOX_II

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
