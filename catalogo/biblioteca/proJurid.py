# proJurid
# Caminho: Catálogo > Biblioteca de scripts > proJurid
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

import clr
import time
from System import *
from System import String
#from System.Xml import XmlDocument
clr.AddReference("Supravizio.Custom")
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System.Data")
from Venki.Supravizio.Processo.Custom import OrdemServico
from Venki.Supravizio.Processo.Custom import Servico
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Recurso.Custom import Tecnico
from System.Text import StringBuilder

from System import Convert, TimeSpan
from System.Data import DataSet

from System.IO import *
from System.Text import *
 
def testeprojurid():
    ## Obtenção dos valores do formulário 
    codDossie = "Campo a definir"
    numProcesso = OrdemServico.GetCustom("PROCESSO_MEMORANDO")
    naturezaDeposito = OrdemServico.GetCustom("ASSUNTOMEMORANDO")
    listaGrid = OrdemServico.GetCustom("GUIASJUDICIAIS")
    
    ## Determina os valores de depósito e custas a partir das guias
    for linha in listaGrid.Rows:
        if linha["CUSTASDEPOSITO"] == "Depósito":
            dataDeposito = ""
            #dataDeposito = linha["DATA_PAGAMENTO"]
            dataVencimento = linha["PRAZO_FATAL"]
            valorDeposito = linha["VALOR"]
        else:
            naturezaCustas = linha["CUSTASDEPOSITO"]
            dataPagamentoCustas = ""
            #dataPagamentoCustas = linha["DATA_PAGAMENTO"]
            dataVencimentoCustas = linha["PRAZO_FATAL"]
            valorCustas = linha["VALOR"]
    
    observacao = OrdemServico.GetCustom("DESCRICAO_DETALHADA")
    abrevBanco = "Campo a definir"
    contaJudicial = OrdemServico.GetCustom("CCMEMORANDO")
    
    ## Array de documentos anexados
    documentos = "["
    for anexo in OrdemServico.ItensAnexados:
    
        nomeArquivo = anexo.ItemConfiguracao.Descricao.ToString()
        localArquivo =anexo.ItemConfiguracao.Localizacao.ToString()
        repositorio = Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM")
        arquivo = repositorio + "\\" + localArquivo
        
        tipoDocumento = nomeArquivo.Split(".")[-1]
        
        nomeDocumento = nomeArquivo.Split(".")[0]

        
        #OrdemServico.AdicionaComentario(arquivo.ToString(),False)
        
        if arquivo.Length > 0:
            sr = StreamReader(arquivo, Encoding.Default)
            AsString = sr.ReadToEnd();
            bytes = Encoding.Default.GetBytes(AsString)
          
            #conteudoBase64 = Convert.ToBase64String(bytes)
            conteudoBase64 = "conteudoBase64"
            
            # Concatena cada documento ao array JSON
            documentos += ("{"+ "\"nomeArquivo\": \"" + nomeArquivo.ToString() + "\", "+ "\"nomeDocumento\": \"" + nomeDocumento.ToString() + "\", "+ "\"tipoDocumento\": \"" + tipoDocumento.ToString() + "\", "+ "\"conteudo\": \"" + conteudoBase64.ToString() + "\""+ "}, ")
    
    # Remove a última vírgula e espaço, e fecha o array
    documentos = documentos.rstrip(", ") + "]"
 
    # Construção do JSON principal
    json = "{"+ "\"codDossie\": \"" + codDossie.ToString() + "\", "+ "\"numProcesso\": \"" + numProcesso.ToString() + "\", "+ "\"naturezaDeposito\": \"" + naturezaDeposito.ToString() + "\", "+ "\"dataDeposito\": \"" + dataDeposito.ToString() + "\", "+ "\"dataVencimento\": \"" + dataVencimento.ToString() + "\", "+ "\"valorDeposito\": " + valorDeposito.ToString() + ", "+ "\"observacao\": \"" + observacao.ToString() + "\", "+ "\"abrevBanco\": \"" + abrevBanco.ToString() + "\", "+ "\"contaJudicial\": \"" + contaJudicial.ToString() + "\", "+ "\"documentos\": " + documentos.ToString() + "}"
    
    return json.ToString()
    
def processarXml(xmlString):
    # Carregar o XML da requisição
    doc = XmlDocument()
    doc.LoadXml(xmlString)
    
    # Extrair os valores do XML
    assuntoGuia = doc.SelectSingleNode("//assuntoGuia").InnerText
    comCopia = doc.SelectSingleNode("//comCopia").InnerText
    referencia = doc.SelectSingleNode("//referencia").InnerText
    titulo = doc.SelectSingleNode("//titulo").InnerText
    processo = doc.SelectSingleNode("//processo").InnerText
    reclamante = doc.SelectSingleNode("//reclamante").InnerText
    reclamada = doc.SelectSingleNode("//reclamada").InnerText
    descricao = doc.SelectSingleNode("//descricao").InnerText
    divisao = doc.SelectSingleNode("//divisao").InnerText
    dtVenc = doc.SelectSingleNode("//dtVenc").InnerText
    pagExcep = doc.SelectSingleNode("//pagExcep").InnerText
    
    # Extraindo o array de guiasJudiciais
    guiasJudiciaisNode = doc.SelectNodes("//guia")
    guiasJudiciais = []
    for guia in guiasJudiciaisNode:
        custaDep = guia.SelectSingleNode("CustaDep").InnerText
        valor = guia.SelectSingleNode("valor").InnerText
        prazo = guia.SelectSingleNode("prazo").InnerText
        guiasJudiciais.append({
            "CustaDep": custaDep,
            "valor": valor,
            "prazo": prazo
        })
    
    login = doc.SelectSingleNode("//login").InnerText
    
    # Chama a função pagJudiciais com os dados extraídos
    resultado = pagJudiciais(assuntoGuia, comCopia, referencia, titulo, processo, reclamante, reclamada, descricao, divisao, dtVenc, pagExcep, guiasJudiciais, login)
    return resultado

def pagJudiciais(assuntoGuia, comCopia, referencia, titulo, processo, reclamante, reclamada, descricao, divisao, dtVenc, pagExcep, guiasJudiciais, login):
    # Aqui você pode tratar os dados da forma que sua aplicação precisa
    #resultado = f"Processando: {assuntoGuia}, {comCopia}, {referencia}, {titulo}, {processo}, {reclamante}, {reclamada}, {descricao}, {divisao}, {dtVenc}, {pagExcep}, {guiasJudiciais}, {login}"
    
    resultado = assuntoGuia + comCopia + referencia + titulo + processo + reclamante + reclamada + descricao + divisao + dtVenc +  pagExcep + guiasJudiciais + login
    return resultado
