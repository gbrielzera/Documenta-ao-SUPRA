# apiPost
# Caminho: Catálogo > Biblioteca de scripts > apiPost
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
from Newtonsoft.Json import *
from Newtonsoft.Json.Linq import *
from System.Net.Http import *
from System.Net.Http.Headers import *
from System.Text import *


urlPost = 'http://127.0.0.1:5000/apiPost'
client = HttpClient()
#authToken = Encoding.UTF8.GetBytes("user:pass")
#client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Basic", Convert.ToBase64String(authToken))
#
payload = {
    "assuntoGuia": "Assunto da Guia",
    "comCopia": "email@example.com",
    "referencia": "123456",
    "titulo": "Título do Documento",
    "processo": "123456789",
    "reclamante": "Nome do Reclamante",
    "reclamada": "Nome da Reclamada",
    "descricao": "Descrição do processo ou da solicitação",
    "divisao": "Divisão responsável",
    "dtVenc": "2024-12-31",
    "pagExcep": "Exceção de Pagamento",
    "guiasJudiciais": [
        {
            "CustaDep": "Depósito Judicial",
            "valor": 1000.50,
            "prazo": "2024-12-31"
        },
        {
            "CustaDep": "Depósito Judicial 2",
            "valor": 500.00,
            "prazo": "2024-11-30"
        }
    ],
    "login": "usuario123"
}

# Serialize payload to JSON
jsonPayload = JsonConvert.SerializeObject(payload)
content = StringContent(jsonPayload, Encoding.UTF8, "application/json")

# Enviar a requisição POST
response = client.PostAsync(urlPost, content).Result
result = response.Content.ReadAsStringAsync().Result  # string dos dados

#OrdemServico.AdicionaComentario(result.ToString(), False)


jsonResult = JObject.Parse(result)


    # Processando o JSON para extrair informações dos campo

    OrdemServico["ASSUNTOMEMORANDO"] = jsonResult["assuntoGuia"].ToString()
    OrdemServico["CCMEMORANDO"] = jsonResult["comCopia"].ToString()
    OrdemServico["REF_MEMORANDO"] = jsonResult["referencia"].ToString()
    OrdemServico["PROCESSO_MEMORANDO"] = jsonResult["processo"].ToString()
    OrdemServico["RECLAMANTE_MEMORANDO"] = jsonResult["reclamante"].ToString()
    OrdemServico["RECLAMADAS_MEMORANDO"] = jsonResult["reclamada"].ToString()
    OrdemServico["Descrição detalhada"] = jsonResult["descricao"].ToString()
    OrdemServico["DIVISAO_JURIDICA"] = jsonResult["divisao"].ToString()
    OrdemServico["DATA_VENCIMENTO"] = jsonResult["dtVenc"].ToString()
    OrdemServico["SIM_NAO10"] = jsonResult["pagExcep"].ToString()
    
    # Inicializando ordem de serviço
    login = '***MASCARADO***'
    assunto = "Projurid Solicitação de pagamento judicial"
    os = OrdemServico.Nova(OrdemServico.Carrega(20),'APPPAGJUDICIAL', 'INICIOPGT', assunto , Servico.Carrega('Sigla','APPPGTJUDICIAL'), Pessoa.Carrega('UsuarioRede',login) , Pessoa.Carrega ('UsuarioRede','fila.csc.-.Contratos'))
    os["ASSUNTOMEMORANDO"] = assuntoGuia
    
    
    os.AvancaAtividade()
    os.Salva()
    return os.Numero.ToString()

   # Adicionando um comentário com o resultado (ajustar conforme a necessidade)
    #OrdemServico.AdicionaComentario(result.ToString(), False)

    # Iterando sobre uma lista no JSON e adicionando registros
    for linha in jsonResult["guiasJudiciais"]:    
        OrdemServico.AdicionaLinhaRegistro("GUIASJUDICIAIS", ["CUSTASDEPOSITO", "VALOR", "PRAZO_FATAL"], [linha["CustaDep"], linha["valor"], linha["prazo"]])

    return jsonResult  # Se precisar retornar o resultado processado
