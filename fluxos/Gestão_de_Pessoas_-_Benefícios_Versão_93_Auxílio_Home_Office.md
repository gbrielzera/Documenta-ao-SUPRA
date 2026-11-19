# Fluxo: Auxílio Home Office (AUXILIOHOMEOFFICE) — versão 93
Caminho: Fluxos > Gestão de Pessoas - Benefícios Versão 93 Auxílio Home Office
XML: `XMLs para teste/Gestão_de_Pessoas_-_Benefícios_Versão_93_Auxílio_Home_Office.xml` | Supravizio 19.1.1 | SubProcessoId 23416 | DesenhoProcessoId 3125 | ProcessoId 105
Órgão dono: 3000003210 - DIVISAO DE BENEFICIOS E MOVIMENTACOES DE PESSOAL | Responsável: PALOMA SABINE AMADO ROSA VARGAS
Classe do subprocesso: Objetivo=Auxílio Home Office; DescricaoCliente=Auxílio Home Office; MetodoPriorizacaoId=2; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorResponsavel; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Auxilio Home Office (AUXHOMEOFFICE)

## Grafo do fluxo
- [373884] EventoFinal "" {Sistema} → (fim)
- [373885] LinkInicial "Chatbot" → [373888] Notifica abertura do chamado
- [373886] Tarefa "Solicitar aprovação do Gerente Imediato" {Gerente Posição do Cliente} → [373894]  | [G83593] Gestor aprovou?
- [373887] EventoIntermediarioMensagem "Notificar inatividade do chamado" → [373884] 
- [373888] EventoIntermediarioMensagem "Notifica abertura do chamado" → [373886] Solicitar aprovação do Gerente Imediato
- [373889] FimCancelamento "" {Sistema} → (fim)
- [373890] EventoFinal "" {Sistema} → (fim)
- [373891] EventoIntermediarioMensagem "Notificação reprovação gerencial" {Fila CSC - Benefícios} → [373889] 
- [373892] EventoIntermediarioMensagem "Notificar conclusão do serviço" {Fila CSC - Benefícios} → [373890] 
- [373893] EventoInicial "Auxílio Home Office" → [373886] Solicitar aprovação do Gerente Imediato
- [373894] EventoIntermediarioTimer "" → [373887] Notificar inatividade do chamado
- [G83593] Gateway "Gestor aprovou?" → «Sim» [373892] Notificar conclusão do serviço | «Não» [373891] Notificação reprovação gerencial

## Gateways
### [G83593] Gestor aprovou? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAR")
```
- alternativa → [373892] Notificar conclusão do serviço: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [373891] Notificação reprovação gerencial: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [373884] EventoFinal ""
Responsável: Sistema (papel 1)
Config: TipoFinalizacao=NaoRealizado

### [373885] LinkInicial "Chatbot"
Config: TipoMensagem=MensagemProcesso
- Associação de subprocesso: AssociacaoId=574; Nome=ADIR CORDEIRO DOS SANTOS FILHO; FraseAssociacao=Chatbot -> Auxilio Home Office

### [373886] Tarefa "Solicitar aprovação do Gerente Imediato"
Responsável: Gerente Posição do Cliente (papel 563)
Config: Codigo=APROVAR
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Solicitar aprovação do Gerente Imediato; ReprovarImediato=true; ReenvioEmailAprovacao=12
  - (aprovação) TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO]
  - (aprovação) TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR]
  - (aprovação) LABEL10 "ATENÇÃO" [Label String(700) → CPE_PDCI2019.LABEL10]
  - (aprovação) TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO]
  - (aprovação) DIAS_DE_TRA "DIAS DE TRAB" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA]
  - (aprovação) MES_REFERENCIA "Mês referência" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA]
  - (aprovação) LABEL1 "IMPORTANTE" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - (aprovação) ANO_REF "Ano referência" [DropDownList String(4) → CPE_CSC.ANO_REF]
  - (aprovação) TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO]
  - (aprovação) TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
  - (aprovação) LABEL11 "ATENÇÃO" [Label String(700) → CPE_PDCI2019.LABEL11]
  - aprovador: Gerente Posição do Cliente (Unico)

### [373887] EventoIntermediarioMensagem "Notificar inatividade do chamado"
Destinatário: Cliente e Gerente Posição (papel 631)
ModeloComunicado: Aviso sobre cancelamento do chamado - 36 horas sem resposta
Corpo do comunicado: Prezado(a),
 O chamado interno OrdemServico.Numero - OrdemServico.Assunto foi cancelado, pois aguardou por 36 horas sem aprovação do gestor. Favor abrir outra solicitação caso necessário.
Atenciosamente,
Central de Serviços

### [373888] EventoIntermediarioMensagem "Notifica abertura do chamado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Aviso de abertura de chamado - 1
Corpo do comunicado: Prezado(a),
Foi aberta a ordem de serviço n°: OrdemServico.Numero referente ao serviço OrdemServico.Servico .
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [373889] FimCancelamento ""
Responsável: Sistema (papel 1)

### [373890] EventoFinal ""
Responsável: Sistema (papel 1)

### [373891] EventoIntermediarioMensagem "Notificação reprovação gerencial"
Responsável: Fila CSC - Benefícios (papel 524)
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de Serviço - Reprovação Auxílio Home Office
Corpo do comunicado: Prezado(a),
Informamos que sua solicitação de auxílio home office foi reprovado pelo seu Gestor.
Para maiores informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [373892] EventoIntermediarioMensagem "Notificar conclusão do serviço"
Responsável: Fila CSC - Benefícios (papel 524)
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de Serviço - Aprovação Auxílio Home Office
Corpo do comunicado: Prezado(a),
Informamos que o auxílio home office foi aprovado pelo seu Gestor. Em breve o benefício será creditado. 
Para maiores informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [373893] EventoInicial "Auxílio Home Office"
TipoSolicitacao: 20.01. Gestão de Pessoas - Benefícios
**ScriptValidacao**
```python
#if Convert.ToInt32(OrdemServico["DIAS_DE_TRA"]) >= 24:
#    Criticas.AdicionaPendencia('A solicitação do auxílio home office está limitada a 23 dias por mês.')
    
    
if (OrdemServico.GetCustom("DEC_AUX_HOM")  == False) :
    Criticas.AdicionaPendencia("A declaração das condições do auxílio home office é um campo obrigatório")
    
if (OrdemServico["ANO_REF"] == DateTime.Now.ToString("yyyy") and OrdemServico["MES_REFERENCIA"] >= DateTime.Now.ToString("MM"))  or (OrdemServico["ANO_REF"] > DateTime.Now.ToString("yyyy")):# or (OrdemServico["MES_REFERENCIA"] > DateTime.Now.ToString("MM")):
    Criticas.AdicionaPendencia("Não é permitido solicitações para o mês corrente e meses futuros. Verifique sua solicitação e tente novamente.")
    
    
#if (OrdemServico["MES_REFERENCIA"] < DateTime.AddDays(DateTime.Now, -90).ToString("MM")):
#    Criticas.AdicionaPendencia("Não são permitidas solicitações com datas anteriores a dois meses do mês referência. Verifique sua solicitação e tente novamente.")

#Verificação mes referencia abaixo em 03/02/2025- Adir + Rramos. O segmento acima dava erro ao abrir chamados para janeiro.

if (Convert.ToDateTime("01" + "/" + OrdemServico["MES_REFERENCIA"].ToString() + "/" + DateTime.Now.Year.ToString()) <= DateTime.AddDays(DateTime.Now, -90)):
    Criticas.AdicionaPendencia("Não são permitidas solicitações com datas anteriores a dois meses do mês referência. Verifique sua solicitação e tente novamente.")
    
    
if (OrdemServico["ANO_REF"] > DateTime.Now.ToString("yyyy")):
    Criticas.AdicionaPendencia("Não é permitida solicitação para anos posteriores ao ano de referência. Verifique sua solicitação e tente novamente.")
    
#--------------------
#Consulta OS de Adesão ao Teletrabalho
queryAdesao = DB.ExecuteDataTable("Select OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, PESSOA.NOME From OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = OCORRENCIA.ID_CLIENTE Where OCORRENCIA.ASSUNTO = 'Home Office Híbrido' AND PESSOA.ID_PESSOA = '"+OrdemServico["TE_NOME_EMPREGADO"] + "' AND OCORRENCIA.SITUACAO = 'FinalizadaSucesso'")


if queryAdesao.Rows.Count == 0:
    Criticas.AdicionaPendencia("A concessão do benefício auxílio home office está condicionada a adesão ao teletrabalho. Não identificamos ordem de serviço finalizada com sucesso para adesão dessa modalidade de trabalho em seu nome. Realize a abertura da ordem de serviço de adesão, aguarde a sua conclusão para posterior solicitação do benefício.")
    
numero = "0"
if (OrdemServico.Numero.ToString()!= ""):
    numero = OrdemServico.Numero.ToString()
    
    
#verifica se existe chamado aberto para a competência atual
sql = " SELECT COUNT(*) AS CONTADOR, O.NUMERO FROM OCORRENCIA O INNER JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) INNER JOIN PESSOA F ON (O.Id_Cliente = F.ID_PESSOA) INNER JOIN CPE_CSC c on ( c.id_ocorrencia = o.id_ocorrencia ) WHERE S.ID_SERVICO = '"+ OrdemServico.ServicoId.ToString() +"' AND (O.SITUACAO = 'Aberto' or O.SITUACAO = 'FinalizadaSucesso') AND O.NUMERO <> '"+ numero +"' AND F.ID_PESSOA = '"+ OrdemServico.Cliente.Id.ToString() + "' and c.MES_REFERENCIA = '"+ OrdemServico["MES_REFERENCIA"].ToString() + "' and c.ANO_REF = '" + OrdemServico["ANO_REF"].ToString() +"' GROUP BY O.NUMERO"

#Criticas.AdicionaPendencia(sql)

lista = Utils.ExecuteDataTable(sql) 

numeroRegistro = 0
osNumero = 0
    
for linha in lista.Rows:
    numeroRegistro = linha["CONTADOR"]
    osNumero = linha["NUMERO"]

if (numeroRegistro >= 1):
    Criticas.AdicionaPendencia("Já existe um chamado aberto para a competência solicitada " + osNumero) 
    

#lista = Utils.ExecuteDataTable(" SELECT COUNT(*) AS CONTADOR FROM OCORRENCIA O INNER JOIN ORDEM_SERVICO OS ON (O.ID_OCORRENCIA = OS.ID_OCORRENCIA) INNER JOIN SERVICO S ON (OS.ID_SERVICO = S.ID_SERVICO) INNER JOIN CP_ORDEM_SERVICO CPOS ON (O.ID_OCORRENCIA = CPOS.ID_OCORRENCIA) INNER JOIN PESSOA F ON (O.Id_Cliente = F.ID_PESSOA) WHERE S.ID_SERVICO = '"+ OrdemServico.ServicoId.ToString() +"' AND O.SITUACAO = 'FinalizadaSucesso' AND O.NUMERO <> '"+ numero +"' AND F.ID_PESSOA = '"+ OrdemServico.Cliente.Id.ToString() + "'") 
#    
#for linha in lista.Rows:
#    numeroRegistro = linha["CONTADOR"]
#
#if (numeroRegistro >= 1):
#    Criticas.AdicionaPendencia("Adesão já realizada e aprovada pela Gepes!") 
#    
#queryAdesaoAberta = DB.ExecuteDataTable("Select OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, PESSOA.NOME From OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = OCORRENCIA.ID_CLIENTE Where OCORRENCIA.ASSUNTO = 'Home Office Híbrido' AND PESSOA.ID_PESSOA = '"+OrdemServico["TE_NOME_EMPREGADO"] + "' OCORRENCIA.SITUACAO = 'Aberta'")
#
#if queryAdesaoAberta.Rows.Count != 0 and queryAdesao.Rows.Count == 0:
#    Criticas.AdicionaPendencia("Existe uma OS em aberto.")
#
#
#queryAdesaoCancelada = DB.ExecuteDataTable("Select OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, PESSOA.NOME From OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = OCORRENCIA.ID_CLIENTE Where OCORRENCIA.ASSUNTO = 'Home Office Híbrido' AND PESSOA.ID_PESSOA = '"+OrdemServico["TE_NOME_EMPREGADO"] + "' OCORRENCIA.SITUACAO = 'Cancelada'")
#
#if queryAdesaoCancelada.Rows.Count != 0 and queryAdesao.Rows.Count == 0:
#    Criticas.AdicionaPendencia("Existe uma OS em cancelada.")
#
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["FAVORECIDO_TODOS"].Visivel = False
Formulario["FAVORECIDO_TODOS"].Habilitado = False
Formulario["FAVORECIDO_COBRA"].Visivel = False
Formulario["FAVORECIDO_COBRA"].Habilitado = False



Formulario['TE_NOME_EMPREGADO'].Habilitado = False

OrdemServico.Assunto = OrdemServico.Servico.DescricaoCliente

Formulario["TE_MATRICULA"].Visivel = False
Formulario["TE_CARGO"].Visivel = False
Formulario["TE_FUNCAO"].Visivel = False
Formulario["TE_UOR"].Visivel = False

Formulario["TE_MATRICULA"].Habilitado = False
Formulario["TE_CARGO"].Habilitado = False
Formulario["TE_FUNCAO"].Habilitado = False
Formulario["TE_UOR"].Habilitado = False

Formulario['TE_NOME_EMPREGADO'].Valor = OrdemServico.ClienteId.ToString()

matricula = ""
cargo = ""
funcao = ""
uor = ""


if Formulario["TE_NOME_EMPREGADO"].Valor != "" or Formulario["TE_NOME_EMPREGADO"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["TE_NOME_EMPREGADO"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["TE_UOR"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable(" SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )

    for linha in lista.Rows:
        cargo = linha["CARGO"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()
        uor = linha["DESCRICAO"].ToString()

    Formulario["TE_CARGO"].Valor = cargo.ToString()
    Formulario["TE_FUNCAO"].Valor = funcao.ToString()
    #Formulario["DESC_COLABORADOR"].Valor = desc_colaborador.ToString()
    Formulario["TE_MATRICULA"].Valor = matricula.ToString()
    Formulario["TE_UOR"].Valor = uor.ToString()
    
    Formulario["TE_MATRICULA"].Visivel = True
    Formulario["TE_CARGO"].Visivel = True
    Formulario["TE_FUNCAO"].Visivel = True
    Formulario["TE_UOR"].Visivel = True
```
- Operação PR0001 Preencher Campos
  - LABEL1 "A solicitação do Auxílio Home Office, deve ser proporcional aos dias úteis trabalhados, conforme os dados preenchidos neste chamado." [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - DEC_AUX_HOM "Estou ciente das condições previstas no regulamento do Auxílio Home Office para a requisição do benefício, bem como declaro usufrui-lo especificamente para a finalidade proposta." [CheckBox Boolean → CPE_PESSOAS.DEC_AUX_HOM] obrigatório
  - TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO] obrigatório
**TE_NOME_EMPREGADO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["TE_MATRICULA"].Visivel = True
Formulario["TE_CARGO"].Visivel = True
Formulario["TE_FUNCAO"].Visivel = True
Formulario["TE_UOR"].Visivel = True

Formulario["TE_MATRICULA"].Habilitado = False
Formulario["TE_CARGO"].Habilitado = False
Formulario["TE_FUNCAO"].Habilitado = False
Formulario["TE_UOR"].Habilitado = False

Formulario["TE_MATRICULA"].Valor = None
Formulario["TE_CARGO"].Valor = None
Formulario["TE_FUNCAO"].Valor = None
Formulario["TE_UOR"].Valor = None

matricula = ""
cargo = ""
funcao = ""
uor = ""

if Formulario["TE_NOME_EMPREGADO"].Valor != "" or Formulario["TE_NOME_EMPREGADO"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["TE_NOME_EMPREGADO"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["TE_UOR"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )

    for linha in lista.Rows:
        cargo = linha["CARGO"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()
        uor = linha["DESCRICAO"].ToString()

    Formulario["TE_CARGO"].Valor = cargo.ToString()
    Formulario["TE_FUNCAO"].Valor = funcao.ToString()
    #Formulario["DESC_COLABORADOR"].Valor = desc_colaborador.ToString()
    Formulario["TE_MATRICULA"].Valor = matricula.ToString()
    Formulario["TE_UOR"].Valor = uor.ToString()
```
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório
  - MES_REFERENCIA "Mês referência" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA] obrigatório
  - ANO_REF "Ano referência" [DropDownList String(4) → CPE_CSC.ANO_REF] obrigatório
  - FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
**FAVORECIDO_COBRA.ScriptModificado**
```python
Formulario["FAVORECIDO_COBRA"].Visivel = False
Formulario["FAVORECIDO_COBRA"].Habilitado = False
```
  - TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO] obrigatório
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - DIAS_DE_TRA "Quantidade de dias trabalhados em home office (em casa):" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA] obrigatório
  - TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO]
  - LABEL27 "<b style="color: red">Atenção a quantidade de dia  presencial!</b>" [Label String(700) → CPE_PDCI2019.LABEL27] obrigatório
  - NUM_SEQ "Quantidade de dias trabalhados presencialmente na BBTS (na Empresa):" [TextBox String(250) → CP_ORDEM_SERVICO.NUM_SEQ] obrigatório
  - LABEL20 "O benefício tem caráter indenizatório, excepcional e temporário, e fará jus os empregados que estiverem laborando na modalidade Home Office. O auxílio está limitado a R$90,00 (noventa reais)." [Label String(500) → CPE_PDCI2019.LABEL20] obrigatório
  - LABEL10 "As solicitações não podem ser abertas para o mês corrente ou meses futuros." [Label String(700) → CPE_PDCI2019.LABEL10]
  - LABEL11 "Caso haja mais de uma solicitação para o mesmo mês, somente será considerada a última solicitação aprovada pelo Gestor do empregado." [Label String(700) → CPE_PDCI2019.LABEL11]
  - FAVORECIDO_TODOS "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
**FAVORECIDO_TODOS.ScriptModificado**
```python
Formulario["FAVORECIDO_TODOS"].Visivel = False
Formulario["FAVORECIDO_TODOS"].Habilitado = False
```

### [373894] EventoIntermediarioTimer ""
Config: TempoIntervalo=5760; MaximoExecucao=1

## Papéis usados
### papel 1: Sistema
Tipo=RelacaoPessoas | pessoas: Sistema
### papel 563: Gerente Posição do Cliente
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.ClienteId))
#gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select cp.ID_PESSOA from CP_PESSOA cp inner join pessoa p on cp.id_pessoa = p.id_pessoa and p.ativo = 'Sim' WHERE MATRICULA = substr('"+favorecido["GESTOR_POSICAO"].ToString()+"',1,6)")))

gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
Atores.Adiciona(gestor)
```
### papel 631: Cliente e Gerente Posição
Tipo=Composto
- composto por: Gerente Posição do Cliente (Script)
- composto por: Cliente (PessoaOrdemServico)
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 524: Fila CSC - Benefícios
Tipo=RelacaoPessoas | pessoas: Fila CSC - Benefícios
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
pessoa = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))
atores = OrdemServico.ObtemAtoresProcesso('Fila CSC - Benefícios')
for ator in atores:
    if ator != pessoa:
        Atores.Adiciona(ator)
```

## Campos customizados usados (definição global)

### TE_FUNCAO — Função
TextBox String → CPE_CSC.TE_FUNCAO

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

### LABEL10 — LABEL10
Label String(700) → CPE_PDCI2019.LABEL10

### TE_CARGO — Cargo
TextBox String → CPE_CSC.TE_CARGO

### DIAS_DE_TRA — DIAS DE TRAB
TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA
Descrição: DIAS DE TRABALHO

### MES_REFERENCIA — Mês referência
DropDownList String(2) → CPE_CSC.MES_REFERENCIA
Itens: 01;02;03;04;05;06;07;08;09;10;11;12

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### ANO_REF — Ano referência
DropDownList String(4) → CPE_CSC.ANO_REF
Itens: 2027;2026;2025

### TE_NOME_EMPREGADO — Nome do empregado
DropDownList String → CPE_CSC.TE_NOME_EMPREGADO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### LABEL11 — LABEL11
Label String(700) → CPE_PDCI2019.LABEL11

### DEC_AUX_HOM — declaração auxilio home
CheckBox Boolean → CPE_PESSOAS.DEC_AUX_HOM
Descrição: declaração auxilio home 

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### LABEL27 — LABEL27
Label String(700) → CPE_PDCI2019.LABEL27

### NUM_SEQ — Número sequencial
TextBox String(250) → CP_ORDEM_SERVICO.NUM_SEQ
Descrição: Número constante do Registro de Constatação. Cada recomendação tem seu próprio número. O número das recomendações emitidas a partir de 2023 possuem 9 dígitos.

### LABEL20 — LABEL20
Label String(500) → CPE_PDCI2019.LABEL20

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

## Biblioteca de scripts referenciada
teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
