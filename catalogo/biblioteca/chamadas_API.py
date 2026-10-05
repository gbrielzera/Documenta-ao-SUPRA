# chamadas_API
# Caminho: Catálogo > Biblioteca de scripts > chamadas_API
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
from Newtonsoft.Json import *
from Newtonsoft.Json.Linq import *
from System.Net import *
#from System.Net.IWebProxy import *
from System.Net.Http import *
from System.Net.Http.Headers import *
#from System.Net.Http.HttpClientHandler import *
 
def testeRetorno(tipo):
    if tipo == 'erro':
        return '{"x_cod_return":"520","x_msg_return":"pg_bbts_integracao_ri.pr_integra_ri_api[E_ERRO]: Origem [COBAN] ou Tipo de Nota[] não autorizado para a integração."}'
    elif tipo == 'sucesso':
        return '{"x_cod_return":"200","x_interface_invoice_id":4401054,"x_msg_return":"Dados Integrados com sucesso: concurrent Id[122985167] - Status Interface[6]:","x_num_entr_operacao":52752,"x_status_operacao":"COMPLETE","x_num_ri":"5271898","x_dt_pgto":"27-SET-2024","x_val_ri":"16801.28"}'
    #else:
    #    return 'Não definido'

# CNPJ NÃO PODE TER CARÁTER ESPECIAL
def retornaCNPJ(campo):
   
    obj = None
    #httFormulario.ExibeMensagem(mensagem)DB.ExecuteScalar(commandText)DB.ExecuteScalar(commandText)
    c = HttpClient()
    c.Timeout = TimeSpan(0,0,15,0,0)
    c.DefaultRequestHeaders.Accept.Clear()
    c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
   
    #response =  c.GetAsync("http://ords0.bbts.com.br:8080/bbts/ebs/spvz/v1/consulta_lista_bens_tranf/?p_sigla_servico="+campo.ToString())
   #TRANSFBENFUNCMSMUOR
    response.Wait()
    #if response.IsSuccessStatusCode:
    resultAsync =  response.Result.Content.ReadAsStringAsync()
    resultAsync.Wait()
    result = resultAsync.Result
    if result != None:
        obj  = JsonConvert.DeserializeObject(result);
        #OrdemServico.AdicionaComentario(obj["items"].ToString(),False);
    return obj["items"].ToString()

# Consulta cnpj na receita federal - CNPJ NÃO PODE TER CARÁTER ESPECIAL
def receitaws_CNPJ(campo):

    obj = None
    result = None
    # Cria o cliente HTTP
    c = HttpClient()
    c.Timeout = TimeSpan(0,0,15,0,0)
    c.DefaultRequestHeaders.Accept.Clear()
    c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
    response =  c.GetAsync("http://receitaws.com.br/v1/cnpj/"+campo.ToString())
    response.Wait()
    resultAsync =  response.Result.Content.ReadAsStringAsync()
    resultAsync.Wait()
    result = resultAsync.Result
    #return result
    if result != None:
        obj  = JsonConvert.DeserializeObject(result);
        #OrdemServico.AdicionaComentario(obj["abertura"].ToString(),False);
        return obj
    else:
        return 'sem resultado'
