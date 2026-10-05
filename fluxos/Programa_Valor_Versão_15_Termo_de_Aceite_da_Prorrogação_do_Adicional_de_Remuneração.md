# Fluxo: Termo de Aceite da Prorrogação do Adicional de Remuneração (ACEITETENCOS) — versão 15
Caminho: Fluxos > Programa Valor Versão 15 Termo de Aceite da Prorrogação do Adicional de Remuneração
XML: `XMLs para teste/Programa_Valor_Versão_15_Termo_de_Aceite_da_Prorrogação_do_Adicional_de_Remuneração.xml` | Supravizio 19.1.1 | SubProcessoId 22277 | DesenhoProcessoId 3012 | ProcessoId 695
Órgão dono: None | Responsável: None
Classe do subprocesso: DescricaoCliente=Termo de Aceite da Prorrogação do Adicional de Remuneração; CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Termo de Aceite da Prorrogação do Adicional de Remuneração (ACEITETECNOS)

## Grafo do fluxo
- [357181] EventoInicial "" → [357182] 
- [357182] EventoFinal "" → (fim)

## Atividades

### [357181] EventoInicial ""
Config: Configuracao={"ServicoIniciador":"<Nenhum>"}
TipoSolicitacao: Termo de Aceite da Prorrogação do Adicional de Remuneração
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
import clr
import System

clr.AddReference("Supravizio.Custom")

from System import Convert, DBNull
from Venki.Supravizio.Recurso.Custom import Pessoa

Formulario['LABEL1'].Valor = "<div style='border:1px solid #D1D5DB;border-radius:4px;padding:8px;font-family:Segoe UI,Arial,sans-serif;font-size:16px;line-height:1.6;color:#323130;font-style:italic;'>\"Estou ciente e anuo que a prorrogação do Adicional de Remuneração do Programa Valor que seria encerrado antes do final do término do segundo semestre de 2026, possui caráter excepcional e temporário; não constitui renovação automática dos ciclos do Programa Valor; e, não gera direito adquirido à manutenção futura do adicional. Permanecem integralmente aplicáveis os critérios de elegibilidade, desempenho e permanência previstos no regulamento do Programa; e a definição dos participantes do ciclo subsequente observará os resultados consolidados do segundo semestre de 2026. Declaro, ainda, ciência de que o período de referência da prorrogação compreende o mês fixado para término do meu ciclo de enquadramento atual até dezembro/2026, com pagamento mensal até o contracheque de janeiro/2027.\"</div>";

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
```
- Operação PR0001 Preencher Campos
  - FAVORECIDO_TODOS "Nome do Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] — Coluna=2
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] — Coluna=3
  - TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO] — Coluna=4
  - LABEL1 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - CHECKBOX1 "Declaro estar ciente, ter compreendido e aceitado todos os termos aos quais estão condicionados a prorrogação excepcional e temporária do adicional do Programa Valor." [CheckBox Boolean → CPE_PESSOAS.CHECKBOX1] obrigatório

### [357182] EventoFinal ""

## Campos customizados usados (definição global)

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

### TE_CARGO — Cargo
TextBox String → CPE_CSC.TE_CARGO

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### CHECKBOX1 — Checkbox1
CheckBox Boolean → CPE_PESSOAS.CHECKBOX1

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
