# Fluxo: Nomeação (NOMEACAO) — versão 75
Caminho: Fluxos > Ascensão Profissional e Movimentação de Pessoas Versão 75 Nomeação
XML: `XMLs para teste/Ascensão_Profissional_e_Movimentação_de_Pessoas_Versão_75_Nomeação.xml` | Supravizio 19.1.1 | SubProcessoId 22746 | DesenhoProcessoId 3071 | ProcessoId 58
Órgão dono: 3000003210 - DIVISAO DE BENEFICIOS E MOVIMENTACOES DE PESSOAL | Responsável: PALOMA SABINE AMADO ROSA VARGAS
Classe do subprocesso: Objetivo=Nomeação de assessores, gerentes e analistas.; DescricaoCliente=NOMEAÇÃO; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Nomeação de assessores, gerentes e analistas.; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Nomeação COM Transferência (NOMEAT); Nomeação SEM transferência (NOMEA)

## Grafo do fluxo
- [370944] SubProcesso "Consulta UniBBTS" {00. Cesec - Outros Serviços} → [370966] Solicitação de Consulta de Férias
- [370945] EventoIntermediarioMensagem "Solicitação de Consulta Controle Disciplinar" → [370948] Consulta Controle Disciplinar
- [370946] EventoIntermediarioMensagem "Término de serviço" → [G83008] Serviço?
- [370947] FimCancelamento "Cancelado" → (fim)
- [370948] SubProcesso "Consulta Controle Disciplinar" {Fila Controle Disciplinar} → [370956] Aguardar retornos dos subchamados (inserir pausa)
- [370949] Tarefa "Avaliar retornos" {Responsável atual} → [G83007] Colaborador apto a nomeação?
- [370950] EventoInicial "Evento inicial" {Movimentação de Pessoal} → [370970] Verificar a dotação
- [370961] EventoIntermediarioMensagem "Solicitação de Consulta a UniBBTS" → [370944] Consulta UniBBTS
- [370962] FimCancelamento "" {Cliente} → (fim)
- [370951] EventoIntermediarioMensagem "Aviso para abertura de Ordens de Serviço" → [370946] Término de serviço
- [370952] EventoIntermediarioMensagem "Aviso de Pendência" → [370953] Resolver pendências
- [370953] Tarefa "Resolver pendências" {Cliente} → [370971]  | [370957] Avaliar retorno sobre pendências
- [370954] SubProcesso "Consulta Férias" {Fila CSC - Serviços Gerais} → [370945] Solicitação de Consulta Controle Disciplinar
- [370955] Tarefa "Abrir chamado manualmente de Bloqueio Centralmais" {Movimentação de Pessoal} → [G83009] Cargo gerencial?
- [370956] Tarefa "Aguardar retornos dos subchamados (inserir pausa)" {Fila CSC - Movimentação Pessoal} → [370949] Avaliar retornos
- [370957] Tarefa "Avaliar retorno sobre pendências" {Responsável atual} → [G83011] Pendências resolvidas?
- [370958] EventoIntermediarioMensagem "Aviso de cancelamento" {Cliente} → [370962] 
- [370959] EventoIntermediarioMensagem "Aviso de encaminhamento" → [370965] Verificar
/cadastrar posição no sistema
- [370960] EventoIntermediarioMensagem "Aviso sobre nomeação" → [G83006] Serviço?
- [370963] EventoIntermediarioMensagem "Aviso de Pendência" → [370953] Resolver pendências
- [370964] EventoFinal "" {Responsável atual} → (fim)
- [370965] Tarefa "Verificar
/cadastrar posição no sistema" {Fila CSC - Movimentação Pessoal} → [370961] Solicitação de Consulta a UniBBTS
- [370966] EventoIntermediarioMensagem "Solicitação de Consulta de Férias" → [370954] Consulta Férias
- [370967] SubProcesso "Realizar cadastro na VOETUR" {Fila CSC - Serviços Gerais} → [370964] 
- [370968] Tarefa "Abrir chamado manualmente para alterar acessos para Gestor Centralmais" {Movimentação de Pessoal} → [370967] Realizar cadastro na VOETUR
- [370969] Tarefa "Aprova a Solicitação" {Ditac} → [G83010] Aprovado
- [370970] Tarefa "Verificar a dotação" {Fila Planejamento e Organização} → [G83012] Dotação?
- [370971] EventoIntermediarioTimer "" → [370947] Cancelado
- [G83010] Gateway "Aprovado" → «Aprovado» [370959] Aviso de encaminhamento | «Reprovado» [370958] Aviso de cancelamento
- [G83011] Gateway "Pendências resolvidas?" → «Sim» [370960] Aviso sobre nomeação | «Não - Informar as pendências para nomeação» [370963] Aviso de Pendência
- [G83012] Gateway "Dotação?" → «SIM» [370969] Aprova a Solicitação | «NÃO» [370958] Aviso de cancelamento
- [G83006] Gateway "Serviço?" → «SEM Tranferência» [370946] Término de serviço | «COM Tranferência» [370951] Aviso para abertura de Ordens de Serviço
- [G83007] Gateway "Colaborador apto a nomeação?" → «Sim» [370960] Aviso sobre nomeação | «Não - Informar as pendências para nomeação» [370952] Aviso de Pendência
- [G83009] Gateway "Cargo gerencial?" → «Sim» [370968] Abrir chamado manualmente para alterar acessos par | «Não» [370967] Realizar cadastro na VOETUR
- [G83008] Gateway "Serviço?" → «SEM Tranferência» [G83009] Cargo gerencial? | «COM Tranferência» [370955] Abrir chamado manualmente de Bloqueio Centralmais

## Gateways
### [G83010] Aprovado (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVA")
```
- alternativa → [370959] Aviso de encaminhamento: OperadorDecision=Equal; SequenciaAvaliacao=0; ReferenciaDecision=Aprovado; RotuloMotivo=teste
**ValorComparacaoDecision**
```python
True
```
- alternativa → [370958] Aviso de cancelamento: OperadorDecision=Equal; SequenciaAvaliacao=1; ReferenciaDecision=Reprovado
**ValorComparacaoDecision**
```python
False
```
### [G83011] Pendências resolvidas? (EventBasedExclusiveDecision)
Codigo=GATEWAY2
- alternativa → [370960] Aviso sobre nomeação: OperadorDecision=Equal; SequenciaAvaliacao=0; ReferenciaDecision=Sim
- alternativa → [370963] Aviso de Pendência: OperadorDecision=Equal; SequenciaAvaliacao=1; ReferenciaDecision=Não - Informar as pendências para nomeação; MotivoObrigatorio=true; PublicarRespostaAA=true
### [G83012] Dotação? (EventBasedExclusiveDecision)
- alternativa → [370969] Aprova a Solicitação: OperadorDecision=Equal; SequenciaAvaliacao=0; ReferenciaDecision=SIM
- alternativa → [370958] Aviso de cancelamento: OperadorDecision=Equal; SequenciaAvaliacao=1; ReferenciaDecision=NÃO; MotivoObrigatorio=true; PublicarRespostaAA=true
### [G83006] Serviço? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla
```
- alternativa → [370946] Término de serviço: OperadorDecision=Equal; SequenciaAvaliacao=1; ReferenciaDecision=SEM Tranferência
**ValorComparacaoDecision**
```python
"NOMEA"
```
- alternativa → [370951] Aviso para abertura de Ordens de Serviço: OperadorDecision=Equal; SequenciaAvaliacao=2; ReferenciaDecision=COM Tranferência
**ValorComparacaoDecision**
```python
"NOMEAT"
```
### [G83007] Colaborador apto a nomeação? (EventBasedExclusiveDecision)
Codigo=GATEWAY
- alternativa → [370960] Aviso sobre nomeação: OperadorDecision=Equal; SequenciaAvaliacao=0; ReferenciaDecision=Sim
- alternativa → [370952] Aviso de Pendência: OperadorDecision=Equal; SequenciaAvaliacao=1; ReferenciaDecision=Não - Informar as pendências para nomeação; MotivoObrigatorio=true
### [G83009] Cargo gerencial? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
(OrdemServico.GetCustom("FUNCAO_DAS_NOMEA") == 'Gerente de Setor')or (OrdemServico.GetCustom("FUNCAO_DAS_NOMEA") == 'Gerente de Equipe') or (OrdemServico.GetCustom("FUNCAO_DAS_NOMEA") == 'GERENTE DE DIVISAO') or (OrdemServico.GetCustom("FUNCAO_DAS_NOMEA") == 'Gerente Executivo') or (OrdemServico.GetCustom("FUNCAO_DAS_NOMEA") == 'Gerente Regional de Rede') or (OrdemServico.GetCustom("FUNCAO_DAS_NOMEA") == 'GERENTE EXECUTIVO')
```
- alternativa → [370968] Abrir chamado manualmente para alterar acessos par: OperadorDecision=Equal; SequenciaAvaliacao=0; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [370967] Realizar cadastro na VOETUR: OperadorDecision=Equal; SequenciaAvaliacao=1; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
### [G83008] Serviço? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla
```
- alternativa → [G83009] Cargo gerencial?: OperadorDecision=Equal; SequenciaAvaliacao=1; ReferenciaDecision=SEM Tranferência
**ValorComparacaoDecision**
```python
"NOMEA"
```
- alternativa → [370955] Abrir chamado manualmente de Bloqueio Centralmais: OperadorDecision=Equal; SequenciaAvaliacao=2; ReferenciaDecision=COM Tranferência
**ValorComparacaoDecision**
```python
"NOMEAT"
```

## Atividades

### [370944] SubProcesso "Consulta UniBBTS"
Responsável: 00. Cesec - Outros Serviços (papel 1039)
Config: ChamadaAssincrona=true; AssociacaoId=1382; PassaTodosItens=true; RetornaTodosItens=true; Configuracao={"ExibirBotaoNovaSubprocessos":false}
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "CSCCADLEVREALCURSOSOBR")
```
  - CustomPropertyId=1362; CustomProperty=CSC_OBS1
  - CustomPropertyId=2385; CustomProperty=SIM_NAO7
  - CustomPropertyId=4646; CustomProperty=CURSOS_OBRIGATORIOS
  - CustomPropertyId=551; CustomProperty=MATRICULA_MOVI
  - CustomPropertyId=510; CustomProperty=FAVORECIDO_TODOS
**ExpressaoValor**
```python
OrdemServico["FAVORECIDO_COBRA"]
```
- RetornoItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2223; ClasseConfiguracao=Anexo
- Associação: Ativo=true; FraseAssociacao=NOMEAÇÃO > OUTROS SERVIÇOS - COMERCIAL, GESTÃO DE PROCESSOS, JURÍDICO E SUPRIMENTOS; FraseInversaAssociacao=OUTROS SERVIÇOS - COMERCIAL, GESTÃO DE PROCESSOS, JURÍDICO E SUPRIMENTOS > NOMEAÇÃO; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=NOMEAÇÃO > OUTROS SERVIÇOS - COMERCIAL, GESTÃO DE PROCESSOS, JURÍDICO E SUPRIMENTOS; SeparadorSequencial=. | fonte: Nomeação → alvo: Outros Serviços - Comercial, Gestão de Pessoas, Jurídico e Suprimentos 

### [370945] EventoIntermediarioMensagem "Solicitação de Consulta Controle Disciplinar"
Destinatário: Responsável Demanda (papel 371)
ModeloComunicado: Solicitação de Consulta ao Controle Disciplinar
Corpo do comunicado: Prezado(a),
Para fins de nomeação em função gratificada solicitamos informar-nos se o empregado abaixo está cumprindo sanção decorrente de processo disciplinar conforme NI 116 – Regulamento Disciplinar.
Empregado: OrdemServico.Customizado.FAVORECIDO_COBRA 
Matrícula: OrdemServico.Customizado.MATRICULA_MOVI 
Atenciosamente,
Central de Serviços

### [370946] EventoIntermediarioMensagem "Término de serviço"
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de serviço
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Em atendimento à Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto, comunico que foi realizado o término da atividade pelo Cesec.
Para mais detalhes sobre esta solicitação, clique no link a seguir ==> Link.Consulta.
 Complemento1 
Atenciosamente,
Central de Serviços

### [370947] FimCancelamento "Cancelado"

### [370948] SubProcesso "Consulta Controle Disciplinar"
Responsável: Fila Controle Disciplinar (papel 605)
Config: ChamadaAssincrona=true; AssociacaoId=1379; PassaTodosItens=true; RetornaTodosItens=true; Configuracao={"ExibirBotaoNovaSubprocessos":true}
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- ValoresInputs:
  - CustomPropertyId=1137; CustomProperty=STEP_FUNCAO
  - CustomPropertyId=1135; CustomProperty=SINDICATO
  - CustomPropertyId=551; CustomProperty=MATRICULA_MOVI
  - CustomPropertyId=550; CustomProperty=FAVORECIDO_COBRA
  - CustomPropertyId=465; CustomProperty=NUM_VERSAO
  - CustomPropertyId=1136; CustomProperty=STEP_CARGO
  - CustomPropertyId=4106; CustomProperty=DATA_ATIVIDADE2
  - CustomPropertyId=1960; CustomProperty=SIM_NAO2
- Associação: Ativo=true; FraseAssociacao=NOMEAÇÃO > CONSULTA CONTROLE DISCIPLINAR; FraseInversaAssociacao=CONSULTA CONTROLE DISCIPLINAR > NOMEAÇÃO; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=NOMEAÇÃO > CONSULTA CONTROLE DISCIPLINAR; SeparadorSequencial=. | fonte: Nomeação → alvo: Consulta Controle Disciplinar

### [370949] Tarefa "Avaliar retornos"
Responsável: Responsável atual (papel 36)
**ScriptFormCarregado**
```python
Formulario["SIM_NAO2"].Visivel = True
Formulario["RESULTADO DA CONSULTA2"].Visivel = True
Formulario["DATA_ATIVIDADE2"].Visivel = False
Formulario["PERIODO01"].Visivel = False
Formulario["PERIODO02"].Visivel = False
Formulario["PERIODO03"].Visivel = False
Formulario["LABEL70"].Visivel = True
Formulario["LABEL71"].Visivel = True
Formulario["LABEL72"].Visivel = True
Formulario["CSC_OBS1"].Visivel = True
Formulario["SIM_NAO7"].Visivel = True

numeroOs = OrdemServico.Numero.ToString()


consultaCursos = DB.ExecuteDataTable(
    "SELECT * "
    "FROM ("
        "SELECT "
            "OC.NUMERO, "
            "LISTAGG("
                "G.DESCRICAO_CURSO || ' - ' || G.SITUACAO, "
                "'; '"
            ") WITHIN GROUP ("
                "ORDER BY G.DESCRICAO_CURSO"
            ") AS RESULTADO_DA_AVALIACAO, "
            "CASE "
                "WHEN SUM("
                    "CASE "
                        "WHEN UPPER(TRIM(G.SITUACAO)) <> 'REALIZADO' "
                        "THEN 1 "
                        "ELSE 0 "
                    "END"
                ") = 0 "
                "THEN 'Sim' "
                "ELSE 'Não' "
            "END AS CURSOS_REALIZADO "
        "FROM SUB_PROCESSO SP "
        "INNER JOIN CLASSE_SUB_PROCESSO CSP "
            "ON CSP.ID_CLASSE_SUB_PROCESSO = "
            "SP.ID_CLASSE_SUB_PROCESSO "
        "INNER JOIN OCORRENCIA OC "
            "ON OC.ID_SUB_PROCESSO = "
            "SP.ID_SUB_PROCESSO "
        "INNER JOIN Z_00143_CURSOS_OBRIGATORIOS G "
            "ON G.ID_OCORRENCIA = "
            "OC.ID_OCORRENCIA "
        "WHERE CSP.SIGLA = 'CSCGENERICO' "
        "AND OC.NUMERO LIKE '" +
            numeroOs +
            ".%' "
        "GROUP BY "
            "OC.NUMERO, "
            "OC.ID_OCORRENCIA "
        "ORDER BY OC.ID_OCORRENCIA DESC"
    ") "
    "WHERE ROWNUM = 1"
)

if consultaCursos.Rows.Count > 0:

    curso = consultaCursos.Rows[0]

    if curso["CURSOS_REALIZADO"] != DBNull.Value:
        Formulario["SIM_NAO7"].Valor = curso[
            "CURSOS_REALIZADO"
        ]

    if curso["RESULTADO_DA_AVALIACAO"] != DBNull.Value:
        Formulario["CSC_OBS1"].Valor = curso[
            "RESULTADO_DA_AVALIACAO"
        ]


consultaDisciplina = DB.ExecuteDataTable(
    "SELECT * "
    "FROM ("
        "SELECT "
            "OC.NUMERO, "
            "PES.DATA_ATIVIDADE2, "
            "CSC.SIM_NAO2 "
        "FROM SUB_PROCESSO SP "
        "INNER JOIN CLASSE_SUB_PROCESSO CSP "
            "ON CSP.ID_CLASSE_SUB_PROCESSO = "
            "SP.ID_CLASSE_SUB_PROCESSO "
        "INNER JOIN OCORRENCIA OC "
            "ON OC.ID_SUB_PROCESSO = "
            "SP.ID_SUB_PROCESSO "
        "LEFT JOIN CPE_CSC CSC "
            "ON CSC.ID_OCORRENCIA = "
            "OC.ID_OCORRENCIA "
        "LEFT JOIN CPE_PESSOAS PES "
            "ON PES.ID_OCORRENCIA = "
            "OC.ID_OCORRENCIA "
        "WHERE CSP.SIGLA = 'CONSULTCONTRDISCIP' "
        "AND OC.NUMERO LIKE '" +
            numeroOs +
            ".%' "
        "ORDER BY OC.ID_OCORRENCIA DESC"
    ") "
    "WHERE ROWNUM = 1"
)

if consultaDisciplina.Rows.Count > 0:

    disciplinar = consultaDisciplina.Rows[0]

    if disciplinar["SIM_NAO2"] != DBNull.Value:
        Formulario["SIM_NAO2"].Valor = disciplinar[
            "SIM_NAO2"
        ]

    if disciplinar["DATA_ATIVIDADE2"] != DBNull.Value:
        Formulario["DATA_ATIVIDADE2"].Valor = disciplinar[
            "DATA_ATIVIDADE2"
        ]


if Formulario["SIM_NAO2"].Valor == "Sim":

    Formulario["DATA_ATIVIDADE2"].Visivel = True
    Formulario["DATA_ATIVIDADE2"].Habilitado = False

else:

    Formulario["DATA_ATIVIDADE2"].Visivel = False
    Formulario["DATA_ATIVIDADE2"].Habilitado = False


consultaPeriodosFerias = DB.ExecuteDataTable(
    "SELECT * "
    "FROM ("
        "SELECT "
            "OC.NUMERO, "
            "CON.RESULTADO_DA_CONSULTA2, "
            "CON.PERIODOS, "
            "CON.PERIODO01, "
            "CON.PERIODO02, "
            "CON.PERIODO03 "
        "FROM SUB_PROCESSO SP "
        "INNER JOIN CLASSE_SUB_PROCESSO CSP "
            "ON CSP.ID_CLASSE_SUB_PROCESSO = "
            "SP.ID_CLASSE_SUB_PROCESSO "
        "INNER JOIN OCORRENCIA OC "
            "ON OC.ID_SUB_PROCESSO = "
            "SP.ID_SUB_PROCESSO "
        "LEFT JOIN CPE_CONTRATOS CON "
            "ON CON.ID_OCORRENCIA = "
            "OC.ID_OCORRENCIA "
        "WHERE CSP.SIGLA = 'CONSULTAFERIAS' "
        "AND OC.NUMERO LIKE '" +
            numeroOs +
            ".%' "
        "AND ("
            "CON.RESULTADO_DA_CONSULTA2 IS NOT NULL "
            "OR CON.PERIODOS IS NOT NULL "
            "OR CON.PERIODO01 IS NOT NULL "
            "OR CON.PERIODO02 IS NOT NULL "
            "OR CON.PERIODO03 IS NOT NULL"
        ") "
        "ORDER BY OC.ID_OCORRENCIA DESC"
    ") "
    "WHERE ROWNUM = 1"
)

periodosDeFerias = ""

if consultaPeriodosFerias.Rows.Count > 0:

    ferias = consultaPeriodosFerias.Rows[0]

    if ferias["RESULTADO_DA_CONSULTA2"] != DBNull.Value:
        Formulario["RESULTADO DA CONSULTA2"].Valor = ferias[
            "RESULTADO_DA_CONSULTA2"
        ]

    if ferias["PERIODOS"] != DBNull.Value:
        periodosDeFerias = ferias[
            "PERIODOS"
        ].ToString()

        Formulario["PERIODOS"].Valor = periodosDeFerias

    if ferias["PERIODO01"] != DBNull.Value:
        Formulario["PERIODO01"].Valor = ferias[
            "PERIODO01"
        ]

    if ferias["PERIODO02"] != DBNull.Value:
        Formulario["PERIODO02"].Valor = ferias[
            "PERIODO02"
        ]

    if ferias["PERIODO03"] != DBNull.Value:
        Formulario["PERIODO03"].Valor = ferias[
            "PERIODO03"
        ]


if (
    periodosDeFerias == "" or
    periodosDeFerias == "[Nenhum(a)]"
):

    Formulario["PERIODO01"].Visivel = False
    Formulario["PERIODO01"].Habilitado = False
    Formulario["PERIODO02"].Visivel = False
    Formulario["PERIODO02"].Habilitado = False
    Formulario["PERIODO03"].Visivel = False
    Formulario["PERIODO03"].Habilitado = False

elif (
    periodosDeFerias == "01" or
    periodosDeFerias == "1"
):

    Formulario["PERIODO01"].Visivel = True
    Formulario["PERIODO01"].Habilitado = True
    Formulario["PERIODO02"].Visivel = False
    Formulario["PERIODO02"].Habilitado = False
    Formulario["PERIODO03"].Visivel = False
    Formulario["PERIODO03"].Habilitado = False

elif (
    periodosDeFerias == "02" or
    periodosDeFerias == "2"
):

    Formulario["PERIODO01"].Visivel = True
    Formulario["PERIODO01"].Habilitado = True
    Formulario["PERIODO02"].Visivel = True
    Formulario["PERIODO02"].Habilitado = True
    Formulario["PERIODO03"].Visivel = False
    Formulario["PERIODO03"].Habilitado = False

elif (
    periodosDeFerias == "03" or
    periodosDeFerias == "3"
):

    Formulario["PERIODO01"].Visivel = True
    Formulario["PERIODO01"].Habilitado = True
    Formulario["PERIODO02"].Visivel = True
    Formulario["PERIODO02"].Habilitado = True
    Formulario["PERIODO03"].Visivel = True
    Formulario["PERIODO03"].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - LABEL71 "Resultado da Consulta ao Controle Disciplinar" [Label String → CPE_CONTRATOS.LABEL71] obrigatório
  - SIM_NAO2 "O colaborador está cumprindo sanção decorrente de processo disciplinar?" [DropDownList String → CPE_CSC.SIM_NAO2]
**SIM_NAO2.ScriptModificado**
```python
if Formulario['SIM_NAO2'].Valor == "Sim":
    Formulario['DATA_ATIVIDADE2'].Visivel = True
    Formulario['DATA_ATIVIDADE2'].Habilitado = True
    
if Formulario['SIM_NAO2'].Valor == "Não":
    Formulario['DATA_ATIVIDADE2'].Visivel = False
    Formulario['DATA_ATIVIDADE2'].Habilitado = True
```
  - DATA_ATIVIDADE2 "Fim do impedimento" [DatePicker DateTime → CPE_PESSOAS.DATA_ATIVIDADE2]
- Operação PR0001 Preencher Campos
  - LABEL70 "Resultado da Consulta à UniBBTS" [Label String(1200) → CPE_HOMOLOGACAO.LABEL70] obrigatório
  - CURSOS_OBRIGATORIOS "Cursos Obrigatorios" [DataGrid RecordList → Z_00143_CURSOS_OBRIGATORIOS.CURSOS_OBRIGATORIOS]
    - coluna DESCRICAO_CURSO obrigatório
    - coluna SITUACAO obrigatório
  - SIM_NAO7 "Cursos obrigatórios realizados?" [DropDownList String → CPE_CSC.SIM_NAO7]
  - CSC_OBS1 "Resultado da avaliação" [Memo String(2000) → CPE_CSC.CSC_OBS1]
- Operação PR0001 Preencher Campos
  - LABEL72 "Resultado da Consulta às Férias" [Label String → CPE_CONTRATOS.LABEL72] obrigatório
  - RESULTADO DA CONSULTA2 "Resultado da consulta a férias programadas" [DropDownList String → CPE_CONTRATOS.RESULTADO_DA_CONSULTA2]
  - PERIODOS "Quantos períodos de férias possui?" [DropDownList String → CPE_CONTRATOS.PERIODOS]
**PERIODOS.ScriptModificado**
```python
Formulario["PERIODOS"].Valor == "[Nenhum(a)]"

if Formulario["PERIODOS"].Valor == "[Nenhum(a)]":
   Formulario["PERIODO01"].Visivel = False
   Formulario["PERIODO01"].Habilitado = False
   Formulario["PERIODO02"].Visivel = False
   Formulario["PERIODO02"].Habilitado = False
   Formulario["PERIODO03"].Visivel = False
   Formulario["PERIODO03"].Habilitado = False

   
if Formulario["PERIODOS"].Valor == "01":
   Formulario["PERIODO01"].Visivel = True
   Formulario["PERIODO01"].Habilitado = True
   Formulario["PERIODO02"].Visivel = False
   Formulario["PERIODO02"].Habilitado = False
   Formulario["PERIODO03"].Visivel = False
   Formulario["PERIODO03"].Habilitado = False   
   
   
if Formulario["PERIODOS"].Valor == "02":
   Formulario["PERIODO01"].Visivel = True
   Formulario["PERIODO01"].Habilitado = True
   Formulario["PERIODO02"].Visivel = True
   Formulario["PERIODO02"].Habilitado = True 
   Formulario["PERIODO03"].Visivel = False
   Formulario["PERIODO03"].Habilitado = False   
   

if Formulario["PERIODOS"].Valor == "03":
   Formulario["PERIODO01"].Visivel = True
   Formulario["PERIODO01"].Habilitado = True
   Formulario["PERIODO02"].Visivel = True
   Formulario["PERIODO02"].Habilitado = True
   Formulario["PERIODO03"].Visivel = True
   Formulario["PERIODO03"].Habilitado = True
```
  - PERIODO01 "Período 01" [TextBox String → CPE_CONTRATOS.PERIODO01] — Configuracao={"Mascara":"00/00/0000 'a' 00/00/0000"}
  - PERIODO02 "Período 02" [TextBox String → CPE_CONTRATOS.PERIODO02] — Configuracao={"Mascara":"00/00/0000 'a' 00/00/0000"}
  - PERIODO03 "Período 03" [TextBox String → CPE_CONTRATOS.PERIODO03] — Configuracao={"Mascara":"00/00/0000 'a' 00/00/0000"}
- Operação PR0004 Associar Itens Configuração
  - anexo "Print da tela de confirmação Peoplesoft - Férias" classes: Arquivo

### [370950] EventoInicial "Evento inicial"
Responsável: Movimentação de Pessoal (papel 230)
Config: PermitirRascunho=true; Configuracao={"ServicoIniciador":"<Nenhum>"}
TipoSolicitacao: 18.01. Gestão de Pessoas - Ascensão e Movimentação de Pessoas
**ScriptFormCarregado**
```python
Formulario["MATRICULA_MOVI"].Visivel = False
#Formulario["DOTACAO"].Visivel = False
#Formulario["LOTACAO"].Visivel = False
#Formulario["CHAMADOS_ABERTOS"].Visivel = False
Formulario["CARGO_DOTA"].Visivel = False
Formulario["CARGO_ATUAL"].Visivel = False
Formulario["NUM_DOCU"].Visivel = False
Formulario["NUM_DOCU"].Habilitado = False
Formulario["NUM_DOCU"].Valor = None
Formulario["TIPO_NOMEACAO"].Valor = "De forma direta"
#Formulario["SALARIO_PRESTA"].Habilitado = False
Formulario["DESC_COLABORADOR"].Visivel = False
Formulario["FAVORECIDO_TODOS"].Visivel = False
Formulario["SIM_NAO"].Visivel = False
Formulario["FAVORECIDO_FUNCIO"].Visivel = False
Formulario["OPCAO_DE_CONFIRMACAO"].Visivel = True


#----- Visível
#Formulario["ENDERECO_FORNECEDOR"].Visivel = False

#----- Habilitado
#Formulario["ENDERECO_FORNECEDOR"].Habilitado = False


Formulario["COMBOBOX2"].Valor = 'Nomeação'

Formulario["RESULTADO DA CONSULTA2"].Visivel = False
Formulario["PERIODOS"].Visivel = False
Formulario["PERIODO01"].Visivel = False
Formulario["PERIODO02"].Visivel = False
Formulario["PERIODO03"].Visivel = False
Formulario["CSC_OBS1"].Visivel = False
Formulario["SIM_NAO7"].Visivel = False
Formulario["CURSOS_OBRIGATORIOS"].Visivel = False
Formulario["DATA_ATIVIDADE2"].Visivel = False
Formulario["RESULTADO DA CONSULTA"].Visivel = False
Formulario["PRINTFERIAS"].Visivel = False

Formulario["FUNCAO_DAS_NOMEA"].Itens = DB.ExecuteDataTable(" select PO.DESCR FROM xxbbtsgate.bbts_ps_jobcode_tbl po order by DESCR")
```
**ScriptValidacao**
```python
from Venki.Supravizio.Processo.Custom import Processo
#if (Convert.ToInt32(OrdemServico.GetCustom("LOTACAO")) + Convert.ToInt32(OrdemServico.GetCustom("CHAMADOS_ABERTOS")) + 1)> (Convert.ToInt32(OrdemServico.GetCustom("DOTACAO"))):
   #Criticas.AdicionaPendencia("Não há dotação para esta vaga no SCR de destino. Consulte a área responsável.")

#Verifica cargos de nomeção são de mesmo nivel de escolaridade
cargoAtual = OrdemServico.GetCustom("CARGO_ATUAL").ToString()
cargoNovo = OrdemServico.GetCustom("CARGO_DOTA").ToString()

#if (cargoAtual == 'ANALISTA ADMINISTRATIVO' or cargoAtual == 'ANALISTA DE OPERACOES') and (cargoNovo not in('ANALISTA ESPECIALISTA', 'ASSESSOR', 'GERENTE SETOR', 'GERENTE DIVISAO', 'GERENTE EXECUTIVO', 'GERENTE REGIONAL DE REDE')):
#    Criticas.AdicionaPendencia("Cargos incompatíveis para Nomeação. Consulte a GPO.")

if OrdemServico.GetCustom("TIPO_NOMEACAO") == "Por Processo Seletivo Interno" and OrdemServico.GetCustom("NUM_DOCU").ToString() == "":
    Criticas.AdicionaPendencia("Para Processo Seletivo Interno, o Número do Edital é Obrigatório!")


#if OrdemServico["DESC_COLABORADOR"] != "":
#    if OrdemServico.PossuiItem("NOMEACAO") == False:
#        Criticas.AdicionaPendencia("O arquivo 'Ato de Nomeação' é Obrigatório")
#    if OrdemServico.PossuiItem("SANCOES") == False:
#        Criticas.AdicionaPendencia("O arquivo 'Arquivo de Sanções' é Obrigatório")
#    if OrdemServico.PossuiItem("CONSUFE") == False:
#        Criticas.AdicionaPendencia("O arquivo 'Consulta ao período de férias' é Obrigatório")
#    if OrdemServico.PossuiItem("DISCIPLINAR") == False:
#        Criticas.AdicionaPendencia("O arquivo 'Controle Disciplinar' é Obrigatório")
#    if OrdemServico.PossuiItem("CURSOBRI") == False:
#        Criticas.AdicionaPendencia("O arquivo 'Cursos obrigatórios' é Obrigatório")
#    if OrdemServico.PossuiItem("RELINAB") == False:
#        Criticas.AdicionaPendencia("O arquivo 'Relação de inabilitados' é Obrigatório")
#    if OrdemServico.PossuiItem("FQ1256") == False:
#        Criticas.AdicionaPendencia("O arquivo 'FQ125-001 - Autorização de Acesso à Declaração de Ajuste Anual de IRRF' é Obrigatório")


funcao = Convert.ToInt32(OrdemServico["CODIGO_FUNCAO_GRATIFICADA"])

if (funcao > 6000 and funcao < 7000) or (funcao >= 8011 and funcao <= 8030):
    if OrdemServico.PossuiItem("COMPGRAPOS").ToString() == 'False':
        Criticas.AdicionaPendencia("A função selecionada possuí o pré-requisito de nível superior, sendo obrigatória a inclusão do diploma do referido empregado comprovando o 3º grau completo, ao chamado.")
        
        
        
        
#--- Verifica se foi marcado o campo de declaração de necessidade dos anexos envolvidos na abertura do chamado
if (OrdemServico.GetCustom("OPCAO_DE_CONFIRMACAO")  == False) :
    Criticas.AdicionaPendencia("A declaração de ciência dos anexos envolvidos na abertura do chamado é um campo obrigatório")        
if Convert.ToInt32(DateTime.Now.ToString("dd")) > 18 and OrdemServico.PossuiItem("AUTOPOSNOMEACAO") == False:
    Criticas.AdicionaPendencia("Não é permitido a abertura de Ordem de Serviço após o dia 18, exceto com autorização em anexo.")
```
- Operação PR0001 Preencher Campos
  - CARGO_ATUAL "Cargo" [TextBox String → CP_ORDEM_SERVICO.CARGO_ATUAL]
  - COMBOBOX2 "Serviço Principal" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2]
  - FAVORECIDO_COBRA "Nome" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
**FAVORECIDO_COBRA.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
###PGESV###

#Formulario["MATRICULA_MOVI"].Valor = None
Formulario["MATRICULA_MOVI"].Visivel = True
Formulario["MATRICULA_MOVI"].Habilitado = False
Formulario["CARGO_ATUAL"].Valor = None
Formulario["CARGO_ATUAL"].Habilitado = False


if Formulario["FAVORECIDO_COBRA"].Valor != "" or Formulario["FAVORECIDO_COBRA"].Valor != None:
    idFavorecido = Convert.ToInt32(Formulario["FAVORECIDO_COBRA"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecido)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    OrdemServico.SetCustom("NOME_DAS", nomeFavorecido) 
    
    #Consulta a matric do Favorecido
    
    lista = Utils.ExecuteDataTable(" SELECT SUBSTR(c.CARGO,INSTR(c.CARGO,'|')+1,LENGTH(c.CARGO)) AS CARGO1, c.FUNCAO_GRATIFICADA, c.DESC_COLABORADOR, c.MATRICULA, c.CPF FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND C.NUMERO_SUBCR_NIVEL1 = O.SIGLA AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )



    #lista = Utils.ExecuteDataTable("SELECT SUBSTR(CARGO,INSTR(CARGO,'|')+1,LENGTH(CARGO)) AS CARGO1, FUNCAO_GRATIFICADA, DESC_COLABORADOR, MATRICULA, CPF FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND LPAD(C.NUMERO_SUBCR_NIVEL1,5) = LPAD(O.SIGLA,5) AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    for linha in lista.Rows:
        Formulario["MATRICULA_MOVI"].Valor = linha["MATRICULA"].ToString()
        Formulario["CARGO_ATUAL"].Valor = linha["CARGO1"].ToString()
        Formulario["DESC_COLABORADOR"].Valor = linha["FUNCAO_GRATIFICADA"].ToString()
        #Formulario["SALARIO_DAS"].Valor = linha["VALOR"].ToString()
        Formulario["CARGO_ATUAL"].Visivel = True
```
  - MATRICULA_MOVI "Matrícula" [TextBox Integer → CP_ORDEM_SERVICO.MATRICULA_MOVI]
  - FUNCAO_DAS_NOMEA "Nova Função" [DropDownList String → CP_ORDEM_SERVICO.FUNCAO_DAS_NOMEA] obrigatório
**FUNCAO_DAS_NOMEA.ScriptModificado**
```python
###PGESV###

Formulario["CARGO_DOTA"].Valor = None
#Formulario["DOTACAO"].Visivel = False
#Formulario["LOTACAO"].Visivel = False
#Formulario["LOTACAO"].Valor = 0
#Formulario["DOTACAO"].Valor = 0
Formulario["SCR_TODOS_RH"].Valor = None

Formulario["CARGO_DOTA"].Valor = DB.ExecuteScalar("select vl1 from sv_param where ch1 = 'FUNCAO_DAS_NOMEA' and VL1 = '" + Formulario["FUNCAO_DAS_NOMEA"].Valor.ToString() + "'")

#qry = DB.ExecuteScalar("select vl2 from sv_param where ch1 = 'FUNCAO_DAS_NOMEA' and ch3 = '" + Formulario["FUNCAO_DAS_NOMEA"].Valor.ToString() + "'")

#Formulario["CODIGO_FUNCAO_GRATIFICADA"].Itens = Utils.ExecuteDataTable(qry.ToString())
#Formulario["CODIGO_FUNCAO_GRATIFICADA"].Itens = Utils.ExecuteDataTable("SELECT DISTINCT CONCAT(SUBSTR(po.GRADE,1,2),LPAD(po.STEP,2,0)) AS GRAU FROM ps_position_data po where SAL_ADMIN_PLAN ='19F' AND DESCR = '" + Formulario["FUNCAO_DAS_NOMEA"].Valor.ToString() + "'")
Formulario["CODIGO_FUNCAO_GRATIFICADA"].Itens = Utils.ExecuteDataTable("select DISTINCT jobcode AS grau FROM xxbbtsgate.bbts_ps_jobcode_tbl po WHERE descr ='" + Formulario["FUNCAO_DAS_NOMEA"].Valor.ToString() + "'")

#if Formulario["FUNCAO_DAS_NOMEA"].Valor == "Gerente de Equipe":
#    Formulario["CARGO_DOTA"].Valor = "GERENTE EQUIPE"
#    Formulario["CODIGO_FUNCAO_GRATIFICADA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT BFG.GRAU FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE BFG.DATA_INICIO <= sysdate AND BFG.DATA_FIM >= sysdate AND BFG.GRAU Between '8000' And '8999' ORDER BY 1 ")
#
#else:
#    if Formulario["FUNCAO_DAS_NOMEA"].Valor == "Gerente de Divisão":
#        Formulario["CARGO_DOTA"].Valor = "GERENTE DIVISAO"
#        Formulario["CODIGO_FUNCAO_GRATIFICADA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT BFG.GRAU FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE BFG.DATA_INICIO <= sysdate AND BFG.DATA_FIM >= sysdate AND BFG.GRAU Between '8000' And '8999' ORDER BY 1 ")        
#    else:
#        if Formulario["FUNCAO_DAS_NOMEA"].Valor == "Gerente Executivo":
#            Formulario["CARGO_DOTA"].Valor = "GERENTE EXECUTIVO"
#            Formulario["CODIGO_FUNCAO_GRATIFICADA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT BFG.GRAU FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE BFG.DATA_INICIO <= sysdate AND BFG.DATA_FIM >= sysdate AND BFG.GRAU Between '8000' And '8999' ORDER BY 1 ")
#        else:
#            if Formulario["FUNCAO_DAS_NOMEA"].Valor == "Assessor":
#                Formulario["CARGO_DOTA"].Valor = "ASSESSOR"
#                Formulario["CODIGO_FUNCAO_GRATIFICADA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT BFG.GRAU FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE BFG.DATA_INICIO <= sysdate AND BFG.DATA_FIM >= sysdate AND BFG.GRAU Between '7000' And '7999' ORDER BY 1 ")    
#            else:
#                if Formulario["FUNCAO_DAS_NOMEA"].Valor == "Diretor":
#                    Formulario["CARGO_DOTA"].Valor = "DIRETOR"
#                    Formulario["CODIGO_FUNCAO_GRATIFICADA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT BFG.GRAU FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE BFG.DATA_INICIO <= sysdate AND BFG.DATA_FIM >= sysdate AND BFG.GRAU ='DIRETORIA' ORDER BY 1 ")
#                else:
#                    if Formulario["FUNCAO_DAS_NOMEA"].Valor == "Presidente":
#                        Formulario["CARGO_DOTA"].Valor = "PRESIDENTE"
#                        Formulario["CODIGO_FUNCAO_GRATIFICADA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT BFG.GRAU FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE BFG.DATA_INICIO <= sysdate AND BFG.DATA_FIM >= sysdate AND BFG.GRAU ='PRESIDENTE' ORDER BY 1 ")
#                    else:
#                        if Formulario["FUNCAO_DAS_NOMEA"].Valor == "Supervisor":
#                            Formulario["CARGO_DOTA"].Valor = "SUPERVISOR"
#                            Formulario["CODIGO_FUNCAO_GRATIFICADA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT BFG.GRAU FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE BFG.DATA_INICIO <= sysdate AND BFG.DATA_FIM >= sysdate AND BFG.GRAU Between '4000' And '4999' ORDER BY 1 ")
#                        else:
#                            if Formulario["FUNCAO_DAS_NOMEA"].Valor == "Técnico Especialista":
#                                Formulario["CARGO_DOTA"].Valor = "TECNICO ESPECIALISTA"
#                                Formulario["CODIGO_FUNCAO_GRATIFICADA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT BFG.GRAU FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE BFG.DATA_INICIO <= sysdate AND BFG.DATA_FIM >= sysdate AND BFG.GRAU Between '5000' And '5999' ORDER BY 1 ")
#                            else:
#                                if Formulario["FUNCAO_DAS_NOMEA"].Valor == "Analista Especialista":
#                                    Formulario["CARGO_DOTA"].Valor = "ANALISTA ESPECIALISTA"
#                                    Formulario["CODIGO_FUNCAO_GRATIFICADA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT BFG.GRAU FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE BFG.DATA_INICIO <= sysdate AND BFG.DATA_FIM >= sysdate AND BFG.GRAU Between '6000' And '6999' ORDER BY 1 ")
#                                else:
#                                    if Formulario["FUNCAO_DAS_NOMEA"].Valor == "Gerente de Setor":
#                                        Formulario["CARGO_DOTA"].Valor = "GERENTE SETOR"
#                                        Formulario["CODIGO_FUNCAO_GRATIFICADA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT BFG.GRAU FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE BFG.DATA_INICIO <= sysdate AND BFG.DATA_FIM >= sysdate AND BFG.GRAU Between '8000' And '8999' ORDER BY 1 ")
#                                    else:
#                                        if Formulario["FUNCAO_DAS_NOMEA"].Valor == "Gerente Regional de Rede":
#                                            Formulario["CARGO_DOTA"].Valor = "GERENTE REGIONAL DE REDE"
#                                            Formulario["CODIGO_FUNCAO_GRATIFICADA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT BFG.GRAU FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE BFG.DATA_INICIO <= sysdate AND BFG.DATA_FIM >= sysdate AND BFG.GRAU Between '8000' And '8999' ORDER BY 1 ")
#                                        else:
#                                            Formulario["CARGO_DOTA"].Valor = None
#                                            Formulario["CODIGO_FUNCAO_GRATIFICADA"].Itens = Utils.ExecuteDataTable(" SELECT DISTINCT BFG.GRAU FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE BFG.DATA_INICIO <= sysdate AND BFG.DATA_FIM >= sysdate ORDER BY 1 ")
#
```
  - CODIGO_FUNCAO_GRATIFICADA "CODIGOS DAS FUNÇÕES GRATIFICADAS" [DropDownList String → CP_ORDEM_SERVICO.CODIGO_FUNCAO_GRATIFICADA] obrigatório
**CODIGO_FUNCAO_GRATIFICADA.ScriptModificado**
```python
Formulario["DATA_ADMISSAO"].Valor = None
#Formulario["SALARIO_PRESTA"].Valor = None
```
  - SCR_TODOS_RH "UOR Movimentação" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH] obrigatório
**SCR_TODOS_RH.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#Formulario["DOTACAO"].Visivel = False
#Formulario["LOTACAO"].Visivel = False
#Formulario["CHAMADOS_ABERTOS"].Visivel = False

Formulario["CARGO_DOTA"].Visivel = False

#Formulario["LOTACAO"].Valor = 0
#Formulario["DOTACAO"].Valor = 0
#Formulario["CHAMADOS_ABERTOS"].Valor = 0
#
#
#lotacao = 0
#dotacao = 0
#abertos = 0
#numeroOS = 0
scr = ""
idgestor = ""
nomegestor = ""


if Formulario["SCR_TODOS_RH"].Valor != None and Formulario["SCR_TODOS_RH"].Valor != "":

    #Consulta a dotação e a lotação
    scr = Formulario["SCR_TODOS_RH"].Valor
    if (scr.ToString() != ""):
#
#        cargosIn = "'" +Formulario["CARGO_DOTA"].Valor + "'"
#
#        # sub-processos a serem considerados
#        siglasIn = "'CONTRACON', 'CONTRADAS', 'NOMEACAO', 'TRANSCOBRA'"
#
#        # Conforme contato telefonico com Roberta em 08/07/2014 as 9:08, não pode haver exceção
#        cargo = Formulario["CARGO_DOTA"].Valor
#
#        qry = " SELECT DISTINCT LOTACAO_AREA, DOTACAO_AREA, CARGO FROM COBRA_HIERARQUIA_SV DOTA where '"
#        qry += scr.ToString()
#        qry += "' = DOTA.SCR AND upper(DOTA.CARGO) = upper('"
#        qry += cargo.ToString()
#        qry += "') "
#        
#        lista = Utils.ExecuteDataTable(qry)
#
#        lotacao = 0
#        dotacao = 0
#
#        for linha in lista.Rows:
#           if linha["LOTACAO_AREA"]:
#              lotacao = Convert.ToInt32(linha["LOTACAO_AREA"])
#           if linha["DOTACAO_AREA"]:
#              dotacao = Convert.ToInt32(linha["DOTACAO_AREA"])
#
#        Formulario["LOTACAO"].Valor = lotacao
#        Formulario["DOTACAO"].Valor = dotacao
#        Formulario["DOTACAO"].Visivel = True
#        Formulario["LOTACAO"].Visivel = True
#
#
#        #Inicio OS = 101342 - Calcula OSs abertas
#        if not String.IsNullOrEmpty(OrdemServico.Numero):
#           numeroOS = Convert.ToInt32(OrdemServico.Numero)
#
#        qry = " SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O INNER JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) "
#        qry += "INNER JOIN CLASSE_SUB_PROCESSO CS ON (O.ID_CLASSE_SUB_PROC = CS.ID_CLASSE_SUB_PROCESSO) "
#        qry += "INNER JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) WHERE '"
#        qry += scr.ToString()
#        qry += "' = CPOS.SCR_TODOS_RH AND O.NUMERO <> '"
#        qry += numeroOS.ToString()
#        qry += "' AND O.SITUACAO = 'Aberto' AND upper(CARGO_DOTA) = upper('"
#        qry += cargo.ToString()
#        qry += "') AND CS.SIGLA IN( "
#        qry += siglasIn.ToString()
#        qry += ") "
#
#        lista = Utils.ExecuteDataTable(qry)
#
#        for linha in lista.Rows:
#           if linha["CONTADOR"]:
#              abertos = Convert.ToInt32(linha["CONTADOR"])
#
#        Formulario["CHAMADOS_ABERTOS"].Valor = abertos
#        Formulario["CHAMADOS_ABERTOS"].Visivel = True
#
#      #Fim OS = 101342 - Calcula OSs abertas
#      
        lista = Utils.ExecuteDataTable(" SELECT DISTINCT ID_GESTOR FROM ORGAO where SIGLA = '"+scr.ToString()+"' AND ATIVO = 'Sim' ")

        for linha in lista.Rows:
            idgestor = Convert.ToInt32(linha["ID_GESTOR"])

        if (idgestor != ""):
            pessoa = Pessoa.Carrega(idgestor)
            nomegestor = pessoa.Nome
            Formulario["FAVORECIDO_TODOS"].Valor = idgestor
            Formulario["FAVORECIDO_TODOS"].Habilitado = False
            Formulario["FAVORECIDO_TODOS"].Visivel = True
```
  - FAVORECIDO_TODOS "Reporta-se a posição" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
  - RESPONSA "Responsável por dependência?" [DropDownList String → CP_ORDEM_SERVICO.RESPONSA]
  - DATA_ADMISSAO "Data de Nomeação" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ADMISSAO] obrigatório
**DATA_ADMISSAO.ScriptModificado**
```python
#dataNome = Formulario["DATA_ADMISSAO"].Valor
#lista=Utils.ExecuteDataTable(" SELECT VALOR FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE TO_CHAR(BFG.DATA_INICIO) <= TO_CHAR('"+ dataNome.ToString() +"') AND TO_CHAR(BFG.DATA_FIM) >= TO_CHAR('"+ dataNome.ToString() +"') AND BFG.GRAU = '" + Formulario["CODIGO_FUNCAO_GRATIFICADA"].Valor + "' ORDER BY 1 ")
#numeroRegistro = None
#for linha in lista.Rows:
#    numeroRegistro = linha["VALOR"]
#if numeroRegistro == None:
#    Formulario["SALARIO_PRESTA"].Valor = numeroRegistro
#else:
#    lista=Utils.ExecuteDataTable(" SELECT VALOR valor FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE BFG.GRAU = '" + Formulario["CODIGO_FUNCAO_GRATIFICADA"].Valor + "' AND ROWNUM = 1 ORDER BY BFG.DATA_FIM desc ")
#    for linha in lista.Rows:
#        numeroRegistro = linha["VALOR"]
#if numeroRegistro != None:
#    Formulario["SALARIO_PRESTA"].Valor = numeroRegistro
#
dataNome = Formulario["DATA_ADMISSAO"].Valor
#lista=Utils.ExecuteDataTable(" SELECT VALOR FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE TO_CHAR(BFG.DATA_INICIO) <= TO_CHAR('"+ dataNome.ToString() +"') AND TO_CHAR(BFG.DATA_FIM) >= TO_CHAR('"+ dataNome.ToString() +"') AND BFG.GRAU = '" + Formulario["CODIGO_FUNCAO_GRATIFICADA"].Valor + "' ORDER BY 1 ")

#lista=Utils.ExecuteDataTable(" SELECT VALOR FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE '" + dataNome.ToString() + "' BETWEEN TO_CHAR(BFG.DATA_INICIO) AND TO_CHAR(BFG.DATA_FIM) AND BFG.GRAU = '" + Formulario["CODIGO_FUNCAO_GRATIFICADA"].Valor + "' ORDER BY 1 ")

lista=Utils.ExecuteDataTable(" SELECT VALOR FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE to_date('" + dataNome.ToString() + "', 'dd/mm/yyyy hh24:mi:ss') BETWEEN BFG.DATA_INICIO AND BFG.DATA_FIM AND BFG.GRAU = '" + Formulario["CODIGO_FUNCAO_GRATIFICADA"].Valor + "' ORDER BY 1 ")

numeroRegistro = None
for linha in lista.Rows:
    numeroRegistro = linha["VALOR"]
if numeroRegistro == None :
    #lista=Utils.ExecuteDataTable(" SELECT VALOR FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE BFG.GRAU = '" + Formulario["CODIGO_FUNCAO_GRATIFICADA"].Valor + "' AND ROWNUM = 1 ORDER BY BFG.DATA_FIM desc ")
    lista=Utils.ExecuteDataTable(" SELECT max(VALOR) VALOR FROM BBTS_FUNCAO_GRATIFICADA BFG WHERE BFG.GRAU = '" + Formulario["CODIGO_FUNCAO_GRATIFICADA"].Valor + "'")
    for linha in lista.Rows:
        numeroRegistro = linha["VALOR"]
if numeroRegistro != None :
    Formulario["SALARIO_PRESTA"].Valor = numeroRegistro
```
  - CARGO_DOTA "Cargo" [TextBox String → CP_ORDEM_SERVICO.CARGO_DOTA]
  - TIPO_NOMEACAO "Tipo de Nomeação" [DropDownList String → CP_ORDEM_SERVICO.TIPO_NOMEACAO] obrigatório
**TIPO_NOMEACAO.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Processo
Formulario["NUM_DOCU"].Valor = None

if Formulario["TIPO_NOMEACAO"].Valor == "Por Processo Seletivo Interno":
    Formulario["NUM_DOCU"].Visivel = True
    Formulario["NUM_DOCU"].Habilitado = True
else:
    Formulario["NUM_DOCU"].Visivel = False
    Formulario["NUM_DOCU"].Habilitado = False

if Formulario["TIPO_NOMEACAO"].Valor == "Por Interinidade":
    Formulario["SIM_NAO"].Visivel = True
    Formulario["SIM_NAO"].Habilitado = True
else:
    Formulario["SIM_NAO"].Visivel = False
    Formulario["SIM_NAO"].Habilitado = False
```
  - SIM_NAO "É por afastamento previdenciário?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
if Formulario["SIM_NAO"].Valor == "Sim":
    Formulario["FAVORECIDO_FUNCIO"].Visivel = True
    Formulario["FAVORECIDO_FUNCIO"].Habilitado = True
else:
    Formulario["FAVORECIDO_FUNCIO"].Visivel = False
    Formulario["FAVORECIDO_FUNCIO"].Habilitado = False
```
  - FAVORECIDO_FUNCIO "Informe quem é o substituído" [SearchList String → CP_ORDEM_SERVICO.FAVORECIDO_FUNCIO] obrigatório
  - NUM_DOCU "Nr.Edital Proc.Sel.Interno" [TextBox String → CP_ORDEM_SERVICO.NUM_DOCU]
  - LOCAL DE ATUACAO "Local de atuação" [DropDownList String → CPE_HOMOLOGACAO.LOCAL_DE_ATUACAO] obrigatório
  - SINDICATO "Código do sindicato" [DropDownList String → CP_ORDEM_SERVICO.SINDICATO] obrigatório
  - DESC_COLABORADOR "Tipo de Colaborador" [DropDownList String → CP_ORDEM_SERVICO.DESC_COLABORADOR]
  - CSC_OBS "Descrição detalhada" [Memo String(2000) → CPE_CSC.CSC_OBS] obrigatório
  - SALARIO_PRESTA "Salário do Prestador de Serviço" [TextBox String → CP_ORDEM_SERVICO.SALARIO_PRESTA]
  - FAVORECIDO_COBRA1 "Novo gestor do favorecido após nomeação:" [DropDownList String → CPE_CONTRATOS.FAVORECIDO_COBRA1] obrigatório
**FAVORECIDO_COBRA1.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
###PGESV###

#Formulario["MATRICULA_MOVI"].Valor = None
Formulario["MATRICULA"].Visivel = True
Formulario["MATRICULA"].Habilitado = False
Formulario["CARGO_ATUAL"].Valor = None
Formulario["CARGO_ATUAL"].Habilitado = False


if Formulario["FAVORECIDO_COBRA1"].Valor != "" or Formulario["FAVORECIDO_COBRA1"].Valor != None:
    idFavorecido = Convert.ToInt32(Formulario["FAVORECIDO_COBRA1"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecido)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    OrdemServico.SetCustom("NOME_DAS", nomeFavorecido) 
    
    #Consulta a matric do Favorecido
    
    lista = Utils.ExecuteDataTable(" SELECT SUBSTR(c.CARGO,INSTR(c.CARGO,'|')+1,LENGTH(c.CARGO)) AS CARGO1, c.FUNCAO_GRATIFICADA, c.DESC_COLABORADOR, c.MATRICULA, c.CPF FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND C.NUMERO_SUBCR_NIVEL1 = O.SIGLA AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )



    #lista = Utils.ExecuteDataTable("SELECT SUBSTR(CARGO,INSTR(CARGO,'|')+1,LENGTH(CARGO)) AS CARGO1, FUNCAO_GRATIFICADA, DESC_COLABORADOR, MATRICULA, CPF FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND LPAD(C.NUMERO_SUBCR_NIVEL1,5) = LPAD(O.SIGLA,5) AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    for linha in lista.Rows:
        Formulario["MATRICULA"].Valor = linha["MATRICULA"].ToString()
        Formulario["CARGO_ATUAL"].Valor = linha["CARGO1"].ToString()
        Formulario["DESC_COLABORADOR"].Valor = linha["FUNCAO_GRATIFICADA"].ToString()
        #Formulario["SALARIO_DAS"].Valor = linha["VALOR"].ToString()
        Formulario["CARGO_ATUAL"].Visivel = True
```
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA]
  - GRID_PESSOAS "Escolher funcionários subordinados (se houver):" [DataGrid RecordList → Z_00143_GRID_PESSOAS.GRID_PESSOAS]
    - coluna PESSOAS obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Documentos obrigatórios" classes: Ato de Nomeação — ProduzidoTermino=true
  - anexo "" classes: FQ125-002 - Form de Aut de Acesso aos Dados das Decl de Ajuste Anual do IRPF — ProduzidoTermino=true
  - anexo "" classes: Relação de inabilitados — ProduzidoTermino=true
  - anexo "" classes: Comprovação de Graduação ou Pós Graduação — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: FQ125-001 - Aut de Acesso à Declaração de Ajuste Anual de IRPF — ProduzidoTermino=true
  - anexo "" classes: FQ140-003 - Declaração de Condutam Parentesco e Autorização — ProduzidoTermino=true
- Operação PR0001 Preencher Campos
  - RESULTADO DA CONSULTA2 "Resultado da consulta a férias programadas" [DropDownList String → CPE_CONTRATOS.RESULTADO_DA_CONSULTA2] obrigatório
  - PERIODOS "Quantos períodos de férias possui?" [DropDownList String → CPE_CONTRATOS.PERIODOS]
**PERIODOS.ScriptModificado**
```python
Formulario["PERIODOS"].Valor == "[Nenhum(a)]"

if Formulario["PERIODOS"].Valor == "[Nenhum(a)]":
   Formulario["PERIODO01"].Visivel = False
   Formulario["PERIODO01"].Habilitado = False
   Formulario["PERIODO02"].Visivel = False
   Formulario["PERIODO02"].Habilitado = False
   Formulario["PERIODO03"].Visivel = False
   Formulario["PERIODO03"].Habilitado = False

   
if Formulario["PERIODOS"].Valor == "01":
   Formulario["PERIODO01"].Visivel = True
   Formulario["PERIODO01"].Habilitado = True
   Formulario["PERIODO02"].Visivel = False
   Formulario["PERIODO02"].Habilitado = False
   Formulario["PERIODO03"].Visivel = False
   Formulario["PERIODO03"].Habilitado = False   
   
   
if Formulario["PERIODOS"].Valor == "02":
   Formulario["PERIODO01"].Visivel = True
   Formulario["PERIODO01"].Habilitado = True
   Formulario["PERIODO02"].Visivel = True
   Formulario["PERIODO02"].Habilitado = True 
   Formulario["PERIODO03"].Visivel = False
   Formulario["PERIODO03"].Habilitado = False   
   

if Formulario["PERIODOS"].Valor == "03":
   Formulario["PERIODO01"].Visivel = True
   Formulario["PERIODO01"].Habilitado = True
   Formulario["PERIODO02"].Visivel = True
   Formulario["PERIODO02"].Habilitado = True
   Formulario["PERIODO03"].Visivel = True
   Formulario["PERIODO03"].Habilitado = True
```
  - PERIODO01 "Período 01" [TextBox String → CPE_CONTRATOS.PERIODO01] — Configuracao={"Mascara":"00/00/0000 'a' 00/00/0000"}
  - PERIODO02 "Período 02" [TextBox String → CPE_CONTRATOS.PERIODO02] — Configuracao={"Mascara":"00/00/0000 'a' 00/00/0000"}
  - PERIODO03 "Período 03" [TextBox String → CPE_CONTRATOS.PERIODO03] — Configuracao={"Mascara":"00/00/0000 'a' 00/00/0000"}
- Operação PR0004 Associar Itens Configuração
  - anexo "Documentos Adicionais" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Autorização de exceções para abertura de chamado após o dia 18" classes: Autorização para Nomeação após o dia 18 — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=PRINTFERIAS
  - anexo "Print da tela de confirmação Peoplesoft - Férias" classes: Arquivo
- Operação PR0001 Preencher Campos
  - RESULTADO DA CONSULTA "O colaborador está cumprindo sanção decorrente de processo disciplinar?" [DropDownList String → CPE_CONTRATOS.RESULTADO_DA_CONSULTA] obrigatório
  - DATA_ATIVIDADE2 "Fim do impedimento" [DatePicker DateTime → CPE_PESSOAS.DATA_ATIVIDADE2] obrigatório
- Operação PR0001 Preencher Campos
  - CURSOS_OBRIGATORIOS "Cursos Obrigatorios" [DataGrid RecordList → Z_00143_CURSOS_OBRIGATORIOS.CURSOS_OBRIGATORIOS] obrigatório
    - coluna DESCRICAO_CURSO obrigatório
    - coluna SITUACAO obrigatório
  - SIM_NAO7 "Cursos obrigatórios realizados?" [DropDownList String → CPE_CSC.SIM_NAO7] obrigatório
  - CSC_OBS1 "Resultado da avaliação" [Memo String(2000) → CPE_CSC.CSC_OBS1] obrigatório
- Operação PR0001 Preencher Campos
  - OPCAO_DE_CONFIRMACA1 "Os chamados de nomeação poderão ser abertos e aprovados entre os dias 1º e 18 do mês vigente. Chamados abertos e aprovados após o dia 18 serão automaticamente transferidos para o primeiro dia útil do mês seguinte, sendo necessário, nesses casos, um novo ato de nomeação (FQ142-001) com a data atualizada." [CheckBox Boolean → CPE_PESSOAS.OPCAO_DE_CONFIRMACA1] obrigatório
**OPCAO_DE_CONFIRMACA1.ScriptModificado**
```python
if Formulario["OPCAO_DE_CONFIRMACA1"].Valor == "" or Formulario["OPCAO_DE_CONFIRMACA1"].Valor == "none":
   Formulario.ExibeMensagem = "É obrigatória a marcação da opção."
```
  - LABEL_500 "<b style="color:black">Para acessar a NI142 NOMEAÇÃO <a href="https://bbts.docnix.com.br/bbts/corporate/index.html#/login?login=&senha=&empresa=1&state=permiLinkDocumento&id=573"target="_blank">clique aqui</a></b>" [Label String(500) → CPE_BOOTCAMP.LABEL_500] obrigatório
  - LABEL100 "<b style="color:black">Para gerar a Certidão de Inabilitados do TCU <a href="https://contas.tcu.gov.br/ords/f?p=1660:3:3638144440469::::P3_TIPO_RELACAO:INABILITADO"target="_blank">clique aqui</a></b>" [Label String(1000) → CPE_CONTRATOS.LABEL100] obrigatório
  - OPCAO_DE_CONFIRMACAO "Confirmo que todos os documentos necessários a nomeação estão devidamente anexados a este chamado." [CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO] obrigatório

### [370961] EventoIntermediarioMensagem "Solicitação de Consulta a UniBBTS"
Config: ListaDestinatarios=UniBBTS@bbtecno.com.br
ModeloComunicado: Aviso de abertura de chamado
Corpo do comunicado: Prezado(a),
Foi aberta a ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [370962] FimCancelamento ""
Responsável: Cliente (papel 18)

### [370951] EventoIntermediarioMensagem "Aviso para abertura de Ordens de Serviço"
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de serviço 5
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Informamos que após a conclusão da Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto, será necessário a abertura de Ordens de Serviço para os serviços de Adaptação, Auxílio mudança e Hospedagem informando os prazos estabelecidos na NI.
Para mais detalhes sobre esta solicitação, clique no link a seguir ==> Link.Consulta.
Atenciosamente,
Central de Serviços

### [370952] EventoIntermediarioMensagem "Aviso de Pendência"
Destinatário: Cliente (papel 18)
ModeloComunicado: Aviso de Pendência 4
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Informamos que o seu chamado OrdemServico.Numero, continua com pendência(s) conforme informado abaixo.
A(s) pendência(s) é(são) a(s) informada(s) abaixo:
Complemento1 
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoGateway("GATEWAY")
```

### [370953] Tarefa "Resolver pendências"
Responsável: Cliente (papel 18)
- Operação PR0001 Preencher Campos
  - OBS1 "Responder abaixo sobre as pendências indicadas" [Memo String(2000) → CPE_CONTRATOS.OBS1] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Documentação solicitada para resolução de pendência" classes: Documentos — RequeridoInicial=true

### [370954] SubProcesso "Consulta Férias"
Responsável: Fila CSC - Serviços Gerais (papel 483)
Config: ChamadaAssincrona=true; AssociacaoId=1381; PassaTodosItens=true; RetornaTodosItens=true; Configuracao={"ExibirBotaoNovaSubprocessos":true}
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- ValoresInputs:
  - CustomPropertyId=4274; CustomProperty=PERIODO01
  - CustomPropertyId=4275; CustomProperty=PERIODO02
  - CustomPropertyId=4276; CustomProperty=PERIODO03
  - CustomPropertyId=4273; CustomProperty=PERIODOS
  - CustomPropertyId=4269; CustomProperty=RESULTADO DA CONSULTA2
  - CustomPropertyId=550; CustomProperty=FAVORECIDO_COBRA
  - CustomPropertyId=465; CustomProperty=NUM_VERSAO
  - CustomPropertyId=1136; CustomProperty=STEP_CARGO
  - CustomPropertyId=1137; CustomProperty=STEP_FUNCAO
  - CustomPropertyId=1135; CustomProperty=SINDICATO
  - CustomPropertyId=551; CustomProperty=MATRICULA_MOVI
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "CONSULFERIAS")
```
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=1655; ClasseConfiguracao=Arquivo
- RetornoItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=1655; ClasseConfiguracao=Arquivo
- Associação: Ativo=true; FraseAssociacao=NOMEAÇÃO > CONSULTA DE FÉRIAS; FraseInversaAssociacao=CONSULTA DE FÉRIAS > NOMEAÇÃO; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=NOMEAÇÃO > CONSULTA DE FÉRIAS; SeparadorSequencial=. | fonte: Nomeação → alvo: Consulta de Férias

### [370955] Tarefa "Abrir chamado manualmente de Bloqueio Centralmais"
Responsável: Movimentação de Pessoal (papel 230)
Config: ChamadaAssincrona=true; AssociacaoId=113
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Atividade
from Venki.Services.Custom import Message
from Venki.Services.Security.Custom import User
import sysAid
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.
#
#
#import System
#from System.IO import *
#from System.Text  import *
#from System.Text.RegularExpressions import *
#clr.AddReference("Newtonsoft.Json")
#clr.AddReference("System.Net.Http")
#from Newtonsoft.Json import *
#from Newtonsoft.Json.Linq import *
#from System.Net.Http import *
#from System.Net.Http.Headers import *
#
#titulo="Bloqueio de usuário"
#categoria = "Controle de Acesso e Privilégios_Bloqueio de Usuário_Nomeação"
#descricao = OrdemServico.Assunto+" - Chamado Supravizio= "+ OrdemServico.Numero.ToString()
#solicitante = OrdemServico.Cliente["MATRICULA"].ToString()
#usuarioAtendido = OrdemServico.GetCustom('MATRICULA_MOVI').ToString()
#pessoa = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))
#nomeColaborador = pessoa.Nome.ToString()
#matricula = OrdemServico.GetCustom('MATRICULA_MOVI').ToString()
#dataRecisao = OrdemServico.GetCustom('DATA_ADMISSAO').ToString()
##empresa = OrdemServico.GetCustom('CSC_EMPRESA').ToString()
#localidade = DB.ExecuteScalar("SELECT DISTINCT E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE) and E.ESTABID='"+OrdemServico.GetCustom('UNIDADE_NEGOCIO').ToString()+"'")
##uor = DB.ExecuteScalar(" SELECT DISTINCT NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO where nome <> SCR ||' - ' and SCR = '"+OrdemServico.GetCustom('CSC_UOR_LISTA').ToString()+"'")
##dtIncio = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_INICIO').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01')+1 )* 60 * 60 * 24 * 1000 from dual")
##dtFim = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('DATA_ADMISSAO').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01') +1)* 60 * 60 * 24 * 1000 from dual")
#
#emailUsuAtendido = DB.ExecuteScalar("select distinct ID from ta_10 where tipo = 0 and ATIVO ='S' and matricula = '"+usuarioAtendido+"'")+"@bbts.com.br"
#
##
###API Autentica no Sysid
##scriptLogin= "$Username = '***MASCARADO***' \n $Password = '***MASCARADO***' \n $SysAidURL = 'https://centraldeti.bbts.com.br' "
##scriptLogin2= '\nFunction Get-SysAidToken {\n    Param(\n    [parameter(Mandatory=$true)]\n    [String]$Username,\n    [Parameter(Mandatory=$true)]\n    [String]$Password,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "$SysAidURL/api/v1/login"\n$ContentType = "application/json"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n    "user_name": "$Username",\n    "password": "$Password"\n}\n"@\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        = $Body\n}\nTry {\n$WebRequest = Invoke-WebRequest @props -ErrorAction Stop\n$StatusCode = $WebRequest.StatusCode\n}\nCatch {\n$StatusCode = $_.Exception.Response.StatusCode.value__\n}\nif ($StatusCode -eq "200") {\nWrite-Verbose "The Web Request Was Successful, Capturing JSESSIONID Cookie..." -Verbose\n$cookies = $WebSession.Cookies.GetCookies($Uri)\nreturn $cookies\nWrite-Verbose "$cookies" -Verbose\n}\nelseif ($StatusCode -eq "401") {\nWrite-Verbose "The Web Request Failed, with status code $StatusCode. Please enter the correct login information." -Verbose\n}\nelseif ($StatusCode -ne "200" -or "401") {\nWrite-Verbose "The Web Request Failed, with status code $StatusCode. Please verify the entered parameters." -Verbose\n}\nreturn $cookies\n} '
##scriptLogin3=scriptLogin + scriptLogin2 + "$JSESSIONID = Get-SysAidToken -Username $Username -Password $Password -SysAidURL $SysAidURL \n $JSESSIONID.Value"
##
###cookie = PowerShell.PSExecuteCmdlet(scriptLogin3)
##
##
###API para consultar o ID do usuário no Sysid
##scriptConsUsu='\nFunction consulta_usuario {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n  [Parameter(Mandatory=$true)]\n    [string]$Email\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/users/search?query=$Email&fields=first_name"\n$ContentType = "application/json"\n$Method = '+"'GET'"+'\n\n$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n}\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props\n}\n$retornoUsu = consulta_usuario -JSESSIONID $JSESSIONID.Value -Email '+OrdemServico.Cliente.Email+'\n$retornoUsuAtend = consulta_usuario -JSESSIONID $JSESSIONID.Value -Email '+emailUsuAtendido
##
###API para abrir chamado de alteração de permissão no Sysid
##scriptCU='\nFunction Amend-SysAidTicketsCategories {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuSolicitante,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuAtendido,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=147"\n$ContentType = "application/json; charset=UTF-8"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n           {"key":"title", "value":"'+titulo.encode('UTF-8')+'"},\n           {"key":"problem_type", "value":"'+categoria.encode('UTF-8')+'"},\n           {"key":"description", "value":"'+descricao.encode('UTF-8')+'"},\n           {"key":"status", "value":"1"},\n           {"key":"request_user", "value":"$UsuSolicitante"},\n           {"key":"followup_user", "value":"$UsuAtendido"},\n           {"key":"CustomColumn8sr", "value":"00000"},\n           {"key":"CustomColumn9sr", "value":"'+localidade.encode('UTF-8')+'"},\n           {"key":"assigned_group", "value":"4807"}\n           ]\n}\n"@\n '
##scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
##scriptCU3 = '$retorno = Amend-SysAidTicketsCategories -JSESSIONID $JSESSIONID.Value -SysAidURL $SysAidURL -UsuSolicitante $retornoUsu.id -UsuAtendido $retornoUsuAtend.id\n $retorno.id'
##script = scriptLogin3 + scriptConsUsu + scriptCU + scriptCU2 + scriptCU3
###OrdemServico.DescricaoDetalhada = script
##resposta = PowerShell.PSExecuteCmdlet(script)
#
#idSolic = consultaUsuario(OrdemServico.Cliente.Email)
#idAtend = consultaUsuario(emailUsuAtendido)
#if idAtend == None:
#    OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+emailUsuAtendido.ToString()
#elif idSolic == None:
#    OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+OrdemServico.Cliente.Email.ToString()
#
#else:
#    resposta = bloqueio23067(categoria, titulo, descricao, localidade, idSolic, idAtend, dataRecisao)
#
#    if String.IsNullOrEmpty(resposta.ToString()):
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada + "\n Atividade automática de abertura de chamado para bloqueio de usuário não realizada "
#    else:
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada +"\n Chamado para bloqueio de usuário: "+resposta.ToString()
#        AvancaProximaAtividade = True
```
- ValoresInputs:
  - CustomPropertyId=52; CustomProperty=DATA_INICIO
**ExpressaoValor**
```python
OrdemServico["DATA_ADMISSAO"]
```
  - PropertyId=1296; Property=Favorecido
**ExpressaoValor**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))
```
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega(129)
```
- Associação: Ativo=true; FraseAssociacao=Nomeação -> Privilégio de acesso; FraseInversaAssociacao=Privilégio de acesso -> Nomeação; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=NOMEAPRIVI | fonte: Nomeação → alvo: Privilégios de acesso - Bloqueio

### [370956] Tarefa "Aguardar retornos dos subchamados (inserir pausa)"
Responsável: Fila CSC - Movimentação Pessoal (papel 510)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno

### [370957] Tarefa "Avaliar retorno sobre pendências"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração
  - anexo "Documentação solicitada para resolução de pendência" classes: Documentos — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - OBS1 "Responder abaixo sobre as pendências indicadas" [Memo String(2000) → CPE_CONTRATOS.OBS1] obrigatório

### [370958] EventoIntermediarioMensagem "Aviso de cancelamento"
Responsável: Cliente (papel 18)
Destinatário: Cliente (papel 18)
ModeloComunicado: Chamado cancelado
Corpo do comunicado: Prezado(a),
O chamado OrdemServico.Numero - OrdemServico.Assunto foi cancelado. Verifique o motivo abaixo:
Motivo: Complemento2 
Para mais informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [370959] EventoIntermediarioMensagem "Aviso de encaminhamento"
Config: ListaDestinatarios=organizacao@bbtecno.com.br
ModeloComunicado: Aviso sobre encaminhamento
Corpo do comunicado: OrdemServico.Cliente.Nome,
Foi encaminhado o chamado interno OrdemServico.Numero - OrdemServico.Assunto.
Acesse a aplicação Supravizio e consulte a solicitação via tela Workspace.
Atenciosamente, 
Central de Serviços

### [370960] EventoIntermediarioMensagem "Aviso sobre nomeação"
Config: ListaDestinatarios=jornada.trabalho@bbts.com.br;adm.empregado@bbts.com.br
ModeloComunicado: Aviso sobre Nomeação
Corpo do comunicado: Prezado(a), 
Informamos a efetivação da nomeação conforme segue:
MP/Chamado: OrdemServico.Numero
Nome: OrdemServico.Customizado.MOV_NOME
Matrícula: OrdemServico.Customizado.MATRICULA_MOVI
SCR: OrdemServico.Customizado.DESCRICAO_ORGAO
Função: OrdemServico.Customizado.FUNCAO_DAS_NOMEA
Nova remuneração: OrdemServico.Customizado.SALARIO_PRESTA
Atenciosamente,
Central de Serviços

### [370963] EventoIntermediarioMensagem "Aviso de Pendência"
Destinatário: Cliente (papel 18)
ModeloComunicado: Aviso de Pendência 3
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Informamos que sua Ordem de Serviço nº OrdemServico.Numero, continua com pendência(s) conforme informado abaixo.
A(s) pendência(s) é(são) a(s) informada(s) abaixo:
Complemento1 
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoGateway("GATEWAY2")
```

### [370964] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [370965] Tarefa "Verificar
/cadastrar posição no sistema"
Responsável: Fila CSC - Movimentação Pessoal (papel 510)
Config: Codigo=ANALIZAR
MotivoInterrupcaoSLA: Aguardando retorno de documentação
**ScriptFormCarregado**
```python
#Formulario["NUM_VERSAO"].Visivel = True
#
##Formulario["STEP_FUNCAO"].Habilitado = False
##Formulario["NUM_ITEM"].Habilitado = False
##Formulario["SINDICATO"].Habilitado = False
##Formulario["STEP_CARGO"].Habilitado = False
##Formulario["MATRICULA_MOVI"].Visivel = False
#
##--- Dados PeopleSoft do Favorecido
#matricula = Formulario["MATRICULA_MOVI"].Valor
#
#lista = Utils.ExecuteDataTable(" SELECT grade_15c || ' - ' || step_15c AS step_cargo, grade_15f || ' - ' || step_15f AS step_funcao, union_cd AS sindicato, position_nbr AS posicao_atual FROM PS_BBTS_F_CA_FU_VW WHERE emplid = '"+ matricula.ToString() +"' ")
#
#lista = Utils.ExecuteDataTable(" SELECT step_15c AS step_cargo, step_15f AS step_funcao, union_cd AS sindicato, position_nbr AS posicao_atual FROM PS_BBTS_F_CA_FU_VW WHERE emplid = '"+ matricula.ToString() +"' ")
#    
#for linha in lista.Rows:
#    step_cargo = linha["STEP_CARGO"].ToString()
#    step_funcao = linha["STEP_FUNCAO"].ToString()
#    sindicato = linha["SINDICATO"].ToString()
#    posicao = linha["POSICAO_ATUAL"].ToString()
#    
#Formulario["STEP_CARGO"].Valor = step_cargo
#Formulario["STEP_FUNCAO"].Valor = step_funcao
#Formulario["NUM_ITEM"].Valor = posicao
#
#
#Formulario["NUM_VERSAO"].Visivel = True
#
#Formulario["STEP_FUNCAO"].Habilitado = False
#Formulario["NUM_ITEM"].Habilitado = False
#Formulario["SINDICATO"].Habilitado = False
#Formulario["STEP_CARGO"].Habilitado = False
#Formulario["MATRICULA_MOVI"].Visivel = False
#
```
- Operação PR0001 Preencher Campos
  - CSC_OBS "Descrição detalhada" [Memo String(2000) → CPE_CSC.CSC_OBS] obrigatório
- Operação PR0001 Preencher Campos
  - FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
  - NUM_VERSAO "Número da posição" [TextBox Integer → CP_ORDEM_SERVICO.NUM_VERSAO]
  - STEP_CARGO "Step Atual do cargo" [TextBox String → CP_ORDEM_SERVICO.STEP_CARGO]
  - STEP_FUNCAO "Step Atual da função" [TextBox String → CP_ORDEM_SERVICO.STEP_FUNCAO]
  - SINDICATO "Código do sindicato" [DropDownList String → CP_ORDEM_SERVICO.SINDICATO]
  - MATRICULA_MOVI "Matrícula" [TextBox Integer → CP_ORDEM_SERVICO.MATRICULA_MOVI]

### [370966] EventoIntermediarioMensagem "Solicitação de Consulta de Férias"
Config: ListaDestinatarios=ferias.fopag@bbts.com.br
ModeloComunicado: Solicitação de Consulta de Férias
Corpo do comunicado: Prezado(a),
Solicito consultar o período de férias do empregado informado abaixo para fins de nomeação que ocorrerá a partir de OrdemServico.Customizado.DATA_ADMISSAO. Em caso afirmativo, peço informar o(s) período(s) marcado(s).
Empregado: OrdemServico.Customizado.FAVORECIDO_COBRA 
Matrícula: OrdemServico.Customizado.MATRICULA_MOVI 
Atenciosamente,
Central de Serviços

### [370967] SubProcesso "Realizar cadastro na VOETUR"
Responsável: Fila CSC - Serviços Gerais (papel 483)
Config: ChamadaAssincrona=true; AssociacaoId=1686
**ScriptInicio**
```python
sub = OrdemServico.IniciaSubProcesso(OrdemServico.Atividade)
servico = OrdemServico.Servico.Sigla
sub.Servico.Sigla = servico
sub.Assunto = 'Cadastro na VOETUR - Vindo do fluxo de Nomeação'
sub.Salva()
#sub.AvancaAtividade()
```
- ValoresInputs:
  - CustomPropertyId=550; CustomProperty=FAVORECIDO_COBRA
  - CustomPropertyId=1883; CustomProperty=MATRICULA
  - CustomPropertyId=578; CustomProperty=SCR_TODOS_RH
  - CustomPropertyId=575; CustomProperty=FUNCAO_DAS_NOMEA
- Associação: Ativo=true; FraseAssociacao=Nomeação -> VOETUR; FraseInversaAssociacao=VOETUR -> Nomeação; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=VOETUR; SeparadorSequencial=. | fonte: Nomeação → alvo: Cadastro na VOETUR

### [370968] Tarefa "Abrir chamado manualmente para alterar acessos para Gestor Centralmais"
Responsável: Movimentação de Pessoal (papel 230)
Config: ChamadaAssincrona=true; AssociacaoId=113
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Atividade
import sysAid
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.
#
#import System
#from System.IO import *
#from System.Text  import *
#from System.Text.RegularExpressions import *
#clr.AddReference("Newtonsoft.Json")
#clr.AddReference("System.Net.Http")
#from Newtonsoft.Json import *
#from Newtonsoft.Json.Linq import *
#from System.Net.Http import *
#from System.Net.Http.Headers import *
#
#titulo="Alterar permissão Nomeação Gestor"
#categoria = "Controle de Acesso e Privilégios_Conta de Rede_Alterar permissão"
#descricao = OrdemServico.Assunto+" - Chamado Supravizio= "+ OrdemServico.Numero.ToString()
#solicitante = OrdemServico.Cliente["MATRICULA"].ToString()
#usuarioAtendido = OrdemServico.GetCustom('MATRICULA_MOVI').ToString()
#pessoa = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))
#nomeColaborador = pessoa.Nome.ToString()
#matricula = OrdemServico.GetCustom('MATRICULA_MOVI').ToString()
#dataNomeacao = OrdemServico.GetCustom('DATA_ADMISSAO').ToString()
##empresa = OrdemServico.GetCustom('CSC_EMPRESA').ToString()
#localidade = DB.ExecuteScalar("SELECT DISTINCT E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE) and E.ESTABID='"+OrdemServico.GetCustom('UNIDADE_NEGOCIO').ToString()+"'")
#uorDestino = OrdemServico.GetCustom('CSC_UOR_LISTA').ToString()
##dtIncio = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_INICIO').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01')+1 )* 60 * 60 * 24 * 1000 from dual")
##dtFim = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('DATA_ADMISSAO').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01') +1)* 60 * 60 * 24 * 1000 from dual")
#
#emailUsuAtendido = DB.ExecuteScalar("select distinct ID from ta_10 where tipo = 0 and ATIVO ='S' and matricula = '"+usuarioAtendido+"'")+"@bbts.com.br"
#
#
#
#idSolic = consultaUsuario(OrdemServico.Cliente.Email)
#idAtend = consultaUsuario(emailUsuAtendido)
#if idAtend == None:
#    OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+emailUsuAtendido.ToString()
#elif idSolic == None:
#    OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+OrdemServico.Cliente.Email.ToString()
#
#else:
#    resposta = alteraPermissaoNomeacao23131(categoria, titulo, descricao, localidade, idSolic, idAtend, dataNomeacao, uorDestino)
#    if String.IsNullOrEmpty(resposta.ToString()):
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada + "\n Atividade automática de abertura de chamado para bloqueio de usuário não realizada "
#    else:
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada +"\n Chamado para Alterar permissão de usuário Gestor: "+resposta.ToString()
#        AvancaProximaAtividade = True
```
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega(129)
```
  - PropertyId=1296; Property=Favorecido
**ExpressaoValor**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))
```
  - CustomPropertyId=52; CustomProperty=DATA_INICIO
**ExpressaoValor**
```python
OrdemServico["DATA_ADMISSAO"]
```
- Associação: Ativo=true; FraseAssociacao=Nomeação -> Privilégio de acesso; FraseInversaAssociacao=Privilégio de acesso -> Nomeação; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=NOMEAPRIVI | fonte: Nomeação → alvo: Privilégios de acesso - Bloqueio

### [370969] Tarefa "Aprova a Solicitação"
Responsável: Ditac (papel 1549)
Config: Codigo=APROVA
- Operação PR0002 Aprovar: MinimoAprovadores=1
  - (aprovação) TIPO_NOMEACAO "Tipo de Nomeação" [DropDownList String → CP_ORDEM_SERVICO.TIPO_NOMEACAO]
  - (aprovação) SIM_NAO "É por afastamento previdenciário?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO]
  - (aprovação) FAVORECIDO_FUNCIO "Informe quem é o substituído" [SearchList String → CP_ORDEM_SERVICO.FAVORECIDO_FUNCIO]
  - (aprovação) NUM_DOCU "Nr.Edital Proc.Sel.Interno" [TextBox String → CP_ORDEM_SERVICO.NUM_DOCU]
  - (aprovação) LOCAL DE ATUACAO "Local de atuação" [DropDownList String → CPE_HOMOLOGACAO.LOCAL_DE_ATUACAO]
  - (aprovação) SINDICATO "Código do sindicato" [DropDownList String → CP_ORDEM_SERVICO.SINDICATO]
  - (aprovação) DESC_COLABORADOR "Tipo de Colaborador" [DropDownList String → CP_ORDEM_SERVICO.DESC_COLABORADOR]
  - (aprovação) CSC_OBS "Descrição detalhada" [Memo String(2000) → CPE_CSC.CSC_OBS]
  - (aprovação) SALARIO_PRESTA "Salário do Prestador de Serviço" [TextBox String → CP_ORDEM_SERVICO.SALARIO_PRESTA]
  - (aprovação) FAVORECIDO_COBRA1 "Novo gestor do favorecido após nomeação:" [DropDownList String → CPE_CONTRATOS.FAVORECIDO_COBRA1]
  - (aprovação) MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA]
  - (aprovação) COMBOBOX2 "Serviço Principal" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2]
  - (aprovação) RESPONSA "Responsável por dependência?" [DropDownList String → CP_ORDEM_SERVICO.RESPONSA]
  - (aprovação) DATA_ADMISSAO "Data de Nomeação" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ADMISSAO]
  - (aprovação) CARGO_DOTA "Cargo" [TextBox String → CP_ORDEM_SERVICO.CARGO_DOTA]
  - (aprovação) FAVORECIDO_COBRA "Nome" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
  - (aprovação) MATRICULA_MOVI "Matrícula" [TextBox Integer → CP_ORDEM_SERVICO.MATRICULA_MOVI]
  - (aprovação) CARGO_ATUAL "Cargo" [TextBox String → CP_ORDEM_SERVICO.CARGO_ATUAL]
  - (aprovação) FUNCAO_DAS_NOMEA "Nova Função" [DropDownList String → CP_ORDEM_SERVICO.FUNCAO_DAS_NOMEA]
  - (aprovação) CODIGO_FUNCAO_GRATIFICADA "CODIGOS DAS FUNÇÕES GRATIFICADAS" [DropDownList String → CP_ORDEM_SERVICO.CODIGO_FUNCAO_GRATIFICADA]
  - (aprovação) SCR_TODOS_RH "UOR Movimentação" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH]
  - (aprovação) FAVORECIDO_TODOS "Reporta-se a posição" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
  - (aprovação) GRID_PESSOAS "Escolher funcionários subordinados (se houver):" [DataGrid RecordList → Z_00143_GRID_PESSOAS.GRID_PESSOAS]
  - (aprovação) CURSOS_OBRIGATORIOS "Cursos Obrigatorios" [DataGrid RecordList → Z_00143_CURSOS_OBRIGATORIOS.CURSOS_OBRIGATORIOS]
  - (aprovação) SIM_NAO7 "Cursos obrigatórios realizados?" [DropDownList String → CPE_CSC.SIM_NAO7]
  - (aprovação) CSC_OBS1 "Resultado da avaliação" [Memo String(2000) → CPE_CSC.CSC_OBS1]
  - (aprovação) RESULTADO DA CONSULTA "O colaborador está cumprindo sanção decorrente de processo disciplinar?" [DropDownList String → CPE_CONTRATOS.RESULTADO_DA_CONSULTA]
  - (aprovação) DATA_ATIVIDADE2 "Fim do impedimento" [DatePicker DateTime → CPE_PESSOAS.DATA_ATIVIDADE2]
  - (aprovação) OPCAO_DE_CONFIRMACA1 "Os chamados de nomeação poderão ser abertos e aprovados entre os dias 1º e 18 do mês vigente. Chamados abertos e aprovados após o dia 18 serão automaticamente transferidos para o primeiro dia útil do mês seguinte, sendo necessário, nesses casos, um novo ato de nomeação (FQ142-001) com a data atualizada." [CheckBox Boolean → CPE_PESSOAS.OPCAO_DE_CONFIRMACA1]
  - (aprovação) LABEL_500 "<b style="color:black">Para acessar a NI142 NOMEAÇÃO <a href="https://bbts.docnix.com.br/bbts/corporate/index.html#/login?login=&senha=&empresa=1&state=permiLinkDocumento&id=573"target="_blank">clique aqui</a></b>" [Label String(500) → CPE_BOOTCAMP.LABEL_500]
  - (aprovação) LABEL100 "<b style="color:black">Para gerar a Certidão de Inabilitados do TCU <a href="https://contas.tcu.gov.br/ords/f?p=1660:3:3638144440469::::P3_TIPO_RELACAO:INABILITADO"target="_blank">clique aqui</a></b>" [Label String(1000) → CPE_CONTRATOS.LABEL100]
  - (aprovação) OPCAO_DE_CONFIRMACAO "Confirmo que todos os documentos necessários a nomeação estão devidamente anexados a este chamado." [CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO]
  - (aprovação) RESULTADO DA CONSULTA2 "Resultado da consulta a férias programadas" [DropDownList String → CPE_CONTRATOS.RESULTADO_DA_CONSULTA2]
  - (aprovação) PERIODOS "Quantos períodos de férias possui?" [DropDownList String → CPE_CONTRATOS.PERIODOS]
  - (aprovação) PERIODO01 "Período 01" [TextBox String → CPE_CONTRATOS.PERIODO01]
  - (aprovação) PERIODO02 "Período 02" [TextBox String → CPE_CONTRATOS.PERIODO02]
  - (aprovação) PERIODO03 "Período 03" [TextBox String → CPE_CONTRATOS.PERIODO03]
  - item para aprovação "Documentos Adicionais"
  - item para aprovação "Documentos obrigatórios"
  - item para aprovação "Print da tela de confirmação Peoplesoft - Férias"
  - item para aprovação "Autorização de exceções para abertura de chamado após o dia 18"
  - aprovador: Ditac (Unico)

### [370970] Tarefa "Verificar a dotação"
Responsável: Fila Planejamento e Organização (papel 154)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno

### [370971] EventoIntermediarioTimer ""
Config: TempoIntervalo=4320

## Papéis usados
### papel 1039: 00. Cesec - Outros Serviços
Tipo=RelacaoPessoas | pessoas: 00. Cesec - Outros Serviços
### papel 371: Responsável Demanda
Tipo=Composto
- composto por: Gestor do Responsável (Script)
- composto por: Responsável atual (PessoaOrdemServico)
- composto por: Gerente Executivo do Responsável atual (Script)
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 605: Fila Controle Disciplinar
Tipo=RelacaoGrupos
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
### papel 483: Fila CSC - Serviços Gerais
Tipo=RelacaoPessoas | pessoas: Fila CSC - Serviços Gerais
### papel 510: Fila CSC - Movimentação Pessoal
Tipo=RelacaoPessoas | pessoas: Fila CSC - Movimentação Pessoal
### papel 1549: Ditac
Tipo=RelacaoPessoas | pessoas: PALOMA SABINE AMADO ROSA VARGAS
### papel 154: Fila Planejamento e Organização
Tipo=RelacaoPessoas | pessoas: Fila Planejamento e Organização, JOSE ANTONIO RODRIGUES NETO, MARIANA SOARES TEODORO FERREIRA

## Campos customizados usados (definição global)

### LABEL71 — LABEL71
Label String → CPE_CONTRATOS.LABEL71

### SIM_NAO2 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO2
Itens: Sim;Não

### DATA_ATIVIDADE2 — Data da atividade
DatePicker DateTime → CPE_PESSOAS.DATA_ATIVIDADE2

### LABEL70 — Label 70
Label String(1200) → CPE_HOMOLOGACAO.LABEL70

### CURSOS_OBRIGATORIOS — Cursos Obrigatorios
DataGrid RecordList → Z_00143_CURSOS_OBRIGATORIOS.CURSOS_OBRIGATORIOS
Colunas do registro:
- DESCRICAO_CURSO "Descrição do Curso" [DropDownList String] itens: Código de Ética e Normas de Conduta do ano vigente;Guia de Integridade;Introdução à Segurança Cibernética do Banco do Brasil;LGPD - O Cuidado com os Dados Pessoais no BB;Gestão e Desenvolvimento de Pessoas;Liderança Assertiva
- SITUACAO "Situação" [DropDownList String] itens: Realizado;Não realizado

### SIM_NAO7 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO7
Itens: Sim;Não

### CSC_OBS1 — Observação/Detalhamento
Memo String(2000) → CPE_CSC.CSC_OBS1
Descrição: Observação

### LABEL72 — LABEL72
Label String → CPE_CONTRATOS.LABEL72

### RESULTADO DA CONSULTA2 — Resultado da consulta
DropDownList String → CPE_CONTRATOS.RESULTADO_DA_CONSULTA2
Itens: Possui férias;Não possui férias

### PERIODOS — Quantos períodos de férias possui?
DropDownList String → CPE_CONTRATOS.PERIODOS
Itens: 01;02;03

### PERIODO01 — Período 01
TextBox String → CPE_CONTRATOS.PERIODO01

### PERIODO02 — Período 02
TextBox String → CPE_CONTRATOS.PERIODO02

### PERIODO03 — Período 03
TextBox String → CPE_CONTRATOS.PERIODO03

### CARGO_ATUAL — Cargo
TextBox String → CP_ORDEM_SERVICO.CARGO_ATUAL

### COMBOBOX2 — COMBOBOX2
DropDownList String → CPE_BOOTCAMP.COMBOBOX2

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### MATRICULA_MOVI — Matrícula
TextBox Integer → CP_ORDEM_SERVICO.MATRICULA_MOVI

### FUNCAO_DAS_NOMEA — Função DAS
DropDownList String → CP_ORDEM_SERVICO.FUNCAO_DAS_NOMEA
Descrição: Função
Itens: ANALISTA DE TECNOLOGIA I;
ANALISTA DE TECNOLOGIA II;
ANALISTA DE TECNOLOGIA III;
ANALISTA DE TECNOLOGIA IV;
ASSESSOR JUNIOR;
ASSESSOR EXEC DA PRESIDENCIA;
ASSESSOR MASTER;
ASSESSOR PLENO;
ASSESSOR SENIOR;
DIRETOR;
GERENTE DE AREA I;
GERENTE DE AREA II;
GERENTE DE CENTRO I;
GERENTE DE CENTRO II;
GERENTE DE CENTRO III;
GERENTE DE CENTRO DE TIC I;
GERENTE DE CENTRO DE TIC II;
GERENTE DE DIVISAO;
GERENTE EXECUTIVO;
GERENTE DE GRUPO DE TIC;
GERENTE DE GRUPO I;
GERENTE DE GRUPO II;
GERENTE DE GRUPO III;
GERENTE DE PROJETOS I;
GERENTE DE PROJETOS II;
GERENTE REGIONAL DE OPERACOES;
GERENTE DE SETOR;SU…

### CODIGO_FUNCAO_GRATIFICADA — CODIGOS DAS FUNÇÕES GRATIFICADAS
DropDownList String → CP_ORDEM_SERVICO.CODIGO_FUNCAO_GRATIFICADA
**LookupScript**
```python
#Itens = DB.ExecuteDataTable(" SELECT DISTINCT BFG.GRAU FROM BBTS_FUNCAO_GRATIFICADA BFG ORDER BY 1 ")

Itens = DB.ExecuteDataTable("SELECT DISTINCT jobcode AS grau FROM xxbbtsgate.bbts_ps_jobcode_tbl po ORDER BY 1 ")
```

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

### RESPONSA — Responsável por dependência?
DropDownList String → CP_ORDEM_SERVICO.RESPONSA
Descrição: Responsabilidade
Itens: Não;Sim

### DATA_ADMISSAO — Data de Admissão
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ADMISSAO

### CARGO_DOTA — Cargo
TextBox String → CP_ORDEM_SERVICO.CARGO_DOTA

### TIPO_NOMEACAO — Tipo de nomeação
DropDownList String → CP_ORDEM_SERVICO.TIPO_NOMEACAO
Itens: De forma direta;De forma direta por destituição;Por Processo Seletivo Interno;Por Interinidade

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### FAVORECIDO_FUNCIO — Colaborador BBTS
SearchList String → CP_ORDEM_SERVICO.FAVORECIDO_FUNCIO
Descrição: Para pesquisa rápida faça:
1 - Clique na seta à direita do campo para abrir a relação de nomes;
2 - Com a lista ABERTA, pressione as teclas Ctrl + F (no IE aparece uma caixa de texto na parte superior esquerda e no Chrome na parte superior direita);
3 -  Digite o nome (ou parte dele) a ser pesquisado (serão marcados todas ocorrências que correspondam ao texto digitado);
**LookupScript**
```python
###PGESV###

lista = DB.ExecuteDataTable("select vl1 from sv_param where ch1 = 'FAVORECIDO_FUNCIO'")
sv_param = "'"
for l in lista.Rows:
    if sv_param != "'":
       sv_param += ",'"
    sv_param += l["vl1"].ToString() + "'"

if sv_param == "'":
   sv_param += " '"
#
sqlValor = "SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cpp on cpp.matricula = f.matricula inner join pessoa p on p.id_pessoa = cpp.id_pessoa WHERE f.status_matricula = 'ATIVO' AND p.ativo = 'Sim' AND P.ID_PESSOA = "+ValorCorrente

sqlEntrada = "SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cpp on cpp.matricula = f.matricula inner join pessoa p on p.id_pessoa = cpp.id_pessoa WHERE f.status_matricula = 'ATIVO' AND p.ativo = 'Sim' AND UPPER(P.NOME) like UPPER('%"+EntradaUsuario+"%')"


#sqlValor = "SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM CAD_FUNCIONARIO_V F, PESSOA P WHERE F.NOME = P.NOME AND F.DESC_COLABORADOR in ('FUNCIONÁRIO COBRA CLT', 'FUNCIONÁRIO CONCURSADO') AND f.status_matricula = 'Ativo' AND p.ativo = 'Sim' AND P.ID_PESSOA = "+ValorCorrente
 
#sqlEntrada = "SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM CAD_FUNCIONARIO_V F, PESSOA P WHERE F.NOME = P.NOME AND F.DESC_COLABORADOR in ('FUNCIONÁRIO COBRA CLT', 'FUNCIONÁRIO CONCURSADO') AND f.status_matricula = 'Ativo' AND p.ativo = 'Sim' AND UPPER(P.NOME) like UPPER('%"+EntradaUsuario+"%')"

sqlOrder = " order by nomemat asc"
 
if not String.IsNullOrEmpty(ValorCorrente) and not String.IsNullOrEmpty(EntradaUsuario):

   Itens = DB.ExecuteDataTable("(" + sqlValor + ") UNION (" + sqlEntrada + " ) " + sqlOrder)
 
elif String.IsNullOrEmpty(EntradaUsuario) and String.IsNullOrEmpty(ValorCorrente):
 
   Itens = DB.ExecuteDataTable( sqlEntrada + sqlOrder)
   #None
 
elif String.IsNullOrEmpty(EntradaUsuario):
   
   Itens = DB.ExecuteDataTable( sqlValor + sqlOrder)
 
else:
   
   Itens = DB.ExecuteDataTable( sqlEntrada + sqlOrder)
```

### NUM_DOCU — Número do documento
TextBox String → CP_ORDEM_SERVICO.NUM_DOCU

### LOCAL DE ATUACAO — LOCAL DE ATUACAO
DropDownList String → CPE_HOMOLOGACAO.LOCAL_DE_ATUACAO
Itens: MACEIO;MANAUS;SALVADOR - AV. LUIS VIANA;SALVADOR - RUA MARQUES;FORTALEZA;BRASILIA - 716 NORTE;BRASILIA - MATRIZ;BRASILIA - PARQUE TECNOLOGICO;BRASILIA - SAUN QD 5;VITORIA;GOIANIA;SÃO LUIZ;BELO HORIZONTE;UBERLANDIA;CAMPO GRANDE;CUIABA;BELEM;JOAO PESSOA;RECIFE;TERESINA;CASCAVEL;CURITIBA - PRAÇA TIRADENTES;CURITIBA - RUA AMINTAS;LONDRINA;PIRAI;RIO DE JANEIRO - Estrada dos bandeirantes 10875;RIO DE JANEIRO - Estrada dos bandeirantes 13843;RIO DE JANEIRO - AV. REPUBLICA DO CHILE;RIO DE JANEIRO - CARIOCA;RIO DE JANEIRO - JACAREPAGUA;	RIO DE JANEIRO - TELEPORTO;NATAL;PORTO VELHO;PASSO FUNDO;PORTO ALE…

### SINDICATO — SINDICATO
DropDownList String → CP_ORDEM_SERVICO.SINDICATO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(C1) as  id, C4 ||  ' (' || C5 || ')' as SINDICATO FROM SINDICATO2 WHERE C3 = 'A'")
```

### DESC_COLABORADOR — Tipo de Colaborador
DropDownList String → CP_ORDEM_SERVICO.DESC_COLABORADOR
Itens: Concursado; Contratado; Temporario; Cedido BB;Estagiario;Jovem Aprendiz

### CSC_OBS — Observação
Memo String(2000) → CPE_CSC.CSC_OBS

### SALARIO_PRESTA — Salário do Prestador de Serviço
TextBox String → CP_ORDEM_SERVICO.SALARIO_PRESTA
Descrição: Salário

### FAVORECIDO_COBRA1 — Colaborador BBTS
DropDownList String → CPE_CONTRATOS.FAVORECIDO_COBRA1
Descrição: Para pesquisa rápida faça:
1 - Clique na seta à direita do campo para abrir a relação de nomes;
2 - Com a lista ABERTA, pressione as teclas Ctrl + F (no IE aparece uma caixa de texto na parte superior esquerda e no Chrome na parte superior direita);
3 -  Digite o nome (ou parte dele) a ser pesquisado (serão marcados todas ocorrências que correspondam ao texto digitado);
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```

### MATRICULA — Matrícula
TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA

### GRID_PESSOAS — Grid Pessoas
DataGrid RecordList → Z_00143_GRID_PESSOAS.GRID_PESSOAS
Colunas do registro:
- PESSOAS "Pessoas" [DropDownList String]
**PESSOAS.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```

### RESULTADO DA CONSULTA — Resultado da consulta
DropDownList String → CPE_CONTRATOS.RESULTADO_DA_CONSULTA
Itens: Sim;Não

### OPCAO_DE_CONFIRMACA1 — Campo confirma uma afirmação
CheckBox Boolean → CPE_PESSOAS.OPCAO_DE_CONFIRMACA1
Descrição: Campo genérico para confirmação de uma afirmação

### LABEL_500 — LABEL_500
Label String(500) → CPE_BOOTCAMP.LABEL_500

### LABEL100 — Label100
Label String(1000) → CPE_CONTRATOS.LABEL100

### OPCAO_DE_CONFIRMACAO — Campo confirma uma afirmação
CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO
Descrição: Campo genérico para confirmação de uma afirmação

### OBS1 — Observação1
Memo String(2000) → CPE_CONTRATOS.OBS1
Descrição: Informe

### NUM_VERSAO — Número da Posição
TextBox Integer → CP_ORDEM_SERVICO.NUM_VERSAO

### STEP_CARGO — Step Atual do cargo
TextBox String → CP_ORDEM_SERVICO.STEP_CARGO

### STEP_FUNCAO — Step Atual da função
TextBox String → CP_ORDEM_SERVICO.STEP_FUNCAO

## Biblioteca de scripts referenciada
sysAid, teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
