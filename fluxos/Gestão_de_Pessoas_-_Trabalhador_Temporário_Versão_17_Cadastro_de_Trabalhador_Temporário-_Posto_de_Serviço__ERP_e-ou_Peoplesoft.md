# Fluxo: Cadastro de Trabalhador Temporário/ Posto de Serviço (ERP e/ou Peoplesoft) (GPESSOASTEMPORARIO) — versão 17
Caminho: Fluxos > Gestão de Pessoas - Trabalhador Temporário Versão 17 Cadastro de Trabalhador Temporário- Posto de Serviço (ERP e-ou Peoplesoft)
XML: `XMLs para teste/Gestão_de_Pessoas_-_Trabalhador_Temporário_Versão_17_Cadastro_de_Trabalhador_Temporário-_Posto_de_Serviço_(ERP_e-ou_Peoplesoft).xml` | Supravizio 19.1.1 | SubProcessoId 23249 | DesenhoProcessoId 3111 | ProcessoId 121
Órgão dono: 3000003210 - DIVISAO DE BENEFICIOS E MOVIMENTACOES DE PESSOAL | Responsável: PALOMA SABINE AMADO ROSA VARGAS
Classe do subprocesso: Objetivo=Cadastro de Trabalhador Temporário/ Posto de Serviço (ERP e/ou Peoplesoft); DescricaoCliente=Cadastro de Trabalhador Temporário/ Posto de Serviço (ERP e/ou Peoplesoft); CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadoresGrupoEnvolvido; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Desligamento de Trabalhador Temporário (DESTRABALHADORTEMPORARIO); Cadastro de Trabalhador Temporário (CADTRABALHADORTEMPORARIO); Prorrogação de Trabalhador Temporário (PRORTRABALHADORTEMPORARIO); Recadastramento de Trabalhador Temporário (RECADASTRAMENTOPOSTO)

## Grafo do fluxo
- [370817] EventoIntermediarioMensagem "E-mail de Término" → [370824] Finalização de Chamado
- [370818] Tarefa "Verificar Criação de Usuário" {Responsável atual} → [G82985] Abertura Acessos Solicitados
- [370819] Tarefa "Abrir Manual o chamado para  SISBB" {Responsável atual} → [G82982] Finalização Acessos Solicitados
- [370820] Tarefa "Abrir Manual o chamado para  WIFI" {Responsável atual} → [G82982] Finalização Acessos Solicitados
- [370821] Tarefa "Abrir Manual o chamado para  ERP" {Responsável atual} → [G82982] Finalização Acessos Solicitados
- [370822] Tarefa "Abrir Manual o chamado para
Criar usuário de Rede" {Responsável atual} → [370818] Verificar Criação de Usuário
- [370823] Tarefa "Abrir Manual o chamado para SICON" {Responsável atual} → [G82982] Finalização Acessos Solicitados
- [370824] EventoFinal "Finalização de Chamado" {Responsável atual} → (fim)
- [370825] EventoFinal "Finalização de Chamado" → (fim)
- [370826] Tarefa "Cadastrar Trabalhador Temporário no LG" {Responsável atual} → [G82983] Acesso a sistema?
- [370827] EventoInicial "Inicio" → [370813] Solicitar Aprovação do Gestor do UOR responsável p
- [370828] EventoIntermediarioMensagem "E-mail de Término" → [370825] Finalização de Chamado
- [370829] EventoIntermediarioMensagem "E-mail de Término" → [370815] Finalização de Chamado
- [370830] FimCancelamento "" {Responsável atual} → (fim)
- [370831] LinkInicial "" {Cliente} → [370813] Solicitar Aprovação do Gestor do UOR responsável p
- [370832] Tarefa "Abrir Manual o chamado para VPN" {Responsável atual} → [G82982] Finalização Acessos Solicitados
- [370835] Tarefa "Abrir Manual o chamado para Bloqueio" {Responsável atual} → [370836] Rescindir com Trabalhador Temporário no HR
- [370812] Tarefa "Finalizar Demanda Automática" {Responsável atual} → [G82982] Finalização Acessos Solicitados
- [370813] Tarefa "Solicitar Aprovação do Gestor do UOR responsável pelo Terceiro" {Fila CSC - Pendente de Aprovação} → [G82986] Aprovado?
- [370833] Tarefa "Cadastrar Trabalhador Temporário no HR" {Responsável atual} → [G82984] Cadastrar no PeopleSoft?
- [370834] Tarefa "Conferir Informações" {Responsável atual} → [G82988] Solicitação aceita?
- [370836] Tarefa "Rescindir com Trabalhador Temporário no HR" {Responsável atual} → [370828] E-mail de Término
- [370814] FimCancelamento "" {Responsável atual} → (fim)
- [370815] EventoFinal "Finalização de Chamado" {Responsável atual} → (fim)
- [370816] Tarefa "Iniciar" {Fila CSC - Prestação de Serviços} → [G82987] Qual Serviço?
- [G82987] Gateway "Qual Serviço?" → «Cadastro ou Prorrogação» [370834] Conferir Informações | «Desligamento» [370835] Abrir Manual o chamado para Bloqueio
- [G82988] Gateway "Solicitação aceita?" → «Sim» [370833] Cadastrar Trabalhador Temporário no HR | «Não» [370814] 
- [G82984] Gateway "Cadastrar no PeopleSoft?" → «Não» [G82983] Acesso a sistema? | «Sim» [370826] Cadastrar Trabalhador Temporário no LG
- [G82982] Gateway "Finalização Acessos Solicitados" → «FECHAMENTO» [370817] E-mail de Término
- [G82985] Gateway "Abertura Acessos Solicitados" → «SISBB» [370819] Abrir Manual o chamado para  SISBB | «SICON» [370823] Abrir Manual o chamado para SICON | «ERP» [370821] Abrir Manual o chamado para  ERP | «VPN» [370832] Abrir Manual o chamado para VPN | «Nenhum acesso» [370812] Finalizar Demanda Automática | «WIFI» [370820] Abrir Manual o chamado para  WIFI
- [G82983] Gateway "Acesso a sistema?" → «Não» [370829] E-mail de Término | «Sim» [370822] Abrir Manual o chamado para
Criar usuário de Rede
- [G82986] Gateway "Aprovado?" → «Aprovado» [370816] Iniciar | «False» [370830] 

## Gateways
### [G82987] Qual Serviço? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla.ToString()
```
- alternativa → [370834] Conferir Informações: OperadorDecision=NotEqual; ReferenciaDecision=Cadastro ou Prorrogação; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
"DESTRABALHADORTEMPORARIO"
```
- alternativa → [370835] Abrir Manual o chamado para Bloqueio: OperadorDecision=Equal; ReferenciaDecision=Desligamento; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
"DESTRABALHADORTEMPORARIO"
```
### [G82988] Solicitação aceita? (EventBasedExclusiveDecision)
Codigo=ACEITA
- alternativa → [370833] Cadastrar Trabalhador Temporário no HR: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [370814] : OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1; PublicarRespostaAA=true
### [G82984] Cadastrar no PeopleSoft? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["CSC_ACESSO_PEOPLESOFT"]
```
- alternativa → [G82983] Acesso a sistema?: OperadorDecision=NotEqual; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
- alternativa → [370826] Cadastrar Trabalhador Temporário no LG: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
### [G82982] Finalização Acessos Solicitados (DataBasedInclusiveDecision)
- alternativa → [370817] E-mail de Término: OperadorDecision=Equal; ReferenciaDecision=FECHAMENTO; SequenciaAvaliacao=0
### [G82985] Abertura Acessos Solicitados (DataBasedInclusiveDecision)
- alternativa → [370819] Abrir Manual o chamado para  SISBB: OperadorDecision=Equal; ReferenciaDecision=SISBB; SequenciaAvaliacao=4
**ValorComparacaoDecision**
```python
OrdemServico["CSC_ACESSO_SISBB"]==True
```
- alternativa → [370823] Abrir Manual o chamado para SICON: OperadorDecision=Equal; ReferenciaDecision=SICON; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
OrdemServico["CSC_ACESSO_SICON"]==True
```
- alternativa → [370821] Abrir Manual o chamado para  ERP: OperadorDecision=Equal; ReferenciaDecision=ERP; SequenciaAvaliacao=2
**ValorComparacaoDecision**
```python
OrdemServico["CSC_ACESSO_ERP"]==True
```
- alternativa → [370832] Abrir Manual o chamado para VPN: OperadorDecision=Equal; ReferenciaDecision=VPN; SequenciaAvaliacao=3
**ValorComparacaoDecision**
```python
OrdemServico["CSC_ACESSO_VPN"]==True
```
- alternativa → [370812] Finalizar Demanda Automática: OperadorDecision=Equal; ReferenciaDecision=Nenhum acesso; SequenciaAvaliacao=5
**ValorComparacaoDecision**
```python
OrdemServico["CSC_ACESSO_SISBB"]!=True and OrdemServico["CSC_ACESSO_VPN"]!=True and OrdemServico["CSC_ACESSO_ERP"]!=True and OrdemServico["CSC_ACESSO_WIFI"]!=True and OrdemServico["CSC_ACESSO_TOA"]!=True and OrdemServico["CSC_ACESSO_SICON"]!=True
```
- alternativa → [370820] Abrir Manual o chamado para  WIFI: OperadorDecision=Equal; ReferenciaDecision=WIFI; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
OrdemServico["CSC_ACESSO_WIFI"]==True
```
### [G82983] Acesso a sistema? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["CSC_ACESSO_REDE_EMAIL"] == None or OrdemServico["CSC_ACESSO_REDE_EMAIL"] == False
```
- alternativa → [370829] E-mail de Término: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
- alternativa → [370822] Abrir Manual o chamado para
Criar usuário de Rede: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
### [G82986] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROV_GESTOR_UOR")
```
- alternativa → [370816] Iniciar: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [370830] : OperadorDecision=Equal; ReferenciaDecision=False; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [370817] EventoIntermediarioMensagem "E-mail de Término"
Destinatário: Cliente (papel 18)
ModeloComunicado: Email de fechamento do chamado
Corpo do comunicado: Prezado,
A Ordem de Serviço nº OrdemServico.Numero referente ao assunto OrdemServico.Assunto foi encerrada com sucesso!
Atebciosamente,
Central de Serviços

### [370818] Tarefa "Verificar Criação de Usuário"
Responsável: Responsável atual (papel 36)

### [370819] Tarefa "Abrir Manual o chamado para  SISBB"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Supravizio.Processo.Custom import Atividade
import sysAid
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.
#
#OrdemServico.SetCustom("CSC_CPF",OrdemServico.Pai.GetCustom("CSC_CPF"))
#OrdemServico.SetCustom("CSC_DATA_FIM",OrdemServico.Pai.GetCustom("CSC_DATA_FIM"))
#OrdemServico.SetCustom("CSC_DATA_INICIO",OrdemServico.Pai.GetCustom("CSC_DATA_INICIO"))
#OrdemServico.SetCustom("CSC_MATRICULA",OrdemServico.Pai.GetCustom("CSC_MATRICULA"))
#OrdemServico.SetCustom("CSC_NOME_COMPLETO",OrdemServico.Pai.GetCustom("CSC_NOME_COMPLETO"))
#OrdemServico.SetCustom("CSC_TRABALHADOR_TEMPORARIO",OrdemServico.Pai.GetCustom("CSC_TRABALHADOR_TEMPORARIO"))
#OrdemServico.SetCustom("CSC_LOCALIDADE_ATUACAO",OrdemServico.Pai.GetCustom("CSC_LOCALIDADE_ATUACAO"))
#OrdemServico.SetCustom("CSC_UOR_LISTA",OrdemServico.Pai.GetCustom("CSC_UOR_LISTA"))
#OrdemServico.Salva()
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
#solicitante = OrdemServico.Cliente["MATRICULA"].ToString()
#usuarioAtendido = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#nomeColaborador = OrdemServico.GetCustom('CSC_NOME_COMPLETO').ToString() + OrdemServico.GetCustom('CSC_TRABALHADOR_TEMPORARIO').ToString()
#matricula = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#
#titulo = "Alterar permissao"
#categoria = "Controle de Acesso e Privilégios_SISBB_Criação de usuário"
#descricao = OrdemServico.Assunto+" - Chamado Supravizio= "+ OrdemServico.Numero.ToString()+", matrícula do temporário: "+usuarioAtendido+ ", nome do temporário: "+nomeColaborador + ", data inicio do contrato: "+OrdemServico.GetCustom('CSC_DATA_INICIO').ToString()+", data fim do contrato: "+OrdemServico.GetCustom('CSC_DATA_FIM').ToString()
#
#cpf = OrdemServico.GetCustom('CSC_CPF').ToString()
#localidade = DB.ExecuteScalar("SELECT DISTINCT E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE) and E.ESTABID='"+OrdemServico.GetCustom('CSC_LOCALIDADE_ATUACAO').ToString()+"'")
##uor = DB.ExecuteScalar(" SELECT DISTINCT NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO where nome <> SCR ||' - ' and SCR = '"+OrdemServico.GetCustom('CSC_UOR_LISTA').ToString()+"'")
##dtIncio = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_INICIO').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01')+1 )* 60 * 60 * 24 * 1000 from dual")
##dtFim = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_FIM').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01') +1)* 60 * 60 * 24 * 1000 from dual")
#
##emailUsuAtendido = DB.ExecuteScalar("select distinct ID from ta_10 where tipo = 0 and ATIVO ='S' and matricula = '"+usuarioAtendido+"'")+"@bbts.com.br"
#
#
#
#idSolic = consultaUsuario(OrdemServico.Cliente.Email)
#idAtend = consultaUsuario(OrdemServico.Cliente.Email)
#if idAtend == None:
#    OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+emailUsuAtendido.ToString()
#elif idSolic == None:
#    OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+OrdemServico.Cliente.Email.ToString()
#else:
#    resposta = acessoSISBB10824(categoria, titulo, descricao, idSolic, idAtend, cpf, localidade)
#    if String.IsNullOrEmpty(resposta.ToString()):
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada + "\n Atividade automática de abertura de chamado para acesso SISBB não realizada "
#    else:
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada +"\n Chamado para acesso SISBB: "+resposta.ToString()
#        AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos
  - DescricaoDetalhada (nativo) "Abertura de chamado no SysAid" obrigatório
- Operação PR0001 Preencher Campos
  - CSC_LOCALIDADE_ATUACAO "Localidade Atuação" [DropDownList String → CPE_CSC.CSC_LOCALIDADE_ATUACAO] obrigatório
  - CSC_UOR_LISTA "UOR" [DropDownList String(500) → CPE_CSC.CSC_UOR_LISTA] obrigatório
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO]
  - CSC_TRABALHADOR_TEMPORARIO "Trabalhador Temporário" [DropDownList String → CPE_CSC.CSC_TRABALHADOR_TEMPORARIO]
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA]
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF]
  - CSC_DATA_INICIO "Data Início" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO]
  - CSC_DATA_FIM "Data Fim" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM]

### [370820] Tarefa "Abrir Manual o chamado para  WIFI"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Supravizio.Processo.Custom import Atividade
from Venki.Services.Custom import Message
from Venki.Services.Security.Custom import User
import sysAid
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.
#
#OrdemServico.SetCustom("CSC_CPF",OrdemServico.Pai.GetCustom("CSC_CPF"))
#OrdemServico.SetCustom("CSC_DATA_FIM",OrdemServico.Pai.GetCustom("CSC_DATA_FIM"))
#OrdemServico.SetCustom("CSC_DATA_INICIO",OrdemServico.Pai.GetCustom("CSC_DATA_INICIO"))
#OrdemServico.SetCustom("CSC_MATRICULA",OrdemServico.Pai.GetCustom("CSC_MATRICULA"))
#OrdemServico.SetCustom("CSC_NOME_COMPLETO",OrdemServico.Pai.GetCustom("CSC_NOME_COMPLETO"))
#OrdemServico.SetCustom("CSC_TRABALHADOR_TEMPORARIO",OrdemServico.Pai.GetCustom("CSC_TRABALHADOR_TEMPORARIO"))
#OrdemServico.SetCustom("CSC_LOCALIDADE_ATUACAO",OrdemServico.Pai.GetCustom("CSC_LOCALIDADE_ATUACAO"))
#OrdemServico.SetCustom("CSC_UOR_LISTA",OrdemServico.Pai.GetCustom("CSC_UOR_LISTA"))
#OrdemServico.Salva()
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
#solicitante = OrdemServico.Cliente["MATRICULA"].ToString()
#usuarioAtendido = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#nomeColaborador = OrdemServico.GetCustom('CSC_NOME_COMPLETO').ToString() + OrdemServico.GetCustom('CSC_TRABALHADOR_TEMPORARIO').ToString()
#matricula = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#
#titulo = "Alterar permissao Acesso wifi"
#categoria = "Controle de Acesso e Privilégios_Conta de Rede_Alterar permissão"
#descricao = OrdemServico.Assunto+" - Chamado Supravizio= "+ OrdemServico.Numero.ToString()+", matrícula do temporário: "+usuarioAtendido+ ", nome do temporário: "+nomeColaborador
#
##empresa = OrdemServico.GetCustom('CSC_EMPRESA').ToString()
#localidade = DB.ExecuteScalar("SELECT DISTINCT E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE) and E.ESTABID='"+OrdemServico.GetCustom('CSC_LOCALIDADE_ATUACAO').ToString()+"'")
##uor = DB.ExecuteScalar(" SELECT DISTINCT NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO where nome <> SCR ||' - ' and SCR = '"+OrdemServico.GetCustom('CSC_UOR_LISTA').ToString()+"'")
##dtIncio = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_INICIO').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01')+1 )* 60 * 60 * 24 * 1000 from dual")
##dtFim = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_FIM').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01') +1)* 60 * 60 * 24 * 1000 from dual")
#
##emailUsuAtendido = DB.ExecuteScalar("select distinct ID from ta_10 where tipo = 0 and ATIVO ='S' and matricula = '"+usuarioAtendido+"'")+"@bbts.com.br"
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
##scriptCU='\nFunction Amend-SysAidTicketsCategories {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuSolicitante,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuAtendido,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=147"\n$ContentType = "application/json; charset=UTF-8"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n           {"key":"title", "value":"Teste API - Alterar permissao Acesso wifi Desconsiderar"},\n           {"key":"problem_type", "value":"'+categoria.encode('UTF-8')+'"},\n           {"key":"description", "value":"'+descricao.encode('UTF-8')+'"},\n           {"key":"status", "value":"1"},\n           {"key":"request_user", "value":"$UsuSolicitante"},\n           {"key":"followup_user", "value":"$UsuAtendido"},\n           {"key":"CustomColumn8sr", "value":"00000"},\n           {"key":"CustomColumn9sr", "value":"'+localidade.encode('UTF-8')+'"},\n           {"key":"assigned_group", "value":"4807"}\n           ]\n}\n"@\n '
##scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
##scriptCU3 = '$retorno = Amend-SysAidTicketsCategories -JSESSIONID $JSESSIONID.Value -SysAidURL $SysAidURL -UsuSolicitante $retornoUsu.id -UsuAtendido $retornoUsuAtend.id\n $retorno.id'
##script = scriptLogin3 + scriptConsUsu + scriptCU + scriptCU2 + scriptCU3
###OrdemServico.DescricaoDetalhada = script
##resposta = PowerShell.PSExecuteCmdlet(script)
#
#
#idSolic = consultaUsuario(OrdemServico.Cliente.Email)
#idAtend = consultaUsuario(OrdemServico.Cliente.Email)
#if idAtend == None:
#    OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+emailUsuAtendido.ToString()
#elif idSolic == None:
#    OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+OrdemServico.Cliente.Email.ToString()
#else:
#    resposta = alteraAcesso466(categoria, titulo, descricao, localidade, idSolic, idAtend)
#    if String.IsNullOrEmpty(resposta.ToString()):
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada + "\n Atividade automática de abertura de chamado para acesso WIFI não realizada "
#    else:
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada +"\n Chamado para acesso WIFI: "+resposta.ToString()
#        AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF]
  - CSC_DATA_INICIO "Data Início" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO]
  - CSC_DATA_FIM "Data Fim" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM]
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO]
  - CSC_TRABALHADOR_TEMPORARIO "Trabalhador Temporário" [DropDownList String → CPE_CSC.CSC_TRABALHADOR_TEMPORARIO]
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA]
  - CSC_LOCALIDADE_ATUACAO "Localidade Atuação" [DropDownList String → CPE_CSC.CSC_LOCALIDADE_ATUACAO] obrigatório
  - CSC_UOR_LISTA "UOR" [DropDownList String(500) → CPE_CSC.CSC_UOR_LISTA] obrigatório
- Operação PR0001 Preencher Campos
  - DescricaoDetalhada (nativo) "Abertura de chamado no SysAid" obrigatório

### [370821] Tarefa "Abrir Manual o chamado para  ERP"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Supravizio.Processo.Custom import Atividade
import sysAid
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.
#
#
#OrdemServico.SetCustom("CSC_CPF",OrdemServico.Pai.GetCustom("CSC_CPF"))
#OrdemServico.SetCustom("CSC_DATA_FIM",OrdemServico.Pai.GetCustom("CSC_DATA_FIM"))
#OrdemServico.SetCustom("CSC_DATA_INICIO",OrdemServico.Pai.GetCustom("CSC_DATA_INICIO"))
#OrdemServico.SetCustom("CSC_MATRICULA",OrdemServico.Pai.GetCustom("CSC_MATRICULA"))
#OrdemServico.SetCustom("CSC_NOME_COMPLETO",OrdemServico.Pai.GetCustom("CSC_NOME_COMPLETO"))
#OrdemServico.SetCustom("CSC_TRABALHADOR_TEMPORARIO",OrdemServico.Pai.GetCustom("CSC_TRABALHADOR_TEMPORARIO"))
#OrdemServico.SetCustom("CSC_LISTA_RESP_ERP",OrdemServico.Pai.GetCustom("CSC_LISTA_RESP_ERP"))
#OrdemServico.SetCustom("CSC_LOCALIDADE_ATUACAO",OrdemServico.Pai.GetCustom("CSC_LOCALIDADE_ATUACAO"))
#OrdemServico.SetCustom("CSC_UOR_LISTA",OrdemServico.Pai.GetCustom("CSC_UOR_LISTA"))
#OrdemServico.Salva()
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
#solicitante = OrdemServico.Cliente["MATRICULA"].ToString()
#usuarioAtendido = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#nomeColaborador = OrdemServico.GetCustom('CSC_NOME_COMPLETO').ToString() + OrdemServico.GetCustom('CSC_TRABALHADOR_TEMPORARIO').ToString()
#matricula = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#
#titulo = "Alterar permissao ERP"
#categoria = "Controle de Acesso e Privilégios_ERP_Liberação de acesso"
#descricao = OrdemServico.Assunto+" - Chamado Supravizio= "+ OrdemServico.Numero.ToString()+", matrícula do temporário: "+usuarioAtendido+ ", nome do temporário: "+nomeColaborador
#
#
##empresa = OrdemServico.GetCustom('CSC_EMPRESA').ToString()
#localidade = DB.ExecuteScalar("SELECT DISTINCT E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE) and E.ESTABID='"+OrdemServico.GetCustom('CSC_LOCALIDADE_ATUACAO').ToString()+"'")
##uor = DB.ExecuteScalar(" SELECT DISTINCT NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO where nome <> SCR ||' - ' and SCR = '"+OrdemServico.GetCustom('CSC_UOR_LISTA').ToString()+"'")
##dtIncio = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_INICIO').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01')+1 )* 60 * 60 * 24 * 1000 from dual")
##dtFim = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_FIM').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01') +1)* 60 * 60 * 24 * 1000 from dual")
#
##emailUsuAtendido = DB.ExecuteScalar("select distinct ID from ta_10 where tipo = 0 and ATIVO ='S' and matricula = '"+usuarioAtendido+"'")+"@bbts.com.br"
#erpObj=OrdemServico.GetCustom("CSC_LISTA_RESP_ERP")
#erp=''
#for linha in erpObj.Rows:
#    if erp=='':
#        erp = linha["MODULOS"]
#    else:
#        erp = erp+', ' + linha["MODULOS"]
##
#
#
#idSolic = consultaUsuario(OrdemServico.Cliente.Email)
#idAtend = consultaUsuario(OrdemServico.Cliente.Email)
#if idAtend == None:
#    OrdemServico.DescricaoDetalhada = 'Usuário não encontrado no SysAid: '+emailUsuAtendido.ToString()
#elif idSolic == None:
#    OrdemServico.DescricaoDetalhada = 'Usuário não encontrado no SysAid: '+OrdemServico.Cliente.Email.ToString()
#else:
#    resposta = acessoERP10814(categoria, titulo, descricao, erp, localidade, idSolic, idAtend)
#    if String.IsNullOrEmpty(resposta.ToString()):
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada + "\n Atividade automática de abertura de chamado para acesso ERP não realizada "
#    else:
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada +"\n Chamado para acesso ERP: "+resposta.ToString()
#        AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos
  - CSC_DATA_FIM "Data Fim" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM]
  - CSC_LISTA_RESP_ERP "Nome da Responsabilidade no ERP " [DataGrid RecordList → Z_00143_CSC_LISTA_RESP_ERP.CSC_LISTA_RESP_ERP] obrigatório
    - coluna MODULOS obrigatório
  - CSC_LOCALIDADE_ATUACAO "Localidade Atuação" [DropDownList String → CPE_CSC.CSC_LOCALIDADE_ATUACAO] obrigatório
  - CSC_UOR_LISTA "UOR" [DropDownList String(500) → CPE_CSC.CSC_UOR_LISTA] obrigatório
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO]
  - CSC_TRABALHADOR_TEMPORARIO "Trabalhador Temporário" [DropDownList String → CPE_CSC.CSC_TRABALHADOR_TEMPORARIO]
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA]
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF]
  - CSC_DATA_INICIO "Data Início" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO]
- Operação PR0001 Preencher Campos
  - DescricaoDetalhada (nativo) "Abertura de chamado no SysAid" obrigatório

### [370822] Tarefa "Abrir Manual o chamado para
Criar usuário de Rede"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Supravizio.Processo.Custom import Atividade
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
#telefone = OrdemServico.GetCustom('CSC_TELEFONE_CONTATO').ToString()
#categoria = "Controle de Acesso e Privilégios_Conta de Rede_Criação de usuário"
#titulo = 'Criacao de Usuario'
#descricao = OrdemServico.Assunto+" - Chamado Supravizio= "+ OrdemServico.Numero.ToString() + " - CPF Trabalhador Temporário= " + OrdemServico.GetCustom("CSC_CPF").ToString()
#solicitante = OrdemServico.Cliente["MATRICULA"].ToString()
#usuarioAtendido = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#if not String.IsNullOrEmpty(OrdemServico.GetCustom("CSC_TRABALHADOR_TEMPORARIO")):
#    nome = DB.ExecuteScalar("select distinct UPPER(full_name) as NOME from per_all_people_f where npw_number = '"+OrdemServico.GetCustom("CSC_TRABALHADOR_TEMPORARIO").ToString()+"'")
#if not String.IsNullOrEmpty(OrdemServico.GetCustom("CSC_NOME_COMPLETO")):
#    nome = OrdemServico.GetCustom("CSC_NOME_COMPLETO")
#nomeColaborador = nome
#matricula = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#empresa = OrdemServico.GetCustom('CSC_EMPRESA').ToString()
#localidade = DB.ExecuteScalar("SELECT DISTINCT E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE) and E.ESTABID='"+OrdemServico.GetCustom('CSC_LOCALIDADE_ATUACAO').ToString()+"'")
#uor = DB.ExecuteScalar(" SELECT DISTINCT NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO where nome <> SCR ||' - ' and SCR = '"+OrdemServico.GetCustom('CSC_UOR_LISTA').ToString()+"'")
#dtIncio = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_INICIO').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01')+1 )* 60 * 60 * 24 * 1000 from dual")
#dtFim = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_FIM').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01') +1)* 60 * 60 * 24 * 1000 from dual")
#
#
#
#idSolic = consultaUsuario(OrdemServico.Cliente.Email)
#
#if idSolic == None:
#    OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+OrdemServico.Cliente.Email.ToString()
#else:
#    resposta = acessoRede467(categoria, titulo, descricao, dtIncio, dtFim, idSolic, nomeColaborador, matricula, empresa, localidade, uor, telefone)
#    if String.IsNullOrEmpty(resposta.ToString()):
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada + "\n Atividade automática de abertura de chamado para Criação de Usuário não realizada "
#    else:
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada +"\n Chamado para Criação de Usuário: "+resposta.ToString()
#        AvancaProximaAtividade = True
```
**ScriptFim**
```python
from Venki.Supravizio.Processo.Custom import Atividade
from Venki.Services.Custom import Message
from Venki.Services.Security.Custom import User
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
##descricao = Regex.Replace(OrdemServico.Assunto+" - Chamado Supravizio= "+ OrdemServico.Numero.ToString(), "[^a-zA-Z0-9_.]+", "", RegexOptions.Compiled) 
#descricao = OrdemServico.Assunto+" - Chamado Supravizio= "+ OrdemServico.Numero.ToString()
#solicitante = OrdemServico.Cliente["MATRICULA"].ToString()
#usuarioAtendido = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#nomeColaborador = OrdemServico.GetCustom('CSC_NOME_COMPLETO').ToString() + OrdemServico.GetCustom('CSC_TRABALHADOR_TEMPORARIO').ToString()
#matricula = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#empresa = OrdemServico.GetCustom('CSC_EMPRESA').ToString()
#localidade = DB.ExecuteScalar("SELECT DISTINCT E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE) and E.ESTABID='"+OrdemServico.GetCustom('CSC_LOCALIDADE_ATUACAO').ToString()+"'")
#uor = DB.ExecuteScalar(" SELECT DISTINCT NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO where nome <> SCR ||' - ' and SCR = '"+OrdemServico.GetCustom('CSC_UOR_LISTA').ToString()+"'")
#dtIncio = DB.ExecuteScalar("select (to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_INICIO').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01')* 60 * 60 * 24 from dual")
#dtFim = DB.ExecuteScalar("select (to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_FIM').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01')* 60 * 60 * 24 from dual")
#
##API Autentica no Sysid
#scriptLogin= "$Username = '***MASCARADO***' \n $Password = '***MASCARADO***' \n $SysAidURL = 'https://centraldeti.bbts.com.br' "
#scriptLogin2= '\nFunction Get-SysAidToken {\n    Param(\n    [parameter(Mandatory=$true)]\n    [String]$Username,\n    [Parameter(Mandatory=$true)]\n    [String]$Password,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "$SysAidURL/api/v1/login"\n$ContentType = "application/json"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n    "user_name": "$Username",\n    "password": "$Password"\n}\n"@\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        = $Body\n}\nTry {\n$WebRequest = Invoke-WebRequest @props -ErrorAction Stop\n$StatusCode = $WebRequest.StatusCode\n}\nCatch {\n$StatusCode = $_.Exception.Response.StatusCode.value__\n}\nif ($StatusCode -eq "200") {\nWrite-Verbose "The Web Request Was Successful, Capturing JSESSIONID Cookie..." -Verbose\n$cookies = $WebSession.Cookies.GetCookies($Uri)\nreturn $cookies\nWrite-Verbose "$cookies" -Verbose\n}\nelseif ($StatusCode -eq "401") {\nWrite-Verbose "The Web Request Failed, with status code $StatusCode. Please enter the correct login information." -Verbose\n}\nelseif ($StatusCode -ne "200" -or "401") {\nWrite-Verbose "The Web Request Failed, with status code $StatusCode. Please verify the entered parameters." -Verbose\n}\nreturn $cookies\n} '
#scriptLogin3=scriptLogin + scriptLogin2 + "$JSESSIONID = Get-SysAidToken -Username $Username -Password $Password -SysAidURL $SysAidURL \n $JSESSIONID.Value"
#
##cookie = PowerShell.PSExecuteCmdlet(scriptLogin3)
#
##API para abrir chamado de criação de usuário no Sysid
#scriptCU='\nFunction Amend-SysAidTicketsCategories {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=149"\n$ContentType = "application/json; charset=iso_8859_1"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n            {"key":"title", "value":"Teste API - Criacao de Usuario Desconsiderar"},\n            {"key":"problem_type", "value":"Controle de Acesso e Privilegios_Conta de Rede_Criacao de Usuario"},\n            {"key":"description", "value":"'+descricao.encode('UTF-8') +'"},\n            {"key":"status", "value":"1"},\n            {"key":"request_user", "value":"'+solicitante+'"},\n            {"key":"followup_user", "value":"'+usuarioAtendido+'"},\n            {"key":"CustomColumn16sr", "value":"'+nomeColaborador.encode('UTF-8')+'"},\n            {"key":"CustomColumn15sr", "value":"'+matricula+'"},'
#scriptCU1= '\n            {"key":"CustomColumn18sr", "value":"'+empresa.encode('UTF-8')+'"},\n            {"key":"CustomColumn9sr", "value":"'+localidade.encode('UTF-8')+'"},\n            {"key":"CustomColumn17sr", "value":"'+uor.encode('UTF-8')+'"},\n            {"key":"CustomColumn19sr", "value":"'+dtIncio.ToString()+'"},\n            {"key":"CustomColumn20sr", "value":"'+dtFim.ToString()+'"},\n            {"key":"CustomColumn21sr", "value":"1"},\n            {"key":"assigned_group", "value":"4807"}\n            ]\n}\n"@\n '
#scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
#scriptCU3 = '$retorno = Amend-SysAidTicketsCategories -JSESSIONID $JSESSIONID.Value -SysAidURL $SysAidURL \n $retorno.id'
#script = scriptLogin3 + scriptCU + scriptCU1 + scriptCU2 + scriptCU3
##OrdemServico.DescricaoDetalhada = script
#resposta = PowerShell.PSExecuteCmdlet(script)
#if String.IsNullOrEmpty(resposta.ToString()):
#    OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada + "\n Atividade automática de abertura de chamado para Criação de Usuário não realizada "
#else:
#    OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada +"\n Chamado para Criação de Usuário: "+resposta[1].ToString()
#    #AvancaProximaAtividade = True










#import System
#from System.IO import *
#from System.Text  import *
#clr.AddReference("Newtonsoft.Json")
#clr.AddReference("System.Net.Http")
#from Newtonsoft.Json import *
#from Newtonsoft.Json.Linq import *
#from System.Net.Http import *
#from System.Net.Http.Headers import * 
#
#uri="https://centraldeti.bbts.com.br/api/v1/login"
#script1 = "$headers = New-Object 'System.Collections.Generic.Dictionary[[String],[String]]' \n "
#script2 = script1 +'$headers.Add("Content-Type", "application/json") \n $headers.Add("Cookie", "JSESSIONID=7AB853B861C3253930BF169FDAB82BE5") \n '
#script3 = script2 +'$body = "{`"user_name`":`"integracao.supravizio`",`"password`":`"123BBTS-2022!@#`"}" \n '
#script = script3+ "$resposta = Invoke-WebRequest '"+uri+"' -Method POST -Body $body -Headers $Headers \n $setCookie= $Resposta.Headers.'Set-Cookie'  -split ';' -split 'JSESSIONID=' \n $setCookie[1]"
#OrdemServico.AdicionaComentario(script,False)
#cookie = PowerShell.PSExecuteCmdlet(script)
#
#OrdemServico.AdicionaComentario(cookie,False) 
##cookie = "456"
#uri="https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=149"
#scriptCU1='$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]" \n $headers.Add("Content-Type", "application/json") \n $headers.Add("Cookie", "JSESSIONID='+cookie+'; JSESSIONID='+cookie+'") \n '
#scriptCU2= '$body = "{ \n `n `"info`": [ \n `n {`"key`":`"title`", `"value`":`"Teste API - Criação de Usuário (Desconsiderar)`"}, \n `n {`"key`":`"problem_type`", `"value`":`"Controle de Acesso e Privilégios_Conta de Rede_Criação de Usuário`"}, \n `n {`"key`":`"description`", `"value`":`"Teste de integração com o Supravizio para abertura de tickets de Criação de Usuário`"}, \n `n {`"key`":`"status`", `"value`":`"1`"}, \n `n {`"key`":`"request_user`", `"value`":`"595`"}, \n `n {`"key`":`"followup_user`", `"value`":`"595`"}, \n `n {`"key`":`"CustomColumn16sr`", `"value`":`"João Silva Pereira`"}, \n `n {`"key`":`"CustomColumn15sr`", `"value`":`"0123456`"}, \n `n {`"key`":`"CustomColumn18sr`", `"value`":`"BBTS`"}, \n `n {`"key`":`"CustomColumn9sr`", `"value`":`"São Paulo, SP`"}, \n `n {`"key`":`"CustomColumn17sr`", `"value`":`"CAT ABC`"}, \n `n {`"key`":`"CustomColumn19sr`", `"value`":`"1669297371000`"}, \n `n {`"key`":`"CustomColumn20sr`", `"value`":`"1688218824000`"}, \n `n {`"key`":`"CustomColumn21sr`", `"value`":`"1`"}, \n `n {`"key`":`"assigned_group`", `"value`":`"4807`"}] \n `n" \n '
#scriptCU3= '$response = Invoke-WebRequest "'+uri+'" -Method "POST" -Headers $headers -Body $body'
#
#OrdemServico.AdicionaComentario(scriptCU1,False)
#OrdemServico.AdicionaComentario(scriptCU2,False)
#OrdemServico.AdicionaComentario(scriptCU3,False)
#cookie = PowerShell.PSExecuteCmdlet(scriptCU1)
```
**ScriptFormCarregado**
```python
Formulario["DESCRICAODETALHADA"].Habilitado 
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.



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
#categoria = "Controle de Acesso e Privilégios_Conta de Rede_Criação de usuário"
#titulo = 'Criacao de Usuario'
#descricao = OrdemServico.Assunto+" - Chamado Supravizio= "+ OrdemServico.Numero.ToString()
#solicitante = OrdemServico.Cliente["MATRICULA"].ToString()
#usuarioAtendido = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#if not String.IsNullOrEmpty(OrdemServico.GetCustom("CSC_TRABALHADOR_TEMPORARIO")):
#    nome = DB.ExecuteScalar("select distinct UPPER(full_name) as NOME from per_all_people_f where npw_number = '"+OrdemServico.GetCustom("CSC_TRABALHADOR_TEMPORARIO").ToString()+"'")
#if not String.IsNullOrEmpty(OrdemServico.GetCustom("CSC_NOME_COMPLETO")):
#    nome = OrdemServico.GetCustom("CSC_NOME_COMPLETO")
#nomeColaborador = nome
#matricula = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#empresa = OrdemServico.GetCustom('CSC_EMPRESA').ToString()
#localidade = DB.ExecuteScalar("SELECT DISTINCT E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE) and E.ESTABID='"+OrdemServico.GetCustom('CSC_LOCALIDADE_ATUACAO').ToString()+"'")
#uor = DB.ExecuteScalar(" SELECT DISTINCT NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO where nome <> SCR ||' - ' and SCR = '"+OrdemServico.GetCustom('CSC_UOR_LISTA').ToString()+"'")
#dtIncio = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_INICIO').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01')+1 )* 60 * 60 * 24 * 1000 from dual")
#dtFim = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_FIM').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01') +1)* 60 * 60 * 24 * 1000 from dual")
#
#idSolic = consultaUsuario(OrdemServico.Cliente.Email)
#Formulario.ExibeMensagem(loginSysAid2('bbb').ToString())
#OrdemServico.DescricaoDetalhada = loginSysAid2('bbb').ToString()
#OrdemServico.AdicionaComentario('PingSucceeded: '+PowerShell.PSExecuteCmdlet("$r=Test-NetConnection santacruz.bbts.com.br\n echo $r.PingSucceeded").ToString(),False)
#OrdemServico.AdicionaComentario('PingSucceeded: '+PowerShell.PSExecuteCmdlet("$r=Test-NetConnection centraldeti.bbts.com.br\n echo $r.PingSucceeded").ToString(),False)
#OrdemServico.AdicionaComentario("Test-NetConnection centraldeti.bbts.com.br",False)
#idSolic = consultaUsuario(OrdemServico.Cliente.Email)
#Formulario.ExibeMensagem(categoria.ToString()+' - '+ titulo.ToString()+' - '+descricao.ToString()+' - '+ dtIncio.ToString()+' - '+ dtFim.ToString()+' - '+ idSolic.ToString() +' - '+ nomeColaborador.ToString()+' - '+ matricula.ToString()+' - '+ empresa.ToString()+' - '+ localidade.ToString()+' - '+ uor.ToString())
#resposta = acessoRede467(categoria, titulo, descricao, dtIncio, dtFim, idSolic, nomeColaborador, matricula, empresa, localidade, uor)

#idSolic = consultaUsuario('leonam.lima@bbts.com.br')
#idSolic=teste()
#OrdemServico.AdicionaComentario(idSolic.ToString(),False)
```
- Operação PR0001 Preencher Campos
  - DescricaoDetalhada (nativo) "Abertura de chamado no SysAid" obrigatório

### [370823] Tarefa "Abrir Manual o chamado para SICON"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Supravizio.Processo.Custom import Atividade
import sysAid
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.
#
#
#OrdemServico.SetCustom("CSC_CPF",OrdemServico.Pai.GetCustom("CSC_CPF"))
#OrdemServico.SetCustom("CSC_DATA_FIM",OrdemServico.Pai.GetCustom("CSC_DATA_FIM"))
#OrdemServico.SetCustom("CSC_DATA_INICIO",OrdemServico.Pai.GetCustom("CSC_DATA_INICIO"))
#OrdemServico.SetCustom("CSC_MATRICULA",OrdemServico.Pai.GetCustom("CSC_MATRICULA"))
#OrdemServico.SetCustom("CSC_NOME_COMPLETO",OrdemServico.Pai.GetCustom("CSC_NOME_COMPLETO"))
#OrdemServico.SetCustom("CSC_TRABALHADOR_TEMPORARIO",OrdemServico.Pai.GetCustom("CSC_TRABALHADOR_TEMPORARIO"))
#OrdemServico.SetCustom("CSC_LOCALIDADE_ATUACAO",OrdemServico.Pai.GetCustom("CSC_LOCALIDADE_ATUACAO"))
#OrdemServico.SetCustom("CSC_UOR_LISTA",OrdemServico.Pai.GetCustom("CSC_UOR_LISTA"))
#OrdemServico.Salva()
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
#
#solicitante = OrdemServico.Cliente["MATRICULA"].ToString()
#usuarioAtendido = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#nomeColaborador = OrdemServico.GetCustom('CSC_NOME_COMPLETO').ToString() + OrdemServico.GetCustom('CSC_TRABALHADOR_TEMPORARIO').ToString()
#matricula = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#
#titulo = "Alterar permissao Sicon"
#categoria = "Controle de Acesso e Privilégios_SICON_Criação de usuário"
#descricao = OrdemServico.Assunto+" - Chamado Supravizio= "+ OrdemServico.Numero.ToString()+", matrícula do temporário: "+usuarioAtendido+ ", nome do temporário: "+nomeColaborador
#
#idSolic = consultaUsuario(OrdemServico.Cliente.Email)
#idAtend = consultaUsuario(OrdemServico.Cliente.Email)
#if idAtend == None:
#    OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+emailUsuAtendido.ToString()
#elif idSolic == None:
#    OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+OrdemServico.Cliente.Email.ToString()
#else:
#    resposta = acessoSICON10822(categoria, titulo, descricao, idSolic, idAtend)
#    if String.IsNullOrEmpty(resposta.ToString()):
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada + "\n Atividade automática de abertura de chamado para acesso Sicon não realizada "
#    else:
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada +"\n Chamado para acesso Sicon: "+resposta.ToString()
#        AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO]
  - CSC_TRABALHADOR_TEMPORARIO "Trabalhador Temporário" [DropDownList String → CPE_CSC.CSC_TRABALHADOR_TEMPORARIO]
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA]
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF]
  - CSC_UOR_LISTA "UOR" [DropDownList String(500) → CPE_CSC.CSC_UOR_LISTA] obrigatório
  - CSC_DATA_INICIO "Data Início" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO]
  - CSC_DATA_FIM "Data Fim" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM]
  - CSC_LOCALIDADE_ATUACAO "Localidade Atuação" [DropDownList String → CPE_CSC.CSC_LOCALIDADE_ATUACAO] obrigatório
- Operação PR0001 Preencher Campos
  - DescricaoDetalhada (nativo) "Abertura de chamado no SysAid" obrigatório

### [370824] EventoFinal "Finalização de Chamado"
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [370825] EventoFinal "Finalização de Chamado"
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [370826] Tarefa "Cadastrar Trabalhador Temporário no LG"
Responsável: Responsável atual (papel 36)
**Regra**
```python
1
```
**ScriptFim**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#OrdemServico.Favorecido=Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("SELECT DISTINCT(ID_PESSOA) ID FROM CP_PESSOA WHERE MATRICULA = '"+OrdemServico["CSC_MATRICULA"]+"'")))
#OrdemServico.Salva()
nome = DB.ExecuteScalar("select distinct npw_number|| ' - ' ||UPPER(full_name) as NOME from per_all_people_f where npw_number is not null and npw_number ='"+OrdemServico["CSC_TRABALHADOR_TEMPORARIO"].ToString()+"'  GROUP BY npw_number,full_name")
if nome != "" and nome != None:
    OrdemServico.SetCustom("CSC_NOME_COMPLETO",nome)
    OrdemServico.Salva()
```
**ScriptFormCarregado**
```python
Formulario['COMBOBOX1'].Habilitado = False
Formulario["LABEL1"].Valor = '<span style=\"color: Black; font-weight: bold\"><br><br>A seleção do Trabalhador Temporário deve aguardar o Supravizio importar as informações do Peoplesoft (Dia do Cadastro + 1).</span>'
Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = False
Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = False
Formulario["CSC_NOME_COMPLETO"].Visivel = True
Formulario["CSC_NOME_COMPLETO"].Habilitado = True
Formulario["CSC_UOR"].Valor = OrdemServico["CSC_UOR_LISTA"]
if OrdemServico.Servico.Sigla.ToString() == 'DESTRABALHADORTEMPORARIO' or OrdemServico.Servico.Sigla.ToString() == 'PRORTRABALHADORTEMPORARIO':
    Formulario["CSC_NOME_COMPLETO"].Visivel = False
    Formulario["CSC_NOME_COMPLETO"].Habilitado = False
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = True
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = True
    Formulario["CSC_MATRICULA"].Habilitado = True
    Formulario["CSC_UOR"].Habilitado = True
    
    #sql = "SELECT MATRICULA, SUBSTR(ORGANIZACAO,1,10) ORGANIZACAO FROM CAD_FUNCIONARIO_V WHERE MATRICULA ='"+OrdemServico["CSC_TRABALHADOR_TEMPORARIO"].ToString()+"' ORDER BY NOME"
    #info = DB.ExecuteDataTable(sql)

    #for linha in info.Rows:
    #    Formulario["CSC_MATRICULA"].Valor = linha['MATRICULA'].ToString()
    #    Formulario["CSC_UOR"].Valor = linha['ORGANIZACAO'].ToString()
```
- Operação PR0001 Preencher Campos
  - LABEL1 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO] obrigatório
  - CSC_TRABALHADOR_TEMPORARIO "Trabalhador Temporário" [DropDownList String → CPE_CSC.CSC_TRABALHADOR_TEMPORARIO] obrigatório
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório
  - CSC_UOR "UOR no People" [TextBox String → CPE_CSC.CSC_UOR] obrigatório
  - COMBOBOX1 "COBAN" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]

### [370827] EventoInicial "Inicio"
TipoSolicitacao: 26.01. Gestão de Pessoas - Trabalhador Temporário
**ScriptFim**
```python
if OrdemServico.Servico.Sigla.ToString() == 'DESTRABALHADORTEMPORARIO' or OrdemServico.Servico.Sigla.ToString() == 'PRORTRABALHADORTEMPORARIO':
    dt= OrdemServico.GetCustom("CSC_LISTA_RESP_ERP")
    mat = OrdemServico.GetCustom("CSC_TRABALHADOR_TEMPORARIO")
    if dt.Rows.Count == 0:
        #sql_erp = "select ROWNUM-1 as RECID, RESP AS MODULOS from ERP_RESP_V where MATRICULA = '3829'"
        sql_erp = "select ROWNUM as RECID, RESPONSABILIDADE AS MODULOS from ERP_RESP_V where MATRICULA = '"+mat.ToString()+"'"
        info_erp = DB.ExecuteDataTable(sql_erp)
        #for linha_x in info_erp.Rows:
        #    qry = "INSERT INTO Z_00143_CSC_LISTA_RESP_ERP (ID_OCORRENCIA,MODULOS) VALUES ("+OrdemServico.Id.ToString()+",'"+linha_x["MODULOS"].ToString()+"')"
        #    DB.ExecuteNonQuery(qry)
        for linha_erp in info_erp.Rows:
            OrdemServico.AdicionaLinhaRegistro("CSC_LISTA_RESP_ERP",["MODULOS"],[linha_erp["MODULOS"].ToString()])
```
**ScriptValidacao**
```python
if OrdemServico.Servico.Sigla.ToString() == 'CADTRABALHADORTEMPORARIO':
    dt= OrdemServico.GetCustom("CSC_LISTA_RESP_ERP")
    if dt.Rows.Count == 0 and OrdemServico["CSC_ACESSO_ERP"] == True:
        Criticas.AdicionaPendencia("O campo 'Nome da Responsabilidade no ERP' deve ser preenchido com o nome dos módulos que o Trabalhador temporário terá acesso.")
```
**ScriptFormCarregado**
```python
OrdemServico.Assunto = None
OrdemServico.Assunto = OrdemServico.ClasseSubProcesso.Descricao +' - '+ OrdemServico.Servico.Descricao

Formulario['COMBOBOX1'].Itens = 'Sim;Não'
Formulario["CSC_NOME_COMPLETO"].Visivel = False
Formulario["CSC_NOME_COMPLETO"].Habilitado = False
Formulario["CSC_NOME_COMPLETO"].Valor = None
Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = False
Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = False
Formulario["CSC_TRABALHADOR_TEMPORARIO"].Valor = None
Formulario["CSC_EMAIL_PESSOAL"].Visivel = False
Formulario["CSC_EMAIL_PESSOAL"].Habilitado = False
Formulario["CSC_EMAIL_PESSOAL"].Valor = None
Formulario["CSC_LOGRADOURO"].Visivel = False
Formulario["CSC_LOGRADOURO"].Habilitado = False
Formulario["CSC_LOGRADOURO"].Valor = None
Formulario["CSC_NUMERO"].Visivel = False
Formulario["CSC_NUMERO"].Habilitado = False
Formulario["CSC_NUMERO"].Valor = None
Formulario["CSC_COMPLEMENTO"].Visivel = False
Formulario["CSC_COMPLEMENTO"].Habilitado = False
Formulario["CSC_COMPLEMENTO"].Valor = None
Formulario["CSC_BAIRRO"].Visivel = False
Formulario["CSC_BAIRRO"].Habilitado = False
Formulario["CSC_BAIRRO"].Valor = None
Formulario["CSC_UF"].Visivel = False
Formulario["CSC_UF"].Habilitado = False
Formulario["CSC_UF"].Valor = None
Formulario["CSC_CIDADE"].Visivel = False
Formulario["CSC_CIDADE"].Habilitado = False
Formulario["CSC_CIDADE"].Valor = None
Formulario["CSC_CEP"].Visivel = False
Formulario["CSC_CEP"].Habilitado = False
Formulario["CSC_CEP"].Valor = None
Formulario["CSC_CPF"].Visivel = False
Formulario["CSC_CPF"].Habilitado = False
Formulario["CSC_CPF"].Valor = None
Formulario["CSC_RG"].Visivel = False
Formulario["CSC_RG"].Habilitado = False
Formulario["CSC_RG"].Valor = None
Formulario["CSC_DATA_EMISSOA"].Visivel = False
Formulario["CSC_DATA_EMISSOA"].Habilitado = False
Formulario["CSC_DATA_EMISSOA"].Valor = None
Formulario["CSC_ORGAO_EMISSOR"].Visivel = False
Formulario["CSC_ORGAO_EMISSOR"].Habilitado = False
Formulario["CSC_ORGAO_EMISSOR"].Valor = None
Formulario["CSC_ESTADO_EMISSOR"].Visivel = False
Formulario["CSC_ESTADO_EMISSOR"].Habilitado = False
Formulario["CSC_ESTADO_EMISSOR"].Valor = None
Formulario["CSC_TELEFONE_CONTATO"].Visivel = False
Formulario["CSC_TELEFONE_CONTATO"].Habilitado = False
Formulario["CSC_TELEFONE_CONTATO"].Valor = None
Formulario["CSC_DATA_NASCIMENTO"].Visivel = False
Formulario["CSC_DATA_NASCIMENTO"].Habilitado = False
Formulario["CSC_DATA_NASCIMENTO"].Valor = None
Formulario["CSC_UF_NASCIMENTO"].Visivel = False
Formulario["CSC_UF_NASCIMENTO"].Habilitado = False
Formulario["CSC_UF_NASCIMENTO"].Valor = None
Formulario["CSC_CIDADE_NASCIMENTO"].Visivel = False
Formulario["CSC_CIDADE_NASCIMENTO"].Habilitado = False
Formulario["CSC_CIDADE_NASCIMENTO"].Valor = None
Formulario["CSC_ESTADO_CIVIL"].Visivel = False
Formulario["CSC_ESTADO_CIVIL"].Habilitado = False
Formulario["CSC_ESTADO_CIVIL"].Valor = None
Formulario["CSC_ESCOLARIDADE"].Visivel = False
Formulario["CSC_ESCOLARIDADE"].Habilitado = False
Formulario["SEXO_M_F"].Visivel = False
Formulario["SEXO_M_F"].Habilitado = False

Formulario["MATRICULA"].Visivel = False
Formulario["MATRICULA"].Habilitado = False
Formulario["SIM_NAO5"].Visivel = False
Formulario["SIM_NAO5"].Habilitado = False

Formulario["CSC_BANCO"].Visivel = False
Formulario["CSC_BANCO"].Habilitado = False
Formulario["CSC_BANCO"].Valor = None
Formulario["CSC_CONTA_CORRENTE"].Visivel = False
Formulario["CSC_CONTA_CORRENTE"].Habilitado = False
Formulario["CSC_CONTA_CORRENTE"].Valor = None
Formulario["CSC_DIGITO_AGENCIA"].Visivel = False
Formulario["CSC_DIGITO_AGENCIA"].Habilitado = False
Formulario["CSC_DIGITO_AGENCIA"].Valor = None
Formulario["CSC_DIGITO_CONTA_CORRENTE"].Visivel = False
Formulario["CSC_DIGITO_CONTA_CORRENTE"].Habilitado = False
Formulario["CSC_DIGITO_CONTA_CORRENTE"].Valor = None
Formulario["CSC_NOME_AGENCIA"].Visivel = False
Formulario["CSC_NOME_AGENCIA"].Habilitado = False
Formulario["CSC_NOME_AGENCIA"].Valor = None
Formulario["CSC_NUMERO_AGENCIA"].Visivel = False
Formulario["CSC_NUMERO_AGENCIA"].Habilitado = False
Formulario["CSC_NUMERO_AGENCIA"].Valor = None

Formulario["CSC_DGCO"].Visivel = False
Formulario["CSC_DGCO"].Habilitado = False
Formulario["CSC_EMPRESA"].Visivel = False
Formulario["CSC_EMPRESA"].Habilitado = False
Formulario["CSC_EMPRESA"].Valor = None
Formulario["DATA_FIM_PREVIST"].Visivel = False
Formulario["DATA_FIM_PREVIST"].Habilitado = False
Formulario["DATA_FIM_PREVIST"].Valor = None
Formulario["DATA_ATIVIDADE"].Visivel = False
Formulario["DATA_ATIVIDADE"].Habilitado = False
Formulario["DATA_ATIVIDADE"].Valor = None
Formulario["OBJETO_CONTRATACAO"].Visivel = False
Formulario["OBJETO_CONTRATACAO"].Habilitado = False
Formulario["OBJETO_CONTRATACAO"].Valor = None

Formulario["CSC_CARGO_LISTA"].Visivel = False
Formulario["CSC_CARGO_LISTA"].Habilitado = False
Formulario["CSC_CARGO_LISTA"].Valor = None
Formulario["CSC_DATA_FIM"].Visivel = False
Formulario["CSC_DATA_FIM"].Habilitado = False
Formulario["CSC_DATA_FIM"].Valor = None
Formulario["CSC_DATA_INICIO"].Visivel = False
Formulario["CSC_DATA_INICIO"].Habilitado = False
Formulario["CSC_DATA_INICIO"].Valor = None
Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = False
Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = False
Formulario["CSC_LOCALIDADE_ATUACAO"].Valor = None
Formulario["CSC_UOR_LISTA"].Visivel = False
Formulario["CSC_UOR_LISTA"].Habilitado = False
Formulario["CSC_UOR_LISTA"].Valor = None

Formulario["CSC_ACESSO_ERP"].Visivel = False
Formulario["CSC_ACESSO_ERP"].Habilitado = False
Formulario["CSC_ACESSO_ERP"].Valor = None
Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = False
Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = False
Formulario["CSC_ACESSO_REDE_EMAIL"].Valor = None
Formulario["CSC_ACESSO_SICON"].Visivel = False
Formulario["CSC_ACESSO_SICON"].Habilitado = False
Formulario["CSC_ACESSO_SICON"].Valor = None
Formulario["CSC_ACESSO_SISBB"].Visivel = False
Formulario["CSC_ACESSO_SISBB"].Habilitado = False
Formulario["CSC_ACESSO_SISBB"].Valor = None
##Formulario["CSC_ACESSO_TOA"].Visivel = False
##Formulario["CSC_ACESSO_TOA"].Habilitado = False
##Formulario["CSC_ACESSO_TOA"].Valor = None
Formulario["CSC_ACESSO_VPN"].Visivel = False
Formulario["CSC_ACESSO_VPN"].Habilitado = False
Formulario["CSC_ACESSO_VPN"].Valor = None
Formulario["CSC_ACESSO_WIFI"].Visivel = False
Formulario["CSC_ACESSO_WIFI"].Habilitado = False
Formulario["CSC_ACESSO_WIFI"].Valor = None
Formulario["LABEL2"].Visivel = False
Formulario["LABEL2"].Habilitado = False
Formulario["LABEL2"].Valor = None
Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
Formulario["CSC_LISTA_RESP_ERP"].Valor = None




if OrdemServico.Servico.Sigla.ToString() == 'CADTRABALHADORTEMPORARIO':
    Formulario["CSC_NOME_COMPLETO"].Visivel = True
    Formulario["CSC_NOME_COMPLETO"].Habilitado = True
    Formulario["CSC_EMAIL_PESSOAL"].Visivel = True
    Formulario["CSC_EMAIL_PESSOAL"].Habilitado = True
    Formulario["CSC_LOGRADOURO"].Visivel = True
    Formulario["CSC_LOGRADOURO"].Habilitado = True
    Formulario["CSC_NUMERO"].Visivel = True
    Formulario["CSC_NUMERO"].Habilitado = True
    Formulario["CSC_COMPLEMENTO"].Visivel = True
    Formulario["CSC_COMPLEMENTO"].Habilitado = True
    Formulario["CSC_BAIRRO"].Visivel = True
    Formulario["CSC_BAIRRO"].Habilitado = True
    Formulario["CSC_UF"].Visivel = True
    Formulario["CSC_UF"].Habilitado = True
    Formulario["CSC_CIDADE"].Visivel = True
    Formulario["CSC_CIDADE"].Habilitado = True
    Formulario["CSC_CEP"].Visivel = True
    Formulario["CSC_CEP"].Habilitado = True
    Formulario["CSC_CPF"].Visivel = True
    Formulario["CSC_CPF"].Habilitado = True
    Formulario["CSC_RG"].Visivel = True
    Formulario["CSC_RG"].Habilitado = True
    Formulario["CSC_DATA_EMISSOA"].Visivel = True
    Formulario["CSC_DATA_EMISSOA"].Habilitado = True
    Formulario["CSC_ORGAO_EMISSOR"].Visivel = True
    Formulario["CSC_ORGAO_EMISSOR"].Habilitado = True
    Formulario["CSC_ESTADO_EMISSOR"].Visivel = True
    Formulario["CSC_ESTADO_EMISSOR"].Habilitado = True
    Formulario["CSC_TELEFONE_CONTATO"].Visivel = True
    Formulario["CSC_TELEFONE_CONTATO"].Habilitado = True
    Formulario["CSC_DATA_NASCIMENTO"].Visivel = True
    Formulario["CSC_DATA_NASCIMENTO"].Habilitado = True
    Formulario["CSC_UF_NASCIMENTO"].Visivel = True
    Formulario["CSC_UF_NASCIMENTO"].Habilitado = True
    Formulario["CSC_CIDADE_NASCIMENTO"].Visivel = True
    Formulario["CSC_CIDADE_NASCIMENTO"].Habilitado = True
    Formulario["CSC_ESTADO_CIVIL"].Visivel = True
    Formulario["CSC_ESTADO_CIVIL"].Habilitado = True
    Formulario["CSC_ESCOLARIDADE"].Visivel = False
    Formulario["CSC_ESCOLARIDADE"].Habilitado = True
    Formulario["SEXO_M_F"].Visivel = True
    Formulario["SEXO_M_F"].Habilitado = True
    Formulario["CSC_BANCO"].Visivel = True
    Formulario["CSC_BANCO"].Habilitado = True
    Formulario["CSC_CONTA_CORRENTE"].Visivel = True
    Formulario["CSC_CONTA_CORRENTE"].Habilitado = True
    Formulario["CSC_DIGITO_AGENCIA"].Visivel = True
    Formulario["CSC_DIGITO_AGENCIA"].Habilitado = True
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Visivel = True
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Habilitado = True
    Formulario["CSC_NOME_AGENCIA"].Visivel = True
    Formulario["CSC_NOME_AGENCIA"].Habilitado = True
    Formulario["CSC_NUMERO_AGENCIA"].Visivel = True
    Formulario["CSC_NUMERO_AGENCIA"].Habilitado = True
    Formulario["CSC_DGCO"].Visivel = True
    Formulario["CSC_DGCO"].Habilitado = True
    Formulario["CSC_EMPRESA"].Visivel = True
    Formulario["CSC_EMPRESA"].Habilitado = True
    Formulario["CSC_CARGO_LISTA"].Visivel = True
    Formulario["CSC_CARGO_LISTA"].Habilitado = True
    Formulario["CSC_DATA_FIM"].Visivel = True
    Formulario["CSC_DATA_FIM"].Habilitado = True
    Formulario["CSC_DATA_INICIO"].Visivel = True
    Formulario["CSC_DATA_INICIO"].Habilitado = True
    Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = True
    Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = True
    Formulario["CSC_UOR_LISTA"].Visivel = True
    Formulario["CSC_UOR_LISTA"].Habilitado = True
    Formulario["CSC_ACESSO_ERP"].Visivel = False
    Formulario["CSC_ACESSO_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = True
    Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = True
    #Formulario["CSC_ACESSO_SICON"].Visivel = False
    #Formulario["CSC_ACESSO_SICON"].Habilitado = False
    Formulario["CSC_ACESSO_SISBB"].Visivel = False
    Formulario["CSC_ACESSO_SISBB"].Habilitado = False
    #Formulario["CSC_ACESSO_TOA"].Visivel = False
    #Formulario["CSC_ACESSO_TOA"].Habilitado = False
    Formulario["CSC_ACESSO_VPN"].Visivel = False
    Formulario["CSC_ACESSO_VPN"].Habilitado = False
    Formulario["CSC_ACESSO_WIFI"].Visivel = False
    Formulario["CSC_ACESSO_WIFI"].Habilitado = False
    Formulario["LABEL2"].Visivel = False
    Formulario["LABEL2"].Habilitado = False
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    Formulario["CSC_DATA_INICIO"].Visivel = True
    Formulario["CSC_DATA_INICIO"].Habilitado = True

if OrdemServico.Servico.Sigla.ToString() == 'PRORTRABALHADORTEMPORARIO':
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = True
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = True
    Formulario["CSC_EMAIL_PESSOAL"].Visivel = False
    Formulario["CSC_EMAIL_PESSOAL"].Habilitado = False
    Formulario["CSC_LOGRADOURO"].Visivel = True
    Formulario["CSC_LOGRADOURO"].Habilitado = True
    Formulario["CSC_NUMERO"].Visivel = True
    Formulario["CSC_NUMERO"].Habilitado = True
    Formulario["CSC_COMPLEMENTO"].Visivel = False
    Formulario["CSC_COMPLEMENTO"].Habilitado = False
    Formulario["CSC_BAIRRO"].Visivel = True
    Formulario["CSC_BAIRRO"].Habilitado = True
    Formulario["CSC_UF"].Visivel = True
    Formulario["CSC_UF"].Habilitado = True
    Formulario["CSC_CIDADE"].Visivel = True
    Formulario["CSC_CIDADE"].Habilitado = True
    Formulario["CSC_CEP"].Visivel = True
    Formulario["CSC_CEP"].Habilitado = True
    Formulario["CSC_CPF"].Visivel = True
    Formulario["CSC_CPF"].Habilitado = True
    Formulario["CSC_RG"].Visivel = False
    Formulario["CSC_RG"].Habilitado = False
    Formulario["CSC_DATA_EMISSOA"].Visivel = False
    Formulario["CSC_DATA_EMISSOA"].Habilitado = False
    Formulario["CSC_ORGAO_EMISSOR"].Visivel = False
    Formulario["CSC_ORGAO_EMISSOR"].Habilitado = False
    Formulario["CSC_ESTADO_EMISSOR"].Visivel = False
    Formulario["CSC_ESTADO_EMISSOR"].Habilitado = False
    Formulario["CSC_TELEFONE_CONTATO"].Visivel = True
    Formulario["CSC_TELEFONE_CONTATO"].Habilitado = True
    Formulario["CSC_DATA_NASCIMENTO"].Visivel = True
    Formulario["CSC_DATA_NASCIMENTO"].Habilitado = True
    Formulario["CSC_UF_NASCIMENTO"].Visivel = True
    Formulario["CSC_UF_NASCIMENTO"].Habilitado = True
    Formulario["CSC_CIDADE_NASCIMENTO"].Visivel = True
    Formulario["CSC_CIDADE_NASCIMENTO"].Habilitado = True
    Formulario["CSC_ESTADO_CIVIL"].Visivel = True
    Formulario["CSC_ESTADO_CIVIL"].Habilitado = True
    Formulario["CSC_ESCOLARIDADE"].Visivel = True
    Formulario["CSC_ESCOLARIDADE"].Habilitado = True
    Formulario["SEXO_M_F"].Visivel = True
    Formulario["SEXO_M_F"].Habilitado = True


    Formulario["CSC_BANCO"].Visivel = False
    Formulario["CSC_BANCO"].Habilitado = False
    Formulario["CSC_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_DIGITO_AGENCIA"].Visivel = False
    Formulario["CSC_DIGITO_AGENCIA"].Habilitado = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_NOME_AGENCIA"].Visivel = False
    Formulario["CSC_NOME_AGENCIA"].Habilitado = False
    Formulario["CSC_NUMERO_AGENCIA"].Visivel = False
    Formulario["CSC_NUMERO_AGENCIA"].Habilitado = False

    Formulario["CSC_DGCO"].Visivel = True
    Formulario["CSC_DGCO"].Habilitado = True
    Formulario["CSC_EMPRESA"].Visivel = True
    Formulario["CSC_EMPRESA"].Habilitado = True

    Formulario["CSC_CARGO_LISTA"].Visivel = True
    Formulario["CSC_CARGO_LISTA"].Habilitado = True
    Formulario["CSC_DATA_FIM"].Visivel = True
    Formulario["CSC_DATA_FIM"].Habilitado = True
    Formulario["CSC_DATA_INICIO"].Visivel = True
    Formulario["CSC_DATA_INICIO"].Habilitado = True
    Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = True
    Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = True
    Formulario["CSC_UOR_LISTA"].Visivel = True
    Formulario["CSC_UOR_LISTA"].Habilitado = True

    Formulario["CSC_ACESSO_ERP"].Visivel = False
    Formulario["CSC_ACESSO_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = True
    Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = True
    #Formulario["CSC_ACESSO_SICON"].Visivel = False
    #Formulario["CSC_ACESSO_SICON"].Habilitado = False
    Formulario["CSC_ACESSO_SISBB"].Visivel = False
    Formulario["CSC_ACESSO_SISBB"].Habilitado = False
    #Formulario["CSC_ACESSO_TOA"].Visivel = False
    #Formulario["CSC_ACESSO_TOA"].Habilitado = False
    Formulario["CSC_ACESSO_VPN"].Visivel = False
    Formulario["CSC_ACESSO_VPN"].Habilitado = False
    Formulario["CSC_ACESSO_WIFI"].Visivel = False
    Formulario["CSC_ACESSO_WIFI"].Habilitado = False
    Formulario["LABEL2"].Visivel = True
    Formulario["LABEL2"].Habilitado = True
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Visivel = True
    Formulario["CSC_ACESSO_PEOPLESOFT"].Habilitado = True

if OrdemServico.Servico.Sigla.ToString() == 'DESTRABALHADORTEMPORARIO':
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = True
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = True
    Formulario["CSC_EMAIL_PESSOAL"].Visivel = False
    Formulario["CSC_EMAIL_PESSOAL"].Habilitado = False
    Formulario["CSC_LOGRADOURO"].Visivel = True
    Formulario["CSC_LOGRADOURO"].Habilitado = True
    Formulario["CSC_NUMERO"].Visivel = True
    Formulario["CSC_NUMERO"].Habilitado = True
    Formulario["CSC_COMPLEMENTO"].Visivel = False
    Formulario["CSC_COMPLEMENTO"].Habilitado = False
    Formulario["CSC_BAIRRO"].Visivel = True
    Formulario["CSC_BAIRRO"].Habilitado = True
    Formulario["CSC_UF"].Visivel = True
    Formulario["CSC_UF"].Habilitado = True
    Formulario["CSC_CIDADE"].Visivel = True
    Formulario["CSC_CIDADE"].Habilitado = True
    Formulario["CSC_CEP"].Visivel = True
    Formulario["CSC_CEP"].Habilitado = True
    Formulario["CSC_CPF"].Visivel = True
    Formulario["CSC_CPF"].Habilitado = True
    Formulario["CSC_RG"].Visivel = False
    Formulario["CSC_RG"].Habilitado = False
    Formulario["CSC_DATA_EMISSOA"].Visivel = False
    Formulario["CSC_DATA_EMISSOA"].Habilitado = False
    Formulario["CSC_ORGAO_EMISSOR"].Visivel = False
    Formulario["CSC_ORGAO_EMISSOR"].Habilitado = False
    Formulario["CSC_ESTADO_EMISSOR"].Visivel = False
    Formulario["CSC_ESTADO_EMISSOR"].Habilitado = False
    Formulario["CSC_TELEFONE_CONTATO"].Visivel = True
    Formulario["CSC_TELEFONE_CONTATO"].Habilitado = True
    Formulario["CSC_DATA_NASCIMENTO"].Visivel = True
    Formulario["CSC_DATA_NASCIMENTO"].Habilitado = True
    Formulario["CSC_UF_NASCIMENTO"].Visivel = True
    Formulario["CSC_UF_NASCIMENTO"].Habilitado = True
    Formulario["CSC_CIDADE_NASCIMENTO"].Visivel = True
    Formulario["CSC_CIDADE_NASCIMENTO"].Habilitado = True
    Formulario["CSC_ESTADO_CIVIL"].Visivel = True
    Formulario["CSC_ESTADO_CIVIL"].Habilitado = True
    Formulario["CSC_ESCOLARIDADE"].Visivel = True
    Formulario["CSC_ESCOLARIDADE"].Habilitado = True
    Formulario["SEXO_M_F"].Visivel = True
    Formulario["SEXO_M_F"].Habilitado = True


    Formulario["CSC_BANCO"].Visivel = False
    Formulario["CSC_BANCO"].Habilitado = False
    Formulario["CSC_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_DIGITO_AGENCIA"].Visivel = False
    Formulario["CSC_DIGITO_AGENCIA"].Habilitado = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_NOME_AGENCIA"].Visivel = False
    Formulario["CSC_NOME_AGENCIA"].Habilitado = False
    Formulario["CSC_NUMERO_AGENCIA"].Visivel = False
    Formulario["CSC_NUMERO_AGENCIA"].Habilitado = False

    Formulario["CSC_DGCO"].Visivel = False
    Formulario["CSC_DGCO"].Habilitado = False
    Formulario["CSC_EMPRESA"].Visivel = False
    Formulario["CSC_EMPRESA"].Habilitado = False

    Formulario["CSC_CARGO_LISTA"].Visivel = False
    Formulario["CSC_CARGO_LISTA"].Habilitado = False
    Formulario["CSC_DATA_FIM"].Visivel = True
    Formulario["CSC_DATA_FIM"].Habilitado = True
    Formulario["CSC_DATA_INICIO"].Visivel = False
    Formulario["CSC_DATA_INICIO"].Habilitado = False
    Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = True
    Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = True
    Formulario["CSC_UOR_LISTA"].Visivel = True
    Formulario["CSC_UOR_LISTA"].Habilitado = True

    Formulario["CSC_ACESSO_ERP"].Visivel = False
    Formulario["CSC_ACESSO_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = True
    Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = True
    #Formulario["CSC_ACESSO_SICON"].Visivel = False
    #Formulario["CSC_ACESSO_SICON"].Habilitado = False
    Formulario["CSC_ACESSO_SISBB"].Visivel = False
    Formulario["CSC_ACESSO_SISBB"].Habilitado = False
    #Formulario["CSC_ACESSO_TOA"].Visivel = False
    #Formulario["CSC_ACESSO_TOA"].Habilitado = False
    Formulario["CSC_ACESSO_VPN"].Visivel = False
    Formulario["CSC_ACESSO_VPN"].Habilitado = False
    Formulario["CSC_ACESSO_WIFI"].Visivel = False
    Formulario["CSC_ACESSO_WIFI"].Habilitado = False
    Formulario["LABEL2"].Visivel = True
    Formulario["LABEL2"].Habilitado = True
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Visivel = True
    Formulario["CSC_ACESSO_PEOPLESOFT"].Habilitado = True
    Formulario["MATRICULA"].Visivel = True
    Formulario["MATRICULA"].Habilitado = True
    Formulario["SIM_NAO5"].Visivel = True
    Formulario["SIM_NAO5"].Habilitado = True

if OrdemServico.Servico.Sigla == "DESTRABALHADORTEMPORARIO":
    Formulario["CSC_ACESSO_ERP"].Visivel = False
    Formulario["CSC_ACESSO_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = False
    Formulario["CSC_ACESSO_SISBB"].Visivel = False
    Formulario["CSC_ACESSO_SISBB"].Habilitado = False
    Formulario["CSC_ACESSO_VPN"].Visivel = False
    Formulario["CSC_ACESSO_VPN"].Habilitado = False
    Formulario["CSC_ACESSO_WIFI"].Visivel = False
    Formulario["CSC_ACESSO_WIFI"].Habilitado = False
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Visivel = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Habilitado = False
    Formulario["MATRICULA"].Visivel = True
    Formulario["MATRICULA"].Habilitado = True
    Formulario["SIM_NAO5"].Visivel = True
    Formulario["SIM_NAO5"].Habilitado = True

if OrdemServico.Servico.Sigla == "RECADASTRAMENTOPOSTO":
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = True
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = True
    Formulario["CSC_NOME_COMPLETO"].Visivel = False
    Formulario["CSC_NOME_COMPLETO"].Habilitado = False
    Formulario["CSC_EMAIL_PESSOAL"].Visivel = False
    Formulario["CSC_EMAIL_PESSOAL"].Habilitado = False
    Formulario["CSC_LOGRADOURO"].Visivel = False
    Formulario["CSC_LOGRADOURO"].Habilitado = False
    Formulario["CSC_NUMERO"].Visivel = False
    Formulario["CSC_NUMERO"].Habilitado = False
    Formulario["CSC_COMPLEMENTO"].Visivel = False
    Formulario["CSC_COMPLEMENTO"].Habilitado = False
    Formulario["CSC_BAIRRO"].Visivel = False
    Formulario["CSC_BAIRRO"].Habilitado = False
    Formulario["CSC_UF"].Visivel = False
    Formulario["CSC_UF"].Habilitado = False
    Formulario["CSC_CIDADE"].Visivel = False
    Formulario["CSC_CIDADE"].Habilitado = False
    Formulario["CSC_CEP"].Visivel = False
    Formulario["CSC_CEP"].Habilitado = False
    Formulario["CSC_CPF"].Visivel = True
    Formulario["CSC_CPF"].Habilitado = True
    Formulario["CSC_RG"].Visivel = False
    Formulario["CSC_RG"].Habilitado = False
    Formulario["CSC_DATA_EMISSOA"].Visivel = False
    Formulario["CSC_DATA_EMISSOA"].Habilitado = False
    Formulario["CSC_ORGAO_EMISSOR"].Visivel = False
    Formulario["CSC_ORGAO_EMISSOR"].Habilitado = False
    Formulario["CSC_ESTADO_EMISSOR"].Visivel = False
    Formulario["CSC_ESTADO_EMISSOR"].Habilitado = False
    Formulario["CSC_TELEFONE_CONTATO"].Visivel = False
    Formulario["CSC_TELEFONE_CONTATO"].Habilitado = False
    Formulario["CSC_DATA_NASCIMENTO"].Visivel = False
    Formulario["CSC_DATA_NASCIMENTO"].Habilitado = False
    Formulario["CSC_UF_NASCIMENTO"].Visivel = False
    Formulario["CSC_UF_NASCIMENTO"].Habilitado = False
    Formulario["CSC_CIDADE_NASCIMENTO"].Visivel = False
    Formulario["CSC_CIDADE_NASCIMENTO"].Habilitado = False
    Formulario["CSC_ESTADO_CIVIL"].Visivel = False
    Formulario["CSC_ESTADO_CIVIL"].Habilitado = False
    Formulario["CSC_ESCOLARIDADE"].Visivel = False
    Formulario["CSC_ESCOLARIDADE"].Habilitado = False
    Formulario["SEXO_M_F"].Visivel = False
    Formulario["SEXO_M_F"].Habilitado = False
    Formulario["CSC_BANCO"].Visivel = False
    Formulario["CSC_BANCO"].Habilitado = False
    Formulario["CSC_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_DIGITO_AGENCIA"].Visivel = False
    Formulario["CSC_DIGITO_AGENCIA"].Habilitado = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_NOME_AGENCIA"].Visivel = False
    Formulario["CSC_NOME_AGENCIA"].Habilitado = False
    Formulario["CSC_NUMERO_AGENCIA"].Visivel = False
    Formulario["CSC_NUMERO_AGENCIA"].Habilitado = False

    Formulario["CSC_DGCO"].Visivel = True
    Formulario["CSC_DGCO"].Habilitado = True
    Formulario["CSC_EMPRESA"].Visivel = True
    Formulario["CSC_EMPRESA"].Habilitado = False
    Formulario["DATA_ATIVIDADE"].Visivel = True
    Formulario["DATA_ATIVIDADE"].Habilitado = True
    Formulario["DATA_FIM_PREVIST"].Visivel = True
    Formulario["DATA_FIM_PREVIST"].Habilitado = True
    Formulario["OBJETO_CONTRATACAO"].Visivel = True
    Formulario["OBJETO_CONTRATACAO"].Habilitado = False

    Formulario["CSC_CARGO_LISTA"].Visivel = False
    Formulario["CSC_CARGO_LISTA"].Habilitado = False
    Formulario["CSC_DATA_FIM"].Visivel = True
    Formulario["CSC_DATA_FIM"].Habilitado = True
    Formulario["CSC_DATA_INICIO"].Visivel = True
    Formulario["CSC_DATA_INICIO"].Habilitado = True
    Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = True
    Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = True
    Formulario["CSC_UOR_LISTA"].Visivel = True
    Formulario["CSC_UOR_LISTA"].Habilitado = True

    Formulario["CSC_ACESSO_ERP"].Visivel = False
    Formulario["CSC_ACESSO_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = True
    Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = True
    #Formulario["CSC_ACESSO_SICON"].Visivel = False
    #Formulario["CSC_ACESSO_SICON"].Habilitado = False
    Formulario["CSC_ACESSO_SISBB"].Visivel = False
    Formulario["CSC_ACESSO_SISBB"].Habilitado = False
    #Formulario["CSC_ACESSO_TOA"].Visivel = False
    #Formulario["CSC_ACESSO_TOA"].Habilitado = False
    Formulario["CSC_ACESSO_VPN"].Visivel = False
    Formulario["CSC_ACESSO_VPN"].Habilitado = False
    Formulario["CSC_ACESSO_WIFI"].Visivel = False
    Formulario["CSC_ACESSO_WIFI"].Habilitado = False
    Formulario["LABEL2"].Visivel = True
    Formulario["LABEL2"].Habilitado = True
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Visivel = True
    Formulario["CSC_ACESSO_PEOPLESOFT"].Habilitado = True
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados da Empresa do Trabalhador Temporário
  - CSC_DGCO "DGCO" [TextBox String → CPE_CSC.CSC_DGCO] obrigatório — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00000/0000"}
**CSC_DGCO.ScriptModificado**
```python
if OrdemServico.Servico.Sigla == "RECADASTRAMENTOPOSTO":
    clr.AddReference("Newtonsoft.Json")
    clr.AddReference("System.Net.Http")
    clr.AddReference("Supravizio.Custom")
    clr.AddReference("System.Data")

    import clr
    from System import Convert
    from Newtonsoft.Json.Linq import JArray
    from Newtonsoft.Json import JsonConvert
    from System.Net.Http import HttpClient
    from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
    from System import TimeSpan

    # Obtém valor do campo CSC_DGCO
    dgco = str(Formulario["CSC_DGCO"].Valor)

    # Token de autenticação
    token = '***MASCARADO***'

    # Obtém o ambiente (Homologação ou Produção)
    sql = "select name from sv_domain where enabled = 'Sim'"
    dom = DB.ExecuteScalar(sql)

    # Define a URL com base no ambiente
    url = ''
    if dom == 'HOMOLOGAÇÃO' or dom == 'PRODUÇÃO':    
        url = 'https://sisccon.bbts.com.br/supravizio/supra/buscar-intervenientes-por-dgco?dgco=' + dgco

    # Log para verificar a URL gerada
    Formulario['CSC_EMPRESA'].Valor = "URL: " + url

    # Verifica se a URL foi gerada corretamente
    if not url:
        Formulario['OBJETO_CONTRATACAO'].Valor = "Erro: URL não gerada corretamente."
    else:
        # Inicializa o HttpClient e configura os cabeçalhos
        client = HttpClient()
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Clear()
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.TryAddWithoutValidation("Content-Type", "application/json")
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

        # Faz a requisição GET
        try:
            response = client.GetAsync(url)
            response.Wait()

            if response.Result.IsSuccessStatusCode:
                # Lê o conteúdo da resposta
                resultAsync = response.Result.Content.ReadAsStringAsync()
                resultAsync.Wait()
                result = resultAsync.Result

                try:
                    # Verifica se o JSON está encapsulado em aspas
                    if result.startswith("\"") and result.endswith("\""):
                        result = JsonConvert.DeserializeObject(result)

                    # Converte o JSON em array
                    jsonArray = JArray.Parse(result)

                    # Se houver contratos a designar, processa os dados
                    if len(jsonArray) > 0:
                        for item in jsonArray:
                            Formulario["CSC_EMPRESA"].Valor = str(item['fornecedor'])
                            Formulario["OBJETO_CONTRATACAO"].Valor = str(item['objeto'])

                except Exception as e:
                    pass

        except Exception as e:
            pass
```
  - CSC_EMPRESA "Empresa" [TextBox String(500) → CPE_CSC.CSC_EMPRESA] obrigatório
  - OBJETO_CONTRATACAO "Objeto" [Memo String(1999) → CP_ORDEM_SERVICO.OBJETO_CONTRATACAO] obrigatório
  - DATA_ATIVIDADE "Data de Inicio da Vigência" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ATIVIDADE] obrigatório
  - DATA_FIM_PREVIST "Data de Fim da Vigência" [DatePicker DateTime → CPE_MOVIMENTACAO_PESSOA.DATA_FIM_PREVIST] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados da Área BBTS Solicitante do Trabalhador Temporário
  - CSC_LOCALIDADE_ATUACAO "Localidade Atuação" [DropDownList String → CPE_CSC.CSC_LOCALIDADE_ATUACAO] obrigatório
  - CSC_CAT "Local de Atendimento (Somente para Gered)" [DropDownList String → CPE_CSC.CSC_CAT] obrigatório
  - CSC_UOR_LISTA "UOR da Área Solicitante" [DropDownList String(500) → CPE_CSC.CSC_UOR_LISTA] obrigatório
  - CSC_CARGO_LISTA "Cargo que o Trabalhador ocupará" [DropDownList String(100) → CPE_CSC.CSC_CARGO_LISTA] obrigatório
  - CSC_DATA_INICIO "Início na BBTS (Contrato atual)" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO] obrigatório
  - CSC_DATA_FIM "Saída da BBTS" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Acesso aos Sistemas
  - CSC_ACESSO_REDE_EMAIL "Acesso Rede e E-mail" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_REDE_EMAIL] obrigatório
**CSC_ACESSO_REDE_EMAIL.ScriptModificado**
```python
Formulario["CSC_ACESSO_ERP"].Visivel = False
Formulario["CSC_ACESSO_ERP"].Habilitado = False
Formulario["CSC_ACESSO_SICON"].Visivel = False
Formulario["CSC_ACESSO_SICON"].Habilitado = False
Formulario["CSC_ACESSO_SISBB"].Visivel = False
Formulario["CSC_ACESSO_SISBB"].Habilitado = False
#Formulario["CSC_ACESSO_TOA"].Visivel = False
#Formulario["CSC_ACESSO_TOA"].Habilitado = False
Formulario["CSC_ACESSO_VPN"].Visivel = False
Formulario["CSC_ACESSO_VPN"].Habilitado = False
Formulario["CSC_ACESSO_WIFI"].Visivel = False
Formulario["CSC_ACESSO_WIFI"].Habilitado = False
Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
```
  - CSC_ACESSO_VPN "Acesso VPN" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_VPN] obrigatório
  - CSC_ACESSO_SICON "Acesso SICON" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_SICON] obrigatório
  - CSC_ACESSO_SISBB "Acesso SISBB" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_SISBB] obrigatório
  - CSC_ACESSO_WIFI "Acesso Wi-fi" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_WIFI] obrigatório
  - CSC_ACESSO_ERP "Acesso ERP" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_ERP] obrigatório
**CSC_ACESSO_ERP.ScriptModificado**
```python
Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
OrdemServico.SetCustom("CSC_LISTA_RESP_ERP", None)
if Formulario["CSC_ACESSO_ERP"].Valor == True:
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = True
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = True
    OrdemServico.SetCustom("CSC_LISTA_RESP_ERP", None)
    
if OrdemServico.Servico.Sigla == "RECADASTRAMENTOPOSTO":
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    OrdemServico.SetCustom("CSC_LISTA_RESP_ERP", None)
    if Formulario["CSC_ACESSO_ERP"].Valor == True:
        Formulario["CSC_LISTA_RESP_ERP"].Visivel = True
        Formulario["CSC_LISTA_RESP_ERP"].Habilitado = True
        OrdemServico.SetCustom("CSC_LISTA_RESP_ERP", None)
```
  - CSC_LISTA_RESP_ERP "Nome da Responsabilidade no ERP - Neste campo, indicar todos os módulos que necessita para o Sistema ERP" [DataGrid RecordList → Z_00143_CSC_LISTA_RESP_ERP.CSC_LISTA_RESP_ERP] — QtdColunasFormulario=1
**CSC_LISTA_RESP_ERP.ScriptAdicionado**
```python
if OrdemServico.Servico.Sigla.ToString() != 'CADTRABALHADORTEMPORARIO':
    dt= OrdemServico.GetCustom("CSC_LISTA_RESP_ERP")
    mat = OrdemServico.GetCustom("CSC_TRABALHADOR_TEMPORARIO")
    if dt.Rows.Count == 0:
        #sql_erp = "select ROWNUM-1 as RECID, RESP AS MODULOS from ERP_RESP_V where MATRICULA = '3829'"
        sql_erp = "select ROWNUM as RECID, RESPONSABILIDADE AS MODULOS from ERP_RESP_V where MATRICULA = '"+mat.ToString()+"'"
        info_erp = DB.ExecuteDataTable(sql_erp)
        if info_erp.Rows.Count == 0:
            Tabela.Clear()
        else:
            for linha_x in info_erp.Rows:
                Tabela.NewRow()
                Tabela.ImportRow(linha_x)
```
**CSC_LISTA_RESP_ERP.ScriptConfirmado**
```python
#Formulario.ExibeMensagem(Formulario['CSC_TRABALHADOR_TEMPORARIO'].Valor.ToString()+'sdfsdfs')
```
    - coluna MODULOS obrigatório
  - CSC_ACESSO_PEOPLESOFT "Acesso LG" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_PEOPLESOFT]
  - LABEL2 "IMPORTANTE: O ACESSO AO TOA É VIA OTRS: https://otrs.bbts.com.br/otrs/customer.pl?Action=CustomerTicketOverview;Subaction=MyTickets" [Label String(2000) → CP_ORDEM_SERVICO.LABEL2]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados Bancários (Não será aceita conta salário e conta poupança. Conta conjunta somente se o prestador for o titular)
  - CSC_NOME_AGENCIA "Nome Agência" [TextBox String(500) → CPE_CSC.CSC_NOME_AGENCIA]
  - CSC_CONTA_CORRENTE "Conta Corrente" [TextBox String → CPE_CSC.CSC_CONTA_CORRENTE]
  - CSC_DIGITO_CONTA_CORRENTE "Dígito Conta Corrente" [TextBox String → CPE_CSC.CSC_DIGITO_CONTA_CORRENTE]
  - CSC_BANCO "Banco" [DropDownList String(500) → CPE_CSC.CSC_BANCO]
  - CSC_NUMERO_AGENCIA "Número da Agência" [TextBox String → CPE_CSC.CSC_NUMERO_AGENCIA]
  - CSC_DIGITO_AGENCIA "Dígito da Agência" [TextBox String → CPE_CSC.CSC_DIGITO_AGENCIA]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados do Trabalhador Temporário
  - CSC_ORGAO_EMISSOR "Órgão Emissor" [TextBox String(200) → CPE_CSC.CSC_ORGAO_EMISSOR]
  - CSC_ESTADO_EMISSOR "Estado Emissor" [DropDownList String(500) → CPE_CSC.CSC_ESTADO_EMISSOR]
  - CSC_TELEFONE_CONTATO "Telefone para Contato" [TextBox String → CPE_CSC.CSC_TELEFONE_CONTATO] obrigatório
  - CSC_DATA_NASCIMENTO "Data de nascimento" [DatePicker DateTime → CPE_CSC.CSC_DATA_NASCIMENTO] obrigatório
  - SEXO_M_F "Sexo" [DropDownList String → CPE_CSC.SEXO_M_F] obrigatório
  - CSC_UF_NASCIMENTO "UF de Nascimento" [DropDownList String → CPE_CSC.CSC_UF_NASCIMENTO] obrigatório
  - CSC_CIDADE_NASCIMENTO "Cidade de Nascimento" [TextBox String(500) → CPE_CSC.CSC_CIDADE_NASCIMENTO] obrigatório
  - CSC_ESTADO_CIVIL "Estado Civil" [DropDownList String → CPE_CSC.CSC_ESTADO_CIVIL] obrigatório
  - CSC_ESCOLARIDADE "Escolaridade" [TextBox String → CPE_CSC.CSC_ESCOLARIDADE] obrigatório
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO]
  - CSC_TRABALHADOR_TEMPORARIO "Trabalhador Temporário" [DropDownList String → CPE_CSC.CSC_TRABALHADOR_TEMPORARIO] obrigatório
**CSC_TRABALHADOR_TEMPORARIO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["CSC_EMAIL_PESSOAL"].Valor = None
Formulario["CSC_LOGRADOURO"].Valor = None
Formulario["CSC_NUMERO"].Valor = None
Formulario["CSC_COMPLEMENTO"].Valor = None
Formulario["CSC_BAIRRO"].Valor = None
Formulario["CSC_UF"].Valor = None
Formulario["CSC_CIDADE"].Valor = None
Formulario["CSC_CEP"].Valor = None
Formulario["CSC_CPF"].Valor = None
Formulario["CSC_RG"].Valor = None
Formulario["CSC_DATA_EMISSOA"].Valor = None
Formulario["CSC_ORGAO_EMISSOR"].Valor = None
Formulario["CSC_ESTADO_EMISSOR"].Valor = None
Formulario["CSC_TELEFONE_CONTATO"].Valor = None
Formulario["CSC_DATA_NASCIMENTO"].Valor = None
Formulario["CSC_UF_NASCIMENTO"].Valor = None
Formulario["CSC_CIDADE_NASCIMENTO"].Valor = None
Formulario["CSC_ESTADO_CIVIL"].Valor = None
Formulario["CSC_BANCO"].Valor = None
Formulario["CSC_CONTA_CORRENTE"].Valor = None
Formulario["CSC_DIGITO_AGENCIA"].Valor = None
Formulario["CSC_DIGITO_CONTA_CORRENTE"].Valor = None
Formulario["CSC_NOME_AGENCIA"].Valor = None
Formulario["CSC_NUMERO_AGENCIA"].Valor = None
Formulario["CSC_UOR_LISTA"].Valor = None
Formulario["CSC_ACESSO_REDE_EMAIL"].Valor = False
Formulario["CSC_ACESSO_SICON"].Valor = False
Formulario["CSC_ACESSO_VPN"].Valor = False
Formulario["CSC_ACESSO_SISBB"].Valor = False
Formulario["CSC_ACESSO_WIFI"].Valor = False
Formulario["CSC_ACESSO_ERP"].Valor = False
Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
Formulario["LABEL2"].Valor = ""
Formulario["LABEL2"].Visivel = False

Utils.LogInformation("Variável Select: "+Controle.Valor.ToString(), "DEBUG")

sql = "SELECT ID, EMAIL_PESSOAL, NOME, ENDERECO, NRO_END, COMPLEMENTO_END, BAIRRO, TO_CHAR(ESTADO) AS ESTADO, CIDADE, CEP, CPF, RG, EMISSAO, RG_ORGAO_EMISSOR, TO_CHAR(RG_ESTADO_EMISSOR) AS RG_ESTADO_EMISSOR, TELEFONE, DATA_NASCIMENTO, TO_CHAR(ESTADO_NASCIMENTO) AS ESTADO_NASCIMENTO, CIDADE_NASCIMENTO, ESTADO_CIVIL, CODIGO_BANCO, CODIGO_AGENCIA, DIGITO_AGENCIA, NOME_AGENCIA, CONTA_NUMERO, CONTA_DIGITO, UOR FROM VW_BBTS_TRABALHADOR_TEMPORARIO WHERE ID = '"+Controle.Valor.ToString()+"'"

sql = "select DISTINCT PAPF.npw_number as ID, NULL AS EMAIL_PESSOAL,PAPF.full_name as NOME, pa.address_line1 AS ENDERECO, pa.address_line2 AS NRO_END, pa.address_line3 AS COMPLEMENTO_END, pa.region_1 AS BAIRRO, pa.region_2 AS ESTADO, pa.town_or_city AS CIDADE, pa.postal_code AS CEP,PAPF.NATIONAL_IDENTIFIER as CPF, PA.TELEPHONE_NUMBER_1 AS TELEFONE, NVL(TO_CHAR(PAPF.DATE_OF_BIRTH, 'DD/MM/RRRR'),'01/01/1900') AS DATA_NASCIMENTO, PAPF.TOWN_OF_BIRTH AS CIDADE_NASCIMENTO,'' AS ESTADO_NASCIMENTO, PAPF.MARITAL_STATUS AS ESTADO_CIVIL , NULL AS CODIGO_BANCO, NULL AS CODIGO_AGENCIA, NULL AS DIGITO_AGENCIA, NULL AS NOME_AGENCIA, NULL AS CONTA_NUMERO, NULL AS CONTA_DIGITO, NULL AS UOR, NULL AS RG, '01/01/1900' AS EMISSAO, NULL AS RG_ORGAO_EMISSOR, '' AS RG_ESTADO_EMISSOR from per_all_people_f PAPF INNER JOIN per_all_assignments_f PAAF ON paaf.person_id = papf.person_id INNER JOIN per_addresses PA ON pa.person_id = papf.person_id where PAPF.EFFECTIVE_START_DATE = (SELECT MAX(PAPF1.EFFECTIVE_START_DATE)FROM per_all_people_f PAPF1 WHERE papf1.person_id = papf.person_id) AND PAAF.EFFECTIVE_START_DATE = (SELECT MAX(PAAF1.EFFECTIVE_START_DATE)FROM per_all_assignments_f PAAF1 WHERE PAAF1.person_id = PAAF.person_id) AND (PAPF.npw_number = '"+Controle.Valor.ToString()+"' or PAPF.employee_number = '"+Controle.Valor.ToString()+"')"


info = DB.ExecuteDataTable(sql)
if info.Rows.Count >=1:
    for linha in info.Rows:
        #Formulario["CSC_EMAIL_PESSOAL"].Valor = linha['EMAIL_PESSOAL'].ToString()
        #Formulario["CSC_LOGRADOURO"].Valor = linha['ENDERECO'].ToString()
        #Formulario["CSC_NUMERO"].Valor = linha['NRO_END'].ToString()
        #Formulario["CSC_COMPLEMENTO"].Valor = linha['COMPLEMENTO_END'].ToString()
        #Formulario["CSC_BAIRRO"].Valor = linha['BAIRRO'].ToString()
        #Formulario["CSC_UF"].Valor = linha['ESTADO'].ToString()
        #Formulario["CSC_CIDADE"].Valor = linha['CIDADE'].ToString()
        #Formulario["CSC_CEP"].Valor = linha['CEP'].ToString()
        #Formulario["CSC_CPF"].Valor = linha['CPF'].ToString()
        #Formulario["CSC_RG"].Valor = linha['RG'].ToString()
        #Formulario["CSC_DATA_EMISSOA"].Valor = linha['EMISSAO'].ToString()
        #Formulario["CSC_ORGAO_EMISSOR"].Valor = linha['RG_ORGAO_EMISSOR'].ToString()
        #Formulario["CSC_ESTADO_EMISSOR"].Valor = linha['RG_ESTADO_EMISSOR'].ToString()
        #Formulario["CSC_TELEFONE_CONTATO"].Valor = linha['TELEFONE'].ToString()
        #Formulario["CSC_DATA_NASCIMENTO"].Valor = linha['DATA_NASCIMENTO'].ToString()
        #Formulario["CSC_UF_NASCIMENTO"].Valor = linha['ESTADO_NASCIMENTO'].ToString()
        #Formulario["CSC_CIDADE_NASCIMENTO"].Valor = linha['CIDADE_NASCIMENTO'].ToString()
        #Formulario["CSC_ESTADO_CIVIL"].Valor = linha['ESTADO_CIVIL'].ToString()
        #Formulario["CSC_BANCO"].Valor = linha['CODIGO_BANCO'].ToString()
        #Formulario["CSC_CONTA_CORRENTE"].Valor = linha['CONTA_NUMERO'].ToString()
        #Formulario["CSC_DIGITO_AGENCIA"].Valor = linha['DIGITO_AGENCIA'].ToString()
        #Formulario["CSC_DIGITO_CONTA_CORRENTE"].Valor = linha['CONTA_DIGITO'].ToString()
        #Formulario["CSC_NOME_AGENCIA"].Valor = linha['NOME_AGENCIA'].ToString()
        #Formulario["CSC_NUMERO_AGENCIA"].Valor = linha['CODIGO_AGENCIA'].ToString()
        Formulario["CSC_UOR_LISTA"].Valor = linha['UOR'].ToString()
else:
    Formulario.ExibeMensagem("O Trabalhador Temporário selecionado não está devidamente cadastrado no People.")
    

if (OrdemServico.Servico.Sigla.ToString() == 'DESTRABALHADORTEMPORARIO' or OrdemServico.Servico.Sigla.ToString() == 'PRORTRABALHADORTEMPORARIO') and info.Rows.Count >=1:
    Formulario["CSC_ACESSO_REDE_EMAIL"].Valor = False
    Formulario["CSC_ACESSO_SICON"].Valor = False
    Formulario["CSC_ACESSO_VPN"].Valor = False
    Formulario["CSC_ACESSO_SISBB"].Valor = False
    Formulario["CSC_ACESSO_WIFI"].Valor = False
    Formulario["CSC_ACESSO_ERP"].Valor = False
    #OrdemServico.SetCustom("CSC_LISTA_RESP_ERP",None)
    OrdemServico.SetCustom("CSC_TRABALHADOR_TEMPORARIO",linha['ID'].ToString())
    OrdemServico["CSC_LISTA_RESP_ERP"].Rows.Clear()
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    Formulario["LABEL2"].Valor = ""
    sql_si = "select * from SI_ACESSOS where MATRICULA = '"+linha['ID'].ToString()+"'"
    info_si = DB.ExecuteDataTable(sql_si)
    sql_erp = "select RESPONSABILIDADE from ERP_RESP_V where MATRICULA = '"+linha['ID'].ToString()+"'"
    info_erp = DB.ExecuteDataTable(sql_erp)
    for linha_si in info_si.Rows:
        if linha_si["LOGON"] == 'S':
            Formulario["CSC_ACESSO_REDE_EMAIL"].Valor = True
        if linha_si["SICON"] == 'S':
            Formulario["CSC_ACESSO_SICON"].Valor = True
        if linha_si["VPN"] == 'S':
            Formulario["CSC_ACESSO_VPN"].Valor = True
        if linha_si["SISBB"] == 'S':
            Formulario["CSC_ACESSO_SISBB"].Valor = True
        if linha_si["WIRELESS"] == 'S':
            Formulario["CSC_ACESSO_WIFI"].Valor = True
        if linha_si["ERP"] == 'S':
            OrdemServico.SetCustom("CSC_TRABALHADOR_TEMPORARIO",linha['ID'].ToString())
            Formulario["CSC_ACESSO_ERP"].Valor = True
            OrdemServico.SetCustom("CSC_LISTA_RESP_ERP",None)
            Formulario["LABEL2"].Visivel = True
            Formulario["LABEL2"].Valor = "<span style=\"color: Black; font-weight: bold\">Acesso já liberado aos seguintes Módulos do ERP:</span>"
            for linha_erp in info_erp.Rows:
                Formulario["LABEL2"].Valor = Formulario["LABEL2"].Valor+"<br>"+linha_erp["RESPONSABILIDADE"].ToString()
                OrdemServico.AdicionaLinhaRegistro("CSC_LISTA_RESP_ERP",["MODULOS"],[linha_erp["RESPONSABILIDADE"].ToString()])
            if OrdemServico.Servico.Sigla.ToString() == 'DESTRABALHADORTEMPORARIO':
                Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
                Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
            else:
                Formulario["LABEL2"].Valor = Formulario["LABEL2"].Valor+"<span style=\"color: Red; font-weight: bold\"><br>Para alterar favor clicar em 'Adicionar novo item' no campo abaixo.</span>"
                Formulario["CSC_LISTA_RESP_ERP"].Visivel = True
                Formulario["CSC_LISTA_RESP_ERP"].Habilitado = True


               
idFavorecidoCustom = Convert.ToInt32(Formulario["CSC_TRABALHADOR_TEMPORARIO"].Valor)
favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
 
sql1 = "SELECT ID, EMAIL_PESSOAL, NOME, ENDERECO, NRO_END, COMPLEMENTO_END, BAIRRO, TO_CHAR(ESTADO) AS ESTADO, CIDADE, CEP, CPF, RG, EMISSAO, RG_ORGAO_EMISSOR, TO_CHAR(RG_ESTADO_EMISSOR) AS RG_ESTADO_EMISSOR, TELEFONE, DATA_NASCIMENTO, TO_CHAR(ESTADO_NASCIMENTO) AS ESTADO_NASCIMENTO, CIDADE_NASCIMENTO, ESTADO_CIVIL, CODIGO_BANCO, CODIGO_AGENCIA, DIGITO_AGENCIA, NOME_AGENCIA, CONTA_NUMERO, CONTA_DIGITO, UOR FROM VW_BBTS_TRABALHADOR_TEMPORARIO WHERE ID = '"+Controle.Valor.ToString()+"'"
dados = DB.ExecuteDataTable(sql1)                
if OrdemServico.Servico.Sigla == "RECADASTRAMENTOPOSTO":
    for lista in dados.Rows:
        Formulario["CSC_EMAIL_PESSOAL"].Valor = lista['EMAIL_PESSOAL'].ToString()
        Formulario["CSC_LOGRADOURO"].Valor = lista['ENDERECO'].ToString()
        Formulario["CSC_NUMERO"].Valor = lista['NRO_END'].ToString()
        Formulario["CSC_COMPLEMENTO"].Valor = lista['COMPLEMENTO_END'].ToString()
        Formulario["CSC_BAIRRO"].Valor = lista['BAIRRO'].ToString()
        Formulario["CSC_UF"].Valor = lista['ESTADO'].ToString()
        Formulario["CSC_CIDADE"].Valor = lista['CIDADE'].ToString()
        Formulario["CSC_CEP"].Valor = lista['CEP'].ToString()
        Formulario["CSC_CPF"].Valor = lista['CPF'].ToString()
        Formulario["CSC_RG"].Valor = lista['RG'].ToString()
        Formulario["CSC_DATA_EMISSOA"].Valor = lista['EMISSAO'].ToString()
        Formulario["CSC_ORGAO_EMISSOR"].Valor = lista['RG_ORGAO_EMISSOR'].ToString()
        Formulario["CSC_ESTADO_EMISSOR"].Valor = lista['RG_ESTADO_EMISSOR'].ToString()
        Formulario["CSC_TELEFONE_CONTATO"].Valor = lista['TELEFONE'].ToString()
        Formulario["CSC_DATA_NASCIMENTO"].Valor = lista['DATA_NASCIMENTO'].ToString()
        Formulario["CSC_UF_NASCIMENTO"].Valor = lista['ESTADO_NASCIMENTO'].ToString()
        Formulario["CSC_CIDADE_NASCIMENTO"].Valor = lista['CIDADE_NASCIMENTO'].ToString()
        Formulario["CSC_ESTADO_CIVIL"].Valor = lista['ESTADO_CIVIL'].ToString()
        Formulario["CSC_BANCO"].Valor = lista['CODIGO_BANCO'].ToString()
        Formulario["CSC_CONTA_CORRENTE"].Valor = lista['CONTA_NUMERO'].ToString()
        Formulario["CSC_DIGITO_AGENCIA"].Valor = lista['DIGITO_AGENCIA'].ToString()
        Formulario["CSC_DIGITO_CONTA_CORRENTE"].Valor = lista['CONTA_DIGITO'].ToString()
        Formulario["CSC_NOME_AGENCIA"].Valor = lista['NOME_AGENCIA'].ToString()
        Formulario["CSC_NUMERO_AGENCIA"].Valor = lista['CODIGO_AGENCIA'].ToString()
        Formulario["CSC_UOR_LISTA"].Valor = lista['UOR'].ToString()
```
  - CSC_EMAIL_PESSOAL "E-mail Pessoal" [TextBox String(500) → CPE_CSC.CSC_EMAIL_PESSOAL]
  - CSC_LOGRADOURO "Logradouro" [TextBox String(500) → CPE_CSC.CSC_LOGRADOURO] obrigatório
  - CSC_NUMERO "Número" [TextBox String(100) → CPE_CSC.CSC_NUMERO] obrigatório
  - CSC_COMPLEMENTO "Complemento" [TextBox String(500) → CPE_CSC.CSC_COMPLEMENTO]
  - CSC_BAIRRO "Bairro" [TextBox String(500) → CPE_CSC.CSC_BAIRRO] obrigatório
  - CSC_UF "UF" [DropDownList String → CPE_CSC.CSC_UF] obrigatório
  - CSC_CIDADE "Cidade" [TextBox String(500) → CPE_CSC.CSC_CIDADE] obrigatório
  - CSC_CEP "CEP" [TextBox String → CPE_CSC.CSC_CEP] obrigatório — Configuracao={"SalvaLiteralMascara":false, "Mascara":"00000\\-000"}
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF] obrigatório — Configuracao={"SalvaLiteralMascara":false, "Mascara":"000\\.000\\.000\\-00"}
  - CSC_RG "RG" [TextBox String → CPE_CSC.CSC_RG]
  - CSC_DATA_EMISSOA "Emissão" [DatePicker DateTime → CPE_CSC.CSC_DATA_EMISSOA]
  - COMBOBOX1 "COBAN" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Cadastro no Peoplesoft
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA]
  - SIM_NAO5 "O trabalhador tem cadastro no peoplesoft?" [DropDownList String → CPE_CSC.SIM_NAO5] obrigatório
**SIM_NAO5.ScriptModificado**
```python
if Formulario["SIM_NAO5"].Valor == 'Sim':
    Formulario["MATRICULA"].Visivel = True
    
if Formulario["SIM_NAO5"].Valor != 'Sim':
    Formulario["MATRICULA"].Visivel = False
```

### [370828] EventoIntermediarioMensagem "E-mail de Término"
Destinatário: Cliente (papel 18)
ModeloComunicado: Chamado Finalizado Cesec
Corpo do comunicado: Prezado(a), OrdemServico.Customizado.FAVORECIDO_COBRA 
Informamos que a Ordem de Serviço nº OrdemServico foi concluída com sucesso!
 Link.Pesquisa 
Atenciosamente,
Central de Serviços

### [370829] EventoIntermediarioMensagem "E-mail de Término"
Destinatário: Cliente (papel 18)
ModeloComunicado: Chamado Finalizado Cesec 3
Corpo do comunicado: Prezado(a), OrdemServico.Customizado.FAVORECIDO_COBRA 
informamos que a Ordem de Serviço nº OrdemServico foi encerrada com sucesso!
Nome: OrdemServico.Customizado.CSC_NOME_COMPLETO 
Matrícula: OrdemServico.Customizado.CSC_MATRICULA 
* Informamos que a criação do Login e Senha foi solicitada a área de TI através do ticket na OS, dentro de 48 horas úteis será encaminhado o login e senha do trabalhador temporário para o solicitante da abertura da Ordem de Serviço.
 Atenciosamente,
Central de Serviços

### [370830] FimCancelamento ""
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
OrdemServico.MotivoCancelamento = OrdemServico.ObtemMotivoReprovacao("APROV_GESTOR_UOR")
```

### [370831] LinkInicial ""
Responsável: Cliente (papel 18)
Config: TipoMensagem=MensagemProcesso
**ScriptFim**
```python
if OrdemServico.Servico.Sigla.ToString() == 'DESTRABALHADORTEMPORARIO' or OrdemServico.Servico.Sigla.ToString() == 'PRORTRABALHADORTEMPORARIO':
    dt= OrdemServico.GetCustom("CSC_LISTA_RESP_ERP")
    mat = OrdemServico.GetCustom("CSC_TRABALHADOR_TEMPORARIO")
    if dt.Rows.Count == 0:
        #sql_erp = "select ROWNUM-1 as RECID, RESP AS MODULOS from ERP_RESP_V where MATRICULA = '3829'"
        sql_erp = "select ROWNUM as RECID, RESPONSABILIDADE AS MODULOS from ERP_RESP_V where MATRICULA = '"+mat.ToString()+"'"
        info_erp = DB.ExecuteDataTable(sql_erp)
        #for linha_x in info_erp.Rows:
        #    qry = "INSERT INTO Z_00143_CSC_LISTA_RESP_ERP (ID_OCORRENCIA,MODULOS) VALUES ("+OrdemServico.Id.ToString()+",'"+linha_x["MODULOS"].ToString()+"')"
        #    DB.ExecuteNonQuery(qry)
        for linha_erp in info_erp.Rows:
            OrdemServico.AdicionaLinhaRegistro("CSC_LISTA_RESP_ERP",["MODULOS"],[linha_erp["MODULOS"].ToString()])
```
**ScriptValidacao**
```python
if OrdemServico.Servico.Sigla.ToString() == 'CADTRABALHADORTEMPORARIO':
    dt= OrdemServico.GetCustom("CSC_LISTA_RESP_ERP")
    if dt.Rows.Count == 0 and OrdemServico["CSC_ACESSO_ERP"] == True:
        Criticas.AdicionaPendencia("O campo 'Nome da Responsabilidade no ERP' deve ser preenchido com o nome dos módulos que o Trabalhador temporário terá acesso.")
```
**ScriptFormCarregado**
```python
OrdemServico.Assunto = None
OrdemServico.Assunto = OrdemServico.ClasseSubProcesso.Descricao +' - '+ OrdemServico.Servico.Descricao

Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = False
Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = False
Formulario["CSC_TRABALHADOR_TEMPORARIO"].Valor = None

Formulario["CSC_ACESSO_ERP"].Visivel = False
Formulario["CSC_ACESSO_ERP"].Habilitado = False
Formulario["CSC_ACESSO_ERP"].Valor = None
Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = False
Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = False
#Formulario["CSC_ACESSO_REDE_EMAIL"].Valor = None
Formulario["CSC_ACESSO_SICON"].Visivel = False
Formulario["CSC_ACESSO_SICON"].Habilitado = False
Formulario["CSC_ACESSO_SICON"].Valor = None
Formulario["CSC_ACESSO_SISBB"].Visivel = False
Formulario["CSC_ACESSO_SISBB"].Habilitado = False
Formulario["CSC_ACESSO_SISBB"].Valor = None
##Formulario["CSC_ACESSO_TOA"].Visivel = False
##Formulario["CSC_ACESSO_TOA"].Habilitado = False
##Formulario["CSC_ACESSO_TOA"].Valor = None
Formulario["CSC_ACESSO_VPN"].Visivel = False
Formulario["CSC_ACESSO_VPN"].Habilitado = False
Formulario["CSC_ACESSO_VPN"].Valor = None
Formulario["CSC_ACESSO_WIFI"].Visivel = False
Formulario["CSC_ACESSO_WIFI"].Habilitado = False
Formulario["CSC_ACESSO_WIFI"].Valor = None
Formulario["LABEL2"].Visivel = False
Formulario["LABEL2"].Habilitado = False
Formulario["LABEL2"].Valor = None
Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
Formulario["CSC_LISTA_RESP_ERP"].Valor = None





#Formulario["CSC_NOME_COMPLETO"].Visivel = False
#Formulario["CSC_NOME_COMPLETO"].Habilitado = False
#Formulario["CSC_NOME_COMPLETO"].Valor = None

#Formulario["CSC_EMAIL_PESSOAL"].Visivel = False
#Formulario["CSC_EMAIL_PESSOAL"].Habilitado = False
#Formulario["CSC_EMAIL_PESSOAL"].Valor = None
#Formulario["CSC_LOGRADOURO"].Visivel = False
#Formulario["CSC_LOGRADOURO"].Habilitado = False
#Formulario["CSC_LOGRADOURO"].Valor = None
#Formulario["CSC_NUMERO"].Visivel = False
#Formulario["CSC_NUMERO"].Habilitado = False
#Formulario["CSC_NUMERO"].Valor = None
#Formulario["CSC_COMPLEMENTO"].Visivel = False
#Formulario["CSC_COMPLEMENTO"].Habilitado = False
#Formulario["CSC_COMPLEMENTO"].Valor = None
#Formulario["CSC_BAIRRO"].Visivel = False
#Formulario["CSC_BAIRRO"].Habilitado = False
#Formulario["CSC_BAIRRO"].Valor = None
#Formulario["CSC_UF"].Visivel = False
#Formulario["CSC_UF"].Habilitado = False
#Formulario["CSC_UF"].Valor = None
#Formulario["CSC_CIDADE"].Visivel = False
#Formulario["CSC_CIDADE"].Habilitado = False
#Formulario["CSC_CIDADE"].Valor = None
#Formulario["CSC_CEP"].Visivel = False
#Formulario["CSC_CEP"].Habilitado = False
#Formulario["CSC_CEP"].Valor = None
#Formulario["CSC_CPF"].Visivel = False
#Formulario["CSC_CPF"].Habilitado = False
#Formulario["CSC_CPF"].Valor = None
#Formulario["CSC_RG"].Visivel = False
#Formulario["CSC_RG"].Habilitado = False
#Formulario["CSC_RG"].Valor = None
#Formulario["CSC_DATA_EMISSOA"].Visivel = False
#Formulario["CSC_DATA_EMISSOA"].Habilitado = False
#Formulario["CSC_DATA_EMISSOA"].Valor = None
#Formulario["CSC_ORGAO_EMISSOR"].Visivel = False
#Formulario["CSC_ORGAO_EMISSOR"].Habilitado = False
#Formulario["CSC_ORGAO_EMISSOR"].Valor = None
#Formulario["CSC_ESTADO_EMISSOR"].Visivel = False
#Formulario["CSC_ESTADO_EMISSOR"].Habilitado = False
#Formulario["CSC_ESTADO_EMISSOR"].Valor = None
#Formulario["CSC_TELEFONE_CONTATO"].Visivel = False
#Formulario["CSC_TELEFONE_CONTATO"].Habilitado = False
#Formulario["CSC_TELEFONE_CONTATO"].Valor = None
#Formulario["CSC_DATA_NASCIMENTO"].Visivel = False
#Formulario["CSC_DATA_NASCIMENTO"].Habilitado = False
#Formulario["CSC_DATA_NASCIMENTO"].Valor = None
#Formulario["CSC_UF_NASCIMENTO"].Visivel = False
#Formulario["CSC_UF_NASCIMENTO"].Habilitado = False
#Formulario["CSC_UF_NASCIMENTO"].Valor = None
#Formulario["CSC_CIDADE_NASCIMENTO"].Visivel = False
#Formulario["CSC_CIDADE_NASCIMENTO"].Habilitado = False
#Formulario["CSC_CIDADE_NASCIMENTO"].Valor = None
#Formulario["CSC_ESTADO_CIVIL"].Visivel = False
#Formulario["CSC_ESTADO_CIVIL"].Habilitado = False
#Formulario["CSC_ESTADO_CIVIL"].Valor = None
#Formulario["CSC_ESCOLARIDADE"].Visivel = False
#Formulario["CSC_ESCOLARIDADE"].Habilitado = False
#Formulario["SEXO_M_F"].Visivel = False
#Formulario["SEXO_M_F"].Habilitado = False
#
Formulario["MATRICULA"].Visivel = False
Formulario["MATRICULA"].Habilitado = False
Formulario["SIM_NAO5"].Visivel = False
Formulario["SIM_NAO5"].Habilitado = False
#
#Formulario["CSC_BANCO"].Visivel = False
#Formulario["CSC_BANCO"].Habilitado = False
#Formulario["CSC_BANCO"].Valor = None
#Formulario["CSC_CONTA_CORRENTE"].Visivel = False
#Formulario["CSC_CONTA_CORRENTE"].Habilitado = False
#Formulario["CSC_CONTA_CORRENTE"].Valor = None
#Formulario["CSC_DIGITO_AGENCIA"].Visivel = False
#Formulario["CSC_DIGITO_AGENCIA"].Habilitado = False
#Formulario["CSC_DIGITO_AGENCIA"].Valor = None
#Formulario["CSC_DIGITO_CONTA_CORRENTE"].Visivel = False
#Formulario["CSC_DIGITO_CONTA_CORRENTE"].Habilitado = False
#Formulario["CSC_DIGITO_CONTA_CORRENTE"].Valor = None
#Formulario["CSC_NOME_AGENCIA"].Visivel = False
#Formulario["CSC_NOME_AGENCIA"].Habilitado = False
#Formulario["CSC_NOME_AGENCIA"].Valor = None
#Formulario["CSC_NUMERO_AGENCIA"].Visivel = False
#Formulario["CSC_NUMERO_AGENCIA"].Habilitado = False
#Formulario["CSC_NUMERO_AGENCIA"].Valor = None
#
#Formulario["CSC_DGCO"].Visivel = False
#Formulario["CSC_DGCO"].Habilitado = False
#Formulario["CSC_EMPRESA"].Visivel = False
#Formulario["CSC_EMPRESA"].Habilitado = False
#Formulario["CSC_EMPRESA"].Valor = None
#Formulario["DATA_FIM_PREVIST"].Visivel = False
#Formulario["DATA_FIM_PREVIST"].Habilitado = False
#Formulario["DATA_FIM_PREVIST"].Valor = None
#Formulario["DATA_ATIVIDADE"].Visivel = False
#Formulario["DATA_ATIVIDADE"].Habilitado = False
#Formulario["DATA_ATIVIDADE"].Valor = None
#Formulario["OBJETO_CONTRATACAO"].Visivel = False
#Formulario["OBJETO_CONTRATACAO"].Habilitado = False
#Formulario["OBJETO_CONTRATACAO"].Valor = None
#
#Formulario["CSC_CARGO_LISTA"].Visivel = False
#Formulario["CSC_CARGO_LISTA"].Habilitado = False
#Formulario["CSC_CARGO_LISTA"].Valor = None
#Formulario["CSC_DATA_FIM"].Visivel = False
#Formulario["CSC_DATA_FIM"].Habilitado = False
#Formulario["CSC_DATA_FIM"].Valor = None
#Formulario["CSC_DATA_INICIO"].Visivel = False
#Formulario["CSC_DATA_INICIO"].Habilitado = False
#Formulario["CSC_DATA_INICIO"].Valor = None
#Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = False
#Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = False
#Formulario["CSC_LOCALIDADE_ATUACAO"].Valor = None
#Formulario["CSC_UOR_LISTA"].Visivel = False
#Formulario["CSC_UOR_LISTA"].Habilitado = False
#Formulario["CSC_UOR_LISTA"].Valor = None
#

#



if OrdemServico.Servico.Sigla.ToString() == 'CADTRABALHADORTEMPORARIO':
    #Formulario["CSC_NOME_COMPLETO"].Visivel = True
    #Formulario["CSC_NOME_COMPLETO"].Habilitado = True
    #Formulario["CSC_EMAIL_PESSOAL"].Visivel = True
    #Formulario["CSC_EMAIL_PESSOAL"].Habilitado = True
    #Formulario["CSC_LOGRADOURO"].Visivel = True
    #Formulario["CSC_LOGRADOURO"].Habilitado = True
    #Formulario["CSC_NUMERO"].Visivel = True
    #Formulario["CSC_NUMERO"].Habilitado = True
    #Formulario["CSC_COMPLEMENTO"].Visivel = True
    #Formulario["CSC_COMPLEMENTO"].Habilitado = True
    #Formulario["CSC_BAIRRO"].Visivel = True
    #Formulario["CSC_BAIRRO"].Habilitado = True
    #Formulario["CSC_UF"].Visivel = True
    #Formulario["CSC_UF"].Habilitado = True
    #Formulario["CSC_CIDADE"].Visivel = True
    #Formulario["CSC_CIDADE"].Habilitado = True
    #Formulario["CSC_CEP"].Visivel = True
    #Formulario["CSC_CEP"].Habilitado = True
    #Formulario["CSC_CPF"].Visivel = True
    #Formulario["CSC_CPF"].Habilitado = True
    #Formulario["CSC_RG"].Visivel = True
    #Formulario["CSC_RG"].Habilitado = True
    #Formulario["CSC_DATA_EMISSOA"].Visivel = True
    #Formulario["CSC_DATA_EMISSOA"].Habilitado = True
    #Formulario["CSC_ORGAO_EMISSOR"].Visivel = True
    #Formulario["CSC_ORGAO_EMISSOR"].Habilitado = True
    #Formulario["CSC_ESTADO_EMISSOR"].Visivel = True
    #Formulario["CSC_ESTADO_EMISSOR"].Habilitado = True
    #Formulario["CSC_TELEFONE_CONTATO"].Visivel = True
    #Formulario["CSC_TELEFONE_CONTATO"].Habilitado = True
    #Formulario["CSC_DATA_NASCIMENTO"].Visivel = True
    #Formulario["CSC_DATA_NASCIMENTO"].Habilitado = True
    #Formulario["CSC_UF_NASCIMENTO"].Visivel = True
    #Formulario["CSC_UF_NASCIMENTO"].Habilitado = True
    #Formulario["CSC_CIDADE_NASCIMENTO"].Visivel = True
    #Formulario["CSC_CIDADE_NASCIMENTO"].Habilitado = True
    #Formulario["CSC_ESTADO_CIVIL"].Visivel = True
    #Formulario["CSC_ESTADO_CIVIL"].Habilitado = True
    #Formulario["CSC_ESCOLARIDADE"].Visivel = False
    #Formulario["CSC_ESCOLARIDADE"].Habilitado = True
    #Formulario["SEXO_M_F"].Visivel = True
    #Formulario["SEXO_M_F"].Habilitado = True
    #Formulario["CSC_BANCO"].Visivel = True
    #Formulario["CSC_BANCO"].Habilitado = True
    #Formulario["CSC_CONTA_CORRENTE"].Visivel = True
    #Formulario["CSC_CONTA_CORRENTE"].Habilitado = True
    #Formulario["CSC_DIGITO_AGENCIA"].Visivel = True
    #Formulario["CSC_DIGITO_AGENCIA"].Habilitado = True
    #Formulario["CSC_DIGITO_CONTA_CORRENTE"].Visivel = True
    #Formulario["CSC_DIGITO_CONTA_CORRENTE"].Habilitado = True
    #Formulario["CSC_NOME_AGENCIA"].Visivel = True
    #Formulario["CSC_NOME_AGENCIA"].Habilitado = True
    #Formulario["CSC_NUMERO_AGENCIA"].Visivel = True
    #Formulario["CSC_NUMERO_AGENCIA"].Habilitado = True
    #Formulario["CSC_DGCO"].Visivel = True
    #Formulario["CSC_DGCO"].Habilitado = True
    #Formulario["CSC_EMPRESA"].Visivel = True
    #Formulario["CSC_EMPRESA"].Habilitado = True
    #Formulario["CSC_CARGO_LISTA"].Visivel = True
    #Formulario["CSC_CARGO_LISTA"].Habilitado = True
    #Formulario["CSC_DATA_FIM"].Visivel = True
    #Formulario["CSC_DATA_FIM"].Habilitado = True
    #Formulario["CSC_DATA_INICIO"].Visivel = True
    #Formulario["CSC_DATA_INICIO"].Habilitado = True
    #Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = True
    #Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = True
    #Formulario["CSC_UOR_LISTA"].Visivel = True
    #Formulario["CSC_UOR_LISTA"].Habilitado = True
    #Formulario["CSC_ACESSO_ERP"].Visivel = False
    #Formulario["CSC_ACESSO_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = True
    Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = True
    ##Formulario["CSC_ACESSO_SICON"].Visivel = False
    ##Formulario["CSC_ACESSO_SICON"].Habilitado = False
    #Formulario["CSC_ACESSO_SISBB"].Visivel = False
    #Formulario["CSC_ACESSO_SISBB"].Habilitado = False
    ##Formulario["CSC_ACESSO_TOA"].Visivel = False
    ##Formulario["CSC_ACESSO_TOA"].Habilitado = False
    #Formulario["CSC_ACESSO_VPN"].Visivel = False
    #Formulario["CSC_ACESSO_VPN"].Habilitado = False
    #Formulario["CSC_ACESSO_WIFI"].Visivel = False
    #Formulario["CSC_ACESSO_WIFI"].Habilitado = False
    #Formulario["LABEL2"].Visivel = False
    #Formulario["LABEL2"].Habilitado = False
    #Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    #Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    #Formulario["CSC_DATA_INICIO"].Visivel = True
    #Formulario["CSC_DATA_INICIO"].Habilitado = True
    
if OrdemServico.Servico.Sigla.ToString() == 'PRORTRABALHADORTEMPORARIO':
    Formulario["CSC_NOME_COMPLETO"].Visivel = False
    Formulario["CSC_NOME_COMPLETO"].Habilitado = False
    Formulario["CSC_NOME_COMPLETO"].Valor = None
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = True
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = True
    Formulario["CSC_EMAIL_PESSOAL"].Visivel = False
    Formulario["CSC_EMAIL_PESSOAL"].Habilitado = False
    Formulario["CSC_LOGRADOURO"].Visivel = True
    Formulario["CSC_LOGRADOURO"].Habilitado = True
    Formulario["CSC_NUMERO"].Visivel = True
    Formulario["CSC_NUMERO"].Habilitado = True
    Formulario["CSC_COMPLEMENTO"].Visivel = False
    Formulario["CSC_COMPLEMENTO"].Habilitado = False
    Formulario["CSC_BAIRRO"].Visivel = True
    Formulario["CSC_BAIRRO"].Habilitado = True
    Formulario["CSC_UF"].Visivel = True
    Formulario["CSC_UF"].Habilitado = True
    Formulario["CSC_CIDADE"].Visivel = True
    Formulario["CSC_CIDADE"].Habilitado = True
    Formulario["CSC_CEP"].Visivel = True
    Formulario["CSC_CEP"].Habilitado = True
    Formulario["CSC_CPF"].Visivel = True
    Formulario["CSC_CPF"].Habilitado = True
    Formulario["CSC_RG"].Visivel = False
    Formulario["CSC_RG"].Habilitado = False
    Formulario["CSC_DATA_EMISSOA"].Visivel = False
    Formulario["CSC_DATA_EMISSOA"].Habilitado = False
    Formulario["CSC_ORGAO_EMISSOR"].Visivel = False
    Formulario["CSC_ORGAO_EMISSOR"].Habilitado = False
    Formulario["CSC_ESTADO_EMISSOR"].Visivel = False
    Formulario["CSC_ESTADO_EMISSOR"].Habilitado = False
    Formulario["CSC_TELEFONE_CONTATO"].Visivel = True
    Formulario["CSC_TELEFONE_CONTATO"].Habilitado = True
    Formulario["CSC_DATA_NASCIMENTO"].Visivel = True
    Formulario["CSC_DATA_NASCIMENTO"].Habilitado = True
    Formulario["CSC_UF_NASCIMENTO"].Visivel = True
    Formulario["CSC_UF_NASCIMENTO"].Habilitado = True
    Formulario["CSC_CIDADE_NASCIMENTO"].Visivel = True
    Formulario["CSC_CIDADE_NASCIMENTO"].Habilitado = True
    Formulario["CSC_ESTADO_CIVIL"].Visivel = True
    Formulario["CSC_ESTADO_CIVIL"].Habilitado = True
    Formulario["CSC_ESCOLARIDADE"].Visivel = True
    Formulario["CSC_ESCOLARIDADE"].Habilitado = True
    Formulario["SEXO_M_F"].Visivel = True
    Formulario["SEXO_M_F"].Habilitado = True
    Formulario["MATRICULA"].Visivel = False
    Formulario["MATRICULA"].Habilitado = False
    Formulario["SIM_NAO5"].Visivel = False
    Formulario["SIM_NAO5"].Habilitado = False

    
    Formulario["CSC_BANCO"].Visivel = False
    Formulario["CSC_BANCO"].Habilitado = False
    Formulario["CSC_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_DIGITO_AGENCIA"].Visivel = False
    Formulario["CSC_DIGITO_AGENCIA"].Habilitado = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_NOME_AGENCIA"].Visivel = False
    Formulario["CSC_NOME_AGENCIA"].Habilitado = False
    Formulario["CSC_NUMERO_AGENCIA"].Visivel = False
    Formulario["CSC_NUMERO_AGENCIA"].Habilitado = False
    
    Formulario["CSC_DGCO"].Visivel = True
    Formulario["CSC_DGCO"].Habilitado = True
    Formulario["CSC_EMPRESA"].Visivel = True
    Formulario["CSC_EMPRESA"].Habilitado = True
    Formulario["DATA_FIM_PREVIST"].Visivel = False
    Formulario["DATA_FIM_PREVIST"].Habilitado = False
    Formulario["DATA_FIM_PREVIST"].Valor = None
    Formulario["DATA_ATIVIDADE"].Visivel = False
    Formulario["DATA_ATIVIDADE"].Habilitado = False
    Formulario["DATA_ATIVIDADE"].Valor = None
    Formulario["OBJETO_CONTRATACAO"].Visivel = False
    Formulario["OBJETO_CONTRATACAO"].Habilitado = False
    Formulario["OBJETO_CONTRATACAO"].Valor = None
    
    Formulario["CSC_CARGO_LISTA"].Visivel = True
    Formulario["CSC_CARGO_LISTA"].Habilitado = True
    Formulario["CSC_DATA_FIM"].Visivel = True
    Formulario["CSC_DATA_FIM"].Habilitado = True
    Formulario["CSC_DATA_INICIO"].Visivel = True
    Formulario["CSC_DATA_INICIO"].Habilitado = True
    Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = True
    Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = True
    Formulario["CSC_UOR_LISTA"].Visivel = True
    Formulario["CSC_UOR_LISTA"].Habilitado = True
    
    Formulario["CSC_ACESSO_ERP"].Visivel = False
    Formulario["CSC_ACESSO_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = True
    Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = True
    #Formulario["CSC_ACESSO_SICON"].Visivel = False
    #Formulario["CSC_ACESSO_SICON"].Habilitado = False
    Formulario["CSC_ACESSO_SISBB"].Visivel = False
    Formulario["CSC_ACESSO_SISBB"].Habilitado = False
    #Formulario["CSC_ACESSO_TOA"].Visivel = False
    #Formulario["CSC_ACESSO_TOA"].Habilitado = False
    Formulario["CSC_ACESSO_VPN"].Visivel = False
    Formulario["CSC_ACESSO_VPN"].Habilitado = False
    Formulario["CSC_ACESSO_WIFI"].Visivel = False
    Formulario["CSC_ACESSO_WIFI"].Habilitado = False
    Formulario["LABEL2"].Visivel = True
    Formulario["LABEL2"].Habilitado = True
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Visivel = True
    Formulario["CSC_ACESSO_PEOPLESOFT"].Habilitado = True
    
if OrdemServico.Servico.Sigla.ToString() == 'DESTRABALHADORTEMPORARIO':
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = True
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = True
    Formulario["CSC_EMAIL_PESSOAL"].Visivel = False
    Formulario["CSC_EMAIL_PESSOAL"].Habilitado = False
    Formulario["CSC_LOGRADOURO"].Visivel = True
    Formulario["CSC_LOGRADOURO"].Habilitado = True
    Formulario["CSC_NUMERO"].Visivel = True
    Formulario["CSC_NUMERO"].Habilitado = True
    Formulario["CSC_COMPLEMENTO"].Visivel = False
    Formulario["CSC_COMPLEMENTO"].Habilitado = False
    Formulario["CSC_BAIRRO"].Visivel = True
    Formulario["CSC_BAIRRO"].Habilitado = True
    Formulario["CSC_UF"].Visivel = True
    Formulario["CSC_UF"].Habilitado = True
    Formulario["CSC_CIDADE"].Visivel = True
    Formulario["CSC_CIDADE"].Habilitado = True
    Formulario["CSC_CEP"].Visivel = True
    Formulario["CSC_CEP"].Habilitado = True
    Formulario["CSC_CPF"].Visivel = True
    Formulario["CSC_CPF"].Habilitado = True
    Formulario["CSC_RG"].Visivel = False
    Formulario["CSC_RG"].Habilitado = False
    Formulario["CSC_DATA_EMISSOA"].Visivel = False
    Formulario["CSC_DATA_EMISSOA"].Habilitado = False
    Formulario["CSC_ORGAO_EMISSOR"].Visivel = False
    Formulario["CSC_ORGAO_EMISSOR"].Habilitado = False
    Formulario["CSC_ESTADO_EMISSOR"].Visivel = False
    Formulario["CSC_ESTADO_EMISSOR"].Habilitado = False
    Formulario["CSC_TELEFONE_CONTATO"].Visivel = True
    Formulario["CSC_TELEFONE_CONTATO"].Habilitado = True
    Formulario["CSC_DATA_NASCIMENTO"].Visivel = True
    Formulario["CSC_DATA_NASCIMENTO"].Habilitado = True
    Formulario["CSC_UF_NASCIMENTO"].Visivel = True
    Formulario["CSC_UF_NASCIMENTO"].Habilitado = True
    Formulario["CSC_CIDADE_NASCIMENTO"].Visivel = True
    Formulario["CSC_CIDADE_NASCIMENTO"].Habilitado = True
    Formulario["CSC_ESTADO_CIVIL"].Visivel = True
    Formulario["CSC_ESTADO_CIVIL"].Habilitado = True
    Formulario["CSC_ESCOLARIDADE"].Visivel = True
    Formulario["CSC_ESCOLARIDADE"].Habilitado = True
    Formulario["SEXO_M_F"].Visivel = True
    Formulario["SEXO_M_F"].Habilitado = True

    
    Formulario["CSC_BANCO"].Visivel = False
    Formulario["CSC_BANCO"].Habilitado = False
    Formulario["CSC_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_DIGITO_AGENCIA"].Visivel = False
    Formulario["CSC_DIGITO_AGENCIA"].Habilitado = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_NOME_AGENCIA"].Visivel = False
    Formulario["CSC_NOME_AGENCIA"].Habilitado = False
    Formulario["CSC_NUMERO_AGENCIA"].Visivel = False
    Formulario["CSC_NUMERO_AGENCIA"].Habilitado = False
    
    Formulario["CSC_DGCO"].Visivel = False
    Formulario["CSC_DGCO"].Habilitado = False
    Formulario["CSC_EMPRESA"].Visivel = False
    Formulario["CSC_EMPRESA"].Habilitado = False
    
    Formulario["CSC_CARGO_LISTA"].Visivel = False
    Formulario["CSC_CARGO_LISTA"].Habilitado = False
    Formulario["CSC_DATA_FIM"].Visivel = True
    Formulario["CSC_DATA_FIM"].Habilitado = True
    Formulario["CSC_DATA_INICIO"].Visivel = False
    Formulario["CSC_DATA_INICIO"].Habilitado = False
    Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = True
    Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = True
    Formulario["CSC_UOR_LISTA"].Visivel = True
    Formulario["CSC_UOR_LISTA"].Habilitado = True
    
    Formulario["CSC_ACESSO_ERP"].Visivel = False
    Formulario["CSC_ACESSO_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = True
    Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = True
    #Formulario["CSC_ACESSO_SICON"].Visivel = False
    #Formulario["CSC_ACESSO_SICON"].Habilitado = False
    Formulario["CSC_ACESSO_SISBB"].Visivel = False
    Formulario["CSC_ACESSO_SISBB"].Habilitado = False
    #Formulario["CSC_ACESSO_TOA"].Visivel = False
    #Formulario["CSC_ACESSO_TOA"].Habilitado = False
    Formulario["CSC_ACESSO_VPN"].Visivel = False
    Formulario["CSC_ACESSO_VPN"].Habilitado = False
    Formulario["CSC_ACESSO_WIFI"].Visivel = False
    Formulario["CSC_ACESSO_WIFI"].Habilitado = False
    Formulario["LABEL2"].Visivel = True
    Formulario["LABEL2"].Habilitado = True
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Visivel = True
    Formulario["CSC_ACESSO_PEOPLESOFT"].Habilitado = True
    Formulario["MATRICULA"].Visivel = True
    Formulario["MATRICULA"].Habilitado = True
    Formulario["SIM_NAO5"].Visivel = True
    Formulario["SIM_NAO5"].Habilitado = True

if OrdemServico.Servico.Sigla == "DESTRABALHADORTEMPORARIO":
    Formulario["CSC_ACESSO_ERP"].Visivel = False
    Formulario["CSC_ACESSO_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = False
    Formulario["CSC_ACESSO_SISBB"].Visivel = False
    Formulario["CSC_ACESSO_SISBB"].Habilitado = False
    Formulario["CSC_ACESSO_VPN"].Visivel = False
    Formulario["CSC_ACESSO_VPN"].Habilitado = False
    Formulario["CSC_ACESSO_WIFI"].Visivel = False
    Formulario["CSC_ACESSO_WIFI"].Habilitado = False
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Visivel = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Habilitado = False
    Formulario["MATRICULA"].Visivel = True
    Formulario["MATRICULA"].Habilitado = True
    Formulario["SIM_NAO5"].Visivel = True
    Formulario["SIM_NAO5"].Habilitado = True
    
if OrdemServico.Servico.Sigla == "RECADASTRAMENTOPOSTO":
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = True
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = True
    Formulario["CSC_NOME_COMPLETO"].Visivel = False
    Formulario["CSC_NOME_COMPLETO"].Habilitado = False
    Formulario["CSC_EMAIL_PESSOAL"].Visivel = False
    Formulario["CSC_EMAIL_PESSOAL"].Habilitado = False
    Formulario["CSC_LOGRADOURO"].Visivel = False
    Formulario["CSC_LOGRADOURO"].Habilitado = False
    Formulario["CSC_NUMERO"].Visivel = False
    Formulario["CSC_NUMERO"].Habilitado = False
    Formulario["CSC_COMPLEMENTO"].Visivel = False
    Formulario["CSC_COMPLEMENTO"].Habilitado = False
    Formulario["CSC_BAIRRO"].Visivel = False
    Formulario["CSC_BAIRRO"].Habilitado = False
    Formulario["CSC_UF"].Visivel = False
    Formulario["CSC_UF"].Habilitado = False
    Formulario["CSC_CIDADE"].Visivel = False
    Formulario["CSC_CIDADE"].Habilitado = False
    Formulario["CSC_CEP"].Visivel = False
    Formulario["CSC_CEP"].Habilitado = False
    Formulario["CSC_CPF"].Visivel = True
    Formulario["CSC_CPF"].Habilitado = True
    Formulario["CSC_RG"].Visivel = False
    Formulario["CSC_RG"].Habilitado = False
    Formulario["CSC_DATA_EMISSOA"].Visivel = False
    Formulario["CSC_DATA_EMISSOA"].Habilitado = False
    Formulario["CSC_ORGAO_EMISSOR"].Visivel = False
    Formulario["CSC_ORGAO_EMISSOR"].Habilitado = False
    Formulario["CSC_ESTADO_EMISSOR"].Visivel = False
    Formulario["CSC_ESTADO_EMISSOR"].Habilitado = False
    Formulario["CSC_TELEFONE_CONTATO"].Visivel = False
    Formulario["CSC_TELEFONE_CONTATO"].Habilitado = False
    Formulario["CSC_DATA_NASCIMENTO"].Visivel = False
    Formulario["CSC_DATA_NASCIMENTO"].Habilitado = False
    Formulario["CSC_UF_NASCIMENTO"].Visivel = False
    Formulario["CSC_UF_NASCIMENTO"].Habilitado = False
    Formulario["CSC_CIDADE_NASCIMENTO"].Visivel = False
    Formulario["CSC_CIDADE_NASCIMENTO"].Habilitado = False
    Formulario["CSC_ESTADO_CIVIL"].Visivel = False
    Formulario["CSC_ESTADO_CIVIL"].Habilitado = False
    Formulario["CSC_ESCOLARIDADE"].Visivel = False
    Formulario["CSC_ESCOLARIDADE"].Habilitado = False
    Formulario["SEXO_M_F"].Visivel = False
    Formulario["SEXO_M_F"].Habilitado = False
    Formulario["CSC_BANCO"].Visivel = False
    Formulario["CSC_BANCO"].Habilitado = False
    Formulario["CSC_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_DIGITO_AGENCIA"].Visivel = False
    Formulario["CSC_DIGITO_AGENCIA"].Habilitado = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_NOME_AGENCIA"].Visivel = False
    Formulario["CSC_NOME_AGENCIA"].Habilitado = False
    Formulario["CSC_NUMERO_AGENCIA"].Visivel = False
    Formulario["CSC_NUMERO_AGENCIA"].Habilitado = False
    
    Formulario["CSC_DGCO"].Visivel = True
    Formulario["CSC_DGCO"].Habilitado = True
    Formulario["CSC_EMPRESA"].Visivel = True
    Formulario["CSC_EMPRESA"].Habilitado = False
    Formulario["DATA_ATIVIDADE"].Visivel = True
    Formulario["DATA_ATIVIDADE"].Habilitado = True
    Formulario["DATA_FIM_PREVIST"].Visivel = True
    Formulario["DATA_FIM_PREVIST"].Habilitado = True
    Formulario["OBJETO_CONTRATACAO"].Visivel = True
    Formulario["OBJETO_CONTRATACAO"].Habilitado = False
    
    Formulario["CSC_CARGO_LISTA"].Visivel = False
    Formulario["CSC_CARGO_LISTA"].Habilitado = False
    Formulario["CSC_DATA_FIM"].Visivel = True
    Formulario["CSC_DATA_FIM"].Habilitado = True
    Formulario["CSC_DATA_INICIO"].Visivel = True
    Formulario["CSC_DATA_INICIO"].Habilitado = True
    Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = True
    Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = True
    Formulario["CSC_UOR_LISTA"].Visivel = True
    Formulario["CSC_UOR_LISTA"].Habilitado = True
    
    Formulario["CSC_ACESSO_ERP"].Visivel = False
    Formulario["CSC_ACESSO_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = True
    Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = True
    #Formulario["CSC_ACESSO_SICON"].Visivel = False
    #Formulario["CSC_ACESSO_SICON"].Habilitado = False
    Formulario["CSC_ACESSO_SISBB"].Visivel = False
    Formulario["CSC_ACESSO_SISBB"].Habilitado = False
    #Formulario["CSC_ACESSO_TOA"].Visivel = False
    #Formulario["CSC_ACESSO_TOA"].Habilitado = False
    Formulario["CSC_ACESSO_VPN"].Visivel = False
    Formulario["CSC_ACESSO_VPN"].Habilitado = False
    Formulario["CSC_ACESSO_WIFI"].Visivel = False
    Formulario["CSC_ACESSO_WIFI"].Habilitado = False
    Formulario["LABEL2"].Visivel = True
    Formulario["LABEL2"].Habilitado = True
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Visivel = True
    Formulario["CSC_ACESSO_PEOPLESOFT"].Habilitado = True
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Acesso aos Sistemas
  - CSC_ACESSO_ERP "Acesso ERP" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_ERP] obrigatório
**CSC_ACESSO_ERP.ScriptModificado**
```python
Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
OrdemServico.SetCustom("CSC_LISTA_RESP_ERP", None)
if Formulario["CSC_ACESSO_ERP"].Valor == True:
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = True
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = True
    OrdemServico.SetCustom("CSC_LISTA_RESP_ERP", None)
    
if OrdemServico.Servico.Sigla == "RECADASTRAMENTOPOSTO":
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    OrdemServico.SetCustom("CSC_LISTA_RESP_ERP", None)
    if Formulario["CSC_ACESSO_ERP"].Valor == True:
        Formulario["CSC_LISTA_RESP_ERP"].Visivel = True
        Formulario["CSC_LISTA_RESP_ERP"].Habilitado = True
        OrdemServico.SetCustom("CSC_LISTA_RESP_ERP", None)
```
  - CSC_ACESSO_SICON "Acesso SICON" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_SICON] obrigatório
  - CSC_ACESSO_SISBB "Acesso SISBB" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_SISBB] obrigatório
  - CSC_ACESSO_WIFI "Acesso Wi-fi" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_WIFI] obrigatório
  - CSC_LISTA_RESP_ERP "Nome da Responsabilidade no ERP - Neste campo, indicar todos os módulos que necessita para o Sistema ERP" [DataGrid RecordList → Z_00143_CSC_LISTA_RESP_ERP.CSC_LISTA_RESP_ERP] — QtdColunasFormulario=1
**CSC_LISTA_RESP_ERP.ScriptAdicionado**
```python
if OrdemServico.Servico.Sigla.ToString() != 'CADTRABALHADORTEMPORARIO':
    dt= OrdemServico.GetCustom("CSC_LISTA_RESP_ERP")
    mat = OrdemServico.GetCustom("CSC_TRABALHADOR_TEMPORARIO")
    if dt.Rows.Count == 0:
        #sql_erp = "select ROWNUM-1 as RECID, RESP AS MODULOS from ERP_RESP_V where MATRICULA = '3829'"
        sql_erp = "select ROWNUM as RECID, RESPONSABILIDADE AS MODULOS from ERP_RESP_V where MATRICULA = '"+mat.ToString()+"'"
        info_erp = DB.ExecuteDataTable(sql_erp)
        if info_erp.Rows.Count == 0:
            Tabela.Clear()
        else:
            for linha_x in info_erp.Rows:
                Tabela.NewRow()
                Tabela.ImportRow(linha_x)
```
**CSC_LISTA_RESP_ERP.ScriptConfirmado**
```python
#Formulario.ExibeMensagem(Formulario['CSC_TRABALHADOR_TEMPORARIO'].Valor.ToString()+'sdfsdfs')
```
    - coluna MODULOS obrigatório
  - CSC_ACESSO_PEOPLESOFT "Acesso LG" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_PEOPLESOFT]
  - LABEL2 "IMPORTANTE: O ACESSO AO TOA É VIA OTRS: https://otrs.bbts.com.br/otrs/customer.pl?Action=CustomerTicketOverview;Subaction=MyTickets" [Label String(2000) → CP_ORDEM_SERVICO.LABEL2]
  - CSC_ACESSO_REDE_EMAIL "Acesso Rede e E-mail" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_REDE_EMAIL] obrigatório
**CSC_ACESSO_REDE_EMAIL.ScriptModificado**
```python
Formulario["CSC_ACESSO_ERP"].Visivel = False
Formulario["CSC_ACESSO_ERP"].Habilitado = False
Formulario["CSC_ACESSO_SICON"].Visivel = False
Formulario["CSC_ACESSO_SICON"].Habilitado = False
Formulario["CSC_ACESSO_SISBB"].Visivel = False
Formulario["CSC_ACESSO_SISBB"].Habilitado = False
#Formulario["CSC_ACESSO_TOA"].Visivel = False
#Formulario["CSC_ACESSO_TOA"].Habilitado = False
Formulario["CSC_ACESSO_VPN"].Visivel = False
Formulario["CSC_ACESSO_VPN"].Habilitado = False
Formulario["CSC_ACESSO_WIFI"].Visivel = False
Formulario["CSC_ACESSO_WIFI"].Habilitado = False
Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
```
  - CSC_ACESSO_VPN "Acesso VPN" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_VPN] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados da Área BBTS Solicitante do Trabalhador Temporário
  - CSC_LOCALIDADE_ATUACAO "Localidade Atuação" [DropDownList String → CPE_CSC.CSC_LOCALIDADE_ATUACAO] obrigatório
  - CSC_CAT "Local de Atendimento (Somente para Gered)" [DropDownList String → CPE_CSC.CSC_CAT]
  - CSC_DATA_FIM "Saída da BBTS" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM] obrigatório
  - CSC_UOR_LISTA "UOR da Área Solicitante" [DropDownList String(500) → CPE_CSC.CSC_UOR_LISTA] obrigatório
  - CSC_CARGO_LISTA "Cargo que o Trabalhador ocupará" [DropDownList String(100) → CPE_CSC.CSC_CARGO_LISTA] obrigatório
  - CSC_DATA_INICIO "Início na BBTS (Contrato atual)" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados do Trabalhador Temporário
  - CSC_ESTADO_EMISSOR "Estado Emissor" [DropDownList String(500) → CPE_CSC.CSC_ESTADO_EMISSOR]
  - CSC_TELEFONE_CONTATO "Telefone para Contato" [TextBox String → CPE_CSC.CSC_TELEFONE_CONTATO] obrigatório
  - CSC_CIDADE_NASCIMENTO "Cidade de Nascimento" [TextBox String(500) → CPE_CSC.CSC_CIDADE_NASCIMENTO] obrigatório
  - CSC_ESTADO_CIVIL "Estado Civil" [DropDownList String → CPE_CSC.CSC_ESTADO_CIVIL] obrigatório
  - CSC_ESCOLARIDADE "Escolaridade" [TextBox String → CPE_CSC.CSC_ESCOLARIDADE] obrigatório
  - CSC_DATA_NASCIMENTO "Data de nascimento" [DatePicker DateTime → CPE_CSC.CSC_DATA_NASCIMENTO] obrigatório
  - SEXO_M_F "Sexo" [DropDownList String → CPE_CSC.SEXO_M_F] obrigatório
  - CSC_UF_NASCIMENTO "UF de Nascimento" [DropDownList String → CPE_CSC.CSC_UF_NASCIMENTO] obrigatório
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO]
  - CSC_LOGRADOURO "Logradouro" [TextBox String(500) → CPE_CSC.CSC_LOGRADOURO] obrigatório
  - CSC_NUMERO "Número" [TextBox String(100) → CPE_CSC.CSC_NUMERO] obrigatório
  - CSC_COMPLEMENTO "Complemento" [TextBox String(500) → CPE_CSC.CSC_COMPLEMENTO]
  - CSC_BAIRRO "Bairro" [TextBox String(500) → CPE_CSC.CSC_BAIRRO] obrigatório
  - CSC_UF "UF" [DropDownList String → CPE_CSC.CSC_UF] obrigatório
  - CSC_CIDADE "Cidade" [TextBox String(500) → CPE_CSC.CSC_CIDADE] obrigatório
  - CSC_CEP "CEP" [TextBox String → CPE_CSC.CSC_CEP] obrigatório — Configuracao={"SalvaLiteralMascara":false, "Mascara":"00000\\-000"}
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF] — Configuracao={"SalvaLiteralMascara":false, "Mascara":"000\\.000\\.000\\-00"}
  - CSC_RG "RG" [TextBox String → CPE_CSC.CSC_RG]
  - CSC_TRABALHADOR_TEMPORARIO "Trabalhador Temporário" [DropDownList String → CPE_CSC.CSC_TRABALHADOR_TEMPORARIO] obrigatório
**CSC_TRABALHADOR_TEMPORARIO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["CSC_EMAIL_PESSOAL"].Valor = None
Formulario["CSC_LOGRADOURO"].Valor = None
Formulario["CSC_NUMERO"].Valor = None
Formulario["CSC_COMPLEMENTO"].Valor = None
Formulario["CSC_BAIRRO"].Valor = None
Formulario["CSC_UF"].Valor = None
Formulario["CSC_CIDADE"].Valor = None
Formulario["CSC_CEP"].Valor = None
Formulario["CSC_CPF"].Valor = None
Formulario["CSC_RG"].Valor = None
Formulario["CSC_DATA_EMISSOA"].Valor = None
Formulario["CSC_ORGAO_EMISSOR"].Valor = None
Formulario["CSC_ESTADO_EMISSOR"].Valor = None
Formulario["CSC_TELEFONE_CONTATO"].Valor = None
Formulario["CSC_DATA_NASCIMENTO"].Valor = None
Formulario["CSC_UF_NASCIMENTO"].Valor = None
Formulario["CSC_CIDADE_NASCIMENTO"].Valor = None
Formulario["CSC_ESTADO_CIVIL"].Valor = None
Formulario["CSC_BANCO"].Valor = None
Formulario["CSC_CONTA_CORRENTE"].Valor = None
Formulario["CSC_DIGITO_AGENCIA"].Valor = None
Formulario["CSC_DIGITO_CONTA_CORRENTE"].Valor = None
Formulario["CSC_NOME_AGENCIA"].Valor = None
Formulario["CSC_NUMERO_AGENCIA"].Valor = None
Formulario["CSC_UOR_LISTA"].Valor = None
Formulario["CSC_ACESSO_REDE_EMAIL"].Valor = False
Formulario["CSC_ACESSO_SICON"].Valor = False
Formulario["CSC_ACESSO_VPN"].Valor = False
Formulario["CSC_ACESSO_SISBB"].Valor = False
Formulario["CSC_ACESSO_WIFI"].Valor = False
Formulario["CSC_ACESSO_ERP"].Valor = False
Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
Formulario["LABEL2"].Valor = ""
Formulario["LABEL2"].Visivel = False

sql = "SELECT ID, EMAIL_PESSOAL, NOME, ENDERECO, NRO_END, COMPLEMENTO_END, BAIRRO, TO_CHAR(ESTADO) AS ESTADO, CIDADE, CEP, CPF, RG, EMISSAO, RG_ORGAO_EMISSOR, TO_CHAR(RG_ESTADO_EMISSOR) AS RG_ESTADO_EMISSOR, TELEFONE, DATA_NASCIMENTO, TO_CHAR(ESTADO_NASCIMENTO) AS ESTADO_NASCIMENTO, CIDADE_NASCIMENTO, ESTADO_CIVIL, CODIGO_BANCO, CODIGO_AGENCIA, DIGITO_AGENCIA, NOME_AGENCIA, CONTA_NUMERO, CONTA_DIGITO, UOR FROM VW_BBTS_TRABALHADOR_TEMPORARIO WHERE ID = '"+Controle.Valor.ToString()+"'"

sql = "select DISTINCT PAPF.npw_number as ID, NULL AS EMAIL_PESSOAL,PAPF.full_name as NOME, pa.address_line1 AS ENDERECO, pa.address_line2 AS NRO_END, pa.address_line3 AS COMPLEMENTO_END, pa.region_1 AS BAIRRO, pa.region_2 AS ESTADO, pa.town_or_city AS CIDADE, pa.postal_code AS CEP,PAPF.NATIONAL_IDENTIFIER as CPF, PA.TELEPHONE_NUMBER_1 AS TELEFONE, NVL(TO_CHAR(PAPF.DATE_OF_BIRTH, 'DD/MM/RRRR'),'01/01/1900') AS DATA_NASCIMENTO, PAPF.TOWN_OF_BIRTH AS CIDADE_NASCIMENTO,'' AS ESTADO_NASCIMENTO, PAPF.MARITAL_STATUS AS ESTADO_CIVIL , NULL AS CODIGO_BANCO, NULL AS CODIGO_AGENCIA, NULL AS DIGITO_AGENCIA, NULL AS NOME_AGENCIA, NULL AS CONTA_NUMERO, NULL AS CONTA_DIGITO, NULL AS UOR, NULL AS RG, '01/01/1900' AS EMISSAO, NULL AS RG_ORGAO_EMISSOR, '' AS RG_ESTADO_EMISSOR from per_all_people_f PAPF INNER JOIN per_all_assignments_f PAAF ON paaf.person_id = papf.person_id INNER JOIN per_addresses PA ON pa.person_id = papf.person_id where PAPF.EFFECTIVE_START_DATE = (SELECT MAX(PAPF1.EFFECTIVE_START_DATE)FROM per_all_people_f PAPF1 WHERE papf1.person_id = papf.person_id) AND PAAF.EFFECTIVE_START_DATE = (SELECT MAX(PAAF1.EFFECTIVE_START_DATE)FROM per_all_assignments_f PAAF1 WHERE PAAF1.person_id = PAAF.person_id) AND (PAPF.npw_number = '"+Controle.Valor.ToString()+"' or PAPF.employee_number = '"+Controle.Valor.ToString()+"')"


info = DB.ExecuteDataTable(sql)
if info.Rows.Count >=1:
    for linha in info.Rows:
        #Formulario["CSC_EMAIL_PESSOAL"].Valor = linha['EMAIL_PESSOAL'].ToString()
        #Formulario["CSC_LOGRADOURO"].Valor = linha['ENDERECO'].ToString()
        #Formulario["CSC_NUMERO"].Valor = linha['NRO_END'].ToString()
        #Formulario["CSC_COMPLEMENTO"].Valor = linha['COMPLEMENTO_END'].ToString()
        #Formulario["CSC_BAIRRO"].Valor = linha['BAIRRO'].ToString()
        #Formulario["CSC_UF"].Valor = linha['ESTADO'].ToString()
        #Formulario["CSC_CIDADE"].Valor = linha['CIDADE'].ToString()
        #Formulario["CSC_CEP"].Valor = linha['CEP'].ToString()
        #Formulario["CSC_CPF"].Valor = linha['CPF'].ToString()
        #Formulario["CSC_RG"].Valor = linha['RG'].ToString()
        #Formulario["CSC_DATA_EMISSOA"].Valor = linha['EMISSAO'].ToString()
        #Formulario["CSC_ORGAO_EMISSOR"].Valor = linha['RG_ORGAO_EMISSOR'].ToString()
        #Formulario["CSC_ESTADO_EMISSOR"].Valor = linha['RG_ESTADO_EMISSOR'].ToString()
        #Formulario["CSC_TELEFONE_CONTATO"].Valor = linha['TELEFONE'].ToString()
        #Formulario["CSC_DATA_NASCIMENTO"].Valor = linha['DATA_NASCIMENTO'].ToString()
        #Formulario["CSC_UF_NASCIMENTO"].Valor = linha['ESTADO_NASCIMENTO'].ToString()
        #Formulario["CSC_CIDADE_NASCIMENTO"].Valor = linha['CIDADE_NASCIMENTO'].ToString()
        #Formulario["CSC_ESTADO_CIVIL"].Valor = linha['ESTADO_CIVIL'].ToString()
        #Formulario["CSC_BANCO"].Valor = linha['CODIGO_BANCO'].ToString()
        #Formulario["CSC_CONTA_CORRENTE"].Valor = linha['CONTA_NUMERO'].ToString()
        #Formulario["CSC_DIGITO_AGENCIA"].Valor = linha['DIGITO_AGENCIA'].ToString()
        #Formulario["CSC_DIGITO_CONTA_CORRENTE"].Valor = linha['CONTA_DIGITO'].ToString()
        #Formulario["CSC_NOME_AGENCIA"].Valor = linha['NOME_AGENCIA'].ToString()
        #Formulario["CSC_NUMERO_AGENCIA"].Valor = linha['CODIGO_AGENCIA'].ToString()
        Formulario["CSC_UOR_LISTA"].Valor = linha['UOR'].ToString()
else:
    Formulario.ExibeMensagem("O Trabalhador Temporário selecionado não está devidamente cadastrado no People.")
    

if (OrdemServico.Servico.Sigla.ToString() == 'DESTRABALHADORTEMPORARIO' or OrdemServico.Servico.Sigla.ToString() == 'PRORTRABALHADORTEMPORARIO') and info.Rows.Count >=1:
    Formulario["CSC_ACESSO_REDE_EMAIL"].Valor = False
    Formulario["CSC_ACESSO_SICON"].Valor = False
    Formulario["CSC_ACESSO_VPN"].Valor = False
    Formulario["CSC_ACESSO_SISBB"].Valor = False
    Formulario["CSC_ACESSO_WIFI"].Valor = False
    Formulario["CSC_ACESSO_ERP"].Valor = False
    #OrdemServico.SetCustom("CSC_LISTA_RESP_ERP",None)
    OrdemServico.SetCustom("CSC_TRABALHADOR_TEMPORARIO",linha['ID'].ToString())
    OrdemServico["CSC_LISTA_RESP_ERP"].Rows.Clear()
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    Formulario["LABEL2"].Valor = ""
    sql_si = "select * from SI_ACESSOS where MATRICULA = '"+linha['ID'].ToString()+"'"
    info_si = DB.ExecuteDataTable(sql_si)
    sql_erp = "select RESPONSABILIDADE from ERP_RESP_V where MATRICULA = '"+linha['ID'].ToString()+"'"
    info_erp = DB.ExecuteDataTable(sql_erp)
    for linha_si in info_si.Rows:
        if linha_si["LOGON"] == 'S':
            Formulario["CSC_ACESSO_REDE_EMAIL"].Valor = True
        if linha_si["SICON"] == 'S':
            Formulario["CSC_ACESSO_SICON"].Valor = True
        if linha_si["VPN"] == 'S':
            Formulario["CSC_ACESSO_VPN"].Valor = True
        if linha_si["SISBB"] == 'S':
            Formulario["CSC_ACESSO_SISBB"].Valor = True
        if linha_si["WIRELESS"] == 'S':
            Formulario["CSC_ACESSO_WIFI"].Valor = True
        if linha_si["ERP"] == 'S':
            OrdemServico.SetCustom("CSC_TRABALHADOR_TEMPORARIO",linha['ID'].ToString())
            Formulario["CSC_ACESSO_ERP"].Valor = True
            OrdemServico.SetCustom("CSC_LISTA_RESP_ERP",None)
            Formulario["LABEL2"].Visivel = True
            Formulario["LABEL2"].Valor = "<span style=\"color: Black; font-weight: bold\">Acesso já liberado aos seguintes Módulos do ERP:</span>"
            for linha_erp in info_erp.Rows:
                Formulario["LABEL2"].Valor = Formulario["LABEL2"].Valor+"<br>"+linha_erp["RESPONSABILIDADE"].ToString()
                OrdemServico.AdicionaLinhaRegistro("CSC_LISTA_RESP_ERP",["MODULOS"],[linha_erp["RESPONSABILIDADE"].ToString()])
            if OrdemServico.Servico.Sigla.ToString() == 'DESTRABALHADORTEMPORARIO':
                Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
                Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
            else:
                Formulario["LABEL2"].Valor = Formulario["LABEL2"].Valor+"<span style=\"color: Red; font-weight: bold\"><br>Para alterar favor clicar em 'Adicionar novo item' no campo abaixo.</span>"
                Formulario["CSC_LISTA_RESP_ERP"].Visivel = True
                Formulario["CSC_LISTA_RESP_ERP"].Habilitado = True


               
idFavorecidoCustom = Convert.ToInt32(Formulario["CSC_TRABALHADOR_TEMPORARIO"].Valor)
favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
 
sql1 = "SELECT ID, EMAIL_PESSOAL, NOME, ENDERECO, NRO_END, COMPLEMENTO_END, BAIRRO, TO_CHAR(ESTADO) AS ESTADO, CIDADE, CEP, CPF, RG, EMISSAO, RG_ORGAO_EMISSOR, TO_CHAR(RG_ESTADO_EMISSOR) AS RG_ESTADO_EMISSOR, TELEFONE, DATA_NASCIMENTO, TO_CHAR(ESTADO_NASCIMENTO) AS ESTADO_NASCIMENTO, CIDADE_NASCIMENTO, ESTADO_CIVIL, CODIGO_BANCO, CODIGO_AGENCIA, DIGITO_AGENCIA, NOME_AGENCIA, CONTA_NUMERO, CONTA_DIGITO, UOR FROM VW_BBTS_TRABALHADOR_TEMPORARIO WHERE ID = '"+Controle.Valor.ToString()+"'"
dados = DB.ExecuteDataTable(sql1)                
if OrdemServico.Servico.Sigla == "RECADASTRAMENTOPOSTO":
    for lista in dados.Rows:
        Formulario["CSC_EMAIL_PESSOAL"].Valor = lista['EMAIL_PESSOAL'].ToString()
        Formulario["CSC_LOGRADOURO"].Valor = lista['ENDERECO'].ToString()
        Formulario["CSC_NUMERO"].Valor = lista['NRO_END'].ToString()
        Formulario["CSC_COMPLEMENTO"].Valor = lista['COMPLEMENTO_END'].ToString()
        Formulario["CSC_BAIRRO"].Valor = lista['BAIRRO'].ToString()
        Formulario["CSC_UF"].Valor = lista['ESTADO'].ToString()
        Formulario["CSC_CIDADE"].Valor = lista['CIDADE'].ToString()
        Formulario["CSC_CEP"].Valor = lista['CEP'].ToString()
        Formulario["CSC_CPF"].Valor = lista['CPF'].ToString()
        Formulario["CSC_RG"].Valor = lista['RG'].ToString()
        Formulario["CSC_DATA_EMISSOA"].Valor = lista['EMISSAO'].ToString()
        Formulario["CSC_ORGAO_EMISSOR"].Valor = lista['RG_ORGAO_EMISSOR'].ToString()
        Formulario["CSC_ESTADO_EMISSOR"].Valor = lista['RG_ESTADO_EMISSOR'].ToString()
        Formulario["CSC_TELEFONE_CONTATO"].Valor = lista['TELEFONE'].ToString()
        Formulario["CSC_DATA_NASCIMENTO"].Valor = lista['DATA_NASCIMENTO'].ToString()
        Formulario["CSC_UF_NASCIMENTO"].Valor = lista['ESTADO_NASCIMENTO'].ToString()
        Formulario["CSC_CIDADE_NASCIMENTO"].Valor = lista['CIDADE_NASCIMENTO'].ToString()
        Formulario["CSC_ESTADO_CIVIL"].Valor = lista['ESTADO_CIVIL'].ToString()
        Formulario["CSC_BANCO"].Valor = lista['CODIGO_BANCO'].ToString()
        Formulario["CSC_CONTA_CORRENTE"].Valor = lista['CONTA_NUMERO'].ToString()
        Formulario["CSC_DIGITO_AGENCIA"].Valor = lista['DIGITO_AGENCIA'].ToString()
        Formulario["CSC_DIGITO_CONTA_CORRENTE"].Valor = lista['CONTA_DIGITO'].ToString()
        Formulario["CSC_NOME_AGENCIA"].Valor = lista['NOME_AGENCIA'].ToString()
        Formulario["CSC_NUMERO_AGENCIA"].Valor = lista['CODIGO_AGENCIA'].ToString()
        Formulario["CSC_UOR_LISTA"].Valor = lista['UOR'].ToString()
```
  - CSC_EMAIL_PESSOAL "E-mail Pessoal" [TextBox String(500) → CPE_CSC.CSC_EMAIL_PESSOAL]
  - CSC_DATA_EMISSOA "Emissão" [DatePicker DateTime → CPE_CSC.CSC_DATA_EMISSOA]
  - CSC_ORGAO_EMISSOR "Órgão Emissor" [TextBox String(200) → CPE_CSC.CSC_ORGAO_EMISSOR]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Cadastro no Peoplesoft
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA]
  - SIM_NAO5 "O trabalhador tem cadastro no peoplesoft?" [DropDownList String → CPE_CSC.SIM_NAO5] obrigatório
**SIM_NAO5.ScriptModificado**
```python
if Formulario["SIM_NAO5"].Valor == 'Sim':
    Formulario["MATRICULA"].Visivel = True
    
if Formulario["SIM_NAO5"].Valor != 'Sim':
    Formulario["MATRICULA"].Visivel = False
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados Bancários (Não será aceita conta salário e conta poupança. Conta conjunta somente se o prestador for o titular)
  - CSC_NUMERO_AGENCIA "Número da Agência" [TextBox String → CPE_CSC.CSC_NUMERO_AGENCIA]
  - CSC_DIGITO_AGENCIA "Dígito da Agência" [TextBox String → CPE_CSC.CSC_DIGITO_AGENCIA]
  - CSC_NOME_AGENCIA "Nome Agência" [TextBox String(500) → CPE_CSC.CSC_NOME_AGENCIA]
  - CSC_CONTA_CORRENTE "Conta Corrente" [TextBox String → CPE_CSC.CSC_CONTA_CORRENTE]
  - CSC_DIGITO_CONTA_CORRENTE "Dígito Conta Corrente" [TextBox String → CPE_CSC.CSC_DIGITO_CONTA_CORRENTE]
  - CSC_BANCO "Banco" [DropDownList String(500) → CPE_CSC.CSC_BANCO]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados da Empresa do Trabalhador Temporário
  - CSC_DGCO "DGCO" [TextBox String → CPE_CSC.CSC_DGCO] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00000/0000"}
**CSC_DGCO.ScriptModificado**
```python
if OrdemServico.Servico.Sigla == "RECADASTRAMENTOPOSTO":
    clr.AddReference("Newtonsoft.Json")
    clr.AddReference("System.Net.Http")
    clr.AddReference("Supravizio.Custom")
    clr.AddReference("System.Data")

    import clr
    from System import Convert
    from Newtonsoft.Json.Linq import JArray
    from Newtonsoft.Json import JsonConvert
    from System.Net.Http import HttpClient
    from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
    from System import TimeSpan

    # Obtém valor do campo CSC_DGCO
    dgco = str(Formulario["CSC_DGCO"].Valor)

    # Token de autenticação
    token = '***MASCARADO***'

    # Obtém o ambiente (Homologação ou Produção)
    sql = "select name from sv_domain where enabled = 'Sim'"
    dom = DB.ExecuteScalar(sql)

    # Define a URL com base no ambiente
    url = ''
    if dom == 'HOMOLOGAÇÃO' or dom == 'PRODUÇÃO':    
        url = 'https://sisccon.bbts.com.br/supravizio/supra/buscar-intervenientes-por-dgco?dgco=' + dgco

    # Log para verificar a URL gerada
    Formulario['CSC_EMPRESA'].Valor = "URL: " + url

    # Verifica se a URL foi gerada corretamente
    if not url:
        Formulario['OBJETO_CONTRATACAO'].Valor = "Erro: URL não gerada corretamente."
    else:
        # Inicializa o HttpClient e configura os cabeçalhos
        client = HttpClient()
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Clear()
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.TryAddWithoutValidation("Content-Type", "application/json")
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

        # Faz a requisição GET
        try:
            response = client.GetAsync(url)
            response.Wait()

            if response.Result.IsSuccessStatusCode:
                # Lê o conteúdo da resposta
                resultAsync = response.Result.Content.ReadAsStringAsync()
                resultAsync.Wait()
                result = resultAsync.Result

                try:
                    # Verifica se o JSON está encapsulado em aspas
                    if result.startswith("\"") and result.endswith("\""):
                        result = JsonConvert.DeserializeObject(result)

                    # Converte o JSON em array
                    jsonArray = JArray.Parse(result)

                    # Se houver contratos a designar, processa os dados
                    if len(jsonArray) > 0:
                        for item in jsonArray:
                            Formulario["CSC_EMPRESA"].Valor = str(item['fornecedor'])
                            Formulario["OBJETO_CONTRATACAO"].Valor = str(item['objeto'])

                except Exception as e:
                    pass

        except Exception as e:
            pass
```
  - CSC_EMPRESA "Empresa" [TextBox String(500) → CPE_CSC.CSC_EMPRESA] obrigatório
  - OBJETO_CONTRATACAO "Objeto" [Memo String(1999) → CP_ORDEM_SERVICO.OBJETO_CONTRATACAO] obrigatório
  - DATA_ATIVIDADE "Data de Inicio da Vigência" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ATIVIDADE] obrigatório
  - DATA_FIM_PREVIST "Data de Fim da Vigência" [DatePicker DateTime → CPE_MOVIMENTACAO_PESSOA.DATA_FIM_PREVIST] obrigatório
- Associação de subprocesso: AssociacaoId=1458; FraseAssociacao=Trabalhador Temporario Carga-->Cadastro Trabalhador Temporario; Nome=TRABALHADORTEMPORARIOCARGA

### [370832] Tarefa "Abrir Manual o chamado para VPN"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Supravizio.Processo.Custom import Atividade
import sysAid
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.
#
#OrdemServico.SetCustom("CSC_CPF",OrdemServico.Pai.GetCustom("CSC_CPF"))
#OrdemServico.SetCustom("CSC_DATA_FIM",OrdemServico.Pai.GetCustom("CSC_DATA_FIM"))
#OrdemServico.SetCustom("CSC_DATA_INICIO",OrdemServico.Pai.GetCustom("CSC_DATA_INICIO"))
#OrdemServico.SetCustom("CSC_MATRICULA",OrdemServico.Pai.GetCustom("CSC_MATRICULA"))
#OrdemServico.SetCustom("CSC_NOME_COMPLETO",OrdemServico.Pai.GetCustom("CSC_NOME_COMPLETO"))
#OrdemServico.SetCustom("CSC_TRABALHADOR_TEMPORARIO",OrdemServico.Pai.GetCustom("CSC_TRABALHADOR_TEMPORARIO"))
#OrdemServico.SetCustom("CSC_LOCALIDADE_ATUACAO",OrdemServico.Pai.GetCustom("CSC_LOCALIDADE_ATUACAO"))
#OrdemServico.SetCustom("CSC_UOR_LISTA",OrdemServico.Pai.GetCustom("CSC_UOR_LISTA"))
#OrdemServico.Salva()
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
#solicitante = OrdemServico.Cliente["MATRICULA"].ToString()
#usuarioAtendido = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#nomeColaborador = OrdemServico.GetCustom('CSC_NOME_COMPLETO').ToString() + OrdemServico.GetCustom('CSC_TRABALHADOR_TEMPORARIO').ToString()
#matricula = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#
#titulo = "Liberacao de Acesso VPN"
#categoria = "Controle de Acesso e Privilégios_VPN_Liberação de acesso"
#descricao = OrdemServico.Assunto+" - Chamado Supravizio= "+ OrdemServico.Numero.ToString()+", matrícula do temporário: "+usuarioAtendido+ ", nome do temporário: "+nomeColaborador
#dtIncio = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_INICIO').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01')+1 )* 60 * 60 * 24 * 1000 from dual")
#
#
#idSolic = consultaUsuario(OrdemServico.Cliente.Email)
#idAtend = consultaUsuario(OrdemServico.Cliente.Email)
#if idAtend == None:
#    OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+emailUsuAtendido.ToString()
#elif idSolic == None:
#    OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+OrdemServico.Cliente.Email.ToString()
#else:
#    resposta = acessoVPN11192(categoria, titulo, descricao,dtIncio, idSolic, idAtend)
#    if String.IsNullOrEmpty(resposta.ToString()):
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada + "\n Atividade automática de abertura de chamado para acesso VPN não realizada "
#    else:
#        OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada +"\n Chamado para acesso VPN: "+resposta.ToString()
#        AvancaProximaAtividade = True
#
#
```
- Operação PR0001 Preencher Campos
  - DescricaoDetalhada (nativo) "Abertura de chamado no SysAid" obrigatório
- Operação PR0001 Preencher Campos
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA]
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO]
  - CSC_TRABALHADOR_TEMPORARIO "Trabalhador Temporário" [DropDownList String → CPE_CSC.CSC_TRABALHADOR_TEMPORARIO]
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF]
  - CSC_DATA_INICIO "Data Início" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO]
  - CSC_DATA_FIM "Data Fim" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM]
  - CSC_LOCALIDADE_ATUACAO "Localidade Atuação" [DropDownList String → CPE_CSC.CSC_LOCALIDADE_ATUACAO] obrigatório
  - CSC_UOR_LISTA "UOR" [DropDownList String(500) → CPE_CSC.CSC_UOR_LISTA] obrigatório

### [370835] Tarefa "Abrir Manual o chamado para Bloqueio"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
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
#titulo="Bloqueio de usuário"
#categoria = "Controle de Acesso e Privilégios_Conta de Rede_Bloqueio de usuário"
#dataRecisao = OrdemServico.GetCustom('CSC_DATA_FIM').ToString()
#descricao = OrdemServico.Assunto+" - Chamado Supravizio= "+ OrdemServico.Numero.ToString()+", data de encerramento do contrato: "+dataRecisao
#solicitante = OrdemServico.Cliente["MATRICULA"].ToString()
#usuarioAtendido = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#nomeColaborador = OrdemServico.GetCustom('CSC_NOME_COMPLETO').ToString() + OrdemServico.GetCustom('CSC_TRABALHADOR_TEMPORARIO').ToString()
#matricula = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#temEmail= DB.ExecuteScalar("select count(1) from ta_10 where tipo = 0 and ATIVO ='S' and matricula = '"+usuarioAtendido.ToString()+"'")
#if temEmail== 0:
#    emailUsuAtendido = '0'
#else:
#    emailUsuAtendido = DB.ExecuteScalar("select distinct ID from ta_10 where tipo = 0 and ATIVO ='S' and matricula = '"+usuarioAtendido.ToString()+"'")+"@bbts.com.br"
#
#localidade = DB.ExecuteScalar("SELECT DISTINCT E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE) and E.ESTABID='"+OrdemServico.GetCustom('CSC_LOCALIDADE_ATUACAO').ToString()+"'")
#uor = DB.ExecuteScalar(" SELECT DISTINCT NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO where nome <> SCR ||' - ' and SCR = '"+OrdemServico.GetCustom('CSC_UOR_LISTA').ToString()+"'")
#dtFim = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_FIM').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01') +1)* 60 * 60 * 24 * 1000 from dual")
#
##token=loginSysAid()
##OrdemServico.DescricaoDetalhada = token.ToString()
#
#idSolic = consultaUsuario(OrdemServico.Cliente.Email)
#idAtend = None
#
#if emailUsuAtendido == None or emailUsuAtendido == '0':
#    OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SI: '+usuarioAtendido.ToString()
#else:
#    idAtend = consultaUsuario(emailUsuAtendido)
#    if idAtend == None:
#        OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+emailUsuAtendido.ToString()
#    elif idSolic == None:
#        OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+OrdemServico.Cliente.Email.ToString()
#    else:
#        resposta = bloqueio147(categoria, titulo, descricao, localidade, idSolic.ToString(), idAtend.ToString())
#        if String.IsNullOrEmpty(resposta.ToString()):
#            OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada + "\n Atividade automática de abertura de chamado para bloqueio de usuário não realizada "
#        else:
#            OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada +"\n Chamado para bloqueio de usuário: "+resposta.ToString()
#            #AvancaProximaAtividade = True
```
**ScriptFim**
```python
from Venki.Supravizio.Processo.Custom import Atividade
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
#categoria = "Controle de Acesso e Privilégios_Conta de Rede_Bloqueio de usuário"
#dataRecisao = OrdemServico.GetCustom('CSC_DATA_FIM').ToString()
#descricao = OrdemServico.Assunto+" - Chamado Supravizio= "+ OrdemServico.Numero.ToString()+", data de encerramento do contrato: "+dataRecisao
#solicitante = OrdemServico.Cliente["MATRICULA"].ToString()
#usuarioAtendido = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#nomeColaborador = OrdemServico.GetCustom('CSC_NOME_COMPLETO').ToString() + OrdemServico.GetCustom('CSC_TRABALHADOR_TEMPORARIO').ToString()
#matricula = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
#temEmail= DB.ExecuteScalar("select count(1) from ta_10 where tipo = 0 and ATIVO ='S' and matricula = '"+usuarioAtendido.ToString()+"'")
#if temEmail== 0:
#    emailUsuAtendido = '0'
#else:
#    emailUsuAtendido = DB.ExecuteScalar("select distinct ID from ta_10 where tipo = 0 and ATIVO ='S' and matricula = '"+usuarioAtendido.ToString()+"'")+"@bbts.com.br"
#
#localidade = DB.ExecuteScalar("SELECT DISTINCT E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE) and E.ESTABID='"+OrdemServico.GetCustom('CSC_LOCALIDADE_ATUACAO').ToString()+"'")
#uor = DB.ExecuteScalar(" SELECT DISTINCT NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO where nome <> SCR ||' - ' and SCR = '"+OrdemServico.GetCustom('CSC_UOR_LISTA').ToString()+"'")
#dtFim = DB.ExecuteScalar("select ((to_date(replace('"+OrdemServico.GetCustom('CSC_DATA_FIM').ToString()+"' ,' 00:00:00',''),'DD-MM-RRRR') - date '1970-01-01') +1)* 60 * 60 * 24 * 1000 from dual")
#
##token=loginSysAid()
##OrdemServico.DescricaoDetalhada = token.ToString()
#
#idSolic = consultaUsuario(OrdemServico.Cliente.Email)
#idAtend = None
#
#if emailUsuAtendido == None or emailUsuAtendido == '0':
#    OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SI: '+usuarioAtendido.ToString()
#else:
#    idAtend = consultaUsuario(emailUsuAtendido)
#    if idAtend == None:
#        OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+emailUsuAtendido.ToString()
#    elif idSolic == None:
#        OrdemServico.DescricaoDetalhada = 'Ususário não encontrado no SysAid: '+OrdemServico.Cliente.Email.ToString()
#    else:
#        resposta = bloqueio147(categoria, titulo, descricao, localidade, idSolic.ToString(), idAtend.ToString())
#        if String.IsNullOrEmpty(resposta.ToString()):
#            OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada + "\n Atividade automática de abertura de chamado para bloqueio de usuário não realizada "
#        else:
#            OrdemServico.DescricaoDetalhada = OrdemServico.DescricaoDetalhada +"\n Chamado para bloqueio de usuário: "+resposta.ToString()
#            #AvancaProximaAtividade = True
```
**ScriptFormCarregado**
```python
Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = True
Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - DescricaoDetalhada (nativo) "Abertura de chamado no SysAid (Será preenchido quando avançar para próxima atividade.)"
- Operação PR0001 Preencher Campos
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO]
  - CSC_TRABALHADOR_TEMPORARIO "Trabalhador Temporário" [DropDownList String → CPE_CSC.CSC_TRABALHADOR_TEMPORARIO]
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA]
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF]
  - CSC_DATA_INICIO "Data Início" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO]
  - CSC_DATA_FIM "Data Fim" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM]
  - CSC_LOCALIDADE_ATUACAO "Localidade Atuação" [DropDownList String → CPE_CSC.CSC_LOCALIDADE_ATUACAO] obrigatório
  - CSC_UOR_LISTA "UOR" [DropDownList String(500) → CPE_CSC.CSC_UOR_LISTA] obrigatório

### [370812] Tarefa "Finalizar Demanda Automática"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
AvancaProximaAtividade = True
```

### [370813] Tarefa "Solicitar Aprovação do Gestor do UOR responsável pelo Terceiro"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=APROV_GESTOR_UOR
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Gestor do UOR responsável pelo Terceiro; ReenvioEmailAprovacao=12
  - (aprovação) CSC_LOGRADOURO "Logradouro" [TextBox String(500) → CPE_CSC.CSC_LOGRADOURO] — PermiteModificarAprovado=true
  - (aprovação) CSC_NUMERO "Número" [TextBox String(100) → CPE_CSC.CSC_NUMERO] — PermiteModificarAprovado=true
  - (aprovação) CSC_CIDADE "Cidade" [TextBox String(500) → CPE_CSC.CSC_CIDADE] — PermiteModificarAprovado=true
  - (aprovação) CSC_CEP "CEP" [TextBox String → CPE_CSC.CSC_CEP] — PermiteModificarAprovado=true
  - (aprovação) CSC_ORGAO_EMISSOR "Órgão Emissor" [TextBox String(200) → CPE_CSC.CSC_ORGAO_EMISSOR] — PermiteModificarAprovado=true
  - (aprovação) CSC_ESTADO_EMISSOR "Estado Emissor" [DropDownList String(500) → CPE_CSC.CSC_ESTADO_EMISSOR] — PermiteModificarAprovado=true
  - (aprovação) CSC_DATA_NASCIMENTO "Data de nascimento" [DatePicker DateTime → CPE_CSC.CSC_DATA_NASCIMENTO] — PermiteModificarAprovado=true
  - (aprovação) CSC_DIGITO_AGENCIA "Dígito da Agência" [TextBox String → CPE_CSC.CSC_DIGITO_AGENCIA] — PermiteModificarAprovado=true
  - (aprovação) CSC_DIGITO_CONTA_CORRENTE "Dígito Conta Corrente" [TextBox String → CPE_CSC.CSC_DIGITO_CONTA_CORRENTE] — PermiteModificarAprovado=true
  - (aprovação) CSC_DGCO "DGCO" [TextBox String → CPE_CSC.CSC_DGCO] — PermiteModificarAprovado=true
  - (aprovação) CSC_EMPRESA "Empresa" [TextBox String(500) → CPE_CSC.CSC_EMPRESA] — PermiteModificarAprovado=true
  - (aprovação) CSC_ACESSO_TOA "Acesso TOA" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_TOA] — PermiteModificarAprovado=true
  - (aprovação) CSC_ACESSO_WIFI "Acesso Wi-fi" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_WIFI] — PermiteModificarAprovado=true
  - (aprovação) CSC_BAIRRO "Bairro" [TextBox String(500) → CPE_CSC.CSC_BAIRRO] — PermiteModificarAprovado=true
  - (aprovação) CSC_NOME_AGENCIA "Nome Agência" [TextBox String(500) → CPE_CSC.CSC_NOME_AGENCIA] — PermiteModificarAprovado=true
  - (aprovação) CSC_ACESSO_SICON "Acesso SICON" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_SICON] — PermiteModificarAprovado=true
  - (aprovação) CSC_DATA_EMISSOA "Emissão" [DatePicker DateTime → CPE_CSC.CSC_DATA_EMISSOA] — PermiteModificarAprovado=true
  - (aprovação) OBJETO_CONTRATACAO "Objeto da Contratação" [Memo String(1999) → CP_ORDEM_SERVICO.OBJETO_CONTRATACAO]
  - (aprovação) CSC_DATA_INICIO "Início na BBTS (Contrato atual)" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO] — PermiteModificarAprovado=true
  - (aprovação) CSC_ACESSO_VPN "Acesso VPN" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_VPN] — PermiteModificarAprovado=true
  - (aprovação) CSC_ACESSO_SISBB "Acesso SISBB" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_SISBB] — PermiteModificarAprovado=true
  - (aprovação) CSC_TRABALHADOR_TEMPORARIO "Trabalhador Temporário" [DropDownList String → CPE_CSC.CSC_TRABALHADOR_TEMPORARIO] — PermiteModificarAprovado=true
  - (aprovação) CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF] — PermiteModificarAprovado=true
  - (aprovação) CSC_UF_NASCIMENTO "UF de Nascimento" [DropDownList String → CPE_CSC.CSC_UF_NASCIMENTO] — PermiteModificarAprovado=true
  - (aprovação) CSC_NUMERO_AGENCIA "Número da Agência" [TextBox String → CPE_CSC.CSC_NUMERO_AGENCIA] — PermiteModificarAprovado=true
  - (aprovação) CSC_CONTA_CORRENTE "Conta Corrente" [TextBox String → CPE_CSC.CSC_CONTA_CORRENTE] — PermiteModificarAprovado=true
  - (aprovação) CSC_CARGO_LISTA "Cargo que o Trabalhador ocupará" [DropDownList String(100) → CPE_CSC.CSC_CARGO_LISTA] — PermiteModificarAprovado=true
  - (aprovação) CSC_EMAIL_PESSOAL "E-mail Pessoal" [TextBox String(500) → CPE_CSC.CSC_EMAIL_PESSOAL] — PermiteModificarAprovado=true
  - (aprovação) CSC_CIDADE_NASCIMENTO "Cidade de Nascimento" [TextBox String(500) → CPE_CSC.CSC_CIDADE_NASCIMENTO] — PermiteModificarAprovado=true
  - (aprovação) CSC_BANCO "Banco" [DropDownList String(500) → CPE_CSC.CSC_BANCO] — PermiteModificarAprovado=true
  - (aprovação) CSC_LISTA_RESP_ERP "Nome da Responsabilidade no ERP" [DataGrid RecordList → Z_00143_CSC_LISTA_RESP_ERP.CSC_LISTA_RESP_ERP] — PermiteModificarAprovado=true
  - (aprovação) CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO] — PermiteModificarAprovado=true
  - (aprovação) CSC_COMPLEMENTO "Complemento" [TextBox String(500) → CPE_CSC.CSC_COMPLEMENTO] — PermiteModificarAprovado=true
  - (aprovação) CSC_RG "RG" [TextBox String → CPE_CSC.CSC_RG] — PermiteModificarAprovado=true
  - (aprovação) CSC_UF "UF" [DropDownList String → CPE_CSC.CSC_UF] — PermiteModificarAprovado=true
  - (aprovação) CSC_TELEFONE_CONTATO "Telefone para Contato" [TextBox String → CPE_CSC.CSC_TELEFONE_CONTATO] — PermiteModificarAprovado=true
  - (aprovação) CSC_ESTADO_CIVIL "Estado Civil" [DropDownList String → CPE_CSC.CSC_ESTADO_CIVIL] — PermiteModificarAprovado=true
  - (aprovação) DATA_ATIVIDADE "Data de Inicio da Vigência" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ATIVIDADE]
  - (aprovação) DATA_FIM_PREVIST "Data de Fim da Vigência" [DatePicker DateTime → CPE_MOVIMENTACAO_PESSOA.DATA_FIM_PREVIST]
  - (aprovação) CSC_UOR_LISTA "UOR da Área Solicitante" [DropDownList String(500) → CPE_CSC.CSC_UOR_LISTA] — PermiteModificarAprovado=true
  - (aprovação) CSC_ACESSO_ERP "Acesso ERP" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_ERP] — PermiteModificarAprovado=true
  - (aprovação) CSC_LOCALIDADE_ATUACAO "Localidade Atuação" [DropDownList String → CPE_CSC.CSC_LOCALIDADE_ATUACAO] — PermiteModificarAprovado=true
  - (aprovação) CSC_DATA_FIM "Saída da BBTS" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM] — PermiteModificarAprovado=true
  - (aprovação) CSC_ACESSO_REDE_EMAIL "Acesso Rede e E-mail" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_REDE_EMAIL] — PermiteModificarAprovado=true
  - aprovador: Gestor da UOR do Trab Temporario (Unico)

### [370833] Tarefa "Cadastrar Trabalhador Temporário no HR"
Responsável: Responsável atual (papel 36)
**ScriptFim**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#OrdemServico.Favorecido=Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("SELECT DISTINCT(ID_PESSOA) ID FROM CP_PESSOA WHERE MATRICULA = '"+OrdemServico["CSC_MATRICULA"]+"'")))
#OrdemServico.Salva()
nome = DB.ExecuteScalar("select distinct npw_number|| ' - ' ||UPPER(full_name) as NOME from per_all_people_f where npw_number is not null and npw_number ='"+OrdemServico["CSC_TRABALHADOR_TEMPORARIO"].ToString()+"'  GROUP BY npw_number,full_name")
if nome != "" and nome != None:
    OrdemServico.SetCustom("CSC_NOME_COMPLETO",nome)
    OrdemServico.Salva()
```
**ScriptFormCarregado**
```python
Formulario['COMBOBOX1'].Habilitado = False
Formulario["LABEL1"].Valor = '<span style=\"color: Black; font-weight: bold\"><br><br>A seleção do Trabalhador Temporário deve aguardar o Supravizio importar as informações do People (Dia do Cadastro + 1).</span>'
Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = False
Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = False
Formulario["CSC_NOME_COMPLETO"].Visivel = True
Formulario["CSC_NOME_COMPLETO"].Habilitado = True
Formulario["CSC_UOR"].Valor = OrdemServico["CSC_UOR_LISTA"]
if OrdemServico.Servico.Sigla.ToString() == 'DESTRABALHADORTEMPORARIO' or OrdemServico.Servico.Sigla.ToString() == 'PRORTRABALHADORTEMPORARIO' or OrdemServico.Servico.Sigla.ToString() == 'RECADASTRAMENTOPOSTO':
    Formulario["CSC_NOME_COMPLETO"].Visivel = False
    Formulario["CSC_NOME_COMPLETO"].Habilitado = False
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = True
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = True
    Formulario["CSC_MATRICULA"].Habilitado = True
    Formulario["CSC_MATRICULA"].Visivel = True
    Formulario["CSC_UOR"].Habilitado = True
    
    #sql = "SELECT MATRICULA, SUBSTR(ORGANIZACAO,1,10) ORGANIZACAO FROM CAD_FUNCIONARIO_V WHERE MATRICULA ='"+OrdemServico["CSC_TRABALHADOR_TEMPORARIO"].ToString()+"' ORDER BY NOME"
    #info = DB.ExecuteDataTable(sql)

    #for linha in info.Rows:
    #    Formulario["CSC_MATRICULA"].Valor = linha['MATRICULA'].ToString()
    #    Formulario["CSC_UOR"].Valor = linha['ORGANIZACAO'].ToString()
```
- Operação PR0001 Preencher Campos
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO] obrigatório
  - CSC_TRABALHADOR_TEMPORARIO "Trabalhador Temporário" [DropDownList String → CPE_CSC.CSC_TRABALHADOR_TEMPORARIO] obrigatório
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório
  - CSC_UOR "UOR no People" [TextBox String → CPE_CSC.CSC_UOR] obrigatório
  - LABEL1 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - COMBOBOX1 "COBAN" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]

### [370834] Tarefa "Conferir Informações"
Responsável: Responsável atual (papel 36)
**ScriptFormCarregado**
```python
Formulario['COMBOBOX1'].Habilitado = False

if OrdemServico["CSC_NOME_COMPLETO"] == None or OrdemServico["CSC_NOME_COMPLETO"] == '':
    Formulario["CSC_NOME_COMPLETO"].Visivel = False
    Formulario["CSC_NOME_COMPLETO"].Habilitado = False
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = True
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = True
else:
    Formulario["CSC_NOME_COMPLETO"].Visivel = True
    Formulario["CSC_NOME_COMPLETO"].Habilitado = True
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = False
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = False
    
OrdemServico.AdicionaComentario(OrdemServico.Servico.Sigla.ToString(), False)

#Formulario["CSC_EMAIL_PESSOAL"].Visivel = False
#Formulario["CSC_EMAIL_PESSOAL"].Habilitado = False
#
#Formulario["CSC_LOGRADOURO"].Visivel = False
#Formulario["CSC_LOGRADOURO"].Habilitado = False
#
#Formulario["CSC_NUMERO"].Visivel = False
#Formulario["CSC_NUMERO"].Habilitado = False
#
#Formulario["CSC_COMPLEMENTO"].Visivel = False
#Formulario["CSC_COMPLEMENTO"].Habilitado = False
#
#Formulario["CSC_BAIRRO"].Visivel = False
#Formulario["CSC_BAIRRO"].Habilitado = False
#
#Formulario["CSC_UF"].Visivel = False
#Formulario["CSC_UF"].Habilitado = False
#
#Formulario["CSC_CIDADE"].Visivel = False
#Formulario["CSC_CIDADE"].Habilitado = False
#
#Formulario["CSC_CEP"].Visivel = False
#Formulario["CSC_CEP"].Habilitado = False
#
#Formulario["CSC_CPF"].Visivel = False
#Formulario["CSC_CPF"].Habilitado = False
#
#Formulario["CSC_RG"].Visivel = False
#Formulario["CSC_RG"].Habilitado = False
#
#Formulario["CSC_DATA_EMISSOA"].Visivel = False
#Formulario["CSC_DATA_EMISSOA"].Habilitado = False
#
#Formulario["CSC_ORGAO_EMISSOR"].Visivel = False
#Formulario["CSC_ORGAO_EMISSOR"].Habilitado = False
#
#Formulario["CSC_ESTADO_EMISSOR"].Visivel = False
#Formulario["CSC_ESTADO_EMISSOR"].Habilitado = False
#
#Formulario["CSC_TELEFONE_CONTATO"].Visivel = False
#Formulario["CSC_TELEFONE_CONTATO"].Habilitado = False
#
#Formulario["CSC_DATA_NASCIMENTO"].Visivel = False
#Formulario["CSC_DATA_NASCIMENTO"].Habilitado = False
#
#Formulario["CSC_UF_NASCIMENTO"].Visivel = False
#Formulario["CSC_UF_NASCIMENTO"].Habilitado = False
#
#Formulario["CSC_CIDADE_NASCIMENTO"].Visivel = False
#Formulario["CSC_CIDADE_NASCIMENTO"].Habilitado = False
#
#Formulario["CSC_ESTADO_CIVIL"].Visivel = False
#Formulario["CSC_ESTADO_CIVIL"].Habilitado = False
#
#Formulario["CSC_ESCOLARIDADE"].Visivel = False
#Formulario["CSC_ESCOLARIDADE"].Habilitado = False
##Formulario["SEXO_M_F"].Visivel = False
##Formulario["SEXO_M_F"].Habilitado = False
#
#Formulario["CSC_BANCO"].Visivel = False
#Formulario["CSC_BANCO"].Habilitado = False
#
#Formulario["CSC_CONTA_CORRENTE"].Visivel = False
#Formulario["CSC_CONTA_CORRENTE"].Habilitado = False
#
#Formulario["CSC_DIGITO_AGENCIA"].Visivel = False
#Formulario["CSC_DIGITO_AGENCIA"].Habilitado = False
#
#Formulario["CSC_DIGITO_CONTA_CORRENTE"].Visivel = False
#Formulario["CSC_DIGITO_CONTA_CORRENTE"].Habilitado = False
#
#Formulario["CSC_NOME_AGENCIA"].Visivel = False
#Formulario["CSC_NOME_AGENCIA"].Habilitado = False
#
#Formulario["CSC_NUMERO_AGENCIA"].Visivel = False
#Formulario["CSC_NUMERO_AGENCIA"].Habilitado = False
#
#
#Formulario["CSC_DGCO"].Visivel = False
#Formulario["CSC_DGCO"].Habilitado = False
#Formulario["CSC_EMPRESA"].Visivel = False
#Formulario["CSC_EMPRESA"].Habilitado = False
#
#Formulario["DATA_FIM_PREVIST"].Visivel = False
#Formulario["DATA_FIM_PREVIST"].Habilitado = False
#
#Formulario["DATA_ATIVIDADE"].Visivel = False
#Formulario["DATA_ATIVIDADE"].Habilitado = False
#
#Formulario["OBJETO_CONTRATACAO"].Visivel = False
#Formulario["OBJETO_CONTRATACAO"].Habilitado = False
#
#
#Formulario["CSC_CARGO_LISTA"].Visivel = False
#Formulario["CSC_CARGO_LISTA"].Habilitado = False
#
#Formulario["CSC_DATA_FIM"].Visivel = False
#Formulario["CSC_DATA_FIM"].Habilitado = False
#
#Formulario["CSC_DATA_INICIO"].Visivel = False
#Formulario["CSC_DATA_INICIO"].Habilitado = False
#
#Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = False
#Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = False
#
#Formulario["CSC_UOR_LISTA"].Visivel = False
#Formulario["CSC_UOR_LISTA"].Habilitado = False
#
#
#Formulario["CSC_ACESSO_ERP"].Visivel = False
#Formulario["CSC_ACESSO_ERP"].Habilitado = False
#
#Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = False
#Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = False
#
#Formulario["CSC_ACESSO_SICON"].Visivel = False
#Formulario["CSC_ACESSO_SICON"].Habilitado = False
#
#Formulario["CSC_ACESSO_SISBB"].Visivel = False
#Formulario["CSC_ACESSO_SISBB"].Habilitado = False
#
###Formulario["CSC_ACESSO_TOA"].Visivel = False
###Formulario["CSC_ACESSO_TOA"].Habilitado = False
#
#Formulario["CSC_ACESSO_VPN"].Visivel = False
#Formulario["CSC_ACESSO_VPN"].Habilitado = False
#
#Formulario["CSC_ACESSO_WIFI"].Visivel = False
#Formulario["CSC_ACESSO_WIFI"].Habilitado = False
#
#Formulario["LABEL2"].Visivel = False
#Formulario["LABEL2"].Habilitado = False
#
#Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
#Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
#
#
#
#
#
if OrdemServico.Servico.Sigla.ToString() == 'CADTRABALHADORTEMPORARIO':
    Formulario["CSC_NOME_COMPLETO"].Visivel = True
    Formulario["CSC_NOME_COMPLETO"].Habilitado = False
    Formulario["CSC_EMAIL_PESSOAL"].Visivel = True
    Formulario["CSC_EMAIL_PESSOAL"].Habilitado = False
    Formulario["CSC_LOGRADOURO"].Visivel = True
    Formulario["CSC_LOGRADOURO"].Habilitado = False
    Formulario["CSC_NUMERO"].Visivel = True
    Formulario["CSC_NUMERO"].Habilitado = False
    Formulario["CSC_COMPLEMENTO"].Visivel = True
    Formulario["CSC_COMPLEMENTO"].Habilitado = False
    Formulario["CSC_BAIRRO"].Visivel = True
    Formulario["CSC_BAIRRO"].Habilitado = False
    Formulario["CSC_UF"].Visivel = True
    Formulario["CSC_UF"].Habilitado = False
    Formulario["CSC_CIDADE"].Visivel = True
    Formulario["CSC_CIDADE"].Habilitado = False
    Formulario["CSC_CEP"].Visivel = True
    Formulario["CSC_CEP"].Habilitado = False
    Formulario["CSC_CPF"].Visivel = True
    Formulario["CSC_CPF"].Habilitado = False
    Formulario["CSC_RG"].Visivel = True
    Formulario["CSC_RG"].Habilitado = False
    Formulario["CSC_DATA_EMISSOA"].Visivel = True
    Formulario["CSC_DATA_EMISSOA"].Habilitado = False
    Formulario["CSC_ORGAO_EMISSOR"].Visivel = True
    Formulario["CSC_ORGAO_EMISSOR"].Habilitado = False
    Formulario["CSC_ESTADO_EMISSOR"].Visivel = True
    Formulario["CSC_ESTADO_EMISSOR"].Habilitado = False
    Formulario["CSC_TELEFONE_CONTATO"].Visivel = True
    Formulario["CSC_TELEFONE_CONTATO"].Habilitado = False
    Formulario["CSC_DATA_NASCIMENTO"].Visivel = True
    Formulario["CSC_DATA_NASCIMENTO"].Habilitado = False
    Formulario["CSC_UF_NASCIMENTO"].Visivel = True
    Formulario["CSC_UF_NASCIMENTO"].Habilitado = False
    Formulario["CSC_CIDADE_NASCIMENTO"].Visivel = True
    Formulario["CSC_CIDADE_NASCIMENTO"].Habilitado = False
    Formulario["CSC_ESTADO_CIVIL"].Visivel = True
    Formulario["CSC_ESTADO_CIVIL"].Habilitado = False
    Formulario["CSC_ESCOLARIDADE"].Visivel = False
    Formulario["CSC_ESCOLARIDADE"].Habilitado = False
    #Formulario["SEXO_M_F"].Visivel = True
    #Formulario["SEXO_M_F"].Habilitado = False

    
    Formulario["CSC_BANCO"].Visivel = True
    Formulario["CSC_BANCO"].Habilitado = False
    Formulario["CSC_CONTA_CORRENTE"].Visivel = True
    Formulario["CSC_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_DIGITO_AGENCIA"].Visivel = True
    Formulario["CSC_DIGITO_AGENCIA"].Habilitado = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Visivel = True
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_NOME_AGENCIA"].Visivel = True
    Formulario["CSC_NOME_AGENCIA"].Habilitado = False
    Formulario["CSC_NUMERO_AGENCIA"].Visivel = True
    Formulario["CSC_NUMERO_AGENCIA"].Habilitado = False
    
    Formulario["CSC_DGCO"].Visivel = True
    Formulario["CSC_DGCO"].Habilitado = False
    Formulario["CSC_EMPRESA"].Visivel = True
    Formulario["CSC_EMPRESA"].Habilitado = False
    
    Formulario["CSC_CARGO_LISTA"].Visivel = True
    Formulario["CSC_CARGO_LISTA"].Habilitado = False
    Formulario["CSC_DATA_FIM"].Visivel = True
    Formulario["CSC_DATA_FIM"].Habilitado = False
    Formulario["CSC_DATA_INICIO"].Visivel = True
    Formulario["CSC_DATA_INICIO"].Habilitado = False
    Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = True
    Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = False
    Formulario["CSC_UOR_LISTA"].Visivel = True
    Formulario["CSC_UOR_LISTA"].Habilitado = False
    
    Formulario["CSC_ACESSO_ERP"].Visivel = False
    Formulario["CSC_ACESSO_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = True
    Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = False
    #Formulario["CSC_ACESSO_SICON"].Visivel = False
    #Formulario["CSC_ACESSO_SICON"].Habilitado = False
    Formulario["CSC_ACESSO_SISBB"].Visivel = False
    Formulario["CSC_ACESSO_SISBB"].Habilitado = False
    #Formulario["CSC_ACESSO_TOA"].Visivel = False
    #Formulario["CSC_ACESSO_TOA"].Habilitado = False
    Formulario["CSC_ACESSO_VPN"].Visivel = False
    Formulario["CSC_ACESSO_VPN"].Habilitado = False
    Formulario["CSC_ACESSO_WIFI"].Visivel = False
    Formulario["CSC_ACESSO_WIFI"].Habilitado = False
    Formulario["CSC_ACESSO_TOA"].Visivel = False
    Formulario["CSC_ACESSO_TOA"].Habilitado = False
    
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    
if OrdemServico.Servico.Sigla.ToString() == 'PRORTRABALHADORTEMPORARIO':
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = True
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = False
    Formulario["CSC_EMAIL_PESSOAL"].Visivel = False
    Formulario["CSC_EMAIL_PESSOAL"].Habilitado = False
    Formulario["CSC_LOGRADOURO"].Visivel = True
    Formulario["CSC_LOGRADOURO"].Habilitado = False
    Formulario["CSC_NUMERO"].Visivel = True
    Formulario["CSC_NUMERO"].Habilitado = False
    Formulario["CSC_COMPLEMENTO"].Visivel = False
    Formulario["CSC_COMPLEMENTO"].Habilitado = False
    Formulario["CSC_BAIRRO"].Visivel = True
    Formulario["CSC_BAIRRO"].Habilitado = False
    Formulario["CSC_UF"].Visivel = True
    Formulario["CSC_UF"].Habilitado = False
    Formulario["CSC_CIDADE"].Visivel = True
    Formulario["CSC_CIDADE"].Habilitado = False
    Formulario["CSC_CEP"].Visivel = True
    Formulario["CSC_CEP"].Habilitado = False
    Formulario["CSC_CPF"].Visivel = True
    Formulario["CSC_CPF"].Habilitado = False
    Formulario["CSC_RG"].Visivel = False
    Formulario["CSC_RG"].Habilitado = False
    Formulario["CSC_DATA_EMISSOA"].Visivel = False
    Formulario["CSC_DATA_EMISSOA"].Habilitado = False
    Formulario["CSC_ORGAO_EMISSOR"].Visivel = False
    Formulario["CSC_ORGAO_EMISSOR"].Habilitado = False
    Formulario["CSC_ESTADO_EMISSOR"].Visivel = False
    Formulario["CSC_ESTADO_EMISSOR"].Habilitado = False
    Formulario["CSC_TELEFONE_CONTATO"].Visivel = True
    Formulario["CSC_TELEFONE_CONTATO"].Habilitado = False
    Formulario["CSC_DATA_NASCIMENTO"].Visivel = True
    Formulario["CSC_DATA_NASCIMENTO"].Habilitado = False
    Formulario["CSC_UF_NASCIMENTO"].Visivel = True
    Formulario["CSC_UF_NASCIMENTO"].Habilitado = False
    Formulario["CSC_CIDADE_NASCIMENTO"].Visivel = True
    Formulario["CSC_CIDADE_NASCIMENTO"].Habilitado = False
    Formulario["CSC_ESTADO_CIVIL"].Visivel = True
    Formulario["CSC_ESTADO_CIVIL"].Habilitado = False
    Formulario["CSC_ESCOLARIDADE"].Visivel = True
    Formulario["CSC_ESCOLARIDADE"].Habilitado = False
    #Formulario["SEXO_M_F"].Visivel = True
    #Formulario["SEXO_M_F"].Habilitado = False

    
    Formulario["CSC_BANCO"].Visivel = False
    Formulario["CSC_BANCO"].Habilitado = False
    Formulario["CSC_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_DIGITO_AGENCIA"].Visivel = False
    Formulario["CSC_DIGITO_AGENCIA"].Habilitado = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_NOME_AGENCIA"].Visivel = False
    Formulario["CSC_NOME_AGENCIA"].Habilitado = False
    Formulario["CSC_NUMERO_AGENCIA"].Visivel = False
    Formulario["CSC_NUMERO_AGENCIA"].Habilitado = False
    
    Formulario["CSC_DGCO"].Visivel = True
    Formulario["CSC_DGCO"].Habilitado = False
    Formulario["CSC_EMPRESA"].Visivel = True
    Formulario["CSC_EMPRESA"].Habilitado = False
    
    Formulario["CSC_CARGO_LISTA"].Visivel = True
    Formulario["CSC_CARGO_LISTA"].Habilitado = False
    Formulario["CSC_DATA_FIM"].Visivel = True
    Formulario["CSC_DATA_FIM"].Habilitado = False
    Formulario["CSC_DATA_INICIO"].Visivel = True
    Formulario["CSC_DATA_INICIO"].Habilitado = False
    Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = True
    Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = False
    Formulario["CSC_UOR_LISTA"].Visivel = True
    Formulario["CSC_UOR_LISTA"].Habilitado = False
    
    Formulario["CSC_ACESSO_ERP"].Visivel = False
    Formulario["CSC_ACESSO_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = True
    Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = True
    #Formulario["CSC_ACESSO_SICON"].Visivel = False
    #Formulario["CSC_ACESSO_SICON"].Habilitado = False
    Formulario["CSC_ACESSO_SISBB"].Visivel = False
    Formulario["CSC_ACESSO_SISBB"].Habilitado = False
    #Formulario["CSC_ACESSO_TOA"].Visivel = False
    #Formulario["CSC_ACESSO_TOA"].Habilitado = False
    Formulario["CSC_ACESSO_VPN"].Visivel = False
    Formulario["CSC_ACESSO_VPN"].Habilitado = False
    Formulario["CSC_ACESSO_WIFI"].Visivel = False
    Formulario["CSC_ACESSO_WIFI"].Habilitado = False
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Visivel = True
    Formulario["CSC_ACESSO_PEOPLESOFT"].Habilitado = True
    Formulario["CSC_ACESSO_TOA"].Visivel = False
    Formulario["CSC_ACESSO_TOA"].Habilitado = False
    
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    
if OrdemServico.Servico.Sigla.ToString() == 'DESTRABALHADORTEMPORARIO':
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = True
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = False
    Formulario["CSC_EMAIL_PESSOAL"].Visivel = False
    Formulario["CSC_EMAIL_PESSOAL"].Habilitado = False
    Formulario["CSC_LOGRADOURO"].Visivel = True
    Formulario["CSC_LOGRADOURO"].Habilitado = False
    Formulario["CSC_NUMERO"].Visivel = True
    Formulario["CSC_NUMERO"].Habilitado = False
    Formulario["CSC_COMPLEMENTO"].Visivel = False
    Formulario["CSC_COMPLEMENTO"].Habilitado = False
    Formulario["CSC_BAIRRO"].Visivel = True
    Formulario["CSC_BAIRRO"].Habilitado = False
    Formulario["CSC_UF"].Visivel = True
    Formulario["CSC_UF"].Habilitado = False
    Formulario["CSC_CIDADE"].Visivel = True
    Formulario["CSC_CIDADE"].Habilitado = False
    Formulario["CSC_CEP"].Visivel = True
    Formulario["CSC_CEP"].Habilitado = False
    Formulario["CSC_CPF"].Visivel = True
    Formulario["CSC_CPF"].Habilitado = False
    Formulario["CSC_RG"].Visivel = False
    Formulario["CSC_RG"].Habilitado = False
    Formulario["CSC_DATA_EMISSOA"].Visivel = False
    Formulario["CSC_DATA_EMISSOA"].Habilitado = False
    Formulario["CSC_ORGAO_EMISSOR"].Visivel = False
    Formulario["CSC_ORGAO_EMISSOR"].Habilitado = False
    Formulario["CSC_ESTADO_EMISSOR"].Visivel = False
    Formulario["CSC_ESTADO_EMISSOR"].Habilitado = False
    Formulario["CSC_TELEFONE_CONTATO"].Visivel = True
    Formulario["CSC_TELEFONE_CONTATO"].Habilitado = False
    Formulario["CSC_DATA_NASCIMENTO"].Visivel = True
    Formulario["CSC_DATA_NASCIMENTO"].Habilitado = False
    Formulario["CSC_UF_NASCIMENTO"].Visivel = True
    Formulario["CSC_UF_NASCIMENTO"].Habilitado = False
    Formulario["CSC_CIDADE_NASCIMENTO"].Visivel = True
    Formulario["CSC_CIDADE_NASCIMENTO"].Habilitado = False
    Formulario["CSC_ESTADO_CIVIL"].Visivel = True
    Formulario["CSC_ESTADO_CIVIL"].Habilitado = False
    Formulario["CSC_ESCOLARIDADE"].Visivel = True
    Formulario["CSC_ESCOLARIDADE"].Habilitado = False
    #Formulario["SEXO_M_F"].Visivel = True
    #Formulario["SEXO_M_F"].Habilitado = False

    
    Formulario["CSC_BANCO"].Visivel = False
    Formulario["CSC_BANCO"].Habilitado = False
    Formulario["CSC_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_DIGITO_AGENCIA"].Visivel = False
    Formulario["CSC_DIGITO_AGENCIA"].Habilitado = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_NOME_AGENCIA"].Visivel = False
    Formulario["CSC_NOME_AGENCIA"].Habilitado = False
    Formulario["CSC_NUMERO_AGENCIA"].Visivel = False
    Formulario["CSC_NUMERO_AGENCIA"].Habilitado = False
    
    Formulario["CSC_DGCO"].Visivel = False
    Formulario["CSC_DGCO"].Habilitado = False
    Formulario["CSC_EMPRESA"].Visivel = False
    Formulario["CSC_EMPRESA"].Habilitado = False
    
    Formulario["CSC_CARGO_LISTA"].Visivel = False
    Formulario["CSC_CARGO_LISTA"].Habilitado = False
    Formulario["CSC_DATA_FIM"].Visivel = True
    Formulario["CSC_DATA_FIM"].Habilitado = False
    Formulario["CSC_DATA_INICIO"].Visivel = False
    Formulario["CSC_DATA_INICIO"].Habilitado = False
    Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = True
    Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = False
    Formulario["CSC_UOR_LISTA"].Visivel = True
    Formulario["CSC_UOR_LISTA"].Habilitado = False
    
    Formulario["CSC_ACESSO_ERP"].Visivel = False
    Formulario["CSC_ACESSO_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = False
    Formulario["CSC_ACESSO_SISBB"].Visivel = False
    Formulario["CSC_ACESSO_SISBB"].Habilitado = False
    Formulario["CSC_ACESSO_VPN"].Visivel = False
    Formulario["CSC_ACESSO_VPN"].Habilitado = False
    Formulario["CSC_ACESSO_WIFI"].Visivel = False
    Formulario["CSC_ACESSO_WIFI"].Habilitado = False
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Visivel = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Habilitado = False
    Formulario["CSC_ACESSO_TOA"].Visivel = False
    Formulario["CSC_ACESSO_TOA"].Habilitado = False
    

if OrdemServico.Servico.Sigla == "DESTRABALHADORTEMPORARIO":
    Formulario["CSC_ACESSO_ERP"].Visivel = False
    Formulario["CSC_ACESSO_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = False
    Formulario["CSC_ACESSO_SISBB"].Visivel = False
    Formulario["CSC_ACESSO_SISBB"].Habilitado = False
    Formulario["CSC_ACESSO_VPN"].Visivel = False
    Formulario["CSC_ACESSO_VPN"].Habilitado = False
    Formulario["CSC_ACESSO_WIFI"].Visivel = False
    Formulario["CSC_ACESSO_WIFI"].Habilitado = False
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Visivel = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Habilitado = False
    Formulario["CSC_ACESSO_TOA"].Visivel = False
    Formulario["CSC_ACESSO_TOA"].Habilitado = False
    
if OrdemServico.Servico.Sigla == "RECADASTRAMENTOPOSTO":
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = True
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = False
    Formulario["CSC_NOME_COMPLETO"].Visivel = False
    Formulario["CSC_NOME_COMPLETO"].Habilitado = False
    Formulario["CSC_EMAIL_PESSOAL"].Visivel = False
    Formulario["CSC_EMAIL_PESSOAL"].Habilitado = False
    Formulario["CSC_LOGRADOURO"].Visivel = False
    Formulario["CSC_LOGRADOURO"].Habilitado = False
    Formulario["CSC_NUMERO"].Visivel = False
    Formulario["CSC_NUMERO"].Habilitado = False
    Formulario["CSC_COMPLEMENTO"].Visivel = False
    Formulario["CSC_COMPLEMENTO"].Habilitado = False
    Formulario["CSC_BAIRRO"].Visivel = False
    Formulario["CSC_BAIRRO"].Habilitado = False
    Formulario["CSC_UF"].Visivel = False
    Formulario["CSC_UF"].Habilitado = False
    Formulario["CSC_CIDADE"].Visivel = False
    Formulario["CSC_CIDADE"].Habilitado = False
    Formulario["CSC_CEP"].Visivel = False
    Formulario["CSC_CEP"].Habilitado = False
    Formulario["CSC_CPF"].Visivel = False
    Formulario["CSC_CPF"].Habilitado = False
    Formulario["CSC_RG"].Visivel = False
    Formulario["CSC_RG"].Habilitado = False
    Formulario["CSC_DATA_EMISSOA"].Visivel = False
    Formulario["CSC_DATA_EMISSOA"].Habilitado = False
    Formulario["CSC_ORGAO_EMISSOR"].Visivel = False
    Formulario["CSC_ORGAO_EMISSOR"].Habilitado = False
    Formulario["CSC_ESTADO_EMISSOR"].Visivel = False
    Formulario["CSC_ESTADO_EMISSOR"].Habilitado = False
    Formulario["CSC_TELEFONE_CONTATO"].Visivel = False
    Formulario["CSC_TELEFONE_CONTATO"].Habilitado = False
    Formulario["CSC_DATA_NASCIMENTO"].Visivel = False
    Formulario["CSC_DATA_NASCIMENTO"].Habilitado = False
    Formulario["CSC_UF_NASCIMENTO"].Visivel = False
    Formulario["CSC_UF_NASCIMENTO"].Habilitado = False
    Formulario["CSC_CIDADE_NASCIMENTO"].Visivel = False
    Formulario["CSC_CIDADE_NASCIMENTO"].Habilitado = False
    Formulario["CSC_ESTADO_CIVIL"].Visivel = False
    Formulario["CSC_ESTADO_CIVIL"].Habilitado = False
    Formulario["CSC_ESCOLARIDADE"].Visivel = False
    Formulario["CSC_ESCOLARIDADE"].Habilitado = False
    #Formulario["SEXO_M_F"].Visivel = False
    #Formulario["SEXO_M_F"].Habilitado = False
    
    Formulario["CSC_BANCO"].Visivel = False
    Formulario["CSC_BANCO"].Habilitado = False
    Formulario["CSC_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_DIGITO_AGENCIA"].Visivel = False
    Formulario["CSC_DIGITO_AGENCIA"].Habilitado = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Visivel = False
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Habilitado = False
    Formulario["CSC_NOME_AGENCIA"].Visivel = False
    Formulario["CSC_NOME_AGENCIA"].Habilitado = False
    Formulario["CSC_NUMERO_AGENCIA"].Visivel = False
    Formulario["CSC_NUMERO_AGENCIA"].Habilitado = False
    
    Formulario["CSC_DGCO"].Visivel = True
    Formulario["CSC_DGCO"].Habilitado = False
    Formulario["CSC_EMPRESA"].Visivel = True
    Formulario["CSC_EMPRESA"].Habilitado = False
    Formulario["DATA_ATIVIDADE"].Visivel = True
    Formulario["DATA_ATIVIDADE"].Habilitado = False
    Formulario["DATA_FIM_PREVIST"].Visivel = True
    Formulario["DATA_FIM_PREVIST"].Habilitado = False
    Formulario["OBJETO_CONTRATACAO"].Visivel = True
    Formulario["OBJETO_CONTRATACAO"].Habilitado = False
    
    Formulario["CSC_CARGO_LISTA"].Visivel = False
    Formulario["CSC_CARGO_LISTA"].Habilitado = False
    Formulario["CSC_DATA_FIM"].Visivel = True
    Formulario["CSC_DATA_FIM"].Habilitado = False
    Formulario["CSC_DATA_INICIO"].Visivel = False
    Formulario["CSC_DATA_INICIO"].Habilitado = False
    Formulario["CSC_LOCALIDADE_ATUACAO"].Visivel = False
    Formulario["CSC_LOCALIDADE_ATUACAO"].Habilitado = False
    Formulario["CSC_UOR_LISTA"].Visivel = True
    Formulario["CSC_UOR_LISTA"].Habilitado = False
    
    Formulario["CSC_ACESSO_ERP"].Visivel = False
    Formulario["CSC_ACESSO_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_REDE_EMAIL"].Visivel = True
    Formulario["CSC_ACESSO_REDE_EMAIL"].Habilitado = True
    #Formulario["CSC_ACESSO_SICON"].Visivel = False
    #Formulario["CSC_ACESSO_SICON"].Habilitado = False
    Formulario["CSC_ACESSO_SISBB"].Visivel = False
    Formulario["CSC_ACESSO_SISBB"].Habilitado = False
    #Formulario["CSC_ACESSO_TOA"].Visivel = False
    #Formulario["CSC_ACESSO_TOA"].Habilitado = False
    Formulario["CSC_ACESSO_VPN"].Visivel = False
    Formulario["CSC_ACESSO_VPN"].Habilitado = False
    Formulario["CSC_ACESSO_WIFI"].Visivel = False
    Formulario["CSC_ACESSO_WIFI"].Habilitado = False
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
    Formulario["CSC_ACESSO_PEOPLESOFT"].Visivel = True
    Formulario["CSC_ACESSO_PEOPLESOFT"].Habilitado = True
    Formulario["CSC_ACESSO_TOA"].Visivel = False
    Formulario["CSC_ACESSO_TOA"].Habilitado = False
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados Bancários (Não será aceita conta salário. Conta conjunta somente se o prestador for o titular)
  - CSC_BANCO "Banco" [DropDownList String(500) → CPE_CSC.CSC_BANCO]
  - CSC_NUMERO_AGENCIA "Número da Agência" [TextBox String → CPE_CSC.CSC_NUMERO_AGENCIA]
  - CSC_DIGITO_AGENCIA "Dígito da Agência" [TextBox String → CPE_CSC.CSC_DIGITO_AGENCIA]
  - CSC_NOME_AGENCIA "Nome Agência" [TextBox String(500) → CPE_CSC.CSC_NOME_AGENCIA]
  - CSC_CONTA_CORRENTE "Conta Corrente" [TextBox String → CPE_CSC.CSC_CONTA_CORRENTE]
  - CSC_DIGITO_CONTA_CORRENTE "Dígito Conta Corrente" [TextBox String → CPE_CSC.CSC_DIGITO_CONTA_CORRENTE]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados da Empresa do Trabalhador Temporário
  - CSC_DGCO "DGCO" [TextBox String → CPE_CSC.CSC_DGCO] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00000/0000"}
**CSC_DGCO.ScriptModificado**
```python
if OrdemServico.Servico.Sigla == "RECADASTRAMENTOPOSTO":
    clr.AddReference("Newtonsoft.Json")
    clr.AddReference("System.Net.Http")
    clr.AddReference("Supravizio.Custom")
    clr.AddReference("System.Data")

    import clr
    from System import Convert
    from Newtonsoft.Json.Linq import JArray
    from Newtonsoft.Json import JsonConvert
    from System.Net.Http import HttpClient
    from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
    from System import TimeSpan

    # Obtém valor do campo CSC_DGCO
    dgco = str(Formulario["CSC_DGCO"].Valor)

    # Token de autenticação
    token = '***MASCARADO***'

    # Obtém o ambiente (Homologação ou Produção)
    sql = "select name from sv_domain where enabled = 'Sim'"
    dom = DB.ExecuteScalar(sql)

    # Define a URL com base no ambiente
    url = ''
    if dom == 'HOMOLOGAÇÃO' or dom == 'PRODUÇÃO':    
        url = 'https://sisccon.bbts.com.br/supravizio/supra/buscar-intervenientes-por-dgco?dgco=' + dgco

    # Log para verificar a URL gerada
    Formulario['CSC_EMPRESA'].Valor = "URL: " + url

    # Verifica se a URL foi gerada corretamente
    if not url:
        Formulario['OBJETO_CONTRATACAO'].Valor = "Erro: URL não gerada corretamente."
    else:
        # Inicializa o HttpClient e configura os cabeçalhos
        client = HttpClient()
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Clear()
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.TryAddWithoutValidation("Content-Type", "application/json")
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

        # Faz a requisição GET
        try:
            response = client.GetAsync(url)
            response.Wait()

            if response.Result.IsSuccessStatusCode:
                # Lê o conteúdo da resposta
                resultAsync = response.Result.Content.ReadAsStringAsync()
                resultAsync.Wait()
                result = resultAsync.Result

                try:
                    # Verifica se o JSON está encapsulado em aspas
                    if result.startswith("\"") and result.endswith("\""):
                        result = JsonConvert.DeserializeObject(result)

                    # Converte o JSON em array
                    jsonArray = JArray.Parse(result)

                    # Se houver contratos a designar, processa os dados
                    if len(jsonArray) > 0:
                        for item in jsonArray:
                            Formulario["CSC_EMPRESA"].Valor = str(item['fornecedor'])
                            Formulario["OBJETO_CONTRATACAO"].Valor = str(item['objeto'])

                except Exception as e:
                    pass

        except Exception as e:
            pass
```
  - CSC_EMPRESA "Empresa" [TextBox String(500) → CPE_CSC.CSC_EMPRESA] obrigatório
  - OBJETO_CONTRATACAO "Objeto" [Memo String(1999) → CP_ORDEM_SERVICO.OBJETO_CONTRATACAO] obrigatório
  - DATA_ATIVIDADE "Data de Inicio da Vigência" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ATIVIDADE] obrigatório
  - DATA_FIM_PREVIST "Data de Fim da Vigência" [DatePicker DateTime → CPE_MOVIMENTACAO_PESSOA.DATA_FIM_PREVIST] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados da Área BBTS Solicitante do Trabalhador Temporário
  - CSC_CARGO_LISTA "Cargo que o Trabalhador ocupará" [DropDownList String(100) → CPE_CSC.CSC_CARGO_LISTA] obrigatório
  - CSC_DATA_INICIO "Início na BBTS (Contrato atual)" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO] obrigatório
  - CSC_DATA_FIM "Saída da BBTS" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM] obrigatório
  - CSC_LOCALIDADE_ATUACAO "Localidade Atuação" [DropDownList String → CPE_CSC.CSC_LOCALIDADE_ATUACAO] obrigatório
  - CSC_UOR_LISTA "UOR da Área Solicitante" [DropDownList String(500) → CPE_CSC.CSC_UOR_LISTA] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Acesso aos Sistemas
  - CSC_ACESSO_SICON "Acesso SICON" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_SICON] obrigatório
  - CSC_ACESSO_SISBB "Acesso SISBB" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_SISBB] obrigatório
  - CSC_ACESSO_WIFI "Acesso Wi-fi" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_WIFI] obrigatório
  - CSC_ACESSO_TOA "Acesso TOA" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_TOA] obrigatório
  - CSC_ACESSO_ERP "Acesso ERP" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_ERP] obrigatório
**CSC_ACESSO_ERP.ScriptModificado**
```python
Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
if Formulario["CSC_ACESSO_ERP"].Valor == True:
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = True
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = True
```
  - CSC_LISTA_RESP_ERP "Nome da Responsabilidade no ERP - Neste campo, indicar todos os módulos que necessita para o Sistema ERP" [DataGrid RecordList → Z_00143_CSC_LISTA_RESP_ERP.CSC_LISTA_RESP_ERP] obrigatório — QtdColunasFormulario=1
    - coluna MODULOS obrigatório
  - CSC_ACESSO_PEOPLESOFT "Acesso PEOPLESOFT" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_PEOPLESOFT]
  - CSC_ACESSO_VPN "Acesso VPN" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_VPN] obrigatório
  - CSC_ACESSO_REDE_EMAIL "Acesso Rede e E-mail" [CheckBox Boolean → CPE_CSC.CSC_ACESSO_REDE_EMAIL] obrigatório
**CSC_ACESSO_REDE_EMAIL.ScriptModificado**
```python
Formulario["CSC_ACESSO_ERP"].Visivel = False
Formulario["CSC_ACESSO_ERP"].Habilitado = False
Formulario["CSC_ACESSO_SICON"].Visivel = False
Formulario["CSC_ACESSO_SICON"].Habilitado = False
Formulario["CSC_ACESSO_SISBB"].Visivel = False
Formulario["CSC_ACESSO_SISBB"].Habilitado = False
Formulario["CSC_ACESSO_TOA"].Visivel = False
Formulario["CSC_ACESSO_TOA"].Habilitado = False
Formulario["CSC_ACESSO_VPN"].Visivel = False
Formulario["CSC_ACESSO_VPN"].Habilitado = False
Formulario["CSC_ACESSO_WIFI"].Visivel = False
Formulario["CSC_ACESSO_WIFI"].Habilitado = False
Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False

if Formulario["CSC_ACESSO_REDE_EMAIL"].Valor == True:
    Formulario["CSC_ACESSO_ERP"].Visivel = True
    Formulario["CSC_ACESSO_ERP"].Habilitado = True
    Formulario["CSC_ACESSO_SICON"].Visivel = True
    Formulario["CSC_ACESSO_SICON"].Habilitado = True
    Formulario["CSC_ACESSO_SISBB"].Visivel = True
    Formulario["CSC_ACESSO_SISBB"].Habilitado = True
    Formulario["CSC_ACESSO_TOA"].Visivel = True
    Formulario["CSC_ACESSO_TOA"].Habilitado = True
    Formulario["CSC_ACESSO_VPN"].Visivel = True
    Formulario["CSC_ACESSO_VPN"].Habilitado = True
    Formulario["CSC_ACESSO_WIFI"].Visivel = True
    Formulario["CSC_ACESSO_WIFI"].Habilitado = True
    Formulario["CSC_LISTA_RESP_ERP"].Visivel = False
    Formulario["CSC_LISTA_RESP_ERP"].Habilitado = False
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados do Trabalhador Temporário
  - COMBOBOX1 "COBAN" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO] obrigatório
  - CSC_ESTADO_EMISSOR "Estado Emissor" [DropDownList String(500) → CPE_CSC.CSC_ESTADO_EMISSOR]
  - CSC_TELEFONE_CONTATO "Telefone para Contato" [TextBox String → CPE_CSC.CSC_TELEFONE_CONTATO] obrigatório
  - CSC_DATA_NASCIMENTO "Data de nascimento" [DatePicker DateTime → CPE_CSC.CSC_DATA_NASCIMENTO] obrigatório
  - CSC_UF_NASCIMENTO "UF de Nascimento" [DropDownList String → CPE_CSC.CSC_UF_NASCIMENTO] obrigatório
  - CSC_CIDADE_NASCIMENTO "Cidade de Nascimento" [TextBox String(500) → CPE_CSC.CSC_CIDADE_NASCIMENTO] obrigatório
  - CSC_ESTADO_CIVIL "Estado Civil" [DropDownList String → CPE_CSC.CSC_ESTADO_CIVIL] obrigatório
  - CSC_UF "UF" [DropDownList String → CPE_CSC.CSC_UF] obrigatório
  - CSC_TRABALHADOR_TEMPORARIO "Trabalhador Temporário" [DropDownList String → CPE_CSC.CSC_TRABALHADOR_TEMPORARIO] obrigatório
**CSC_TRABALHADOR_TEMPORARIO.ScriptModificado**
```python
#sql = "SELECT T1.EMPLID AS ID,T1.EMAIL_ADDR2 AS EMAIL_PESSOAL,T1.NAME_DISPLAY AS NOME,T1.ADDR_FIELD2 ||' ' || T1.ADDRESS1 AS ENDERECO,T1.NUM1 AS NRO_END, T1.ADDRESS2 AS COMPLEMENTO_END, T1.ADDRESS4 AS BAIRRO,T1.STATE AS ESTADO,T1.CITY AS CIDADE,T1.POSTAL AS CEP,T1.NID_CPF_BRA AS CPF,T1.NID_RG_BRA AS RG,T1.RG_ISSUED_DT_BRA AS EMISSAO,T1.RG_ISSUEDBY_BRA  AS RG_ORGAO_EMISSOR,T1.RG_STATE_BRA AS RG_ESTADO_EMISSOR,T1.PHONE2 AS TELEFONE,T1.BIRTHDATE AS DATA_NASCIMENTO,T1.BIRTHSTATE AS ESTADO_NASCIMENTO,T1.BIRTHPLACE AS CIDADE_NASCIMENTO,T1.MAR_STATUS AS ESTADO_CIVIL,T2.BANK_CD AS CODIGO_BANCO,T2.BRANCH_EC_CD AS CODIGO_AGENCIA,DA.VERIFY_DIGIT_BRA AS DIGITO_AGENCIA,NA.DESCR AS NOME_AGENCIA,T2.ACCOUNT_EC_ID AS CONTA_NUMERO,T2.CHECK_DIGIT AS CONTA_DIGITO,T1.DEPTID AS UOR FROM PS_BBTS_FUNCS_VW T1 INNER JOIN PS_PYE_BANKACCT T2 ON T1.EMPLID   = T2.EMPLID INNER JOIN PS_BANK_BRCH_BRA DA ON T2.BANK_CD = DA.BANK_CD AND T2.BRANCH_EC_CD = DA.BRANCH_EC_CD INNER JOIN PS_BANK_BRANCH_TBL NA ON T2.BANK_CD = NA.BANK_CD AND T2.BRANCH_EC_CD = NA.BRANCH_EC_CD WHERE T2.EFF_STATUS = 'A' AND T1.EMPLID = '"+Controle.Valor.ToString()+"'"

Formulario["CSC_EMAIL_PESSOAL"].Valor = None
Formulario["CSC_LOGRADOURO"].Valor = None
Formulario["CSC_NUMERO"].Valor = None
Formulario["CSC_COMPLEMENTO"].Valor = None
Formulario["CSC_BAIRRO"].Valor = None
Formulario["CSC_UF"].Valor = None
Formulario["CSC_CIDADE"].Valor = None
Formulario["CSC_CEP"].Valor = None
Formulario["CSC_CPF"].Valor = None
Formulario["CSC_RG"].Valor = None
#Formulario["CSC_DATA_EMISSOA"].Valor = None
Formulario["CSC_ORGAO_EMISSOR"].Valor = None
Formulario["CSC_ESTADO_EMISSOR"].Valor = None
Formulario["CSC_TELEFONE_CONTATO"].Valor = None
#Formulario["CSC_DATA_NASCIMENTO"].Valor = None
Formulario["CSC_UF_NASCIMENTO"].Valor = None
Formulario["CSC_CIDADE_NASCIMENTO"].Valor = None
Formulario["CSC_ESTADO_CIVIL"].Valor = None
Formulario["CSC_BANCO"].Valor = None
Formulario["CSC_CONTA_CORRENTE"].Valor = None
Formulario["CSC_DIGITO_AGENCIA"].Valor = None
Formulario["CSC_DIGITO_CONTA_CORRENTE"].Valor = None
Formulario["CSC_NOME_AGENCIA"].Valor = None
Formulario["CSC_NUMERO_AGENCIA"].Valor = None
Formulario["CSC_UOR_LISTA"].Valor = None

#sql = "SELECT ID, EMAIL_PESSOAL, NOME, ENDERECO, NRO_END, COMPLEMENTO_END, BAIRRO, TO_CHAR(ESTADO) AS ESTADO, CIDADE, CEP, CPF, RG, EMISSAO, RG_ORGAO_EMISSOR, TO_CHAR(RG_ESTADO_EMISSOR) AS RG_ESTADO_EMISSOR, TELEFONE, DATA_NASCIMENTO, TO_CHAR(ESTADO_NASCIMENTO) AS ESTADO_NASCIMENTO, CIDADE_NASCIMENTO, ESTADO_CIVIL, CODIGO_BANCO, CODIGO_AGENCIA, DIGITO_AGENCIA, NOME_AGENCIA, CONTA_NUMERO, CONTA_DIGITO, UOR FROM VW_BBTS_TRABALHADOR_TEMPORARIO WHERE ID = '"+Controle.Valor.ToString()+"'"
sql = "select DISTINCT PAPF.npw_number as ID, NULL AS EMAIL_PESSOAL,PAPF.full_name as NOME, pa.address_line1 AS ENDERECO, pa.address_line2 AS NRO_END, pa.address_line3 AS COMPLEMENTO_END, pa.region_1 AS BAIRRO, pa.region_2 AS ESTADO, pa.town_or_city AS CIDADE, pa.postal_code AS CEP,PAPF.NATIONAL_IDENTIFIER as CPF, PA.TELEPHONE_NUMBER_1 AS TELEFONE, NVL(TO_CHAR(PAPF.DATE_OF_BIRTH, 'DD/MM/RRRR'),'01/01/1900') AS DATA_NASCIMENTO, PAPF.TOWN_OF_BIRTH AS CIDADE_NASCIMENTO,'' AS ESTADO_NASCIMENTO, PAPF.MARITAL_STATUS AS ESTADO_CIVIL , NULL AS CODIGO_BANCO, NULL AS CODIGO_AGENCIA, NULL AS DIGITO_AGENCIA, NULL AS NOME_AGENCIA, NULL AS CONTA_NUMERO, NULL AS CONTA_DIGITO, NULL AS UOR, NULL AS RG, '01/01/1900' AS EMISSAO, NULL AS RG_ORGAO_EMISSOR, '' AS RG_ESTADO_EMISSOR from per_all_people_f PAPF INNER JOIN per_all_assignments_f PAAF ON paaf.person_id = papf.person_id LEFT JOIN per_addresses PA ON pa.person_id = papf.person_id where PAPF.EFFECTIVE_START_DATE = (SELECT MAX(PAPF1.EFFECTIVE_START_DATE)FROM per_all_people_f PAPF1 WHERE papf1.person_id = papf.person_id) AND PAAF.EFFECTIVE_START_DATE = (SELECT MAX(PAAF1.EFFECTIVE_START_DATE)FROM per_all_assignments_f PAAF1 WHERE PAAF1.person_id = PAAF.person_id) AND (PAPF.npw_number = '"+Controle.Valor.ToString()+"' or PAPF.employee_number = '"+Controle.Valor.ToString()+"')"

#Formulario.ExibeMensagem(sql)
info = DB.ExecuteDataTable(sql)

for linha in info.Rows:
    Formulario["CSC_EMAIL_PESSOAL"].Valor = linha['EMAIL_PESSOAL'].ToString()
    Formulario["CSC_LOGRADOURO"].Valor = linha['ENDERECO'].ToString()
    Formulario["CSC_NUMERO"].Valor = linha['NRO_END'].ToString()
    Formulario["CSC_COMPLEMENTO"].Valor = linha['COMPLEMENTO_END'].ToString()
    Formulario["CSC_BAIRRO"].Valor = linha['BAIRRO'].ToString()
    Formulario["CSC_UF"].Valor = linha['ESTADO'].ToString()
    Formulario["CSC_CIDADE"].Valor = linha['CIDADE'].ToString()
    Formulario["CSC_CEP"].Valor = linha['CEP'].ToString()
    Formulario["CSC_CPF"].Valor = linha['CPF'].ToString()
    Formulario["CSC_RG"].Valor = linha['RG'].ToString()
    #Formulario["CSC_DATA_EMISSOA"].Valor = linha['EMISSAO'].ToString()
    Formulario["CSC_ORGAO_EMISSOR"].Valor = linha['RG_ORGAO_EMISSOR'].ToString()
    Formulario["CSC_ESTADO_EMISSOR"].Valor = linha['RG_ESTADO_EMISSOR'].ToString()
    Formulario["CSC_TELEFONE_CONTATO"].Valor = linha['TELEFONE'].ToString()
    #Formulario["CSC_DATA_NASCIMENTO"].Valor = linha['DATA_NASCIMENTO'].ToString()
    Formulario["CSC_UF_NASCIMENTO"].Valor = linha['ESTADO_NASCIMENTO'].ToString()
    Formulario["CSC_CIDADE_NASCIMENTO"].Valor = linha['CIDADE_NASCIMENTO'].ToString()
    Formulario["CSC_ESTADO_CIVIL"].Valor = linha['ESTADO_CIVIL'].ToString()
    Formulario["CSC_BANCO"].Valor = linha['CODIGO_BANCO'].ToString()
    Formulario["CSC_CONTA_CORRENTE"].Valor = linha['CONTA_NUMERO'].ToString()
    Formulario["CSC_DIGITO_AGENCIA"].Valor = linha['DIGITO_AGENCIA'].ToString()
    Formulario["CSC_DIGITO_CONTA_CORRENTE"].Valor = linha['CONTA_DIGITO'].ToString()
    Formulario["CSC_NOME_AGENCIA"].Valor = linha['NOME_AGENCIA'].ToString()
    Formulario["CSC_NUMERO_AGENCIA"].Valor = linha['CODIGO_AGENCIA'].ToString()
    Formulario["CSC_UOR_LISTA"].Valor = linha['UOR'].ToString()

    

if OrdemServico.Servico.Sigla.ToString() == 'DESTRABALHADORTEMPORARIO' or OrdemServico.Servico.Sigla.ToString() == 'PRORTRABALHADORTEMPORARIO':
    sql_si = "select count(1) as CONTADOR from SI_LOGON where AUTORIZADO = 'S' AND MATRICULA = '"+linha['ID'].ToString()+"'"
    info_si = DB.ExecuteScalar("select count(1) as CONTADOR from SI_LOGON where AUTORIZADO = 'S' AND MATRICULA = '"+linha['ID'].ToString()+"'")
    Formulario.ExibeMensagem(sql_si.ToString())
    if info_si > 0:
        Formulario["CSC_ACESSO_REDE_EMAIL"].Valor = True
```
  - CSC_EMAIL_PESSOAL "E-mail Pessoal" [TextBox String(500) → CPE_CSC.CSC_EMAIL_PESSOAL]
  - CSC_ESCOLARIDADE "Escolaridade" [TextBox String → CPE_CSC.CSC_ESCOLARIDADE] obrigatório
  - CSC_LOGRADOURO "Logradouro" [TextBox String(500) → CPE_CSC.CSC_LOGRADOURO] obrigatório
  - CSC_NUMERO "Número" [TextBox String(100) → CPE_CSC.CSC_NUMERO] obrigatório
  - CSC_COMPLEMENTO "Complemento" [TextBox String(500) → CPE_CSC.CSC_COMPLEMENTO]
  - CSC_BAIRRO "Bairro" [TextBox String(500) → CPE_CSC.CSC_BAIRRO] obrigatório
  - CSC_CIDADE "Cidade" [TextBox String(500) → CPE_CSC.CSC_CIDADE] obrigatório
  - CSC_CEP "CEP" [TextBox String → CPE_CSC.CSC_CEP] obrigatório
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF] — Configuracao={"SalvaLiteralMascara":false, "Mascara":""}
  - CSC_RG "RG" [TextBox String → CPE_CSC.CSC_RG]
  - CSC_DATA_EMISSOA "Emissão" [DatePicker DateTime → CPE_CSC.CSC_DATA_EMISSOA]
  - CSC_ORGAO_EMISSOR "Órgão Emissor" [TextBox String(200) → CPE_CSC.CSC_ORGAO_EMISSOR]

### [370836] Tarefa "Rescindir com Trabalhador Temporário no HR"
Responsável: Responsável atual (papel 36)
**ScriptFim**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#OrdemServico.Favorecido=Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("SELECT DISTINCT(ID_PESSOA) ID FROM CP_PESSOA WHERE MATRICULA = '"+OrdemServico["CSC_MATRICULA"]+"'")))
#OrdemServico.Salva()
nome = DB.ExecuteScalar("select distinct npw_number|| ' - ' ||UPPER(full_name) as NOME from per_all_people_f where npw_number is not null and npw_number ='"+OrdemServico["CSC_TRABALHADOR_TEMPORARIO"].ToString()+"'  GROUP BY npw_number,full_name")
if nome != "" and nome != None:
    OrdemServico.SetCustom("CSC_NOME_COMPLETO",nome)
    OrdemServico.Salva()
```
**ScriptFormCarregado**
```python
Formulario["LABEL1"].Valor = '<span style=\"color: Black; font-weight: bold\"><br><br>A seleção do Trabalhador Temporário deve aguardar o Supravizio importar as informações do People (Dia do Cadastro + 1).</span>'
Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = False
Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = False
Formulario["CSC_NOME_COMPLETO"].Visivel = True
Formulario["CSC_NOME_COMPLETO"].Habilitado = True
Formulario["CSC_UOR"].Valor = OrdemServico["CSC_UOR_LISTA"]
if OrdemServico.Servico.Sigla.ToString() == 'DESTRABALHADORTEMPORARIO' or OrdemServico.Servico.Sigla.ToString() == 'PRORTRABALHADORTEMPORARIO':
    Formulario["CSC_NOME_COMPLETO"].Visivel = False
    Formulario["CSC_NOME_COMPLETO"].Habilitado = False
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Visivel = True
    Formulario["CSC_TRABALHADOR_TEMPORARIO"].Habilitado = True
    Formulario["CSC_MATRICULA"].Habilitado = True
    Formulario["CSC_UOR"].Habilitado = True
    
    #sql = "SELECT MATRICULA, SUBSTR(ORGANIZACAO,1,10) ORGANIZACAO FROM CAD_FUNCIONARIO_V WHERE MATRICULA ='"+OrdemServico["CSC_TRABALHADOR_TEMPORARIO"].ToString()+"' ORDER BY NOME"
    #info = DB.ExecuteDataTable(sql)

    #for linha in info.Rows:
    #    Formulario["CSC_MATRICULA"].Valor = linha['MATRICULA'].ToString()
    #    Formulario["CSC_UOR"].Valor = linha['ORGANIZACAO'].ToString()
```
- Operação PR0001 Preencher Campos
  - CSC_UOR "UOR no People" [TextBox String → CPE_CSC.CSC_UOR] obrigatório
  - LABEL1 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO] obrigatório
  - CSC_TRABALHADOR_TEMPORARIO "Trabalhador Temporário" [DropDownList String → CPE_CSC.CSC_TRABALHADOR_TEMPORARIO] obrigatório
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório

### [370814] FimCancelamento ""
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
OrdemServico.MotivoCancelamento = OrdemServico.ObtemMotivoReprovacao("ACEITA")
```

### [370815] EventoFinal "Finalização de Chamado"
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [370816] Tarefa "Iniciar"
Responsável: Fila CSC - Prestação de Serviços (papel 539)

## Papéis usados
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```
### papel 461: Fila CSC - Pendente de Aprovação
Tipo=RelacaoPessoas | pessoas: Fila CSC - Pendente de Aprovação
### papel 670: Gestor da UOR do Trab Temporario
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Processo.Custom import Ator
id = DB.ExecuteScalar(" select id_orgao from orgao where sigla = "+ OrdemServico["CSC_UOR_LISTA"] +" ")

idScr = Convert.ToInt32(id)
scr = Orgao.Carrega(idScr)
if (scr != None):
    pessoa = scr.Gestor
    if (pessoa != None):
        Atores.Adiciona(pessoa)
```
### papel 539: Fila CSC - Prestação de Serviços
Tipo=RelacaoPessoas | pessoas: Fila CSC - Prestação de Serviços

## Campos customizados usados (definição global)

### CSC_LOCALIDADE_ATUACAO — Localidade Atuação
DropDownList String → CPE_CSC.CSC_LOCALIDADE_ATUACAO
Descrição: Localidade Autação
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT E.ESTABID, E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE)")
```

### CSC_UOR_LISTA — UOR
DropDownList String(500) → CPE_CSC.CSC_UOR_LISTA
**LookupScript**
```python
Itens=DB.ExecuteDataTable(" SELECT DISTINCT SCR, NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO where nome <> SCR ||' - ' ORDER BY SCR ")
```

### CSC_NOME_COMPLETO — Nome Completo
TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO

### CSC_TRABALHADOR_TEMPORARIO — Trabalhador Temporário
DropDownList String → CPE_CSC.CSC_TRABALHADOR_TEMPORARIO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("select TO_CHAR(p.npw_number) as MATRICULA, p.npw_number || ' - ' ||UPPER(p.full_name) as NOME from per_all_people_f p where p.npw_number is not null and p.effective_start_date = (select max(p2.effective_start_date) from per_all_people_f p2 where p2.full_name = p.full_name) UNION select TO_CHAR(p.employee_number) as MATRICULA, p.employee_number || ' - ' ||UPPER(p.full_name) as NOME from per_all_people_f p where p.employee_number is not null and p.effective_start_date = (select max(p2.effective_start_date) from per_all_people_f p2 where p2.full_name = p.full_name)")
```

### CSC_MATRICULA — Matrícula
TextBox String → CPE_CSC.CSC_MATRICULA

### CSC_CPF — CPF
TextBox String(300) → CPE_CSC.CSC_CPF

### CSC_DATA_INICIO — Data Início
DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO

### CSC_DATA_FIM — Data Fim
DatePicker DateTime → CPE_CSC.CSC_DATA_FIM

### CSC_LISTA_RESP_ERP — Nome da Responsabilidade no ERP 
DataGrid RecordList → Z_00143_CSC_LISTA_RESP_ERP.CSC_LISTA_RESP_ERP
Colunas do registro:
- MODULOS "Módulo" [TextBox String]

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### CSC_UOR — CSC_UOR
TextBox String → CPE_CSC.CSC_UOR

### COMBOBOX1 — Chamado Aberto?
DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1

### CSC_DGCO — DGCO
TextBox String → CPE_CSC.CSC_DGCO

### CSC_EMPRESA — Empresa
TextBox String(500) → CPE_CSC.CSC_EMPRESA

### OBJETO_CONTRATACAO — Objeto da Contratação
Memo String(1999) → CP_ORDEM_SERVICO.OBJETO_CONTRATACAO

### DATA_ATIVIDADE — Data da atividade
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ATIVIDADE

### DATA_FIM_PREVIST — Data fim previsto
DatePicker DateTime → CPE_MOVIMENTACAO_PESSOA.DATA_FIM_PREVIST

### CSC_CAT — Listas de atuação dos Técnicos de Campo
DropDownList String → CPE_CSC.CSC_CAT
**LookupScript**
```python
Itens = DB.ExecuteDataTable("select DESCR50 from ps_bbts_loc_atend")
```

### CSC_CARGO_LISTA — Cargo que o Trabalhador ocupará
DropDownList String(100) → CPE_CSC.CSC_CARGO_LISTA
Itens: Técnico; Analista
;Posto de Serviço de TI;Posto de Serviço de teleatendimento;Posto de Serviço - Outros


### CSC_ACESSO_REDE_EMAIL — Acesso Rede e E-mail
CheckBox Boolean → CPE_CSC.CSC_ACESSO_REDE_EMAIL

### CSC_ACESSO_VPN — Acesso VPN
CheckBox Boolean → CPE_CSC.CSC_ACESSO_VPN

### CSC_ACESSO_SICON — Acesso SICON
CheckBox Boolean → CPE_CSC.CSC_ACESSO_SICON

### CSC_ACESSO_SISBB — Acesso SISBB
CheckBox Boolean → CPE_CSC.CSC_ACESSO_SISBB

### CSC_ACESSO_WIFI — Acesso Wi-fi
CheckBox Boolean → CPE_CSC.CSC_ACESSO_WIFI

### CSC_ACESSO_ERP — Acesso ERP
CheckBox Boolean → CPE_CSC.CSC_ACESSO_ERP

### CSC_ACESSO_PEOPLESOFT — Acesso PEOPLESOFT
CheckBox Boolean → CPE_CSC.CSC_ACESSO_PEOPLESOFT

### LABEL2 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL2
Descrição: Texto informativo

### CSC_NOME_AGENCIA — Nome Agência
TextBox String(500) → CPE_CSC.CSC_NOME_AGENCIA

### CSC_CONTA_CORRENTE — Conta Corrente
TextBox String → CPE_CSC.CSC_CONTA_CORRENTE

### CSC_DIGITO_CONTA_CORRENTE — Dígito Conta Corrente
TextBox String → CPE_CSC.CSC_DIGITO_CONTA_CORRENTE

### CSC_BANCO — Banco
DropDownList String(500) → CPE_CSC.CSC_BANCO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT B.BANK_CD,B.BANK_CD ||' - ' || B.BANK_NM AS DESCRICAO FROM PS_BANK_EC_TBL B WHERE EFF_STATUS='A' ORDER BY B.BANK_CD")
```

### CSC_NUMERO_AGENCIA — Número da Agência
TextBox String → CPE_CSC.CSC_NUMERO_AGENCIA

### CSC_DIGITO_AGENCIA — Dígito da Agência
TextBox String → CPE_CSC.CSC_DIGITO_AGENCIA

### CSC_ORGAO_EMISSOR — Órgão Emissor
TextBox String(200) → CPE_CSC.CSC_ORGAO_EMISSOR

### CSC_ESTADO_EMISSOR — Estado Emissor
DropDownList String(500) → CPE_CSC.CSC_ESTADO_EMISSOR
**LookupScript**
```python
Itens = DB.ExecuteDataTable("select ID_ESTADO, DESCRICAO from ESTADO_V where ID_PAIS = 'BRA'")
```

### CSC_TELEFONE_CONTATO — Telefone para Contato
TextBox String → CPE_CSC.CSC_TELEFONE_CONTATO

### CSC_DATA_NASCIMENTO — Data de nascimento
DatePicker DateTime → CPE_CSC.CSC_DATA_NASCIMENTO

### SEXO_M_F — Sexo
DropDownList String → CPE_CSC.SEXO_M_F
Itens: Masculino;Feminino

### CSC_UF_NASCIMENTO — UF de Nascimento
DropDownList String → CPE_CSC.CSC_UF_NASCIMENTO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("select ID_ESTADO, DESCRICAO from ESTADO_V where ID_PAIS = 'BRA'")
```

### CSC_CIDADE_NASCIMENTO — Cidade de Nascimento
TextBox String(500) → CPE_CSC.CSC_CIDADE_NASCIMENTO
**LookupScript**
```python
#Itens = DB.ExecuteDataTable("SELECT TO_CHAR(ID_CIDADE), DESCRICAO FROM CIDADE_V ORDER BY DESCRICAO")
```

### CSC_ESTADO_CIVIL — Estado Civil
DropDownList String → CPE_CSC.CSC_ESTADO_CIVIL
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT ID_ESTADO_CIVIL, DESCRICAO FROM ESTADO_CIVIL_V ORDER BY DESCRICAO")
```

### CSC_ESCOLARIDADE — Escolaridade
TextBox String → CPE_CSC.CSC_ESCOLARIDADE

### CSC_EMAIL_PESSOAL — E-mail Pessoal
TextBox String(500) → CPE_CSC.CSC_EMAIL_PESSOAL

### CSC_LOGRADOURO — Logradouro
TextBox String(500) → CPE_CSC.CSC_LOGRADOURO

### CSC_NUMERO — Número
TextBox String(100) → CPE_CSC.CSC_NUMERO

### CSC_COMPLEMENTO — Complemento
TextBox String(500) → CPE_CSC.CSC_COMPLEMENTO

### CSC_BAIRRO — Bairro
TextBox String(500) → CPE_CSC.CSC_BAIRRO

### CSC_UF — UF
DropDownList String → CPE_CSC.CSC_UF
**LookupScript**
```python
Itens = DB.ExecuteDataTable("select ID_ESTADO, DESCRICAO from ESTADO_V where ID_PAIS = 'BRA'")
```

### CSC_CIDADE — Cidade
TextBox String(500) → CPE_CSC.CSC_CIDADE
**LookupScript**
```python
#Itens = DB.ExecuteDataTable("SELECT DESCRICAO FROM CIDADE_V ORDER BY DESCRICAO")
```

### CSC_CEP — CEP
TextBox String → CPE_CSC.CSC_CEP

### CSC_RG — RG
TextBox String → CPE_CSC.CSC_RG

### CSC_DATA_EMISSOA — Emissão
DatePicker DateTime → CPE_CSC.CSC_DATA_EMISSOA

### MATRICULA — Matrícula
TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA

### SIM_NAO5 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO5
Itens: Sim;Não

### CSC_ACESSO_TOA — Acesso TOA
CheckBox Boolean → CPE_CSC.CSC_ACESSO_TOA

## Biblioteca de scripts referenciada
sysAid, teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
