# Fluxo: Cartilha de Aprendizado: Prevenção à Violência Contra Mulheres (CARTILHA) — versão 2
Caminho: Fluxos > ativação teste Versão 2 Cartilha de Aprendizado Prevenção à Violência Contra Mulheres
XML: `XMLs para teste/ativação_teste_Versão_2_Cartilha_de_Aprendizado_Prevenção_à_Violência_Contra_Mulheres.xml` | Supravizio 19.1.1 | SubProcessoId 21503 | DesenhoProcessoId 2941 | ProcessoId 768
Órgão dono: None | Responsável: None
Classe do subprocesso: CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true

## Grafo do fluxo
- [341956] EventoInicial "" {Cliente} → [341957] Acesso à cartilha
- [342005] Tarefa "Respondeu todas perguntas?" {Cliente} → [G77446] Respondeu todas perguntas?
- [341978] Tarefa "Responder pergunta 01" {Cliente} → [341979] Responder pergunta 02
- [341979] Tarefa "Responder pergunta 02" {Cliente} → [341980] Responder pergunta 03
- [341980] Tarefa "Responder pergunta 03" {Cliente} → [342005] Respondeu todas perguntas?
- [341981] Tarefa "Registrar Ciência" {Cliente} → [341982] 
- [341958] Tarefa "Leitura do Conteúdo" {Cliente} → [341978] Responder pergunta 01
- [341982] EventoFinal "" {Cliente} → (fim)
- [341957] Tarefa "Acesso à cartilha" {Cliente} → [341958] Leitura do Conteúdo
- [G77446] Gateway "Respondeu todas perguntas?" → «Sim» [341981] Registrar Ciência | «Não» [341978] Responder pergunta 01

## Gateways
### [G77446] Respondeu todas perguntas? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico['SIM_NAO'] == 'Sim'
```
- alternativa → [341981] Registrar Ciência: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [341978] Responder pergunta 01: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [341956] EventoInicial ""
Responsável: Cliente (papel 18)
Config: Configuracao={"ServicoIniciador":"<Nenhum>"}
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
import clr
import System
from System import Convert


def Texto(valor):
    if valor == None:
        return ""
    texto = Convert.ToString(valor)
    if texto == None:
        return ""
    return texto


def SqlTexto(valor):
    return Texto(valor).replace("'", "''")


def PreencherCampoPessoa(nomeCampo, pessoaObj, pessoaId, nomePessoa):
    preenchido = False

    try:
        campo = Formulario[nomeCampo]
    except Exception as ex:
        Formulario.ExibeMensagem("Campo " + nomeCampo + " não encontrado/acessível: " + Texto(ex))
        return False

    idTexto = Texto(pessoaId)

    try:
        campo.Visivel = True
    except:
        pass

    try:
        campo.Habilitado = True
    except:
        pass

    try:
        campo.HabilitadoFormulario = True
    except:
        pass

    try:
        campo.PermiteModificar = True
    except:
        pass

    try:
        campo.CarregaItensSobDemanda = False
    except:
        pass

    try:
        campo.Mascara = "{TEXTO}"
    except:
        pass

    try:
        if pessoaObj != None:
            OrdemServico.Favorecido = pessoaObj
    except:
        pass

    try:
        sqlItens = "SELECT TO_CHAR(P.ID_PESSOA) AS VALOR, P.NOME AS TEXTO FROM PESSOA P WHERE P.ID_PESSOA = '" + idTexto + "'"
        dtItens = Utils.ExecuteDataTable(sqlItens)

        campo.Itens = dtItens

    except Exception as ex:
        Formulario.ExibeMensagem("Erro ao carregar colaborador no campo " + nomeCampo + ": " + Texto(ex))

    try:
        campo.Valor = idTexto

        try:
            campo.ScriptModificado = True
        except:
            pass

        valorAtual = Texto(campo.Valor)

        if valorAtual != "" and valorAtual != "[Nenhum(a)]":
            preenchido = True

    except Exception as ex:
        Formulario.ExibeMensagem("Erro ao setar colaborador no campo " + nomeCampo + ": " + Texto(ex))

    try:
        campo.Habilitado = False
    except:
        pass

    return preenchido


# Data/hora de criação
a = OrdemServico.DataHoraCriacao
Formulario["DATA_HORA_CRIACAO"].Valor = a


# Label de aviso
Formulario["LABEL1"].Valor = '<p><span style="color: red;">Atenção:</span> Clique em Concluir Abertura para continuar.<br>Após a abertura será disponibilizado a cartilha de prevenção. Após a leitura, serão feitas 3 perguntas acerca dela.</p>'


# Oculta e bloqueia inicialmente
Formulario["TE_MATRICULA"].Visivel = False
Formulario["TE_UOR"].Visivel = False

Formulario["TE_MATRICULA"].Habilitado = False
Formulario["TE_UOR"].Habilitado = False


matricula = ""
uor = ""
funcao = ""
desc_colaborador = ""
nomeFavorecido = ""
orgaoFavorecido = None
favorecidoCustom = None
idFavorecidoCustom = None

clienteId = OrdemServico.ClienteId
clienteIdTexto = Texto(clienteId)


if clienteId != None and clienteIdTexto != "":

    idFavorecidoCustom = Convert.ToInt32(clienteIdTexto)
    idFavorecidoCustomTexto = Texto(idFavorecidoCustom)

    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)

    if favorecidoCustom != None:
        nomeFavorecido = Texto(favorecidoCustom.Nome)
        orgaoFavorecido = favorecidoCustom.OrgaoId

    else:
        if OrdemServico.Favorecido != None:
            favorecidoCustom = OrdemServico.Favorecido
            nomeFavorecido = Texto(OrdemServico.Favorecido.Nome)
            orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    sql = "SELECT P.NOME, CASE WHEN P.CARGO IS NOT NULL THEN TO_CHAR(P.CARGO) ELSE CAST(SUBSTR(C.CARGO, INSTR(C.CARGO, '|') + 1, LENGTH(C.CARGO)) AS VARCHAR2(50)) END CARGO, CASE WHEN CP.FUNCAO_GRATIFICADA IS NOT NULL THEN TO_CHAR(CP.FUNCAO_GRATIFICADA) ELSE CAST(C.FUNCAO_GRATIFICADA AS VARCHAR2(50)) END FUNCAO_GRATIFICADA, TO_CHAR(C.DESC_COLABORADOR) AS DESC_COLABORADOR, TO_CHAR(CP.MATRICULA) AS MATRICULA, C.FIM_DATA_FUNCAO, TO_CHAR(O.DESCRICAO) AS DESCRICAO FROM PESSOA P LEFT JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL WHERE P.ID_PESSOA = '" + idFavorecidoCustomTexto + "'"

    lista = Utils.ExecuteDataTable(sql)

    for linha in lista.Rows:

        nomeFavorecido = Texto(linha["NOME"])

        fimDataFuncao = Texto(linha["FIM_DATA_FUNCAO"])

        if fimDataFuncao == "":
            funcao = Texto(linha["FUNCAO_GRATIFICADA"])

        desc_colaborador = Texto(linha["DESC_COLABORADOR"])
        matricula = Texto(linha["MATRICULA"])
        uor = Texto(linha["DESCRICAO"])

    # Fallback de matrícula pela CAD_FUNCIONARIO_V
    if matricula == "" and nomeFavorecido != "":
        try:
            sqlMatricula = "SELECT TO_CHAR(MATRICULA) AS MATRICULA FROM CAD_FUNCIONARIO_V WHERE NOME = '" + SqlTexto(nomeFavorecido) + "' AND DATA_DE_DEMISSAO IS NULL"
            listaMatricula = Utils.ExecuteDataTable(sqlMatricula)

            for linhaMatricula in listaMatricula.Rows:
                matricula = Texto(linhaMatricula["MATRICULA"])
                break

        except Exception as ex:
            Formulario.ExibeMensagem("Não foi possível buscar matrícula na CAD_FUNCIONARIO_V: " + Texto(ex))

    # Preenche Colaborador BBTS
    PreencherCampoPessoa(
        "FAVORECIDO_COBRA",
        favorecidoCustom,
        idFavorecidoCustom,
        nomeFavorecido
    )

    # Preenche matrícula
    Formulario["TE_MATRICULA"].Visivel = True
    Formulario["TE_MATRICULA"].Habilitado = True
    Formulario["TE_MATRICULA"].Valor = matricula
    Formulario["TE_MATRICULA"].Habilitado = False

    # Preenche UOR
    Formulario["TE_UOR"].Visivel = True
    Formulario["TE_UOR"].Habilitado = True
    Formulario["TE_UOR"].Valor = uor
    Formulario["TE_UOR"].Habilitado = False

else:
    Formulario.ExibeMensagem("ClienteId está vazio ou None.")
```
- Operação PR0001 Preencher Campos
  - FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório — Coluna=2
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
  - DATA_HORA_CRIACAO "Data/Hora do registro" [DateTimePicker DateTime → CPE_CONTRATOS.DATA_HORA_CRIACAO] obrigatório — Coluna=2
  - LABEL1 "Aviso" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]

### [342005] Tarefa "Respondeu todas perguntas?"
Responsável: Cliente (papel 18)
**ScriptFormCarregado**
```python
Formulario['COMBOBOX_I'].Habilitado = False
Formulario['COMBOBOX_II'].Habilitado = False
Formulario['COMBOBOX_III'].Habilitado = False
Formulario['LABEL11'].Visivel = False
Formulario['LABEL14'].Visivel = False
Formulario['LABEL10'].Visivel = False
Formulario['LABEL9'].Visivel = False

Formulario['LABEL11'].Valor = '<p><span style="color: red;">Resposta Errada!</span> Resposta certa: C) Qualquer ato que cause dano físico, emocional ou sexual.</p>'

Formulario['LABEL12'].Valor = '<p><span style="color: red;">Resposta Errada!</span> Resposta certa: B) Qualquer ato que cause dano físico, emocional ou sexual.</p>'

Formulario['LABEL13'].Valor = '<p><span style="color: red;">Resposta Errada!</span> Resposta certa: A) Qualquer ato que cause dano físico, emocional ou sexual.</p>'

Formulario['LABEL14'].Valor = '<p><span style="color: green;">Resposta Certa!</span></p>'
Formulario['LABEL10'].Valor = '<p><span style="color: green;">Resposta Certa!</span></p>'
Formulario['LABEL9'].Valor = '<p><span style="color: green;">Resposta Certa!</span></p>'

if Formulario['COMBOBOX_I'].Valor != 'C':
    Formulario['LABEL11'].Visivel = True
else:
    Formulario['LABEL14'].Visivel = True
    Formulario['LABEL11'].Visivel = False

if Formulario['COMBOBOX_II'].Valor != 'B':
    Formulario['LABEL12'].Visivel = True
else:
    Formulario['LABEL10'].Visivel = True
    Formulario['LABEL12'].Visivel = False

if Formulario['COMBOBOX_III'].Valor != 'A':
    Formulario['LABEL13'].Visivel = True
else:
    Formulario['LABEL9'].Visivel = True
    Formulario['LABEL13'].Visivel = False
```
- Operação PR0001 Preencher Campos
  - SIM_NAO "Respondeu todas perguntas?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
  - COMBOBOX_I "Resposta 1" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_I] obrigatório
  - COMBOBOX_II "Resposta 2" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_II] obrigatório — Coluna=2
  - COMBOBOX_III "Resposta 3" [DropDownList String → CPE_BENS_INVENTARIO.COMBOBOX_III] obrigatório — Coluna=3
  - LABEL11 "Status" [Label String(700) → CPE_PDCI2019.LABEL11]
  - LABEL12 "Status" [Label String(700) → CPE_PDCI2019.LABEL12] — Coluna=2
  - LABEL13 "Status" [Label String(700) → CPE_PDCI2019.LABEL13] — Coluna=3
  - LABEL14 "Status" [Label String(1000) → CPE_PDCI2019.LABEL14]
  - LABEL10 "Status" [Label String(700) → CPE_PDCI2019.LABEL10] — Coluna=2
  - LABEL9 "Status" [Label String(1500) → CPE_PDCI2019.LABEL9] — Coluna=3

### [341978] Tarefa "Responder pergunta 01"
Responsável: Cliente (papel 18)
**ScriptFormCarregado**
```python
Formulario['LABEL15'].Valor = '<p>Pergunta 1: O que é considerado violência contra a mulher?<br><br>A) Apenas agressão física<br>B) Apenas violência dentro de casa<br>C) Qualquer ato que cause dano físico, emocional ou sexual<br>D) Apenas crimes registrados na polícia</p>'

Formulario['COMBOBOX_I'].Itens = 'A;B;C;D'

Formulario['COMBOBOX_I'].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - LABEL15 "Pergunta N°1" [Label String(700) → CPE_PDCI2019.LABEL15]
  - COMBOBOX_I "Selecione a opção da pergunta:" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_I] obrigatório

### [341979] Tarefa "Responder pergunta 02"
Responsável: Cliente (papel 18)
**ScriptFormCarregado**
```python
Formulario['LABEL16'].Valor = '<p>Qual número deve ser acionado para orientação e apoio às mulheres em situação de violência?<br><br>A) 192<br>B) 180<br>C) 156<br>D) 190</p>'

Formulario['COMBOBOX_II'].Itens = 'A;B;C;D'

Formulario['COMBOBOX_II'].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - LABEL16 "Pergunta N°2" [Label String(700) → CPE_PDCI2019.LABEL16]
  - COMBOBOX_II "Selecione a opção da pergunta:" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_II] obrigatório

### [341980] Tarefa "Responder pergunta 03"
Responsável: Cliente (papel 18)
**ScriptFormCarregado**
```python
Formulario['LABEL17'].Valor = '<p>Segundo a Lei Maria da Penha, qual das opções abaixo é um tipo de violência?<br><br>A) Psicológica, física e moral<br>B) Apenas física<br>C) Apenas verbal<br>D) Apenas econômica</p>'

Formulario['COMBOBOX_III'].Itens = 'A;B;C;D'

Formulario['COMBOBOX_III'].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - LABEL17 "Pergunta N°3" [Label String(700) → CPE_PDCI2019.LABEL17]
  - COMBOBOX_III "Selecione a opção da pergunta:" [DropDownList String → CPE_BENS_INVENTARIO.COMBOBOX_III] obrigatório

### [341981] Tarefa "Registrar Ciência"
Responsável: Cliente (papel 18)
**ScriptFormCarregado**
```python
Formulario['LABEL18'].Valor = '<p>Declaro que tive acesso ao conteúdo, e compreendi as orientações apresentadas.</p>'
```
- Operação PR0001 Preencher Campos
  - CHECKBOX1 "Estou ciente." [CheckBox Boolean → CPE_PESSOAS.CHECKBOX1] obrigatório
  - LABEL18 "Ciência" [Label String(700) → CP_ORDEM_SERVICO.LABEL18]

### [341958] Tarefa "Leitura do Conteúdo"
Responsável: Cliente (papel 18)

### [341982] EventoFinal ""
Responsável: Cliente (papel 18)

### [341957] Tarefa "Acesso à cartilha"
Responsável: Cliente (papel 18)
**ScriptFormCarregado**
```python
Formulario['LABEL2'].Valor = '<div><h3>Prevenção da Violência Contra Mulheres - BBTS</h3><p><strong>Gepes | Maio/2026 | v1.0</strong></p><p>Cartilha adaptada para orientar e sensibilizar os públicos da BBTS sobre prevenção da violência contra a mulher, promovendo empatia, respeito e acolhimento.</p><h4>1. Tipos de violência</h4><ul><li><strong>Física:</strong> tapas, socos, empurrões, chutes, queimaduras ou uso de armas.</li><li><strong>Psicológica:</strong> ameaças, humilhações, xingamentos, chantagens, controle ou isolamento.</li><li><strong>Moral:</strong> calúnia, difamação, insultos, mentiras ou exposição da vítima.</li><li><strong>Sexual:</strong> forçar relações/práticas indesejadas ou impedir contracepção.</li><li><strong>Patrimonial:</strong> destruir documentos, controlar dinheiro, quebrar objetos ou impedir trabalho.</li></ul><h4>2. O que fazer?</h4><ul><li>Confie no que sente: violência nunca é normal.</li><li>Busque apoio de familiares, amigas e serviços públicos.</li><li>Em risco imediato, ligue 190.</li><li>Para orientação, ligue 180 ou WhatsApp (61) 99610-0180.</li></ul><h4>3. Lei Maria da Penha</h4><p>Protege mulheres em situação de violência doméstica ou familiar, independentemente da identidade de gênero ou orientação sexual.</p><h4>4. Medidas protetivas</h4><p>Incluem afastamento do agressor, proibição de aproximação, apreensão de armas, proteção patrimonial e retirada de postagens ofensivas.</p><h4>5. Apoio</h4><ul><li>190: Polícia Militar.</li><li>180: Central de Atendimento à Mulher.</li><li>Ouvidoria Feminina BBTS: ouvidoriafeminina@bbts.com.br</li></ul><p style="background:#fff3cd; padding:10px; border-left:5px solid #ffc107;"><strong>Importante:</strong> Esta label apresenta uma versão adaptada da cartilha original para leitura direta no Supravizio.</p><p><a href="https://bbtecno-my.sharepoint.com/:b:/g/personal/gabriel_peres_bbts_com_br/IQDc8CZgjOL0RpUQgT2GTr0qAYhooNUc1n-MXc8250hZOSw?e=O6rf8B" target="_blank">Clique AQUI para acessar a cartilha completa.</p></a></div>';
```
- Operação PR0001 Preencher Campos
  - LABEL2 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL2]

## Papéis usados
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```

## Campos customizados usados (definição global)

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### DATA_HORA_CRIACAO — Data hora da criação
DateTimePicker DateTime → CPE_CONTRATOS.DATA_HORA_CRIACAO

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### COMBOBOX_I — COMBOBOX_I
DropDownList String → CPE_BOOTCAMP.COMBOBOX_I

### COMBOBOX_II — COMBOBOX_II
DropDownList String → CPE_BOOTCAMP.COMBOBOX_II

### COMBOBOX_III — COMBOBOX_III
DropDownList String → CPE_BENS_INVENTARIO.COMBOBOX_III

### LABEL11 — LABEL11
Label String(700) → CPE_PDCI2019.LABEL11

### LABEL12 — LABEL12
Label String(700) → CPE_PDCI2019.LABEL12

### LABEL13 — LABEL13
Label String(700) → CPE_PDCI2019.LABEL13

### LABEL14 — LABEL14
Label String(1000) → CPE_PDCI2019.LABEL14

### LABEL10 — LABEL10
Label String(700) → CPE_PDCI2019.LABEL10

### LABEL9 — LABEL9
Label String(1500) → CPE_PDCI2019.LABEL9

### LABEL15 — LABEL15
Label String(700) → CPE_PDCI2019.LABEL15

### LABEL16 — LABEL16
Label String(700) → CPE_PDCI2019.LABEL16

### LABEL17 — LABEL17
Label String(700) → CPE_PDCI2019.LABEL17

### CHECKBOX1 — Checkbox1
CheckBox Boolean → CPE_PESSOAS.CHECKBOX1

### LABEL18 — LABEL18
Label String(700) → CP_ORDEM_SERVICO.LABEL18

### LABEL2 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL2
Descrição: Texto informativo

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
