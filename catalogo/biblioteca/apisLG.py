# apisLG
# Caminho: Catálogo > Biblioteca de scripts > apisLG
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (4 variantes entre os XMLs; esta é a mais recente)

import clr
import time
from System import *
clr.AddReference("Supravizio.Custom")
from Venki.Supravizio.Processo.Custom import OrdemServico
from Venki.Supravizio.Processo.Custom import Servico
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Recurso.Custom import Tecnico
from System.Text import StringBuilder

clr.AddReference("System")
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
from System.Globalization import CultureInfo
import re
# URL da API
url = ''
sql="select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)

if dom == 'DESENVOLVIMENTO': 
    urlORDS = 'https://ords0.bbts.com.br/bbts/xxbbtslg/rh-funcionarios/v1/'
    urlLG = 'https://apis0.bbts.com.br/LG_SUPRAVIZIO/'
    tokenLG='***MASCARADO***'

if dom == 'HOMOLOGAÇÃO':    
    urlORDS = 'https://ords0.bbts.com.br/bbts/xxbbtslg/rh-funcionarios/v1/'
    urlLG = 'https://apis0.bbts.com.br/LG_SUPRAVIZIO/'
    tokenLG='***MASCARADO***'

if dom == 'PRODUÇÃO':    
    urlORDS = 'https://ords.bbts.com.br/bbts/xxbbtslg/rh-funcionarios/v1/'
    urlLG = 'https://apis.bbts.com.br/LG_SUPRAVIZIO/'
    tokenLG='***MASCARADO***'
    
#A chamada retorna os seguintes campos:
#   "cdMatricula": "0000000", - Matrícula do funcionário consultado
#    "dtEfetiva": "DD-MM-YYYY", - Data de inicio do valor do salário base
#    "vlCompensacao": 9999.99, - valor do salario base
#    "cdDepartamento": "0000000000" - Número da Uor do funcionário

def consultaValoresPlanoSaude(p_plano, p_idade): 
    
    try:

        c = HttpClient()
        token=tokenLG
        c.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        c.Timeout = TimeSpan(0,0,15,0,0)
        c.DefaultRequestHeaders.Accept.Clear()
        c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        response =  c.GetAsync(urlLG+"valor_plano_saude/v1?p_empresa=001")
        response.Wait()
        resultAsync =  response.Result.Content.ReadAsStringAsync()
        resultAsync.Wait()
        result = resultAsync.Result
        obj  = JsonConvert.DeserializeObject(result);
        msg = 'Erro verificar no LOG do Supravizio'

        if obj.success == True:
            msg = "Lista de valores do Plano retornada com Sucesso."
            if obj.data.ToString() == 'Null':
                msg = msg+" Lista de valores da API retornada vazia."
            else:
                plano=''
                idadeAux=''
                for linha in obj.data:
                    #plano=linha.DescricaoDaFaixa
                    if linha.DescricaoDaFaixa.ToString() != '':
                        plano=linha.DescricaoDaFaixa.ToString()
                    idadeI=linha.ValorInicial.ToString().Split('.');
                    if idadeI[1].ToString() == '':
                        idadeI[1]= '0'
                    idadeI=Convert.ToDecimal(idadeI[1].ToString())
                    idadeF=linha.ValorFinal.ToString().Split('.');
                    if idadeF[1].ToString() == '99':
                        idadeF[1] = '200'
                    if idadeF[1].ToString() == '':
                        idadeF[1] = '0'
                    idadeF=Convert.ToDecimal(idadeF[1].ToString())
                    
                    p_idade2=Convert.ToDecimal(p_idade.ToString())

                    if p_plano.ToUpper() == plano.ToUpper() and (p_idade2 >= idadeI and p_idade2 <= idadeF):
                        return("{\"success\": true, \"data\": "+linha.Deducao.ToString()+"}")
                    else:
                        msg=' Não foram encontrados valores dentro dos parâmetros passados.'           
        return("{\"success\": false,\"errors\": " + msg.ToString() + ",\"data\": 0}")

    except Exception as e:
        Utils.LogError("Erro ao autenticar no LG: "+ e.Message + " URL: " + urlORDS.ToString(), "Erro " + OrdemServico.Numero.ToString());
        return ("{\"success\": false,\"errors\": Erro ao autenticar no LG: " + e.Message.ToString() + ",\"data\": 0}")
        
def consultaMargemConsignavel(p_matricula, p_ano_folha, p_mes_folha):
        
    try:
        c = HttpClient()
        token=tokenLG
        c.Timeout = TimeSpan(0,0,15,0,0)
        c.DefaultRequestHeaders.Accept.Clear()
        c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        
        if dom == 'PRODUÇÃO':
            c.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
            chamadaAPI = urlLG.ToString()+"margem_consignavel/v1?empresa_codigo=1&codigo_lancamento=17900&tipo_folha=1&matricula="+p_matricula.ToString()+"&ano_folha="+p_ano_folha.ToString()+"&mes_folha="+p_mes_folha.ToString()
        else:    
            chamadaAPI = urlORDS.ToString()+"margem_consignavel/v1?empresa_codigo=1&codigo_lancamento=17900&tipo_folha=1&matricula="+p_matricula.ToString()+"&ano_folha="+p_ano_folha.ToString()+"&mes_folha="+p_mes_folha.ToString()
        
        response = c.GetAsync(chamadaAPI)
        response.Wait()
        resultAsync =  response.Result.Content.ReadAsStringAsync()
        resultAsync.Wait()
        result = resultAsync.Result
        #obj = JObject.Parse(result)
        obj  = JsonConvert.DeserializeObject(result);
        
        if obj["success"]== True:
            if obj["data"]["margem_consignavel"]!='':
                try:     
            
                    valorConsignavel = Decimal.Parse(obj["data"]["margem_consignavel"].ToString(),CultureInfo.InvariantCulture)
                    ptBR = CultureInfo("pt-BR")
                    consignavelMoeda = valorConsignavel.ToString("C", ptBR)
                    Utils.LogInformation("Chamada Margem consignavel - URL: "+chamadaAPI.ToString()+"Retorno margem: "+consignavelMoeda, "Information")
                    return consignavelMoeda
                except Exception as e:
                    
                    Utils.LogError("Erro ao realizar a conversão da margem: "+e.Message)
                    return("{\"success\": false,\"errors\": Erro ao realizar a conversão da margem: " + e.Message.ToString() + ",\"data\": 0}")
                return obj["data"]["margem_consignavel"].ToString()
            else:
                return 'R$ 0,00'
        else:
            Utils.LogError("Retorno sem sucesso da API")

    except Exception as e:
        Utils.LogError("Erro ao realizar a consulta na API LG: "+ e.Message+" Consulta realizada na url: "+chamadaAPI.ToString(), "Erro " + OrdemServico.Numero.ToString())
        return ("{\"success\": false,\"errors\": Erro ao realizar a consulta na API LG: " + e.Message.ToString() + ",\"data\": 0}")
