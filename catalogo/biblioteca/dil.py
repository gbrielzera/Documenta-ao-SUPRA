# dil
# Caminho: Catálogo > Biblioteca de scripts > dil
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

import clr
import System
clr.AddReference("System.Data")
from System.Data import DataSet 
clr.AddReference("Newtonsoft.Json")
from Newtonsoft.Json import * 
from System.Text import StringBuilder
from System.Web import *

from Venki.Supravizio.Processo.Custom import OrdemServico
from Venki.Supravizio.Processo.Custom import Servico
from Venki.Supravizio.Recurso.Custom import Pessoa
        
        
def buscarDadosChamadao(numeroOs):
    try:
        projetos = [];
        
        # ExecuteReader retorna um conjunto de resultados 
        result_table2 = DB.ExecuteDataTable("Select OCORRENCIA.ID_CLASSE_SUB_PROC, OCORRENCIA.NUMERO, OCORRENCIA.ASSUNTO, OCORRENCIA.DATA_HORA_SOL, PESSOA.NOME As SOLICITANTE, CPE_ORDEM_SERVICO.SIM_NAO_PROC As PUBLICADO_DOU, CPE_ORDEM_SERVICO.SIM_NAO_INFRA As PUBLICADO_BBTS, CPE_CSC.SIM_NAO7 As PUBLICADO_SIASG From OCORRENCIA Inner Join PESSOA On OCORRENCIA.ID_CLIENTE = PESSOA.ID_PESSOA Inner Join CPE_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CPE_ORDEM_SERVICO.ID_OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Where OCORRENCIA.ID_CLASSE_SUB_PROC = 344 And OCORRENCIA.NUMERO = " + numeroOs)
        
        
        
        
        for row in result_table2.Rows:
            projeto = {
                "numero": row["NUMERO"],
                "assunto": row["ASSUNTO"],
                "dataHoraSolicitacao": row["DATA_HORA_SOL"],
                "publicadoDou": row["PUBLICADO_DOU"],
                "publicadoBbts": row["PUBLICADO_BBTS"],
                "publicadoSiasg": row["PUBLICADO_SIASG"]
            }
            
        projetos.append(projeto)
        
        
        # Verificar se a lista de projetos está vazia
        if len(projetos) == 0:
            return "Nenhuma solicitação encontrada."

        # Serializar a lista de projetos para JSON
        json_data = JsonConvert.SerializeObject(projetos)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
        
        
        
        
def buscarDetalhesReservaDgco(numeroOs):
    try:
        result_table2 = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, OCORRENCIA.DATA_HORA_SOL, ORDEM_SERVICO.DESCRICAO_DETALHADA, OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ID_CLASSE_SUB_PROC_INI From OCORRENCIA Inner Join ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = ORDEM_SERVICO.ID_OCORRENCIA Inner Join CPE_FINANCEIRO On OCORRENCIA.ID_OCORRENCIA = CPE_FINANCEIRO.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = OCORRENCIA.ID_RESPONSAVEL Where OCORRENCIA.ID_CLASSE_SUB_PROC_INI = 1122 And OCORRENCIA.NUMERO = '"+str(numeroOs)+"'")
        
        json_data = JsonConvert.SerializeObject(result_table2)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
