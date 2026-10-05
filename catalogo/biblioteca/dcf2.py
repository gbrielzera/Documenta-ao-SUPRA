# dcf2
# Caminho: Catálogo > Biblioteca de scripts > dcf2
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("Supravizio.Custom")
clr.AddReference("System.Data")

from System import Convert, TimeSpan
from System.Text import StringBuilder
from System.Data import DataSet
from System.Net.Http import HttpClient
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

from Newtonsoft.Json import JsonConvert
from Newtonsoft.Json.Linq import JArray, JValue

from Venki.Supravizio.Processo.Custom import OrdemServico
from Venki.Supravizio.Processo.Custom import Servico
from Venki.Supravizio.Recurso.Custom import Pessoa


def dispararChamadosAvaliacao():
    
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
                    
                        
                            
                        
                            
                            
                        novaOS = OrdemServico.Nova("AVALIAFISCASERVICOOO","TESTECODIGOINICIO","Avaliação Fiscal Serviço Aberto Por: ", Servico.Carrega(974),Pessoa.Carrega(3536),Pessoa.Carrega(Convert.ToInt32(idPessoa)))
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
                        return True  # Por exemplo, retorna um booleano indicando sucesso

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
    
    


        
        
def listarSolicitacoesNotificacao():
    try:
        projetos = [];
        
        # ExecuteReader retorna um conjunto de resultados
        result_table2 = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO, OCORRENCIA.DATA_HORA_SOL, CPE_CSC.OBJETO_CONTRATO, CPE_CSC.CSC_DATA_FIM, CPE_CSC.CSC_DGCO, CPE_CSC.OBSERVACAO, CP_ORDEM_SERVICO.NOME_FORNECEDOR, ORDEM_SERVICO.DESCRICAO_DETALHADA, PESSOA.NOME As FISCAL_DE_SERVICO, PESSOA1.NOME As FISCAL_ADM_DO_CONTRATO, PESSOA2.NOME As GESTOR_DO_CONTRATO, OCORRENCIA.ID_OCORRENCIA, PESSOA3.NOME As RESPONSAVEL, PESSOA3.USUARIO_REDE As USUARIO_RESPONSAVEL From OCORRENCIA Left Join CLASSE_SUB_PROCESSO On CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO = OCORRENCIA.ID_CLASSE_SUB_PROC_INI Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = CPE_CSC.FISCAL_DE_SERVICO Inner Join PESSOA PESSOA1 On PESSOA1.ID_PESSOA = CPE_CSC.FISCAL_ADM_DO_CONTRATO Inner Join PESSOA PESSOA2 On PESSOA2.ID_PESSOA = CPE_CSC.GESTOR_DO_CONTRATO Inner Join PESSOA PESSOA3 On PESSOA3.ID_PESSOA = OCORRENCIA.ID_RESPONSAVEL Where CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO = 600")
        
        
        for row in result_table2.Rows:
            projeto = {
                "identificador": row["ID_OCORRENCIA"],
                "numero": row["NUMERO"],
                "assunto": row["ASSUNTO"],
                "situacao": row["SITUACAO"],
                "dataHoraSolicitacao": row["DATA_HORA_SOL"],
                "fiscalServico": row["FISCAL_DE_SERVICO"],
                "fiscalAdmContrato": row["FISCAL_ADM_DO_CONTRATO"],
                "gestorContrato": row["GESTOR_DO_CONTRATO"],
                "objetoContrato": row["OBJETO_CONTRATO"],
                "fimVigenciaContrato": row["CSC_DATA_FIM"],
                "dgco": row["CSC_DGCO"],
                "observacao": row["OBSERVACAO"],
                "nomeFornecedor": row["NOME_FORNECEDOR"],
                "descricaoDetalhada": row["DESCRICAO_DETALHADA"],
                "responsavel": row["RESPONSAVEL"],
                "usuarioResponsavel": row["USUARIO_RESPONSAVEL"]
            }
            
            projetos.append(projeto)
            
        
        # Verificar se a lista de projetos está vazia
        if len(projetos) == 0:
            return 'Nenhum resultado encontrado!'

        # Serializar a lista de projetos para JSON
        json_data = JsonConvert.SerializeObject(projetos)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
        
        
        
        
def listarAvisosEncerramentoContratual():
    try:
        avisos = [];
        
        # ExecuteReader retorna um conjunto de resultados
        result_table = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO, OCORRENCIA.DATA_HORA_SOL, CPE_CSC.OBJETO_CONTRATO, CPE_CSC.CSC_DATA_FIM, CPE_CSC.CSC_DGCO, CPE_CSC.OBSERVACAO, CP_ORDEM_SERVICO.NOME_FORNECEDOR, ORDEM_SERVICO.DESCRICAO_DETALHADA, PESSOA.NOME As FISCAL_DE_SERVICO, PESSOA1.NOME As FISCAL_ADM_DO_CONTRATO, PESSOA2.NOME As GESTOR_DO_CONTRATO, OCORRENCIA.ID_OCORRENCIA, PESSOA3.NOME As RESPONSAVEL, PESSOA3.ID_PESSOA, PESSOA3.USUARIO_REDE As USUARIO_RESPONSAVEL From OCORRENCIA Left Join CLASSE_SUB_PROCESSO On CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO = OCORRENCIA.ID_CLASSE_SUB_PROC_INI Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = CPE_CSC.FISCAL_DE_SERVICO Inner Join PESSOA PESSOA1 On PESSOA1.ID_PESSOA = CPE_CSC.FISCAL_ADM_DO_CONTRATO Inner Join PESSOA PESSOA2 On PESSOA2.ID_PESSOA = CPE_CSC.GESTOR_DO_CONTRATO Inner Join PESSOA PESSOA3 On PESSOA3.ID_PESSOA = OCORRENCIA.ID_RESPONSAVEL Where CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO = 536")
        
        
        
        
        for row in result_table.Rows:
            aviso = {
                "identificador": row["ID_OCORRENCIA"],
                "numero": row["NUMERO"],
                "assunto": row["ASSUNTO"],
                "situacao": row["SITUACAO"],
                "dataHoraSolicitacao": row["DATA_HORA_SOL"],
                "fiscalServico": row["FISCAL_DE_SERVICO"],
                "fiscalAdmContrato": row["FISCAL_ADM_DO_CONTRATO"],
                "gestorContrato": row["GESTOR_DO_CONTRATO"],
                "objetoContrato": row["OBJETO_CONTRATO"],
                "fimVigenciaContrato": row["CSC_DATA_FIM"],
                "dgco": row["CSC_DGCO"],
                "observacao": row["OBSERVACAO"],
                "nomeFornecedor": row["NOME_FORNECEDOR"],
                "descricaoDetalhada": row["DESCRICAO_DETALHADA"],
                "responsavel": row["RESPONSAVEL"],
                "usuarioResponsavel": row["USUARIO_RESPONSAVEL"]
            }
            
            avisos.append(aviso)
            
        
        # Verificar se a lista de avisos está vazia
        if len(avisos) == 0:
            return 'Nenhum resultado encontrado!'

        # Serializar a lista de projetos para JSON
        json_data = JsonConvert.SerializeObject(avisos)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)







def listarTermosDesignacao():
    try:
        designacoes = [];
        
        # ExecuteReader retorna um conjunto de resultados
        result_table = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA As IDENTIFICADOR, OCORRENCIA.ASSUNTO As ASSUNTO, OCORRENCIA.DATA_HORA_SOL As DATA_HORA_SOL, OCORRENCIA.SITUACAO As SITUACAO, CPE_CONTRATOS02.DESIGNA_TITU_OR_SUP As TITULAR_SUPLENTE, CPE_CONTRATOS02.TIPO_DESIGNACAO_INTERV As TIPO_DESIGNACAO, CPE_FINANCEIRO.DGCO_BB As NUMERO_DGCO, PESSOA.NOME As DESIGNADO From OCORRENCIA Inner Join CPE_FINANCEIRO On OCORRENCIA.ID_OCORRENCIA = CPE_FINANCEIRO.ID_OCORRENCIA Inner Join CPE_CONTRATOS02 On OCORRENCIA.ID_OCORRENCIA = CPE_CONTRATOS02.ID_OCORRENCIA, CPE_CSC Inner Join CP_PESSOA On CPE_CSC.CSC_MATRICULA = CP_PESSOA.MATRICULA Inner Join PESSOA On CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA Where OCORRENCIA.ID_CLASSE_SUB_PROC_INI = 1236")
        
        
        # Verificar se a lista de avisos está vazia
        if len(result_table.Rows) == 0:
            return 'Nenhum resultado encontrado!'

        # Serializar a lista de projetos para JSON
        json_data = JsonConvert.SerializeObject(result_table)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)        
        
        

def listarAtestadosCapacidadeTecnica():
    try:
        atestados = [];
        
        # ExecuteReader retorna um conjunto de resultados
        result_table = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, OCORRENCIA.DATA_HORA_SOL, ORDEM_SERVICO.DESCRICAO_DETALHADA, OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ID_CLASSE_SUB_PROC_INI, CPE_FINANCEIRO.DGCO_BB, CP_ORDEM_SERVICO.NOME_FORNECEDOR, PESSOA.NOME As RESPONSAVEL, PESSOA.USUARIO_REDE As USUARIO_RESPONSAVEL From OCORRENCIA Inner Join ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = ORDEM_SERVICO.ID_OCORRENCIA Inner Join CPE_FINANCEIRO On OCORRENCIA.ID_OCORRENCIA = CPE_FINANCEIRO.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = OCORRENCIA.ID_RESPONSAVEL Where OCORRENCIA.ID_CLASSE_SUB_PROC_INI = 398")
        
        
        
        
        for row in result_table.Rows:
            atestado = {
                "identificador": row["ID_OCORRENCIA"],
                "numero": row["NUMERO"],
                "assunto": row["ASSUNTO"],
                "situacao": row["SITUACAO"],
                "dataHoraSolicitacao": row["DATA_HORA_SOL"],
                "descricaoDetalhada": row["DESCRICAO_DETALHADA"],
                "dgco": row["DGCO_BB"],
                "nomeFornecedor": row["NOME_FORNECEDOR"],
                "responsavel": row["RESPONSAVEL"],
                "usuarioResponsavel": row["USUARIO_RESPONSAVEL"]
            }
            
            atestados.append(atestado)
            
        
        # Verificar se a lista de avisos está vazia
        if len(atestados) == 0:
            return 'Nenhum resultado encontrado!'

        # Serializar a lista de projetos para JSON
        json_data = JsonConvert.SerializeObject(atestados)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
        
        
        
        

def listarSolicitacoesAditamento():
    try:
        atestados = [];
        
        # ExecuteReader retorna um conjunto de resultados
        result_table = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO, OCORRENCIA.DATA_HORA_SOL, CPE_CSC.OBJETO_CONTRATO, CPE_CSC.CSC_DATA_FIM, CPE_CSC.CSC_DGCO, CPE_CSC.OBSERVACAO, CP_ORDEM_SERVICO.NOME_FORNECEDOR, ORDEM_SERVICO.DESCRICAO_DETALHADA, PESSOA.NOME As FISCAL_DE_SERVICO, PESSOA1.NOME As FISCAL_ADM_DO_CONTRATO, PESSOA2.NOME As GESTOR_DO_CONTRATO, OCORRENCIA.ID_OCORRENCIA, PESSOA3.NOME As RESPONSAVEL, PESSOA3.USUARIO_REDE As USUARIO_RESPONSAVEL From OCORRENCIA Left Join CLASSE_SUB_PROCESSO On CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO = OCORRENCIA.ID_CLASSE_SUB_PROC_INI Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = CPE_CSC.FISCAL_DE_SERVICO Inner Join PESSOA PESSOA1 On PESSOA1.ID_PESSOA = CPE_CSC.FISCAL_ADM_DO_CONTRATO Inner Join PESSOA PESSOA2 On PESSOA2.ID_PESSOA = CPE_CSC.GESTOR_DO_CONTRATO Inner Join PESSOA PESSOA3 On PESSOA3.ID_PESSOA = OCORRENCIA.ID_RESPONSAVEL Where CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO = 379")
        
        
        
        
        for row in result_table.Rows:
            atestado = {
                "identificador": row["ID_OCORRENCIA"],
                "numero": row["NUMERO"],
                "assunto": row["ASSUNTO"],
                "situacao": row["SITUACAO"],
                "dataHoraSolicitacao": row["DATA_HORA_SOL"],
                "fiscalServico": row["FISCAL_DE_SERVICO"],
                "fiscalAdmContrato": row["FISCAL_ADM_DO_CONTRATO"],
                "gestorContrato": row["GESTOR_DO_CONTRATO"],
                "objetoContrato": row["OBJETO_CONTRATO"],
                "fimVigenciaContrato": row["CSC_DATA_FIM"],
                "dgco": row["CSC_DGCO"],
                "observacao": row["OBSERVACAO"],
                "nomeFornecedor": row["NOME_FORNECEDOR"],
                "descricaoDetalhada": row["DESCRICAO_DETALHADA"],
                "responsavel": row["RESPONSAVEL"],
                "usuarioResponsavel": row["USUARIO_RESPONSAVEL"]
            }
            
            atestados.append(atestado)
            
        
        # Verificar se a lista de avisos está vazia
        if len(atestados) == 0:
            return 'Nenhum resultado encontrado!'

        # Serializar a lista de projetos para JSON
        json_data = JsonConvert.SerializeObject(atestados)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
        
        
        
        

def listarRevisoesOrdemCompra():
    try:
        revisoes = [];
        
        # ExecuteReader retorna um conjunto de resultados
        result_table = DB.ExecuteDataTable("Select OCORRENCIA.ASSUNTO, OCORRENCIA.DATA_HORA_SOL, OCORRENCIA.ID_CLASSE_SUB_PROC_INI, OCORRENCIA.NUMERO, OCORRENCIA.SITUACAO, OCORRENCIA.ID_OCORRENCIA, ORDEM_SERVICO.DESCRICAO_DETALHADA, CP_ORDEM_SERVICO.CNPJ, CP_ORDEM_SERVICO.NOME_FORNECEDOR, CP_ORDEM_SERVICO.NUMERO_OC, CPE_CSC.CSC_DGCO, CPE_CSC.NUMERO_RC, ORDEM_SERVICO.JUSTIFICATIVA, CP_ORDEM_SERVICO.CPF, CPE_CSC.CSC_CPF, CPE_CSC.FISICA_JUDIRICA, CP_ORDEM_SERVICO.SIM_NAO, PESSOA.NOME As RESPONSAVEL, PESSOA.USUARIO_REDE As USUARIO_RESPONSAVEL From OCORRENCIA Inner Join ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = ORDEM_SERVICO.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On ORDEM_SERVICO.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = OCORRENCIA.ID_RESPONSAVEL Where OCORRENCIA.ID_CLASSE_SUB_PROC_INI = 395")
        
        
        
        
        for row in result_table.Rows:
            revisao = {
                "assunto": row["ASSUNTO"],
                "dataHoraSolicitacao": row["DATA_HORA_SOL"],
                "numero": row["NUMERO"],
                "situacao": row["SITUACAO"],
                "identificador": row["ID_OCORRENCIA"],
                "descricaoDetalhada": row["DESCRICAO_DETALHADA"],
                "cnpj": row["CNPJ"],
                "nomeFornecedor": row["NOME_FORNECEDOR"],
                "numeroOc": row["NUMERO_OC"],
                "numeroDgco": row["CSC_DGCO"],
                "numeroRc": row["NUMERO_RC"],
                "justificativa": row["JUSTIFICATIVA"],
                "cpf": row["CSC_CPF"],
                "fisicaJuridica": row["FISICA_JUDIRICA"],
                "simNao": row["SIM_NAO"],
                "responsavel": row["RESPONSAVEL"],
                "usuarioResponsavel": row["USUARIO_RESPONSAVEL"]
            }
            
            revisoes.append(revisao)
            
        
        # Verificar se a lista de avisos está vazia
        if len(revisoes) == 0:
            return 'Nenhum resultado encontrado!'

        # Serializar a lista de projetos para JSON
        json_data = JsonConvert.SerializeObject(revisoes)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
        
        
        
        

def listarAutorizacaoAlteracaoDadosBancarios():
    try:
        alteracoes = [];
        
        # ExecuteReader retorna um conjunto de resultados
        result_table = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ASSUNTO, OCORRENCIA.DATA_HORA_SOL, OCORRENCIA.ID_CLASSE_SUB_PROC_INI, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, CPE_CSC.BANCO_NOME, CPE_CSC.AGENCIA_NUMERO, CPE_CSC.CSC_DIGITO_AGENCIA, CPE_CSC.CONTA_CORRENTE_NUMERO, CPE_CSC.CSC_CPF, CPE_CONTRATOS.OBS2, CP_ORDEM_SERVICO.NOME_FORNECEDOR, CP_ORDEM_SERVICO.CNPJ_FORNECEDOR, CPE_CONTRATOS.OBS3, PESSOA.NOME As RESPONSAVEL, PESSOA.USUARIO_REDE As USUARIO_RESPONSAVEL From OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CPE_CONTRATOS On OCORRENCIA.ID_OCORRENCIA = CPE_CONTRATOS.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = OCORRENCIA.ID_RESPONSAVEL Where OCORRENCIA.ID_CLASSE_SUB_PROC_INI = 357")
        
        
        
        
        for row in result_table.Rows:
            alteracao = {
                "identificador": row["ID_OCORRENCIA"],
                "assunto": row["ASSUNTO"],
                "dataHoraSolicitacao": row["DATA_HORA_SOL"],
                "situacao": row["SITUACAO"],
                "numero": row["NUMERO"],
                "bancoNome": row["BANCO_NOME"],
                "agenciaNumero": row["AGENCIA_NUMERO"],
                "agenciaDigito": row["CSC_DIGITO_AGENCIA"],
                "numeroContaCorrente": row["CONTA_CORRENTE_NUMERO"],
                "nomeFornecedor": row["NOME_FORNECEDOR"],
                "cnpjFornecedor": row["CNPJ_FORNECEDOR"],
                "cpfFornecedor": row["CSC_CPF"],
                "objetoContratacao": row["OBS2"],
                "observacoes": row["OBS3"],
                "responsavel": row["RESPONSAVEL"],
                "usuarioResponsavel": row["USUARIO_RESPONSAVEL"]
            }
            
            alteracoes.append(alteracao)
        
        # Verificar se a lista de avisos está vazia
        if len(alteracoes) == 0:
            return 'Nenhum resultado encontrado!'

        # Serializar a lista de projetos para JSON
        json_data = JsonConvert.SerializeObject(alteracoes)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
        
        
        
        

def listarSolicitacoesProrrogacao():
    try:
        prorrogacoes = [];
        
        # ExecuteReader retorna um conjunto de resultados
        result_table = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ASSUNTO, OCORRENCIA.DATA_HORA_SOL, OCORRENCIA.ID_CLASSE_SUB_PROC_INI, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, CPE_CSC.OBJETO_CONTRATO, CPE_CSC.CSC_DGCO, CPE_CSC.CSC_DATA_FIM, CPE_CSC.OBSERVACAO, CP_ORDEM_SERVICO.NOME_FORNECEDOR, PESSOA.NOME As GESTOR_DO_CONTRATO, PESSOA1.NOME As FISCAL_ADM_DO_CONTRATO, PESSOA2.NOME As FISCAL_DE_SERVICO, ORDEM_SERVICO.DESCRICAO_DETALHADA, PESSOA3.NOME As RESPONSAVEL, PESSOA3.USUARIO_REDE As USUARIO_RESPONSAVEL From OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = CPE_CSC.GESTOR_DO_CONTRATO Inner Join PESSOA PESSOA1 On PESSOA1.ID_PESSOA = CPE_CSC.FISCAL_ADM_DO_CONTRATO Inner Join PESSOA PESSOA2 On PESSOA2.ID_PESSOA = CPE_CSC.FISCAL_DE_SERVICO Inner Join ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA PESSOA3 On OCORRENCIA.ID_RESPONSAVEL = PESSOA3.ID_PESSOA Where OCORRENCIA.ID_CLASSE_SUB_PROC_INI = 899")
        
        
        for row in result_table.Rows:
            prorrogacao = {
                "identificador": row["ID_OCORRENCIA"],
                "assunto": row["ASSUNTO"],
                "dataHoraSolicitacao": row["DATA_HORA_SOL"],
                "situacao": row["SITUACAO"],
                "numero": row["NUMERO"],
                "objetoContrato": row["OBJETO_CONTRATO"],
                "dgco": row["CSC_DGCO"],
                "fimVigenciaContrato": row["CSC_DATA_FIM"],
                "observacao": row["OBSERVACAO"],
                "nomeFornecedor": row["NOME_FORNECEDOR"],
                "gestorContrato": row["GESTOR_DO_CONTRATO"],
                "fiscalAdmContrato": row["FISCAL_ADM_DO_CONTRATO"],
                "fiscalServico": row["FISCAL_DE_SERVICO"],
                "descricaoDetalhada": row["DESCRICAO_DETALHADA"],
                "responsavel": row["RESPONSAVEL"],
                "usuarioResponsavel": row["USUARIO_RESPONSAVEL"]
            }
            
            prorrogacoes.append(prorrogacao)
        
        # Verificar se a lista de avisos está vazia
        if len(prorrogacoes) == 0:
            return 'Nenhum resultado encontrado!'

        # Serializar a lista de projetos para JSON
        json_data = JsonConvert.SerializeObject(prorrogacoes)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
        
        
        
        

def listarRevisaoOCRateio():
    try:
        revisoes = [];
        
        # ExecuteReader retorna um conjunto de resultados
        result_table = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ASSUNTO, OCORRENCIA.DATA_HORA_SOL, OCORRENCIA.ID_CLASSE_SUB_PROC_INI, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, CPE_CSC.SIM_NAO1 As E_OC_CONTRATO, CPE_CSC.NUMERO_RC, CPE_CSC.CSC_DGCO, CPE_CSC.FISICA_JUDIRICA As FISICA_JURIDICA, CPE_CSC.CSC_CPF, CP_ORDEM_SERVICO.NUMERO_OC, CP_ORDEM_SERVICO.NOME_FORNECEDOR, CP_ORDEM_SERVICO.CNPJ, CP_ORDEM_SERVICO.SIM_NAO As NECESSARIO_REVISAR_RC, CPE_RECONHECER.JUSTIFGEREXEC, ORDEM_SERVICO.JUSTIFICATIVA, PESSOA.NOME As RESPONSAVEL, PESSOA.USUARIO_REDE As USUARIO_RESPONSAVEL From OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join CPE_RECONHECER On OCORRENCIA.ID_OCORRENCIA = CPE_RECONHECER.ID_OCORRENCIA Inner Join ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On OCORRENCIA.ID_RESPONSAVEL = PESSOA.ID_PESSOA Where OCORRENCIA.ID_CLASSE_SUB_PROC_INI = 636")
        
        
        for row in result_table.Rows:
            revisao = {
                "identificador": row["ID_OCORRENCIA"],
                "assunto": row["ASSUNTO"],
                "dataHoraSolicitacao": row["DATA_HORA_SOL"],
                "situacao": row["SITUACAO"],
                "numero": row["NUMERO"],
                "eOcDeContrato": row["E_OC_CONTRATO"],
                "numeroRc": row["NUMERO_RC"],
                "dgco": row["CSC_DGCO"],
                "fisicaJuridica": row["FISICA_JURIDICA"],
                "cpf": row["CSC_CPF"],
                "numeroOc": row["NUMERO_OC"],
                "nomeFornecedor": row["NOME_FORNECEDOR"],
                "cnpj": row["CNPJ"],
                "necessarioRevisarRc": row["NECESSARIO_REVISAR_RC"],
                "justificativaGerex": row["JUSTIFGEREXEC"],
                "justificativa": row["JUSTIFICATIVA"],
                "responsavel": row["RESPONSAVEL"],
                "usuarioResponsavel": row["USUARIO_RESPONSAVEL"]
            }
            
            revisoes.append(revisao)
        
        # Verificar se a lista de avisos está vazia
        if len(revisoes) == 0:
            return 'Nenhum resultado encontrado!'

        # Serializar a lista de projetos para JSON
        json_data = JsonConvert.SerializeObject(revisoes)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
        
        
        
        

def listarProcessosAdministrativos():
    try:
        processos = [];
        
        # ExecuteReader retorna um conjunto de resultados
        result_table = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ASSUNTO, OCORRENCIA.DATA_HORA_SOL, OCORRENCIA.ID_CLASSE_SUB_PROC_INI, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, CPE_CSC.CSC_DATA_FIM, CPE_CSC.CSC_DGCO, CPE_CSC.OBSERVACAO, PESSOA.NOME As FISCAL_ADM_DO_CONTRATO, PESSOA1.NOME As FISCAL_DE_SERVICO, PESSOA2.NOME As GESTOR_DO_CONTRATO, CP_ORDEM_SERVICO.NOME_FORNECEDOR, ORDEM_SERVICO.DESCRICAO_DETALHADA, CPE_CSC.OBJETO_CONTRATO, PESSOA3.NOME As RESPONSAVEL, PESSOA3.USUARIO_REDE As USUARIO_RESPONSAVEL From OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = CPE_CSC.FISCAL_ADM_DO_CONTRATO Inner Join PESSOA PESSOA1 On PESSOA1.ID_PESSOA = CPE_CSC.FISCAL_DE_SERVICO Inner Join PESSOA PESSOA2 On PESSOA2.ID_PESSOA = CPE_CSC.GESTOR_DO_CONTRATO Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA PESSOA3 On OCORRENCIA.ID_RESPONSAVEL = PESSOA3.ID_PESSOA Where OCORRENCIA.ID_CLASSE_SUB_PROC_INI = 598")
        
        
        for row in result_table.Rows:
            processo = {
                "identificador": row["ID_OCORRENCIA"],
                "assunto": row["ASSUNTO"],
                "dataHoraSolicitacao": row["DATA_HORA_SOL"],
                "situacao": row["SITUACAO"],
                "numero": row["NUMERO"],
                "dgco": row["CSC_DGCO"],
                "fimVigencia": row["CSC_DATA_FIM"],
                "observacao": row["OBSERVACAO"],
                "objeto": row["OBJETO_CONTRATO"],
                "gestorContrato": row["GESTOR_DO_CONTRATO"],
                "fiscalAdmContrato": row["FISCAL_ADM_DO_CONTRATO"],
                "fiscalServico": row["FISCAL_DE_SERVICO"],
                "nomeFornecedor": row["NOME_FORNECEDOR"],
                "descricaoDetalhada": row["DESCRICAO_DETALHADA"],
                "responsavel": row["RESPONSAVEL"],
                "usuarioResponsavel": row["USUARIO_RESPONSAVEL"]
            }
            
            processos.append(processo)
        
        # Verificar se a lista de avisos está vazia
        if len(processos) == 0:
            return 'Nenhum resultado encontrado!'

        # Serializar a lista de projetos para JSON
        json_data = JsonConvert.SerializeObject(processos)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
        
        
        
        

def listarDistratosRecisoes():
    try:
        processos = [];

        # ExecuteReader retorna um conjunto de resultados
        result_table = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ASSUNTO, OCORRENCIA.DATA_HORA_SOL, OCORRENCIA.ID_CLASSE_SUB_PROC_INI, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, CPE_CSC.NUMERO_DGCO, CPE_HOMOLOGACAO.TIP_SOLDR, ORDEM_SERVICO.DESCRICAO_DETALHADA, PESSOA.NOME As RESPONSAVEL, PESSOA.USUARIO_REDE As USUARIO_RESPONSAVEL From OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CPE_HOMOLOGACAO On OCORRENCIA.ID_OCORRENCIA = CPE_HOMOLOGACAO.ID_OCORRENCIA Inner Join ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On OCORRENCIA.ID_RESPONSAVEL = PESSOA.ID_PESSOA Where OCORRENCIA.ID_OCORRENCIA > 1690000 And OCORRENCIA.ID_CLASSE_SUB_PROC_INI = 380")
        
        
        for row in result_table.Rows:
            processo = {
                "identificador": row["ID_OCORRENCIA"],
                "assunto": row["ASSUNTO"],
                "dataHoraSolicitacao": row["DATA_HORA_SOL"],
                "situacao": row["SITUACAO"],
                "numero": row["NUMERO"],
                "dgco": row["NUMERO_DGCO"],
                "tipoSolicitacao": row["TIP_SOLDR"],
                "descricaoDetalhada": row["DESCRICAO_DETALHADA"],
                "responsavel": row["RESPONSAVEL"],
                "usuarioResponsavel": row["USUARIO_RESPONSAVEL"]
            }
            
            processos.append(processo)
        
        # Verificar se a lista de avisos está vazia
        if len(processos) == 0:
            return 'Nenhum resultado encontrado!'
            
        # Serializar a lista de projetos para JSON
        json_data = JsonConvert.SerializeObject(processos)
        return json_data
        
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
        
        
        
        
        
def enviaDadosAvaliacaoFornecedor():
    try:
        result_table2 = DB.ExecuteDataTable("Select CP_ORDEM_SERVICO.COMBOBOX As TIPO_FORMULARIO, CP_ORDEM_SERVICO.COMBOBOX1 As FISCAL_AVALIADOR, CP_ORDEM_SERVICO.NOME_FORNECEDOR As EMPRESA_CONTRATADA, CPE_CSC.CSC_DGCO As DGCO, CPE_CSC.CSC_OBS As OBJETO, CPE_CSC.CSC_DATA_FIM As VIGENCIA_CONTRATO, CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO, CPE_CONTRATOS02.UTILIZA_UNIFORMEEQUIPA_AVALI As UTLIZACAO_UNIFORME_EQUIPAMENTOS, CPE_CONTRATOS02.UNICADE_CLIMA_AVALI As UNIDADE_CLIMATIZACAO, CPE_CONTRATOS02.REALIZACAO_SERV_AVALI As REALIZACAO_SERV_PERIODICIDADE_DETERMINADA, CPE_CONTRATOS02.REALIZA_AVALI As REALIZACAO_SERV_MANUTENCAO_PREV, CPE_CONTRATOS02.MANUTENCAO_AVALI As MANUTENCAO_CONDICOES_SEGURANCA_E_HIGIENE, CPE_CONTRATOS02.DISPONIBILIDADE_AVALI As DISPONIBILIDADE_FERRAMENTAS_EQUIPAMENTOS, CPE_CONTRATOS02.COMPROVA_FORM_AVALI As COMPROVACAO_FORMACAO_TECNICAESPECIFICA, CPE_CONTRATOS02.APRESENTACAO_RELATO_AVALI As AP_RELATORIOS_OCORRENCIAS, CP_ORDEM_SERVICO.VALOR_COMPARACAO As MEDIA, CPE_CONTRATOS.AP_EXAME_AVALI As AP_EXAMES_ADMISSIONAIS, CPE_CONTRATOS.APRESENT_RELAC_AVALI As AP_RELACAO_EMPREGADOS_ALOCADOS, CPE_CONTRATOS.APRESENTA_BENS_AVALI As AP_BENS_CERTIFICACOES_EXIGIDAS, CPE_CONTRATOS.APRESENTA_DOC_AVALIACAO As APRESENT_DOCTECNICA, CPE_CONTRATOS.APRESENTA_TERMO_AVALI As AP_TERMO_GARANTIA_BENS, CPE_CONTRATOS.ATENDIMENTO_AVALI As ATENDIMENTO_INSTRUCOES_NORMATIVAS, CPE_CONTRATOS.COMPROVACAO_FORMAVALIACAO As COMPROVACAO_FORMACAOTECNICA, CPE_CONTRATOS.CONTROLE_ENTRADA_AVALI As CONTROL_ENTRADA_VISITANTES, CPE_CONTRATOS.CONTROLE_ENTRADAAVALI As CONTROL_ENTRADA_SAIDA_VEICULOS, CPE_CONTRATOS.CUMPRI_ACORD_AVALIACAO As CUMPRIMENTO_ACORDNV_SERVICO, CPE_CONTRATOS.CUMPRIMENTO_JORNADA_AVALI As CUMPRIMENTO_JORNADA_DIATRABALHO, CPE_CONTRATOS.CUMPRIMENTO_PRAZOSAVALI1 As CUMPRIMENTO_PRAZOS, CPE_CONTRATOS.ENTREGA_BENS_AVALI As ENTREGA_BENS_ESPECIFICACOES, CPE_CONTRATOS.ENTREGA_BENS_QUANTAVALI As ENTREGA_BENS_QUANT_SOLICITADAS, CPE_CONTRATOS.ENTREGA_PECAS_AVALI As ENTREGA_PECAS_REPARADAS_NOPRAZO, CPE_CONTRATOS.ENTREGA1AVALI1 As ENTREGA_RELAC_ALOCADOS, CPE_CONTRATOS.ENTREGA2AVALI1 As ENTREGACTPS, CPE_CONTRATOS.ENTREGA3AVALI1 As ENTREGA_EXAME, CPE_CONTRATOS.EXECUCAO_ROTINA1 As EXECUCAO_ROTINA_SERV, CPE_CONTRATOS.FISCALIZACAO_ENTRASAIDA_AVALI As FISCALI_ENTRA_SAI_MATERIAIS, CPE_CONTRATOS.INCIDENCIA_RESOLU_AVALI As INCENDENCIA_RESOLUCAO_OCORRENCIAS_RELACIONADAS, CPE_CONTRATOS.INCIDENCIA_RESOLU1 As INCENDENCIA_RESOLUCAO, CPE_CONTRATOS.INDICA_MANUAVALI As INDICACAO_MANUTENCAO_PREPOSTO_LOCAL_EXECUSERVICO, CPE_CONTRATOS.INDICACAO_E_MANUTENCAOAVALI1 As INDICACAO_MANUTENCAO_PREPOSTO, CPE_CONTRATOS.INSPECAO_AVALI As INSPECAO_POSTOS_VIGI, CPE_CONTRATOS.INTEGRIDADE_BENSAVALI As INTEGRIDADE_DOS_BENS, CPE_CONTRATOS.MANUTENCAO_BOM_ESTADO_AVALI1 As MANUTENCAO_BOM_ESTADO, CPE_CONTRATOS.MAO_DE_OBRAAVALIA1 As MAO_DE_OBRA, CPE_CONTRATOS.PERMISSAO_INGRESSOAVALI As PERMISSAO_INGRESSO_INSTALACOES, CPE_CONTRATOS.PRODUTO_LIMPEZAAVALI1 As PRODUTOS_LIMPEZAHIGIENE, CPE_CONTRATOS.REALIZACAO_RONDAAVALI As REALIZACAO_RONDAS, CPE_CONTRATOS.REGISTRO_OCORREAVALI As REGISTRO_DE_OCORRENCIAS, CPE_CONTRATOS.REPAROS_AVALI As REPAROS_ACORDO_QUALIDADE_ESTABELECIDA, CPE_CONTRATOS.REPASSE_VIGILANTES_AVALI As REPASSE_AOS_VIGILANTES, CPE_CONTRATOS.UTILIZA_EMBA_AVALI As UTILIZACAO_EMBALAGENS_APROPRIADAS, CPE_CONTRATOS.UTLILIZA_UNIFORMEAVALIA1 As UTILIZACAO_UNIFORME_EQUIPAMENTOS, CPE_CSC.OBS21 As JUSTIFICATIVA_AVALIACOES From CP_ORDEM_SERVICO Left Join OCORRENCIA On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Left Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Left Join CLASSE_SUB_PROCESSO On OCORRENCIA.ID_CLASSE_SUB_PROC = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO Left Join CPE_CONTRATOS On OCORRENCIA.ID_OCORRENCIA = CPE_CONTRATOS.ID_OCORRENCIA Left Join CPE_CONTRATOS02 On OCORRENCIA.ID_OCORRENCIA = CPE_CONTRATOS02.ID_OCORRENCIA Where CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO = 1146")

        
        json_data = JsonConvert.SerializeObject(result_table2)
        return json_data
    except Exception as e:
        return "Erro ao executar a consulta: " + str(e)
