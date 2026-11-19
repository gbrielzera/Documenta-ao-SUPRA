# apiSuprimentosCompras
# Caminho: Catálogo > Biblioteca de scripts > apiSuprimentosCompras
# Fonte: Reembolsos__I.A_Versão_1_Reembolso_-_Iniciativa_IA.xml

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

sql="select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)

if dom == 'DESENVOLVIMENTO': 
    prefixoCaminho = "\\\\santacruz0.cobra.com.br\\supravizio$\\"

if dom == 'HOMOLOGAÇÃO':    
    prefixoCaminho = "\\\\santacruz1.cobra.com.br\\supravizio$\\"

if dom == 'PRODUÇÃO':    
    prefixoCaminho = "\\\\santacruz.cobra.com.br\\supravizio$\\"
    
#Utils.LogInformation(dom.ToString()+" , "+prefixoCaminho.ToString(), "DEBUG")

def buscaDadosCadastroFornecedor(nOS):

    arquivos = []
    tipoFornecedor = ""

    try:
    
        sql = "SELECT CPE_CSC.TIPO_FORNECEDOR FROM OCORRENCIA LEFT JOIN CPE_CSC ON CPE_CSC.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA WHERE NUMERO ='"+nOS.ToString() +"'"
    
        result_table = DB.ExecuteDataTable(sql)

        if result_table.Rows.Count > 0:

            tipoFornecedor = result_table.Rows[0]["TIPO_FORNECEDOR"].ToString()
        else:
            return (
                "{\"status\": \"erro\", "
                "\"mensagem\": \"Não foi possível localizar a OS apartir do numero informado.\", "
                "}"
            )    

        os = OrdemServico.Carrega('Numero',nOS.ToString())

        for arq in os.ItensAnexados:

            try:
               nomeArqAnex = arq.ItemConfiguracao.Descricao.ToString()
               caminhoArqAnex = arq.ItemConfiguracao.Localizacao.ToString()
               caminho_arquivo = (prefixoCaminho +caminhoArqAnex)
               conteudoBytes = File.ReadAllBytes(caminho_arquivo)
               conteudoBase64 = Convert.ToBase64String(conteudoBytes)

               arquivos.append({"nomeArquivo": nomeArqAnex,"situacao":"LOCALIZADO","conteudoBase64": conteudoBase64})

            except Exception as e:
                
                arquivos.append({"nomeArquivo": nomeArqAnex,"situacao": "NAO_LOCALIZADO",
                "mensagem": "Arquivo não localizado no repositório. Entre em contato com o administrador do sistema.",
                "localizacao": caminhoArqAnex})
                Utils.LogInformation("Erro ao processar arquivo: " + str(e),"DEBUG")

        retorno = {
            "status": "sucesso",
            "mensagem": "Consulta realizada com sucesso",
            "tipoFornecedor": tipoFornecedor,
            "arquivos": arquivos
        }

        return JsonConvert.SerializeObject(retorno)
    except Exception as e:
        return (
            "{\"status\": \"erro\", "
            "\"mensagem\": \"Não foi possível realizar a consulta.\", "
            "\"detalhes\": [" + e + "]"
            "}"
        )
        
def buscaDadosCheckListCompras(nOS):

    arquivos = []
    tipoOcCSC = ""
    fornecedor2 = ""
    numeroDeOc = ""
    numeroOCVincMaster2 = ""
    numero1 = ""
    valorF1 = ""
    ModalidadeLicitacao = ""  
  
    try:
        sql = "SELECT CSC.TIPO_OC_CSC, CSC.FORNECEDOR2, CT.NUMERO_DE_OC, CT.NUMERO_OC_VINCULADA_MASTER2, CT.NUMERO_1, CT2.VALORF1, OS.MODALIDADE_LICITACAO FROM OCORRENCIA OC LEFT JOIN CPE_CSC CSC ON CSC.ID_OCORRENCIA = OC.ID_OCORRENCIA LEFT JOIN CPE_CONTRATOS CT ON CT.ID_OCORRENCIA = OC.ID_OCORRENCIA LEFT JOIN CPE_CONTRATOS02 CT2 ON CT2.ID_OCORRENCIA = OC.ID_OCORRENCIA LEFT JOIN CP_ORDEM_SERVICO OS ON OS.ID_OCORRENCIA = OC.ID_OCORRENCIA WHERE NUMERO ='"+nOS.ToString() +"'"
    
        result_table = DB.ExecuteDataTable(sql)
      
        if result_table.Rows.Count > 0:

            tipoOcCSC = result_table.Rows[0]["TIPO_OC_CSC"].ToString()
            fornecedor2 = result_table.Rows[0]["FORNECEDOR2"].ToString()
            numeroDeOc = result_table.Rows[0]["NUMERO_DE_OC"].ToString()
            numeroOCVincMaster2 = result_table.Rows[0]["NUMERO_OC_VINCULADA_MASTER2"].ToString()
            numero1 = result_table.Rows[0]["NUMERO_1"].ToString()
            valorF1 = result_table.Rows[0]["VALORF1"].ToString()
            ModalidadeLicitacao = result_table.Rows[0]["MODALIDADE_LICITACAO"].ToString()

        else:
            return (
                "{\"status\": \"erro\", "
                "\"mensagem\": \"Não foi possível localizar a OS apartir do numero informado.\", "
                "}"
            )
        
        os = OrdemServico.Carrega('Numero',nOS.ToString())

        for arq in os.ItensAnexados:

            try:
               nomeArqAnex = arq.ItemConfiguracao.Descricao.ToString()
               caminhoArqAnex = arq.ItemConfiguracao.Localizacao.ToString()
               caminho_arquivo = ("\\\\santacruz0.cobra.com.br\\supravizio$\\" +caminhoArqAnex)
               conteudoBytes = File.ReadAllBytes(caminho_arquivo)
               conteudoBase64 = Convert.ToBase64String(conteudoBytes)

               arquivos.append({"nomeArquivo": nomeArqAnex,"situacao":"LOCALIZADO","conteudoBase64": conteudoBase64})

            except Exception as e:
                
                arquivos.append({"nomeArquivo": nomeArqAnex,"situacao": "NAO_LOCALIZADO",
                "mensagem": "Arquivo não localizado no repositório. Entre em contato com o administrador do sistema.",
                "localizacao": caminhoArqAnex})
                Utils.LogInformation("Erro ao processar arquivo: " + str(e),"DEBUG")
        
        retorno = {
            "status": "sucesso",
            "mensagem": "Consulta realizada com sucesso",
            "tipoOcCSC": tipoOcCSC,
            "fornecedor2": fornecedor2,
            "numeroDeOc": numeroDeOc,
            "numeroOCVincMaster2": numeroOCVincMaster2,
            "numero1": numero1,
            "valorF1": valorF1,
            "ModalidadeLicitacao": ModalidadeLicitacao,
            "arquivos": arquivos
        }
    
        
        
        return JsonConvert.SerializeObject(retorno)
    
    except Exception as e:
        return (
            "{\"status\": \"erro\", "
            "\"mensagem\": \"Não foi possível realizar a consulta.\", "
            "\"detalhes\": [" + str(e) + "]"
            "}"
        )
