# Fluxo: Portal de Estruturação de Negócios (PORTALNEG) — versão 30
Caminho: Fluxos > Nova Estruturação de Negócios Versão 30 Portal de Estruturação de Negócios
XML: `XMLs para teste/Nova_Estruturação_de_Negócios_Versão_30_Portal_de_Estruturação_de_Negócios.xml` | Supravizio 19.1.1 | SubProcessoId 20350 | DesenhoProcessoId 2875 | ProcessoId 79
Órgão dono: 4000006015- DIRETORIA  DE NOVOS NEGOCIOS E RELACIONAMENTO | Responsável: ANDERSON FRANKLIN ROQUE DOS SANTOS
Classe do subprocesso: Objetivo=Novo Portal de Estruturação de Negócios; DescricaoCliente=Portal de Estruturação de Negócios (Projeto); CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Novo Portal de Estruturação de Negócios; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Estruturação de Negócios (NOVOSNEG)

## Grafo do fluxo
- [325490] SubProcesso "MODELAGEM: Consolidação Técnica (Abrir somente uma OS)" {Responsável atual} → [325465] PRECIFICAÇÃO: Informação Contábil
- [325485] Tarefa "PRECIFICAÇÃO: 
Preencher informações para consulta Fisico Tributária" {Responsável atual} → [325450] PRECIFICAÇÃO: Consulta Fisco - Tributária (Estadua
- [325486] EventoInicial "Prospecção" → [G74213] O Gestor do produto já se manifestou pela continui
- [325487] SubProcesso "PRECIFICAÇÃO: Parecer Orçamentário" {Responsável atual} → [325479] PRECIFICAÇÃO:
Estratégia de Preço
- [325488] EventoIntermediarioMensagem "Notificar Tomadores de Conhecimento" → [325451] PROSPECÇÃO: Registrar Aprovação
- [325489] Tarefa "CONTRATAÇÃO: 
Proposta Comercial" {Cliente} → [325457] Proposta Comercial
- [325491] SubProcesso "PRECIFICAÇÃO: Estudo Financeiro e/ou Hedge cambial" {Responsável atual} → [325455] PRECIFICAÇÃO: Precificação e Orçamento
- [325461] EventoIntermediarioTimer "Timer Diário" → [325453] Aviso de Pendência
- [325463] LinkInicial "" {Fila de Oportunidade} → [325464] Avaliação Inicial
- [325464] Tarefa "Avaliação Inicial" {Fila de Oportunidade} → [G74213] O Gestor do produto já se manifestou pela continui
- [325465] SubProcesso "PRECIFICAÇÃO: Informação Contábil" {Responsável atual} → [325484] PRECIFICAÇÃO: Parecer jurídico
- [325467] Tarefa "NEGOCIAÇÃO:
Cenário aprovado" {Responsável atual} → [G74214] Comunicar colegiado?
- [325468] Tarefa "PRECIFICAÇÃO:
Informações para Hedge cambial e investimentos" {Responsável atual} → [325491] PRECIFICAÇÃO: Estudo Financeiro e/ou Hedge cambial
- [325470] Tarefa "MODELAGEM: Estruturação" {Favorecido Cobra} → [G74211] Informações suficientes ?
- [325471] EventoIntermediarioMensagem "Aprovação do Cenário" → [G74216] Comunicar a Equipe Comercial?
- [325473] Tarefa "PRECIFICAÇÃO:
Aguardar finalização dos intervenientes " {Responsável atual} → [G74209] Haverá investimento para o negócio?
- [325474] EventoIntermediarioMensagem "Preço de Referência" → [325458] NEGOCIAÇÃO:
Preço Referência
- [325475] Tarefa "MODELAGEM: Modelagem de Produto
" {Responsável atual} → [325490] MODELAGEM: Consolidação Técnica (Abrir somente uma
- [325478] Tarefa "PROSPECÇÃO: Detalhamento do Go do Gestor
" {Responsável atual} → [325488] Notificar Tomadores de Conhecimento
- [325481] Tarefa "CONTRATAÇÃO:
Elaboração e Aprovação da NT" {Favorecido Cobra} → [325489] CONTRATAÇÃO: 
Proposta Comercial
- [325482] EventoIntermediarioMensagem "Aprovação do Cenário" → [325480] Aprovação do Cenário
- [325479] Tarefa "PRECIFICAÇÃO:
Estratégia de Preço" {Favorecido Cobra} → [325467] NEGOCIAÇÃO:
Cenário aprovado
- [325480] EventoIntermediarioMensagem "Aprovação do Cenário" → [325471] Aprovação do Cenário
- [325483] EventoIntermediarioMensagem "Novos Negócios - Resolução de Pendências" → [325470] MODELAGEM: Estruturação
- [325484] SubProcesso "PRECIFICAÇÃO: Parecer jurídico" {Responsável atual} → [G74212] Solicitar Estudo Financeiro e/ou Hedge cambial?
- [325450] SubProcesso "PRECIFICAÇÃO: Consulta Fisco - Tributária (Estadual, Municipal ou Federal)" {Responsável atual} → [325473] PRECIFICAÇÃO:
Aguardar finalização dos intervenien
- [325448] Tarefa "MODELAGEM: Estruturação" {Fila de Oportunidade} → [G74211] Informações suficientes ?
- [325449] Tarefa "PRECIFICAÇÃO: Inserir DRE
" {Responsável atual} → [325487] PRECIFICAÇÃO: Parecer Orçamentário
- [325451] Tarefa "PROSPECÇÃO: Registrar Aprovação" {Responsável atual} → [325448] MODELAGEM: Estruturação
- [325452] EventoIntermediarioMensagem "Preços de Referência" → [325481] CONTRATAÇÃO:
Elaboração e Aprovação da NT
- [325453] EventoIntermediarioMensagem "Aviso de Pendência" → [325460] PROSPECÇÃO: 
Ajustar Informações
- [325454] SubProcesso "MODELAGEM: Acionamento do Licenter" {Responsável atual} → [325475] MODELAGEM: Modelagem de Produto

- [325455] SubProcesso "PRECIFICAÇÃO: Precificação e Orçamento" {Responsável atual} → [325485] PRECIFICAÇÃO: 
Preencher informações para consulta
- [325456] EventoFinal "" {Responsável atual} → (fim)
- [325457] EventoIntermediarioMensagem "Proposta Comercial" → [G74215] Proposta comercial aceita
- [325458] Tarefa "NEGOCIAÇÃO:
Preço Referência" {Cliente} → [G74210] Preço de ReferÊncia aceito?
- [325459] SubProcesso "PROSPECÇÃO: Aprovar GO ou No Go" {Responsável atual} → [325448] MODELAGEM: Estruturação
- [325460] Tarefa "PROSPECÇÃO: 
Ajustar Informações" {Cliente} → [325461] Timer Diário | [325483] Novos Negócios - Resolução de Pendências
- [G74209] Gateway "Haverá investimento para o negócio?" → «Sim» [325449] PRECIFICAÇÃO: Inserir DRE
 | «Não» [325479] PRECIFICAÇÃO:
Estratégia de Preço
- [G74210] Gateway "Preço de ReferÊncia aceito?" → «Sim» [325452] Preços de Referência | «Não» [325479] PRECIFICAÇÃO:
Estratégia de Preço
- [G74211] Gateway "Informações suficientes ?" → «Sim» [G74217] Essa oportunidade envolve algum dos produtos do Li | «Não» [325453] Aviso de Pendência
- [G74212] Gateway "Solicitar Estudo Financeiro e/ou Hedge cambial?" → «Sim» [325468] PRECIFICAÇÃO:
Informações para Hedge cambial e inv | «Não» [325455] PRECIFICAÇÃO: Precificação e Orçamento
- [G74213] Gateway "O Gestor do produto já se manifestou pela continuidade do processo de estruturação?" → «Não» [325459] PROSPECÇÃO: Aprovar GO ou No Go | «Sim» [325478] PROSPECÇÃO: Detalhamento do Go do Gestor

- [G74214] Gateway "Comunicar colegiado?" → «Sim» [325482] Aprovação do Cenário | «Não» [G74216] Comunicar a Equipe Comercial?
- [G74215] Gateway "Proposta comercial aceita" → «Não» [325479] PRECIFICAÇÃO:
Estratégia de Preço | [325456] 
- [G74216] Gateway "Comunicar a Equipe Comercial?" → «Sim» [325474] Preço de Referência | «Não» [325458] NEGOCIAÇÃO:
Preço Referência
- [G74217] Gateway "Essa oportunidade envolve algum dos produtos do Licenter?" → «Não» [325475] MODELAGEM: Modelagem de Produto
 | «Sim» [325454] MODELAGEM: Acionamento do Licenter

## Gateways
### [G74209] Haverá investimento para o negócio? (EventBasedExclusiveDecision)
- alternativa → [325449] PRECIFICAÇÃO: Inserir DRE
: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [325479] PRECIFICAÇÃO:
Estratégia de Preço: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
### [G74210] Preço de ReferÊncia aceito? (EventBasedExclusiveDecision)
- alternativa → [325452] Preços de Referência: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [325479] PRECIFICAÇÃO:
Estratégia de Preço: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1; MotivoObrigatorio=true; PublicarRespostaAA=true
### [G74211] Informações suficientes ? (EventBasedExclusiveDecision)
Codigo=DADOSCONFEREM
- alternativa → [G74217] Essa oportunidade envolve algum dos produtos do Li: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [325453] Aviso de Pendência: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1; MotivoObrigatorio=true; PublicarRespostaAA=true
### [G74212] Solicitar Estudo Financeiro e/ou Hedge cambial? (EventBasedExclusiveDecision)
- alternativa → [325468] PRECIFICAÇÃO:
Informações para Hedge cambial e inv: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [325455] PRECIFICAÇÃO: Precificação e Orçamento: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
### [G74213] O Gestor do produto já se manifestou pela continuidade do processo de estruturação? (EventBasedExclusiveDecision)
Codigo=DETALHAMENTOGO
- alternativa → [325459] PROSPECÇÃO: Aprovar GO ou No Go: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
- alternativa → [325478] PROSPECÇÃO: Detalhamento do Go do Gestor
: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=2
### [G74214] Comunicar colegiado? (EventBasedExclusiveDecision)
- alternativa → [325482] Aprovação do Cenário: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [G74216] Comunicar a Equipe Comercial?: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
### [G74215] Proposta comercial aceita (EventBasedExclusiveDecision)
- alternativa → [325479] PRECIFICAÇÃO:
Estratégia de Preço: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1; MotivoObrigatorio=true; PublicarRespostaAA=true
- alternativa → [325456] : OperadorDecision=Equal; SequenciaAvaliacao=2
### [G74216] Comunicar a Equipe Comercial? (EventBasedExclusiveDecision)
- alternativa → [325474] Preço de Referência: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [325458] NEGOCIAÇÃO:
Preço Referência: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
### [G74217] Essa oportunidade envolve algum dos produtos do Licenter? (EventBasedExclusiveDecision)
Codigo=ACIONALICENTER
- alternativa → [325475] MODELAGEM: Modelagem de Produto
: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
- alternativa → [325454] MODELAGEM: Acionamento do Licenter: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0

## Atividades

### [325490] SubProcesso "MODELAGEM: Consolidação Técnica (Abrir somente uma OS)"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=934; ChamadaAssincrona=true; Codigo=APROV_CONSO
- ValoresInputs:
  - CustomPropertyId=550; CustomProperty=FAVORECIDO_COBRA
  - CustomPropertyId=2551; CustomProperty=APROVADOR_PB
  - CustomPropertyId=952; CustomProperty=NN_OBJETO_PROPOSTA
  - PropertyId=1263; Property=Assunto
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2157; ClasseConfiguracao=Consolidação Técnica
  - SuperClasse=Artefato; ClasseConfiguracaoId=2731; ClasseConfiguracao=Qualificação de Oportunidade
- Associação: Ativo=true; FraseAssociacao=Portal de Estruturação de Negócios (Projeto) -> Aprovação Consolidação Técnica; FraseInversaAssociacao=Aprovação Consolidação Técnica -> Portal de Estruturação de Negócios (Projeto); CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=NNAPROVACAOCONSOTEC; SeparadorSequencial=. | fonte: Portal de Estruturação de Negócios → alvo: Aprovação Consolidação Técnica (Abrir somente uma OS)

### [325485] Tarefa "PRECIFICAÇÃO: 
Preencher informações para consulta Fisico Tributária"
Responsável: Responsável atual (papel 36)
**ScriptFormCarregado**
```python
#Formulario["FINALIDADE_RUB"].Visivel = False

#Formulario["NN_FORMA_PAGAMENTO"].Visivel = False
#Formulario["NN_FORMA_PAGAMENTO"].Habilitado = False
#Formulario["NN_PAIS"].Visivel = False
#Formulario["NN_PAIS"].Habilitado = False
#Formulario["NN_LOCAL"].Visivel = False
#Formulario["NN_LOCAL"].Habilitado = False   
#Formulario["SIM_NAO4"].Visivel = False
#Formulario["SIM_NAO4"].Habilitado = False
#Formulario["NN_BENEFICIO_FISCAL"].Visivel = False
#Formulario["NN_BENEFICIO_FISCAL"].Habilitado = False

Formulario['NN_FORMA_PAGAMENTO'].Habilitado = False
Formulario['NN_PAIS'].Habilitado = False
Formulario['NN_LOCAL'].Habilitado = False
Formulario['SIM_NAO4'].Habilitado = False
Formulario['NN_BENEFICIO_FISCAL'].Habilitado = False
Formulario['NN_BENEFICIO_FISCAL'].Visivel = False

Formulario["NN_LOCAL_SUPORTE"].Visivel = False
Formulario["NN_LOCAL_SUPORTE"].Habilitado = False


Formulario['NN_CANCELA'].Itens = 'Sim;Não'

if Formulario['NN_CANCELA'].Valor == 'Sim':
    Formulario['Justificativa'].Visivel = True
    Formulario['NN_MOTIVO_CANCELAMENTO'].Visivel = True

else:
    Formulario['Justificativa'].Visivel = False
    Formulario['NN_MOTIVO_CANCELAMENTO'].Visivel = False
    
    #################novo formulário
#Formulario["SIM_NAO6"].Visivel = False
#Formulario["SIM_NAO6"].Habilitado = False
#    
#Formulario["NN_LOCAL_SUPORTE"].Visivel = False
#Formulario["NN_LOCAL_SUPORTE"].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - SIM_NAO6 "Os profissionais vão atuar preferencialmente presencial no cliente?" [DropDownList String → CPE_CSC.SIM_NAO6]
**SIM_NAO6.ScriptModificado**
```python
if Formulario["SIM_NAO6"].Valor == "Sim":
    Formulario["NN_LOCAL_SUPORTE"].Visivel = True
    Formulario["NN_LOCAL_SUPORTE"].Habilitado = True
    
if Formulario["SIM_NAO6"].Valor != "Sim":
    Formulario["NN_LOCAL_SUPORTE"].Visivel = False
    Formulario["NN_LOCAL_SUPORTE"].Habilitado = False
```
  - NN_LOCAL_SUPORTE "Local onde será prestado o suporte presencial?" [DataGrid RecordList → Z_00143_NN_LOCAL_SUPORTE.NN_LOCAL_SUPORTE] — FormaEdicaoWeb=JanelaPopup
    - coluna MUNICIPIO obrigatório
    - coluna ESTADO obrigatório
  - ORIGEM_SERVICO "Qual a origem da aquisição/local de faturamento do SERVIÇO do fornecedor?" [DataGrid RecordList → Z_00143_ORIGEM_SERVICO.ORIGEM_SERVICO] — FormaEdicaoWeb=JanelaPopup
    - coluna ITEM obrigatório
    - coluna ESTADO obrigatório
    - coluna MUNICIPIO obrigatório
  - ORIGEM_PRODUTO "Qual a origem da aquisição/local de faturamento do PRODUTO do fornecedor?" [DataGrid RecordList → Z_00143_ORIGEM_PRODUTO.ORIGEM_PRODUTO] — FormaEdicaoWeb=JanelaPopup
    - coluna ITEM obrigatório
    - coluna ESTADO obrigatório
    - coluna MUNICIPIO obrigatório
  - DESTINACAO_BBTS "Qual a destinação da aquisição (Filial da BBTS)?" [DataGrid RecordList → Z_00143_DESTINACAO_BBTS.DESTINACAO_BBTS] — FormaEdicaoWeb=JanelaPopup
    - coluna ESTADO obrigatório
    - coluna MUNICIPIO obrigatório
  - NN_SIM_NAO "O orçamento enviado pelo fornecedor contempla todos os tributos?" [DropDownList String → CPE_NEGOCIOS.NN_SIM_NAO]
  - SIM_NAO7 "A BBTS irá prestar suporte com pessoal próprio ou terceiro do seu quadro?" [DropDownList String → CPE_CSC.SIM_NAO7]
**SIM_NAO7.ScriptModificado**
```python
if Formulario["SIM_NAO7"].Valor == "Sim":
    Formulario["SIM_NAO6"].Visivel = True
    Formulario["SIM_NAO6"].Habilitado = True
    
if Formulario["SIM_NAO7"].Valor != "Sim":
    Formulario["SIM_NAO6"].Visivel = False
    Formulario["SIM_NAO6"].Habilitado = False
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Formulário de Cancelamento
  - NN_CANCELA "Cancela chamado?" [DropDownList String → CPE_NEGOCIOS.NN_CANCELA]
**NN_CANCELA.ScriptModificado**
```python
if Formulario["NN_CANCELA"].Valor == 'Sim':
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = True
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["Justificativa"].Visivel = True
    Formulario["Justificativa"].Valor = None
else:
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = False
    Formulario["Justificativa"].Valor = None
    Formulario["Justificativa"].Visivel = False

OrdemServico.Salva()
```
  - NN_MOTIVO_CANCELAMENTO "Motivo do cancelamento(após a seleção de um motivo, o chamado será cancelado automaticamente)" [DropDownList String → CPE_NEGOCIOS.NN_MOTIVO_CANCELAMENTO]
**NN_MOTIVO_CANCELAMENTO.ScriptModificado**
```python
motivoCancelamento = Formulario["NN_MOTIVO_CANCELAMENTO"].Valor
justificativa = Formulario["Justificativa"].Valor

OrdemServico.SetCustom("NN_CANCELA", Formulario["NN_CANCELA"].Valor)
OrdemServico.SetCustom("NN_MOTIVO_CANCELAMENTO", motivoCancelamento.ToString())
OrdemServico.Justificativa = justificativa.ToString()
OrdemServico.Salva()

OrdemServico.Cancela(motivoCancelamento.ToString())

OrdemServico.Salva()
```
  - Justificativa (nativo)
- Operação PR0001 Preencher Campos
  - NN_FORMA_PAGAMENTO "Forma de pagamento" [DropDownList String → CPE_NEGOCIOS.NN_FORMA_PAGAMENTO]
  - NN_PAIS "Qual o país do fornecedor?" [TextBox String → CPE_NEGOCIOS.NN_PAIS]
  - NN_LOCAL "Qual o local de residência (país) dos sócios do fornecedor?" [TextBox String → CPE_NEGOCIOS.NN_LOCAL]
    - coluna QUANTIDADE obrigatório
    - coluna VALORTRATAMENTO obrigatório
    - coluna PRAZO obrigatório
    - coluna VALORPAGO obrigatório
    - coluna TRATAMENTO obrigatório
    - coluna NOME obrigatório
  - SIM_NAO4 "O fornecedor sediado no exterior tem algum benefício fiscal? " [DropDownList String → CPE_CSC.SIM_NAO4]
**SIM_NAO4.ScriptModificado**
```python
if Formulario["SIM_NAO4"].Valor == "Sim":
    Formulario["NN_BENEFICIO_FISCAL"].Visivel = True
    Formulario["NN_BENEFICIO_FISCAL"].Habilitado = True
    
if Formulario["SIM_NAO4"].Valor != "Sim":
    Formulario["NN_BENEFICIO_FISCAL"].Visivel = False
    Formulario["NN_BENEFICIO_FISCAL"].Habilitado = False
```
  - NN_BENEFICIO_FISCAL "Qual benefício fiscal?" [TextBox String → CPE_NEGOCIOS.NN_BENEFICIO_FISCAL]

### [325486] EventoInicial "Prospecção"
Config: Configuracao={"ServicoIniciador":"NOVOSNEG"}
TipoSolicitacao: Novos Negócios
**ScriptFormCarregado**
```python
Formulario['COMBOBOX1'].Visivel = True
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo de documento" classes: Documentos — RequeridoInicial=true; PermiteMultiplosItens=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos
  - NN_NUMERO_NDA "Número do Chamado do NDA " [TextBox String → CPE_NEGOCIOS.NN_NUMERO_NDA]
  - NN_FORMACONTRATACAO "Forma de Contratação" [DropDownList String → CPE_HOMOLOGACAO.NN_FORMACONTRATACAO] obrigatório
  - NN_POC "Teve POC/Piloto/Degustação" [DropDownList String → CPE_NEGOCIOS.NN_POC] obrigatório
**NN_POC.ScriptModificado**
```python
if Formulario['NN_POC'].Valor == 'Não':
    Formulario['MOTIVO'].Visivel = False
    Formulario['MOTIVO'].Habilitado = False
    
else:
    Formulario['MOTIVO'].Visivel = True
    Formulario['MOTIVO'].Habilitado = True
```
  - MOTIVO "Detalhamento POC/Piloto/Degustação" [Memo String(1500) → CP_ORDEM_SERVICO.MOTIVO] obrigatório
  - CANALDEVENDA "Contato(s) do Cliente" [DataGrid RecordList → Z_00143_CANALDEVENDA.CANALDEVENDA] obrigatório — FormaEdicaoWeb=JanelaPopup; LarguraJanelaPopup=300
    - coluna TELLCLIENT obrigatório
    - coluna DATARESPCLIENT obrigatório
    - coluna EMAILCLIENT obrigatório
    - coluna CARGOCLIENT obrigatório
    - coluna SETCLIENT obrigatório
    - coluna DATAINIPROSP obrigatório
    - coluna NOMECTTCLIENT obrigatório
  - CANALDEVENDA1 "Canal de Venda" [DropDownList String(900) → CPE_NEGOCIOS.CANALDEVENDA1] obrigatório
  - NN_DATAPICKER1 "Data inicio da Prospecção" [DatePicker DateTime → CPE_NEGOCIOS.NN_DATAPICKER1] obrigatório
  - NN_DATA_REPROG "Resposta ao Cliente" [DataGrid RecordList → Z_00143_NN_DATA_REPROG.NN_DATA_REPROG] — FormaEdicaoWeb=JanelaPopup
    - coluna SITUACAO obrigatório
    - coluna DATA obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: RFP RFI RFQ  — RequeridoInicial=true; IncluirPaginaAssinatura=true
  - anexo "" classes: Projeto Básico — RequeridoInicial=true; IncluirPaginaAssinatura=true
  - anexo "Documentos da Qualificação" classes: Edital — RequeridoInicial=true; IncluirPaginaAssinatura=true
  - anexo "" classes: Outros documentos — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Qualificação da Oportunidade" classes: Qualificação de Oportunidade — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos
  - GRID_PESSOAS "Tomar Conhecimento da Oportunidade (Gerex e Super)" [DataGrid RecordList → Z_00143_GRID_PESSOAS.GRID_PESSOAS] — FormaEdicaoWeb=JanelaPopup
    - coluna PESSOAS
  - PREMISSA_DOD "Premissas/Restrições/Volumetria" [Memo String(2000) → CP_ORDEM_SERVICO.PREMISSA_DOD] obrigatório
  - NN_PORTFOLIO "Referência de mercado (fornecedor/intervenientes/concorrentes/normas, etc)" [Memo String(2000) → CPE_NEGOCIOS.NN_PORTFOLIO] obrigatório
  - NN_SEGMENTO "Segmento de Mercado" [DropDownList String → CPE_NEGOCIOS.NN_SEGMENTO] obrigatório
**NN_SEGMENTO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Local
if Formulario["NN_SEGMENTO"].Valor == 'Mercado':
    Formulario["COMBOBOX1"].Itens = '3Corp;AIDC;Aiko;Algar;Assban;Banco ABC;Banco Inter;Banco Original;Banco Pan;Banco Topázio;Banrisul;Basa;Bradesco;Brasil Digital;Brinks;Centurylink;Ceuma;Clear Sales;Connectoway;Conservo;Credfisa;Ctis;Daten;Dell;Digio;Dotz;Engepron;Engie;Envestcon;Espaço Y;E-Vida;FazSol;FGCOOP;Galgo;Gemalto;Gerdau;Globo;Grupo Saga;HCL Tech;IBCG;ICESP;Infinity;INPI;Lenovo;Lever Tech;Localiza;M4U;Mercantil;Montreal;Oi;Perto;Porto Seguro;PrevData;Prevpeb;Prosegur;Qintess;Ririera;Salutis;Sicob;Sicredi;Smiles;Thales;Valor Invest;Via Varejo;Viridi;Vivo;Zoom;SPDM - ASSOCIACAO PAULISTA PARA O DESENVOLVIMENTO DA MEDICINA;AUDIO CODES;Shooting House;Grupo Concórdia;Grupo Artico;AIDC;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True
    
elif Formulario["NN_SEGMENTO"].Valor == 'Governo':
    Formulario["COMBOBOX1"].Itens = 'Aeronáutica;AGU;ANA;Bacen;Banco do Nordeste;BANDES;Banestes;Banpará;BNDES;BRB;Caixa;Caixa Asset;Caixa Cartões;Caixa DTVM;Caixa Previ;Caixa Seguridade;Câmara dos Deputados;CBTU;CEB;CFP;Conab;Correios;Dataprev;Detran DF;EBC;Eletrobrás;Embasa;Emgea;Exército;Finep;FUNPREV PIAUÍ;Fusan;Governo da Bahia;Governo da SC;Governo do ACRE;HC-UFG;Hemobrás;IPLanrio;IPMT Teresina;Iprev;JUCESP;MDIC;ME e MTPS;Ministério das Comunicações;Ministério MDA;MME;MPF;Neoenergia;OAB;PCDF;Petrobrás;PJRN;Prevdata;Procuradoria-Geral da Fazenda Nacional;Prodam;Prode Pará;Prodemge;SCJF-DF;Sebrae;Sefaz MA;SEFAZ SP;Serpro;SJ Campos;SPTrans;TC Rondônia;TJ ES;TJ Sergipe;TJ SC;TJ TO;TRE Pará;TRE Roraima;TRF1ª;TRF2ª;TRF4ª;Valec;ANATEL;TRT4;Tribunal de Contas/RR;Tribunal de Contas/GO;SUPEL/RO;Pref. de Rio Branco/AC;CREA/PR;Detran/PE;Defensoria Pública/BA;Dataprev;Tribunal de Justiça/BA;Pref. de Schroeder/SC;Fund. Oswaldo Cruz/RJ;SEPLOG/SE;SESC/SE;Sec. de Seg. Pública/PI;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True

elif Formulario["NN_SEGMENTO"].Valor == 'Banco do Brasil':
    Formulario["COMBOBOX1"].Itens = 'USI;DITEC;DIOPE;DISEC;DIGOV;DICRE;DICOI;UCS;DIREC;UGE;UCR;DICOR;UAC;DINED;UAN;DIRAG;DIMEP;DIEMP;DIJUR;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True
    
elif Formulario["NN_SEGMENTO"].Valor == 'ELBB':
    Formulario["COMBOBOX1"].Itens = 'ALELO;ALIANÇA DO BRASIL SEGUROS;ALIANÇA PAG;ALPHA SERV. DE AUTOATENDIMENTO;ATIVOS S.A. SEC. DE CRÉD. FINANCEIROS;BANCO PATAGONIA;BANCO VOTORANTIM;BB ADMINISTRADORA DE CARTÕES DE CRÉDITO;BB AG;BB AMERICAS;BB ASSET;BB ASSET MANAGEMENT IRELAND;BB BANCO DE INVESTIMENTO (BB-BI);BB CAYMAN ISLANDS HOLDING (BB-CI);BB CONSÓRCIOS;BB CORRETORA DE SEGUROS E ADMI.DE BENS S.A. (BB CORRETORA);BB ELO CARTÕES;BB LEASING;BB MAPFRE PARTICIPAÇÕES S.A;BB PREVIDÊNCIA;BB SECURITIES;BB SEGURIDADE;BB SEGUROS;BB USA HOLDING COMPANY INC;BRASIL DENTAL;BRASILCAP;BRASILPREV SEG. E PREV. S.A.;BRASILSEG;BV EMPREEND. E PARTICIPAÇÕES;BV INVEST. ALTERN. E GEST. DE RECUR;CADAM OVERSEAS LTD;CADAM;CAIXA DE ASSISTÊNCIA DOS EMPREGADOS (SIM);CÂMARA INTERBANCÁRIA DE PAGAMENTOS (CIP);CASSI;CATENO;CIA. HIDROMINERAL PIRATUBA;CICLIC;CIELO;CIELO S.A.;ECONOMUS;ELO HOLDING FINANCEIRA;ELO SERVIÇOS;ELOPAR;ESTRUT. BRAS. DE PROJ.;FUNDAÇÃO BANCO DO BRASIL (FBB);FUNDAÇÃO CODESC DE SEGURIDADE SOCIAL (FUSESC);GALGO SISTEMAS DE INFORMAÇÃO;GPAT COMPAÑIA FINANCIERA;KAOLIN INTERNATIONAL N.V.;KARTRA PARTICIPAÇÕES;LIVELO;MERCHANT E-SOLUTIONS;PAGGO SOLUÇÕES E MEIOS DE PAGAMENTOS;PREVBEP;PREVI;PROMOTIVA;QUOD;SERVINET SERVIÇOS;STELO;TBFORTE TRANSP. VALORES BRASIL FORTE;TBNET COM., LOCAÇÃO E ADM.;TECNOLOGIA BANCÁRIA;UBS BB SERV. \ ASSE. FIN. PART.;VOTORANTIM CORR. SEGUROS;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True
```
  - COMBOBOX1 "Clientes" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
  - CNPJ "CNPJ do Cliente" [TextBox String → CP_ORDEM_SERVICO.CNPJ] obrigatório — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00\\.000\\.000\\/0000\\-00"}
  - NN_GERENCIA_NEGOCIO "Área gestora do produto/serviço" [DropDownList String → CP_ORDEM_SERVICO.NN_GERENCIA_NEGOCIO] obrigatório
  - NN_LINHA_NEGOCIO "Linha de Negócio" [DropDownList String → CPE_NEGOCIOS.NN_LINHA_NEGOCIO] obrigatório
**NN_LINHA_NEGOCIO.ScriptModificado**
```python
from Venki.Supravizio.Configuracao.Custom import Software
if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Infraestrutura e Disponibilidade':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Disponibilidade Operacional de TAA;Disponibilidade Operacional de Bens de Automação Bancária;Monitoração de Ambientes;Infraestrutura de Data Center;Assistência Técnica de Sistemas de Portas Giratórias, Sala On-Line e Nobreak'



if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Gestão de Segurança':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Disponibilidade Operacional de Sistema de Alarme e Dispositivos de Resposta;Disponibilidade Operacional de Sistema de Imagens;PSIM - Plataforma de Integração e Gerenciamento de informações de segurança física;Cross Data Team (CDT);Managed Security Services Provider ¿ MSSP (Centro de Operação de Cyber Segurança ¿ SOC N1/N2/N3, Professional Security Services, Phishing, Pentest e Gestão de Vulnerabilidade)'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Comunicação e Conectividade':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Intevia - Mensageria SMS;Intevia - Mensageria e e-mail marketing;Teya - Outsourcing de Telefonia (Plataforma de Voz e Vídeo)'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Canais e Backoffice':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Centrais de Relacionamento e Telecobrança;Cobrança Extrajudicial de Dívidas;Gestão Eletrônica De Documentos (GED);Kit Pré-Ajuizamento;Microfilmagem'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Soluções Digitais':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Fábrica de Software;Plataformas (Aprovve Service);Hiperautomação (LowCode)'



if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Soluções de Parcerias Estratégicas':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Interoperabilidade (HIVEPlace);Revenda Especializada (Licenter)'



if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Correspondente Bancário':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Gestão de Correspondentes Bancários;Representação Comercial;Agente de Crédito Rural (ACR)'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Outros':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Outros'
```
  - NN_PRODUTO "Produto" [DropDownList String → CPE_NEGOCIOS.NN_PRODUTO] obrigatório
  - NN_PRODUTO_EXISTENTE "Produto do portfólio?" [DropDownList String → CPE_NEGOCIOS.NN_PRODUTO_EXISTENTE] obrigatório
  - SIM_NAO "Projeto contido no orçamento?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
  - NN_DATA_REPROG "Resposta ao Cliente" [DataGrid RecordList → Z_00143_NN_DATA_REPROG.NN_DATA_REPROG] — FormaEdicaoWeb=JanelaPopup
    - coluna DATA obrigatório
    - coluna SITUACAO obrigatório
  - NN_OBJETO_PROPOSTA "Objetivo do Negócio (Necessidade do cliente)" [Memo String(2000) → CP_ORDEM_SERVICO.NN_OBJETO_PROPOSTA] obrigatório
  - APROVADOR_PB "GESTOR(ES) DO(S) PRODUTO(S) - (Gediv)" [DataGrid RecordList → Z_00143_APROVADOR_PB.APROVADOR_PB] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna APROVADORES obrigatório
  - NN_STATUS_PROJETO "Status projeto" [DropDownList String → CPE_NEGOCIOS.NN_STATUS_PROJETO] obrigatório
  - NN_PRAZO_ESTIMADO "Prazo do contrato estimado" [DropDownList String → CPE_NEGOCIOS.NN_PRAZO_ESTIMADO] obrigatório
- ClientesAutorizados:
  - PapelProcessoId=59849; PapelAutorizado=Disec
  - PapelProcessoId=59853; PapelAutorizado=Novos Negócios
  - PapelProcessoId=59854; PapelAutorizado=Novos Negócios - provisório
  - PapelProcessoId=59859; PapelAutorizado=Divisão de Negócios em Licitação

### [325487] SubProcesso "PRECIFICAÇÃO: Parecer Orçamentário"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=961; ChamadaAssincrona=true; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2157; ClasseConfiguracao=Consolidação Técnica
  - SuperClasse=Artefato; ClasseConfiguracaoId=2754; ClasseConfiguracao=DRE
- Associação: Ativo=true; FraseAssociacao=Portal de Estruturação de Negócios (Projeto) -> Parecer Orçamentário; FraseInversaAssociacao=Parecer Orçamentário -> Portal de Estruturação de Negócios (Projeto); CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=ESTRUTURACAOORCAMENTO; SeparadorSequencial=. | fonte: Portal de Estruturação de Negócios → alvo: Parecer Orçamentário

### [325488] EventoIntermediarioMensagem "Notificar Tomadores de Conhecimento"
Destinatário: Grid Pessoas  (papel 1068)
ModeloComunicado: Notificar Tomadores de Conhecimento
Corpo do comunicado: Prezados,
Seguem anexas às informações de nova oportunidade de negócio referente ao Projeto OrdemServico.Assunto, conduzida pelo chamado de número OrdemServico.Numero Link.Consulta .
Estamos à disposição para os esclarecimentos que sobrevierem.
Atenciosamente,
Central de Serviços

### [325489] Tarefa "CONTRATAÇÃO: 
Proposta Comercial"
Responsável: Cliente (papel 18)
**ScriptFormCarregado**
```python
Formulario['NN_CANCELA'].Itens = 'Sim;Não'
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Formulário de Cancelamento
  - NN_CANCELA "Cancela chamado?" [DropDownList String → CPE_NEGOCIOS.NN_CANCELA]
**NN_CANCELA.ScriptModificado**
```python
if Formulario["NN_CANCELA"].Valor == 'Sim':
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = True
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["Justificativa"].Visivel = True
    Formulario["Justificativa"].Valor = None
else:
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = False
    Formulario["Justificativa"].Valor = None
    Formulario["Justificativa"].Visivel = False

OrdemServico.Salva()
```
  - Justificativa (nativo)
  - NN_MOTIVO_CANCELAMENTO "Motivo do cancelamento(após a seleção de um motivo, o chamado será cancelado automaticamente)" [DropDownList String → CPE_NEGOCIOS.NN_MOTIVO_CANCELAMENTO]
**NN_MOTIVO_CANCELAMENTO.ScriptModificado**
```python
motivoCancelamento = Formulario["NN_MOTIVO_CANCELAMENTO"].Valor
justificativa = Formulario["Justificativa"].Valor

OrdemServico.SetCustom("NN_CANCELA", Formulario["NN_CANCELA"].Valor)
OrdemServico.SetCustom("NN_MOTIVO_CANCELAMENTO", motivoCancelamento.ToString())
OrdemServico.Justificativa = justificativa.ToString()
OrdemServico.Salva()

OrdemServico.Cancela(motivoCancelamento.ToString())

OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos
  - NN_DATA_ENVIO_PROPOSTA "Data de envio da proposta" [DataGrid RecordList → Z_00143_NN_DATA_ENVIO_PROPOSTA.NN_DATA_ENVIO_PROPOSTA] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna DATA_ENVIO_PROPOSTA obrigatório
    - coluna VALOR_GLOBAL obrigatório
    - coluna NN_PROPOSTA_COMERCIAL obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Proposta Comercial" classes: Proposta Comercial — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [325491] SubProcesso "PRECIFICAÇÃO: Estudo Financeiro e/ou Hedge cambial"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=776; ChamadaAssincrona=true; PassaTodosItens=true; RetornaTodosItens=true
- ValoresInputs:
  - CustomPropertyId=2554; CustomProperty=OBS20
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
- Associação: Ativo=true; FraseAssociacao=Portal de Estruturação de Négocios -> Estudo Financeiro e/ou Hedge cambial; FraseInversaAssociacao=Estudo Financeiro e/ou Hedge cambial -> Portal de Estruturação de Negócios; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=ESTUDO_FINANCEIRO; SeparadorSequencial=. | fonte: Portal de Estruturação de Negócios → alvo: Estudo Financeiro e/ou Hedge cambial

### [325461] EventoIntermediarioTimer "Timer Diário"
Config: TempoIntervalo=1440; MaximoExecucao=1

### [325463] LinkInicial ""
Responsável: Fila de Oportunidade (papel 599)
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - NN_OBJETO_PROPOSTA "Objetivo do Negócio (Necessidade do cliente)" [Memo String(2000) → CP_ORDEM_SERVICO.NN_OBJETO_PROPOSTA] obrigatório
  - PREMISSA_DOD "Premissas/Restrições/Volumetria" [Memo String(2000) → CP_ORDEM_SERVICO.PREMISSA_DOD] obrigatório
  - NN_PORTFOLIO "Referência de mercado (fornecedor/intervenientes/concorrentes/normas, etc)" [Memo String(2000) → CPE_NEGOCIOS.NN_PORTFOLIO] obrigatório
  - NN_SEGMENTO "Segmento de Mercado" [DropDownList String → CPE_NEGOCIOS.NN_SEGMENTO] obrigatório
**NN_SEGMENTO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Local
if Formulario["NN_SEGMENTO"].Valor == 'Mercado':
    Formulario["COMBOBOX1"].Itens = '3Corp;AIDC;Aiko;Algar;Assban;Banco ABC;Banco Inter;Banco Original;Banco Pan;Banco Topázio;Banrisul;Basa;Bradesco;Brasil Digital;Brinks;Centurylink;Ceuma;Clear Sales;Connectoway;Conservo;Credfisa;Ctis;Daten;Dell;Digio;Dotz;Engepron;Engie;Envestcon;Espaço Y;E-Vida;FazSol;FGCOOP;Galgo;Gemalto;Gerdau;Globo;Grupo Saga;HCL Tech;IBCG;ICESP;Infinity;INPI;Lenovo;Lever Tech;Localiza;M4U;Mercantil;Montreal;Oi;Perto;Porto Seguro;PrevData;Prevpeb;Prosegur;Qintess;Ririera;Salutis;Sicob;Sicredi;Smiles;Thales;Valor Invest;Via Varejo;Viridi;Vivo;Zoom;SPDM - ASSOCIACAO PAULISTA PARA O DESENVOLVIMENTO DA MEDICINA;AUDIO CODES;Shooting House;Grupo Concórdia;Grupo Artico;AIDC;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True
    
elif Formulario["NN_SEGMENTO"].Valor == 'Governo':
    Formulario["COMBOBOX1"].Itens = 'Aeronáutica;AGU;ANA;Bacen;Banco do Nordeste;BANDES;Banestes;Banpará;BNDES;BRB;Caixa;Caixa Asset;Caixa Cartões;Caixa DTVM;Caixa Previ;Caixa Seguridade;Câmara dos Deputados;CBTU;CEB;CFP;Conab;Correios;Dataprev;Detran DF;EBC;Eletrobrás;Embasa;Emgea;Exército;Finep;FUNPREV PIAUÍ;Fusan;Governo da Bahia;Governo da SC;Governo do ACRE;HC-UFG;Hemobrás;IPLanrio;IPMT Teresina;Iprev;JUCESP;MDIC;ME e MTPS;Ministério das Comunicações;Ministério MDA;MME;MPF;Neoenergia;OAB;PCDF;Petrobrás;PJRN;Prevdata;Procuradoria-Geral da Fazenda Nacional;Prodam;Prode Pará;Prodemge;SCJF-DF;Sebrae;Sefaz MA;SEFAZ SP;Serpro;SJ Campos;SPTrans;TC Rondônia;TJ ES;TJ Sergipe;TJ SC;TJ TO;TRE Pará;TRE Roraima;TRF1ª;TRF2ª;TRF4ª;Valec;ANATEL;TRT4;Tribunal de Contas/RR;Tribunal de Contas/GO;SUPEL/RO;Pref. de Rio Branco/AC;CREA/PR;Detran/PE;Defensoria Pública/BA;Dataprev;Tribunal de Justiça/BA;Pref. de Schroeder/SC;Fund. Oswaldo Cruz/RJ;SEPLOG/SE;SESC/SE;Sec. de Seg. Pública/PI;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True

elif Formulario["NN_SEGMENTO"].Valor == 'Banco do Brasil':
    Formulario["COMBOBOX1"].Itens = 'USI;DITEC;DIOPE;DISEC;DIGOV;DICRE;DICOI;UCS;DIREC;UGE;UCR;DICOR;UAC;DINED;UAN;DIRAG;DIMEP;DIEMP;DIJUR;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True
    
elif Formulario["NN_SEGMENTO"].Valor == 'ELBB':
    Formulario["COMBOBOX1"].Itens = 'ALELO;ALIANÇA DO BRASIL SEGUROS;ALIANÇA PAG;ALPHA SERV. DE AUTOATENDIMENTO;ATIVOS S.A. SEC. DE CRÉD. FINANCEIROS;BANCO PATAGONIA;BANCO VOTORANTIM;BB ADMINISTRADORA DE CARTÕES DE CRÉDITO;BB AG;BB AMERICAS;BB ASSET;BB ASSET MANAGEMENT IRELAND;BB BANCO DE INVESTIMENTO (BB-BI);BB CAYMAN ISLANDS HOLDING (BB-CI);BB CONSÓRCIOS;BB CORRETORA DE SEGUROS E ADMI.DE BENS S.A. (BB CORRETORA);BB ELO CARTÕES;BB LEASING;BB MAPFRE PARTICIPAÇÕES S.A;BB PREVIDÊNCIA;BB SECURITIES;BB SEGURIDADE;BB SEGUROS;BB USA HOLDING COMPANY INC;BRASIL DENTAL;BRASILCAP;BRASILPREV SEG. E PREV. S.A.;BRASILSEG;BV EMPREEND. E PARTICIPAÇÕES;BV INVEST. ALTERN. E GEST. DE RECUR;CADAM OVERSEAS LTD;CADAM;CAIXA DE ASSISTÊNCIA DOS EMPREGADOS (SIM);CÂMARA INTERBANCÁRIA DE PAGAMENTOS (CIP);CASSI;CATENO;CIA. HIDROMINERAL PIRATUBA;CICLIC;CIELO;CIELO S.A.;ECONOMUS;ELO HOLDING FINANCEIRA;ELO SERVIÇOS;ELOPAR;ESTRUT. BRAS. DE PROJ.;FUNDAÇÃO BANCO DO BRASIL (FBB);FUNDAÇÃO CODESC DE SEGURIDADE SOCIAL (FUSESC);GALGO SISTEMAS DE INFORMAÇÃO;GPAT COMPAÑIA FINANCIERA;KAOLIN INTERNATIONAL N.V.;KARTRA PARTICIPAÇÕES;LIVELO;MERCHANT E-SOLUTIONS;PAGGO SOLUÇÕES E MEIOS DE PAGAMENTOS;PREVBEP;PREVI;PROMOTIVA;QUOD;SERVINET SERVIÇOS;STELO;TBFORTE TRANSP. VALORES BRASIL FORTE;TBNET COM., LOCAÇÃO E ADM.;TECNOLOGIA BANCÁRIA;UBS BB SERV. \ ASSE. FIN. PART.;VOTORANTIM CORR. SEGUROS;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True
```
  - COMBOBOX1 "Clientes" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
  - CNPJ "CNPJ do Cliente" [TextBox String → CP_ORDEM_SERVICO.CNPJ] obrigatório — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00\\.000\\.000\\/0000\\-00"}
  - NN_GERENCIA_NEGOCIO "Área gestora do produto/serviço" [DropDownList String → CP_ORDEM_SERVICO.NN_GERENCIA_NEGOCIO] obrigatório
  - NN_LINHA_NEGOCIO "Linha de Negócio" [DropDownList String → CPE_NEGOCIOS.NN_LINHA_NEGOCIO] obrigatório
**NN_LINHA_NEGOCIO.ScriptModificado**
```python
from Venki.Supravizio.Configuracao.Custom import Software
if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Infraestrutura e Disponibilidade':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Disponibilidade Operacional de TAA;Disponibilidade Operacional de Bens de Automação Bancária;Monitoração de Ambientes;Infraestrutura de Data Center;Assistência Técnica de Sistemas de Portas Giratórias, Sala On-Line e Nobreak'



if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Gestão de Segurança':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Disponibilidade Operacional de Sistema de Alarme e Dispositivos de Resposta;Disponibilidade Operacional de Sistema de Imagens;PSIM - Plataforma de Integração e Gerenciamento de informações de segurança física;Cross Data Team (CDT);Managed Security Services Provider ¿ MSSP (Centro de Operação de Cyber Segurança ¿ SOC N1/N2/N3, Professional Security Services, Phishing, Pentest e Gestão de Vulnerabilidade)'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Comunicação e Conectividade':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Intevia - Mensageria SMS;Intevia - Mensageria e e-mail marketing;Teya - Outsourcing de Telefonia (Plataforma de Voz e Vídeo)'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Canais e Backoffice':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Centrais de Relacionamento e Telecobrança;Cobrança Extrajudicial de Dívidas;Gestão Eletrônica De Documentos (GED);Kit Pré-Ajuizamento;Microfilmagem'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Soluções Digitais':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Fábrica de Software;Plataformas (Aprovve Service);Hiperautomação (LowCode)'



if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Soluções de Parcerias Estratégicas':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Interoperabilidade (HIVEPlace);Revenda Especializada (Licenter)'



if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Correspondente Bancário':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Gestão de Correspondentes Bancários;Representação Comercial;Agente de Crédito Rural (ACR)'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Outros':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Outros'
```
  - NN_PRODUTO "Produto" [DropDownList String → CPE_NEGOCIOS.NN_PRODUTO] obrigatório
  - NN_STATUS_PROJETO "Status projeto" [DropDownList String → CPE_NEGOCIOS.NN_STATUS_PROJETO] obrigatório
  - NN_PRAZO_ESTIMADO "Prazo do contrato estimado" [DropDownList String → CPE_NEGOCIOS.NN_PRAZO_ESTIMADO] obrigatório
  - NN_PRODUTO_EXISTENTE "Produto do portfólio?" [DropDownList String → CPE_NEGOCIOS.NN_PRODUTO_EXISTENTE] obrigatório
  - SIM_NAO "Projeto contido no orçamento?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
  - NN_DATA_REPROG "Resposta ao Cliente" [DataGrid RecordList → Z_00143_NN_DATA_REPROG.NN_DATA_REPROG] — FormaEdicaoWeb=JanelaPopup
    - coluna DATA obrigatório
    - coluna SITUACAO obrigatório
  - APROVADOR_PB "GESTOR(ES) DO(S) PRODUTO(S) - (Gediv)" [DataGrid RecordList → Z_00143_APROVADOR_PB.APROVADOR_PB] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna APROVADORES obrigatório
  - GRID_PESSOAS "Tomar Conhecimento da Oportunidade (Gerex e Super)" [DataGrid RecordList → Z_00143_GRID_PESSOAS.GRID_PESSOAS] — FormaEdicaoWeb=JanelaPopup
    - coluna PESSOAS
- Operação PR0001 Preencher Campos
  - CANALDEVENDA "Contato(s) do Cliente" [DataGrid RecordList → Z_00143_CANALDEVENDA.CANALDEVENDA] obrigatório — FormaEdicaoWeb=JanelaPopup; LarguraJanelaPopup=300
    - coluna SETCLIENT obrigatório
    - coluna DATAINIPROSP obrigatório
    - coluna NOMECTTCLIENT obrigatório
    - coluna TELLCLIENT obrigatório
    - coluna DATARESPCLIENT obrigatório
    - coluna EMAILCLIENT obrigatório
    - coluna CARGOCLIENT obrigatório
  - CANALDEVENDA1 "Canal de Venda" [DropDownList String(900) → CPE_NEGOCIOS.CANALDEVENDA1] obrigatório
  - NN_DATAPICKER1 "Data inicio da Prospecção" [DatePicker DateTime → CPE_NEGOCIOS.NN_DATAPICKER1] obrigatório
  - NN_DATA_REPROG "Resposta ao Cliente" [DataGrid RecordList → Z_00143_NN_DATA_REPROG.NN_DATA_REPROG] — FormaEdicaoWeb=JanelaPopup
    - coluna DATA obrigatório
    - coluna SITUACAO obrigatório
  - NN_NUMERO_NDA "Número do Chamado do NDA " [TextBox String → CPE_NEGOCIOS.NN_NUMERO_NDA]
  - NN_FORMACONTRATACAO "Forma de Contratação" [DropDownList String → CPE_HOMOLOGACAO.NN_FORMACONTRATACAO] obrigatório
  - NN_POC "Teve POC/Piloto/Degustação" [DropDownList String → CPE_NEGOCIOS.NN_POC] obrigatório
**NN_POC.ScriptModificado**
```python
if Formulario['NN_POC'].Valor == 'Não':
    Formulario['MOTIVO'].Visivel = False
    Formulario['MOTIVO'].Habilitado = False
    
else:
    Formulario['MOTIVO'].Visivel = True
    Formulario['MOTIVO'].Habilitado = True
```
  - MOTIVO "Detalhamento POC/Piloto/Degustação" [Memo String(1500) → CP_ORDEM_SERVICO.MOTIVO]
- Associação de subprocesso: AssociacaoId=1542; Nome=DANIELA BERNARDO PROVAZI PESCI; FraseAssociacao=Hive Place > Portal Novos Negócios

### [325464] Tarefa "Avaliação Inicial"
Responsável: Fila de Oportunidade (papel 599)

### [325465] SubProcesso "PRECIFICAÇÃO: Informação Contábil"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1065; ChamadaAssincrona=true; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2157; ClasseConfiguracao=Consolidação Técnica
- Associação: Ativo=true; FraseAssociacao=Portal de Estruturação de Negócios (Projeto) -> Informação Contábil; FraseInversaAssociacao=Informação Contábil -> Portal de Estruturação de Negócios (Projeto); CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=INFORMARCONTABIL; SeparadorSequencial=. | fonte: Portal de Estruturação de Negócios → alvo: Informação Contábil

### [325467] Tarefa "NEGOCIAÇÃO:
Cenário aprovado"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - OBS1 "Premissas Internas" [Memo String(2000) → CPE_CONTRATOS.OBS1] obrigatório
  - OBS3 "Premissas do Cliente" [Memo String(2000) → CPE_CONTRATOS.OBS3] obrigatório
  - SELECAPROV "Membros do Colegiado (Gerex dos Produtos envolvidos)" [DataGrid RecordList → Z_00143_SELECAPROV.SELECAPROV] obrigatório
    - coluna APROVADORES obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "
Modelo de Preço do Cliente" classes: Modelo — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [325468] Tarefa "PRECIFICAÇÃO:
Informações para Hedge cambial e investimentos"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - OBS20 "Detalhamento do pedido para Hedge cambial e/ou investimentos" [Memo String(40000) → CPE_CSC.OBS20] obrigatório

### [325470] Tarefa "MODELAGEM: Estruturação"
Responsável: Favorecido Cobra (papel 277)

### [325471] EventoIntermediarioMensagem "Aprovação do Cenário"
Destinatário: Aprovadores Projeto Básico (papel 842)
ModeloComunicado: Novos Negócios - Aprovação do Cenário
Corpo do comunicado: Prezados,
Após a avaliação colegiada, a decisão foi favorável para apresentar os preços do projeto OrdemServico.Assunto, conduzido pelo chamado número OrdemServico.Numero, conforme o seguinte cenário:
O OrdemServico.Customizado.COMBOBOX4 foi aprovado.
Estamos à disposição para os esclarecimentos que sobrevierem.
Atenciosamente,
Central de Serviços
Atenciosamente,
Central de Serviços
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=2716; ClasseConfiguracao=Tela Azul

### [325473] Tarefa "PRECIFICAÇÃO:
Aguardar finalização dos intervenientes "
Responsável: Responsável atual (papel 36)
**ScriptFormCarregado**
```python
Formulario['NN_CANCELA'].Itens = 'Sim;Não'
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Formulário de Cancelamento
  - NN_CANCELA "Cancela chamado?" [DropDownList String → CPE_NEGOCIOS.NN_CANCELA]
**NN_CANCELA.ScriptModificado**
```python
if Formulario["NN_CANCELA"].Valor == 'Sim':
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = True
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["Justificativa"].Visivel = True
    Formulario["Justificativa"].Valor = None
else:
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = False
    Formulario["Justificativa"].Valor = None
    Formulario["Justificativa"].Visivel = False

OrdemServico.Salva()
```
  - Justificativa (nativo)
  - NN_MOTIVO_CANCELAMENTO "Motivo do cancelamento(após a seleção de um motivo, o chamado será cancelado automaticamente)" [DropDownList String → CPE_NEGOCIOS.NN_MOTIVO_CANCELAMENTO]
**NN_MOTIVO_CANCELAMENTO.ScriptModificado**
```python
motivoCancelamento = Formulario["NN_MOTIVO_CANCELAMENTO"].Valor
justificativa = Formulario["Justificativa"].Valor

OrdemServico.SetCustom("NN_CANCELA", Formulario["NN_CANCELA"].Valor)
OrdemServico.SetCustom("NN_MOTIVO_CANCELAMENTO", motivoCancelamento.ToString())
OrdemServico.Justificativa = justificativa.ToString()
OrdemServico.Salva()

OrdemServico.Cancela(motivoCancelamento.ToString())

OrdemServico.Salva()
```

### [325474] EventoIntermediarioMensagem "Preço de Referência"
Destinatário: Cliente e Responsavel Atual (papel 544)
Config: ListaDestinatarios=comercial@bbts.com.br
ModeloComunicado: Novos Negócios - Preço de Referência
Corpo do comunicado: Prezado(a) OrdemServico.Cliente.Nome,
Após a avaliação colegiada, a decisão foi favorável para apresentar os preços de referência do projeto OrdemServico.Assunto, conduzido pelo chamado número OrdemServico.Numero ( Link.Consulta ), conforme as seguintes premissas:
O OrdemServico.Customizado.COMBOBOX4 foi aprovado.
Premissas internas
 OrdemServico.Customizado.OBS1 
Premissas do cliente
 OrdemServico.Customizado.OBS3 
Estamos à disposição para os esclarecimentos que sobrevierem.
Atenciosamente,
Central de Serviços
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=2157; ClasseConfiguracao=Consolidação Técnica
  - ClasseConfiguracaoId=2288; ClasseConfiguracao=DRE Tela Azul
  - ClasseConfiguracaoId=2508; ClasseConfiguracao=Evidências
  - ClasseConfiguracaoId=2702; ClasseConfiguracao=RFP RFI RFQ 
  - ClasseConfiguracaoId=2731; ClasseConfiguracao=Qualificação de Oportunidade

### [325475] Tarefa "MODELAGEM: Modelagem de Produto
"
Responsável: Responsável atual (papel 36)
**ScriptFormCarregado**
```python
Formulario['NN_CANCELA'].Itens = 'Sim;Não'
```
**ScriptInicio**
```python
#OrdemServico.SetCustom("NN_CONTRATO_COBRA","MODELAGEM")
```
- Operação PR0004 Associar Itens Configuração: Nome=CONSOLIDAÇÃO TÉCNICA
  - anexo "Consolidação Técnica" classes: Consolidação Técnica — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Formulário de Cancelamento
  - NN_CANCELA "Cancela chamado?" [DropDownList String → CPE_NEGOCIOS.NN_CANCELA]
**NN_CANCELA.ScriptModificado**
```python
if Formulario["NN_CANCELA"].Valor == 'Sim':
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = True
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["Justificativa"].Visivel = True
    Formulario["Justificativa"].Valor = None
else:
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = False
    Formulario["Justificativa"].Valor = None
    Formulario["Justificativa"].Visivel = False

OrdemServico.Salva()
```
  - Justificativa (nativo)
  - NN_MOTIVO_CANCELAMENTO "Motivo do cancelamento(após a seleção de um motivo, o chamado será cancelado automaticamente)" [DropDownList String → CPE_NEGOCIOS.NN_MOTIVO_CANCELAMENTO]
**NN_MOTIVO_CANCELAMENTO.ScriptModificado**
```python
motivoCancelamento = Formulario["NN_MOTIVO_CANCELAMENTO"].Valor
justificativa = Formulario["Justificativa"].Valor

OrdemServico.SetCustom("NN_CANCELA", Formulario["NN_CANCELA"].Valor)
OrdemServico.SetCustom("NN_MOTIVO_CANCELAMENTO", motivoCancelamento.ToString())
OrdemServico.Justificativa = justificativa.ToString()
OrdemServico.Salva()

OrdemServico.Cancela(motivoCancelamento.ToString())

OrdemServico.Salva()
```

### [325478] Tarefa "PROSPECÇÃO: Detalhamento do Go do Gestor
"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - Justificativa (nativo) "Detalhamento do Go do Gestor" obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Aprovação do Go do Gestor" classes: Aprovação do Go do Gestor — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [325481] Tarefa "CONTRATAÇÃO:
Elaboração e Aprovação da NT"
Responsável: Favorecido Cobra (papel 277)
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
Formulario['NN_CANCELA'].Itens = 'Sim;Não'


Formulario["LABEL34"].Valor = '<html><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><head><link rel="icon" href=""><style>.forma {text-shadow: 2px 2px #e9f507;}</style></head><body><div class="forma"><justify><font color="#0a1170" size="3"><p><font size="6"><i class="fa fa-cogs fa-fw"></i></font></b></p></div><p>Selecione o tipo de risco associado e insira uma breve descrição sobre.</p><br><p>Operacional</p><p>Compliance /Conduta</p><p>Estratégia</p><p>Liquidez</p><p>Legal</p><p>Cibernético/Segurança da Informação</p><p>Tecnologia da Informação</p><p>Terceiros (Fornecedores) </p></body></html><br>'
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Formulário de Cancelamento
  - NN_CANCELA "Cancela chamado?" [DropDownList String → CPE_NEGOCIOS.NN_CANCELA]
**NN_CANCELA.ScriptModificado**
```python
if Formulario["NN_CANCELA"].Valor == 'Sim':
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = True
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["Justificativa"].Visivel = True
    Formulario["Justificativa"].Valor = None
else:
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = False
    Formulario["Justificativa"].Valor = None
    Formulario["Justificativa"].Visivel = False

OrdemServico.Salva()
```
  - OBS3 "Observação3" [Memo String(2000) → CPE_CONTRATOS.OBS3] obrigatório
  - Justificativa (nativo)
  - NN_MOTIVO_CANCELAMENTO "Motivo do cancelamento(após a seleção de um motivo, o chamado será cancelado automaticamente)" [DropDownList String → CPE_NEGOCIOS.NN_MOTIVO_CANCELAMENTO]
**NN_MOTIVO_CANCELAMENTO.ScriptModificado**
```python
motivoCancelamento = Formulario["NN_MOTIVO_CANCELAMENTO"].Valor
justificativa = Formulario["Justificativa"].Valor

OrdemServico.SetCustom("NN_CANCELA", Formulario["NN_CANCELA"].Valor)
OrdemServico.SetCustom("NN_MOTIVO_CANCELAMENTO", motivoCancelamento.ToString())
OrdemServico.Justificativa = justificativa.ToString()
OrdemServico.Salva()

OrdemServico.Cancela(motivoCancelamento.ToString())

OrdemServico.Salva()
```
  - label34 "Lista de Riscos NI910 (4.7.3)"
  - OBSERVACAO "Descrever Riscos" [TextBox String(2000) → CPE_CSC.OBSERVACAO] obrigatório
  - SIM_NAO10 "É Transação com a Parte Relacionada?" [DropDownList String → CPE_CSC.SIM_NAO10] obrigatório
  - TIPO "Tipo: Contrato / Renovação / Repactuação " [TextBox String → CP_ORDEM_SERVICO.TIPO]
  - NOME_CONTRATO "Nome da parte relacionada" [TextBox String → CPE_CSC.NOME_CONTRATO]
  - CSC_VALOR2 "Valor:" [TextBox Decimal → CPE_CSC.CSC_VALOR2]
  - SIM_NAO2 "É recorrente" [DropDownList String → CPE_CSC.SIM_NAO2] obrigatório
  - CSC_OBS2_A "Diretrizes POL900" [TextBox String(2000) → CPE_CSC.CSC_OBS2_A] obrigatório
  - REFERENCIA_GUIA "Qual a relação entre a BBTS e a outra parte? (POL001)" [TextBox String → CP_ORDEM_SERVICO.REFERENCIA_GUIA]
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: DRE da Nota Técnica — RequeridoInicial=true; IncluirPaginaAssinatura=true
  - anexo "" classes: Nota Técnica — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [325482] EventoIntermediarioMensagem "Aprovação do Cenário"
Destinatário: Seleção de aprovadores (papel 1055)
Config: ListaDestinatarios=gustavo.lustosa@bbts.com.br
;ananias.silva@bbts.com.br;
erica.santos@bbts.com.br
;gustavojose@bbts.com.br;olinto.neto@bbts.com.br
ModeloComunicado: Novos Negócios - Aprovação do Cenário
Corpo do comunicado: Prezados,
Após a avaliação colegiada, a decisão foi favorável para apresentar os preços do projeto OrdemServico.Assunto, conduzido pelo chamado número OrdemServico.Numero, conforme o seguinte cenário:
O OrdemServico.Customizado.COMBOBOX4 foi aprovado.
Estamos à disposição para os esclarecimentos que sobrevierem.
Atenciosamente,
Central de Serviços
Atenciosamente,
Central de Serviços
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=2716; ClasseConfiguracao=Tela Azul

### [325479] Tarefa "PRECIFICAÇÃO:
Estratégia de Preço"
Responsável: Favorecido Cobra (papel 277)
**ScriptFormCarregado**
```python
Formulario['NN_CANCELA'].Itens = 'Sim;Não'

Formulario["COMBOBOX4"].Itens = "Cenário 1;Cenário 2;Cenário 3;Cenário 4;Cenário 5;Cenário 7;Cenário 8;Cenário 9;Cenário10;Cenário 11;Cenário 12;Cenário 13;Cenário 14"

Formulario["APROV_FAVORECIDO"].Habilitado = True


Formulario["APROV_GESTOR_FAVORECIDO"].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - APROV_FAVORECIDO "Aprovação GO / NO GO" [TextBox String → CPE_CSC.APROV_FAVORECIDO] obrigatório
  - APROV_GESTOR_FAVORECIDO "Aprovação Consolidação Técnica" [TextBox String → CPE_CSC.APROV_GESTOR_FAVORECIDO]
  - COMBOBOX4 "Informe o Cenário indicado pela Diretoria" [DropDownList String → CPE_BOOTCAMP.COMBOBOX4] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Evidências — RequeridoInicial=true; IncluirPaginaAssinatura=true
  - anexo "" classes: Tela Azul — RequeridoInicial=true; IncluirPaginaAssinatura=true
  - anexo "" classes: DRE Tela Azul — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Formulário de Cancelamento
  - NN_MOTIVO_CANCELAMENTO "Motivo do cancelamento(após a seleção de um motivo, o chamado será cancelado automaticamente)" [DropDownList String → CPE_NEGOCIOS.NN_MOTIVO_CANCELAMENTO]
**NN_MOTIVO_CANCELAMENTO.ScriptModificado**
```python
motivoCancelamento = Formulario["NN_MOTIVO_CANCELAMENTO"].Valor
justificativa = Formulario["Justificativa"].Valor

OrdemServico.SetCustom("NN_CANCELA", Formulario["NN_CANCELA"].Valor)
OrdemServico.SetCustom("NN_MOTIVO_CANCELAMENTO", motivoCancelamento.ToString())
OrdemServico.Justificativa = justificativa.ToString()
OrdemServico.Salva()

OrdemServico.Cancela(motivoCancelamento.ToString())

OrdemServico.Salva()
```
  - Justificativa (nativo)
  - NN_CANCELA "Cancela chamado?" [DropDownList String → CPE_NEGOCIOS.NN_CANCELA]
**NN_CANCELA.ScriptModificado**
```python
if Formulario["NN_CANCELA"].Valor == 'Sim':
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = True
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["Justificativa"].Visivel = True
    Formulario["Justificativa"].Valor = None
else:
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = False
    Formulario["Justificativa"].Valor = None
    Formulario["Justificativa"].Visivel = False

#OrdemServico.Salva()
```

### [325480] EventoIntermediarioMensagem "Aprovação do Cenário"
Destinatário: Grid Pessoas  (papel 1068)
ModeloComunicado: Novos Negócios - Aprovação do Cenário
Corpo do comunicado: Prezados,
Após a avaliação colegiada, a decisão foi favorável para apresentar os preços do projeto OrdemServico.Assunto, conduzido pelo chamado número OrdemServico.Numero, conforme o seguinte cenário:
O OrdemServico.Customizado.COMBOBOX4 foi aprovado.
Estamos à disposição para os esclarecimentos que sobrevierem.
Atenciosamente,
Central de Serviços
Atenciosamente,
Central de Serviços
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=2716; ClasseConfiguracao=Tela Azul

### [325483] EventoIntermediarioMensagem "Novos Negócios - Resolução de Pendências"
Destinatário: Favorecido Cobra (papel 277)
ModeloComunicado: Novos Negócios - Resolução de Pendências
Corpo do comunicado: Prezado(a) OrdemServico.Customizado.FAVORECIDO_COBRA, 
A OS conduzida pelo chamado nº OrdemServico.Numero (Link.Edicao), referente ao projeto OrdemServico.Assunto , foi(foram) solucionada(s) à(s) pendência(s) indicada(s).
Solicitamos reavaliar e dar continuidade ao processo de estruturação.
Atenciosamente,
Central de Serviços

### [325484] SubProcesso "PRECIFICAÇÃO: Parecer jurídico"
Referência: Abrir chamado para parecer COJUR
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=82; ChamadaAssincrona=true; Codigo=COJUR_DF1; PassaTodosItens=true; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega(189)
```
  - PropertyId=1223; Property=DescricaoDetalhada
**ExpressaoValor**
```python
OrdemServico.GetCustom("NN_OBJETO_PROPOSTA")
```
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
  - CustomPropertyId=129; CustomProperty=EMPRESAS ENVOLVIDAS
**ExpressaoValor**
```python
OrdemServico["NN_APELIDO_PROJETO"]
```
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2157; ClasseConfiguracao=Consolidação Técnica
- Associação: Ativo=true; FraseAssociacao=Portal Negócios -> Consulta Jurídica; FraseInversaAssociacao=Consulta Jurídica -> Portal Negócios; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=NNCOJURRJ; SeparadorSequencial=. | fonte: Portal de Estruturação de Negócios → alvo: Consultas Jurídicas

### [325450] SubProcesso "PRECIFICAÇÃO: Consulta Fisco - Tributária (Estadual, Municipal ou Federal)"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=83; ChamadaAssincrona=true; Codigo=FISCOTRIBUT; PassaTodosItens=true; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega(517)
```
  - CustomPropertyId=3811; CustomProperty=ORIGEM_SERVICO
  - CustomPropertyId=3812; CustomProperty=ORIGEM_PRODUTO
  - CustomPropertyId=3814; CustomProperty=DESTINACAO_BBTS
  - CustomPropertyId=3815; CustomProperty=NN_SIM_NAO
  - CustomPropertyId=2385; CustomProperty=SIM_NAO7
  - CustomPropertyId=2322; CustomProperty=SIM_NAO6
  - CustomPropertyId=3817; CustomProperty=NN_LOCAL_SUPORTE
  - CustomPropertyId=1965; CustomProperty=SIM_NAO3
  - CustomPropertyId=2791; CustomProperty=NN_FORMA_PAGAMENTO
  - CustomPropertyId=2792; CustomProperty=NN_PAIS
  - CustomPropertyId=2793; CustomProperty=NN_LOCAL
  - CustomPropertyId=2289; CustomProperty=SIM_NAO4
  - CustomPropertyId=2794; CustomProperty=NN_BENEFICIO_FISCAL
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
  - CustomPropertyId=1553; CustomProperty=NN_CANCELA
  - PropertyId=1250; Property=Justificativa
  - CustomPropertyId=1554; CustomProperty=NN_MOTIVO_CANCELAMENTO
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2157; ClasseConfiguracao=Consolidação Técnica
- Associação: Ativo=true; FraseAssociacao=Portal Negócios - Fisco; FraseInversaAssociacao=Fisco - Portal Negócios; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=NNFISCO; SeparadorSequencial=. | fonte: Portal de Estruturação de Negócios → alvo: Consulta Fisco - Tributária (Estadual, Municipal ou Federal)

### [325448] Tarefa "MODELAGEM: Estruturação"
Responsável: Fila de Oportunidade (papel 599)
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Empresa
from Venki.Supravizio.Recurso.Custom import Local
#Formulario['NN_CANCELA'].Itens = 'Sim;Não'
#Formulario['NN_AREA_RELACIONAMENTO'].Visivel = False
#Formulario['NN_PRODUTO'].Visivel = False
#Formulario["COMBOBOX1"].Visivel = False
#Formulario["NN_APELIDO_PROJETO"].Visivel = False

if Formulario['NN_CANCELA'].Valor == 'Sim':
    Formulario['Justificativa'].Visivel = True
    Formulario['NN_MOTIVO_CANCELAMENTO'].Visivel = True

else:
    Formulario['Justificativa'].Visivel = False
    Formulario['NN_MOTIVO_CANCELAMENTO'].Visivel = False
    
    
    
#Formulario["COMBOBOX1"].Itens = '3Consult;3Corp;ABC Brasil;Abissal;Aeronáutica;AGU;Aiko;Algar;Alpargatas;ANA - Agência Nacional de Águas e Saneamento Básico;ANABB - Associação Nacional dos Funcionários do Banco do Brasil;Assban - Associação dos bancos;Bacen;Banco BMG;Banco do Nordeste;Banco Inter;Banco Mercantil;Banco Original;Banco Pan;Banco Patagônia;Banco Topázio;Bancorbrás;BANDES;Banestes;Banpará;Banrisul;BASA;BNDES;Bradesco;Brako;Brasil Digital;BRB - Banco de Brasília;BRF Global;Brinks;BV Financeira;Café do Sítio;Caixa Asset;Caixa Cartões;Caixa DTVM;Caixa Previ;Caixa Seguridade;Callink;CBTU;CCBB - Centro Cultural Banco do Brasil;CEB - Companhia Energética de Brasília;CEF - Caixa Econônica Federal;CenturyLink;CERC - Central de Recebíveis;CEUMA - Centro Universitário do Maranhão;CFP - Conselho Federal de Psicologia;CGT Eletrosul;Ciclic;Cidadania;Cielo;CIP - Centro Integrado de Psicologia;Círculo;Claro;Clear Sale;Codevasf;Collins;Conab - Companhia Nacional de Abastecimento;Connectoway;Cooperforte;Correios;Credfisa;CTIS;Dataprev;Daten;Dell;Detran DF;Diebold;Digio;Dotz;EBC - Empresa Brasil de Comunicação;Eccosave;Economus;Eletrobrás;Embasa;Emgea - Empresa Gestora de Ativos;Emgepron;Esdeva;Espaço Y;E-VIDA - Assistência à Saúde;Exército;FazSol;FBB - Fundação Banco do Brasil;Fenabb - Federação Nacional de Assoc Atleticas Bco do Brasil;FGCoop;Finep;Fiocruz;Funcef;Fusan - Fundação Sanepar de Previdência e Assistência Social;Fusesc;Galgo;GEFID;Gemalto;Gerdau;Gesat;Getin BB;Globo;Governo da Bahia;Governo de SC;Grupo Alga;Grupo Conservo;Grupo Saga;Grupos CEU;Hemobrás;Hospital das Clínicas da UFG;Hospital Sírio-Libanês;IBGC;ICESP;Infinity;Infraero;INPI;INSS;Investco;IplanRio;IPOG Brasília;Iprev;Iris;JC Peres Engenharia;JUCESP;Leads;Lenovo;Localiza;M4U;Mapfre;Marinha do Brasil;MDIC;ME e MTPS;Mercantil;Ministério da Economia;Ministério das Cidades;Ministério das Comunicações;Ministério de Minas e Energia;Ministério MDA;MJSP;Montreal;Movera;MPF;Neoenergia;NTT DATA BUSINESS;OAB DF;OI;PCDF;Perto S.A.;Petrobras;Petros;PGFN - Procuradoria Geral da Fazenda Nacional;PJRN;Porto Seguro;Poupex;Prevbep;Prevdata;Previc;Prodam;Prode Pará;Prodemge;Prosegur;PSJC;Qintess;Raviera;Sabin;Salutis;SC Orlando;SCJF-DF;Sebrae;Secex;Sefaz-MA;Sefaz-SP;Serpro;SIA Brasil;Sicoob;Sicredi;Sindifisco;Sistec;SJ Campos;Smilles;Spark;SPTrans;Systech;TC Rondônia;Tecban;Thales/Gemalto;TJ-ES;TJ-SC;TJ-SE;TJ-TO;Todos;TRE Pará;TRE Roraima;TRF 2ª Região;TRF 4º Região;TRT 1ª Região;Valec;Valor Invest;Via Varejo;Viridi e A5;Zoom Tecnologia'
```
- Operação PR0001 Preencher Campos
  - APROVADOR_PB "GESTOR(ES) DO(S)  PRODUTO(S) " [DataGrid RecordList → Z_00143_APROVADOR_PB.APROVADOR_PB] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna APROVADORES obrigatório
  - GRID_PESSOAS "Tomar Conhecimento da Oportunidade" [DataGrid RecordList → Z_00143_GRID_PESSOAS.GRID_PESSOAS] — FormaEdicaoWeb=JanelaPopup
    - coluna PESSOAS
  - NN_PORTFOLIO "Referência de mercado (fornecedor/intervenientes/concorrentes/normas, etc)" [Memo String(2000) → CPE_NEGOCIOS.NN_PORTFOLIO] obrigatório
  - NN_SEGMENTO "Segmento de Mercado" [DropDownList String → CPE_NEGOCIOS.NN_SEGMENTO] obrigatório
**NN_SEGMENTO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Local
if Formulario["NN_SEGMENTO"].Valor == 'Mercado':
    Formulario["COMBOBOX1"].Itens = '3Corp;AIDC;Aiko;Algar;Assban;Banco ABC;Banco Inter;Banco Original;Banco Pan;Banco Topázio;Banrisul;Basa;Bradesco;Brasil Digital;Brinks;Centurylink;Ceuma;Clear Sales;Connectoway;Conservo;Credfisa;Ctis;Daten;Dell;Digio;Dotz;Engepron;Engie;Envestcon;Espaço Y;E-Vida;FazSol;FGCOOP;Galgo;Gemalto;Gerdau;Globo;Grupo Saga;HCL Tech;IBCG;ICESP;Infinity;INPI;Lenovo;Lever Tech;Localiza;M4U;Mercantil;Montreal;Oi;Perto;Porto Seguro;PrevData;Prevpeb;Prosegur;Qintess;Ririera;Salutis;Sicob;Sicredi;Smiles;Thales;Valor Invest;Via Varejo;Viridi;Vivo;Zoom;SPDM - ASSOCIACAO PAULISTA PARA O DESENVOLVIMENTO DA MEDICINA;AUDIO CODES;Shooting House;Grupo Concórdia;Grupo Artico;AIDC;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True
    
elif Formulario["NN_SEGMENTO"].Valor == 'Governo':
    Formulario["COMBOBOX1"].Itens = 'Aeronáutica;AGU;ANA;Bacen;Banco do Nordeste;BANDES;Banestes;Banpará;BNDES;BRB;Caixa;Caixa Asset;Caixa Cartões;Caixa DTVM;Caixa Previ;Caixa Seguridade;Câmara dos Deputados;CBTU;CEB;CFP;Conab;Correios;Dataprev;Detran DF;EBC;Eletrobrás;Embasa;Emgea;Exército;Finep;FUNPREV PIAUÍ;Fusan;Governo da Bahia;Governo da SC;Governo do ACRE;HC-UFG;Hemobrás;IPLanrio;IPMT Teresina;Iprev;JUCESP;MDIC;ME e MTPS;Ministério das Comunicações;Ministério MDA;MME;MPF;Neoenergia;OAB;PCDF;Petrobrás;PJRN;Prevdata;Procuradoria-Geral da Fazenda Nacional;Prodam;Prode Pará;Prodemge;SCJF-DF;Sebrae;Sefaz MA;SEFAZ SP;Serpro;SJ Campos;SPTrans;TC Rondônia;TJ ES;TJ Sergipe;TJ SC;TJ TO;TRE Pará;TRE Roraima;TRF1ª;TRF2ª;TRF4ª;Valec;ANATEL;TRT4;Tribunal de Contas/RR;Tribunal de Contas/GO;SUPEL/RO;Pref. de Rio Branco/AC;CREA/PR;Detran/PE;Defensoria Pública/BA;Dataprev;Tribunal de Justiça/BA;Pref. de Schroeder/SC;Fund. Oswaldo Cruz/RJ;SEPLOG/SE;SESC/SE;Sec. de Seg. Pública/PI;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True

elif Formulario["NN_SEGMENTO"].Valor == 'Banco do Brasil':
    Formulario["COMBOBOX1"].Itens = 'USI;DITEC;DIOPE;DISEC;DIGOV;DICRE;DICOI;UCS;DIREC;UGE;UCR;DICOR;UAC;DINED;UAN;DIRAG;DIMEP;DIEMP;DIJUR;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True
    
elif Formulario["NN_SEGMENTO"].Valor == 'ELBB':
    Formulario["COMBOBOX1"].Itens = 'ALELO;ALIANÇA DO BRASIL SEGUROS;ALIANÇA PAG;ALPHA SERV. DE AUTOATENDIMENTO;ATIVOS S.A. SEC. DE CRÉD. FINANCEIROS;BANCO PATAGONIA;BANCO VOTORANTIM;BB ADMINISTRADORA DE CARTÕES DE CRÉDITO;BB AG;BB AMERICAS;BB ASSET;BB ASSET MANAGEMENT IRELAND;BB BANCO DE INVESTIMENTO (BB-BI);BB CAYMAN ISLANDS HOLDING (BB-CI);BB CONSÓRCIOS;BB CORRETORA DE SEGUROS E ADMI.DE BENS S.A. (BB CORRETORA);BB ELO CARTÕES;BB LEASING;BB MAPFRE PARTICIPAÇÕES S.A;BB PREVIDÊNCIA;BB SECURITIES;BB SEGURIDADE;BB SEGUROS;BB USA HOLDING COMPANY INC;BRASIL DENTAL;BRASILCAP;BRASILPREV SEG. E PREV. S.A.;BRASILSEG;BV EMPREEND. E PARTICIPAÇÕES;BV INVEST. ALTERN. E GEST. DE RECUR;CADAM OVERSEAS LTD;CADAM;CAIXA DE ASSISTÊNCIA DOS EMPREGADOS (SIM);CÂMARA INTERBANCÁRIA DE PAGAMENTOS (CIP);CASSI;CATENO;CIA. HIDROMINERAL PIRATUBA;CICLIC;CIELO;CIELO S.A.;ECONOMUS;ELO HOLDING FINANCEIRA;ELO SERVIÇOS;ELOPAR;ESTRUT. BRAS. DE PROJ.;FUNDAÇÃO BANCO DO BRASIL (FBB);FUNDAÇÃO CODESC DE SEGURIDADE SOCIAL (FUSESC);GALGO SISTEMAS DE INFORMAÇÃO;GPAT COMPAÑIA FINANCIERA;KAOLIN INTERNATIONAL N.V.;KARTRA PARTICIPAÇÕES;LIVELO;MERCHANT E-SOLUTIONS;PAGGO SOLUÇÕES E MEIOS DE PAGAMENTOS;PREVBEP;PREVI;PROMOTIVA;QUOD;SERVINET SERVIÇOS;STELO;TBFORTE TRANSP. VALORES BRASIL FORTE;TBNET COM., LOCAÇÃO E ADM.;TECNOLOGIA BANCÁRIA;UBS BB SERV. \ ASSE. FIN. PART.;VOTORANTIM CORR. SEGUROS;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True
```
  - CNPJ "CNPJ do Cliente" [TextBox String → CP_ORDEM_SERVICO.CNPJ] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00\\.000\\.000\\/0000\\-00"}
  - COMBOBOX1 "Clientes" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
  - NN_OBJETO_PROPOSTA "Objetivo do Negócio (Problema do cliente)" [Memo String(2000) → CP_ORDEM_SERVICO.NN_OBJETO_PROPOSTA] obrigatório
  - PREMISSA_DOD "Premissas/Restrições/Volumetria" [Memo String(2000) → CP_ORDEM_SERVICO.PREMISSA_DOD] obrigatório
  - NN_GERENCIA_NEGOCIO "Área gestora do produto/serviço" [DropDownList String → CP_ORDEM_SERVICO.NN_GERENCIA_NEGOCIO] obrigatório
  - NN_LINHA_NEGOCIO "Linha de Negócio" [DropDownList String → CPE_NEGOCIOS.NN_LINHA_NEGOCIO] obrigatório
**NN_LINHA_NEGOCIO.ScriptModificado**
```python
from Venki.Supravizio.Configuracao.Custom import Software
if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Infraestrutura e Disponibilidade':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Disponibilidade Operacional de TAA;Disponibilidade Operacional de Bens de Automação Bancária;Monitoração de Ambientes;Infraestrutura de Data Center'



if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Gestão de Segurança':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Disponibilidade Operacional Sistema de Alarme, Gerador de Neblina, Fechadura de Retardo, Rastreadores, AudioBidirecional e outros;Disponibilidade Operacional de Sistema de Imagens;Assistência Técnica de sistemas de Portas Giratórias, CFTV e demais equipamentos legados;PSIM - Plataforma de Integração e Gerenciamento de informações de segurança física;Centro de Operação de Cyber Segurança'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Comunicação e Conectividade':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Intevia(SMS);Intevia (E-mail Marketing);Teya (Outsourcing de Telefonia)'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Canais e Backoffice':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Centrais de Relacionamento e Telecobrança;Cobrança Extrajudicial de dívidas;Gestão Eletrônica de Documentos (GED);Kit Pré-Ajuizamento;Microfilmagem'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Soluções Digitais':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Plataformas (Aprovve Service);Hiperautomação;Fábrica de Software'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Soluções de Parcerias Estratégicas':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Interoperabilidade - (HIVEPlace);Revenda Especializada'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Correspondente Bancário':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Agente de Crédito Rural (ACR);Gestão da Rede de Correspondentes Bancários BB;Representação Comercial'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Outros':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Outros'
```
  - NN_PRODUTO "Produto" [DropDownList String → CPE_NEGOCIOS.NN_PRODUTO] obrigatório
  - NN_STATUS_PROJETO "Status projeto" [DropDownList String → CPE_NEGOCIOS.NN_STATUS_PROJETO] obrigatório
  - NN_PRAZO_ESTIMADO "Prazo do contrato estimado" [DropDownList String → CPE_NEGOCIOS.NN_PRAZO_ESTIMADO] obrigatório
  - NN_PRODUTO_EXISTENTE "Produto do portfólio?" [DropDownList String → CPE_NEGOCIOS.NN_PRODUTO_EXISTENTE] obrigatório
  - SIM_NAO "Projeto contido no orçamento?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
  - FAVORECIDO_COBRA "Responsável Estruturação" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - NN_DATA_REPROG "Resposta ao Cliente" [DataGrid RecordList → Z_00143_NN_DATA_REPROG.NN_DATA_REPROG] — FormaEdicaoWeb=JanelaPopup
    - coluna DATA obrigatório
    - coluna SITUACAO obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Formulário de Cancelamento
  - NN_CANCELA "Cancela chamado?" [DropDownList String → CPE_NEGOCIOS.NN_CANCELA]
**NN_CANCELA.ScriptModificado**
```python
if Formulario["NN_CANCELA"].Valor == 'Sim':
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = True
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["Justificativa"].Visivel = True
    Formulario["Justificativa"].Valor = None
else:
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = False
    Formulario["Justificativa"].Valor = None
    Formulario["Justificativa"].Visivel = False

OrdemServico.Salva()
```
  - Justificativa (nativo)
  - NN_MOTIVO_CANCELAMENTO "Motivo do cancelamento(após a seleção de um motivo, o chamado será cancelado automaticamente)" [DropDownList String → CPE_NEGOCIOS.NN_MOTIVO_CANCELAMENTO]
**NN_MOTIVO_CANCELAMENTO.ScriptModificado**
```python
motivoCancelamento = Formulario["NN_MOTIVO_CANCELAMENTO"].Valor
justificativa = Formulario["Justificativa"].Valor

OrdemServico.SetCustom("NN_CANCELA", Formulario["NN_CANCELA"].Valor)
OrdemServico.SetCustom("NN_MOTIVO_CANCELAMENTO", motivoCancelamento.ToString())
OrdemServico.Justificativa = justificativa.ToString()
OrdemServico.Salva()

OrdemServico.Cancela(motivoCancelamento.ToString())

OrdemServico.Salva()
```

### [325449] Tarefa "PRECIFICAÇÃO: Inserir DRE
"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração
  - anexo "DRE" classes: DRE — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [325451] Tarefa "PROSPECÇÃO: Registrar Aprovação"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
OrdemServico["APROV_FAVORECIDO"] = "Aprovado"

AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos
  - APROV_FAVORECIDO "Aprovação GO / NO GO" [TextBox String → CPE_CSC.APROV_FAVORECIDO]

### [325452] EventoIntermediarioMensagem "Preços de Referência"
Destinatário: Favorecido Cobra (papel 277)
ModeloComunicado: Novos Negócios - Preços de Referência
Corpo do comunicado: Prezados,
A equipe Comercial encerrou a etapa de Negociação do projeto OrdemServico.Assunto, conduzido pelo chamado número OrdemServico.Numero ( Link.Edicao Worklist ).
Solicitamos dar continuidade no processo de estruturação.
Estamos à disposição para os esclarecimentos que sobrevierem.
Atenciosamente,
Central de Serviços

### [325453] EventoIntermediarioMensagem "Aviso de Pendência"
Destinatário: Cliente (papel 18)
ModeloComunicado: Novos Negócios - Aviso de Pendências
Corpo do comunicado: Prezado(a) OrdemServico.Cliente.Nome ,
A OS conduzida pelo chamado nº OrdemServico.Numero ( Link.Edicao ), referente ao projeto OrdemServico.Assunto , possui à(s) seguinte(s) pendência(s):
 Complemento1 
Solicitamos providência essa(s) informação(ões), para darmos continuidade ao processo de estruturação.
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoGateway("DADOSCONFEREM")
```

### [325454] SubProcesso "MODELAGEM: Acionamento do Licenter"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1066; ChamadaAssincrona=true; PassaTodosItens=true; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2131; ClasseConfiguracao=Proposta Comercial
  - SuperClasse=Artefato; ClasseConfiguracaoId=2157; ClasseConfiguracao=Consolidação Técnica
  - SuperClasse=Artefato; ClasseConfiguracaoId=1768; ClasseConfiguracao=Nota Técnica
  - SuperClasse=Artefato; ClasseConfiguracaoId=2292; ClasseConfiguracao=Minuta
  - SuperClasse=Artefato; ClasseConfiguracaoId=2231; ClasseConfiguracao=Modelo
  - SuperClasse=Artefato; ClasseConfiguracaoId=2774; ClasseConfiguracao=Aprovação do Go do Gestor
  - SuperClasse=Artefato; ClasseConfiguracaoId=2732; ClasseConfiguracao=DRE da Nota Técnica
  - SuperClasse=Artefato; ClasseConfiguracaoId=2733; ClasseConfiguracao=Preço de referência
- Associação: Ativo=true; FraseAssociacao=Portal de Estruturação de Negócios (Projeto) -> Acionamento do Licenter; FraseInversaAssociacao=Acionamento do Licenter -> Portal de Estruturação de Negócios (Projeto); CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=ACIONAMENTOLICENTER; SeparadorSequencial=. | fonte: Portal de Estruturação de Negócios → alvo: Acionamento do Licenter

### [325455] SubProcesso "PRECIFICAÇÃO: Precificação e Orçamento"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=80; ChamadaAssincrona=true; Codigo=PRECORC; PassaTodosItens=true; Configuracao={"ExibirBotaoNovaSubprocessos":true, "ValidacaoFinalizacao":"Nenhuma restri\u00e7\u00e3o"}
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega(540)
```
  - CustomPropertyId=939; CustomProperty=NN_NOME_PROJETO
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2157; ClasseConfiguracao=Consolidação Técnica
- RetornoItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2158; ClasseConfiguracao=Planilha de preço (versão final)
- Associação: Ativo=true; FraseAssociacao=Portal Negócios - Precificação; FraseInversaAssociacao=Precificação - Portal Negócios; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=NNPRECIF; SeparadorSequencial=. | fonte: Portal de Estruturação de Negócios → alvo: Precificação e Orçamento

### [325456] EventoFinal ""
Responsável: Responsável atual (papel 36)

### [325457] EventoIntermediarioMensagem "Proposta Comercial"
Destinatário: Favorecido Cobra (papel 277)
ModeloComunicado: Novos Negócios - Proposta Comercial
Corpo do comunicado: Prezados,
A equipe Comercial informou que o Cliente aceitou a Proposta Comercial do projeto OrdemServico.Assunto, conduzido pelo chamado número OrdemServico.Numero ( Link.Edicao Worklist ).
Solicitamos dar continuidade no processo de estruturação.
Solicitamos dar continuidade no processo de estruturação.
Atenciosamente,
Central de Serviços

### [325458] Tarefa "NEGOCIAÇÃO:
Preço Referência"
Responsável: Cliente (papel 18)
**ScriptFormCarregado**
```python
Formulario['NN_CANCELA'].Itens = 'Sim;Não'
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Formulário de Cancelamento
  - NN_CANCELA "Cancela chamado?" [DropDownList String → CPE_NEGOCIOS.NN_CANCELA]
**NN_CANCELA.ScriptModificado**
```python
if Formulario["NN_CANCELA"].Valor == 'Sim':
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = True
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["Justificativa"].Visivel = True
    Formulario["Justificativa"].Valor = None
else:
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = False
    Formulario["Justificativa"].Valor = None
    Formulario["Justificativa"].Visivel = False

OrdemServico.Salva()
```
  - Justificativa (nativo)
  - NN_MOTIVO_CANCELAMENTO "Motivo do cancelamento(após a seleção de um motivo, o chamado será cancelado automaticamente)" [DropDownList String → CPE_NEGOCIOS.NN_MOTIVO_CANCELAMENTO]
**NN_MOTIVO_CANCELAMENTO.ScriptModificado**
```python
motivoCancelamento = Formulario["NN_MOTIVO_CANCELAMENTO"].Valor
justificativa = Formulario["Justificativa"].Valor

OrdemServico.SetCustom("NN_CANCELA", Formulario["NN_CANCELA"].Valor)
OrdemServico.SetCustom("NN_MOTIVO_CANCELAMENTO", motivoCancelamento.ToString())
OrdemServico.Justificativa = justificativa.ToString()
OrdemServico.Salva()

OrdemServico.Cancela(motivoCancelamento.ToString())

OrdemServico.Salva()
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Preço de referência" classes: Preço de referência — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos
  - NN_DATA_ENVIO_PRECO "Data de envio do preço de referência" [DataGrid RecordList → Z_00143_NN_DATA_ENVIO_PRECO.NN_DATA_ENVIO_PRECO] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna DATA_ENVIO_PROPOSTA obrigatório
    - coluna NN_PROPOSTA_COMERCIAL obrigatório
    - coluna VALOR_GLOBAL obrigatório

### [325459] SubProcesso "PROSPECÇÃO: Aprovar GO ou No Go"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=933; ChamadaAssincrona=true; PassaTodosItens=true; RetornaTodosItens=true
- ValoresInputs:
  - CustomPropertyId=506; CustomProperty=PREMISSA_DOD
  - CustomPropertyId=1778; CustomProperty=NN_PORTFOLIO
  - CustomPropertyId=1779; CustomProperty=NN_SEGMENTO
  - CustomPropertyId=1074; CustomProperty=COMBOBOX1
  - CustomPropertyId=240; CustomProperty=CNPJ
  - CustomPropertyId=958; CustomProperty=NN_GERENCIA_NEGOCIO
  - CustomPropertyId=1781; CustomProperty=NN_LINHA_NEGOCIO
  - CustomPropertyId=1782; CustomProperty=NN_PRODUTO
  - CustomPropertyId=1785; CustomProperty=NN_STATUS_PROJETO
  - CustomPropertyId=1783; CustomProperty=NN_PRAZO_ESTIMADO
  - CustomPropertyId=1950; CustomProperty=NN_PRODUTO_EXISTENTE
  - CustomPropertyId=1002; CustomProperty=SIM_NAO
  - CustomPropertyId=2551; CustomProperty=APROVADOR_PB
  - CustomPropertyId=3636; CustomProperty=GRID_PESSOAS
  - CustomPropertyId=3352; CustomProperty=CANALDEVENDA
  - CustomPropertyId=3585; CustomProperty=CANALDEVENDA1
  - CustomPropertyId=3598; CustomProperty=NN_DATAPICKER1
  - CustomPropertyId=3613; CustomProperty=NN_DATA_REPROG
  - CustomPropertyId=3587; CustomProperty=NN_NUMERO_NDA
  - CustomPropertyId=3630; CustomProperty=NN_POC
  - CustomPropertyId=952; CustomProperty=NN_OBJETO_PROPOSTA
  - CustomPropertyId=44; CustomProperty=MOTIVO
  - CustomPropertyId=3665; CustomProperty=COMBOBOX4
  - CustomPropertyId=2511; CustomProperty=APROV_FAVORECIDO
  - CustomPropertyId=2514; CustomProperty=APROV_GESTOR_FAVORECIDO
  - CustomPropertyId=3609; CustomProperty=NN_FORMACONTRATACAO
- Associação: Ativo=true; FraseAssociacao=Portal de Estruturação de  Negócios -> Aprovação do Go ou No Go; FraseInversaAssociacao=Aprovação do Go ou No Go -> Portal de Estruturação de Negócios; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=NNAPROVACAOGONOGO; SeparadorSequencial=. | fonte: Portal de Estruturação de Negócios → alvo: Aprovação Go /no Go (Abrir somente uma OS)

### [325460] Tarefa "PROSPECÇÃO: 
Ajustar Informações"
Responsável: Cliente (papel 18)
**ScriptFormCarregado**
```python
#Formulario['NN_CANCELA'].Itens = 'Sim;Não'
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Edital" classes: Edital — RequeridoInicial=true; IncluirPaginaAssinatura=true
  - anexo "Documentos Diversos" classes: Outros documentos — RequeridoInicial=true; IncluirPaginaAssinatura=true
  - anexo "Projeto Básico" classes: Projeto Básico — RequeridoInicial=true; IncluirPaginaAssinatura=true
  - anexo "RFP" classes: RFP RFI RFQ  — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo de documento" classes: Documentos — RequeridoInicial=true; PermiteMultiplosItens=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Qualificação da Oportunidade" classes: Qualificação de Oportunidade — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos
  - GRID_PESSOAS "Tomar Conhecimento da Oportunidade (Gerex e Super)" [DataGrid RecordList → Z_00143_GRID_PESSOAS.GRID_PESSOAS] — FormaEdicaoWeb=JanelaPopup
    - coluna PESSOAS
  - NN_OBJETO_PROPOSTA "Objetivo do Negócio (Necessidade do cliente)" [Memo String(2000) → CP_ORDEM_SERVICO.NN_OBJETO_PROPOSTA] obrigatório
  - PREMISSA_DOD "Premissas/Restrições/Volumetria" [Memo String(2000) → CP_ORDEM_SERVICO.PREMISSA_DOD] obrigatório
  - NN_PORTFOLIO "Referência de mercado (fornecedor/intervenientes/concorrentes/normas, etc)" [Memo String(2000) → CPE_NEGOCIOS.NN_PORTFOLIO] obrigatório
  - NN_SEGMENTO "Segmento de Mercado" [DropDownList String → CPE_NEGOCIOS.NN_SEGMENTO] obrigatório
**NN_SEGMENTO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Local
if Formulario["NN_SEGMENTO"].Valor == 'Mercado':
    Formulario["COMBOBOX1"].Itens = '3Corp;AIDC;Aiko;Algar;Assban;Banco ABC;Banco Inter;Banco Original;Banco Pan;Banco Topázio;Banrisul;Basa;Bradesco;Brasil Digital;Brinks;Centurylink;Ceuma;Clear Sales;Connectoway;Conservo;Credfisa;Ctis;Daten;Dell;Digio;Dotz;Engepron;Engie;Envestcon;Espaço Y;E-Vida;FazSol;FGCOOP;Galgo;Gemalto;Gerdau;Globo;Grupo Saga;HCL Tech;IBCG;ICESP;Infinity;INPI;Lenovo;Lever Tech;Localiza;M4U;Mercantil;Montreal;Oi;Perto;Porto Seguro;PrevData;Prevpeb;Prosegur;Qintess;Ririera;Salutis;Sicob;Sicredi;Smiles;Thales;Valor Invest;Via Varejo;Viridi;Vivo;Zoom;OUTROS'
    
elif Formulario["NN_SEGMENTO"].Valor == 'Governo':
    Formulario["COMBOBOX1"].Itens = 'Aeronáutica;AGU;ANA;Bacen;Banco do Nordeste;BANDES;Banestes;Banpará;BNDES;BRB;Caixa;Caixa Asset;Caixa Cartões;Caixa DTVM;Caixa Previ;Caixa Seguridade;Câmara dos Deputados;CBTU;CEB;CFP;Conab;Correios;Dataprev;Detran DF;EBC;Eletrobrás;Embasa;Emgea;Exército;Finep;FUNPREV PIAUÍ;Fusan;Governo da Bahia;Governo da SC;Governo do ACRE;HC-UFG;Hemobrás;IPLanrio;IPMT Teresina;Iprev;JUCESP;MDIC;ME e MTPS;Ministério das Comunicações;Ministério MDA;MME;MPF;Neoenergia;OAB;PCDF;Petrobrás;PJRN;Prevdata;Procuradoria-Geral da Fazenda Nacional;Prodam;Prode Pará;Prodemge;SCJF-DF;Sebrae;Sefaz MA;SEFAZ SP;Serpro;SJ Campos;SPTrans;TC Rondônia;TJ ES;TJ Sergipe;TJ SC;TJ TO;TRE Pará;TRE Roraima;TRF1ª;TRF2ª;TRF4ª;Valec;OUTROS'

elif Formulario["NN_SEGMENTO"].Valor == 'Banco do Brasil':
    Formulario["COMBOBOX1"].Itens = 'USI;DITEC;DIOPE;DISEC;DIGOV;DICRE;DICOI;UCS;DIREC;UGE;UCR;DICOR;UAC;DINED;UAN;DIRAG;DIMEP;DIEMP;DIJUR;OUTROS'
    
elif Formulario["NN_SEGMENTO"].Valor == 'ELBB':
    Formulario["COMBOBOX1"].Itens = 'ALELO;ALIANÇA DO BRASIL SEGUROS;ALIANÇA PAG;ALPHA SERV. DE AUTOATENDIMENTO;ATIVOS S.A. SEC. DE CRÉD. FINANCEIROS;BANCO PATAGONIA;BANCO VOTORANTIM;BB ADMINISTRADORA DE CARTÕES DE CRÉDITO;BB AG;BB AMERICAS;BB ASSET;BB ASSET MANAGEMENT IRELAND;BB BANCO DE INVESTIMENTO (BB-BI);BB CAYMAN ISLANDS HOLDING (BB-CI);BB CONSÓRCIOS;BB CORRETORA DE SEGUROS E ADMI.DE BENS S.A. (BB CORRETORA);BB ELO CARTÕES;BB LEASING;BB MAPFRE PARTICIPAÇÕES S.A;BB PREVIDÊNCIA;BB SECURITIES;BB SEGURIDADE;BB SEGUROS;BB USA HOLDING COMPANY INC;BRASIL DENTAL;BRASILCAP;BRASILPREV SEG. E PREV. S.A.;BRASILSEG;BV EMPREEND. E PARTICIPAÇÕES;BV INVEST. ALTERN. E GEST. DE RECUR;CADAM OVERSEAS LTD;CADAM;CAIXA DE ASSISTÊNCIA DOS EMPREGADOS (SIM);CÂMARA INTERBANCÁRIA DE PAGAMENTOS (CIP);CASSI;CATENO;CIA. HIDROMINERAL PIRATUBA;CICLIC;CIELO;CIELO S.A.;ECONOMUS;ELO HOLDING FINANCEIRA;ELO SERVIÇOS;ELOPAR;ESTRUT. BRAS. DE PROJ.;FUNDAÇÃO BANCO DO BRASIL (FBB);FUNDAÇÃO CODESC DE SEGURIDADE SOCIAL (FUSESC);GALGO SISTEMAS DE INFORMAÇÃO;GPAT COMPAÑIA FINANCIERA;KAOLIN INTERNATIONAL N.V.;KARTRA PARTICIPAÇÕES;LIVELO;MERCHANT E-SOLUTIONS;PAGGO SOLUÇÕES E MEIOS DE PAGAMENTOS;PREVBEP;PREVI;PROMOTIVA;QUOD;SERVINET SERVIÇOS;STELO;TBFORTE TRANSP. VALORES BRASIL FORTE;TBNET COM., LOCAÇÃO E ADM.;TECNOLOGIA BANCÁRIA;UBS BB SERV. \ ASSE. FIN. PART.;VOTORANTIM CORR. SEGUROS;OUTROS'
```
  - COMBOBOX1 "Clientes" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
  - CNPJ "CNPJ do Cliente" [TextBox String → CP_ORDEM_SERVICO.CNPJ] obrigatório — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00\\.000\\.000\\/0000\\-00"}
  - NN_GERENCIA_NEGOCIO "Área gestora do produto/serviço" [DropDownList String → CP_ORDEM_SERVICO.NN_GERENCIA_NEGOCIO] obrigatório
  - NN_LINHA_NEGOCIO "Linha de Negócio" [DropDownList String → CPE_NEGOCIOS.NN_LINHA_NEGOCIO] obrigatório
**NN_LINHA_NEGOCIO.ScriptModificado**
```python
from Venki.Supravizio.Configuracao.Custom import Software
if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Infraestrutura e Disponibilidade':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Disponibilidade Operacional de TAA;Disponibilidade Operacional de Bens de Automação Bancária;Monitoração de Ambientes;Infraestrutura de Data Center;Assistência Técnica de Sistemas de Portas Giratórias, Sala On-Line e Nobreak'



if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Gestão de Segurança':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Disponibilidade Operacional de Sistema de Alarme e Dispositivos de Resposta;Disponibilidade Operacional de Sistema de Imagens;PSIM - Plataforma de Integração e Gerenciamento de informações de segurança física;Cross Data Team (CDT);Managed Security Services Provider ¿ MSSP (Centro de Operação de Cyber Segurança ¿ SOC N1/N2/N3, Professional Security Services, Phishing, Pentest e Gestão de Vulnerabilidade)'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Comunicação e Conectividade':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Intevia ¿ Mensageria SMS;Intevia ¿ Mensageria e e-mail marketing;Teya - Outsourcing de Telefonia (Plataforma de Voz e Vídeo)'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Canais e Backoffice':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Centrais de Relacionamento e Telecobrança;Cobrança Extrajudicial de Dívidas;Gestão Eletrônica De Documentos (GED);Kit Pré-Ajuizamento;Microfilmagem'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Produtos e Soluções Digitais':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Fábrica de Software;Plataformas (Aprovve Service);Hiperautomação (LowCode)'



if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Soluções de Parcerias Estratégicas':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Interoperabilidade (HIVEPlace);Revenda Especializada (Licenter)'



if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Correspondente Bancário':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Gestão de Correspondentes Bancários;Representação Comercial;Agente de Crédito Rural (ACR)'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Outros':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Outros'
```
  - NN_PRODUTO "Produto" [DropDownList String → CPE_NEGOCIOS.NN_PRODUTO] obrigatório
  - NN_STATUS_PROJETO "Status projeto" [DropDownList String → CPE_NEGOCIOS.NN_STATUS_PROJETO] obrigatório
  - NN_PRAZO_ESTIMADO "Prazo do contrato estimado" [DropDownList String → CPE_NEGOCIOS.NN_PRAZO_ESTIMADO] obrigatório
  - NN_PRODUTO_EXISTENTE "Produto do portfólio?" [DropDownList String → CPE_NEGOCIOS.NN_PRODUTO_EXISTENTE] obrigatório
  - SIM_NAO "Projeto contido no orçamento?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
  - NN_DATA_REPROG "Resposta ao Cliente" [DataGrid RecordList → Z_00143_NN_DATA_REPROG.NN_DATA_REPROG] — FormaEdicaoWeb=JanelaPopup
    - coluna SITUACAO obrigatório
    - coluna DATA obrigatório
  - APROVADOR_PB "GESTOR(ES) DO(S) PRODUTO(S) ¿ Gediv" [DataGrid RecordList → Z_00143_APROVADOR_PB.APROVADOR_PB] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna APROVADORES obrigatório
- Operação PR0001 Preencher Campos
  - NN_DATAPICKER1 "Data inicio da Prospecção" [DatePicker DateTime → CPE_NEGOCIOS.NN_DATAPICKER1] obrigatório
  - NN_NUMERO_NDA "Número do Chamado do NDA " [TextBox String → CPE_NEGOCIOS.NN_NUMERO_NDA]
  - NN_DATA_REPROG "Resposta ao Cliente" [DataGrid RecordList → Z_00143_NN_DATA_REPROG.NN_DATA_REPROG] — FormaEdicaoWeb=JanelaPopup
    - coluna DATA obrigatório
    - coluna SITUACAO obrigatório
  - NN_FORMACONTRATACAO "Forma de Contratação" [DropDownList String → CPE_HOMOLOGACAO.NN_FORMACONTRATACAO] obrigatório
  - NN_POC "Teve POC/Piloto/Degustação" [DropDownList String → CPE_NEGOCIOS.NN_POC] obrigatório
**NN_POC.ScriptModificado**
```python
if Formulario['NN_POC'].Valor == 'Não':
    Formulario['MOTIVO'].Visivel = False
    Formulario['MOTIVO'].Habilitado = False
    
else:
    Formulario['MOTIVO'].Visivel = True
    Formulario['MOTIVO'].Habilitado = True
```
  - MOTIVO "Detalhamento POC/Piloto/Degustação" [Memo String(1500) → CP_ORDEM_SERVICO.MOTIVO] obrigatório
  - CANALDEVENDA "Contato(s) do Cliente" [DataGrid RecordList → Z_00143_CANALDEVENDA.CANALDEVENDA] obrigatório — FormaEdicaoWeb=JanelaPopup; LarguraJanelaPopup=300
    - coluna EMAILCLIENT obrigatório
    - coluna CARGOCLIENT obrigatório
    - coluna TELLCLIENT obrigatório
    - coluna DATARESPCLIENT obrigatório
    - coluna SETCLIENT obrigatório
    - coluna DATAINIPROSP obrigatório
    - coluna NOMECTTCLIENT obrigatório
  - CANALDEVENDA1 "Canal de Venda" [DropDownList String(900) → CPE_NEGOCIOS.CANALDEVENDA1] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo (Opcional):" classes: Arquivo — RequeridoInicial=true; PermiteMultiplosItens=true; IncluirPaginaAssinatura=true
- Acoes:
  - Acao=Categorizar; Percentual=100; CodigoGrupoANO=2a9284dc-01df-4354-85b1-211cff2cbfb2; CategoriaId=2; Categoria=Baixa

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
### papel 1068: Grid Pessoas 
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
pesquisa01 = DB.ExecuteDataTable("select ID_OCORRENCIA, PESSOAS FROM Z_00143_GRID_PESSOAS WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")

for pessoa in pesquisa01.Rows:    
    aprovadores = Pessoa.Carrega(Convert.ToInt32(pessoa["PESSOAS"]))
    Atores.Adiciona(aprovadores)
```
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 599: Fila de Oportunidade
Tipo=RelacaoGrupos
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
### papel 842: Aprovadores Projeto Básico
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
#pesquisa01 = DB.ExecuteDataTable("select ID_OCORRENCIA, APROVADORES FROM Z_00143_APROVADOR_PB WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")

tentativa = 0

while tentativa < 5:
    pesquisa01 = DB.ExecuteDataTable("select ID_OCORRENCIA, APROVADORES FROM Z_00143_APROVADOR_PB WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
    tentativa = tentativa + 1
    for pessoa in pesquisa01.Rows:    
        aprovadores = Pessoa.Carrega(Convert.ToInt32(pessoa["APROVADORES"]))
        Atores.Adiciona(aprovadores)
```
### papel 544: Cliente e Responsavel Atual
Tipo=Composto
- composto por: Cliente (PessoaOrdemServico)
- composto por: Responsável atual (PessoaOrdemServico)
### papel 1055: Seleção de aprovadores
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
pesquisa01 = DB.ExecuteDataTable("select ID_OCORRENCIA, APROVADORES FROM Z_00143_SELECAPROV WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")

for pessoa in pesquisa01.Rows:    
    aprovadores = Pessoa.Carrega(Convert.ToInt32(pessoa["APROVADORES"]))
    Atores.Adiciona(aprovadores)
```

## Campos customizados usados (definição global)

### SIM_NAO6 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO6
Itens: Sim;Não

### NN_LOCAL_SUPORTE — Local onde será prestado o suporte?
DataGrid RecordList → Z_00143_NN_LOCAL_SUPORTE.NN_LOCAL_SUPORTE
Colunas do registro:
- ESTADO "Estado" [TextBox String]
- MUNICIPIO "Município" [TextBox String]

### ORIGEM_SERVICO — Qual a origem da aquisição/local de faturamento do SERVIÇO do fornecedor?
DataGrid RecordList → Z_00143_ORIGEM_SERVICO.ORIGEM_SERVICO
Colunas do registro:
- ITEM "Item" [DropDownList String] itens: Licenciamento Perpétuo;Serviço;Subscrição;Suporte;Treinamento
- ESTADO "Estado" [TextBox String]
- MUNICIPIO "Município" [TextBox String]

### ORIGEM_PRODUTO — Qual a origem da aquisição/local de faturamento do PRODUTO do fornecedor?
DataGrid RecordList → Z_00143_ORIGEM_PRODUTO.ORIGEM_PRODUTO
Colunas do registro:
- ITEM "Item" [DropDownList String] itens: Hardware;Bens e Produto
- ESTADO "Estado" [TextBox String]
- MUNICIPIO "Município" [TextBox String]

### DESTINACAO_BBTS — Qual a destinação da aquisição (Filial da BBTS)?
DataGrid RecordList → Z_00143_DESTINACAO_BBTS.DESTINACAO_BBTS
Colunas do registro:
- ESTADO "estado" [TextBox String]
- MUNICIPIO "Município" [TextBox String]

### NN_SIM_NAO — O orçamento enviado pelo fornecedor contempla todos os tributos?
DropDownList String → CPE_NEGOCIOS.NN_SIM_NAO
Itens: Sim;Não;Ambos

### SIM_NAO7 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO7
Itens: Sim;Não

### NN_CANCELA — Cancela chamado?
DropDownList String → CPE_NEGOCIOS.NN_CANCELA
Itens: Sim;Não

### NN_MOTIVO_CANCELAMENTO — Motivo do cancelamento(após a seleção de um motivo, o chamado será cancelado automaticamente)
DropDownList String → CPE_NEGOCIOS.NN_MOTIVO_CANCELAMENTO
Descrição: Motivo do cancelamento
Itens: Demanda absorvida por outro projeto;
Inviabilidade técnica/operacional;
Negociação suspensa pela BBTS;
Negociação suspensa pelo Cliente;
Duplicidade/Teste;
Proposta comercial não aceita - Preço;
Decisão estratégica da BBTS;
A pedido do cliente;Preço de referência expirado

### NN_FORMA_PAGAMENTO — Forma de pagamento
DropDownList String → CPE_NEGOCIOS.NN_FORMA_PAGAMENTO
Itens: Dólar;Real;Euro;Outros

### NN_PAIS — País
TextBox String → CPE_NEGOCIOS.NN_PAIS

### NN_LOCAL — Local
TextBox String → CPE_NEGOCIOS.NN_LOCAL

### SIM_NAO4 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO4
Itens: Sim;Não

### NN_BENEFICIO_FISCAL — Qual benefício fiscal?
TextBox String → CPE_NEGOCIOS.NN_BENEFICIO_FISCAL

### NN_NUMERO_NDA — Número NDA
TextBox String → CPE_NEGOCIOS.NN_NUMERO_NDA

### NN_FORMACONTRATACAO — Forma de Contratação
DropDownList String → CPE_HOMOLOGACAO.NN_FORMACONTRATACAO
Itens: Novo Contrato;Aditivo;Renovação;Recontratação

### NN_POC — Teve POC
DropDownList String → CPE_NEGOCIOS.NN_POC
Itens: POC;Piloto;Degustação;Não

### MOTIVO — Motivo da solicitação de serviço
Memo String(1500) → CP_ORDEM_SERVICO.MOTIVO

### CANALDEVENDA — Canal de Venda
DataGrid RecordList → Z_00143_CANALDEVENDA.CANALDEVENDA
Colunas do registro:
- NOMECTTCLIENT "Nome do contato do cliente" [TextBox String]
- TELLCLIENT "Telefone do cliente" [TextBox String]
- EMAILCLIENT "E-mail do cliente" [TextBox String]
- CARGOCLIENT "Cargo do cliente" [TextBox String]
- SETCLIENT "Setor do cliente" [TextBox String]

### CANALDEVENDA1 — Combo Box
DropDownList String(900) → CPE_NEGOCIOS.CANALDEVENDA1
Itens: Prospecção;Indicação;Parceria;Pós-venda;RFP/RFI/RFQ;Licitação;Canais Digitais;Network.

### NN_DATAPICKER1 — Data picker NN
DatePicker DateTime → CPE_NEGOCIOS.NN_DATAPICKER1

### NN_DATA_REPROG — Data de Reprogramaçãoo
DataGrid RecordList → Z_00143_NN_DATA_REPROG.NN_DATA_REPROG
Descrição: Data de Reprogramação
Colunas do registro:
- SITUACAO "Situação" [DropDownList String] itens: Reprogramação;Resposta ao cliente
- DATA "Data" [DateTimePicker DateTime]

### GRID_PESSOAS — Grid Pessoas
DataGrid RecordList → Z_00143_GRID_PESSOAS.GRID_PESSOAS
Colunas do registro:
- PESSOAS "Pessoas" [DropDownList String]
**PESSOAS.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```

### PREMISSA_DOD — Premissas
Memo String(2000) → CP_ORDEM_SERVICO.PREMISSA_DOD
Descrição: O requisitante deve descrever fatores que, para fim de planejamento, são considerados reais, que afetam todos os aspectos do planejamento do projeto.


### NN_PORTFOLIO — Portfólio de soluções do provedor
Memo String(2000) → CPE_NEGOCIOS.NN_PORTFOLIO

### NN_SEGMENTO — Segmento de Mercado
DropDownList String → CPE_NEGOCIOS.NN_SEGMENTO
Itens: Banco do Brasil;ELBB;Mercado;Governo

### COMBOBOX1 — Chamado Aberto?
DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1

### CNPJ — CNPJ
TextBox String → CP_ORDEM_SERVICO.CNPJ

### NN_GERENCIA_NEGOCIO — Gerência Executiva do Negócio
DropDownList String → CP_ORDEM_SERVICO.NN_GERENCIA_NEGOCIO
**LookupScript**
```python
Itens = DB.ExecuteDataTable(" SELECT DISTINCT TO_CHAR(id_orgao) AS id_orgao, DESCRICAO FROM ORGAO WHERE ATIVO LIKE 'Sim' ORDER BY DESCRICAO ")

#Itens = DB.ExecuteDataTable(" SELECT DISTINCT TO_CHAR(id_orgao) AS id_orgao, DESCRICAO FROM ORGAO WHERE ATIVO LIKE 'Sim' AND (DESCRICAO LIKE '%DIRE%' OR DESCRICAO LIKE '%GERE%' OR DESCRICAO LIKE '%GERÊ%' OR DESCRICAO LIKE '%PROGRA%') AND (DESCRICAO NOT LIKE '%DIV%' OR DESCRICAO NOT LIKE '%COMITE%' OR DESCRICAO NOT LIKE '%REGIO%') and id_orgao not in (1215, 1197) ORDER BY DESCRICAO ")
```

### NN_LINHA_NEGOCIO — Linha de Negócio
DropDownList String → CPE_NEGOCIOS.NN_LINHA_NEGOCIO
Itens: Infraestrutura e Disponibilidade;
Gestão de Segurança;
Comunicação e Conectividade;
Canais e Backoffice;Soluções Digitais;
Correspondente Bancário;Soluções de Parcerias Estratégicas;
Outros

### NN_PRODUTO — Produto
DropDownList String → CPE_NEGOCIOS.NN_PRODUTO
Itens: Disponibilidade Operacional de TAA;
Disponibilidade Operacional de Bens de Automação Bancária;
Monitoração de Ambientes;
Infraestrutura de Data Center;
Assistência Técnica;
DOSA;
DOCA;
DOSI;
PSIM;
SOC;
CDT;
Mensageria SMS;
Mensageria E-mail Marketing;
Outsourcing de Telefonia - PVV;
Central de Relacionamento e Telecobrança;
Cobrança Extrajudicial;
Preparação para Ajuizamento de Operações;
Microfilmagem;
Fábrica de Software;
Aprovve Service;
HIVEPlace;
Revenda Especializada;
Hosting de Data Center;
Gestão de rede de correspondentes substabelecidos;
Outros

### NN_PRODUTO_EXISTENTE — Produtu existente?
DropDownList String → CPE_NEGOCIOS.NN_PRODUTO_EXISTENTE
Descrição: Produto existente?
Itens: Sim;
Não

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### NN_OBJETO_PROPOSTA — Objetivo da Proposta
Memo String(2000) → CP_ORDEM_SERVICO.NN_OBJETO_PROPOSTA

### APROVADOR_PB — Vistoriador dos Bens (no mínimo 3, sendo um o gestor de patrimônio)
DataGrid RecordList → Z_00143_APROVADOR_PB.APROVADOR_PB
Colunas do registro:
- APROVADORES "Aprovadores" [DropDownList String]
**APROVADORES.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```

### NN_STATUS_PROJETO — Status projeto
DropDownList String → CPE_NEGOCIOS.NN_STATUS_PROJETO
Itens: Normal;Alerta;Crítico

### NN_PRAZO_ESTIMADO — Prazo estimado do contrato
DropDownList String → CPE_NEGOCIOS.NN_PRAZO_ESTIMADO
Itens: 06 meses;12 meses;24 meses;36 meses;48 meses;60 meses

### NN_DATA_ENVIO_PROPOSTA — Data de envio da proposta
DataGrid RecordList → Z_00143_NN_DATA_ENVIO_PROPOSTA.NN_DATA_ENVIO_PROPOSTA
Colunas do registro:
- VALOR_GLOBAL "Valor Global" [TextBox Decimal]
- NN_PROPOSTA_COMERCIAL "Proposta Comercial" [DropDownList String] itens: Em negociação;Proposta aceita; Sem Proposta
- DATA_ENVIO_PROPOSTA "Data de envio da proposta" [DatePicker DateTime]

### OBS1 — Observação1
Memo String(2000) → CPE_CONTRATOS.OBS1
Descrição: Informe

### OBS3 — Observação3
Memo String(2000) → CPE_CONTRATOS.OBS3
Descrição: Informe

### SELECAPROV — Seleção dos aprovadores
DataGrid RecordList → Z_00143_SELECAPROV.SELECAPROV
Descrição: Seleção dos aprovadores e indicação da obrigatoriedade de voto (obrigatória ou opcional)
Colunas do registro:
- APROVADORES "Nome" [DropDownList String]
**APROVADORES.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```

### OBS20 — Observação20
Memo String(40000) → CPE_CSC.OBS20

### OBSERVACAO — .
TextBox String(2000) → CPE_CSC.OBSERVACAO
Descrição: Observação

### SIM_NAO10 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO10
Itens: Sim;Não

### TIPO — Tipo
TextBox String → CP_ORDEM_SERVICO.TIPO

### NOME_CONTRATO — Nome contrato
TextBox String → CPE_CSC.NOME_CONTRATO
Descrição: Nome do contrato

### CSC_VALOR2 — Valor
TextBox Decimal → CPE_CSC.CSC_VALOR2

### SIM_NAO2 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO2
Itens: Sim;Não

### CSC_OBS2_A — Observação
TextBox String(2000) → CPE_CSC.CSC_OBS2_A

### REFERENCIA_GUIA — Referência
TextBox String → CP_ORDEM_SERVICO.REFERENCIA_GUIA

### APROV_FAVORECIDO — Nome do aprovador favorecido
TextBox String → CPE_CSC.APROV_FAVORECIDO

### APROV_GESTOR_FAVORECIDO — Aprovação gestor favorecido
TextBox String → CPE_CSC.APROV_GESTOR_FAVORECIDO
Descrição: Aprovação gestor favorecido.

### COMBOBOX4 — COMBOBOX4
DropDownList String → CPE_BOOTCAMP.COMBOBOX4
Itens: Borderô - Relatório de Solicitação de Transferência Bancária

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Não') order by nomemat")
```

### NN_DATA_ENVIO_PRECO — Data de envio do preço de referência
DataGrid RecordList → Z_00143_NN_DATA_ENVIO_PRECO.NN_DATA_ENVIO_PRECO
Colunas do registro:
- DATA_ENVIO_PROPOSTA "Data de envio da proposta" [DatePicker DateTime]
- NN_PROPOSTA_COMERCIAL "Proposta Comercial" [DropDownList String] itens: Em negociação;Proposta aceita; Sem Proposta
- VALOR_GLOBAL "Valor Global" [TextBox Decimal]

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
