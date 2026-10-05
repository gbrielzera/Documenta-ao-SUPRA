# Fluxo: Comunicação de Acidente de Trabalho - CAT (CAT) — versão 1
Caminho: Fluxos > Comunicação de Acidente de Trabalho - CAT Versão 1 Comunicação de Acidente de Trabalho - CAT
XML: `XMLs para teste/Comunicação_de_Acidente_de_Trabalho_-_CAT_Versão_1_Comunicação_de_Acidente_de_Trabalho_-_CAT.xml` | Supravizio 19.1.1 | SubProcessoId 20267 | DesenhoProcessoId 2866 | ProcessoId 758
Órgão dono: 3000003200 - GERENCIA DE PESSOAS | Responsável: JEAN DE SOUSA ESTEVES FOGGIA
Classe do subprocesso: DescricaoCliente=Comunicação de Acidente de Trabalho - CAT; CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: CAT - Inicial (CATINICIAL); CAT - Reabertura (CATREABERTURA); CAT - Comunicado de Óbito (CATCOMUNICADODEOBITO)

## Grafo do fluxo
- [324340] EventoInicial "" {Favorecido} → [324341] Aviso sobre abertura de Ordem de Serviço
- [324341] EventoIntermediarioMensagem "Aviso sobre abertura de Ordem de Serviço" → [324342] Analisar a solicitação

- [324342] Tarefa "Analisar a solicitação
" {Analista CAT} → [G73987] Processo aprovado?
- [324343] Tarefa "Informar dados da solicitação
" {Favorecido} → [324342] Analisar a solicitação

- [324344] Tarefa "Informar o erro
" {Responsável atual} → [324345] Aviso de Ajuste de Informações
- [324345] EventoIntermediarioMensagem "Aviso de Ajuste de Informações" → [324343] Informar dados da solicitação

- [324335] EventoIntermediarioMensagem "Aviso de Conclusão sem necessidade de CAT" → [324336] 
- [324336] EventoFinal "" → (fim)
- [324334] Tarefa "Informar motivo da reprovação" {Responsável atual} → [324335] Aviso de Conclusão sem necessidade de CAT
- [324339] EventoFinal "" → (fim)
- [324337] Tarefa "Informar Número do Recibo E-Social + Anexo do Pdf" {Responsável atual} → [324338] Aviso de Conclusão + informações e pdf
- [324338] EventoIntermediarioMensagem "Aviso de Conclusão + informações e pdf" → [324339] 
- [G73988] Gateway "Necessidade de abertura de CAT?" → «Sim» [324337] Informar Número do Recibo E-Social + Anexo do Pdf | «Não» [324334] Informar motivo da reprovação
- [G73987] Gateway "Processo aprovado?" → «Aprovado» [G73988] Necessidade de abertura de CAT? | «Reprovado» [324344] Informar o erro


## Gateways
### [G73988] Necessidade de abertura de CAT? (EventBasedExclusiveDecision)
- alternativa → [324337] Informar Número do Recibo E-Social + Anexo do Pdf: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0; RotuloMotivo=Sim; MotivoObrigatorio=true
- alternativa → [324334] Informar motivo da reprovação: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1; RotuloMotivo=Não
### [G73987] Processo aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVADO")
```
- alternativa → [G73988] Necessidade de abertura de CAT?: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
- alternativa → [324344] Informar o erro
: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [324340] EventoInicial ""
Responsável: Favorecido (papel 76)
Config: Configuracao={"ServicoIniciador":"CAT"}
TipoSolicitacao: Comunicação de Acidente de Trabalho - CAT
**ScriptFormCarregado**
```python
#Formulario["REG_POL"].Visivel = False
#Formulario["REG_POL"].Habilitado = False

for controle in Formulario.Controles:
    Formulario[controle.Key].Visivel = False
    Formulario[controle.Key].Habilitado = False
    Formulario[controle.Key].Valor = None

if OrdemServico.Servico.Sigla == "CATINICIAL" or OrdemServico.Servico.Sigla == "CATREABERTURA" or OrdemServico.Servico.Sigla == "CATCOMUNICADODEOBITO":
    Formulario["FAVORECIDO_TODOS"].Visivel = True
    Formulario["FAVORECIDO_TODOS"].Habilitado = True
```
- Operação PR0004 Associar Itens Configuração: Nome=REG_POL
  - anexo "Registro Policial" classes: Anexo — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações do acidente
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA] obrigatório — Coluna=2
  - TIPO_CAT "Tipo de CAT" [DropDownList String → CPE_PESSOAS.TIPO_CAT] obrigatório — Coluna=3
  - REG_POLICIAL "Registro Policial/Boletim de Ocorrência" [DropDownList String → CPE_PESSOAS.REG_POLICIAL] obrigatório
**REG_POLICIAL.ScriptModificado**
```python
if Formulario["REG_POLICIAL"].Valor == "Sim":
    Formulario["REG_POL"].Visivel = True
    Formulario["REG_POL"].Habilitado = True
elif Formulario["REG_POLICIAL"].Valor == "Não":
    Formulario["REG_POL"].Visivel = False
    Formulario["REG_POL"].Habilitado = False
```
  - FAVORECIDO_TODOS "Nome do Funcionário Acidentado" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
**FAVORECIDO_TODOS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
pessoa = Pessoa.Carrega("Id", Convert.ToInt32(Formulario["FAVORECIDO_TODOS"].Valor))
orgao = Orgao.Carrega(pessoa.OrgaoId)

OrdemServico.Favorecido = pessoa

for controle in Formulario.Controles:
    if controle.Key != "FAVORECIDO_TODOS":
       Formulario[controle.Key].Visivel = False
       Formulario[controle.Key].Valor = None
       
    Formulario["MATRICULA"].Valor = pessoa["MATRICULA"]
    Formulario["MATRICULA"].Visivel = True
    Formulario["MATRICULA"].Habilitado = False

       
    if OrdemServico.Servico.Sigla == "CATINICIAL":
        Formulario["TIPO_AT"].Visivel = True
        Formulario["TIPO_AT"].Habilitado = True
        Formulario["TIPO_CAT"].Visivel = True
        Formulario["TIPO_CAT"].Valor = "INICIAL"
        Formulario["TIPO_CAT"].Habilitado = False
        Formulario["REG_POLICIAL"].Visivel = True
        Formulario["REG_POLICIAL"].Habilitado = True
        Formulario["ACIDENTE_CAT"].Visivel = True
        Formulario["ACIDENTE_CAT"].Habilitado = True
        Formulario["DESCRICAO_DETALHADA"].Visivel = True
        Formulario["DESCRICAO_DETALHADA"].Habilitado = True
        Formulario["LOCAL_ACIDENTE"].Visivel = True
        Formulario["LOCAL_ACIDENTE"].Habilitado = True
        Formulario["MAIS_INFO"].Visivel = True
        Formulario["MAIS_INFO"].Habilitado = True
        Formulario["MAIS_INFO2"].Visivel = True
        Formulario["MAIS_INFO2"].Habilitado = True
        Formulario["MAIS_INFO3"].Visivel = True
        Formulario["MAIS_INFO3"].Habilitado = True
        

    if OrdemServico.Servico.Sigla == "CATREABERTURA":
        Formulario["TIPO_AT"].Visivel = True
        Formulario["TIPO_AT"].Habilitado = True
        Formulario["TIPO_CAT"].Visivel = True
        Formulario["TIPO_CAT"].Habilitado = False
        Formulario["TIPO_CAT"].Valor = "REABERTURA"
        Formulario["ACIDENTE_CAT"].Visivel = True
        Formulario["ACIDENTE_CAT"].Habilitado = True
        Formulario["DESCRICAO_DETALHADA"].Visivel = True
        Formulario["DESCRICAO_DETALHADA"].Habilitado = True
        Formulario["LOCAL_ACIDENTE"].Visivel = True
        Formulario["LOCAL_ACIDENTE"].Habilitado = True
        Formulario["MAIS_INFO"].Visivel = True
        Formulario["MAIS_INFO"].Habilitado = True
        Formulario["MAIS_INFO2"].Visivel = True
        Formulario["MAIS_INFO2"].Habilitado = True
        Formulario["MAIS_INFO3"].Visivel = True
        Formulario["MAIS_INFO3"].Habilitado = True
        Formulario["REG_POLICIAL"].Visivel = True
        Formulario["REG_POLICIAL"].Habilitado = True
        

    elif OrdemServico.Servico.Sigla == "CATCOMUNICADODEOBITO":
        Formulario["TIPO_AT"].Visivel = True
        Formulario["TIPO_AT"].Habilitado = True
        Formulario["TIPO_CAT"].Visivel = True
        Formulario["TIPO_CAT"].Habilitado = False
        Formulario["TIPO_CAT"].Valor = "COMUNICADO DE ÓBITO"
        Formulario["ACIDENTE_CAT"].Visivel = True
        Formulario["ACIDENTE_CAT"].Habilitado = True
        Formulario["DESCRICAO_DETALHADA"].Visivel = True
        Formulario["DESCRICAO_DETALHADA"].Habilitado = True
        Formulario["LOCAL_ACIDENTE"].Visivel = True
        Formulario["LOCAL_ACIDENTE"].Habilitado = True
        Formulario["MAIS_INFO"].Visivel = True
        Formulario["MAIS_INFO"].Habilitado = True
        Formulario["MAIS_INFO2"].Visivel = True
        Formulario["MAIS_INFO2"].Habilitado = True
        Formulario["MAIS_INFO3"].Visivel = True
        Formulario["MAIS_INFO3"].Habilitado = True
        Formulario["REG_POLICIAL"].Visivel = True
        Formulario["REG_POLICIAL"].Habilitado = True

Formulario["ATESTADO_MEDICO"].Visivel = True
Formulario["ATESTADO_MEDICO"].Habilitado = True
Formulario["DESCRICAO_DETALHADA"].Visivel = False
```
  - TIPO_AT "Tipo de Acidente de Trabalho" [DropDownList String → CPE_PESSOAS.TIPO_AT] obrigatório — Coluna=2
  - DATA_ENTREGA "Data e horário que o empregado informou o acidente ao gestor." [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ENTREGA] obrigatório
    - coluna QUANTIDADE_PARTICIPANTES obrigatório
    - coluna DATA_HORA_INICIO obrigatório
    - coluna DATA_HORA_FIM obrigatório
  - DESCRICAO_DETALHADA "Descrição detalhada" [Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório
  - CPF "CPF do Empregado." [TextBox String(15) → CP_ORDEM_SERVICO.CPF] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"000\\.000\\.000\\-00"}
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Detalhes do Acidente
  - ACIDENTE_CAT "Acidente CAT" [DataGrid RecordList → Z_00143_ACIDENTE_CAT.ACIDENTE_CAT] obrigatório — FormaEdicaoWeb=JanelaPopup; LarguraJanelaPopup=500
    - coluna ULTIMO_DIA_TRABALHADO obrigatório
    - coluna HORA_ACIDENTE obrigatório
    - coluna DET_ACIDENTE
    - coluna OBITO obrigatório
    - coluna DATA_ACIDENTE obrigatório
    - coluna HORAS_TRABALHADAS obrigatório
    - coluna DATAHORA obrigatório
    - coluna CPF obrigatório
    - coluna DESCRICAO obrigatório
  - LOCAL_ACIDENTE "Local do Acidente" [DataGrid RecordList → Z_00143_LOCAL_ACIDENTE.LOCAL_ACIDENTE] obrigatório — FormaEdicaoWeb=JanelaPopup; LarguraJanelaPopup=500
**LOCAL_ACIDENTE.ScriptModificado**
```python
if FormularioRegistro["TIPO_LOCAL_ACIDENTE"].Valor == "Outros":
    FormularioRegistro["DESCACD"].Visivel = True
else:
    FormularioRegistro["DESCACD"].Visivel = False
```
    - coluna ENDERECO_ACIDENTE obrigatório
    - coluna CEP_ACIDENTE obrigatório
    - coluna COMPLEMENTO obrigatório
    - coluna TIPO_LOCAL_ACIDENTE obrigatório
    - coluna CIDADE obrigatório
    - coluna UF_ACIDENTE obrigatório
    - coluna DESCACD
    - coluna CNPJ_CLIENTE obrigatório
    - coluna CNPJ_EMPREGADOR obrigatório
  - MAIS_INFO3 "Informações médicas" [DataGrid RecordList → Z_00143_MAIS_INFO3.MAIS_INFO3] obrigatório — FormaEdicaoWeb=JanelaPopup; QtdColunasFormulario=3; LarguraJanelaPopup=500
    - coluna CNPJ_SETOR_EMPREGADO obrigatório
    - coluna CNPJ_CLIENTE
    - coluna HR_DT_ATEND_MEDICO obrigatório
    - coluna LOCAL_ATEND_MEDICO obrigatório
    - coluna HORA_ATENDIMENTO_MEDICO obrigatório
    - coluna AFASTAMENTO obrigatório
  - MAIS_INFO "Informações médicas " [DataGrid RecordList → Z_00143_MAIS_INFO.MAIS_INFO] obrigatório — FormaEdicaoWeb=JanelaPopup; LarguraJanelaPopup=500
    - coluna DATA_ATENDIMENTO obrigatório
    - coluna PARTE_CORPO_ATINGIDA obrigatório
    - coluna LOCAL_ATENDIMENTO obrigatório
    - coluna INTERNACAO obrigatório
    - coluna DURACAO_TRATAMENTO obrigatório
    - coluna CNPJ_SETOR_EMPREGADO obrigatório
    - coluna CNPJ_CLIENTE obrigatório
    - coluna LATERALIDADE obrigatório
    - coluna DESCRICAO_LESAO obrigatório
  - MAIS_INFO2 "Informações médicas" [DataGrid RecordList → Z_00143_MAIS_INFO2.MAIS_INFO2] obrigatório — FormaEdicaoWeb=JanelaPopup; LarguraJanelaPopup=500
    - coluna CRM obrigatório
    - coluna UF_CRM obrigatório
    - coluna NOME_MEDICO obrigatório
    - coluna APOSENTADO obrigatório
    - coluna DETALHE_ACIDENTE obrigatório
    - coluna CID obrigatório
  - DESCRICAO_DETALHADA "Fato gerador do acidente" [Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=ATESTADO_MEDICO
  - anexo "Atestado Médico" classes: Anexo — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [324341] EventoIntermediarioMensagem "Aviso sobre abertura de Ordem de Serviço"
Destinatário: Analista CAT (papel 1159)
Config: ListaDestinatarios=jean.foggia@bbts.com.br;saudeocupacional@bbtecno.com.br; saude@bbts.com.br; EnviaMensagemIndividual=true
ModeloComunicado: Aviso sobre Abertura de Chamado
Corpo do comunicado: Prezados(as),
Foi aberta a Ordem de Serviço nº OrdemServico.Numero referente ao assunto: OrdemServico.SubProcesso .
Descrição Detalhada:
OrdemServico.DescricaoDetalhada 
 OrdemServico.Customizado.DESCRICAO_OBRIG 
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [324342] Tarefa "Analisar a solicitação
"
Responsável: Analista CAT (papel 1159)
Config: Codigo=APROVADO
- Operação PR0002 Aprovar: MinimoAprovadores=1; ReprovarImediato=true
  - (aprovação) MAIS_INFO2 "Mais Informações" [DataGrid RecordList → Z_00143_MAIS_INFO2.MAIS_INFO2]
  - (aprovação) MAIS_INFO3 "Mais Informações" [DataGrid RecordList → Z_00143_MAIS_INFO3.MAIS_INFO3]
  - (aprovação) DESCRICAO_DETALHADA "Relato detalhado do acidente" [Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA]
  - (aprovação) LOCAL_ACIDENTE "Local do Acidente" [DataGrid RecordList → Z_00143_LOCAL_ACIDENTE.LOCAL_ACIDENTE]
  - (aprovação) TIPO_AT "Tipo de Acidente de Trabalho" [DropDownList String → CPE_PESSOAS.TIPO_AT]
  - (aprovação) ACIDENTE_CAT "Acidente CAT" [DataGrid RecordList → Z_00143_ACIDENTE_CAT.ACIDENTE_CAT]
  - (aprovação) AFASTAMENTO "Houve Afastamento?" [DropDownList String → CPE_PESSOAS.AFASTAMENTO]
  - (aprovação) TIPO_CAT "Tipo de CAT" [DropDownList String → CPE_PESSOAS.TIPO_CAT]
  - (aprovação) REG_POLICIAL "Registro Policial/Boletim de Ocorrência" [DropDownList String → CPE_PESSOAS.REG_POLICIAL]
  - (aprovação) MAIS_INFO "Mais Informações" [DataGrid RecordList → Z_00143_MAIS_INFO.MAIS_INFO]
  - aprovador: Analista CAT (Unico)

### [324343] Tarefa "Informar dados da solicitação
"
Responsável: Favorecido (papel 76)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
**ScriptFormCarregado**
```python
OrdemServico.ModificaCampoFormularioVisivel('REG_POL1', False)
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações do acidente
  - DATA_ENTREGA "Data e horário que o empregado informou o acidente ao gestor." [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ENTREGA] obrigatório
  - TIPO_AT "Tipo de Acidente de Trabalho" [DropDownList String → CPE_PESSOAS.TIPO_AT] obrigatório
  - REG_POLICIAL "Registro Policial/Boletim de Ocorrência" [DropDownList String → CPE_PESSOAS.REG_POLICIAL] obrigatório
**REG_POLICIAL.ScriptModificado**
```python
if Formulario["REG_POLICIAL1"].Valor == "Sim":
    Formulario["REG_POL1"].Visivel = True
else:
    Formulario["REG_POL1"].Visivel = False
```
  - AFASTAMENTO "Houve Afastamento?" [DropDownList String → CPE_PESSOAS.AFASTAMENTO] obrigatório
**AFASTAMENTO.ScriptModificado**
```python
if Formulario["AFASTAMENTO"].Valor == "Sim":
    Formulario["ATESTADO_MEDICO"].Visivel = True
else:
    Formulario["ATESTADO_MEDICO"].Visivel = False
```
  - ACIDENTE_CAT "Acidente CAT" [DataGrid RecordList → Z_00143_ACIDENTE_CAT.ACIDENTE_CAT] obrigatório — FormaEdicaoWeb=PropriaLinha; LarguraJanelaPopup=100
    - coluna DET_ACIDENTE obrigatório
    - coluna ULTIMO_DIA_TRABALHADO obrigatório
    - coluna DATA_ACIDENTE obrigatório
    - coluna HORAS_TRABALHADAS obrigatório
    - coluna OBITO obrigatório
    - coluna HORA_ACIDENTE obrigatório
    - coluna DESCRICAO obrigatório
    - coluna CPF obrigatório
    - coluna DATAHORA obrigatório
  - MAIS_INFO "Mais Informações" [DataGrid RecordList → Z_00143_MAIS_INFO.MAIS_INFO] obrigatório
    - coluna DESCRICAO_LESAO obrigatório
    - coluna DURACAO_TRATAMENTO obrigatório
    - coluna LOCAL_ATENDIMENTO obrigatório
    - coluna LATERALIDADE obrigatório
    - coluna DATA_ATENDIMENTO obrigatório
    - coluna PARTE_CORPO_ATINGIDA obrigatório
    - coluna INTERNACAO obrigatório
    - coluna CID obrigatório
    - coluna CNPJ_SETOR_EMPREGADO obrigatório
    - coluna CNPJ_CLIENTE obrigatório
    - coluna CRM obrigatório
    - coluna UF_CRM obrigatório
    - coluna NOME_MEDICO obrigatório
    - coluna APOSENTADO obrigatório
  - MAIS_INFO2 "Mais Informações" [DataGrid RecordList → Z_00143_MAIS_INFO2.MAIS_INFO2] obrigatório
    - coluna CID obrigatório
    - coluna CRM obrigatório
    - coluna UF_CRM obrigatório
    - coluna NOME_MEDICO obrigatório
    - coluna APOSENTADO obrigatório
    - coluna DETALHE_ACIDENTE obrigatório
  - LOCAL_ACIDENTE "Local do Acidente" [DataGrid RecordList → Z_00143_LOCAL_ACIDENTE.LOCAL_ACIDENTE] obrigatório — LarguraJanelaPopup=800
    - coluna TIPO_LOCAL_ACIDENTE obrigatório
    - coluna CIDADE obrigatório
    - coluna UF_ACIDENTE obrigatório
    - coluna ENDERECO_ACIDENTE obrigatório
    - coluna CEP_ACIDENTE obrigatório
    - coluna COMPLEMENTO obrigatório
    - coluna CNPJ_CLIENTE obrigatório
    - coluna CNPJ_EMPREGADOR obrigatório
  - CPF "CPF do Empregado." [TextBox String(15) → CP_ORDEM_SERVICO.CPF] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"000\\.000\\.000\\-00"}
    - coluna MATRICULA obrigatório
    - coluna PIX obrigatório
    - coluna MES obrigatório
    - coluna ANO obrigatório
    - coluna TOMADOR obrigatório
    - coluna CPF obrigatório
    - coluna FUNCIONARIO obrigatório
    - coluna VALOR obrigatório
    - coluna BANCO obrigatório
    - coluna AGENCIA obrigatório
    - coluna CONTA obrigatório
    - coluna OPERACAO obrigatório
    - coluna VARIACAO obrigatório
    - coluna TIPO_DA_CONTA obrigatório
    - coluna JUSTIFICATIVA obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=ATESTADO_MEDICO1
  - anexo "Atestado Médico" classes: Anexo — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração: Nome=REG_POL1
  - anexo "Registro Policial" classes: Anexo — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [324344] Tarefa "Informar o erro
"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - DESCRICAO_DETALHADA "Informe o problema:" [Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Print do erro (Opcional)" classes: Anexo — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [324345] EventoIntermediarioMensagem "Aviso de Ajuste de Informações"
Destinatário: Favorecido (papel 76)
Config: ListaDestinatarios=saudeocupacional@bbtecno.com.br; saude@bbts.com.br
ModeloComunicado: Ajuste de Informações - CAT
Corpo do comunicado: Prezado(a),
Informamos que o chamado foi devolvido para ajustes conforme descrito: OrdemServico.Customizado.DESCRICAO_DETALHADA 
Por favor, corrigir as informações o mais breve possível para dar seguimento à finalização do serviço.
Para maiores informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [324335] EventoIntermediarioMensagem "Aviso de Conclusão sem necessidade de CAT"
Destinatário: Favorecido (papel 76)
ModeloComunicado: Aviso de reprovação de chamados - CAT
Corpo do comunicado: Prezado(a) OrdemServico.Cliente.Nome ,
A Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto foi finalizada sem a necessidade de abertura de CAT pelo seguinte motivo: OrdemServico.Customizado.DESCRICAO1 .
Para obter mais detalhes sobre a solicitação e a reprovação, CLIQUE no link =>> Link.Consulta 
Atenciosamente,
Central de Serviços

### [324336] EventoFinal ""

### [324334] Tarefa "Informar motivo da reprovação"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - DESCRICAO1 "Descreva o motivo para reprovação" [Memo String → CP_ORDEM_SERVICO.DESCRICAO1] obrigatório

### [324339] EventoFinal ""

### [324337] Tarefa "Informar Número do Recibo E-Social + Anexo do Pdf"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração: Nome=ANEXO_PDF
  - anexo "Anexo do pdf" classes: Anexo — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos
  - NUM_ITEM "Número do Recibo E-Social" [TextBox String(30) → CP_ORDEM_SERVICO.NUM_ITEM] obrigatório

### [324338] EventoIntermediarioMensagem "Aviso de Conclusão + informações e pdf"
Destinatário: Favorecido (papel 76)
Config: AnexarTodosDocumentos=true
ModeloComunicado: Finalização de Processo - CAT
Corpo do comunicado: Prezado(a),
 A Ordem de Serviço OrdemServico.Numero foi finalizada com sucesso. 
Informamos que a NF do E-social está disponível para Download na aba "Anexos" dessa Ordem de Serivço.
eSocial: OrdemServico.Customizado.NUM_ITEM 
Atenciosamente,
Central de Serviços
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=2223; ClasseConfiguracao=Anexo

## Papéis usados
### papel 76: Favorecido
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Favorecido
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Favorecido)
```
### papel 1159: Analista CAT
Tipo=RelacaoPessoas | pessoas: MARIA ANGELICA RODRIGUES MACHADO DA SILVA, CECILIA GOMES DE SOUSA, ROSECLAIR DOS SANTOS PINTO
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```

## Campos customizados usados (definição global)

### MATRICULA — Matrícula
TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA

### TIPO_CAT — Tipo de CAT
DropDownList String → CPE_PESSOAS.TIPO_CAT
Itens: INICIAL; REABERTURA;
COMUNICADO DE ÓBITO

### REG_POLICIAL — Registro Policial/Boletim de Ocorrência
DropDownList String → CPE_PESSOAS.REG_POLICIAL
Descrição: Registro Policial
Itens: Sim; Não

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### TIPO_AT — Tipo de Acidente de Trabalho
DropDownList String → CPE_PESSOAS.TIPO_AT
Itens: Tipico;
Doença;
Trajeto

### DATA_ENTREGA — Data de entrega
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ENTREGA
Descrição: Data prevista para entrega

### DESCRICAO_DETALHADA — Descrição detalhada
Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA

### CPF — CPF
TextBox String(15) → CP_ORDEM_SERVICO.CPF

### ACIDENTE_CAT — Acidente CAT
DataGrid RecordList → Z_00143_ACIDENTE_CAT.ACIDENTE_CAT
Colunas do registro:
- DESCRICAO "Fato gerador do acidente" [Memo String]
- CPF "CPF do empregado" [TextBox String]
- DATAHORA "Data e horário que o empregado informou o acidente ao gestor" [DateTimePicker DateTime]
- DATA_ACIDENTE "DATA DO ACIDENTE" [DatePicker DateTime]
- HORAS_TRABALHADAS "HORAS TRABALHADAS" [TextBox Decimal]
- OBITO "OBITO" [DropDownList String] itens: Sim; Não
- ULTIMO_DIA_TRABALHADO "ULTIMO DIA TRABALHADO" [DatePicker DateTime]
- DET_ACIDENTE "Descrição do acidente" [Memo String]
- HORA_ACIDENTE "Hora do Acidente" [TextBox DateTime]

### LOCAL_ACIDENTE — Local do Acidente
DataGrid RecordList → Z_00143_LOCAL_ACIDENTE.LOCAL_ACIDENTE
Colunas do registro:
- CNPJ_CLIENTE "CNPJ do Cliente" [TextBox String]
- CNPJ_EMPREGADOR "CNPJ do Empregador" [TextBox String]
- DESCACD "Descrever acidente" [Memo String]
- ENDERECO_ACIDENTE "Endereço do Acidente" [Memo String]
- CEP_ACIDENTE "CEP do Local" [TextBox String]
- COMPLEMENTO "Complemento" [Memo String]
- TIPO_LOCAL_ACIDENTE "Tipo do Local do Acidente" [DropDownList String] itens: Estabelecimento do empregador no Brasil;
Estabelecimento do empregador no Exterior;
Estabelecimento de tereceiros onde o empregador presta serviços;
Via pública;
Área rural;
Embarcação;Outros
- CIDADE "Cidade do Acidente" [TextBox String]
- UF_ACIDENTE "UF do Acidente" [TextBox String]

### MAIS_INFO3 — Mais Informações
DataGrid RecordList → Z_00143_MAIS_INFO3.MAIS_INFO3
Colunas do registro:
- AFASTAMENTO "Afastamento" [DropDownList String] itens: Sim; Não
- HORA_ATENDIMENTO_MEDICO "Hora Do Atendimento Médico" [TextBox DateTime]
- HR_DT_ATEND_MEDICO "Data do atendimento médico" [DatePicker DateTime]
- LOCAL_ATEND_MEDICO "Local do atendimento Médico" [TextBox String]

### MAIS_INFO — Mais Informações
DataGrid RecordList → Z_00143_MAIS_INFO.MAIS_INFO
Colunas do registro:
- DURACAO_TRATAMENTO "Duração do Tratamento (Dias Úteis)" [TextBox Integer]
- DESCRICAO_LESAO "Descrição completa da lesão" [Memo String]
- LATERALIDADE "Lateralidade" [DropDownList String] itens: Esquerda; Direita; Ambas; Não se aplica
- PARTE_CORPO_ATINGIDA "Parte(s) atingida(s)" [Memo String]
- INTERNACAO "Internação?" [DropDownList String] itens: Sim; Não

### MAIS_INFO2 — Mais Informações
DataGrid RecordList → Z_00143_MAIS_INFO2.MAIS_INFO2
Colunas do registro:
- CID "CID do Atestado" [TextBox String]
- CRM "CRM do Médico" [TextBox String]
- UF_CRM "UF do CRM" [TextBox String]
- NOME_MEDICO "Nome do Médico" [Memo String]
- APOSENTADO "É aposentado?" [DropDownList String] itens: Sim; Não
- DETALHE_ACIDENTE "Detalhes do Acidente" [Memo String]

### AFASTAMENTO — Houve afastamento?
DropDownList String → CPE_PESSOAS.AFASTAMENTO
Itens: Sim; Não

### DESCRICAO1 — Caixa de texto
Memo String → CP_ORDEM_SERVICO.DESCRICAO1

### NUM_ITEM — Número do Ítem
TextBox String(30) → CP_ORDEM_SERVICO.NUM_ITEM

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
