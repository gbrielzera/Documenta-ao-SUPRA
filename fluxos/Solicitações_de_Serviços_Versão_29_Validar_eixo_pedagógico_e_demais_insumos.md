# Fluxo: Validar eixo pedagógico e demais insumos (AVALEIXOPEDAGRES) — versão 29
Caminho: Fluxos > Solicitações de Serviços Versão 29 Validar eixo pedagógico e demais insumos
XML: `XMLs para teste/Solicitações_de_Serviços_Versão_29_Validar_eixo_pedagógico_e_demais_insumos.xml` | Supravizio 19.1.1 | SubProcessoId 22517 | DesenhoProcessoId 3054 | ProcessoId 29
Órgão dono: 3000003211 - SETOR DE DESENVOLVIMENTO PROFISSIONAL E MOVIMENTACAO | Responsável: RENATA BIANGOLINO BENICIO SORANSSO
Classe do subprocesso: CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Encaminhar eixo pedagógico e demais insumos (EIXOPED)

## Grafo do fluxo
- [360128] Tarefa "Avaliar e reportar" {Fila Treinamento} → [G80947] Aprovado?
- [360129] EventoFinal "" → (fim)
- [360127] EventoIntermediarioMensagem "Abertura de demanda" → [360128] Avaliar e reportar
- [360130] EventoInicial "" → [360127] Abertura de demanda
- [360131] EventoFinal "" → (fim)
- [360132] EventoIntermediarioMensagem "Comunica reprovação" → [360131] 
- [360133] EventoIntermediarioMensagem "Comunica aprovação" → [360129] 
- [G80947] Gateway "Aprovado?" → «Aprovado» [360133] Comunica aprovação | «Reprovado» [360132] Comunica reprovação

## Gateways
### [G80947] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAEIXO")
```
- alternativa → [360133] Comunica aprovação: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [360132] Comunica reprovação: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [360128] Tarefa "Avaliar e reportar"
Responsável: Fila Treinamento (papel 188)
Config: Codigo=APROVAEIXO
- Operação PR0002 Aprovar: CopiarAnexados=true
  - (aprovação) LISTA_DE_PESSOAS "Lista de Pessoas" [DataGrid RecordList → Z_00143_LISTA_DE_PESSOAS.LISTA_DE_PESSOAS]
  - (aprovação) TE_DT_INICIO "Data prevista para realização do treinamento/workshop/oficina/palestra/live  " [DatePicker DateTime → CPE_CSC.TE_DT_INICIO]
  - (aprovação) SCR_TODOS_RH "UOR" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH]
  - (aprovação) TE_CURSO "Nome do curso/ evento" [TextBox String → CPE_CSC.TE_CURSO]
  - (aprovação) NOME_PROJETO "Tema" [TextBox String → CP_ORDEM_SERVICO.NOME_PROJETO]
  - (aprovação) COMBOBOX1 "Modalidade" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - (aprovação) COMBOBOX "Tipo evento" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX]
  - item para aprovação " FQ148-002 - Eixo Pedagógico"
  - item para aprovação "Demais insumos (roteiro, apresentação, etc.)"
  - aprovador: Gestor do Serviço (Unico)
- Operação PR0001 Preencher Campos
  - LISTA_DE_PESSOAS "Lista de Pessoas" [DataGrid RecordList → Z_00143_LISTA_DE_PESSOAS.LISTA_DE_PESSOAS]
    - coluna NOME obrigatório
    - coluna MATRICULA obrigatório
    - coluna UOR obrigatório

### [360129] EventoFinal ""

### [360127] EventoIntermediarioMensagem "Abertura de demanda"
Destinatário: Gestor do Serviço (papel 17)
Config: ListaDestinatarios=desenvolvimentoprofissional@bbts.com.br
ModeloComunicado: Comunicado GEPES - Concurso
Corpo do comunicado: Complemento1 
 Complemento2 
 Complemento3 
 Complemento4 
 Complemento5
**ScriptEvento**
```python
#Mensagem.Destinatarios.Add(OrdemServico["CSC_EMAIL_PESSOAL"])
UOR = DB.ExecuteScalar("SELECT NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO Where to_char(SCR) ='" + OrdemServico["SCR_TODOS_RH"] + "'") 

Mensagem.Assunto = "Validar Eixo Pedagógico e demais insumos - Nova Solicitação" 
Mensagem.Complemento1 = "Prezados,<br><Br>Gostaria de informar que um novo chamado de solicitação foi aberto para a validação do eixo pedagógico e demais insumos, e está aguardando sua aprovação. Seguem os detalhes abaixo:<br><br>Chamado Número: "+ OrdemServico.Numero + "<br>Cliente: " + OrdemServico.Cliente.Nome + "<br>UOR: " + UOR.ToString() + "<br><br>Atenciosamente,<br><Br>"
```
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=1655; ClasseConfiguracao=Arquivo
  - ClasseConfiguracaoId=2763; ClasseConfiguracao=Anexo

### [360130] EventoInicial ""
TipoSolicitacao: Solicitação de Serviços
**ScriptValidacao**
```python
if (OrdemServico["COMBOBOX"] == 'Treinamento Interno Multiplicadores' or OrdemServico["COMBOBOX"] =='Treinamento Interno Educadores') and OrdemServico.PossuiItem('ARQUIVO') == False:
    Criticas.AdicionaPendencia("Para Treinamentos Internos Multiplicador ou Educador o FQ148-002 - Eixo Pedagógico, é obrigatório.")

if DateTime.AddDays(OrdemServico["TE_DT_INICIO"], -10) <= DateTime.Now.Date:
    Criticas.AdicionaPendencia("Conforme orientação contida no PRO148, a GEPES deve ser comunicada 10 dias antes da realização do evento.")
```
**ScriptFormCarregado**
```python
Formulario["COMBOBOX"].Itens = "Workshop/Oficina;Palestra/Live;Treinamento Interno Multiplicadores;Treinamento Interno Educadores"

Formulario["COMBOBOX1"].Itens = "Presencial;On-line"
```
- Operação PR0004 Associar Itens Configuração: Nome=DEMAIS
  - anexo "Demais insumos (roteiro, apresentação, etc.)" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos
  - LABEL1 "<div style="color: red"><b>Para Treinamentos Internos Multiplicador ou Educador anexar obrigatoriamente a FQ148-002 - Eixo Pedagógico.<br>
Para Workshop, Oficina, Palestra ou Live anexar obrigatoriamente a FQ 148-006 - Capacitação Corporativa - Resumo.
<br> Outros documentos e informações poderão ser solicitados a critério da Gepes/UniBBTS.</b></div>" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - COMBOBOX "Tipo evento" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
  - COMBOBOX1 "Modalidade" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
  - NOME_PROJETO "Tema" [TextBox String → CP_ORDEM_SERVICO.NOME_PROJETO] obrigatório
  - TE_CURSO "Nome do curso/ evento" [TextBox String → CPE_CSC.TE_CURSO] obrigatório
  - SCR_TODOS_RH "UOR" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH] obrigatório
  - TE_DT_INICIO "Data prevista para realização do treinamento/workshop/oficina/palestra/live  " [DatePicker DateTime → CPE_CSC.TE_DT_INICIO] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=EIXOPEDAGOGICO
  - anexo " FQ148-002 - Eixo Pedagógico" classes: Arquivo — RequeridoInicial=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Lista de Pessoas
  - LISTA_DE_PESSOAS "Lista de Favorecidos" [DataGrid RecordList → Z_00143_LISTA_DE_PESSOAS.LISTA_DE_PESSOAS] obrigatório — QtdColunasFormulario=1
    - coluna NOME
**LISTA_DE_PESSOAS.NOME.ScriptModificado**
```python
import clr
import System

from System import Convert, DBNull


def Texto(valor):
    try:
        if valor is None or valor == DBNull.Value:
            return ""

        texto = Convert.ToString(valor)

        if texto is None:
            return ""

        return texto.Trim()

    except:
        return ""


idPessoaTexto = Texto(
    FormularioRegistro["NOME"].Valor
)


if idPessoaTexto == "":

    FormularioRegistro["MATRICULA"].Valor = ""
    FormularioRegistro["UOR"].Valor = ""

else:

    try:
        idPessoa = Convert.ToInt32(
            idPessoaTexto
        )

        sql = (
            "SELECT "
            "P.NOME, "
            "TO_CHAR(CP.MATRICULA) AS MATRICULA, "
            "TO_CHAR(O.DESCRICAO) AS UOR "
            "FROM PESSOA P "
            "LEFT JOIN CP_PESSOA CP "
            "ON CP.ID_PESSOA = P.ID_PESSOA "
            "LEFT JOIN ORGAO O "
            "ON O.ID_ORGAO = P.ID_ORGAO "
            "WHERE P.ID_PESSOA = {0} "
            "AND ROWNUM = 1"
        ).format(
            idPessoa
        )

        dados = DB.ExecuteDataTable(
            sql
        )

        if dados.Rows.Count > 0:

            registro = dados.Rows[0]

            matricula = Texto(
                registro["MATRICULA"]
            )

            uor = Texto(
                registro["UOR"]
            )

            FormularioRegistro["MATRICULA"].Valor = matricula
            FormularioRegistro["UOR"].Valor = uor

        else:

            FormularioRegistro["MATRICULA"].Valor = ""
            FormularioRegistro["UOR"].Valor = ""

            Formulario.ExibeMensagem(
                "Não foi encontrada uma pessoa para o identificador {0}.".format(
                    idPessoaTexto
                )
            )

    except Exception as ex:

        FormularioRegistro["MATRICULA"].Valor = ""
        FormularioRegistro["UOR"].Valor = ""

        Formulario.ExibeMensagem(
            "Não foi possível consultar os dados da pessoa: {0}".format(
                Texto(ex)
            )
        )
```
    - coluna MATRICULA
**LISTA_DE_PESSOAS.MATRICULA.ScriptModificado**
```python
import clr
import System

from System import Convert, DBNull


def Texto(valor):
    try:
        if valor is None or valor == DBNull.Value:
            return ""

        texto = Convert.ToString(valor)

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


def PreencherCampoPessoaRegistro(idPessoa, nomePessoa):
    try:
        campoNome = FormularioRegistro["NOME"]

        idTexto = Texto(
            idPessoa
        )

        if idTexto == "":
            return False

        # Carrega no seletor somente a pessoa encontrada.
        sqlItens = (
            "SELECT "
            "TO_CHAR(P.ID_PESSOA) AS VALOR, "
            "P.NOME AS TEXTO "
            "FROM PESSOA P "
            "WHERE P.ID_PESSOA = {0}"
        ).format(
            Convert.ToInt32(idTexto)
        )

        itens = Utils.ExecuteDataTable(
            sqlItens
        )

        try:
            campoNome.CarregaItensSobDemanda = False
        except:
            pass

        try:
            campoNome.Mascara = "{TEXTO}"
        except:
            pass

        campoNome.Itens = itens
        campoNome.Valor = idTexto

        return True

    except Exception as ex:

        try:
            Formulario.ExibeMensagem(
                "Não foi possível preencher o campo NOME: {0}".format(
                    Texto(ex)
                )
            )
        except:
            pass

        return False


matricula = Texto(
    FormularioRegistro["MATRICULA"].Valor
)


if matricula == "":

    try:
        FormularioRegistro["NOME"].Valor = ""
    except:
        pass

    FormularioRegistro["UOR"].Valor = ""

else:

    try:
        sql = (
            "SELECT "
            "TO_CHAR(P.ID_PESSOA) AS ID_PESSOA, "
            "P.NOME, "
            "TO_CHAR(CP.MATRICULA) AS MATRICULA, "
            "TO_CHAR(O.DESCRICAO) AS UOR "
            "FROM PESSOA P "
            "INNER JOIN CP_PESSOA CP "
            "ON CP.ID_PESSOA = P.ID_PESSOA "
            "LEFT JOIN ORGAO O "
            "ON O.ID_ORGAO = P.ID_ORGAO "
            "WHERE TRIM(TO_CHAR(CP.MATRICULA)) = "
            "TRIM('{0}') "
            "AND ROWNUM = 1"
        ).format(
            SqlTexto(matricula)
        )

        dados = DB.ExecuteDataTable(
            sql
        )

        if dados.Rows.Count > 0:

            registro = dados.Rows[0]

            idPessoa = Texto(
                registro["ID_PESSOA"]
            )

            nomePessoa = Texto(
                registro["NOME"]
            )

            uor = Texto(
                registro["UOR"]
            )

            PreencherCampoPessoaRegistro(
                idPessoa,
                nomePessoa
            )

            FormularioRegistro["UOR"].Valor = uor

        else:

            try:
                FormularioRegistro["NOME"].Valor = ""
            except:
                pass

            FormularioRegistro["UOR"].Valor = ""

            Formulario.ExibeMensagem(
                "Não foi encontrado funcionário para a matrícula {0}.".format(
                    matricula
                )
            )

    except Exception as ex:

        FormularioRegistro["UOR"].Valor = ""

        Formulario.ExibeMensagem(
            "Não foi possível consultar a matrícula {0}: {1}".format(
                matricula,
                Texto(ex)
            )
        )
```
    - coluna UOR

### [360131] EventoFinal ""
Config: TipoFinalizacao=NaoRealizado

### [360132] EventoIntermediarioMensagem "Comunica reprovação"
Destinatário: Cliente (papel 18)
ModeloComunicado: Comunicado GEPES
Corpo do comunicado: Complemento1 
 Complemento2 
 Complemento3 
 Complemento4 
 Complemento5
**ScriptEvento**
```python
#Mensagem.Destinatarios.Add(OrdemServico["CSC_EMAIL_PESSOAL"])
Mensagem.Assunto = "Validar Eixo Pedagógico e demais insumos - Aprovado " 

motivo = OrdemServico.ObtemMotivoReprovacao("APROVAEIXO").ToString()

Mensagem.Complemento1 = "Prezados, " + OrdemServico.Cliente.Nome +"<br><Br>Gostaria de informar que, conforme solicitado, o eixo pedagógico e demais insumos não foi aprovado pelo motivo: " +  motivo.ToString() + ".<br>Gentileza realizar os ajustes solicitados e abrir nova ordem de serviço com os insumos revisados e atualizados.<br><br>Atenciosamente,<br><Br>"
```

### [360133] EventoIntermediarioMensagem "Comunica aprovação"
Destinatário: Cliente (papel 18)
ModeloComunicado: Comunicado GEPES
Corpo do comunicado: Complemento1 
 Complemento2 
 Complemento3 
 Complemento4 
 Complemento5
**ScriptEvento**
```python
#Mensagem.Destinatarios.Add(OrdemServico["CSC_EMAIL_PESSOAL"])
Mensagem.Assunto = "Validação de Eixo Pedagógico e demais insumos - Aprovado " 
Mensagem.Complemento1 = "Prezados, " + OrdemServico.Cliente.Nome +"<br><Br>Gostaria de informar que, conforme solicitado, o eixo pedagógico e demais insumos foram aprovados. <br><br>Atenciosamente,<br><Br>Central de Serviços"
```

## Papéis usados
### papel 188: Fila Treinamento
Tipo=RelacaoPessoas | pessoas: Fila Treinamento
### papel 17: Gestor do Serviço
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.Servico.ResponsávelArea
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Servico.ResponsavelArea, "Pessoa cadastrada como responsável pelo Serviço '" + OrdemServico.Servico.Descricao + "' na área de negócio")
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

### LISTA_DE_PESSOAS — Lista de Favorecidos
DataGrid RecordList → Z_00143_LISTA_DE_PESSOAS.LISTA_DE_PESSOAS
Colunas do registro:
- NOME "Nome Colaborador" [DropDownList String]
**NOME.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE f.status_matricula = 'Ativo' AND p.ativo = 'Sim' order by nomemat")
```
- MATRICULA "MATRICULA" [TextBox String]
- UOR "UOR" [TextBox String]

### TE_DT_INICIO — Data inicial
DatePicker DateTime → CPE_CSC.TE_DT_INICIO

### SCR_TODOS_RH — UOR Movimentação
DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH
Descrição: SCR Movimentação
**LookupScript**
```python
###PGESV###
Itens = DB.ExecuteDataTable("SELECT to_char(SCR) as SCR, NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO");
```

### TE_CURSO — Nome do curso/ evento
TextBox String → CPE_CSC.TE_CURSO

### NOME_PROJETO — Nome do Projeto
TextBox String → CP_ORDEM_SERVICO.NOME_PROJETO

### COMBOBOX1 — Chamado Aberto?
DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX
Itens: Órtese;Órtese Dentária; Prótese;Recurso para Saúde

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
