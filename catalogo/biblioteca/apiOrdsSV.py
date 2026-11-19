# apiOrdsSV
# Caminho: Catálogo > Biblioteca de scripts > apiOrdsSV
# Fonte: Reembolsos__I.A_Versão_1_Reembolso_-_Iniciativa_IA.xml

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
if dom == 'DESENVOLVIMENTO':
    urlORDS= 'https://ords0.bbts.com.br'
if dom == 'HOMOLOGAÇÃO':
    urlORDS= 'https://ords1.bbts.com.br'
if dom == 'PRODUÇÃO':
    urlORDS= 'https://ords.bbts.com.br'

def atualizaTab(linha_id):
    json=''
    client = HttpClient()
    data = StringContent(json,Encoding.UTF8,"application/json")
    url = urlORDS+"/bbts/ebs/spvz/v1/arquivo_deslocamento/?tipoOperacao=ATUALIZAR&cadastroId="+linha_id.ToString()
    response =  client.PostAsync(url, data).Result
    return response

    
def consultaTab(chamado):
    
    obj = None
    
    # Cria o cliente HTTP
    c = HttpClient()
    c.Timeout = TimeSpan(0,0,15,0,0)
    c.DefaultRequestHeaders.Accept.Clear()
    c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
    response =  c.GetAsync(urlORDS+"/bbts/ebs/spvz/v1/arquivo_deslocamento/?os="+chamado.ToString())
    response.Wait()
    resultAsync =  response.Result.Content.ReadAsStringAsync()
    resultAsync.Wait()
    result = resultAsync.Result
    #return result
    if result != None:
        obj  = JsonConvert.DeserializeObject(result);
        #OrdemServico.AdicionaComentario(obj["items"].ToString(),False);
        return obj
    else:
        return 'sem resultado'
