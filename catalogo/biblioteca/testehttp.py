# testehttp
# Caminho: Catálogo > Biblioteca de scripts > testehttp
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

import clr
import System

clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("Supravizio.Custom")
clr.AddReference("System.Data")

clr.AddReference("System.Data")
from System.Data import DataSet 
clr.AddReference("Newtonsoft.Json")
from Newtonsoft.Json import * 
from System.Text import StringBuilder
from System.Web import *

from Venki.Supravizio.Processo.Custom import OrdemServico
from Venki.Supravizio.Processo.Custom import Servico
from Venki.Supravizio.Recurso.Custom import Pessoa


from Newtonsoft.Json import JsonConvert
from Newtonsoft.Json.Linq import JArray, JValue




import clr
from System import Convert, TimeSpan
from System.Text import StringBuilder
from System.Data import DataSet
from System.Net.Http import HttpClient
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue


        
def TesteAberturaChamado():
    # Token de autenticação
    token = '***MASCARADO***'

    # URL da API
    url = 'https://sisccon.bbts.com.br/supravizio/supra/lista-designacao-fornecedor'

    # Inicializa o HttpClient e configura os cabeçalhos
    client = HttpClient()
    client.Timeout = TimeSpan.FromSeconds(60)
    client.DefaultRequestHeaders.Accept.Clear()
    client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
    client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        
        
        
    # Envia a requisição GET
    response = client.GetAsync(url)
    response.Wait()
    
    try:
        # Verifica o código de status da resposta
        if response.Result.IsSuccessStatusCode:
            # Lê o conteúdo da resposta
            resultAsync = response.Result.Content.ReadAsStringAsync()
            resultAsync.Wait()
            result = resultAsync.Result

            # Adiciona um comentário com o JSON bruto para depuração
            # OrdemServico.AdicionaComentario("JSON bruto: {0}".format(result), True)

            try:
                # Verifica se o JSON é uma string encapsulada e tenta deserializar
                if result.startswith("\"") and result.endswith("\""):
                    # Remove as aspas extras
                    result = JsonConvert.DeserializeObject(result)
                
                # Tenta deserializar o JSON como um array
                jsonArray = JArray.Parse(result)

                # Itera sobre os objetos na lista
                contador = 0
                for i, item in enumerate(jsonArray):
                    dgco = item["dgco"]
                    nomeTitular = item["titular"]
                    matriculaTitular = item["matricula_titular"]
                    nomeSuplente = item["suplente"]
                    matriculaSuplente = item["matricula_suplente"]
                    tipoDesignacao = item["tipo_designacao"]
                    dataDesignacao = item["dt_designacao"]
                    status = item["status"]
                    idContrato = item["id_contrato"]
                    uorTitular = item["uor_titular"]
                    uorSuplente = item["uor_suplente"]
                    objeto = item["objeto"]
                    dataInicioVigencia = item["dt_inicio_vigencia"]
                    diasVigentes = item["dias_desde_inicio"]
                    fornecedor = item["nome_fornecedor"]
                    
                    
                    if (diasVigentes > 60) and (tipoDesignacao == 'FISCALIZACAO_ADMINISTRATIVA' or tipoDesignacao == 'FISCALIZACAO_SERVICO'):
                        result_pessoa = DB.ExecuteDataTable("Select PESSOA.ID_PESSOA, PESSOA.NOME, CP_PESSOA.MATRICULA From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Where CP_PESSOA.MATRICULA = '"+matriculaTitular.ToString()+"'")
                    
                        idPessoa = 0
                        
                        for row in result_pessoa.Rows:
                            idPessoa =  row["ID_PESSOA"]
                    
                        
                            
                        
                            
                            
                        novaOS = OrdemServico.Nova("AVALIAFISCASERVICOOO","TESTECODIGOINICIO","Avaliação Fiscal Serviço Aberto Por: ",Servico.Carrega(974),Pessoa.Carrega(3536),Pessoa.Carrega(Convert.ToInt32(idPessoa)))
                        novaOS.Assunto =  "Avaliação Fiscal Serviço Aberto Por: " + str(nomeTitular)
                        novaOS.Salva()
                        numeroOs = novaOS.Numero.ToString()
                        
                        contador = contador + 1
                        result_table2 = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.ID_OCORRENCIA From OCORRENCIA Where OCORRENCIA.NUMERO = '"+numeroOs+"'")
                        
                        

                        
                        
                        for row in result_table2.Rows:
                            os = OrdemServico.Carrega(Convert.ToInt32(row["ID_OCORRENCIA"]))
                            
                            if os != None:
                                os.SetCustom("CSC_DGCO", dgco)
                                os.SetCustom("CSC_OBS", objeto)
                                os.SetCustom("NOME_FORNECEDOR", fornecedor)
                                os.SetCustom("RUBRICA", dataInicioVigencia)
                                os.SetCustom("COLABORADOR", nomeTitular)
                                

                                # OrdemServico.AdicionaComentario("Alterado o valor de CSC_DGCO para {0} no chamado de OS: {1} de tipo {2}".format(dgco.ToString(), os.Numero.ToString(), tipoDesignacao), True)
                                os.Salva()
                                
                                
            
                        
                        
                    if contador == 1:
                        # Retorna um indicador de sucesso que não seja uma string
                        return True

                    # Se não houver 'contador == 1', você pode optar por retornar None ou um objeto vazio, dependendo do contexto
                    # return None

                    # Se não houver retorno explícito dentro do bloco do 'for', pode-se adicionar um retorno no final da função
                    return None
            except Exception as e:
                # Adiciona um comentário com o erro de extração
                return "Erro de extração: {0}".format(str(e))
        else:
            # Em caso de erro, adiciona o comentário com o código de erro
            return "Erro: {0}".format(response.Result.StatusCode)

    except Exception as e:
        # Adiciona um comentário com o erro genérico
        return "Erro de execução: {0}".format(str(e))
