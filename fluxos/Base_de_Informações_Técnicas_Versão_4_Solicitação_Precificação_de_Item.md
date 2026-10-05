# Fluxo: Solicitação Precificação de Item (PRECIFICACCAO) — versão 4
Caminho: Fluxos > Base de Informações Técnicas Versão 4 Solicitação Precificação de Item
XML: `XMLs para teste/Base_de_Informações_Técnicas_Versão_4_Solicitação_Precificação_de_Item.xml` | Supravizio 19.1.1 | SubProcessoId 22291 | DesenhoProcessoId 3022 | ProcessoId 762
Órgão dono: None | Responsável: None
Classe do subprocesso: DescricaoCliente=Solicitação Precificação de Item; CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Solicitação Precificação de Item (PRECIFICACAOITEM)

## Grafo do fluxo
- [357276] EventoFinal "" → (fim)
- [357277] Tarefa "Alocar um técnico" {Fila Planejamento de Materiais} → [357278] Precificar o item
- [357278] Tarefa "Precificar o item" {Favorecido Cobra} → [357279] Aviso de finalização
- [357279] EventoIntermediarioMensagem "Aviso de finalização" → [357280] 
- [357280] EventoFinal "" → (fim)
- [357268] EventoInicial "" {Cliente} → [359220] Aguardar aprovação
- [357275] Tarefa "Verificar solicitação e precificar o item" {Fila SOENG} → [G80417] Aprovado?
- [359220] Tarefa "Aguardar aprovação" {Fila SOENG} → [357275] Verificar solicitação e precificar o item
- [G80417] Gateway "Aprovado?" → «Não» [357276]  | «Sim» [357277] Alocar um técnico

## Gateways
### [G80417] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROV")
```
- alternativa → [357276] : SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [357277] Alocar um técnico: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```

## Atividades

### [357276] EventoFinal ""

### [357277] Tarefa "Alocar um técnico"
Responsável: Fila Planejamento de Materiais (papel 1522)
**ScriptFormCarregado**
```python
if not String.IsNullOrEmpty(Formulario['TEXT2'].Valor.ToString()):
    Formulario['TEXT2'].Visivel = True
else:
    Formulario['TEXT2'].Visivel = False

Formulario['COMBOBOX__1'].Habilitado = False
Formulario['TEXT'].Habilitado = False
Formulario['TEXT2'].Habilitado = False
Formulario['COMBOBOX'].Habilitado = False
Formulario['PRECO_GLOBAL'].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - TEXT "Item" [TextBox String(1000) → CPE_CSC.TEXT]
  - COMBOBOX__1 "Unidade" [DropDownList String → CPE_CSC.COMBOBOX__1]
  - COMBOBOX "Lista de Preço" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX]
  - PRECO_GLOBAL "Preço" [TextBox String → CPE_CONTRATOS.PRECO_GLOBAL]
  - TEXT2 "Outro" [TextBox String → CPE_CSC.TEXT2] obrigatório
  - FAVORECIDO_COBRA "Técnico a ser alocado para precificar o item" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório

### [357278] Tarefa "Precificar o item"
Responsável: Favorecido Cobra (papel 277)
**ScriptFormCarregado**
```python
if not String.IsNullOrEmpty(Formulario['TEXT2'].Valor.ToString()):
    Formulario['TEXT2'].Visivel = True
else:
    Formulario['TEXT2'].Visivel = False

Formulario['COMBOBOX__1'].Habilitado = False
Formulario['TEXT'].Habilitado = False
Formulario['TEXT2'].Habilitado = False
Formulario['COMBOBOX'].Habilitado = False
Formulario['PRECO_GLOBAL'].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - TEXT "Item" [TextBox String(1000) → CPE_CSC.TEXT]
  - COMBOBOX__1 "Unidade" [DropDownList String → CPE_CSC.COMBOBOX__1]
  - COMBOBOX "Lista de Preço" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX]
  - PRECO_GLOBAL "Preço" [TextBox String → CPE_CONTRATOS.PRECO_GLOBAL]
  - DESCRICAO_DETALHADA "Observações (Opcional)" [Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA]
  - TEXT2 "Outro" [TextBox String → CPE_CSC.TEXT2] obrigatório

### [357279] EventoIntermediarioMensagem "Aviso de finalização"
Destinatário: Cliente (papel 18)
ModeloComunicado: Finalização da solicitação
Corpo do comunicado: As informações solicitadas são:
Quantidade Administrativo: OrdemServico.Customizado.QTD_PESSOAS 
Quantidade Operacional : OrdemServico.Customizado.QUANTIDADE 
Quantidade total: OrdemServico.Customizado.VALOR_TOTAL 
Atenciosamente,
Central de Serviços

### [357280] EventoFinal ""

### [357268] EventoInicial ""
Responsável: Cliente (papel 18)
TipoSolicitacao: Solicitação Precificação de Item
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
import clr
import System

clr.AddReference("Supravizio.Custom")

from System import Convert, DBNull
from Venki.Supravizio.Recurso.Custom import Pessoa


# ============================================================
# FUNCOES AUXILIARES
# ============================================================

def Texto(valor):
    try:
        if valor is None:
            return ""

        if valor == DBNull.Value:
            return ""

        texto = Convert.ToString(valor)

        if texto is None:
            return ""

        return texto.Trim()

    except:
        try:
            texto = valor.ToString()

            if texto is None:
                return ""

            return texto.Trim()

        except:
            return ""


def SqlTexto(valor):
    try:
        return Texto(valor).Replace(
            "'",
            "''"
        )

    except:
        return ""


def ExibirMensagem(texto):
    try:
        Formulario.ExibeMensagem(
            texto
        )
    except:
        pass


def DefinirVisibilidade(campo, visivel):
    try:
        Formulario[campo].Visivel = visivel
    except:
        pass


def DefinirHabilitado(campo, habilitado):
    try:
        Formulario[campo].Habilitado = habilitado
    except:
        pass


def PreencherCampoTexto(nomeCampo, valor, bloquear):
    try:
        campo = Formulario[nomeCampo]

    except Exception as ex:
        ExibirMensagem(
            "Campo {0} nao encontrado ou inacessivel: {1}".format(
                nomeCampo,
                Texto(ex)
            )
        )

        return False


    try:
        campo.Visivel = True
    except:
        pass


    try:
        campo.Habilitado = True
    except:
        pass


    try:
        campo.Valor = Texto(
            valor
        )

    except Exception as ex:
        ExibirMensagem(
            "Erro ao preencher o campo {0}: {1}".format(
                nomeCampo,
                Texto(ex)
            )
        )

        return False


    if bloquear:
        try:
            campo.Habilitado = False
        except:
            pass


    return True


def PreencherCampoPessoa(
    nomeCampo,
    pessoaId,
    nomePessoa,
    bloquear
):
    preenchido = False

    try:
        campo = Formulario[nomeCampo]

    except Exception as ex:
        ExibirMensagem(
            "Campo {0} nao encontrado ou inacessivel: {1}".format(
                nomeCampo,
                Texto(ex)
            )
        )

        return False


    idTexto = Texto(
        pessoaId
    )

    nomeTexto = Texto(
        nomePessoa
    )


    if idTexto == "":
        ExibirMensagem(
            "Nao foi recebido um ID_PESSOA para preencher o campo {0}.".format(
                nomeCampo
            )
        )

        return False


    # --------------------------------------------------------
    # PREPARA O CONTROLE
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # CARREGA A PESSOA NA LISTA DO CONTROLE
    # --------------------------------------------------------

    try:
        sqlItens = (
            "SELECT "
            "TO_CHAR(P.ID_PESSOA) AS VALOR, "
            "P.NOME AS TEXTO "
            "FROM PESSOA P "
            "WHERE P.ID_PESSOA = {0}"
        ).format(
            Convert.ToInt32(idTexto)
        )

        dtItens = Utils.ExecuteDataTable(
            sqlItens
        )

        campo.Itens = dtItens

    except Exception as ex:
        ExibirMensagem(
            (
                "Erro ao carregar a pessoa {0} no campo {1}: {2}"
            ).format(
                nomeTexto,
                nomeCampo,
                Texto(ex)
            )
        )


    # --------------------------------------------------------
    # DEFINE O VALOR DO CAMPO
    # --------------------------------------------------------

    try:
        campo.Valor = idTexto

        try:
            campo.ScriptModificado = True
        except:
            pass

        valorAtual = Texto(
            campo.Valor
        )

        if (
            valorAtual != "" and
            valorAtual != "[Nenhum(a)]"
        ):
            preenchido = True

    except Exception as ex:
        ExibirMensagem(
            (
                "Erro ao definir a pessoa no campo {0}: {1}"
            ).format(
                nomeCampo,
                Texto(ex)
            )
        )


    if bloquear:
        try:
            campo.Habilitado = False
        except:
            pass


    return preenchido


# ============================================================
# DATA E HORA DE CRIACAO
# ============================================================

try:
    Formulario["DATA_HORA_CRIACAO"].Valor = (
        OrdemServico.DataHoraCriacao
    )
except:
    pass


# ============================================================
# OCULTA E BLOQUEIA OS CAMPOS INICIALMENTE
# ============================================================

camposAutomaticos = [
    "FAVORECIDO_TODOS",
    "TE_UOR",
    "TE_MATRICULA",
    "TE_CARGO"
]

for nomeCampoAutomatico in camposAutomaticos:

    DefinirVisibilidade(
        nomeCampoAutomatico,
        False
    )

    DefinirHabilitado(
        nomeCampoAutomatico,
        False
    )


# ============================================================
# INICIALIZACAO DOS DADOS
# ============================================================

matricula = ""
uor = ""
cargo = ""
funcao = ""
descColaborador = ""
nomePessoa = ""

pessoaSelecionada = None
idPessoa = None


# ============================================================
# UTILIZA O CLIENTE DA OS COMO A PESSOA A SER PREENCHIDA
# ============================================================

clienteId = None

try:
    clienteId = OrdemServico.ClienteId
except:
    clienteId = None


clienteIdTexto = Texto(
    clienteId
)


if clienteIdTexto == "":

    ExibirMensagem(
        "ClienteId esta vazio ou nao foi informado."
    )

else:

    try:
        idPessoa = Convert.ToInt32(
            clienteIdTexto
        )

    except:
        raise Exception(
            (
                "O ClienteId retornado pela OS nao e valido: {0}."
            ).format(
                clienteIdTexto
            )
        )


    # ========================================================
    # CARREGA O OBJETO PESSOA
    # ========================================================

    try:
        pessoaSelecionada = Pessoa.Carrega(
            idPessoa
        )

    except Exception as exPessoa:
        pessoaSelecionada = None

        ExibirMensagem(
            (
                "Nao foi possivel carregar a pessoa do ClienteId {0}: {1}"
            ).format(
                idPessoa,
                Texto(exPessoa)
            )
        )


    if pessoaSelecionada is not None:

        try:
            nomePessoa = Texto(
                pessoaSelecionada.Nome
            )
        except:
            nomePessoa = ""


    # ========================================================
    # CONSULTA OS DADOS DA PESSOA
    # ========================================================

    try:
        sql = (
            "SELECT "
            "P.NOME, "

            "CASE "
            "WHEN P.CARGO IS NOT NULL "
            "THEN TO_CHAR(P.CARGO) "
            "ELSE CAST("
            "SUBSTR("
            "C.CARGO, "
            "INSTR(C.CARGO, '|') + 1, "
            "LENGTH(C.CARGO)"
            ") AS VARCHAR2(100)"
            ") "
            "END AS CARGO, "

            "CASE "
            "WHEN CP.FUNCAO_GRATIFICADA IS NOT NULL "
            "THEN TO_CHAR(CP.FUNCAO_GRATIFICADA) "
            "ELSE CAST("
            "C.FUNCAO_GRATIFICADA AS VARCHAR2(100)"
            ") "
            "END AS FUNCAO_GRATIFICADA, "

            "TO_CHAR(C.DESC_COLABORADOR) AS DESC_COLABORADOR, "
            "TO_CHAR(CP.MATRICULA) AS MATRICULA, "
            "C.FIM_DATA_FUNCAO, "
            "TO_CHAR(O.DESCRICAO) AS DESCRICAO "

            "FROM PESSOA P "

            "LEFT JOIN CP_PESSOA CP "
            "ON CP.ID_PESSOA = P.ID_PESSOA "

            "LEFT JOIN ORGAO O "
            "ON O.ID_ORGAO = P.ID_ORGAO "

            "LEFT JOIN CAD_FUNCIONARIO_V C "
            "ON UPPER(TRIM(C.NOME)) = UPPER(TRIM(P.NOME)) "
            "AND C.DATA_DE_DEMISSAO IS NULL "

            "WHERE P.ID_PESSOA = {0}"
        ).format(
            idPessoa
        )


        lista = Utils.ExecuteDataTable(
            sql
        )


        for linha in lista.Rows:

            nomePessoa = Texto(
                linha["NOME"]
            )

            cargo = Texto(
                linha["CARGO"]
            )

            fimDataFuncao = Texto(
                linha["FIM_DATA_FUNCAO"]
            )

            if fimDataFuncao == "":
                funcao = Texto(
                    linha["FUNCAO_GRATIFICADA"]
                )

            descColaborador = Texto(
                linha["DESC_COLABORADOR"]
            )

            matricula = Texto(
                linha["MATRICULA"]
            )

            uor = Texto(
                linha["DESCRICAO"]
            )

            break


    except Exception as exConsulta:

        ExibirMensagem(
            (
                "Nao foi possivel consultar os dados da pessoa "
                "ID {0}: {1}"
            ).format(
                idPessoa,
                Texto(exConsulta)
            )
        )


    # ========================================================
    # FALLBACK DO NOME
    # ========================================================

    if nomePessoa == "":

        try:
            nomePessoa = Texto(
                Utils.ExecuteScalar(
                    (
                        "SELECT P.NOME "
                        "FROM PESSOA P "
                        "WHERE P.ID_PESSOA = {0} "
                        "AND ROWNUM = 1"
                    ).format(
                        idPessoa
                    )
                )
            )

        except:
            nomePessoa = ""


    # ========================================================
    # FALLBACK DA MATRICULA
    # ========================================================

    if matricula == "":

        try:
            matricula = Texto(
                Utils.ExecuteScalar(
                    (
                        "SELECT TO_CHAR(CP.MATRICULA) "
                        "FROM CP_PESSOA CP "
                        "WHERE CP.ID_PESSOA = {0} "
                        "AND CP.MATRICULA IS NOT NULL "
                        "AND ROWNUM = 1"
                    ).format(
                        idPessoa
                    )
                )
            )

        except:
            matricula = ""


    if matricula == "" and nomePessoa != "":

        try:
            sqlMatricula = (
                "SELECT TO_CHAR(MATRICULA) AS MATRICULA "
                "FROM CAD_FUNCIONARIO_V "
                "WHERE UPPER(TRIM(NOME)) = "
                "UPPER(TRIM('{0}')) "
                "AND DATA_DE_DEMISSAO IS NULL "
                "AND ROWNUM = 1"
            ).format(
                SqlTexto(nomePessoa)
            )

            matricula = Texto(
                Utils.ExecuteScalar(
                    sqlMatricula
                )
            )

        except Exception as exMatricula:

            ExibirMensagem(
                (
                    "Nao foi possivel buscar a matricula "
                    "na CAD_FUNCIONARIO_V: {0}"
                ).format(
                    Texto(exMatricula)
                )
            )


    # ========================================================
    # FALLBACK DA UOR
    # ========================================================

    if uor == "":

        try:
            uor = Texto(
                Utils.ExecuteScalar(
                    (
                        "SELECT TO_CHAR(O.DESCRICAO) "
                        "FROM PESSOA P "
                        "LEFT JOIN ORGAO O "
                        "ON O.ID_ORGAO = P.ID_ORGAO "
                        "WHERE P.ID_PESSOA = {0} "
                        "AND ROWNUM = 1"
                    ).format(
                        idPessoa
                    )
                )
            )

        except:
            uor = ""


    # ========================================================
    # FALLBACK DO CARGO
    # ========================================================

    if cargo == "" and nomePessoa != "":

        try:
            sqlCargo = (
                "SELECT "
                "CAST("
                "SUBSTR("
                "C.CARGO, "
                "INSTR(C.CARGO, '|') + 1, "
                "LENGTH(C.CARGO)"
                ") AS VARCHAR2(100)"
                ") AS CARGO "
                "FROM CAD_FUNCIONARIO_V C "
                "WHERE UPPER(TRIM(C.NOME)) = "
                "UPPER(TRIM('{0}')) "
                "AND C.DATA_DE_DEMISSAO IS NULL "
                "AND ROWNUM = 1"
            ).format(
                SqlTexto(nomePessoa)
            )

            cargo = Texto(
                Utils.ExecuteScalar(
                    sqlCargo
                )
            )

        except:
            cargo = ""


    # ========================================================
    # SE CARGO ESTIVER VAZIO, TENTA DESCRICAO DO COLABORADOR
    # ========================================================

    if cargo == "" and descColaborador != "":
        cargo = descColaborador


    # ========================================================
    # PREENCHE FAVORECIDO_TODOS
    # ========================================================

    PreencherCampoPessoa(
        "FAVORECIDO_TODOS",
        idPessoa,
        nomePessoa,
        True
    )


    # ========================================================
    # PREENCHE TE_MATRICULA
    # ========================================================

    PreencherCampoTexto(
        "TE_MATRICULA",
        matricula,
        True
    )


    # ========================================================
    # PREENCHE TE_UOR
    # ========================================================

    PreencherCampoTexto(
        "TE_UOR",
        uor,
        True
    )


    # ========================================================
    # PREENCHE TE_CARGO
    # ========================================================

    PreencherCampoTexto(
        "TE_CARGO",
        cargo,
        True
    )

Formulario['COMBOBOX__1'].Itens = 'CAT;BAU;BEM;BEL;BRA;CAM;CUI;CENTRAL;CGR;CUR;FLO;FOR;GOI;JOI;LON;MAN;MAC;RIO;NAT;MOL;PAL;PAF;PAM;POV;CAR;NULOG-REC;RIP;SAL;SLU;TER;UBE;VIT;NULOG-SPO;OUTRO'
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Precificação de Itens
  - COMBOBOX__1 "Informe sua unidade" [DropDownList String → CPE_CSC.COMBOBOX__1] obrigatório
  - TEXT "Informe o item" [TextBox String(1000) → CPE_CSC.TEXT] obrigatório
  - TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO] — Coluna=4
  - FAVORECIDO_TODOS "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] — Coluna=2
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] — Coluna=3

### [357275] Tarefa "Verificar solicitação e precificar o item"
Responsável: Fila SOENG (papel 1527)
**ScriptFormCarregado**
```python
if not String.IsNullOrEmpty(Formulario['TEXT2'].Valor.ToString()):
    Formulario['TEXT2'].Visivel = True
else:
    Formulario['TEXT2'].Visivel = False

Formulario['COMBOBOX__1'].Habilitado = False
Formulario['TEXT'].Habilitado = False
Formulario['TEXT2'].Habilitado = True
Formulario['COMBOBOX'].Habilitado = True
Formulario['PRECO_GLOBAL'].Habilitado = True
Formulario['COMBOBOX'].Itens = 'BBTS MANUTENÇÃO;BBTS ATIVOS;BBTS FIEL DEPOSITÁRIO;Outro'
```
- Operação PR0001 Preencher Campos
  - PRECO_GLOBAL "Preço do Item" [TextBox String → CPE_CONTRATOS.PRECO_GLOBAL] obrigatório
  - COMBOBOX "Lista de Preços" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
**COMBOBOX.ScriptModificado**
```python
if Formulario['COMBOBOX'].Valor == 'Outro':
    Formulario['TEXT2'].Visivel = True
```
  - TEXT2 "Outro:" [TextBox String → CPE_CSC.TEXT2]
  - TEXT "Item" [TextBox String(1000) → CPE_CSC.TEXT]
  - COMBOBOX__1 "Unidade" [DropDownList String → CPE_CSC.COMBOBOX__1]

### [359220] Tarefa "Aguardar aprovação"
Responsável: Fila SOENG (papel 1527)
Config: Codigo=APROV
**ScriptFormCarregado**
```python
Formulario['COMBOBOX__1'].Habilitado = False
Formulario['TEXT'].Habilitado = False
#Formulario['TEXT2'].Visivel = False

#Formulario['COMBOBOX'].Itens = 'BBTS MANUTENÇÃO;BBTS ATIVOS;BBTS FIEL DEPOSITÁRIO;Outro'
```
- Operação PR0002 Aprovar: MinimoAprovadores=1; ReprovarImediato=true
  - (aprovação) TEXT "Nome do item" [TextBox String(1000) → CPE_CSC.TEXT]
  - (aprovação) COMBOBOX__1 "Unidade" [DropDownList String → CPE_CSC.COMBOBOX__1]
  - aprovador: Gestores Setor de Engenharia (Unico)
- Operação PR0001 Preencher Campos
  - TEXT "Item" [TextBox String(1000) → CPE_CSC.TEXT]
  - COMBOBOX__1 "Unidade" [DropDownList String → CPE_CSC.COMBOBOX__1]

## Papéis usados
### papel 1522: Fila Planejamento de Materiais
Tipo=RelacaoPessoas | pessoas: Fila Planejamento de Materiais
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
### papel 1527: Fila SOENG
Tipo=RelacaoPessoas | pessoas: Fila SOENG
### papel 1515: Gestores Setor de Engenharia
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
sql = DB.ExecuteDataTable("Select PESSOA.NOME, CP_PESSOA.CARGO_FUNCIONAL, ORGAO.SIGLA, PESSOA.ID_PESSOA From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Inner Join ORGAO On ORGAO.ID_ORGAO = PESSOA.ID_ORGAO Where (CP_PESSOA.CARGO_FUNCIONAL Like '%GERENTE%' Or CP_PESSOA.CARGO_FUNCIONAL Like '%ASSESSOR%') And ORGAO.SIGLA Like '%2000007792%'")

for i in sql.Rows:
    funcionario = i['ID_PESSOA']
    pessoa = Pessoa.Carrega(Convert.ToInt32(funcionario))
    Atores.Adiciona(pessoa)
```

## Campos customizados usados (definição global)

### TEXT — TEXT
TextBox String(1000) → CPE_CSC.TEXT

### COMBOBOX__1 — COMBOBOX__1
DropDownList String → CPE_CSC.COMBOBOX__1
Itens: IPTU;Alvará Funcionamento;Vigilância Sanitária;AVCB/Bombeiros;Taxa Municipal;Taxa Estadual;Taxa Federal;Outros

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX
Itens: Órtese;Órtese Dentária; Prótese;Recurso para Saúde

### PRECO_GLOBAL — PRECO_GLOBAL
TextBox String → CPE_CONTRATOS.PRECO_GLOBAL

### TEXT2 — TEXT2
TextBox String → CPE_CSC.TEXT2

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### DESCRICAO_DETALHADA — Descrição detalhada
Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA

### TE_CARGO — Cargo
TextBox String → CPE_CSC.TE_CARGO

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
