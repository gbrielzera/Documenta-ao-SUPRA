# Fluxo: Melhoria de Processos (MELHORIADISEC) — versão 1
Caminho: Fluxos > Administração - Disec Versão 1 Melhoria de Processos
XML: `XMLs para teste/Administração_-_Disec_Versão_1_Melhoria_de_Processos.xml` | Supravizio 19.1.1 | SubProcessoId 21550 | DesenhoProcessoId 2820 | ProcessoId 732
Órgão dono: None | Responsável: None
Classe do subprocesso: CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Melhoria de Processos (MELHORIADISEC)

## Grafo do fluxo
- [342785] Tarefa "Validação do Gestor de Centro" {Cliente} → [G77570] Aprovado?
- [342786] Tarefa "Comparar antes/depois" {Disec} → [342784] Calcular percentual sobre total do centro
- [342787] EventoInicial "" {Cliente} → [342785] Validação do Gestor de Centro
- [342788] Tarefa "Validação Disec" {Cliente} → [G77573] Aprovado?
- [342782] Tarefa "Validação do Gestor do Setor" {Cliente} → [G77572] Aprovado?
- [342783] EventoFinal "" → (fim)
- [342784] Tarefa "Calcular percentual sobre total do centro" {Disec} → [342783] 
- [343232] FimCancelamento "Chamado reprovado" → (fim)
- [G77573] Gateway "Aprovado?" → «Aprovado» [342786] Comparar antes/depois | «Reprovado» [343232] Chamado reprovado
- [G77570] Gateway "Aprovado?" → «Sim» [342782] Validação do Gestor do Setor | «Reprovado» [343232] Chamado reprovado
- [G77572] Gateway "Aprovado?" → «Aprovado» [342788] Validação Disec | «Reprovado» [343232] Chamado reprovado

## Gateways
### [G77573] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROV3")
```
- alternativa → [342786] Comparar antes/depois: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [343232] Chamado reprovado: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G77570] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROV")
```
- alternativa → [342782] Validação do Gestor do Setor: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [343232] Chamado reprovado: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G77572] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROV2")
```
- alternativa → [342788] Validação Disec: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [343232] Chamado reprovado: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [342785] Tarefa "Validação do Gestor de Centro"
Responsável: Cliente (papel 18)
Config: Codigo=APROV
- Operação PR0002 Aprovar
  - aprovador: Gestor do Cliente (Unico)

### [342786] Tarefa "Comparar antes/depois"
Responsável: Disec (papel 816)
- Operação PR0001 Preencher Campos
  - OBS23 "Observações" [Memo String(4000) → CPE_CSC.OBS23] obrigatório

### [342787] EventoInicial ""
Responsável: Cliente (papel 18)
Config: Configuracao={"ServicoIniciador":"MELHORIADISEC"}
TipoSolicitacao: 00.03. Administração e Patrimônio - Criação/Alteração de Subprocessos e Relatórios na Central de Serviços
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


# Mantém visível para abertura e atendimento, mas bloqueado para edição
Formulario["TE_MATRICULA"].Visivel = True
Formulario["CSC_UOR"].Visivel = True

Formulario["TE_MATRICULA"].Habilitado = False
Formulario["CSC_UOR"].Habilitado = False


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

# Fallback para quando ClienteId não vier preenchido em outra etapa/visão
if clienteIdTexto == "" and OrdemServico.Favorecido != None:
    try:
        clienteId = OrdemServico.Favorecido.Id
        clienteIdTexto = Texto(clienteId)
    except:
        pass


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

    # SQL principal em uma linha
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
    Formulario["CSC_UOR"].Visivel = True
    Formulario["CSC_UOR"].Habilitado = True
    Formulario["CSC_UOR"].Valor = uor
    Formulario["CSC_UOR"].Habilitado = False

else:
    # Mantém os campos visíveis mesmo sem ClienteId, para não sumirem na etapa do responsável
    Formulario["TE_MATRICULA"].Visivel = True
    Formulario["CSC_UOR"].Visivel = True

    Formulario["TE_MATRICULA"].Habilitado = False
    Formulario["CSC_UOR"].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - OBS6 "Registrar melhoria" [Memo String(2000) → CPE_CSC.OBS6] obrigatório
  - VALOR_UTILIZADO "Número da OS de melhoria" [TextBox String → CPE_CSC.VALOR_UTILIZADO] obrigatório
  - SIM_NAO2 "Há necessidade de automação?" [DropDownList String → CPE_CSC.SIM_NAO2] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexar evidências" classes: Arquivo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - FAVORECIDO_COBRA "Nome" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] — Coluna=2
  - CSC_UOR "UOR" [TextBox String → CPE_CSC.CSC_UOR] obrigatório — Coluna=3

### [342788] Tarefa "Validação Disec"
Responsável: Cliente (papel 18)
Config: Codigo=APROV3
- Operação PR0002 Aprovar
  - (aprovação) SIM_NAO4 "É passível de ajustes?" [DropDownList String → CPE_CSC.SIM_NAO4] — Obrigatoriedade=Aprovacao
  - aprovador: Gerente de Divisão Disec (Unico)

### [342782] Tarefa "Validação do Gestor do Setor"
Responsável: Cliente (papel 18)
Config: Codigo=APROV2
- Operação PR0002 Aprovar
  - aprovador: Gestor de Setor - DISEC (Unico)

### [342783] EventoFinal ""

### [342784] Tarefa "Calcular percentual sobre total do centro"
Responsável: Disec (papel 816)
- Operação PR0001 Preencher Campos
  - NUMERO_OC "Número de processos melhorados" [TextBox Integer → CP_ORDEM_SERVICO.NUMERO_OC] obrigatório

### [343232] FimCancelamento "Chamado reprovado"

## Papéis usados
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 753: Gestor do Cliente
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.Cliente.Orgao.GestorId.ToString() == OrdemServico.ClienteId.ToString():
    Atores.Add(OrdemServico.Cliente.Orgao.OrgaoPai.Gestor)
else:
    Atores.Add(OrdemServico.Cliente.ObtemChefia(False))
```
### papel 816: Disec
Tipo=RelacaoOrgaos
### papel 758: Gerente de Divisão Disec
Tipo=RelacaoOrgaos
### papel 1490: Gestor de Setor - DISEC
Tipo=RelacaoPessoas | pessoas: BRUNO ROBERTO OLIVEIRA PRADO

## Campos customizados usados (definição global)

### OBS23 — Observação23
Memo String(4000) → CPE_CSC.OBS23

### OBS6 — Observação6
Memo String(2000) → CPE_CSC.OBS6

### VALOR_UTILIZADO — Valor Utilizado
TextBox String → CPE_CSC.VALOR_UTILIZADO

### SIM_NAO2 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO2
Itens: Sim;Não

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### CSC_UOR — CSC_UOR
TextBox String → CPE_CSC.CSC_UOR

### SIM_NAO4 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO4
Itens: Sim;Não

### NUMERO_OC — Número da OC
TextBox Integer → CP_ORDEM_SERVICO.NUMERO_OC

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
