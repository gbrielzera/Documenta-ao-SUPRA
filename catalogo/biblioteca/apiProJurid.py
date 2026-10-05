# apiProJurid
# Caminho: Catálogo > Biblioteca de scripts > apiProJurid
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (3 variantes entre os XMLs; esta é a mais recente)

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("Supravizio.Custom")
clr.AddReference("System.Data")

import time
from datetime import datetime
from System import *
from System import Text
from System import Convert, TimeSpan
from System.Text import *
from System.Text import StringBuilder
from System.Data import DataSet
from System.Collections.Generic import *
from System.Collections.Generic import Dictionary
from System.IO import *
from Newtonsoft.Json import *
from Newtonsoft.Json import JsonConvert
from Newtonsoft.Json.Linq import *
from Newtonsoft.Json.Linq import JArray, JValue
from System.Net.Http import *
from System.Net.Http import HttpClient
import System
import clr
import re
 

from System.Net.Http.Headers import *
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

from Venki.Supravizio.Processo.Custom import OrdemServico
from Venki.Supravizio.Processo.Custom import Servico
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Recurso.Custom import Tecnico


# URL da API
url = ''
sql="select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)

if dom == 'HOMOLOGAÇÃO':    
    url = 'https://www.projuridweb.com.br/BBTS_ProcessoApi_Hmlg/api/'

if dom == 'PRODUÇÃO':    
    url = 'https://www.projuridweb.com.br/BBTS_ProcessoApi/api/'

def obtemCaminho():
    try:
        path = DB.ExecuteScalar("SELECT FILES_PATH FROM SERVICES_PRAM")
        return path
    except Exception as e:
        Utils.LogError("Erro ao obter caminho do arquivo: " + e.Message.ToString(), "Erro " + OrdemServico.Numero.ToString())
        return ("{\"isSuccess\": false,\"errors\": Erro ao obter caminho do arquivo: " + e.Message.ToString() + ",\"data\": 0}")


        
def autenticaProjurid(): 
    try:
        #Definindo a URL do endpoint e os parâmetros de autenticação
        urlPost = url+'security/token'
        params = Dictionary[str, str]()

        if dom == 'PRODUÇÃO':
            params.Add("client_id", '96468087-1418-483e-81cc-72edbe7fca41')
            params.Add("client_secret", '208fb8a1-f06b-4b95-be30-c341312ee60f')
        else:
            params.Add("client_id", '86e37c37-d55f-419a-bbfc-3b47beac8999')
            params.Add("client_secret", '527ab26d-b5ec-455c-b71e-1286cab9513f')
        params.Add("grant_type", "client_credentials")  #Definindo o grant_type
         
        #Criando o cliente HTTP
        client = HttpClient()
        
        #Utils.LogError(" client " + client.ToString() + " URL: " + urlPost.ToString() , "Debug " + OrdemServico.Numero.ToString())
        #Definindo o conteúdo da requisição como x-www-form-urlencoded
        content = FormUrlEncodedContent(params)
        
        #Utils.LogError(" content " + content.ToString() + " URL: " + urlPost.ToString() , "Debug " + OrdemServico.Numero.ToString())
        
        Utils.LogError("Realizando requisição POST para " + urlPost.ToString() , "Debug " + OrdemServico.Numero.ToString())
        
        #Fazendo a requisição POST para autenticação
        response = client.PostAsync(urlPost, content).Result
        
        #Verificando se a resposta é bem-sucedida
        if response.IsSuccessStatusCode:
            # Lendo o conteúdo da resposta
            result = response.Content.ReadAsStringAsync().Result
            Utils.LogError("Autenticação bem-sucedida " + urlPost.ToString() , "Debug " + OrdemServico.Numero.ToString())
            jsonResult = JObject.Parse(result)  #Converte a resposta em JSON
            return jsonResult['access_token'].ToString()
        else:
            Utils.LogError("Erro na autenticação. Código de status: " + response.StatusCode.ToString() + " Detalhes: " + response.Content.ReadAsStringAsync().Result + " URL: " + urlPost.ToString() , "Erro " + OrdemServico.Numero.ToString())
            return ("{\"isSuccess\": false,\"errors\": Erro na autenticação. Código de status: " + response.StatusCode.ToString() + " Detalhes: " + response.Content.ReadAsStringAsync().Result + " URL: " + urlPost.ToString() + ",\"data\": 0}")
    except Exception as e:
    
        Utils.LogError("Erro ao autenticar no Projurid: "+ e.Message + " URL: " + urlPost.ToString(), "Erro " + OrdemServico.Numero.ToString());
        return ("{\"isSuccess\": false,\"errors\": Erro ao autenticar no Projurid: " + e.Message.ToString() + ",\"data\": 0}")
        
def remove_aspas_dupla(input_string):
    return input_string.replace('"', '')
        
def formatar_data(data_str):
    if data_str:
        try:
            # Tenta primeiro o formato com hora
            dt = datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
        except ValueError:
            # Caso falhe, tenta o formato sem hora
            dt = datetime.strptime(data_str, "%d/%m/%Y")
        return dt.strftime("%Y-%m-%dT%H:%M:%S") + ".0000000-03:00"  # Ajuste o fuso horário conforme necessário
    return ""

def processar_anexo(anexo, tipo_documento):
    ## Determina os valores de depósito e custas a partir das guias
    repositorio =  Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM")
    if anexo:
        try:
            local_arquivo = anexo.Localizacao.ToString()
            arquivo = repositorio + "\\" + local_arquivo
            nome_arquivo = anexo.Descricao.ToString()
            nome_documento = nome_arquivo.Split(".")[0]
     
            if File.Exists(arquivo):
                with StreamReader(arquivo, Encoding.Default) as sr:
                    as_string = sr.ReadToEnd()
                bytes = Encoding.Default.GetBytes(as_string)
                conteudo_base64 = Convert.ToBase64String(bytes)
                #conteudo_base64 = "arquivobase64"
                documento = ("{"+ "\"nomeArquivo\": \"" + nome_arquivo + "\", "+ "\"nomeDocumento\": \"" + nome_documento + "\", "+ "\"tipoDocumento\": \"" + tipo_documento + "\", "+ "\"conteudo\": \"" + conteudo_base64 + "\""+ "}, ")
                return documento
            else:
                Utils.LogError("Arquivo não encontrado: "+ arquivo.ToString(), "Erro " + OrdemServico.Numero.ToString())
                return ("{\"isSuccess\": false,\"errors\": Arquivo não encontrado: " + arquivo.ToString() + ",\"data\": 0}")            
        except Exception as e: 
            Utils.LogError("Erro ao processar anexo "+ anexo.Descricao.ToString(), "Erro " + OrdemServico.Numero.ToString())
            
    return ("{\"isSuccess\": false,\"errors\": Erro ao processar anexo " + anexo.Descricao.ToString() + ",\"data\": 0}")   
    
def IncluiDeposito():
    #{
    #  "codDossie": "string",
    #  "numProcesso": "string",
    #  "naturezaDeposito": "string",
    #  "dataDeposito": "string",
    #  "dataVencimento": "string",
    #  "valorDeposito": 0,
    #  "naturezaCustas": "string",
    #  "dataVencimentoCustas": "string",
    #  "dataPagamentoCustas": "string",
    #  "valorCustas": 0,
    #  "observacao": "string",
    #  "numeroDocumento": "string",
    #  "abrevBanco": "string",
    #  "contaJudicial": "string",
    #  "documentos": [
    #    {
    #      "nomeArquivo": "string",
    #      "nomeDocumento": "string",
    #      "tipoDocumento": "string",
    #      "conteudo": "string"
    #    }
    #  ]
    #}
    try:
    
        SQLVersao = "SELECT dp.versao FROM OCORRENCIA o inner join DESENHO_PROCESSO dp on o.ID_DESENHO_PROCESSO = dp.ID_DESENHO_PROCESSO where o.numero = '" + OrdemServico.Numero.ToString() + "'"
        versao = Utils.ExecuteScalar(SQLVersao)
        
        ## Obtenção dos valores do formulário
        cod_raw = OrdemServico.GetCustom("CODIGO_BBTS")

        codDossie = None

        if cod_raw:
            # Remove espaços no início, fim e entre caracteres
            cod_normalizado = re.sub(r'\s+', '', cod_raw)

            # Regex: exatamente CBR- + 4 ou mais dígitos
            pattern = r'^CBR-(?!0+$|123$)\d{4,}$'

            if re.match(pattern, cod_normalizado):
                codDossie = cod_normalizado #"CBR-1956" 
            else:
                return ("{\"isSuccess\": false,\"errors\": O código do dossiê: " + codDossie.ToString() + ", é inválido. Não deve conter espaços e deve seguir o padrão CBR-1234.' \"data\": 0}")
        
        numProcesso = OrdemServico.GetCustom("PROCESSO_MEMORANDO")
        
        if versao <= 9:
            numeroDocumento = " "
        else:
            numeroDocumento = OrdemServico.GetCustom("NUM_DOCU")
            
        #naturezaDeposito = OrdemServico.GetCustom("ASSUNTOMEMORANDO")
        listaGrid = OrdemServico.GetCustom("GUIASJUDICIAIS")
        
        if not codDossie or not numProcesso:
            Utils.LogError("Dados essenciais do processo estão faltando " , "Erro " + OrdemServico.Numero.ToString())
            return ("{\"isSuccess\": false,\"errors\": Dados essenciais do processo estão faltando: Dossiê e Número do Processo,\"data\": 0}")
            
        if not codDossie.startswith("CBR-"):
            Utils.LogError("Erro no prefixo do Dossiê " , "Erro " + OrdemServico.Numero.ToString())
            return ("{\"isSuccess\": false,\"errors\": O código do dossiê: " + codDossie.ToString() + ", não possui o prefixo 'CBR-' \"data\": 0}")
            
        #Inicializar valiáveis
        json = ""
        naturezaDeposito = ""
        dataDeposito = ""
        dataVencimento = ""
        valorDeposito = 0
        valDeposito = 0
        naturezaCustas = ""
        dataPagamentoCustas = ""
        dataVencimentoCustas = ""
        valorCustas = 0
        valCustas = 0
        tipoDocumento = ""

        documentos = "["
        
        # Determina os valores de depósito e custas a partir das guias
        for linha in listaGrid.Rows:
            try:
                anexoGuia = None
                anexoPgto = None

                if linha["CUSTASDEPOSITO"] == "Depósito":
                    naturezaDeposito = linha["NATUREZA"]
                    dataDeposito = linha["DATA_PAGAMENTO"].ToString("yyyy-MM-dd")
                    dataVencimento = linha["PRAZO_FATAL"].ToString("yyyy-MM-dd")
                    valDeposito = linha["VALOR"]
                    tipoDocumento = linha["TIPO_DOCUMENTO"]
                    
                    if not naturezaDeposito or not dataDeposito or not dataVencimento or not valDeposito or not tipoDocumento:
                        Utils.LogError("Dados essenciais da Guia de Depósito estão faltando " , "Erro " + OrdemServico.Numero.ToString())
                        return ("{\"isSuccess\": false,\"errors\": Dados essenciais da Guia de Depósito estão faltando: Natureza, Data vencimento, Data pagamento, valor ou Tipo pagamento do depósito,\"data\": 0}")
                    
                    if OrdemServico.PossuiItem("GUIASPAGAMENTO"):
                        anexoGuia = OrdemServico.ObtemItem("GUIASPAGAMENTO")
                        documentos += processar_anexo(anexoGuia, tipoDocumento)
                        
                    if OrdemServico.PossuiItem("COMPAG"):
                        anexoPgto = OrdemServico.ObtemItem("COMPAG")
                        documentos += processar_anexo(anexoPgto, tipoDocumento)  
                else:
                    naturezaCustas = linha["NATUREZA"]
                    dataPagamentoCustas = linha["DATA_PAGAMENTO"].ToString("yyyy-MM-dd")
                    dataVencimentoCustas = linha["PRAZO_FATAL"].ToString("yyyy-MM-dd")
                    valCustas = linha["VALOR"]
                    tipoDocumento = linha["TIPO_DOCUMENTO"]
                    
                    if not naturezaCustas or not dataPagamentoCustas or not dataVencimentoCustas or not valCustas or not tipoDocumento:
                        Utils.LogError("Dados essenciais da Guia de Custas estão faltando " , "Erro " + OrdemServico.Numero.ToString())
                        return ("{\"isSuccess\": false,\"errors\": Dados essenciais da Guia de Custas estão faltando: Natureza, Data vencimento, Data pagamento, valor ou Tipo pagamento do custas,\"data\": 0}")
                    
                    if OrdemServico.PossuiItem("GUIASCUSTAS"):
                        anexoGuia = OrdemServico.ObtemItem("GUIASCUSTAS")
                        documentos += processar_anexo(anexoGuia, tipoDocumento)
                        
                    if OrdemServico.PossuiItem("COMPAGCUSTAS"):
                        anexoPgto = OrdemServico.ObtemItem("COMPAGCUSTAS")
                        documentos += processar_anexo(anexoPgto, tipoDocumento)
                
                Utils.LogError("Documentos " + documentos.ToString(), "Debug " + OrdemServico.Numero.ToString())              

            
            except Exception as e:
                Utils.LogError("Erro ao processar linha de guia judicial: " + e.Message.ToString(), "Erro " + OrdemServico.Numero.ToString())
                return ("{\"isSuccess\": false,\"errors\": Erro ao processar linha de guia judicial: " + e.Message.ToString() + ",\"data\": 0}")

        caminho = Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM")
    
        AnexoEmail = Utils.ExecuteScalar("SELECT A.File_name FROM SV_MESSAGE_ATTACH A INNER JOIN SV_MESSAGE S ON A.ID = S.ID INNER JOIN OCORRENCIA O ON S.ID_OBJECT = O.ID_OCORRENCIA WHERE O.ID_OCORRENCIA = " + OrdemServico.Id.ToString() + " AND A.ID = (SELECT MAX(A2.ID) FROM SV_MESSAGE_ATTACH A2 INNER JOIN SV_MESSAGE S2 ON A2.ID = S2.ID INNER JOIN OCORRENCIA O2 ON S2.ID_OBJECT = O2.ID_OCORRENCIA WHERE O2.ID_OCORRENCIA = " + OrdemServico.Id.ToString() + " AND A2.FILE_NAME like '%\AnexosEmails%') AND A.FILE_NAME like '%\AnexosEmails%'")
        
        #Adiciona relatório de apoio Memorando nos arquivos do projurid
        arquivo = caminho + "\\" + AnexoEmail
        nome_arquivo = AnexoEmail.split('\\')[-1]
        nome_documento = nome_arquivo.Split(".")[0]
        tipo_documento = "DEPÓSITO RECURSAL/JUDICIAL"
        
        if File.Exists(arquivo):
            with StreamReader(arquivo, Encoding.Default) as sr:
                as_string = sr.ReadToEnd()
            bytes = Encoding.Default.GetBytes(as_string)
            conteudo_base64 = Convert.ToBase64String(bytes)
            #conteudo_base64 = "arquivobase64"
            documentos += ("{"+ "\"nomeArquivo\": \"" + nome_arquivo + "\", "+ "\"nomeDocumento\": \"" + nome_documento + "\", "+ "\"tipoDocumento\": \"" + tipo_documento + "\", "+ "\"conteudo\": \"" + conteudo_base64 + "\""+ "}, ")
            
        #OrdemServico.AdicionaComentario(documentos.ToString(), False)
        
        observacao = remove_aspas_dupla(OrdemServico.DescricaoDetalhada)
        abrevBanco = OrdemServico.GetCustom("COMBOBOX") 
        contaJudicial = OrdemServico.GetCustom("CCMEMORANDO")
        
        if not observacao or not abrevBanco or not contaJudicial:
            Utils.LogError("Dados essenciais do processo estão faltando " , "Erro " + OrdemServico.Numero.ToString())
            return ("{\"isSuccess\": false,\"errors\": Dados essenciais do processo estão faltando: Observação, Nome do Banco ou Conta Judicial,\"data\": 0}")
        
        # Limitando a 512 caracteres 
        if observacao.Length > 512:     
            observacao = observacao.Substring(0, 512)
        
        # Remove a última vírgula e espaço, e fecha o array
        documentos = documentos.rstrip(", ") + "]"
        
        # Substituindo a vírgula por ponto
        if valDeposito != 0 and valDeposito != None:
            valorDeposito = valDeposito.ToString().replace(",", ".")
        else:
            valorDeposito = valDeposito
  
        if valCustas != 0 and valCustas != None:
            valorCustas = valCustas.ToString().replace(",", ".")
        else:
            valorCustas = valCustas
            
     
        # Construção do JSON principal
        #Alteração número documento
        json = "{"+ "\"codDossie\": \"" + codDossie.ToString() + "\", "+ "\"numProcesso\": \"" + numProcesso.ToString() + "\", "+ "\"naturezaDeposito\": \"" + naturezaDeposito.ToString() + "\", "+ "\"dataDeposito\": \"" + dataDeposito.ToString() + "\", "+ "\"dataVencimento\": \"" + dataVencimento.ToString() + "\", "+ "\"valorDeposito\": " + valorDeposito.ToString() + ", " + "\"naturezaCustas\": \"" + naturezaCustas.ToString() + "\", "+ "\"dataVencimentoCustas\": \"" + dataVencimentoCustas.ToString() + "\", "+ "\"dataPagamentoCustas\": \"" + dataPagamentoCustas.ToString() + "\", "+ "\"valorCustas\": " + valorCustas.ToString() + ", " + "\"observacao\": \"" + observacao.ToString() + "\", " + "\"numeroDocumento\": \"" + numeroDocumento.ToString() + "\", "+ "\"abrevBanco\": \"" + abrevBanco.ToString() + "\", "+ "\"contaJudicial\": \"" + contaJudicial.ToString() + "\", "+ "\"documentos\": " + documentos.ToString() + "}"
        
        
        #json1 = "{"+ "\"codDossie\": \"" + codDossie.ToString() + "\", "+ "\"numProcesso\": \"" + numProcesso.ToString() + "\", "+ "\"naturezaDeposito\": \"" + naturezaDeposito.ToString() + "\", "+ "\"dataDeposito\": \"" + dataDeposito.ToString() + "\", "+ "\"dataVencimento\": \"" + dataVencimento.ToString() + "\", "+ "\"valorDeposito\": " + valorDeposito.ToString() + ", " + "\"naturezaCustas\": \"" + naturezaCustas.ToString() + "\", "+ "\"dataVencimentoCustas\": \"" + dataVencimentoCustas.ToString() + "\", "+ "\"dataPagamentoCustas\": \"" + dataPagamentoCustas.ToString() + "\", "+ "\"valorCustas\": " + valorCustas.ToString() + ", " + "\"observacao\": \"" + observacao.ToString() + "\", " + "\"numeroDocumento\": \"" + numeroDocumento.ToString() + "\", "+ "\"abrevBanco\": \"" + abrevBanco.ToString() + "\", "+ "\"contaJudicial\": \"" + contaJudicial.ToString() + "\", "+ "\"documentos\": "
        
        #Utils.LogError("Passa Json1" + json1.ToString() , "Debug " + OrdemServico.Numero.ToString())
        
        #Utils.LogError("Passa Json" , "Debug " + OrdemServico.Numero.ToString())
        
        #OrdemServico.AdicionaComentario(json.ToString(), False)
        #OrdemServico.Justificativa = json.ToString()
        #return json.ToString()
        
        # Autenticação e envio da requisição
        token = autenticaProjurid()
        
        if token is None:
            Utils.LogError("Erro ao obter token de autenticação. ", "Erro " + OrdemServico.Numero.ToString())
            return ("{\"isSuccess\": false,\"errors\": Erro ao obter token de autenticação.,\"data\": 0}")
            
        
        client = HttpClient()
        data = StringContent(json, Encoding.UTF8, "application/json")
        url2 = url + "financeiro/IncluiDeposito"
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

        response = client.PostAsync(url2, data).Result
        
        if response.IsSuccessStatusCode:
            #return response.Content.ReadAsStringAsync().Result
            result = response.Content.ReadAsStringAsync().Result
            return result
        else: 
            Utils.LogError("Json " + json.ToString() , "Debug " + OrdemServico.Numero.ToString())
            
            Utils.LogError("Erro na API 1: " + response.StatusCode.ToString() + " Detalhes: " + response.Content.ReadAsStringAsync().Result.ToString(), "Erro " + OrdemServico.Numero.ToString())        
        return result
    
    except Exception as e:
        Utils.LogError("Erro geral - Erro ao enviar JSON de guias judiciais: " + e.Message.ToString(), "Erro " + OrdemServico.Numero.ToString())
        return ("{\"isSuccess\": false,\"errors\": Erro geral - Erro ao enviar JSON de guias judiciais:  " + e.Message.ToString() + ",\"data\": 0}")
        
        
def pagJud(assuntoGuia):
    return assuntoGuia

def pagJudiciais(assuntoGuia, ccMemo, referencia, titulo, processo, reclamante, reclamada, descricao, divisao, dtVenc, pagExcep, guiasJudiciais):
    # Validação manual do JSON
    jsonResult = None
    if not guiasJudiciais:
        Utils.LogError("GuiasJudiciais está vazio! ", "Erro " + OrdemServico.Numero.ToString())
        return "GuiasJudiciais está vazio!"
    
    try:
        jsonResult = JObject.Parse(guiasJudiciais)
    except Exception as e:
        Utils.LogError("Erro ao processar JSON de guias judiciais: " + str(e.Message), "Erro " + OrdemServico.Numero.ToString())
        return "Erro ao processar JSON de guias judiciais: " + str(e.Message)
        

    # Validação de parâmetros essenciais para criar uma OS
    if not processo or not reclamante or not reclamada:
        Utils.LogError("Dados essenciais do processo estão faltando " , "Erro " + OrdemServico.Numero.ToString())
        return "Erro: Dados essenciais do processo estão faltando "
        
    # Verifica se a ordem de serviço pode ser criada
    login = '***MASCARADO***'
    assunto = "Projurid Solicitação de pagamento judicial"
    ordem_servico = OrdemServico.Carrega(20)
    servico = Servico.Carrega('Sigla', 'SOLPAGJUDAPP')
    pessoa = Pessoa.Carrega('UsuarioRede', login)
    pessoa_contratos = Pessoa.Carrega('UsuarioRede', 'fila.csc.-.Contratos')
    
    if not ordem_servico or not servico or not pessoa or not pessoa_contratos:
        Utils.LogError("Erro ao carregar parâmetros para criação da OS " , "Erro " + OrdemServico.Numero.ToString())
        return "Erro: Não foi possível carregar dados para criar a OS "
        
    os = OrdemServico.Nova(ordem_servico, 'APPSOLPAGJUD', 'INICIOPGT', assunto, servico, pessoa, pessoa_contratos)
    
    # Atribuindo valores aos campos da OS
    if assuntoGuia == "Honorarios Periciais":
        os["ASSUNTOMEMORANDO"] = "Honorários Periciais"
    elif assuntoGuia == "RO - Recurso Ordinario":
        os["ASSUNTOMEMORANDO"] = "RO - Recurso Ordinário"
    else:
        os["ASSUNTOMEMORANDO"] = assuntoGuia

    os["CCMEMORANDO"] = ccMemo
    os["DATA_MEMORANDO"] = referencia
    os["REF_MEMORANDO"] = titulo
    os["PROCESSO_MEMORANDO"] = processo
    os["RECLAMANTE_MEMORANDO"] = reclamante
    os["RECLAMADAS_MEMORANDO"] = reclamada
    os.DescricaoDetalhada = descricao
    os["DIVISAO_JURIDICA"] = divisao
    os["DATA_VENCIMENTO"] = dtVenc

    if pagExcep == 'Nao':
        os["SIM_NAO10"] = 'Não'
    else:
        os["SIM_NAO10"] = pagExcep

    Utils.LogInformation(os.Numero.ToString(), "OS")
    
    # Valida se existem guias para processar
    if not jsonResult or not jsonResult["guias"]:
        Utils.LogError("Não há guias judiciais para processar " , "Erro " + OrdemServico.Numero.ToString())
        return "Erro: Não há guias judiciais para processar "
        

    # Processamento das guias judiciais
    for linha in jsonResult["guias"]:
        info = linha["custaDep"].ToString() if "custaDep" in linha else None
        valor = linha["valor"].ToString() if "valor" in linha else None
        data = linha["prazo"].ToString() if "prazo" in linha else None

        if info and valor and data:
            if info == "Deposito":
                custaDep = "Depósito"
            else:
                custaDep = info
                
            os.AdicionaLinhaRegistro("GUIASJUDICIAIS", ["CUSTASDEPOSITO", "VALOR", "PRAZO_FATAL"], [custaDep, valor, data])
            Utils.LogInformation(custaDep + " - " + valor + " - " + data, "Guias")
        else:
            Utils.LogError("Dados incompletos na linha da guia judicial " , "Erro " + OrdemServico.Numero.ToString())
            return "Erro: Dados incompletos na linha da guia judicial "
        

    # Tenta avançar a OS e salvar
    if os.Numero:
        os.AvancaAtividade()
        os.Salva()
        return os.Numero.ToString()
    else:
        Utils.LogError("Erro ao avançar ou salvar a OS " , "Erro " + OrdemServico.Numero.ToString())
        return "Erro: Erro ao avançar ou salvar a OS "
