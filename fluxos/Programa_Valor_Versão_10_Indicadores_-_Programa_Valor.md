# Fluxo: Indicadores - Programa Valor (INDICPV) — versão 10
Caminho: Fluxos > Programa Valor Versão 10 Indicadores - Programa Valor
XML: `XMLs para teste/Programa_Valor_Versão_10_Indicadores_-_Programa_Valor.xml` | Supravizio 19.1.1 | SubProcessoId 19398 | DesenhoProcessoId 2765 | ProcessoId 695
Órgão dono: 3000004051 - PROJETO SAIET | Responsável: DAIANY NEVES ROSA
Classe do subprocesso: CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PermiteVisualizacaoGestorSubNiveis=true; RegraAutorizacao=VisivelSolucionadorMacroprocesso; PublicarApontamentosAA=Nunca
Serviços: Indicadores - Programa Valor (INDICAPV)

## Grafo do fluxo
- [310411] Tarefa "Motivo de Aprovação do chamado (Tarefa Avança Automáticamente)" {Cliente} → [310406] Aprovação e Finalização do Chamado
- [310399] SubProcesso "Índice de Proposição e Validação de Casos de Uso para o SOC" {Gerente de Centro Comitê} → [310402] Subprocesso e Chamado Finalizado
- [310400] EventoIntermediarioMensagem "E-mail de Confirmação das Respostas" → [310405] Abertura de Chamado - Comitê
- [310401] EventoFinal "Sucesso" → (fim)
- [310402] EventoIntermediarioMensagem "Subprocesso e Chamado Finalizado" → [310401] Sucesso
- [310403] EventoFinal "Sucesso" → (fim)
- [310404] Tarefa "Aprovação do Gerente de Centro" {Gerente do Cliente} → [G71422] Aprovado?
- [310405] EventoIntermediarioMensagem "Abertura de Chamado - Comitê" → [310404] Aprovação do Gerente de Centro
- [310406] EventoIntermediarioMensagem "Aprovação e Finalização do Chamado" → [310403] Sucesso
- [310407] EventoIntermediarioMensagem "Reprovação de Chamado" → [310410] Cancelado
- [310408] EventoInicial "Inicio" {Cliente} → [G71424] Indice de Proposição e Validação?
- [310409] Tarefa "Motivo de Reprovação do chamado (Tarefa Avança Automáticamente)" {Cliente} → [310407] Reprovação de Chamado
- [310410] FimCancelamento "Cancelado" → (fim)
- [G71422] Gateway "Aprovado?" → «Não» [310409] Motivo de Reprovação do chamado (Tarefa Avança Aut | «Sim» [310411] Motivo de Aprovação do chamado (Tarefa Avança Auto
- [G71423] Gateway " Confirmação de Respostas?" → «Não» [310405] Abertura de Chamado - Comitê | «Sim» [310400] E-mail de Confirmação das Respostas
- [G71424] Gateway "Indice de Proposição e Validação?" → «Não» [G71423]  Confirmação de Respostas? | «Sim» [310399] Índice de Proposição e Validação de Casos de Uso p

## Gateways
### [G71422] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROV")
```
- alternativa → [310409] Motivo de Reprovação do chamado (Tarefa Avança Aut: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
- alternativa → [310411] Motivo de Aprovação do chamado (Tarefa Avança Auto: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
### [G71423]  Confirmação de Respostas? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.GetCustom("CHECKBOX1") == True
```
- alternativa → [310405] Abertura de Chamado - Comitê: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
- alternativa → [310400] E-mail de Confirmação das Respostas: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
### [G71424] Indice de Proposição e Validação? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.GetCustom("TEXT4") == "47 - Índice de Proposição e Validação de Casos de Uso para o SOC"
```
- alternativa → [G71423]  Confirmação de Respostas?: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
- alternativa → [310399] Índice de Proposição e Validação de Casos de Uso p: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```

## Atividades

### [310411] Tarefa "Motivo de Aprovação do chamado (Tarefa Avança Automáticamente)"
Responsável: Cliente (papel 18)
**ScriptInicio**
```python
numero = OrdemServico.Numero

query = DB.ExecuteDataTable("SELECT OCORRENCIA.NUMERO, MIN(APROVACAO.MOTIVO) AS MOTIVO_MINIMO, MAX(APROVACAO.MOTIVO) AS MOTIVO_MAXIMO FROM OCORRENCIA INNER JOIN CLASSE_SUB_PROCESSO ON OCORRENCIA.ID_CLASSE_SUB_PROC = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO INNER JOIN ASSUNTO_APROVACAO ON OCORRENCIA.ID_OCORRENCIA = ASSUNTO_APROVACAO.ID_OCORRENCIA INNER JOIN VERSAO_APROVACAO ON ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO = VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO INNER JOIN APROVACAO ON VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO = APROVACAO.ID_ASSUNTO_APROVACAO WHERE OCORRENCIA.NUMERO = '"+numero.ToString()+"' GROUP BY OCORRENCIA.NUMERO")

for motivo in query.Rows:
    motivo1 = motivo["MOTIVO_MINIMO"].ToString()
    
    OrdemServico["OBS30"] = motivo1.ToString()

    

AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos
  - OBS30 "Motivo da Aprovação do Chamado" [Memo String(900) → CPE_CSC.OBS30] obrigatório

### [310399] SubProcesso "Índice de Proposição e Validação de Casos de Uso para o SOC"
Responsável: Gerente de Centro Comitê (papel 1307)
Config: AssociacaoId=1461; PassaTodosItens=true
- ValoresInputs:
  - CustomPropertyId=3792; CustomProperty=CHECKBOX1
  - CustomPropertyId=550; CustomProperty=FAVORECIDO_COBRA
  - CustomPropertyId=1579; CustomProperty=TE_MATRICULA
  - CustomPropertyId=1589; CustomProperty=TE_UOR
  - CustomPropertyId=5101; CustomProperty=TEXT4
  - CustomPropertyId=5053; CustomProperty=TITULO_PROPOSTA
  - CustomPropertyId=2583; CustomProperty=OBS23
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2763; ClasseConfiguracao=Anexo
- Associação: Ativo=true; FraseAssociacao=Indicadores --> Índice de Proposição e Validação de Casos de Uso para o SOC; FraseInversaAssociacao=Índice de Proposição e Validação de Casos de Uso para o SOC --> Indicadores; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=INDICAINDICE; SeparadorSequencial=. | fonte: Indicadores - Programa Valor → alvo: Índice de Proposição e Validação de Casos de Uso para o SOC

### [310400] EventoIntermediarioMensagem "E-mail de Confirmação das Respostas"
Destinatário: Cliente (papel 18)
ModeloComunicado: Indicadores - Programa Valor ( Confirmação das Respostas)
Corpo do comunicado: Assunto:
 [Programa Valor] Indicadores - Programa Valor
 Corpo do e-mail:
 Prezado(a) Técnico(a),
 Encaminhamos abaixo os itens referentes à abertura do chamado no âmbito do Programa Valor – Indicadores:
 Favorecido:
 OrdemServico.Customizado.FAVORECIDO_COBRA 
 Matrícula:
 OrdemServico.Customizado.TE_MATRICULA 
 UOR:
 OrdemServico.Customizado.TE_UOR 
 Competência selecionada:
 OrdemServico.Customizado.COMBOBOX_I 
 Indicador da Competência "Automatizador":
 OrdemServico.Customizado.COMBOBOX_II 
 Título da Automatização/Inovação:
 OrdemServico.Customizado.TITULO_AUTOMACAO 
 Indicador da Competência "Viagem de Longa Distância":
 OrdemServico.Customizado.TEXT_1 
 Número Sisloc:
 OrdemServico.Cus…

### [310401] EventoFinal "Sucesso"

### [310402] EventoIntermediarioMensagem "Subprocesso e Chamado Finalizado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Indicadores - Programa Valor ( Chamado Finalizado com Sucesso Subprocesso)
Corpo do comunicado: Assunto:
[Programa Valor] Indicadores- Programa Valor
Corpo do e-mail:
Prezado(a) Técnico(a),
Informamos que o seu chamado de número: OrdemServico.Numero foi finalizado com sucesso!
Sua solicitação de Indicadores - Programa Valor foi OrdemServico.Customizado.COMBOBOX_I 
Atenciosamente,
Programa Valor

### [310403] EventoFinal "Sucesso"

### [310404] Tarefa "Aprovação do Gerente de Centro"
Responsável: Gerente do Cliente (papel 10)
Config: Codigo=APROV
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexar Documento (Opcional)" classes: Anexo — RequeridoInicial=true
- Operação PR0002 Aprovar: MinimoAprovadores=1; ObrigatoriedadeMotivo=Todas
  - (aprovação) COMBOBOX_IV "Selecione a Skill" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_IV]
  - (aprovação) TEXT_1 "Selecione o Indicador da Competência "Viagem de Longa Distância":" [TextBox String(1000) → CPE_CSC.TEXT_1]
  - (aprovação) FAVORECIDO_COBRA "Favorecido:" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
  - (aprovação) OBS23 "Descrição da proposta:" [Memo String(4000) → CPE_CSC.OBS23]
  - (aprovação) INDICADOR_MULTISKILL "Selecione o Indicador da Competência Multiskill" [DropDownList String → CPE_CONTRATOS02.INDICADOR_MULTISKILL]
  - (aprovação) OBS22 "Descreva a peça modelada:" [Memo String(4000) → CPE_CSC.OBS22]
  - (aprovação) ESPECIALIDADE_PV "Selecione a Especialidade" [DropDownList String → CPE_CONTRATOS02.ESPECIALIDADE_PV]
  - (aprovação) COMBOBOX_I "Selecione a Competência:" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_I]
  - (aprovação) OBS21 "Descreva a Automatização ou Inovação:" [Memo String(4000) → CPE_CSC.OBS21]
  - (aprovação) TEXT2 "Selecione o Indicador da Competência "Modelagem de Peças":" [TextBox String → CPE_CSC.TEXT2]
  - (aprovação) TEXT4 "Selecione o Indicador da Competência "Segurança de TIC":" [TextBox String → CPE_CONTRATOS.TEXT4]
  - (aprovação) TITULO_PROPOSTA "Título da proposta:" [TextBox String → CPE_CSC.TITULO_PROPOSTA]
  - (aprovação) COMBOBOX_II "Selecione o Indicador da Competência "Automatizador":" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_II]
  - (aprovação) NUMERO_1 "Número Sisloc:" [TextBox String → CPE_CONTRATOS.NUMERO_1]
  - (aprovação) CHECKBOX1 "Enviar-me um email de confirmação de minhas respostas" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX1]
  - (aprovação) TITULO_AUTOMACAO "Informe o título da sua Automatização ou Inovação:" [TextBox String → CPE_CONTRATOS.TITULO_AUTOMACAO]
  - (aprovação) COMBOBOX_III "Selecione a Categoria" [DropDownList String → CPE_BENS_INVENTARIO.COMBOBOX_III]
  - (aprovação) TE_MATRICULA "Matricula:" [TextBox String → CPE_CSC.TE_MATRICULA]
  - (aprovação) TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR]
  - item para aprovação "Anexar Documento(s)"
  - aprovador: Gerente do Cliente (Unico)

### [310405] EventoIntermediarioMensagem "Abertura de Chamado - Comitê"
Destinatário: Gerente de Centro Comitê (papel 1307)
Config: ListaDestinatarios=richard.pistori@bbts.com.br; omar.barham@bbts.com.br; EnviaMensagemIndividual=true; EmailRemetente=omar.barham@bbts.com.br
ModeloComunicado: Aviso de abertura de chamado - 1
Corpo do comunicado: Prezado(a),
Foi aberta a ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [310406] EventoIntermediarioMensagem "Aprovação e Finalização do Chamado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Indicadores - Programa Valor ( Chamado Finalizado com Sucesso)
Corpo do comunicado: Assunto:
[Programa Valor] Indicadores - Número: OrdemServico.Numero 
Corpo do e-mail:
Prezado(a) Técnico(a),
Sua solicitação para OrdemServico.Customizado.COMBOBOX_I foi aprovada com sucesso pelo comitê avaliador.
Segue abaixo o motivo da aprovação: 
OrdemServico.Customizado.OBS30 
Atenciosamente,
Programa Valor

### [310407] EventoIntermediarioMensagem "Reprovação de Chamado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Indicadores - Programa Valor ( Chamado Cancelado)
Corpo do comunicado: Assunto:[Programa Valor] Indicadores - Número: OrdemServico.Numero 
Corpo do e-mail:
Prezado(a) Técnico(a),
Sua solicitação para OrdemServico.Customizado.COMBOBOX_I foi reprovada pelo comitê avaliador.
Segue abaixo o motivo da reprovação: 
OrdemServico.Customizado.OBS31 
Atenciosamente,
Programa Valor

### [310408] EventoInicial "Inicio"
Responsável: Cliente (papel 18)
TipoSolicitacao: Indicadores - Programa Valor
**ScriptFormCarregado**
```python
from Venki.Supravizio.Processo.Custom import Indicador
from Venki.Supravizio.Processo.Custom import Processo
#=== Escondendo os campos
Formulario["COMBOBOX_II"].Visivel = False
Formulario["TEXT_1"].Visivel = False
Formulario["TEXT2"].Visivel = False
Formulario["TEXT4"].Visivel = False
Formulario["OBS21"].Visivel = False
Formulario["OBS22"].Visivel = False
Formulario["OBS23"].Visivel = False
Formulario["NUMERO_1"].Visivel = False
Formulario["TITULO_AUTOMACAO"].Visivel = False
Formulario["TITULO_PROPOSTA"].Visivel = False
Formulario["INDICADOR_MULTISKILL"].Visivel = False
Formulario["ESPECIALIDADE_PV"].Visivel = False
Formulario['COMBOBOX_IV'].Visivel = False
Formulario['COMBOBOX_III'].Visivel = False
 

# === Dicionário com Competências e Indicadores
indicadores_por_perfil = {
    "Automatização (Gecob)": [
        "48 - Inovação - N1",
        "48 - Inovação - N2",
        "49 - Automatização - N1",
        "49 - Automatização - N2",
        "49 - Automatização - N3"
    ],
    "Automatização (demais unidades)": [
        "26 - Automatizador de Tecnologia - N1",
        "26 - Automatizador de Tecnologia - N2",
        "27 - Inovação de Processos - N1",
        "27 - Inovação de Processos - N2",
        "27 - Inovação de Processos - N3"
    ],
    "Viagem de Longa Distância": [],
    "Modelagem de Peças": [],
    "Segurança de TIC": [],
    "MultiSkill": []
}

def ativar_campo(*nomes):
    for nome in nomes:
        Formulario[nome].Visivel = True

def desativar_campo(*campos):
    for campo in campos:
        Formulario[campo].Visivel = False    

# Preenche COMBOBOX_I com as chaves do dicionário
Formulario["COMBOBOX_I"].Itens = "; ".join(indicadores_por_perfil.keys())

# Obtém valor selecionado na COMBOBOX_I
competencia = Formulario["COMBOBOX_I"].Valor

if competencia in ["Automatização (Gecob)", "Automatização (demais unidades)"]:
    ativar_campo("COMBOBOX_II", "TITULO_AUTOMACAO", "OBS21")
    desativar_campo("TEXT_1", "NUMERO_1", "TEXT2", "OBS22", "TEXT4", "TITULO_PROPOSTA", "OBS23")
    Formulario["COMBOBOX_II"].Itens = "; ".join(indicadores_por_perfil.get(competencia, []))

elif competencia == "Viagem de Longa Distância":
    ativar_campo("TEXT_1", "NUMERO_1")
    desativar_campo("COMBOBOX_II", "TITULO_AUTOMACAO", "OBS21",
                    "TEXT2", "OBS22", "TEXT4", "TITULO_PROPOSTA", "OBS23")
    Formulario["TEXT_1"].Valor = "25 - Viagem longa distância (Acima de 400 km)"
    Formulario["TEXT_1"].Habilitado = False

elif competencia == "Modelagem de Peças":
    ativar_campo("TEXT2", "OBS22")
    desativar_campo("COMBOBOX_II", "TITULO_AUTOMACAO", "OBS21",
                    "TEXT_1", "NUMERO_1", "TEXT4", "TITULO_PROPOSTA", "OBS23")
    Formulario["TEXT2"].Valor = "28 - Projetos modelados para impressão de peças"
    Formulario["TEXT2"].Habilitado = False

elif competencia == "Segurança de TIC":
    ativar_campo("TEXT4", "TITULO_PROPOSTA", "OBS23")
    desativar_campo("COMBOBOX_II", "TITULO_AUTOMACAO", "OBS21",
                    "TEXT_1", "NUMERO_1", "TEXT2", "OBS22")
    Formulario["TEXT4"].Valor = "47 - Índice de Proposição e Validação de Casos de Uso para o SOC"
    Formulario["TEXT2"].Habilitado = False

fonte = 'Times New Roman'
Formulario['LABEL_GRANDE'].Valor = '<div style="display: flex; justify-content: center; align-items: center;"><div style="display: flex; align-items: center; width: 100%; background-color: yellow; border-radius: 16px; padding: 2%;"><img src="https://bbtecno.sharepoint.com/sites/ProgramaValor/_api/siteiconmanager/getsitelogo?type=%271%27&hash=638572528631350848" alt="Ícone" style="height: 60px; margin-right: 16px;"><br><p style="flex: 1; text-align: center; color: blue; font-weight: 600; font-size: 28px; font-family: {0}; margin: 0;">INDICADORES - Programa Valor</p></div></div><br>'.format(fonte)


Formulario['INDICADOR_MULTISKILL'].Itens = 'Operação 360°'
Formulario['ESPECIALIDADE_PV'].Itens = 'Monitoração de Equipamentos; Atendimento Especializado em Processos de Rede; Planejamento de Materiais'
```
- Operação PR0001 Preencher Campos
  - LABEL_GRANDE "Label Grande" [Label String(2000) → CPE_MOVIMENTACAO_PESSOA.LABEL_GRANDE] obrigatório
  - FAVORECIDO_COBRA "Favorecido:" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
**FAVORECIDO_COBRA.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
# === Converte o campo Favorecido Cobra
idFavorecidoCobra = Convert.ToInt32(Formulario["FAVORECIDO_COBRA"].Valor)
FavorecidoCobra = Pessoa.Carrega(idFavorecidoCobra)

# === Consulta para trazer as informações MATRICULA e UOR
query = Utils.ExecuteDataTable("SELECT CP.MATRICULA, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO WHERE P.ID_PESSOA = '" + idFavorecidoCobra.ToString() + "'")


# === Percorre os valores na query, preenche e ativa os campos.
for campo in query.Rows:
    Formulario["TE_MATRICULA"].Visivel = True
    Formulario["TE_UOR"].Visivel = True
    
    Formulario["TE_MATRICULA"].Valor = campo["MATRICULA"].ToString()
    Formulario["TE_UOR"].Valor = campo["DESCRICAO"].ToString()
    
    Formulario["TE_MATRICULA"].Habilitado = False
    Formulario["TE_UOR"].Habilitado = False
```
  - TE_MATRICULA "Matricula:" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório — Coluna=2
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório — Coluna=3
  - COMBOBOX_I "Selecione a Competência:" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_I] obrigatório
**COMBOBOX_I.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Indicador
from Venki.Supravizio.Processo.Custom import Processo
# === Dicionário com Competências e Indicadores
indicadores_por_perfil = {
    "Automatização (Gecob)": [
        "48 - Inovação - N1",
        "48 - Inovação - N2",
        "49 - Automatização - N1",
        "49 - Automatização - N2",
        "49 - Automatização - N3"
    ],
    "Automatização (demais unidades)": [
        "26 - Automatizador de Tecnologia - N1",
        "26 - Automatizador de Tecnologia - N2",
        "27 - Inovação de Processos - N1",
        "27 - Inovação de Processos - N2",
        "27 - Inovação de Processos - N3"
    ],
    "Viagem de Longa Distância": [],
    "Modelagem de Peças": [],
    "Segurança de TIC": [],
    "MultiSkill": [],
    "Atendimento": [
        "Criticidade de Peças"
    ]
}

def ativar_campo(*nomes):
    for nome in nomes:
        Formulario[nome].Visivel = True

def desativar_campo(*campos):
    for campo in campos:
        Formulario[campo].Visivel = False
      
       

# Preenche COMBOBOX_I com as chaves do dicionário
Formulario["COMBOBOX_I"].Itens = "; ".join(indicadores_por_perfil.keys())

# Obtém valor selecionado na COMBOBOX_I
competencia = Formulario["COMBOBOX_I"].Valor

Formulario.ExibeMensagem(competencia)

if competencia in ["Automatização (Gecob)", "Automatização (demais unidades)"]:
    ativar_campo("COMBOBOX_II", "TITULO_AUTOMACAO", "OBS21")
    desativar_campo("TEXT_1", "NUMERO_1", "TEXT2", "OBS22", "TEXT4", "TITULO_PROPOSTA", "OBS23", "COMBOBOX_III", "COMBOBOX_IV", "INDICADOR_MULTISKILL", "ESPECIALIDADE_PV")
    Formulario["COMBOBOX_II"].Itens = "; ".join(indicadores_por_perfil.get(competencia, []))

elif competencia == "Atendimento":

    desativar_campo(
        "TITULO_AUTOMACAO", "OBS21",
        "TEXT_1", "NUMERO_1",
        "TEXT2", "OBS22",
        "TITULO_PROPOSTA", "OBS23",
        "INDICADOR_MULTISKILL", "ESPECIALIDADE_PV",
        "COMBOBOX_III", "COMBOBOX_IV", "TEXT4"
    )

    Formulario['COMBOBOX_II'].Itens = "Criticidade de Peças"

elif competencia == "Viagem de Longa Distância":
    ativar_campo("TEXT_1", "NUMERO_1")
    desativar_campo("COMBOBOX_II", "TITULO_AUTOMACAO", "OBS21",
                    "TEXT2", "OBS22", "TEXT4", "TITULO_PROPOSTA", "OBS23", "INDICADOR_MULTISKILL", "ESPECIALIDADE_PV", "COMBOBOX_III", "COMBOBOX_IV")
    Formulario["TEXT_1"].Valor = "25 - Viagem longa distância (Acima de 400 km)"
    Formulario["TEXT_1"].Habilitado = False

elif competencia == "Modelagem de Peças":
    ativar_campo("TEXT2", "OBS22")
    desativar_campo("COMBOBOX_II", "TITULO_AUTOMACAO", "OBS21",
                    "TEXT_1", "NUMERO_1", "TEXT4", "TITULO_PROPOSTA", "OBS23", "INDICADOR_MULTISKILL", "ESPECIALIDADE_PV", "COMBOBOX_III", "COMBOBOX_IV")
    Formulario["TEXT2"].Valor = "28 - Projetos modelados para impressão de peças"
    Formulario["TEXT2"].Habilitado = False

elif competencia == "Segurança de TIC":
    ativar_campo("TEXT4", "TITULO_PROPOSTA", "OBS23")
    desativar_campo("COMBOBOX_II", "TITULO_AUTOMACAO", "OBS21",
                    "TEXT_1", "NUMERO_1", "TEXT2", "OBS22", "INDICADOR_MULTISKILL", "ESPECIALIDADE_PV", "COMBOBOX_III", "COMBOBOX_IV")
    Formulario["TEXT4"].Valor = "47 - Índice de Proposição e Validação de Casos de Uso para o SOC"
    Formulario["TEXT4"].Habilitado = False
    
elif competencia == "MultiSkill":
    ativar_campo("INDICADOR_MULTISKILL", "ESPECIALIDADE_PV")
    desativar_campo("TEXT_1", "NUMERO_1", "TEXT2", "OBS22", "TEXT4", "TITULO_PROPOSTA", "OBS23", "COMBOBOX_II", "TITULO_AUTOMACAO")
```
  - INDICADOR_MULTISKILL "Selecione o Indicador da Competência Multiskill" [DropDownList String → CPE_CONTRATOS02.INDICADOR_MULTISKILL] obrigatório — Coluna=2
  - ESPECIALIDADE_PV "Selecione a Especialidade" [DropDownList String → CPE_CONTRATOS02.ESPECIALIDADE_PV] obrigatório — Coluna=3
**ESPECIALIDADE_PV.ScriptModificado**
```python
espec = Formulario['ESPECIALIDADE_PV'].Valor
categoria = Formulario['COMBOBOX_III']
skill = Formulario['COMBOBOX_IV']
skill.Habilitado = True
skill.Valor = ""


if not String.IsNullOrEmpty(espec):
    if espec == "Monitoração de Equipamentos":
        skill.Itens = "Monitoração eqpt. não terceirizados;Monitoração eqpt. terceirizados;Abastecimento;ANS;TAATI;Gestão de ativos"
        skill.Visivel = True
        categoria.Visivel = False
        
    else:
        categoria.Itens = "Administrativo; Atende; Demais Bens; Outsourcing; TAA; Alertas; Planejamento; Análise e Estoques; Cadastros; Distribuição e Cargas; Fluxos e Acionamentos"
        categoria.Visivel = True
        skill.Visivel = True
```
  - COMBOBOX_II "Selecione o Indicador da Competência "Automatizador":" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_II] obrigatório
  - COMBOBOX_III "Selecione a Categoria" [DropDownList String → CPE_BENS_INVENTARIO.COMBOBOX_III] obrigatório
**COMBOBOX_III.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Supravizio.Processo.Custom import Atividade
categoria = Formulario['COMBOBOX_III']
skill = Formulario['COMBOBOX_IV']

if categoria.Valor == "Administrativo":
    skill.Itens = "Administração contratos;Administração predial;Atividades V360;Controle de OC;Faturamento;Fiscalização de serviços;Serviços administrativos;Validação documentação e notas fiscais;Fiscalização de Serviços"
    
elif categoria.Valor == "Atende":
    skill.Itens = "Acionamento garantia;Agendamentos;Agendamentos gerais;Atendimentos eventuais;Atividades credenciada PGDM;Atividades sala online;Contrato 06;Laudos (análise e inserção);Remanejamento;Substituição banco de baterias;Fiscalização de Serviços"
    
elif categoria.Valor == "Demais Bens":
    skill.Itens = "Acompanhamento PDS;Agendamentos específicos;Agendamentos gerais;Atendimentos eventuais e cota 100;Atividades de TI;Instalação switch;Remanejamento;Validação demandas e documentações;Fiscalização de Serviços"
    
elif categoria.Valor == "Outsourcing":
    skill.Itens = "Agendamentos gerais;Carro oficina;Instalação equipamentos PVV/Áudio bidirecional;Instalação equipamentos segurança;Manutenção de infraestrutura;Fiscalização de Serviços"
    
elif categoria.Valor == "TAA":
    skill.Itens = "Agendamentos gerais;Atividades de controle e validação de documentos;Atividades de controle e validação serviços;Cofre;Descarte;Modernização;Remanejamento;Revitalização;Terceirização/desterceirização;TAATI;AFRANIO;Fiscalização de Serviços"
    
elif categoria.Valor == "Alertas":
    skill.Itens = "SOBR PLAN JS;SOBR PLAN CS;SOBR PLAN LA;FIEL; ATOS"
    
elif categoria.Valor == "Planejamento":
    skill.Itens = "Plano Reparo; Plano Aquisição; Tratamento Requisições"
    
elif categoria.Valor == "Análise e Estoques":
    skill.Itens = "Retirada IMOB; Retirada Manut; Retirada WR; Dotação Semanal"
    
elif categoria.Valor == "Cadastros":
    skill.Itens = "Acerto Sistêmico; Precificação de Itens; Baixa para despesa"
    
elif categoria.Valor == "Distribuição e Cargas":
    skill.Itens = "Distribuição Embalagem; Distribuição Ferramentas; Ordens Transferência FIEL; Ordens Transferência ATOS; Ordens Transferência SOBR; Cobovalt SOBR/FIEL/ATOS; Relatório FUP; Relatório OV pendentes/Atos/Fiel"
    
elif categoria.Valor == "Fluxos e Acionamentos":
    skill.Itens = "Análise Transações diversas; Análise de Orçamento e Cota/50; Garantia Ativos"
```
  - COMBOBOX_IV "Selecione a Skill" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_IV] obrigatório — Coluna=2
  - TITULO_AUTOMACAO "Informe o título da sua Automatização ou Inovação:" [TextBox String → CPE_CONTRATOS.TITULO_AUTOMACAO] obrigatório
  - TEXT_1 "Selecione o Indicador da Competência "Viagem de Longa Distância":" [TextBox String(1000) → CPE_CSC.TEXT_1] obrigatório
  - NUMERO_1 "Número Sisloc:" [TextBox String → CPE_CONTRATOS.NUMERO_1] obrigatório
  - TEXT2 "Selecione o Indicador da Competência "Modelagem de Peças":" [TextBox String → CPE_CSC.TEXT2] obrigatório
  - TEXT4 "Selecione o Indicador da Competência "Segurança de TIC":" [TextBox String → CPE_CONTRATOS.TEXT4] obrigatório
  - TITULO_PROPOSTA "Título da proposta:" [TextBox String → CPE_CSC.TITULO_PROPOSTA] obrigatório
  - OBS21 "Descreva a Automatização ou Inovação:" [Memo String(4000) → CPE_CSC.OBS21] obrigatório
  - OBS22 "Descreva a peça modelada:" [Memo String(4000) → CPE_CSC.OBS22] obrigatório
  - OBS23 "Descrição da proposta:" [Memo String(4000) → CPE_CSC.OBS23] obrigatório
  - CHECKBOX1 "Enviar-me um email de confirmação de minhas respostas" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX1] obrigatório
  - CHECKBOX2 "Ler Planilha" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX2] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexar Documento(s)" classes: Anexo — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=PLANILHA
  - anexo "Anexar Planilha de Criticidade" classes: Arquivo 01 — RequeridoInicial=true

### [310409] Tarefa "Motivo de Reprovação do chamado (Tarefa Avança Automáticamente)"
Responsável: Cliente (papel 18)
**ScriptInicio**
```python
numero = OrdemServico.Numero

query = DB.ExecuteDataTable("SELECT OCORRENCIA.NUMERO, MIN(APROVACAO.MOTIVO) AS MOTIVO_MINIMO, MAX(APROVACAO.MOTIVO) AS MOTIVO_MAXIMO FROM OCORRENCIA INNER JOIN CLASSE_SUB_PROCESSO ON OCORRENCIA.ID_CLASSE_SUB_PROC = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO INNER JOIN ASSUNTO_APROVACAO ON OCORRENCIA.ID_OCORRENCIA = ASSUNTO_APROVACAO.ID_OCORRENCIA INNER JOIN VERSAO_APROVACAO ON ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO = VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO INNER JOIN APROVACAO ON VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO = APROVACAO.ID_ASSUNTO_APROVACAO WHERE OCORRENCIA.NUMERO = '"+numero.ToString()+"' GROUP BY OCORRENCIA.NUMERO")

for motivo in query.Rows:
    motivo1 = motivo["MOTIVO_MINIMO"].ToString()
    
    OrdemServico["OBS31"] = motivo1.ToString()

    

AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos
  - OBS31 "Motivo da Reprovação do Chamado" [Memo String(900) → CPE_CSC.OBS31] obrigatório

### [310410] FimCancelamento "Cancelado"

## Papéis usados
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 1307: Gerente de Centro Comitê
Tipo=RelacaoOrgaos
### papel 10: Gerente do Cliente
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

### OBS30 — Observação30
Memo String(900) → CPE_CSC.OBS30

### COMBOBOX_IV — COMBOBOX_IV
DropDownList String → CPE_BOOTCAMP.COMBOBOX_IV

### TEXT_1 — TEXT_1
TextBox String(1000) → CPE_CSC.TEXT_1

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### OBS23 — Observação23
Memo String(4000) → CPE_CSC.OBS23

### INDICADOR_MULTISKILL — Selecione o Indicador da Competência Multiskill
DropDownList String → CPE_CONTRATOS02.INDICADOR_MULTISKILL
**LookupScript**
```python
#
```

### OBS22 — Observação22
Memo String(4000) → CPE_CSC.OBS22

### ESPECIALIDADE_PV — Selecione a Especialidade
DropDownList String → CPE_CONTRATOS02.ESPECIALIDADE_PV
**LookupScript**
```python
#
```

### COMBOBOX_I — COMBOBOX_I
DropDownList String → CPE_BOOTCAMP.COMBOBOX_I

### OBS21 — Observação21
Memo String(4000) → CPE_CSC.OBS21

### TEXT2 — TEXT2
TextBox String → CPE_CSC.TEXT2

### TEXT4 — TEXT4
TextBox String → CPE_CONTRATOS.TEXT4

### TITULO_PROPOSTA — Titulo da Proposta
TextBox String → CPE_CSC.TITULO_PROPOSTA
Descrição: TITULO_PROPOSTA

### COMBOBOX_II — COMBOBOX_II
DropDownList String → CPE_BOOTCAMP.COMBOBOX_II

### NUMERO_1 — NUMERO_1
TextBox String → CPE_CONTRATOS.NUMERO_1

### CHECKBOX1 — Checkbox1
CheckBox Boolean → CPE_PESSOAS.CHECKBOX1

### TITULO_AUTOMACAO — TITULO_AUTOMACAO
TextBox String → CPE_CONTRATOS.TITULO_AUTOMACAO

### COMBOBOX_III — COMBOBOX_III
DropDownList String → CPE_BENS_INVENTARIO.COMBOBOX_III

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

### LABEL_GRANDE — Label Grande
Label String(2000) → CPE_MOVIMENTACAO_PESSOA.LABEL_GRANDE

### CHECKBOX2 — Checkbox2
CheckBox Boolean → CPE_PESSOAS.CHECKBOX2

### OBS31 — Observação31
Memo String(900) → CPE_CSC.OBS31

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
