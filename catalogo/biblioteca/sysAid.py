# sysAid
# Caminho: Catálogo > Biblioteca de scripts > sysAid
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

import clr
import time
from System import *
clr.AddReference("Supravizio.Custom")
from Venki.Supravizio.Processo.Custom import OrdemServico
from Venki.Supravizio.Processo.Custom import Servico
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Recurso.Custom import Tecnico
from System.Text import StringBuilder

clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("Supravizio.Custom")
clr.AddReference("System.Data")
from Newtonsoft.Json import *
from Newtonsoft.Json.Linq import *
from System.Net.Http import *
from System.Net.Http.Headers import *
from System import *
from System.Data import DataSet
from System.Text import * 
import System
import clr
import re

def teste():
    return PowerShell.PSExecuteCmdlet("$r = Invoke-WebRequest -URI https://centraldeti.bbts.com.br -UseBasicParsing \n  $r")
    #return PowerShell.PSExecuteCmdlet("$HTTP_Request = [System.Net.WebRequest]::Create('https://centraldeti.bbts.com.br')\n $HTTP_Response = $HTTP_Request.GetResponse()\n $HTTP_Status = [int]$HTTP_Response.StatusCode\n If ($HTTP_Status -eq 200) { Write-Host 'Site is OK!'} Else { Write-Host 'The Site may be down, please check!'}\n If ($HTTP_Response -eq $null) { } Else { $HTTP_Response.Close() }")
    #return PowerShell.PSExecuteCmdlet('$r=Test-NetConnection centraldeti.bbts.com.br\n echo $r.PingSucceeded')

def transfBemPatrimonial(descricao, login):
   sql = "select count(1) from pessoa where usuario_rede ='"+login+"'"
   result = DB.ExecuteScalar(sql)
   if result ==0:
    login = '***MASCARADO***'
   assunto = "SysAid Solicitação de novo Equipamento"
   os = OrdemServico.Nova(OrdemServico.Carrega(20),'ATUALIZARDADOSERP', 'INICIOTIC', assunto , Servico.Carrega('Sigla','TRANSBENSPATRIMONIAIS'), Pessoa.Carrega('UsuarioRede',login) , Pessoa.Carrega ('UsuarioRede','fila.csc.-.bens.patrimoniais'))
   os["DESCRICAO_OBRIG"] = descricao
   os.AvancaAtividade()
   os.Salva()
   return os.Numero.ToString()
   
def loginSysAid():
    scriptLogin= "$Username = '***MASCARADO***' \n $Password = '***MASCARADO***'\n $SysAidURL = 'https://centraldeti.bbts.com.br' "
    #scriptLogin= "$Username = '***MASCARADO***' \n $Password = '***MASCARADO***'\n $SysAidURL = 'https://centraldeti.bbts.com.br' "
    scriptLogin2= '\nFunction Get-SysAidToken {\n    Param(\n    [parameter(Mandatory=$true)]\n    [String]$Username,\n    [Parameter(Mandatory=$true)]\n    [String]$Password,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "$SysAidURL/api/v1/login"\n$ContentType = "application/json"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n    "user_name": "$Username",\n    "password": "$Password"\n}\n"@\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$props = @{\n    Uri = $Uri.AbsoluteUri \n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body = $Body\n}\nTry {\n$WebRequest = Invoke-WebRequest -UseBasicParsing @props -ErrorAction Stop\n$StatusCode = $WebRequest.StatusCode\n}\nCatch {\n$StatusCode = $_.Exception.Response.StatusCode.value__\n}\nif ($StatusCode -eq "200") {\nWrite-Verbose "The Web Request Was Successful, Capturing JSESSIONID Cookie..." -Verbose\n$cookies = $WebSession.Cookies.GetCookies($Uri)\nreturn $cookies\nWrite-Verbose "$cookies" -Verbose\n}\nelseif ($StatusCode -eq "401") {\nWrite-Verbose "The Web Request Failed, with status code $StatusCode. Please enter the correct login information." -Verbose\n}\nelseif ($StatusCode -ne "200" -or "401") {\nWrite-Verbose "The Web Request Failed, with status code $StatusCode. Please verify the entered parameters." -Verbose\n}\nreturn $cookies\n} '
    scriptLogin3=scriptLogin + scriptLogin2 + "$JSESSIONID = Get-SysAidToken -Username $Username -Password $Password -SysAidURL $SysAidURL \n $JSESSIONID.Value"
    resposta = PowerShell.PSExecuteCmdlet(scriptLogin3)
    return resposta
    #return scriptLogin3
    
def consultaUsuario(email):
    token=loginSysAid()
    scriptConsUsu='\nFunction consulta_usuario {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n  [Parameter(Mandatory=$true)]\n    [string]$Email\n )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/users/search?query=$Email&fields=first_name"\n$ContentType = "application/json"\n$Method = '+"'GET'"+'\n\n$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n Uri = $Uri.AbsoluteUri\n ContentType = $ContentType\n Method = $Method\n WebSession = $WebSession\n}\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props\n}\n$retornoUsu = consulta_usuario -JSESSIONID '+token[1].ToString()+' -Email '+email.ToString()+' \n$retornoUsu'
    resposta = token[1].ToString()
    resposta = PowerShell.PSExecuteCmdlet(scriptConsUsu)
    if resposta == None:
        resposta = None
    else:
        scriptConsUsu='\nFunction consulta_usuario {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n  [Parameter(Mandatory=$true)]\n    [string]$Email\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/users/search?query=$Email&fields=first_name"\n$ContentType = "application/json"\n$Method = '+"'GET'"+'\n\n$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n}\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props\n}\n$retornoUsu = consulta_usuario -JSESSIONID '+token[1].ToString()+' -Email '+email+' \n$retornoUsu.id'
        resposta = PowerShell.PSExecuteCmdlet(scriptConsUsu)  
    return resposta
    
def bloqueio147(categoria, titulo, descricao, localidade, idSolic, idAtend):
    token=loginSysAid()
    scriptCU='$SysAidURL = "https://centraldeti.bbts.com.br"\nFunction bloqueio {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuSolicitante,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuAtendido,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=147"\n$ContentType = "application/json; charset=UTF-8"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n           {"key":"title", "value":"'+titulo+'"},\n           {"key":"problem_type", "value":"'+categoria+'"},\n           {"key":"description", "value":"'+descricao+'"},\n           {"key":"status", "value":"1"},\n           {"key":"request_user", "value":"$UsuSolicitante"},\n           {"key":"followup_user", "value":"$UsuAtendido"},\n           {"key":"CustomColumn8sr", "value":"00000"},\n           {"key":"CustomColumn9sr", "value":"'+localidade+'"},\n           {"key":"assigned_group", "value":"7610"}\n           ]\n}\n"@\n '
    scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
    scriptCU3 = '$retorno = bloqueio -JSESSIONID '+token[1].ToString()+' -SysAidURL $SysAidURL -UsuSolicitante '+idSolic.ToString()+' -UsuAtendido '+idAtend.ToString()+' \n $retorno.id'
    script = scriptCU + scriptCU2 + scriptCU3
    #OrdemServico.DescricaoDetalhada = script
    resposta = PowerShell.PSExecuteCmdlet(script)
    return resposta
    
def bloqueio23067(categoria, titulo, descricao, localidade, idSolic, idAtend, dataRecisao):
    token=loginSysAid()
    scriptCU='$SysAidURL = "https://centraldeti.bbts.com.br"\nFunction bloqueio {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuSolicitante,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuAtendido,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=23067"\n$ContentType = "application/json; charset=UTF-8"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n           {"key":"title", "value":"'+titulo+'"},\n           {"key":"problem_type", "value":"'+categoria+'"},\n           {"key":"description", "value":"'+descricao+'"},\n           {"key":"status", "value":"1"},\n           {"key":"request_user", "value":"$UsuSolicitante"},\n           {"key":"followup_user", "value":"$UsuAtendido"},\n           {"key":"CustomColumn8sr", "value":"00000"},\n           {"key":"CustomColumn9sr", "value":"'+localidade+'"},\n           {"key":"CustomColumn284sr", "value":"'+dataRecisao+'"},\n           {"key":"assigned_group", "value":"7610"}\n           ]\n}\n"@\n '
    scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
    scriptCU3 = '$retorno = bloqueio -JSESSIONID '+token[1].ToString()+' -SysAidURL $SysAidURL -UsuSolicitante '+idSolic.ToString()+' -UsuAtendido '+idAtend.ToString()+' \n $retorno.id'
    script = scriptCU + scriptCU2 + scriptCU3
    #OrdemServico.DescricaoDetalhada = script
    resposta = PowerShell.PSExecuteCmdlet(script)
    return resposta
    
def acessoVPN478(categoria, titulo, descricao,dtIncio, idSolic, idAtend):
    token=loginSysAid()
    scriptCU='$SysAidURL = "https://centraldeti.bbts.com.br"\nFunction liberaAcesso {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuSolicitante,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuAtendido,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=478"\n$ContentType = "application/json; charset=UTF-8"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n           {"key":"title", "value":"'+titulo+'"},\n           {"key":"problem_type", "value":"'+categoria+'"},\n           {"key":"description", "value":"'+descricao+'"},\n           {"key":"request_user", "value":"$UsuSolicitante"},\n           {"key":"followup_user", "value":"$UsuAtendido"},\n           {"key":"CustomColumn8sr", "value":"00000"},\n           {"key":"CustomColumn12sr", "value":"'+dtIncio.ToString()+'"},\n           {"key":"CustomColumn32sr", "value":"6"},\n           {"key":"CustomColumn51sr", "value":""},\n           {"key":"assigned_group", "value":"7610"}\n           ]\n}\n"@\n '
    scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
    scriptCU3 = '$retorno = liberaAcesso -JSESSIONID '+token[1].ToString()+' -SysAidURL $SysAidURL -UsuSolicitante '+idSolic.ToString()+' -UsuAtendido '+idAtend.ToString()+' \n $retorno.id'
    script = scriptCU + scriptCU2 + scriptCU3
    #OrdemServico.DescricaoDetalhada = script
    resposta = PowerShell.PSExecuteCmdlet(script)
    return resposta
    
    
def acessoVPN11192(categoria, titulo, descricao,dtIncio, idSolic, idAtend):
    token=loginSysAid()
    scriptCU='$SysAidURL = "https://centraldeti.bbts.com.br"\nFunction liberaAcesso {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuSolicitante,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuAtendido,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=11192"\n$ContentType = "application/json; charset=UTF-8"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n           {"key":"title", "value":"'+titulo+'"},\n           {"key":"problem_type", "value":"'+categoria+'"},\n           {"key":"description", "value":"'+descricao+'"},\n           {"key":"request_user", "value":"$UsuSolicitante"},\n           {"key":"followup_user", "value":"$UsuAtendido"},\n           {"key":"CustomColumn8sr", "value":"00000"},\n           {"key":"CustomColumn12sr", "value":"'+dtIncio.ToString()+'"},\n           {"key":"CustomColumn32sr", "value":"6"},\n           {"key":"CustomColumn51sr", "value":""},\n           {"key":"assigned_group", "value":"7610"}\n           ]\n}\n"@\n '
    scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
    scriptCU3 = '$retorno = liberaAcesso -JSESSIONID '+token[1].ToString()+' -SysAidURL $SysAidURL -UsuSolicitante '+idSolic.ToString()+' -UsuAtendido '+idAtend.ToString()+' \n $retorno.id'
    script = scriptCU + scriptCU2 + scriptCU3
    #OrdemServico.DescricaoDetalhada = script
    resposta = PowerShell.PSExecuteCmdlet(script)
    return resposta
    
    
def acessoRede467(categoria, titulo, descricao, dtIncio, dtFim, idSolic, nomeColaborador, matricula, empresa, localidade, uor, telefone):
    token=loginSysAid()
    scriptCU='$SysAidURL = "https://centraldeti.bbts.com.br"\nFunction acessoRede {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuSolicitante,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=467"\n$ContentType = "application/json; charset=UTF-8"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n            {"key":"title", "value":"'+titulo.ToString()+'"},\n            {"key":"problem_type", "value":"'+categoria.ToString()+'"},\n            {"key":"description", "value":"'+descricao.ToString() +'"},\n            {"key":"status", "value":"1"},\n            {"key":"request_user", "value":"$UsuSolicitante"},\n            {"key":"followup_user", "value":"$UsuSolicitante"},\n            {"key":"CustomColumn16sr", "value":"'+nomeColaborador.ToString()+'"},\n            {"key":"CustomColumn15sr", "value":"'+matricula.ToString()+'"},'
    scriptCU1= '\n            {"key":"CustomColumn18sr", "value":"'+empresa.ToString()+'"},\n            {"key":"CustomColumn9sr", "value":"'+localidade.ToString()+'"},\n            {"key":"CustomColumn17sr", "value":"'+uor.ToString()+'"},\n            {"key":"CustomColumn19sr", "value":"'+dtIncio.ToString()+'"},\n            {"key":"CustomColumn20sr", "value":"'+dtFim.ToString()+'"},\n            {"key":"CustomColumn76sr", "value":"'+telefone.ToString()+'"},\n            {"key":"CustomColumn21sr", "value":"1"},\n            {"key":"assigned_group", "value":"7610"}\n            ]\n}\n"@\n '
    scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
    scriptCU3 = '$retorno = acessoRede -JSESSIONID '+token[1].ToString()+' -SysAidURL $SysAidURL -UsuSolicitante '+idSolic.ToString()+' \n$retorno.id'
    script = scriptCU + scriptCU1 + scriptCU2 + scriptCU3
    resposta = PowerShell.PSExecuteCmdlet(script)
    return resposta
    
    
    
def acessoSISBB477(categoria, titulo, descricao, idSolic, idAtend, cpf, localidade):
    token=loginSysAid()
    scriptCU='$SysAidURL = "https://centraldeti.bbts.com.br"\nFunction liberaAcesso {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuSolicitante,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuAtendido,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=477"\n$ContentType = "application/json; charset=UTF-8"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n            {"key":"title", "value":"'+titulo+'"},\n           {"key":"problem_type", "value":"'+categoria+'"},\n           {"key":"description", "value":"'+descricao+'"},\n           {"key":"request_user", "value":"$UsuSolicitante"},\n           {"key":"followup_user", "value":"$UsuAtendido"},\n           {"key":"CustomColumn9sr", "value":"'+localidade+'"},\n           {"key":"CustomColumn29sr", "value":"'+cpf+'"},\n           {"key":"CustomColumn30sr", "value":" "},\n           {"key":"CustomColumn31sr", "value":"2"},\n           {"key":"assigned_group", "value":"7610"}\n           ]\n}\n"@\n '
    scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
    scriptCU3 = '$retorno = liberaAcesso -JSESSIONID '+token[1].ToString()+' -SysAidURL $SysAidURL -UsuSolicitante '+idSolic.ToString()+' -UsuAtendido '+idAtend.ToString()+' \n $retorno.id'
    script = scriptCU + scriptCU2 + scriptCU3
    resposta = PowerShell.PSExecuteCmdlet(script)
    return resposta
    
def acessoSISBB10824(categoria, titulo, descricao, idSolic, idAtend, cpf, localidade):
    token=loginSysAid()
    scriptCU='$SysAidURL = "https://centraldeti.bbts.com.br"\nFunction liberaAcesso {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuSolicitante,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuAtendido,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=10824"\n$ContentType = "application/json; charset=UTF-8"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n            {"key":"title", "value":"'+titulo+'"},\n           {"key":"problem_type", "value":"'+categoria+'"},\n           {"key":"description", "value":"'+descricao+'"},\n           {"key":"request_user", "value":"$UsuSolicitante"},\n           {"key":"followup_user", "value":"$UsuAtendido"},\n           {"key":"CustomColumn9sr", "value":"'+localidade+'"},\n           {"key":"CustomColumn29sr", "value":"'+cpf+'"},\n           {"key":"CustomColumn30sr", "value":" "},\n           {"key":"CustomColumn31sr", "value":"2"},\n           {"key":"assigned_group", "value":"7610"}\n           ]\n}\n"@\n '
    scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
    scriptCU3 = '$retorno = liberaAcesso -JSESSIONID '+token[1].ToString()+' -SysAidURL $SysAidURL -UsuSolicitante '+idSolic.ToString()+' -UsuAtendido '+idAtend.ToString()+' \n $retorno.id'
    script = scriptCU + scriptCU2 + scriptCU3
    resposta = PowerShell.PSExecuteCmdlet(script)
    return resposta
    
def acessoSICON517(categoria, titulo, descricao, idSolic, idAtend):
    token=loginSysAid()
    scriptCU='$SysAidURL = "https://centraldeti.bbts.com.br"\nFunction liberaAcesso {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuSolicitante,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuAtendido,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=517"\n$ContentType = "application/json; charset=UTF-8"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n           {"key":"title", "value":"'+titulo+'"},\n           {"key":"problem_type", "value":"'+categoria+'"},\n           {"key":"description", "value":"'+descricao+'"},\n           {"key":"request_user", "value":"$UsuSolicitante"},\n           {"key":"followup_user", "value":"$UsuAtendido"},\n           {"key":"assigned_group", "value":"7610"}\n           ]\n}\n"@\n '
    scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
    scriptCU3 = '$retorno = liberaAcesso -JSESSIONID '+token[1].ToString()+' -SysAidURL $SysAidURL -UsuSolicitante '+idSolic.ToString()+' -UsuAtendido '+idAtend.ToString()+' \n $retorno.id'
    script = scriptCU + scriptCU2 + scriptCU3
    resposta = PowerShell.PSExecuteCmdlet(script)
    return resposta
    
def acessoSICON10822(categoria, titulo, descricao, idSolic, idAtend):
    token=loginSysAid()
    scriptCU='$SysAidURL = "https://centraldeti.bbts.com.br"\nFunction liberaAcesso {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuSolicitante,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuAtendido,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=10822"\n$ContentType = "application/json; charset=UTF-8"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n           {"key":"title", "value":"'+titulo+'"},\n           {"key":"problem_type", "value":"'+categoria+'"},\n           {"key":"description", "value":"'+descricao+'"},\n           {"key":"request_user", "value":"$UsuSolicitante"},\n           {"key":"followup_user", "value":"$UsuAtendido"},\n           {"key":"assigned_group", "value":"7610"}\n           ]\n}\n"@\n '
    scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
    scriptCU3 = '$retorno = liberaAcesso -JSESSIONID '+token[1].ToString()+' -SysAidURL $SysAidURL -UsuSolicitante '+idSolic.ToString()+' -UsuAtendido '+idAtend.ToString()+' \n $retorno.id'
    script = scriptCU + scriptCU2 + scriptCU3
    resposta = PowerShell.PSExecuteCmdlet(script)
    return resposta
    
def acessoERP482(categoria, titulo, descricao, erp, localidade, idSolic, idAtend):
    token=loginSysAid()
    scriptCU='$SysAidURL = "https://centraldeti.bbts.com.br"\nFunction liberaAcesso {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuSolicitante,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuAtendido,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=482"\n$ContentType = "application/json; charset=UTF-8"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n           {"key":"title", "value":"'+titulo+'"},\n           {"key":"problem_type", "value":"'+categoria+'"},\n           {"key":"description", "value":"'+descricao+'"},\n           {"key":"request_user", "value":"$UsuSolicitante"},\n           {"key":"followup_user", "value":"$UsuAtendido"},\n           {"key":"CustomColumn260sr", "value":"'+erp+'"},\n           {"key":"CustomColumn9sr", "value":"'+localidade+'"},\n           {"key":"assigned_group", "value":"7610"}\n           ]\n}\n"@\n '
    scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
    scriptCU3 = '$retorno = liberaAcesso -JSESSIONID '+token[1].ToString()+' -SysAidURL $SysAidURL -UsuSolicitante '+idSolic.ToString()+' -UsuAtendido '+idAtend.ToString()+' \n $retorno.id'
    script = scriptCU + scriptCU2 + scriptCU3
    resposta = PowerShell.PSExecuteCmdlet(script)
    return resposta
    
def acessoERP10814(categoria, titulo, descricao, erp, localidade, idSolic, idAtend):
    token=loginSysAid()
    scriptCU='$SysAidURL = "https://centraldeti.bbts.com.br"\nFunction liberaAcesso {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuSolicitante,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuAtendido,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=10814"\n$ContentType = "application/json; charset=UTF-8"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n           {"key":"title", "value":"'+titulo+'"},\n           {"key":"problem_type", "value":"'+categoria+'"},\n           {"key":"description", "value":"'+descricao+'"},\n           {"key":"request_user", "value":"$UsuSolicitante"},\n           {"key":"followup_user", "value":"$UsuAtendido"},\n           {"key":"CustomColumn260sr", "value":"'+erp+'"},\n           {"key":"CustomColumn9sr", "value":"'+localidade+'"},\n           {"key":"assigned_group", "value":"7610"}\n           ]\n}\n"@\n '
    scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
    scriptCU3 = '$retorno = liberaAcesso -JSESSIONID '+token[1].ToString()+' -SysAidURL $SysAidURL -UsuSolicitante '+idSolic.ToString()+' -UsuAtendido '+idAtend.ToString()+' \n $retorno.id'
    script = scriptCU + scriptCU2 + scriptCU3
    resposta = PowerShell.PSExecuteCmdlet(script)
    return resposta
    
def alteraAcesso466(categoria, titulo, descricao, localidade, idSolic, idAtend):
    token=loginSysAid()
    scriptCU='$SysAidURL = "https://centraldeti.bbts.com.br"\nFunction alteraAcesso {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuSolicitante,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuAtendido,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=466"\n$ContentType = "application/json; charset=UTF-8"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n           {"key":"title", "value":"'+titulo+'"},\n           {"key":"problem_type", "value":"'+categoria+'"},\n           {"key":"description", "value":"'+descricao+'"},\n           {"key":"status", "value":"1"},\n           {"key":"request_user", "value":"$UsuSolicitante"},\n           {"key":"followup_user", "value":"$UsuAtendido"},\n           {"key":"CustomColumn8sr", "value":"00000"},\n           {"key":"CustomColumn9sr", "value":"'+localidade+'"},\n           {"key":"assigned_group", "value":"7610"}\n           ]\n}\n"@\n '
    scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
    scriptCU3 = '$retorno = alteraAcesso -JSESSIONID '+token[1].ToString()+' -SysAidURL $SysAidURL -UsuSolicitante '+idSolic.ToString()+' -UsuAtendido '+idAtend.ToString()+' \n $retorno.id'
    script = scriptCU + scriptCU2 + scriptCU3
    #OrdemServico.DescricaoDetalhada = script
    resposta = PowerShell.PSExecuteCmdlet(script)
    return resposta
    
def alteraPermissaoNomeacao23131(categoria, titulo, descricao, localidade, idSolic, idAtend, dataNomeacao, uorDestino):
    token=loginSysAid()
    scriptCU='$SysAidURL = "https://centraldeti.bbts.com.br"\nFunction alteraAcesso {\n    Param(\n    [Parameter(Mandatory=$true)]\n    [string]$JSESSIONID,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuSolicitante,\n    [Parameter(Mandatory=$true)]\n    [string]$UsuAtendido,\n    [Parameter(Mandatory=$true)]\n    [string]$SysAidURL\n    )\n[System.Uri]$Uri  = "https://centraldeti.bbts.com.br/api/v1/sr?type=request&template=23131"\n$ContentType = "application/json; charset=UTF-8"\n$Method = '+"'POST'"+'\n$Body = @"\n{\n  "info": [\n           {"key":"title", "value":"'+titulo+'"},\n           {"key":"problem_type", "value":"'+categoria+'"},\n           {"key":"description", "value":"'+descricao+'"},\n           {"key":"status", "value":"1"},\n           {"key":"request_user", "value":"$UsuSolicitante"},\n           {"key":"followup_user", "value":"$UsuAtendido"},\n           {"key":"CustomColumn8sr", "value":"00000"},\n           {"key":"CustomColumn9sr", "value":"'+localidade+'"},\n           {"key":"CustomColumn285sr", "value":"'+dataNomeacao+'"},\n           {"key":"CustomColumn36sr", "value":"'+uorDestino+'"},\n           {"key":"assigned_group", "value":"7610"}\n           ]\n}\n"@\n '
    scriptCU2= '$Cookie = New-Object System.Net.Cookie\n$Cookie.Name = "JSESSIONID"\n$Cookie.Value = $JSESSIONID\n$Cookie.Domain = $uri.DnsSafeHost\n$WebSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession\n$WebSession.Cookies.Add($Cookie)\n$props = @{\n    Uri         = $Uri.AbsoluteUri\n    ContentType = $ContentType\n    Method      = $Method\n    WebSession  = $WebSession\n    Body        =  $Body }\nWrite-Verbose -Message "Adjusting " -Verbose\nInvoke-RestMethod @props \n}\n'
    scriptCU3 = '$retorno = alteraAcesso -JSESSIONID '+token[1].ToString()+' -SysAidURL $SysAidURL -UsuSolicitante '+idSolic.ToString()+' -UsuAtendido '+idAtend.ToString()+' \n $retorno.id'
    script = scriptCU + scriptCU2 + scriptCU3
    #OrdemServico.DescricaoDetalhada = script
    resposta = PowerShell.PSExecuteCmdlet(script)
    return resposta
