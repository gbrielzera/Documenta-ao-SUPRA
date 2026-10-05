# ebs
# Caminho: Catálogo > Biblioteca de scripts > ebs
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

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
sql="select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)
if dom == 'HOMOLOGAÇÃO':
    urlORDS= 'https://ords1.bbts.com.br'
if dom == 'PRODUÇÃO':
    urlORDS= 'https://ords.bbts.com.br'

def cadastro_nf_ri(json):

    client = HttpClient()
    data = StringContent(json,Encoding.UTF8,"application/json")
    url = urlORDS+"/ords/cqrsebs/cqrsebs/ri/v1/create_ri_entry"
    response =  client.PostAsync(url, data).Result
    result = response.Content.ReadAsStringAsync()
    result = result.Result
    resultado = result.ToString()
    return resultado
    
    
def cadastroFornecedor(json):
    client = HttpClient()
    
    data = StringContent(json,Encoding.UTF8,"application/json")
    
    url = urlORDS+"/ords/cqrsebs/cqrsebs/intsv/v1/cria_fornecedor/"
    
    response =  client.PostAsync(url, data).Result
    
    result = response.Content.ReadAsStringAsync()
    result = result.Result
    resultado = result.ToString()
    return resultado
    
def cadastroCliente(json):
    client = HttpClient()
    
    data = StringContent(json,Encoding.UTF8,"application/json")
    
    url = urlORDS+"/ords/cqrsebs/cqrsebs/intsv/v1/cria_cliente/"
    
    response =  client.PostAsync(url, data).Result
    
    result = response.Content.ReadAsStringAsync()
    result = result.Result
    resultado = result.ToString()
    return resultado
    
def listarCATTRSSUPER():
    
    obj = None
    
    # Cria o cliente HTTP
    c = HttpClient()
    c.Timeout = TimeSpan(0,0,15,0,0)
    c.DefaultRequestHeaders.Accept.Clear()
    c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
    response =  c.GetAsync(urlORDS+"/bbts/cqrsebs/cqrsebs/supravizio/v1/lista_grupos_crm")
    response.Wait()
    resultAsync =  response.Result.Content.ReadAsStringAsync()
    resultAsync.Wait()
    result = resultAsync.Result

    if result != None:
        obj  = JsonConvert.DeserializeObject(result);
        #OrdemServico.AdicionaComentario(obj["abertura"].ToString(),False);
        return obj
    else:
        return 'sem resultado'

    #
    #response =  client.PostAsync(url).Result
    #
    #result = response.Content.ReadAsStringAsync()
    #result = result.Result
    #resultado = result.ToString()
    #return resultado
    #
def consultaEmpregadoCRM(matricula):

    obj = None
    
    # Cria o cliente HTTP
    c = HttpClient()
    c.Timeout = TimeSpan(0,0,15,0,0)
    c.DefaultRequestHeaders.Accept.Clear()
    c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
    response =  c.GetAsync(urlORDS+"/bbts/cqrsebs/cqrsebs/supravizio/v1/employee_ebs?matricula="+matricula)
    response.Wait()
    resultAsync =  response.Result.Content.ReadAsStringAsync()
    resultAsync.Wait()
    result = resultAsync.Result
    #return result.ToString()
    if result != None:
        obj  = JsonConvert.DeserializeObject(result);
        #OrdemServico.AdicionaComentario(obj["abertura"].ToString(),False);
        return obj
    else:
        return 'sem resultado'


    #response =  client.PostAsync(url,data).Result
    #
    #result = response.Content.ReadAsStringAsync()
    #result = result.Result
    #resultado = result.ToString()
    #return resultado
    
def consultaEmpregadoPSFTCRM(matricula):
    obj = None
    
    # Cria o cliente HTTP
    c = HttpClient()
    c.Timeout = TimeSpan(0,0,15,0,0)
    c.DefaultRequestHeaders.Accept.Clear()
    c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
    response =  c.GetAsync(urlORDS+"/bbts/cqrsebs/cqrsebs/supravizio/v1/employee_people_ebs?matricula="+matricula)
    response.Wait()
    resultAsync =  response.Result.Content.ReadAsStringAsync()
    resultAsync.Wait()
    result = resultAsync.Result
    #return result.ToString()
    if result != None:
        obj  = JsonConvert.DeserializeObject(result);
        #OrdemServico.AdicionaComentario(obj["abertura"].ToString(),False);
        return obj
    else:
        return 'sem resultado'


    #response =  client.PostAsync(url).Result
    #
    #result = response.Content.ReadAsStringAsync()
    #result = result.Result
    #resultado = result.ToString()
    #return resultado
