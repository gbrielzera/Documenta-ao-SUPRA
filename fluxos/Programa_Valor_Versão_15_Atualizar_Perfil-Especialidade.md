# Fluxo: Atualizar Perfil/Especialidade (ATTPERFILESPEC) — versão 15
Caminho: Fluxos > Programa Valor Versão 15 Atualizar Perfil-Especialidade
XML: `XMLs para teste/Programa_Valor_Versão_15_Atualizar_Perfil-Especialidade.xml` | Supravizio 19.1.1 | SubProcessoId 22034 | DesenhoProcessoId 3012 | ProcessoId 695
Órgão dono: 3000004051 - PROJETO SAIET | Responsável: DAIANY NEVES ROSA
Classe do subprocesso: CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadoresGrupo; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Atualizar Perfil/Especialidade (ATUALIZARPERFILESPECIALIDADE)

## Grafo do fluxo
- [350719] EventoIntermediarioMensagem "Aviso Aprovação Centro" → [350720] Aprovação do Gerente de Centro
- [350720] Tarefa "Aprovação do Gerente de Centro" {Gerente de Centro do favorecido} → [G79281] Aprovado?
- [350722] Tarefa "Justificativa de Aprovação do Gestor" {Gerente de Centro do favorecido} → [350721] Aviso Aprovado
- [350723] EventoIntermediarioMensagem "Aviso Reprovação" → [350727] 
- [350724] EventoInicial "Inicio" {Cliente} → [350719] Aviso Aprovação Centro
- [350725] Tarefa "Justificativa de Reprovação do Gestor" {Gerente de Centro do favorecido} → [350723] Aviso Reprovação
- [350721] EventoIntermediarioMensagem "Aviso Aprovado" → [350726] 
- [350727] FimCancelamento "" → (fim)
- [350726] EventoFinal "" → (fim)
- [G79281] Gateway "Aprovado?" → «Não» [350725] Justificativa de Reprovação do Gestor | «Sim» [350722] Justificativa de Aprovação do Gestor

## Gateways
### [G79281] Aprovado? (DataBasedExclusiveDecision)
Codigo=APROV
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao('APROV')
```
- alternativa → [350725] Justificativa de Reprovação do Gestor: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [350722] Justificativa de Aprovação do Gestor: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```

## Atividades

### [350719] EventoIntermediarioMensagem "Aviso Aprovação Centro"
Destinatário: Gerente Favorecido Cobra (papel 278)
Config: ListaDestinatarios=diego.soares@bbts.com.br; EnviaMensagemIndividual=true
ModeloComunicado: Aviso Aprovação Espec
Corpo do comunicado: Assunto: 
[Programa Valor] Validar Especialização 
 Corpo do e-mail: 
Prezado(a) Gestor(a), 
 O empregado OrdemServico.Customizado.FAVORECIDO_COBRA solicita validação na(s) Especialidade(s) abaixo para enquadramento do seu perfil de pontuação no Programa Valor. 
 Avalie a solicitação e proceda com a aprovação ou reprovação do pedido.
Perfil Primário:
 - OrdemServico.Customizado.COMBOBOX 
 Especialidade Principal:
 - OrdemServico.Customizado.COMBOBOX1
Perfil Secundário:
- OrdemServico.Customizado.COMBOBOX_BOX1 
 Especialidade Secundária:
 - OrdemServico.Customizado.COMBOBOX2
Perfil Terciário: 
- OrdemServico.Customizado.COMBOBOX_SIM_NAO 
 Especialidade Terciária:
 - OrdemServico.Customizado.C…

### [350720] Tarefa "Aprovação do Gerente de Centro"
Responsável: Gerente de Centro do favorecido (papel 1349)
Config: Codigo=APROV
- Operação PR0001 Preencher Campos
  - COMBOBOX_BOX1 "Perfil 2:" [DropDownList String → CPE_CONTRATOS02.COMBOBOX_BOX1]
**COMBOBOX_BOX1.ScriptModificado**
```python
especialidades_por_perfil = {"Téc. de Cobrança": ["Atendimento Administrativo", "Atendimento BackOffice"],"Téc. de Serviços Compartilhados": ["Atendimento à Inovação", "Atendimento Administrativo", "Atendimento Especializado", "Atendimento Serviços Compartilhados"],"Téc. de Soluções": ["Atendimento Agências (Cat)", "Atendimento Infra e Datacenter (Cesid)", "Atendimento Rede Man e Atendimento Priorizado", "Reparo de Peças"],"Téc. de Suporte Administrativo": ["Atendimento à Inovação", "Atendimento Administrativo", "Atendimento Especializado", "Atendimento Estoque e Logística", "Controle de Chamados"],"Téc. de TIC": ["Atendimento Segurança Cibernética", "Atendimento TIC"]}

perfil1 = Formulario["COMBOBOX"].Valor
esp1 = Formulario["COMBOBOX1"].Valor
perfil2 = Formulario["COMBOBOX_BOX1"].Valor

if perfil2:
    Formulario["COMBOBOX2"].Visivel = True
    especialidades2 = especialidades_por_perfil.get(perfil2, [])
    if perfil1 == perfil2:
        especialidades2 = [e for e in especialidades2 if e != esp1]
    else:
        especialidades2 = [e for e in especialidades2 if e != esp1]

    Formulario["COMBOBOX2"].Itens = "; ".join(especialidades2) if especialidades2 else "Null"
    Formulario["COMBOBOX_SIM_NAO"].Visivel = True
```
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório — Coluna=2
  - TE_UOR "Descrição(UOR)" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - FAVORECIDO_COBRA "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - COMBOBOX "Perfil 1:" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX]
**COMBOBOX.ScriptModificado**
```python
especialidades_por_perfil = {"Téc. de Cobrança": ["Atendimento Administrativo", "Atendimento BackOffice"],"Téc. de Serviços Compartilhados": ["Atendimento à Inovação", "Atendimento Administrativo", "Atendimento Especializado", "Atendimento Serviços Compartilhados"],"Téc. de Soluções": ["Atendimento Agências (Cat)", "Atendimento Infra e Datacenter (Cesid)", "Atendimento Rede Man e Atendimento Priorizado", "Reparo de Peças"],"Téc. de Suporte Administrativo": ["Atendimento à Inovação", "Atendimento Administrativo", "Atendimento Especializado", "Atendimento Estoque e Logística", "Controle de Chamados"],"Téc. de TIC": ["Atendimento Segurança Cibernética", "Atendimento TIC"]}

perfil1 = Formulario["COMBOBOX"].Valor

if perfil1:
    Formulario["COMBOBOX1"].Visivel = True
    Formulario["COMBOBOX1"].Itens = "; ".join(especialidades_por_perfil.get(perfil1, []))
    Formulario["COMBOBOX_BOX1"].Visivel = True
```
  - COMBOBOX1 "Especialidade Principal:" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] — Coluna=2
  - COMBOBOX2 "Especialidade Secundária:" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2] — Coluna=2
  - LABEL1 "<p style="color: red; font-weight: bold;">A especialidade híbrida ocorre quando o empregado realiza combinações de atividades dentro da sua atuação principal, tornando essas, Especialidades Secundárias e/ou Terciárias. Para caracterizar a Especialidade Híbrida é necessário que o empregado execute a atividade por no mínimo uma vez na semana.</p>" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - COMBOBOX_SIM_NAO "Perfil 3:" [DropDownList String → CPE_CONTRATOS.COMBOBOX_SIM_NAO]
**COMBOBOX_SIM_NAO.ScriptModificado**
```python
especialidades_por_perfil = {"Téc. de Cobrança": ["Atendimento Administrativo", "Atendimento BackOffice"],"Téc. de Serviços Compartilhados": ["Atendimento à Inovação", "Atendimento Administrativo", "Atendimento Especializado", "Atendimento Serviços Compartilhados"],"Téc. de Soluções": ["Atendimento Agências (Cat)", "Atendimento Infra e Datacenter (Cesid)", "Atendimento Rede Man e Atendimento Priorizado", "Reparo de Peças"],"Téc. de Suporte Administrativo": ["Atendimento à Inovação", "Atendimento Administrativo", "Atendimento Especializado", "Atendimento Estoque e Logística", "Controle de Chamados"],"Téc. de TIC": ["Atendimento Segurança Cibernética", "Atendimento TIC"]}

perfil1 = Formulario["COMBOBOX"].Valor
esp1 = Formulario["COMBOBOX1"].Valor
perfil2 = Formulario["COMBOBOX_BOX1"].Valor
esp2 = Formulario["COMBOBOX2"].Valor
perfil3 = Formulario["COMBOBOX_SIM_NAO"].Valor

if perfil3:
    Formulario["COMBOBOX3"].Visivel = True
    especialidades3 = especialidades_por_perfil.get(perfil3, [])
    
    # Elimina repetições de especialidade anteriores
    especialidades3 = [e for e in especialidades3 if e != esp1 and e != esp2]

    Formulario["COMBOBOX3"].Itens = "; ".join(especialidades3) if especialidades3 else "Null"
```
  - COMBOBOX3 "Especialidade Terciária:" [DropDownList String(900) → CPE_CONTRATOS.COMBOBOX3] — Coluna=2
  - DESCRICAO_DETALHADA "Comentário:" [Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA]
- Operação PR0002 Aprovar: MinimoAprovadores=1
  - (aprovação) FAVORECIDO_COBRA "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
  - (aprovação) COMBOBOX3 "Especialidade Terciária:" [DropDownList String(900) → CPE_CONTRATOS.COMBOBOX3]
  - (aprovação) COMBOBOX1 "Especialidade Principal:" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - (aprovação) TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
  - (aprovação) COMBOBOX "Perfil 1:" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX]
  - (aprovação) COMBOBOX2 "Especialidade Secundária:" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2]
  - (aprovação) TE_UOR "Descrição(UOR)" [TextBox String → CPE_CSC.TE_UOR]
  - (aprovação) DESCRICAO_DETALHADA "Comentário:" [Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA]
  - aprovador: Gerente de Centro do favorecido (Unico)

### [350722] Tarefa "Justificativa de Aprovação do Gestor"
Responsável: Gerente de Centro do favorecido (papel 1349)
**ScriptInicio**
```python
numero = OrdemServico.Numero

query = DB.ExecuteDataTable("SELECT OCORRENCIA.NUMERO, APROVACAO.MOTIVO FROM OCORRENCIA INNER JOIN CLASSE_SUB_PROCESSO ON OCORRENCIA.ID_CLASSE_SUB_PROC = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO INNER JOIN ASSUNTO_APROVACAO ON OCORRENCIA.ID_OCORRENCIA = ASSUNTO_APROVACAO.ID_OCORRENCIA INNER JOIN VERSAO_APROVACAO ON ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO = VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO INNER JOIN APROVACAO ON VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO = APROVACAO.ID_ASSUNTO_APROVACAO WHERE OCORRENCIA.NUMERO = '"+numero.ToString()+"'")

for motivo in query.Rows:
    motivo1 = motivo["MOTIVO"].ToString()
    
    OrdemServico["DESCRICAO_MEMORANDO"] = motivo1.ToString()
    

OrdemServico.AdicionaComentario(OrdemServico.ResponsavelId.ToString(), False)
    
AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos
  - DESCRICAO_MEMORANDO "Motivo:" [Memo String(2000) → CPE_CSC.DESCRICAO_MEMORANDO] obrigatório
**DESCRICAO_MEMORANDO.ScriptModificado**
```python
numero = OrdemServico.Numero

query = DB.ExecuteDataTable("SELECT OCORRENCIA.NUMERO, APROVACAO.MOTIVO FROM OCORRENCIA INNER JOIN CLASSE_SUB_PROCESSO ON OCORRENCIA.ID_CLASSE_SUB_PROC = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO INNER JOIN ASSUNTO_APROVACAO ON OCORRENCIA.ID_OCORRENCIA = ASSUNTO_APROVACAO.ID_OCORRENCIA INNER JOIN VERSAO_APROVACAO ON ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO = VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO INNER JOIN APROVACAO ON VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO = APROVACAO.ID_ASSUNTO_APROVACAO WHERE OCORRENCIA.NUMERO = '"+numero.ToString()+"'")

for motivo in query.Rows:
    motivo1 = motivo["MOTIVO"].ToString()
    
    Formulario["DESCRICAO_OBRIG"].Valor = motivo1.ToString()
```

### [350723] EventoIntermediarioMensagem "Aviso Reprovação"
Destinatário: Favorecido Cobra (papel 277)
ModeloComunicado: Aviso Reprovado Espec
Corpo do comunicado: Assunto: 
[Programa Valor] Validar Especialização 
 Corpo do e-mail: 
Prezado(a) Técnico(a), 
 Sua solicitação de Especialização foi rejeitada pelo gestor, segue a justificativa: 
 - OrdemServico.Customizado.DESCRICAO_OBRIG 
 Perfil Primário:
- OrdemServico.Customizado.COMBOBOX 
Especialidade Principal:
 - OrdemServico.Customizado.COMBOBOX1
Perfil Secundário:
- OrdemServico.Customizado.COMBOBOX_BOX1 
Especialidade Secundária:
 - OrdemServico.Customizado.COMBOBOX2
Perfil Terciário:
- OrdemServico.Customizado.COMBOBOX_SIM_NAO 
Especialidade Terciária:
 - OrdemServico.Customizado.COMBOBOX3 
 Atenciosamente, 
 Programa Valor

### [350724] EventoInicial "Inicio"
Responsável: Cliente (papel 18)
Config: Configuracao={"ServicoIniciador":"ATUALIZARPERFILESPECIALIDADE"}
TipoSolicitacao: Atualizar Perfil/Especialidade
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Supravizio.Processo.Custom import Processo
import clr
import System

from System import Convert


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def Texto(valor):
    try:
        if valor is None:
            return ""

        texto = Convert.ToString(valor)

        if texto is None:
            return ""

        return texto.Trim()

    except:
        return ""


def Verdadeiro(valor):
    try:
        if valor is None:
            return False

        if valor == True:
            return True

        texto = Texto(valor).ToUpper()

        return texto in [
            "TRUE",
            "VERDADEIRO",
            "SIM",
            "1"
        ]

    except:
        return False


def DefinirVisibilidade(campo, visivel):
    try:
        Formulario[campo].Visivel = visivel
    except:
        pass


def DefinirItens(campo, itens):
    try:
        Formulario[campo].Itens = ";".join(itens)
    except:
        pass


# ============================================================
# PERFIS DISPONÍVEIS
# ============================================================

perfis = [
    "Téc. de Backoffice",
    "Téc. de Canais",
    "Téc. de Cibersegurança",
    "Téc. de Soluções",
    "Téc. de Suporte Administrativo",
    "Téc. de Tic",
    "Téc. de Serviços Compartilhados"
]


DefinirItens(
    "COMBOBOX",
    perfis
)

DefinirItens(
    "COMBOBOX_BOX1",
    perfis
)

DefinirItens(
    "COMBOBOX_SIM_NAO",
    perfis
)


# ============================================================
# ESPECIALIDADES PRINCIPAIS POR PERFIL
# ============================================================

especialidades_principais = {

    "Téc. de Backoffice": [
        "Apoio Administrativo",
        "Apoio em Sistemas",
        "Apoio Operacional",
        "Controle de Produção"
    ],

    "Téc. de Canais": [
        "Controle Administrativo",
        "Controle de Qualidade",
        "Controle Operacional"
    ],

    "Téc. de Cibersegurança": [
        "Monitoração e Tratamento de Incidentes de Segurança"
    ],

    "Téc. de Soluções": [
        "Atendimento Agências (Base Destacada)",
        "Atendimento Agências (Cat)",
        "Atendimento Infra e Datacenter",
        "Atendimento Rede Man e Priorizado",
        "Reparo de Peças"
    ],

    "Téc. de Suporte Administrativo": [
        "Atendimento à Inovação",
        "Atendimento Administrativo",
        "Atendimento Especializado",
        "Atendimento Especializado em Processos da Rede",
        "Atendimento Estoque e Logística",
        "Atendimento Estoque e Logística (REC)",
        "Atendimento Estoque e Logística (SPO)",
        "Controle de Documentação Técnica",
        "Controle Operacional de Estoque",
        "Desenvolvimento de Soluções Digitais",
        "Monitoração de Equipamentos",
        "Planejamento de Materiais"
    ],

    "Téc. de Tic": [
        "Monitoração Ativa de Infra de TI",
        "Suporte de TIC e Gestão de Acesso"
    ],

    "Téc. de Serviços Compartilhados": [
        "Administrativo",
        "Compras",
        "Contratos",
        "Finanças",
        "Inovação",
        "Recursos Humanos",
        "Reskilling"
    ]
}


# ============================================================
# ESPECIALIDADES SECUNDÁRIAS POR PERFIL 2
# ============================================================

especialidades_secundarias = {

    "Téc. de Soluções": [
        "Atendimento Agências (Cat)",
        "Atendimento Infra e Datacenter",
        "Atendimento Rede Man e Priorizado",
        "Reparo de Peças"
    ],

    "Téc. de Suporte Administrativo": [
        "Atendimento à Inovação",
        "Atendimento Administrativo",
        "Atendimento Especializado",
        "Controle de Documentação Técnica",
        "Controle Operacional de Estoque",
        "Desenvolvimento de Soluções Digitais"
    ]
}


# ============================================================
# ESPECIALIDADES TERCIÁRIAS POR PERFIL 3
# ============================================================

especialidades_terciarias = {

    "Téc. de Soluções": [
        "Atendimento Agências (Cat)",
        "Atendimento Infra e Datacenter",
        "Atendimento Rede Man e Priorizado",
        "Reparo de Peças"
    ],

    "Téc. de Suporte Administrativo": [
        "Atendimento à Inovação",
        "Atendimento Administrativo",
        "Atendimento Especializado",
        "Controle de Documentação Técnica",
        "Controle Operacional de Estoque",
        "Desenvolvimento de Soluções Digitais"
    ]
}


# ============================================================
# ESPECIALIDADES HÍBRIDAS
# ============================================================

especialidades_hibridas = [
    "Atendimento Agências (Base Destacada)",
    "Atendimento Agências (Cat)",
    "Atendimento Infra e Datacenter",
    "Atendimento Rede Man e Priorizado",
    "Reparo de Peças",
    "Atendimento à Inovação",
    "Atendimento Administrativo",
    "Atendimento Especializado",
    "Atendimento Especializado em Processos da Rede",
    "Atendimento Estoque e Logística",
    "Atendimento Estoque e Logística (REC)",
    "Atendimento Estoque e Logística (SPO)",
    "Controle de Documentação Técnica",
    "Controle Operacional de Estoque",
    "Desenvolvimento de Soluções Digitais",
    "Monitoração de Equipamentos",
    "Planejamento de Materiais"
]


# ============================================================
# VALORES ATUAIS DO FORMULÁRIO
# ============================================================

perfil1 = ""

try:
    perfil1 = Texto(
        Formulario["COMBOBOX"].Valor
    )
except:
    pass


especialidade1 = ""

try:
    especialidade1 = Texto(
        Formulario["COMBOBOX1"].Valor
    )
except:
    pass


perfil2 = ""

try:
    perfil2 = Texto(
        Formulario["COMBOBOX_BOX1"].Valor
    )
except:
    pass


perfil3 = ""

try:
    perfil3 = Texto(
        Formulario["COMBOBOX_SIM_NAO"].Valor
    )
except:
    pass


# ============================================================
# VISIBILIDADE INICIAL
# ============================================================

DefinirVisibilidade(
    "COMBOBOX1",
    False
)

DefinirVisibilidade(
    "COMBOBOX_BOX1",
    False
)

DefinirVisibilidade(
    "COMBOBOX2",
    False
)

DefinirVisibilidade(
    "COMBOBOX_SIM_NAO",
    False
)

DefinirVisibilidade(
    "COMBOBOX3",
    False
)

DefinirVisibilidade(
    "TE_UOR",
    False
)

DefinirVisibilidade(
    "TE_MATRICULA",
    False
)


# ============================================================
# FAVORECIDO / DADOS FUNCIONAIS
# ============================================================

favorecidoSelecionado = False

try:
    favorecidoSelecionado = Verdadeiro(
        Formulario["FAVORECIDO_COBRA"].Valor
    )
except:
    favorecidoSelecionado = False


if favorecidoSelecionado:

    DefinirVisibilidade(
        "TE_UOR",
        True
    )

    DefinirVisibilidade(
        "TE_MATRICULA",
        True
    )


# ============================================================
# CARREGA ESPECIALIDADE PRINCIPAL
# ============================================================

if perfil1 in especialidades_principais:

    DefinirItens(
        "COMBOBOX1",
        especialidades_principais[perfil1]
    )

    DefinirVisibilidade(
        "COMBOBOX1",
        True
    )


# ============================================================
# VERIFICA SE A ESPECIALIDADE PRINCIPAL É HÍBRIDA
# ============================================================

if especialidade1 in especialidades_hibridas:

    # Exibe os controles dos níveis 2 e 3.
    DefinirVisibilidade(
        "COMBOBOX_BOX1",
        True
    )

    DefinirVisibilidade(
        "COMBOBOX_SIM_NAO",
        True
    )

    # Perfis permitidos nos níveis adicionais.
    DefinirItens(
        "COMBOBOX_BOX1",
        [
            "Téc. de Soluções",
            "Téc. de Suporte Administrativo"
        ]
    )

    DefinirItens(
        "COMBOBOX_SIM_NAO",
        [
            "Téc. de Soluções",
            "Téc. de Suporte Administrativo"
        ]
    )


    # ========================================================
    # PERFIL 2 / ESPECIALIDADE SECUNDÁRIA
    # ========================================================

    if perfil2 in especialidades_secundarias:

        DefinirItens(
            "COMBOBOX2",
            especialidades_secundarias[perfil2]
        )

        DefinirVisibilidade(
            "COMBOBOX2",
            True
        )

    else:

        DefinirVisibilidade(
            "COMBOBOX2",
            False
        )


    # ========================================================
    # PERFIL 3 / ESPECIALIDADE TERCIÁRIA
    # ========================================================

    if perfil3 in especialidades_terciarias:

        DefinirItens(
            "COMBOBOX3",
            especialidades_terciarias[perfil3]
        )

        DefinirVisibilidade(
            "COMBOBOX3",
            True
        )

    else:

        DefinirVisibilidade(
            "COMBOBOX3",
            False
        )


else:

    # Especialidade única, vazia ou não reconhecida.
    # Mantém os níveis 2 e 3 ocultos.

    DefinirVisibilidade(
        "COMBOBOX_BOX1",
        False
    )

    DefinirVisibilidade(
        "COMBOBOX2",
        False
    )

    DefinirVisibilidade(
        "COMBOBOX_SIM_NAO",
        False
    )

    DefinirVisibilidade(
        "COMBOBOX3",
        False
    )
```
**ScriptValidacao**
```python
esp1 = OrdemServico.GetCustom("COMBOBOX1")
esp2 = OrdemServico.GetCustom("COMBOBOX2")
esp3 = OrdemServico.GetCustom("COMBOBOX3")

#if esp1 == esp2 or esp1 == esp3 or esp2 == esp3:
#    Criticas.AdicionaPendencia("Atenção: As especialidades selecionadas não podem ser IGUAIS. Por favor, atualize as especialidades.")
```
- Operação PR0001 Preencher Campos
  - LABEL1 "<p style="color: red; font-weight: bold;">A especialidade híbrida ocorre quando o empregado realiza combinações de atividades dentro da sua atuação principal, tornando essas, Especialidades Secundárias e/ou Terciárias. Para caracterizar a Especialidade Híbrida é necessário que o empregado execute a atividade por no mínimo uma vez na semana.</p>" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - FAVORECIDO_COBRA "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
**FAVORECIDO_COBRA.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
# Pega o valor do campo "Favorecido Todos", converte para inteiro e guarda esse valor na variável "idFavorecidoCustom"
idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_COBRA"].Valor)
favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)

#Faz uma pesquisa em SQL trazendo a Matricula e o UOR da pessoa e guarda nessa variável chamada "lista"
lista = Utils.ExecuteDataTable("SELECT CP.MATRICULA, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'")

#Percorre os parâmetros que receberão os valores (No caso o campo "Matricula e UOR", e adiciona os respectivos valores
for linha in lista.Rows:
    matricula = linha["MATRICULA"].ToString()
    uor = linha["DESCRICAO"].ToString()

    # Habilita esses campos, pois o início do fluxo apenas aparece o campo de "Favorecido Todos"
    Formulario["TE_MATRICULA"].Valor = matricula.ToString()
    Formulario["TE_UOR"].Valor = uor.ToString()
    
    Formulario["TE_MATRICULA"].Visivel = True
    Formulario["TE_UOR"].Visivel = True
    Formulario["TE_MATRICULA"].Habilitado = False
    Formulario["TE_UOR"].Habilitado = False
```
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório — Coluna=2
  - TE_UOR "Descrição(UOR)" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - COMBOBOX "Perfil 1:" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
**COMBOBOX.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Supravizio.Processo.Custom import Processo
import clr
import System

from System import Convert


def Texto(valor):
    try:
        if valor is None:
            return ""

        texto = Convert.ToString(valor)

        if texto is None:
            return ""

        return texto.Trim()

    except:
        return ""


def DefinirVisibilidade(campo, visivel):
    try:
        Formulario[campo].Visivel = visivel
    except:
        pass


def DefinirItens(campo, itens):
    try:
        Formulario[campo].Itens = ";".join(itens)
    except:
        pass


def LimparCampo(campo):
    try:
        valorAtual = Texto(
            Formulario[campo].Valor
        )

        if valorAtual != "":
            Formulario[campo].Valor = ""

    except:
        pass


# ============================================================
# ESPECIALIDADES PRINCIPAIS POR PERFIL 1
# ============================================================

especialidades_por_perfil = {

    "Téc. de Backoffice": [
        "Apoio Administrativo",
        "Apoio em Sistemas",
        "Apoio Operacional",
        "Controle de Produção"
    ],

    "Téc. de Canais": [
        "Controle Administrativo",
        "Controle de Qualidade",
        "Controle Operacional"
    ],

    "Téc. de Cibersegurança": [
        "Monitoração e Tratamento de Incidentes de Segurança"
    ],

    "Téc. de Soluções": [
        "Atendimento Agências (Base Destacada)",
        "Atendimento Agências (Cat)",
        "Atendimento Infra e Datacenter",
        "Atendimento Rede Man e Priorizado",
        "Reparo de Peças"
    ],

    "Téc. de Suporte Administrativo": [
        "Atendimento à Inovação",
        "Atendimento Administrativo",
        "Atendimento Especializado",
        "Atendimento Especializado em Processos da Rede",
        "Atendimento Estoque e Logística",
        "Atendimento Estoque e Logística (REC)",
        "Atendimento Estoque e Logística (SPO)",
        "Controle de Documentação Técnica",
        "Controle Operacional de Estoque",
        "Desenvolvimento de Soluções Digitais",
        "Monitoração de Equipamentos",
        "Planejamento de Materiais"
    ],

    "Téc. de Tic": [
        "Monitoração Ativa de Infra de TI",
        "Suporte de TIC e Gestão de Acesso"
    ],

    "Téc. de Serviços Compartilhados": [
        "Administrativo",
        "Compras",
        "Contratos",
        "Finanças",
        "Inovação",
        "Recursos Humanos",
        "Reskilling"
    ]
}


# ============================================================
# PERFIL 1 SELECIONADO
# ============================================================

perfil1 = Texto(
    Formulario["COMBOBOX"].Valor
)


# ============================================================
# AO TROCAR O PERFIL 1, LIMPA OS CAMPOS DEPENDENTES
# ============================================================

LimparCampo(
    "COMBOBOX1"
)

LimparCampo(
    "COMBOBOX_BOX1"
)

LimparCampo(
    "COMBOBOX2"
)

LimparCampo(
    "COMBOBOX_SIM_NAO"
)

LimparCampo(
    "COMBOBOX3"
)


# ============================================================
# OCULTA OS NÍVEIS 2 E 3
# O COMBOBOX1 DEPOIS DECIDIRÁ SE DEVEM APARECER
# ============================================================

DefinirVisibilidade(
    "COMBOBOX_BOX1",
    False
)

DefinirVisibilidade(
    "COMBOBOX2",
    False
)

DefinirVisibilidade(
    "COMBOBOX_SIM_NAO",
    False
)

DefinirVisibilidade(
    "COMBOBOX3",
    False
)


# ============================================================
# CARREGA A ESPECIALIDADE PRINCIPAL
# ============================================================

if perfil1 in especialidades_por_perfil:

    DefinirItens(
        "COMBOBOX1",
        especialidades_por_perfil[perfil1]
    )

    DefinirVisibilidade(
        "COMBOBOX1",
        True
    )

else:

    DefinirItens(
        "COMBOBOX1",
        []
    )

    DefinirVisibilidade(
        "COMBOBOX1",
        False
    )
```
  - COMBOBOX1 "Especialidade Principal:" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório — Coluna=2
**COMBOBOX1.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Processo
import clr
import System

from System import Convert


def Texto(valor):
    try:
        if valor is None:
            return ""

        texto = Convert.ToString(valor)

        if texto is None:
            return ""

        return texto.Trim()

    except:
        return ""


def DefinirVisibilidade(campo, visivel):
    try:
        Formulario[campo].Visivel = visivel
    except:
        pass


def DefinirItens(campo, itens):
    try:
        Formulario[campo].Itens = ";".join(itens)
    except:
        pass


def LimparCampo(campo):
    try:
        if Texto(Formulario[campo].Valor) != "":
            Formulario[campo].Valor = ""
    except:
        pass


especialidades_hibridas = [
    "Atendimento Agências (Base Destacada)",
    "Atendimento Agências (Cat)",
    "Atendimento Infra e Datacenter",
    "Atendimento Rede Man e Priorizado",
    "Reparo de Peças",
    "Atendimento à Inovação",
    "Atendimento Administrativo",
    "Atendimento Especializado",
    "Atendimento Especializado em Processos da Rede",
    "Atendimento Estoque e Logística",
    "Atendimento Estoque e Logística (REC)",
    "Atendimento Estoque e Logística (SPO)",
    "Controle de Documentação Técnica",
    "Controle Operacional de Estoque",
    "Desenvolvimento de Soluções Digitais",
    "Monitoração de Equipamentos",
    "Planejamento de Materiais"
]


especialidade_principal = Texto(
    Formulario["COMBOBOX1"].Valor
)


if especialidade_principal in especialidades_hibridas:

    perfis_adicionais = [
        "Téc. de Soluções",
        "Téc. de Suporte Administrativo"
    ]

    DefinirItens(
        "COMBOBOX_BOX1",
        perfis_adicionais
    )

    DefinirItens(
        "COMBOBOX_SIM_NAO",
        perfis_adicionais
    )

    DefinirVisibilidade(
        "COMBOBOX_BOX1",
        True
    )

    DefinirVisibilidade(
        "COMBOBOX_SIM_NAO",
        True
    )

    # As listas de especialidade 2 e 3 só aparecem
    # depois que os respectivos perfis forem escolhidos.
    DefinirVisibilidade(
        "COMBOBOX2",
        False
    )

    DefinirVisibilidade(
        "COMBOBOX3",
        False
    )

    LimparCampo(
        "COMBOBOX2"
    )

    LimparCampo(
        "COMBOBOX3"
    )

else:

    # Especialidade única, vazia ou não reconhecida.
    for campo in [
        "COMBOBOX_BOX1",
        "COMBOBOX2",
        "COMBOBOX_SIM_NAO",
        "COMBOBOX3"
    ]:
        DefinirVisibilidade(
            campo,
            False
        )

        LimparCampo(
            campo
        )
```
  - COMBOBOX_BOX1 "Perfil 2:" [DropDownList String → CPE_CONTRATOS02.COMBOBOX_BOX1]
**COMBOBOX_BOX1.ScriptModificado**
```python
import clr
import System

from System import Convert


def Texto(valor):
    try:
        if valor is None:
            return ""

        texto = Convert.ToString(valor)

        if texto is None:
            return ""

        return texto.Trim()

    except:
        return ""


def LimparCampo(campo):
    try:
        if Texto(Formulario[campo].Valor) != "":
            Formulario[campo].Valor = ""
    except:
        pass


especialidades_secundarias = {
    "Téc. de Soluções": [
        "Atendimento Agências (Cat)",
        "Atendimento Infra e Datacenter",
        "Atendimento Rede Man e Priorizado",
        "Reparo de Peças"
    ],

    "Téc. de Suporte Administrativo": [
        "Atendimento à Inovação",
        "Atendimento Administrativo",
        "Atendimento Especializado",
        "Controle de Documentação Técnica",
        "Controle Operacional de Estoque",
        "Desenvolvimento de Soluções Digitais"
    ]
}


perfil2 = Texto(
    Formulario["COMBOBOX_BOX1"].Valor
)


if perfil2 in especialidades_secundarias:

    especialidade_atual = Texto(
        Formulario["COMBOBOX2"].Valor
    )

    if (
        especialidade_atual != "" and
        especialidade_atual not in especialidades_secundarias[perfil2]
    ):
        LimparCampo(
            "COMBOBOX2"
        )

    Formulario["COMBOBOX2"].Itens = ";".join(
        especialidades_secundarias[perfil2]
    )

    Formulario["COMBOBOX2"].Visivel = True

else:

    Formulario["COMBOBOX2"].Visivel = False

    LimparCampo(
        "COMBOBOX2"
    )
```
  - COMBOBOX2 "Especialidade Secundária:" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2] — Coluna=2
  - COMBOBOX_SIM_NAO "Perfil 3:" [DropDownList String → CPE_CONTRATOS.COMBOBOX_SIM_NAO]
**COMBOBOX_SIM_NAO.ScriptModificado**
```python
import clr
import System

from System import Convert


def Texto(valor):
    try:
        if valor is None:
            return ""

        texto = Convert.ToString(valor)

        if texto is None:
            return ""

        return texto.Trim()

    except:
        return ""


def LimparCampo(campo):
    try:
        if Texto(Formulario[campo].Valor) != "":
            Formulario[campo].Valor = ""
    except:
        pass


especialidades_terciarias = {
    "Téc. de Soluções": [
        "Atendimento Agências (Cat)",
        "Atendimento Infra e Datacenter",
        "Atendimento Rede Man e Priorizado",
        "Reparo de Peças"
    ],

    "Téc. de Suporte Administrativo": [
        "Atendimento à Inovação",
        "Atendimento Administrativo",
        "Atendimento Especializado",
        "Controle de Documentação Técnica",
        "Controle Operacional de Estoque",
        "Desenvolvimento de Soluções Digitais"
    ]
}


perfil3 = Texto(
    Formulario["COMBOBOX_SIM_NAO"].Valor
)


if perfil3 in especialidades_terciarias:

    especialidade_atual = Texto(
        Formulario["COMBOBOX3"].Valor
    )

    if (
        especialidade_atual != "" and
        especialidade_atual not in especialidades_terciarias[perfil3]
    ):
        LimparCampo(
            "COMBOBOX3"
        )

    Formulario["COMBOBOX3"].Itens = ";".join(
        especialidades_terciarias[perfil3]
    )

    Formulario["COMBOBOX3"].Visivel = True

else:

    Formulario["COMBOBOX3"].Visivel = False

    LimparCampo(
        "COMBOBOX3"
    )
```
  - COMBOBOX3 "Especialidade Terciária:" [DropDownList String(900) → CPE_CONTRATOS.COMBOBOX3] — Coluna=2
  - DESCRICAO_DETALHADA "Comentário:" [Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA]

### [350725] Tarefa "Justificativa de Reprovação do Gestor"
Responsável: Gerente de Centro do favorecido (papel 1349)
**ScriptInicio**
```python
numero = OrdemServico.Numero

query = DB.ExecuteDataTable("SELECT OCORRENCIA.NUMERO, APROVACAO.MOTIVO FROM OCORRENCIA INNER JOIN CLASSE_SUB_PROCESSO ON OCORRENCIA.ID_CLASSE_SUB_PROC = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO INNER JOIN ASSUNTO_APROVACAO ON OCORRENCIA.ID_OCORRENCIA = ASSUNTO_APROVACAO.ID_OCORRENCIA INNER JOIN VERSAO_APROVACAO ON ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO = VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO INNER JOIN APROVACAO ON VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO = APROVACAO.ID_ASSUNTO_APROVACAO WHERE OCORRENCIA.NUMERO = '"+numero.ToString()+"'")

for motivo in query.Rows:
    motivo1 = motivo["MOTIVO"].ToString()
    
    OrdemServico["DESCRICAO_OBRIG"] = motivo1.ToString()
    
AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos
  - DESCRICAO_OBRIG "Motivo:" [Memo String(2000) → CP_ORDEM_SERVICO.DESCRICAO_OBRIG] obrigatório
**DESCRICAO_OBRIG.ScriptModificado**
```python
numero = OrdemServico.Numero

query = DB.ExecuteDataTable("SELECT OCORRENCIA.NUMERO, APROVACAO.MOTIVO FROM OCORRENCIA INNER JOIN CLASSE_SUB_PROCESSO ON OCORRENCIA.ID_CLASSE_SUB_PROC = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO INNER JOIN ASSUNTO_APROVACAO ON OCORRENCIA.ID_OCORRENCIA = ASSUNTO_APROVACAO.ID_OCORRENCIA INNER JOIN VERSAO_APROVACAO ON ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO = VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO INNER JOIN APROVACAO ON VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO = APROVACAO.ID_ASSUNTO_APROVACAO WHERE OCORRENCIA.NUMERO = '"+numero.ToString()+"'")

for motivo in query.Rows:
    motivo1 = motivo["MOTIVO"].ToString()
    
    Formulario["DESCRICAO_OBRIG"].Valor = motivo1.ToString()
```

### [350721] EventoIntermediarioMensagem "Aviso Aprovado"
Destinatário: Favorecido Cobra (papel 277)
ModeloComunicado: Aviso Aprovado Espec
Corpo do comunicado: Assunto:
 Validar Especialização
 Corpo do e-mail:
 Prezado(a) Técnico(a),
 Sua solicitação de Especialização foi aprovada com sucesso pelo(a) gestor(a). 
 Perfil Primário:
 - OrdemServico.Customizado.COMBOBOX 
Especialidade Principal:
 - OrdemServico.Customizado.COMBOBOX1
Perfil Secundário
- OrdemServico.Customizado.COMBOBOX_BOX1 
Especialidade Secundária 
 - OrdemServico.Customizado.COMBOBOX2
Perfil Terciário
- OrdemServico.Customizado.COMBOBOX_SIM_NAO 
Especialidade Terciária
 - OrdemServico.Customizado.COMBOBOX3 
 Comentário do(a) Gestor(a)
 - OrdemServico.Customizado.DESCRICAO_MEMORANDO 
 Atenciosamente, 
Programa Valor

### [350727] FimCancelamento ""

### [350726] EventoFinal ""

## Papéis usados
### papel 278: Gerente Favorecido Cobra
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecidoBBTec["GESTOR_POSICAO"].ToString()+"'")))
#gestor = favorecidoBBTec.ObtemChefia(False)

#if favorecidoBBTec == gestor:
#    gestor = gestor.Orgao.OrgaoPai.Gestor

Atores.Adiciona(gestor, "Gerente do Favorecido")
```
### papel 1349: Gerente de Centro do favorecido
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
subordinado = OrdemServico.GetCustom("FAVORECIDO_COBRA")
 
gestor = DB.ExecuteDataTable("Select PESSOA.NOME As NomePessoa, CP_PESSOA.CARGO_FUNCIONAL As CargoPessoa, PESSOA1.NOME As NomeGestor, CP_PESSOA1.CARGO_FUNCIONAL As CargoGestor, PESSOA2.NOME As NomeGestorDoGestor, CP_PESSOA2.CARGO_FUNCIONAL As CargoGestorDoGestor, SUBORDINADO.NOME As NomeSubordinado, CP_SUBORDINADO.CARGO_FUNCIONAL As CargoSubordinado, PESSOA1.ID_PESSOA From PESSOA Left Join ORGAO On ORGAO.ID_ORGAO = PESSOA.ID_ORGAO Left Join CP_PESSOA On CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA Left Join PESSOA PESSOA1 On PESSOA1.ID_PESSOA = ORGAO.ID_GESTOR Left Join CP_PESSOA CP_PESSOA1 On CP_PESSOA1.ID_PESSOA = PESSOA1.ID_PESSOA Left Join ORGAO ORGAO1 On ORGAO1.ID_ORGAO = PESSOA1.ID_ORGAO Left Join PESSOA PESSOA2 On PESSOA2.ID_PESSOA = ORGAO1.ID_GESTOR Left Join CP_PESSOA CP_PESSOA2 On CP_PESSOA2.ID_PESSOA = PESSOA2.ID_PESSOA Left Join ORGAO ORGAO2 On ORGAO2.ID_GESTOR = PESSOA.ID_PESSOA Left Join PESSOA SUBORDINADO On SUBORDINADO.ID_ORGAO = ORGAO2.ID_ORGAO Left Join CP_PESSOA CP_SUBORDINADO On CP_SUBORDINADO.ID_PESSOA = SUBORDINADO.ID_PESSOA Where SUBORDINADO.ID_PESSOA = '"+OrdemServico['FAVORECIDO_COBRA'].ToString()+"'")
 
if gestor.Rows.Count != 0 or gestor.Rows.Count != None:
    for i in gestor.Rows:
        id_gestor = Convert.ToInt32(i['ID_PESSOA'])
        gtor = Pessoa.Carrega(id_gestor)
        Atores.Adiciona(gtor)
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
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```

## Campos customizados usados (definição global)

### COMBOBOX_BOX1 — COMBOBOX_BOX1
DropDownList String → CPE_CONTRATOS02.COMBOBOX_BOX1
Itens: Instalação; Preventiva; Corretiva

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX

### COMBOBOX1 — Chamado Aberto?
DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1

### COMBOBOX2 — COMBOBOX2
DropDownList String → CPE_BOOTCAMP.COMBOBOX2

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### COMBOBOX_SIM_NAO — COMBOBOX_SIM_NAO
DropDownList String → CPE_CONTRATOS.COMBOBOX_SIM_NAO
Itens: Sim;Não

### COMBOBOX3 — Combobox 3
DropDownList String(900) → CPE_CONTRATOS.COMBOBOX3
Itens: Acionamento do contrato de Mão de Obra Temporária;Pagamento de Credenciamento de reparo;Pagamento de credenciamento de serviço de engenharia

### DESCRICAO_DETALHADA — Descrição detalhada
Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA

### DESCRICAO_MEMORANDO — Descrição do memorando jurídico
Memo String(2000) → CPE_CSC.DESCRICAO_MEMORANDO

### DESCRICAO_OBRIG — Descrição obrigatória
Memo String(2000) → CP_ORDEM_SERVICO.DESCRICAO_OBRIG
Descrição: Breve descrição

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
