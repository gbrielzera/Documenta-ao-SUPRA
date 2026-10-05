# Fluxo: Cartilha De Combate e Prevenção à Violência Contra as Mulheres (CARTILHA) — versão 1
Caminho: Fluxos > Cartilha De Combate e Prevenção à Violência Contra as Mulheres Versão 1 Cartilha De Combate e Prevenção à Violência Contra as Mulheres
XML: `XMLs para teste/Cartilha_De_Combate_e_Prevenção_à_Violência_Contra_as_Mulheres_Versão_1_Cartilha_De_Combate_e_Prevenção_à_Violência_Contra_as_Mulheres.xml` | Supravizio 19.1.1 | SubProcessoId 21507 | DesenhoProcessoId 2971 | ProcessoId 772
Órgão dono: None | Responsável: None
Classe do subprocesso: DescricaoCliente=Cartilha de Aprendizado: Prevenção à Violência Contra Mulheres; CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Cartilha de Aprendizado: Prevenção à Violência Contra Mulheres (CARTILHA)

## Grafo do fluxo
- [342036] EventoFinal "" {Cliente} → (fim)
- [342038] EventoInicial "" {Cliente} → [342036] 

## Atividades

### [342036] EventoFinal ""
Responsável: Cliente (papel 18)

### [342038] EventoInicial ""
Responsável: Cliente (papel 18)
TipoSolicitacao: Cartilha de Aprendizado Prevenção à Violência Contra Mulheres
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
    
Formulario['LABEL18'].Valor = '<p>Declaro que tive acesso ao conteúdo, e compreendi as orientações apresentadas.</p>'
Formulario['LABEL2'].Valor = '<div><h3>Combate e Prevenção à Violência Contra as Mulheres - BBTS</h3><p><b>Gepes | Junho/2026 | v1.0</b></p><p>Violência contra a mulher é qualquer ação ou omissão baseada no gênero que cause morte, lesão ou sofrimento físico, sexual, psicológico, moral ou patrimonial.</p><p><b>1. Tipos:</b> física (agressões/armas); psicológica (ameaças, humilhações, controle); moral (calúnia, difamação, ofensas); sexual (ato sem consentimento ou coerção); patrimonial (controle/destruição de bens, documentos ou dinheiro); digital/institucional (perseguição virtual, exposição de dados/imagens, negligência ou revitimização).</p><p><b>2. O que fazer:</b> confie na sua percepção: violência nunca é normal. Busque rede de apoio e serviços especializados. Em risco imediato, ligue 190. Para orientação, acolhimento e encaminhamento, ligue 180.</p><p><b>3. Proteção:</b> a Lei Maria da Penha protege mulheres em violência doméstica ou familiar. Medidas protetivas podem afastar o agressor, proibir contato, apreender armas, proteger bens e retirar conteúdo ofensivo da internet.</p><p><b>4. Rede de apoio:</b> escute sem julgar, acredite no relato, preserve o sigilo, oriente sobre canais de ajuda e acione o 190 em risco.</p><p><b>5. Canais:</b> 190 emergência; 180 Central de Atendimento à Mulher; Ouvidoria Feminina BBTS: ouvidoriafeminina@bbts.com.br</p><p style="background:#fff3cd;padding:8px;border-left:4px solid #ffc107;"><b>Importante:</b> Esta é uma prévia da cartilha, para lê-la por completo clique no link abaixo.</p><p><a href="https://bbtecno-my.sharepoint.com/:b:/g/personal/gabriel_peres_bbts_com_br/IQCX7FM74pilQ5pgA5N_kpQ1AWATRUnMw56peHhikBJ9raU?e=OirYYy" target="_blank">Clique AQUI para acessar a cartilha completa.</a></p></div>'
```
- Operação PR0001 Preencher Campos
  - LABEL2 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL2]
- Operação PR0001 Preencher Campos
  - FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório — Coluna=2
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
  - DATA_HORA_CRIACAO "Data/Hora de Registro" [DateTimePicker DateTime → CPE_CONTRATOS.DATA_HORA_CRIACAO] obrigatório — Coluna=2
- Operação PR0001 Preencher Campos
  - LABEL18 "Ciência" [Label String(700) → CP_ORDEM_SERVICO.LABEL18]
  - CHECKBOX1 "Estou ciente." [CheckBox Boolean → CPE_PESSOAS.CHECKBOX1]

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

### LABEL2 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL2
Descrição: Texto informativo

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

### LABEL18 — LABEL18
Label String(700) → CP_ORDEM_SERVICO.LABEL18

### CHECKBOX1 — Checkbox1
CheckBox Boolean → CPE_PESSOAS.CHECKBOX1

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
