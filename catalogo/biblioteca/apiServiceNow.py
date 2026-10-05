# apiServiceNow
# Caminho: Catálogo > Biblioteca de scripts > apiServiceNow
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

# Importa bibliotecas essenciais do ambiente .NET e do Supravizio
import clr
import time
import System
import re
import time

# Adiciona referências a assemblies utilizados na execução do script
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("Supravizio.Custom")
clr.AddReference("System")
clr.AddReference("System.Data")

# Importações de tipos e classes .NET utilizadas no código
from datetime import datetime
from System import DateTime
from System import *
from System import Text
from System import Convert, TimeSpan
from System import String
from System.Globalization import CultureInfo
from System.Text import NormalizationForm
from System.Text import *
from System.Text import StringBuilder
from System.Data import DataSet
from System.Collections.Generic import *
from System.Collections.Generic import Dictionary
from System.IO import *

# Importações da biblioteca Newtonsoft.Json para manipulação de JSON
from Newtonsoft.Json import *
from Newtonsoft.Json import JsonConvert
from Newtonsoft.Json.Linq import *
from Newtonsoft.Json.Linq import JObject
from Newtonsoft.Json.Linq import JArray, JValue

# Importações para uso de requisições HTTP
from System.Net.Http import *
from System.Net.Http.Headers import *
from System.Net.Http import HttpClient
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# Importações de classes específicas do Supravizio
from Venki.Supravizio.Processo.Custom import OrdemServico
from Venki.Supravizio.Processo.Custom import Servico
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Recurso.Custom import Tecnico

#seleção da url conforme o ambiente
sql="select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)
if dom == 'HOMOLOGAÇÃO':
    urlSN= 'https://apis0.bbts.com.br/snow'
if dom == 'PRODUÇÃO':
    urlSN= 'https://apis.bbts.com.br/snow'
    
# Função para pegar o token de acesso a API ServiceNow ITSM
def getToken():
    try:
        #Definindo a URL do endpoint e os parâmetros de autenticação
        url = urlSN+'/token'
        params = Dictionary[str, str]()

        if dom == 'PRODUÇÃO':
            params.Add("client_id", '')
            params.Add("client_secret", '')
            params.Add("username", '')
            params.Add("password", '')
        elif dom == 'HOMOLOGAÇÃO':
            params.Add("client_id", '6c55a4e5a3c14303ba345144a913c2de')
            params.Add("client_secret", 'd+-Jwhu2Er')
            params.Add("username", 'integracao.supravizio')
            params.Add("password", 'ho+bVF<&#i=V_!8;Z,2.M=;.L4e)b>pKz#;$k6rdQo<IfCEpiM^,eF!nmCAq-Z],djOei8bD-uAc}vsrFd(CaoyLFQ&2t!,B_Hz_')
        params.Add("grant_type", "password")  #Definindo o grant_type
         
        #Criando o cliente HTTP
        client = HttpClient()
        
        #Definindo o conteúdo da requisição como x-www-form-urlencoded
        content = FormUrlEncodedContent(params)
        
        Utils.LogError("Realizando requisição POST para " + url.ToString() , "Debug " + OrdemServico.Numero.ToString())
        
        #Fazendo a requisição POST para autenticação
        response = client.PostAsync(url, content).Result
        
        #Verificando se a resposta é bem-sucedida
        if response.IsSuccessStatusCode:
            # Lendo o conteúdo da resposta
            result = response.Content.ReadAsStringAsync().Result
            Utils.LogError("Autenticação bem-sucedida " + url.ToString() , "Debug " + OrdemServico.Numero.ToString())
            jsonResult = JObject.Parse(result)  #Converte a resposta em JSON
            return jsonResult['access_token'].ToString()
        else:
            Utils.LogError("Erro na autenticação. Código de status: " + response.StatusCode.ToString() + " Detalhes: " + response.Content.ReadAsStringAsync().Result + " URL: " + url.ToString() , "Erro " + OrdemServico.Numero.ToString())
            return ("{\"isSuccess\": false,\"errors\": Erro na autenticação. Código de status: " + response.StatusCode.ToString() + " Detalhes: " + response.Content.ReadAsStringAsync().Result + " URL: " + url.ToString() + ",\"data\": 0}")
    except Exception as e:
    
        Utils.LogError("Erro ao autenticar no ServiceNow ITSM: "+ e.Message + " URL: " + url.ToString(), "Erro " + OrdemServico.Numero.ToString());
        return ("{\"isSuccess\": false,\"errors\": Erro ao autenticar no ServiceNow ITSM: " + e.Message.ToString() + ",\"data\": 0}")    

def criarIncidente(descricao, titulo, impacto, urgencia, categoria, subcat, sintoma, tipoIncidente, origem ):
    try:
    
        # Construção do JSON principal
        #Alteração número documento
        json = "{"+ "\"short_description\": \"" + titulo.ToString() + "\", "+ "\"description\": \"" + descricao.ToString() + "\", "+ "\"impact\": " + impacto.ToString() + ", "+ "\"urgency\": " + urgencia.ToString() + ", "+ "\"category\": \"" + categoria.ToString() + "\", "+ "\"subcategory\": \"" + subcat.ToString() + "\", "+ "\"u_sintoma\": \"" + sintoma.ToString() + "\", "+ "\"u_incident_type\": \"" + tipoIncidente.ToString() + "\", "+ "\"u_id_ref_origem\": \"" + origem.ToString() + "\"}"
        
        
        Utils.LogError("Passa Json" + json.ToString() , "Debug " + OrdemServico.Numero.ToString())
        
        #Utils.LogError("Passa Json" , "Debug " + OrdemServico.Numero.ToString())
        
        #OrdemServico.AdicionaComentario(json.ToString(), False)
        #OrdemServico.Justificativa = json.ToString()
        #return json.ToString()
        
        # Autenticação e envio da requisição
        token = getToken()
        
        if token is None:
            Utils.LogError("Erro ao obter token de autenticação. ", "Erro " + OrdemServico.Numero.ToString())
            return ("{\"isSuccess\": false,\"errors\": Erro ao obter token de autenticação.,\"data\": 0}")
            
        
        client = HttpClient()
        data = StringContent(json, Encoding.UTF8, "application/json")
        url2 = urlSN + "/itsm/x_bbtes_bbts_int_1/bbts_incidente/criar"
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

        response = client.PostAsync(url2, data).Result
        if response.IsSuccessStatusCode:
            result = response.Content.ReadAsStringAsync().Result
            return result
        else: 
            Utils.LogError("Json " + json.ToString() , "Debug " + OrdemServico.Numero.ToString())
            
            Utils.LogError("Erro na API : " + response.StatusCode.ToString() + " Detalhes: " + response.Content.ReadAsStringAsync().Result.ToString(), "Erro " + OrdemServico.Numero.ToString())        
        return result
    
    except Exception as e:
        Utils.LogError("Erro geral - Erro ao enviar JSON abertura de incidente: " + e.Message.ToString(), "Erro " + OrdemServico.Numero.ToString())
        return ("{\"isSuccess\": false,\"errors\": Erro geral - Erro ao enviar JSON abertura de incidente:  " + e.Message.ToString() + ",\"data\": 0}")

#Função para consulta de incidentes
def consultarIncidente(sys_id):

        # Autenticação e envio da requisição
        token = getToken()

        #parte fixa das url's
        consultaEndpoint='/itsm/now/table/incident/' 
        paransConsulta='?sysparm_fields=number%2Cshort_description%2Cdescription'
        
        if token is None:
            Utils.LogError("Erro ao obter token de autenticação. ", "Erro " + OrdemServico.Numero.ToString())
            return ("{\"isSuccess\": false,\"errors\": Erro ao obter token de autenticação.,\"data\": 0}")
        else:
            clientConsulta = HttpClient()
            clientConsulta.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
            #responseConsulta = clientConsulta.GetAsync('https://apis0.bbts.com.br/snow/itsm/now/table/incident/aa0b0895fbe366504ef5f7b56eefdcfe?sysparm_fields=number%2Cshort_description%2Cdescription').Result
            responseConsulta = clientConsulta.GetAsync(urlSN+consultaEndpoint+sys_id+paransConsulta).Result
            #jsonResult = JObject.Parse(responseConsulta)
            Utils.LogError('Resposta da Consulta ao Incidente numero '+sys_id+': '+ responseConsulta.StatusCode.ToString(),'HTTP RES')
            
            
            return responseConsulta.Content.ReadAsStringAsync().Result

        
# Função para remover acentos
def remover_acentos(texto):
    try:
        texto_normalizado = texto.Normalize(NormalizationForm.FormD)
        texto_sem_acentos = ""
        for c in texto_normalizado:
            if not System.Globalization.CharUnicodeInfo.GetUnicodeCategory(c).ToString().startswith("NonSpacingMark"):
                texto_sem_acentos += c
        return texto_sem_acentos
    except Exception as e:
        Utils.LogError("Erro ao remover acentos: " + str(e), "remover_acentos" )
        return texto
    


# Função para obter processo associado a uma OS
def obter_processo_associado(numero_os):
    qry = "SELECT pai.id_ocorrencia, pai.numero, filho.id_ocorrencia AS id_ocorrenciacf, filho.numero, csp.sigla AS sigla_processo, csp.descricao AS desc_processo " + \
    "FROM associacao_ocorr ass " + \
        "INNER JOIN ocorrencia pai ON pai.id_ocorrencia = ass.id_ocorr_fonte " + \
        "INNER JOIN ocorrencia filho ON filho.id_ocorrencia = ass.id_ocorr_alvo " + \
        "INNER JOIN classe_sub_processo csp ON pai.ID_CLASSE_SUB_PROC = csp.id_classe_sub_processo " \
    "WHERE filho.numero = '" + numero_os.ToString() + "' "
    return DB.ExecuteDataTable(qry)
    

# Corrige string JSON com barras invertidas e converte em objeto
def corrigir_json_pagamentos(pagamentos):
    try:
        pagamentosJson = pagamentos.replace('\\"', '"')
        json_obj = JObject.Parse(pagamentosJson)
        if not json_obj["pagamentos"]:
            raise Exception("Campo 'pagamentos' não encontrado ou está vazio.")
        return json_obj["pagamentos"]
    except Exception as e:
        Utils.LogError("Erro ao converter JSON de pagamentos: " + str(e), "corrigir_json_pagamentos")
        raise

# Função para anexar um arquivo em base64 à OS
def anexar_arquivo_base64(nome_arquivo, arquivo_base64):
    try:
        caminho_arquivo = "\\\\santacruz1.cobra.com.br\\supravizio$\\" + nome_arquivo.ToString()
        bytes_arquivo = Convert.FromBase64String(arquivo_base64)
        File.WriteAllBytes(caminho_arquivo, bytes_arquivo)
        return caminho_arquivo
    except Exception as e:
        Utils.LogError("Erro ao processar arquivo base64: " + str(e), "anexar_arquivo_base64" )
        raise
        
def validar_parametros_obrigatorios(pagamento, campos, numero_os):
    for campo in campos:
        if pagamento[campo] is None or pagamento[campo].ToString().Trim() == "":
            return ("{\"status\": \"erro\", \"mensagem\": \"Campo obrigatório '" + campo + "' ausente, nulo, em branco ou vazio no pagamento.\", \"detalhes\": [{\"numero_os\": \"" + numero_os + "\"}]}")
    return None

def processar_anexo(os, caminho, tipo_anexo):
    try:
        os.AnexaArquivo(caminho, tipo_anexo, True)
        return True
    except Exception as e:
        Utils.LogError("Erro ao anexar arquivo: " + str(e), "Anexo")
        return False

def processar_pagamento(os, array_pagamentos, numero_os, desc, campo_data, tipo_anexo):
    for pagamento in array_pagamentos:
        erro_validacao = validar_parametros_obrigatorios(pagamento, ["arquivo_base64", "nome_arquivo"], numero_os)
        if erro_validacao:
            return erro_validacao

        numeroRI = pagamento["numero_ri"].ToString()
        dataPagamento = pagamento["data_pagamento"].ToString()
        nomeArquivo = pagamento["nome_arquivo"].ToString()
        arquivoBase64 = pagamento["arquivo_base64"].ToString()
        dataFormatada = DateTime.Parse(dataPagamento).ToString("dd/MM/yyyy")

        if campo_data:
            os[campo_data] = dataPagamento

        caminho = anexar_arquivo_base64(nomeArquivo, arquivoBase64)
        processar_anexo(os, caminho, tipo_anexo)

        Utils.LogInformation("Pagamento atualizado com sucesso | Número da OS: " + numero_os + " | Número do RI: " + numeroRI + " | Data: " + dataFormatada, "Atualização Processo " + desc)
        break

    os.AvancaAtividade()
    os.Salva()
    return None

def processar_guias(os, array_pagamentos, numero_os, idOcorrenciaCF):
    listaGrid = os["GUIASJUDICIAIS"]

    for pagamento in array_pagamentos:
        erro_validacao = validar_parametros_obrigatorios(pagamento, ["arquivo_base64", "nome_arquivo"], numero_os)
        if erro_validacao:
            return erro_validacao

        numeroRI = pagamento["numero_ri"].ToString()
        dataPagamento = pagamento["data_pagamento"].ToString()
        nomeArquivo = pagamento["nome_arquivo"].ToString()
        arquivoBase64 = pagamento["arquivo_base64"].ToString()
        dataFormatada = DateTime.Parse(dataPagamento).ToString("dd/MM/yyyy")

        encontrouRI = False

        for linha in listaGrid.Rows:
            if linha["NUMERO_RI"].ToString() == numeroRI:
                encontrouRI = True
                tipoGuia = remover_acentos(linha["CUSTASDEPOSITO"].ToString().lower())
                linha["DATA_PAGAMENTO"] = dataPagamento

                caminho = anexar_arquivo_base64(nomeArquivo, arquivoBase64)
                tipo_anexo = "COMPAGCUSTAS" if tipoGuia == "custas" else "COMPAG"
                processar_anexo(os, caminho, tipo_anexo)

                Utils.LogInformation("Arquivo anexado com sucesso: " + caminho + " | Número da OS: " + numero_os.ToString(), "Arquivo")
                os["GUIASJUDICIAIS"] = os["GUIASJUDICIAIS"]
                os.Salva()
                Utils.LogInformation("Pagamento atualizado com sucesso | Número da OS: " + numero_os + " | Número do RI: " + numeroRI + " | Data do pagamento: " + dataFormatada, "Atualização de Guia Judicial")
                break

        if not encontrouRI:
            return ("{\"status\": \"erro\", \"mensagem\": \"O número do RI " + numeroRI + " não foi localizado nas guias vinculadas ao chamado.\", \"detalhes\": [{\"numero_os\": \"" + numero_os + "\", \"status\": \"Falha ao localizar o número do RI na grid de pagamentos judiciais\"}]}")

    qry1 = "SELECT g.id_ocorrencia FROM Z_00143_GUIASJUDICIAIS g WHERE g.id_ocorrencia = '" + idOcorrenciaCF.ToString() + "' AND g.data_pagamento is not null"
    guias = DB.ExecuteDataTable(qry1)

    if listaGrid.Rows.Count == guias.Rows.Count:
        os.AvancaAtividade()

    return None

# Função principal

def receber_pagamento(numero_os, pagamentos):
    try:
        if not numero_os or not pagamentos:
            return ("{\"status\": \"erro\", \"mensagem\": \"Parâmetros obrigatórios ausentes: número_os e pagamentos são requeridos.\", \"detalhes\": []}")

        processo = obter_processo_associado(numero_os)

        if processo.Rows.Count == 0:
            return ("{\"status\": \"erro\", \"mensagem\": \"O número do chamado informado não foi localizado\", \"detalhes\": [{\"numero_os\": \"" + numero_os + "\", \"status\": \"Ordem de serviço associada não encontrada no sistema.\"}]}")

        row = processo.Rows[0]
        sigla = row['SIGLA_PROCESSO']
        desc = row['DESC_PROCESSO']
        idOcorrenciaCF = row['id_ocorrenciaCF']

        os = OrdemServico.Carrega(idOcorrenciaCF)

        try:
            array_pagamentos = corrigir_json_pagamentos(pagamentos)
        except Exception as e:
            return ("{\"status\": \"erro\", \"mensagem\": \"Erro ao interpretar o JSON de pagamentos: " + str(e) + "\", \"detalhes\": [{\"numero_os\": \"" + numero_os + "\"}]}")

        #sigla subprocesso: (nome campo data do pagamento, sigla item de configuração)
        parametros_por_sigla = {
            "ANUIDADEORDEMCLASSE":     ("DATA_APROVACAO", "ARQUIVO"),
            "AUXILIOADAPTACAO":        ("DATA_APROVACAO", "ARQUIVO"),
            "MUDPECCEDBB":             ("DATA_APROVACAO", "ARQUIVO"),
            "PGTORCC":                 ("DATA_APROVACAO", "ARQUIVO"),
            "PGTOTRIBUTOS":            ("DATA_DE_PAGAMENTO", "ARQUIVO"),
            "TRT":                     ("DATA_DE_PAGAMENTO", "ARQUIVO"),
            "ARQUIVOELETROBANCARIO":   (None, "ARQUIVOELETROBANCARIO"),
            "PDPEP":                   (None, "ARQUIVOELETROBANCARIO"),
            "PUBLICARDOU":             (None, "ARQUIVOELETROBANCARIO"),
            "SDESTAB":                 ("DATA_DE_PAGAMENTO", "ARQJURI"),
            "PROGRAMAECOA":            ("DATA_DE_PAGAMENTO_3", "COMPAG")
        }

        if sigla == "SOLICITARPAGAMENTOSJUDICIAIS":
            erro = processar_guias(os, array_pagamentos, numero_os, idOcorrenciaCF)
        elif sigla in parametros_por_sigla:
            campo_data, tipo_anexo = parametros_por_sigla[sigla]
            erro = processar_pagamento(os, array_pagamentos, numero_os, desc, campo_data, tipo_anexo)
        else:
            Utils.LogInformation("sigla: " + sigla.ToString(), "Pagamento Serviço")
            return ("{\"status\": \"erro\", \"mensagem\": \"Serviço " + desc + " não compatível para este tipo de pagamento.\", \"detalhes\": [{\"numero_os\": \"" + numero_os + "\", \"status\": \"Serviço está na lista de automação deste processo.\"}]}")

        if erro:
            return erro

        return ("{\"status\": \"sucesso\", \"mensagem\": \"Pagamento registrado com sucesso.\", \"detalhes\": [{\"numero_os\": \"" + numero_os + "\", \"status\": \"Dados da ordem de serviço atualizados corretamente.\"}]}")

    except Exception as e:
        Utils.LogError("Erro inesperado em receber_pagamento: " + str(e), "Receber Pagamento")
        return ("{\"status\": \"erro\", \"mensagem\": \"Erro interno ao processar pagamento: " + str(e) + "\", \"detalhes\": [{\"numero_os\": \"" + numero_os + "\"}]}")
