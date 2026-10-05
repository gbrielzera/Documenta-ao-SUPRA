# consultaPeopleBASE
# Caminho: Catálogo > Biblioteca de scripts > consultaPeopleBASE
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
import re
# URL da API
url = ''
sql="select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)

if dom == 'HOMOLOGAÇÃO':    
    url = 'http://apis.bbts.com.br:8000/func_pmi'

if dom == 'PRODUÇÃO':    
    url = 'http://apis.bbts.com.br:8000/func_pmi'
        
    
    
def consultaAusencias(matricula,data): 
    try:
        c = HttpClient()
        token='***MASCARADO***'
        c.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        
        c.Timeout = TimeSpan(0,0,15,0,0)
        c.DefaultRequestHeaders.Accept.Clear()
        c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        response =  c.GetAsync(urlPS+"ausencias/v1?matricula="+matricula+"&dataInicial="+data)
        response.Wait()
        resultAsync =  response.Result.Content.ReadAsStringAsync()
        resultAsync.Wait()
        result = resultAsync.Result
        jsonResult = JObject.Parse(result)  #Converte a resposta em JSON
        #return "b"+result
        if jsonResult['lsAusencias'].ToString() != '[]':
            return jsonResult['lsAusencias']
        else:
            return 'Matrícula ou data não encontrada'

    except Exception as e:
    
        return ("{\"isSuccess\": false,\"errors\": Erro ao autenticar: " + e.Message.ToString() + ",\"data\": 0}")
        

def consultaFuncionarios(status, matricula):
    try:
        c = HttpClient()
        token='***MASCARADO***'
        c.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        
        c.Timeout = TimeSpan(0,0,15,0,0)
        c.DefaultRequestHeaders.Accept.Clear()
        c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        response =  c.GetAsync(urlPS+"funcionarios/v2?status="+status+"&matricula="+matricula)
        response.Wait()
        resultAsync =  response.Result.Content.ReadAsStringAsync()
        resultAsync.Wait()
        result = resultAsync.Result
        jsonResult = JObject.Parse(result)  
        
        #return "b"+result
        if jsonResult['lsFuncionarios'].ToString() != '[]':
            return jsonResult['lsFuncionarios']
        else:
            return 'Matrícula ou tipo não encontrados'

    except Exception as e:
    
        return ("{\"isSuccess\": false,\"errors\": Erro ao autenticar: " + e.Message.ToString() + ",\"data\": 0}")
