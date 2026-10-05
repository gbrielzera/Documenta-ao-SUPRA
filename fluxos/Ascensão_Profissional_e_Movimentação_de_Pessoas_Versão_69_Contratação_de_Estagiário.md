# Fluxo: Contratação de Estagiário (CONTRAESTAG) — versão 69
Caminho: Fluxos > Ascensão Profissional e Movimentação de Pessoas Versão 69 Contratação de Estagiário
XML: `XMLs para teste/Ascensão_Profissional_e_Movimentação_de_Pessoas_Versão_69_Contratação_de_Estagiário.xml` | Supravizio 19.1.1 | SubProcessoId 20778 | DesenhoProcessoId 2917 | ProcessoId 58
Órgão dono: 3000003210 - DIVISAO DE BENEFICIOS E MOVIMENTACOES DE PESSOAL | Responsável: PALOMA SABINE AMADO ROSA
Classe do subprocesso: Objetivo=Movimentação de pessoas por Contratação de Estagiário.; DescricaoCliente=Contratação de Estagiário gp; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorResponsavel; AcessoTotalAdmin=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Movimentação de pessoas por Contratação de Estagiário.; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Contratação de Estagiário (CONTRAESTAG)

## Grafo do fluxo
- [331028] EventoInicial "Contratação de Estagiário" {Movimentação de Pessoal} → [331032] Solicitar Aprovação do Gestor
- [331029] EventoIntermediarioMensagem "Término de serviço" → [331034] Chamado Finalizado
- [331030] EventoFinal "" {Responsável atual} → (fim)
- [331031] Tarefa "Aguardar Documentação do Estagiário" {Fila CSC - Movimentação Pessoal} → [331040] Criar posição no sistema
- [331032] Tarefa "Solicitar Aprovação do Gestor" {Fila CSC - Movimentação Pessoal} → [G75271] Gestor aprova?
- [331033] Tarefa "Convocar Estagiário " {Fila CSC - Movimentação Pessoal} → [331041] Solicitar documentação
- [331034] EventoFinal "Chamado Finalizado" {Responsável atual} → (fim)
- [331035] Tarefa "Preencher informações do estágio" {Fila CSC - Movimentação Pessoal} → [G75273] LOCALIDADE DE ACESSO?
- [331036] EventoIntermediarioMensagem "Reprovação do chamado" → [331030] 
- [331037] EventoIntermediarioMensagem "Admissão do estagiário" → [331029] Término de serviço
- [331038] SubProcesso "Controle de Acesso - Brasília" {Responsável atual} → [331039] Confecção de material - Crachá
- [331039] SubProcesso "Confecção de material - Crachá" {Responsável atual} → [331042] Disponibilização de Notebook (Caso necessário)
- [331040] Tarefa "Criar posição no sistema" {Fila CSC - Movimentação Pessoal} → [331035] Preencher informações do estágio
- [331041] Tarefa "Solicitar documentação" {Fila CSC - Movimentação Pessoal} → [331031] Aguardar Documentação do Estagiário
- [331042] Tarefa "Disponibilização de Notebook (Caso necessário)" {Responsável atual} → [331037] Admissão do estagiário
- [331043] Tarefa "Verificar solicitação" {Fila CSC - Movimentação Pessoal} → [331033] Convocar Estagiário 
- [G75271] Gateway "Gestor aprova?" → «Não» [331036] Reprovação do chamado | «Sim» [331043] Verificar solicitação
- [G75273] Gateway "LOCALIDADE DE ACESSO?" → «Brasília» [331038] Controle de Acesso - Brasília | «Não Precisa» [331039] Confecção de material - Crachá

## Gateways
### [G75271] Gestor aprova? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROV_GESTOR")
```
- alternativa → [331036] Reprovação do chamado: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [331043] Verificar solicitação: SequenciaAvaliacao=2; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
### [G75273] LOCALIDADE DE ACESSO? (EventBasedExclusiveDecision)
- alternativa → [331038] Controle de Acesso - Brasília: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Brasília
- alternativa → [331039] Confecção de material - Crachá: SequenciaAvaliacao=2; OperadorDecision=Equal; ReferenciaDecision=Não Precisa

## Atividades

### [331028] EventoInicial "Contratação de Estagiário"
Responsável: Movimentação de Pessoal (papel 230)
TipoSolicitacao: 18.01. Gestão de Pessoas - Ascensão e Movimentação de Pessoas
**ScriptFim**
```python
#lista = Utils.ExecuteDataTable("SELECT DISTINCT PESSOA.NOME_ABREVIADO AS NOME_COMPLETO FROM ORGAO LEFT OUTER JOIN PESSOA ON ORGAO.ID_GESTOR = PESSOA.ID_PESSOA WHERE ROWNUM = 1 AND ORGAO.ID_ORGAO = '"+OrdemServico.GetCustom("SCR_MOVI").ToString()+"' AND ORGAO.ATIVO like 'Sim'")

#for linha in lista.Rows:
#	gestor = linha["NOME_COMPLETO"].ToString()
	
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
Formulario["CNPJ"].Visivel = False
#Formulario["ENDERECO_FORNECEDOR"].Visivel = False

#----- Habilitado
#Formulario["ENDERECO_FORNECEDOR"].Habilitado = False
Formulario["CNPJ"].Habilitado = False

#Formulario["SCR_TODOS_RH"].Habilitado = True
```
- Operação PR0004 Associar Itens Configuração: Nome=ANEXO DE DOCUMENTO
  - anexo "Currículo do Estagiario selecionado" classes: Currículo — ProduzidoTermino=true
- Operação PR0001 Preencher Campos
  - CSC_NOME_COMPLETO "Nome do Estagiário" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO] obrigatório
  - SCR_TODOS_RH "UOR de Contratação" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH] obrigatório
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
  - FAVORECIDO_TODOS "Gestor para aprovação da movimentação" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
  - ESCOLARIDADE "Escolaridade" [DropDownList String → CP_ORDEM_SERVICO.ESCOLARIDADE] obrigatório
  - CURSO "Curso solicitado" [TextBox String → CP_ORDEM_SERVICO.CURSO] obrigatório
  - PERIODO_CURSO "Período cursando" [DropDownList String → CP_ORDEM_SERVICO.PERIODO_CURSO] obrigatório
  - SEXO_CONTRA "Sexo" [DropDownList String → CP_ORDEM_SERVICO.SEXO_CONTRA] obrigatório
  - ATIVIDADES "Atividades a serem desenvolvidas (listar pelo menos 3 atividades)" [Memo String(2000) → CP_ORDEM_SERVICO.ATIVIDADES] obrigatório
  - FAVORECIDO_MONITOR "Supervisor do estagiário" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_MONITOR] obrigatório
**FAVORECIDO_MONITOR.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
monitor = Formulario["FAVORECIDO_MONITOR"].Valor
cargo = Pessoa.Carrega("Cargo", monitor)
OrdemServico.SetCustom("CARGO", cargo)
```
  - CSC_OBS "Descrição detalhada" [Memo String(2000) → CPE_CSC.CSC_OBS] obrigatório
  - LOCAL DE ATUACAO "Local de atuação" [DropDownList String → CPE_HOMOLOGACAO.LOCAL_DE_ATUACAO] obrigatório
  - CNPJ "CNPJ" [TextBox String → CP_ORDEM_SERVICO.CNPJ] — Configuracao={"SalvaLiteralMascara":true, "Mascara":""}
  - NÚMERO DO CHAMADO "Número da OS de Abertura de vaga para Contratação de Estagiário. (Inteiro)" [TextBox Integer → CP_ORDEM_SERVICO.NUMERO_DO_CHAMADO] obrigatório
  - HORARIO_ESTAG "Horário do estágio (o estagiário deverá cumprir 6 horas diárias)" [DropDownList String → CP_ORDEM_SERVICO.HORARIO_ESTAG] obrigatório

### [331029] EventoIntermediarioMensagem "Término de serviço"
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de serviço
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Em atendimento à Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto, comunico que foi realizado o término da atividade pelo Cesec.
Para mais detalhes sobre esta solicitação, clique no link a seguir ==> Link.Consulta.
 Complemento1 
Atenciosamente,
Central de Serviços

### [331030] EventoFinal ""
Responsável: Responsável atual (papel 36)
Config: TipoFinalizacao=NaoRealizado

### [331031] Tarefa "Aguardar Documentação do Estagiário"
Responsável: Fila CSC - Movimentação Pessoal (papel 510)
MotivoInterrupcaoSLA: Aguardando ação de intervenientes externos
- Operação PR0001 Preencher Campos
  - OBS_ACOMPA "Acompanhamento da Solicitação" [Memo String → CP_ORDEM_SERVICO.OBS_ACOMPA]

### [331032] Tarefa "Solicitar Aprovação do Gestor"
Responsável: Fila CSC - Movimentação Pessoal (papel 510)
Config: Codigo=APROV_GESTOR
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
#orgao = Orgao.Carrega("Id", OrdemServico.GetCustom("SCR_MOVI"));
#if (orgao != None):
#	OrdemServico.SetCustom("DESCRICAO_ORGAO",orgao.ToString())
#else:
#	OrdemServico.SetCustom("DESCRICAO_ORGAO","ORGAO NAO ENCONTRADO")
```
**ScriptFim**
```python
OrdemServico.MotivoCancelamento = OrdemServico.ObtemMotivoReprovacao("APROV_GESTOR")
```
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovação do Gestor; CopiarAnexados=true; MinimoAprovadores=1; UtilizaIdentidadeSolicitante=true; ReutilizaAprovacaoAnterior=true; ReenvioEmailAprovacao=12
  - (aprovação) DescricaoDetalhada (nativo) "Observação" — PermiteModificarAprovado=true
  - (aprovação) ATIVIDADES "Atividades a serem desenvolvidas" [Memo String(2000) → CP_ORDEM_SERVICO.ATIVIDADES] — PermiteModificarAprovado=true
  - (aprovação) PERIODO_CURSO "Período cursando" [DropDownList String → CP_ORDEM_SERVICO.PERIODO_CURSO] — PermiteModificarAprovado=true
  - (aprovação) SCR_TODOS_RH "UOR Movimentação" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH] — PermiteModificarAprovado=true
  - (aprovação) REQUISITOS "Requisitos desejáveis" [Memo String(2000) → CP_ORDEM_SERVICO.REQUISITOS] — PermiteModificarAprovado=true
  - (aprovação) HORARIO_ESTAG "Horário do estágio" [DropDownList String → CP_ORDEM_SERVICO.HORARIO_ESTAG] — PermiteModificarAprovado=true
  - (aprovação) FAVORECIDO_MONITOR "Supervisor" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_MONITOR] — PermiteModificarAprovado=true
  - (aprovação) CURSO "Curso" [TextBox String → CP_ORDEM_SERVICO.CURSO] — PermiteModificarAprovado=true
  - (aprovação) LOCALIDADE_MOV "Localidade Movimentação" [TextBox String → CP_ORDEM_SERVICO.LOCALIDADE_MOV] — PermiteModificarAprovado=true
  - (aprovação) SEXO_CONTRA "Sexo" [DropDownList String → CP_ORDEM_SERVICO.SEXO_CONTRA] — PermiteModificarAprovado=true
  - (aprovação) ESCOLARIDADE "Escolaridade" [DropDownList String → CP_ORDEM_SERVICO.ESCOLARIDADE] — PermiteModificarAprovado=true
  - aprovador: Aprovador de uma movimentação (Unico)

### [331033] Tarefa "Convocar Estagiário "
Responsável: Fila CSC - Movimentação Pessoal (papel 510)
**ScriptValidacao**
```python
if OrdemServico.GetCustom("ENTREGA_DOCUMENTO") == "Parcial" :
    Criticas.AdicionaPendencia("Entrega de documentação parcial !")
```

### [331034] EventoFinal "Chamado Finalizado"
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [331035] Tarefa "Preencher informações do estágio"
Responsável: Fila CSC - Movimentação Pessoal (papel 510)
Config: ConfirmaResponsabilidade=true
- Operação PR0001 Preencher Campos
  - CSC_OBS "Observação" [Memo String(2000) → CPE_CSC.CSC_OBS] obrigatório
  - HORA_ENTRADA "Horário do almoço" [TextBox String(80) → CP_ORDEM_SERVICO.HORA_ENTRADA] obrigatório
  - VALOR "Valor da Bolsa auxilio" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - VALOR_REMUNERACAO "Valor do Refeição" [TextBox String(13) → CP_ORDEM_SERVICO.VALOR_REMUNERACAO] obrigatório
  - VALOR_PAGAMENTO_RI "Auxilio Transporte" [TextBox String → CPE_CSC.VALOR_PAGAMENTO_RI] obrigatório
  - DATA_ADMISSAO "Data de Admissão" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ADMISSAO] obrigatório
  - VALOR_REEMBOLSO "Beneficios" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=ANEXOS
  - anexo "" classes: Solicitação de abertura de vaga
  - anexo "" classes: RG
  - anexo "Anexos" classes: Comprovante de Matrícula
  - anexo "" classes: CPF

### [331036] EventoIntermediarioMensagem "Reprovação do chamado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Aviso de reprovação de chamados
Corpo do comunicado: Prezado(a) OrdemServico.Cliente.Nome ,
A Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto não foi aprovada.
 Complemento1 
Para obter mais detalhes sobre a solicitação e a reprovação, CLIQUE no link =>> Link.Consulta 
Central de Serviços

### [331037] EventoIntermediarioMensagem "Admissão do estagiário"
Config: ListaDestinatarios=marcia_neves@bbtecno.com.br;admempregado@bbtecno.com.br;movimentacaopessoal@bbtecno.com.br;jovemaprendiz_estagiario@bbtecno.com.br
ModeloComunicado: Aviso sobre Contratação de Estagiário
Corpo do comunicado: Prezado(a),
Solicitamos a admissão do estagiário abaixo:
Chamado: OrdemServico.Numero 
Data de admissão: OrdemServico.Customizado.DATA_ADMISSAO 
SCR: OrdemServico.Customizado.SCR_TODOS_RH 
Dados: OrdemServico.Justificativa 
Atenciosamente,
Central de Serviços

### [331038] SubProcesso "Controle de Acesso - Brasília"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=704; ChamadaAssincrona=true; Configuracao={"ExibirBotaoNovaSubprocessos":false}
- ValoresInputs:
  - CustomPropertyId=1797; CustomProperty=CSC_NOME_COMPLETO
  - CustomPropertyId=545; CustomProperty=FAVORECIDO_MONITOR
  - CustomPropertyId=1350; CustomProperty=CSC_OBS
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
- Associação: Ativo=true; FraseAssociacao=A: CARTAO ACESSO MATRIZ; FraseInversaAssociacao=B: CONTR ESTAG; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=CONTRATA_ESTAG_X_ACESSO_BSB; SeparadorSequencial=. | fonte: Contratação de Estagiário → alvo: Cartão de Acesso - Matriz Brasília

### [331039] SubProcesso "Confecção de material - Crachá"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=707; ChamadaAssincrona=true; Configuracao={"ExibirBotaoNovaSubprocessos":false}
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
- Associação: Ativo=true; FraseAssociacao=A: CONTRATA ESTAGIARIO B: CONFEC MAT; FraseInversaAssociacao=A: CONTRATA ESTAGIARIO B: CONFEC MAT; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=A: CONTRATA ESTAGIARIO B: CONFEC MAT; SeparadorSequencial=. | fonte: Contratação de Estagiário → alvo: Confecção de Crachá

### [331040] Tarefa "Criar posição no sistema"
Responsável: Fila CSC - Movimentação Pessoal (papel 510)
**ScriptFormCarregado**
```python
Formulario["NUM_VERSAO"].Visivel=True
```
- Operação PR0001 Preencher Campos
  - NUM_VERSAO "Número da posição" [TextBox Integer → CP_ORDEM_SERVICO.NUM_VERSAO] obrigatório

### [331041] Tarefa "Solicitar documentação"
Responsável: Fila CSC - Movimentação Pessoal (papel 510)

### [331042] Tarefa "Disponibilização de Notebook (Caso necessário)"
Referência: Caro Solucionador,
Informar ao Solicitante o caminho para solicitação de Notebook.
https://centraldeti.bbts.com.br/servicePortal/submitSR?category_id=536
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=711; ChamadaAssincrona=true; Configuracao={"ExibirBotaoNovaSubprocessos":false}
- Associação: Ativo=true; FraseAssociacao=A: DISPONIBI BEM PAT C: CONTRATA ESTAG; FraseInversaAssociacao=C: CONTRATA ESTAG A: DISPONIBI BEM PAT; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=CONTRATA_ESTAG_; SeparadorSequencial=. | fonte: Contratação de Estagiário → alvo: Disponibilidade de Bem Patrimonial

### [331043] Tarefa "Verificar solicitação"
Responsável: Fila CSC - Movimentação Pessoal (papel 510)
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

## Papéis usados
### papel 230: Movimentação de Pessoal
Tipo=RelacaoGrupos
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
### papel 510: Fila CSC - Movimentação Pessoal
Tipo=RelacaoPessoas | pessoas: Fila CSC - Movimentação Pessoal
### papel 245: Aprovador de uma movimentação
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
idGestorRecurso = OrdemServico.GetCustom("FAVORECIDO_TODOS")
if idGestorRecurso != None:
    gestorRecurso = Pessoa.Carrega(Convert.ToInt32(idGestorRecurso))
    if gestorRecurso != None:
        Atores.Adiciona(gestorRecurso, "Gestor para aprovação")
```

## Campos customizados usados (definição global)

### CSC_NOME_COMPLETO — Nome Completo
TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO

### SCR_TODOS_RH — UOR Movimentação
DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH
Descrição: SCR Movimentação
**LookupScript**
```python
###PGESV###
Itens = DB.ExecuteDataTable("SELECT to_char(SCR) as SCR, NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO");
```

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### ESCOLARIDADE — Escolaridade
DropDownList String → CP_ORDEM_SERVICO.ESCOLARIDADE
Itens: Nível Médio;Nível Superior

### CURSO — Curso
TextBox String → CP_ORDEM_SERVICO.CURSO

### PERIODO_CURSO — Período cursando
DropDownList String → CP_ORDEM_SERVICO.PERIODO_CURSO
Itens: 1;2;3;4;5;6;7;8

### SEXO_CONTRA — Sexo
DropDownList String → CP_ORDEM_SERVICO.SEXO_CONTRA
Itens: Feminino;Masculino;Indiferente

### ATIVIDADES — Atividades
Memo String(2000) → CP_ORDEM_SERVICO.ATIVIDADES

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

### CSC_OBS — Observação
Memo String(2000) → CPE_CSC.CSC_OBS

### LOCAL DE ATUACAO — LOCAL DE ATUACAO
DropDownList String → CPE_HOMOLOGACAO.LOCAL_DE_ATUACAO
Itens: MACEIO;MANAUS;SALVADOR - AV. LUIS VIANA;SALVADOR - RUA MARQUES;FORTALEZA;BRASILIA - 716 NORTE;BRASILIA - MATRIZ;BRASILIA - PARQUE TECNOLOGICO;BRASILIA - SAUN QD 5;VITORIA;GOIANIA;SÃO LUIZ;BELO HORIZONTE;UBERLANDIA;CAMPO GRANDE;CUIABA;BELEM;JOAO PESSOA;RECIFE;TERESINA;CASCAVEL;CURITIBA - PRAÇA TIRADENTES;CURITIBA - RUA AMINTAS;LONDRINA;PIRAI;RIO DE JANEIRO - Estrada dos bandeirantes 10875;RIO DE JANEIRO - Estrada dos bandeirantes 13843;RIO DE JANEIRO - AV. REPUBLICA DO CHILE;RIO DE JANEIRO - CARIOCA;RIO DE JANEIRO - JACAREPAGUA;	RIO DE JANEIRO - TELEPORTO;NATAL;PORTO VELHO;PASSO FUNDO;PORTO ALE…

### CNPJ — CNPJ
TextBox String → CP_ORDEM_SERVICO.CNPJ

### NÚMERO DO CHAMADO — Número do Chamado
TextBox Integer → CP_ORDEM_SERVICO.NUMERO_DO_CHAMADO
Descrição: Número do Chamado no Sistema CHAMA.

### HORARIO_ESTAG — Horário do estágio (o estagiário deverá cumprir 6 horas diárias)
DropDownList String → CP_ORDEM_SERVICO.HORARIO_ESTAG
Itens: 08:00-15:00;08:30-15:30;09:00-16:00

### OBS_ACOMPA — Acompanhamento da Solicitação
Memo String → CP_ORDEM_SERVICO.OBS_ACOMPA

### REQUISITOS — Requisitos desejáveis
Memo String(2000) → CP_ORDEM_SERVICO.REQUISITOS

### LOCALIDADE_MOV — Localidade Movimentação
TextBox String → CP_ORDEM_SERVICO.LOCALIDADE_MOV

### HORA_ENTRADA — Hora Entrada
TextBox String(80) → CP_ORDEM_SERVICO.HORA_ENTRADA

### VALOR — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR
Descrição: Informe

### VALOR_REMUNERACAO — Valor da Remuneração
TextBox String(13) → CP_ORDEM_SERVICO.VALOR_REMUNERACAO

### VALOR_PAGAMENTO_RI — Valor de pagamento do RI
TextBox String → CPE_CSC.VALOR_PAGAMENTO_RI

### DATA_ADMISSAO — Data de Admissão
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ADMISSAO

### VALOR_REEMBOLSO — Valor do Reembolso
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REEMBOLSO

### NUM_VERSAO — Número da Posição
TextBox Integer → CP_ORDEM_SERVICO.NUM_VERSAO

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
