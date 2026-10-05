# peopleSoft
# Caminho: Catálogo > Biblioteca de scripts > peopleSoft
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (3 variantes entre os XMLs; esta é a mais recente)

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
    url = 'http://apis.bbts.com.br:8000/func_pmi/'
    urlPS = 'http://apis1.bbts.com.br:8000/psft/'
    urlORDS = 'https://ords1.bbts.com.br/bbts/intass/psft/v1/'
    tokenPS='***MASCARADO***'

if dom == 'PRODUÇÃO':
    url = 'http://apis.bbts.com.br:8000/func_pmi/'
    urlPS = 'http://apis.bbts.com.br:8000/psft/'
    tokenPS='***MASCARADO***'
    
#A chamada retorna os seguintes campos:
#   "cdMatricula": "0000000", - Matrícula do funcionário consultado
#    "dtEfetiva": "DD-MM-YYYY", - Data de inicio do valor do salário base
#    "vlCompensacao": 9999.99, - valor do salario base
#    "cdDepartamento": "0000000000" - Número da Uor do funcionário

def consultaValorMaxReembolso(sexo,idade): 
    try:
        c = HttpClient()
        token=tokenPS
        c.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        c.Timeout = TimeSpan(0,0,15,0,0)
        c.DefaultRequestHeaders.Accept.Clear()
        c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        response =  c.GetAsync(urlPS+"reembolsomaximo/v1?tpSexo="+sexo+"&tpIdade="+idade)
        response.Wait()
        resultAsync =  response.Result.Content.ReadAsStringAsync()
        resultAsync.Wait()
        result = resultAsync.Result
        if result != None:
            valor = result.find('"type"').ToString()
            if valor == '-1':
                obj  = JsonConvert.DeserializeObject(result);
                return obj
            valor = result.find('"vlMaximo"').ToString()
            if valor == '-1':
                return 'sem resultado'
        else:
            return 'sem resultado'

    except Exception as e:
        #Utils.LogError("Erro ao autenticar: "+ e.Message + " URL: " +url+"?matricula="+param1, "Erro " + OrdemServico.Numero.ToString());
        return ("{\"isSuccess\": false,\"errors\": Erro ao autenticar: " + e.Message.ToString() + ",\"data\": 0}")

def consultaSalbase(matricula): 
    try:
        c = HttpClient()
        token=tokenPS
        c.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        c.Timeout = TimeSpan(0,0,15,0,0)
        c.DefaultRequestHeaders.Accept.Clear()
        c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        response =  c.GetAsync(urlPS+"remuneracao/v1?nremp="+matricula)
        response.Wait()
        resultAsync =  response.Result.Content.ReadAsStringAsync()
        resultAsync.Wait()
        result = resultAsync.Result
        if result != None:
            valor = result.find('"type"').ToString()
            if valor == '-1':
                obj  = JsonConvert.DeserializeObject(result);
                return obj
            valor = result.find('"cdMatricula"').ToString()
            if valor == '-1':
                return 'sem resultado'
        else:
            return 'sem resultado'

    except Exception as e:
        #Utils.LogError("Erro ao autenticar: "+ e.Message + " URL: " +url+"?matricula="+param1, "Erro " + OrdemServico.Numero.ToString());
        return ("{\"isSuccess\": false,\"errors\": Erro ao autenticar: " + e.Message.ToString() + ",\"data\": 0}")
    
def consultaAusencias(matricula,data): 
    try:
        c = HttpClient()
        token=tokenPS
        c.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        
        c.Timeout = TimeSpan(0,0,15,0,0)
        c.DefaultRequestHeaders.Accept.Clear()
        c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        response =  c.GetAsync(urlPS+"ausencias/v1?flAusenciaAtual=Y&matricula="+matricula+"&dataInicial="+data) 
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
        token=tokenPS
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
    
    
    
        
def consultaPMI(matricula): 
    
    try:
        c = HttpClient()
        
        authToken = Encoding.UTF8.GetBytes("func_pmi:^L8h%4so*jnBF.a@nZ)_")
        
        c.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Basic",Convert.ToBase64String(authToken))
        
        c.Timeout = TimeSpan(0,0,15,0,0)
        c.DefaultRequestHeaders.Accept.Clear()
        c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        response =  c.GetAsync(url+"?matricula="+matricula)
        response.Wait()
        resultAsync =  response.Result.Content.ReadAsStringAsync()
        resultAsync.Wait()
        result = resultAsync.Result
        jsonResult = JObject.Parse(result)  #Converte a resposta em JSON
        
        if jsonResult['items'].ToString() != '[]':
            obj  = jsonResult['items'][0]['st_pmi'].ToString()
            #OrdemServico.AdicionaComentario(obj["abertura"].ToString(),False);
            return obj
        else:
            return 'Matrícula não encontrada'

    except Exception as e:
    
        #Utils.LogError("Erro ao autenticar: "+ e.Message + " URL: " +url+"?matricula="+param1, "Erro " + OrdemServico.Numero.ToString());
        return ("{\"isSuccess\": false,\"errors\": Erro ao autenticar: " + e.Message.ToString() + ",\"data\": 0}")

def alterarGestorGDP(func,gestor):
    client = HttpClient()
    json = "{\"TEST_BBTS_EPEE\": {\r\n\"TEST_BBTS_EPXPRFERR\": {\"\": \"\",\" | | | | \": \"\"},\r\n\t\"TEST_BBTS_EPEEXPRF\": \r\n\t{\r\n\t\t\t\"EMPLID\": \""+func+"\",\r\n\t\t\"EP_NEW_MANAGER_ID\": \""+gestor+"\"\r\n\t}\r\n}\r\n}"
    authToken = Encoding.UTF8.GetBytes("leonam.lima:123senha")
    
    client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Basic",Convert.ToBase64String(authToken))
    
    data = StringContent(json,Encoding.UTF8,"application/json")
    
    url = "http://p05194apiaca.bbts.com.br:8000/PSIGW/RESTListeningConnector/PSFT_HR/TEST_EPEETRANSFDOC.v1/employee"
    
    response =  client.PostAsync(url, data).Result
    
    result = response.Content.ReadAsStringAsync()
    result = result.Result
    valor = result.find('"ERRORCODE": "0"').ToString()
    if valor == '-1':
        resultado = result.ToString()
    else:
        resultado = 'Sucesso'
    return resultado
