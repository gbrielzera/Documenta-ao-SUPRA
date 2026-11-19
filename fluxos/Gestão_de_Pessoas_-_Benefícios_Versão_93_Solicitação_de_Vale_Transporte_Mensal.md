# Fluxo: Solicitação de Vale Transporte Mensal (SOLVALETRANSPDIA) — versão 93
Caminho: Fluxos > Gestão de Pessoas - Benefícios Versão 93 Solicitação de Vale Transporte Mensal
XML: `XMLs para teste/Gestão_de_Pessoas_-_Benefícios_Versão_93_Solicitação_de_Vale_Transporte_Mensal.xml` | Supravizio 19.1.1 | SubProcessoId 23440 | DesenhoProcessoId 3125 | ProcessoId 105
Órgão dono: 3000003210 - DIVISAO DE BENEFICIOS E MOVIMENTACOES DE PESSOAL | Responsável: PALOMA SABINE AMADO ROSA VARGAS
Classe do subprocesso: Objetivo=Fluxo para os gestores informarem os funcionários e quantidade de vale transporte.
Será aceito no máximo 44 vales por mês; DescricaoCliente=Solicitação de Vale Transporte Mensal; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Fluxo para os gestores informarem os funcionários e quantidade de vale transporte.Será aceito no máximo 44 vales por mês; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Solicitação de Vale Transporte Mensal (SOLVTMENSAL)

## Grafo do fluxo
- [374175] EventoIntermediarioMensagem "Notificar abertura do chamado para aprovação" → [374181] Solicitar aprovação do Gerente Imediato
- [374176] FimCancelamento "" {Sistema} → (fim)
- [374177] EventoIntermediarioMensagem "Notificar inatividade do chamado" → [374182] 
- [374178] EventoFinal "" {Sistema} → (fim)
- [374179] EventoIntermediarioMensagem "Notificar reprovação gerencial" → [374176] 
- [374180] EventoIntermediarioTimer "" → [374177] Notificar inatividade do chamado
- [374181] Tarefa "Solicitar aprovação do Gerente Imediato" {Gerente Posição do Cliente} → [374180]  | [G83642] Gerente aprovou?
- [374182] EventoFinal "" {Sistema} → (fim)
- [374183] EventoInicial "Solicitação de Vale Transporte Mensal" → [374175] Notificar abertura do chamado para aprovação
- [374184] EventoIntermediarioMensagem "Notificar conclusão do serviço" → [374178] 
- [G83642] Gateway "Gerente aprovou?" → «Sim» [374184] Notificar conclusão do serviço | «Não» [374179] Notificar reprovação gerencial

## Gateways
### [G83642] Gerente aprovou? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAR")
```
- alternativa → [374184] Notificar conclusão do serviço: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [374179] Notificar reprovação gerencial: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [374175] EventoIntermediarioMensagem "Notificar abertura do chamado para aprovação"
Destinatário: Cliente e Gerente Posição (papel 631)
ModeloComunicado: Aviso abertura de chamado Solicitação de Vale Transporte Mensal para aprovação
Corpo do comunicado: Prezado(a),
A ordem de serviço n° OrdemServico.Numero - OrdemServico.Servico , está pendente de aprovação.
Essa solicitação ficará disponível para aprovação por até 5 (cinco) dias úteis.
Após este período, caso não haja aprovação, a ordem de serviço será automaticamente cancelada.
O processamento da ordem de serviço só ocorrerá após aprovação do gestor(a) ou seu substituto(a).
Solicitações abertas e aprovadas após o dia 18 terão impacto na folha de pagamento do mês subsequente, quando o pagamento do item será efetuado.
Usuario solicitante: OrdemServico.Cliente 
Para obter mais informações e efetuar sua aprovação Link.Consulta. 
Central de Serviços

### [374176] FimCancelamento ""
Responsável: Sistema (papel 1)

### [374177] EventoIntermediarioMensagem "Notificar inatividade do chamado"
Destinatário: Cliente e Gerente Posição (papel 631)
ModeloComunicado: Aviso sobre cancelamento do chamado - 120 horas sem resposta
Corpo do comunicado: Prezado(a),
O chamado interno OrdemServico.Numero - OrdemServico.Assunto foi cancelado, pois aguardou por 120 horas sem aprovação do gestor. Favor abrir outra solicitação caso necessário.
Atenciosamente,
Central de Serviços

### [374178] EventoFinal ""
Responsável: Sistema (papel 1)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [374179] EventoIntermediarioMensagem "Notificar reprovação gerencial"
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de Serviço - Reprovação Solicitação Vale Transporte por Dia
Corpo do comunicado: Prezado(a),
Informamos que sua solicitação de Vale Transporte Mensal foi reprovado pelo seu Gestor.
Para maiores informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [374180] EventoIntermediarioTimer ""
Config: TempoIntervalo=7200; MaximoExecucao=1

### [374181] Tarefa "Solicitar aprovação do Gerente Imediato"
Responsável: Gerente Posição do Cliente (papel 563)
Config: Codigo=APROVAR
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Solicitar aprovação do Gerente Imediato; ReprovarImediato=true; ReenvioEmailAprovacao=24
  - (aprovação) LABEL11 "ATENÇÃO" [Label String(700) → CPE_PDCI2019.LABEL11]
  - (aprovação) LABEL10 "ATENÇÃO" [Label String(700) → CPE_PDCI2019.LABEL10]
  - (aprovação) TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO]
  - (aprovação) LABEL1 "IMPORTANTE" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - (aprovação) MES_REFERENCIA "Mês referência" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA]
  - (aprovação) TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR]
  - (aprovação) NUM_SEQ "Quantidade de dias trabalhados presencialmente" [TextBox String(250) → CP_ORDEM_SERVICO.NUM_SEQ]
  - (aprovação) TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
  - (aprovação) ANO_REF "Ano referência" [DropDownList String(4) → CPE_CSC.ANO_REF]
  - (aprovação) TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO]
  - (aprovação) TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO]
  - aprovador: Gerente Posição do Cliente (Unico)

### [374182] EventoFinal ""
Responsável: Sistema (papel 1)
Config: TipoFinalizacao=NaoRealizado

### [374183] EventoInicial "Solicitação de Vale Transporte Mensal"
Config: Configuracao={"ServicoIniciador":"<Nenhum>"}
TipoSolicitacao: 20.01. Gestão de Pessoas - Benefícios
**ScriptValidacao**
```python
if Convert.ToInt32(OrdemServico["NUM_SEQ"]) >= 32:
    Criticas.AdicionaPendencia('A solicitação do auxílio vale transporte está limitada a 31 dias por mês.')
    
#if OrdemServico["ANO_REF"] == DateTime.Now.ToString("yyyy") and OrdemServico["MES_REFERENCIA"] >= DateTime.Now.ToString("MM") or OrdemServico["ANO_REF"] > DateTime.Now.ToString("yyyy") and OrdemServico["MES_REFERENCIA"] > DateTime.Now.ToString("MM"):
    #Criticas.AdicionaPendencia("Não é permitido solicitações para o mês corrente e meses futuros. Verifique sua solicitação e tente novamente.")


queryAdesao = DB.ExecuteDataTable("select cp.ID_PESSOA, cp.matricula, cp.matricula||' - '||p.nome from pessoa p inner join cp_pessoa cp on p.id_pessoa = cp.id_pessoa inner join orgao o on p.id_orgao = o.id_orgao inner join funcionario_beneficios_v fbv on fbv.id_funcionario = cp.matricula where cp.ID_PESSOA = '"+OrdemServico["TE_NOME_EMPREGADO"] + "' and p.ativo = 'Sim' and o.ativo = 'Sim' and p.tipo <> 'Fila' and fbv.COD_PLANO = 'A70001'")

if  queryAdesao.Rows.Count == 0:
    Criticas.AdicionaPendencia("A concessão do benefício Vale Transporte / Tele Trabalho está condicionada a adesão da opção do vale transporte. Não identificamos ordem de serviço finalizada com sucesso para opção do beneficio de vale transporte. Realize a abertura da ordem de serviço de opção do vale transporte, aguarde a sua conclusão para posterior solicitação do benefício.") 
    
#--------------------
#Criticar abertura de chamados retroativos limitados até 3 meses/
#Não permitir lançamento posterior ao ano subsequente ao vigente
#Não permitir abertura de chamado com mês de referência superior a um em relação am mês vigente. 
mesAtual = Convert.ToInt32(DateTime.Now.ToString("MM"))
mesDeclarado = Convert.ToInt32(OrdemServico.GetCustom("MES_REFERENCIA"))

anoAtual = Convert.ToInt32(DateTime.Now.ToString("yyyy"))
anoDeclarado = Convert.ToInt32(OrdemServico.GetCustom("ANO_REF"))

today = DateTime.Now;
prevDate = DateTime(anoDeclarado, mesDeclarado, 01)

#if anoDeclarado == anoAtual and mesDeclarado > (mesAtual + 1) or anoDeclarado > anoAtual and mesDeclarado > (mesAtual + 1):
    #Criticas.AdicionaPendencia("Só é permitido aberturas para o mês atual e o subsequente.")
    
#if anoDeclarado > anoAtual:
    #Criticas.AdicionaPendencia("Não é permitido lançamentos para o ano subsequente ou posterior")

diffOfDates = ((today.Year - prevDate.Year) * 12) + today.Month - prevDate.Month

if diffOfDates >= 3:
    Criticas.AdicionaPendencia("A abertura retroativa está limitada a até 3 meses a partir do mês atual.")
    
    
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
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["FAVORECIDO_TODOS"].Visivel = False
Formulario["FAVORECIDO_TODOS"].Habilitado = False
Formulario["FAVORECIDO_COBRA"].Visivel = False
Formulario["FAVORECIDO_COBRA"].Habilitado = False



Formulario['TE_NOME_EMPREGADO'].Habilitado = False
Formulario['TE_NOME_EMPREGADO'].Visivel = True


OrdemServico.Assunto = OrdemServico.Servico.DescricaoCliente

Formulario["TE_MATRICULA"].Visivel = False
Formulario["TE_CARGO"].Visivel = False
Formulario["TE_FUNCAO"].Visivel = False
Formulario["TE_UOR"].Visivel = False

Formulario["TE_MATRICULA"].Habilitado = False
Formulario["TE_CARGO"].Habilitado = False
Formulario["TE_FUNCAO"].Habilitado = False
Formulario["TE_UOR"].Habilitado = False

Formulario['TE_NOME_EMPREGADO'].Valor = DB.ExecuteScalar("SELECT DISTINCT TO_CHAR(p.id_pessoa) AS id_pessoa, p.nome || ' (' || p.usuario_rede || ')' AS nomemat, cp.matricula, p.ativo FROM pessoa p inner join cp_pessoa cp on cp.id_pessoa = p.id_pessoa WHERE TIPO_COLABORADOR = 'Empregado' AND p.ativo = 'Sim' AND p.id_pessoa = '"+OrdemServico.ClienteId.ToString()+"'")

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
  - OPCAO_DE_CONFIRMACAO "Declaro que estou ciente das regras de uso do vale transporte." [CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO] obrigatório
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - OBS10 "Observação:" [Memo String(2000) → CPE_CSC.OBS10]
  - LABEL10 "As solicitações podem ser abertas retroativamente ou para o mês subsequente." [Label String(700) → CPE_PDCI2019.LABEL10]
  - FAVORECIDO_TODOS "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
**FAVORECIDO_TODOS.ScriptModificado**
```python
Formulario["FAVORECIDO_TODOS"].Visivel = False
Formulario["FAVORECIDO_TODOS"].Habilitado = False
```
  - LABEL1 "A solicitação de Vale Transporte, deve ser proporcional aos dias de trabalho presencial na Empresa." [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
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
  - TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO] obrigatório
  - TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO]
  - FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
**FAVORECIDO_COBRA.ScriptModificado**
```python
Formulario["FAVORECIDO_COBRA"].Visivel = False
Formulario["FAVORECIDO_COBRA"].Habilitado = False
```
  - NUM_SEQ "Quantidade de dias a trabalhar presencialmente." [TextBox String(250) → CP_ORDEM_SERVICO.NUM_SEQ] obrigatório
  - MES_REFERENCIA "Mês referência" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA] obrigatório
  - ANO_REF "Ano referência" [DropDownList String(4) → CPE_CSC.ANO_REF] obrigatório
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório

### [374184] EventoIntermediarioMensagem "Notificar conclusão do serviço"
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de serviço - Aprovação Solicitação Vale Transporte por Dia
Corpo do comunicado: Prezado (a),
Informamos que a sua Solicitação Vale Transporte Mensal foi aprovada pelo seu Gestor. Em breve o benefício será creditado.
Para maiores informações Link.Consulta 
Atenciosamente,
Central de Serviços

## Papéis usados
### papel 631: Cliente e Gerente Posição
Tipo=Composto
- composto por: Gerente Posição do Cliente (Script)
- composto por: Cliente (PessoaOrdemServico)
### papel 1: Sistema
Tipo=RelacaoPessoas | pessoas: Sistema
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
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

## Campos customizados usados (definição global)

### LABEL11 — LABEL11
Label String(700) → CPE_PDCI2019.LABEL11

### LABEL10 — LABEL10
Label String(700) → CPE_PDCI2019.LABEL10

### TE_FUNCAO — Função
TextBox String → CPE_CSC.TE_FUNCAO

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### MES_REFERENCIA — Mês referência
DropDownList String(2) → CPE_CSC.MES_REFERENCIA
Itens: 01;02;03;04;05;06;07;08;09;10;11;12

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

### NUM_SEQ — Número sequencial
TextBox String(250) → CP_ORDEM_SERVICO.NUM_SEQ
Descrição: Número constante do Registro de Constatação. Cada recomendação tem seu próprio número. O número das recomendações emitidas a partir de 2023 possuem 9 dígitos.

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### ANO_REF — Ano referência
DropDownList String(4) → CPE_CSC.ANO_REF
Itens: 2027;2026;2025

### TE_CARGO — Cargo
TextBox String → CPE_CSC.TE_CARGO

### TE_NOME_EMPREGADO — Nome do empregado
DropDownList String → CPE_CSC.TE_NOME_EMPREGADO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### OPCAO_DE_CONFIRMACAO — Campo confirma uma afirmação
CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO
Descrição: Campo genérico para confirmação de uma afirmação

### OBS10 — Observação10
Memo String(2000) → CPE_CSC.OBS10

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

## Biblioteca de scripts referenciada
teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
