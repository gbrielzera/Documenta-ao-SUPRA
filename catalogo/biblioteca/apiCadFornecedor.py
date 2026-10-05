# apiCadFornecedor
# Caminho: Catálogo > Biblioteca de scripts > apiCadFornecedor
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (3 variantes entre os XMLs; esta é a mais recente)

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

# Função para anexar um arquivo em base64 à OS
def anexar_arquivo_base64(nome_arquivo, arquivo_base64):
    try:
        caminho_arquivo = "\\\\santacruz1.cobra.com.br\\supravizio$\\" + nome_arquivo.ToString()
        bytes_arquivo = Convert.FromBase64String(arquivo_base64)
        
        if len(bytes_arquivo) < 10:
            Utils.LogError("Arquivo base64 muito pequeno: " + nome_arquivo, "anexar_arquivo_base64")
        
        File.WriteAllBytes(caminho_arquivo, bytes_arquivo)
        return caminho_arquivo
    except Exception as e:
        Utils.LogError("Erro ao processar arquivo base64: " + e.ToString(), "anexar_arquivo_base64" )
        raise

def processar_anexo(os, caminho, tipo_anexo):
    try:
        os.AnexaArquivo(caminho, tipo_anexo, True)
        return True
    except Exception as e:
        Utils.LogError("Erro ao anexar arquivo: " + e.ToString(), "Anexo")
        return False

# Função para validar campos obrigatórios
# Função para validar campos obrigatórios
def validar_campo_obrigatorio(dados, campos):
    campos_invalidos = []
 
    for campo in campos:
        if campo not in dados:
            campos_invalidos.append("{\"campo\": \"" + campo + "\", \"motivo\": \"ausente\"}")
        else:
            valor = dados[campo]
 
            if valor is None:
                campos_invalidos.append("{\"campo\": \"" + campo + "\", \"motivo\": \"nulo\"}")
            else:
                texto_valor = str(valor).strip()
                if texto_valor == "":
                    campos_invalidos.append("{\"campo\": \"" + campo + "\", \"motivo\": \"vazio\"}")
 
    if len(campos_invalidos) > 0:
        return (
            "{\"status\": \"erro\", "
            "\"mensagem\": \"Existem campos obrigatórios inválidos no XML.\", "
            "\"detalhes\": [" + ",".join(campos_invalidos) + "]}"
            "}"
        )
 
    return None

# Função principal: cadastrar subestabelecimento
def cadastrar_subestabelecimento(subestabelecimento):
    try:
        if not subestabelecimento:
            return ("{\"status\": \"erro\", \"mensagem\": \"Parâmetros obrigatórios ausentes: dados do subestabelecimento são requeridos.\", \"detalhes\": []}")
            
        dados = JObject.Parse(subestabelecimento)
        
        # Validação de campos obrigatórios
        campos_obrigatorios = ["fisica_juridica", "nome_fornecedor",  "objeto", "especif_tecnica", "tipo_fornecedor", "cep", "estado", "cidade", "bairro", "tipo_logradouro", "logradouro", "numero", "banco_nome", "agencia_numero", "digito_agencia", "conta_corrente_numero"]
        erro_campo = validar_campo_obrigatorio(dados, campos_obrigatorios)
        if erro_campo:
            return erro_campo 
        
        matricula = dados["solicitante"].ToString()
        idPessoa = 0
        
        if matricula is not None and not matricula.ToString().Trim() == "" and not String.IsNullOrEmpty(matricula):
            result_pessoa = DB.ExecuteDataTable("SELECT p.id_pessoa FROM pessoa p INNER JOIN cp_pessoa cpp ON p.id_pessoa = cpp.id_pessoa WHERE cpp.matricula ='" + matricula.ToString().Trim() + "'")

            for linha in result_pessoa.Rows:
                idPessoa = linha["ID_PESSOA"]

        # Verifica se a ordem de serviço pode ser criada
        #login = '***MASCARADO***'
        #login = '***MASCARADO***'
        login = dados["login"].ToString()
        assunto = "Cadastro fornecedor - Integração Portal Parceiro"
        ordem_servico = OrdemServico.Carrega(20)
        servico = Servico.Carrega("Sigla", "CADFORNEC")
        pessoa = Pessoa.Carrega('UsuarioRede', login)
        pessoa_contratos = Pessoa.Carrega('UsuarioRede', 'fila.csc.-.Contratos')
        
        os = OrdemServico.Nova(ordem_servico, 'CADASTROFORNECEDOR', 'INICIOCAD', assunto, servico, pessoa, pessoa_contratos)
        
        # Atribuindo valores aos campos da OS
        #Dados do Fornededor
        os["FISICA_JUDIRICA"] = dados["fisica_juridica"].ToString()
        os["NOME_FORNECEDOR"] = dados["nome_fornecedor"].ToString()
        idFornededor = dados["idFornededor"].ToString()
        
       
        if dados["fisica_juridica"].ToString() == "Pessoa Jurídica":
            
            os["CNPJ_FORNECEDOR"] = idFornededor
            os["NUMERO_FORNECEDOR"] = "0"+idFornededor[0:8]
            os["NUM_CHAVE"] = "0"+idFornededor[0:8]
            os["NUM_DOCU"] = idFornededor[8:12]
            os["NUM_ITEM"] = idFornededor[12:14]
            nome_endereco = idFornededor[8:12]+" "+idFornededor[12:14]
            os["FORNECEDOR1"] = 'CNPJ'
            
        else:
        
            os["CSC_CPF"] = idFornededor
            os["NUMERO_FORNECEDOR"] = idFornededor[0:9]
            os["NUM_CHAVE"] = idFornededor[0:9]
            os["NUM_DOCU"] = idFornededor[5:9]
            os["NUM_ITEM"] = idFornededor[9:12]
            nome_endereco = idFornededor[5:9]+" "+idFornededor[9:11]
            os["FORNECEDOR1"] = 'CPF'
        
        os["OBS2"] = dados["objeto"].ToString()
        os.DescricaoDetalhada = dados["especif_tecnica"].ToString() 
        os["TIPO_FORNECEDOR"] = dados["tipo_fornecedor"].ToString()
        os["MOTIVO_ATUAL_CADAS_FORN"] = dados["motivo"].ToString()
        os.Justificativa = dados["observacao"].ToString()
        os["TP_PARTE_RELACIONADA"] = "Não se Aplica"
        os["CONVENIADA"] = "Não"
        os["CSC_NOVO_ESTABELECIMENTO"] = nome_endereco
        
        if (not String.IsNullOrEmpty(idPessoa.ToString()) and idPessoa is not None and idPessoa.ToString().Trim() != "" and idPessoa != 0):
            os["FAVORECIDO_COBRA"] = idPessoa.ToString()
            
        try: 
        
            #Verifica se o fornecedor já está cadastrado no ERP
            sql = "select count(VENDOR_NAME) as contador from po_vendors where segment1 = '"+"0"+idFornededor[0:8]+"'"
            cont = DB.ExecuteScalar(sql)
            
            if cont.ToString() != '0':
                Utils.LogError("Erro ao processar Fornecedor. Este fornecedor já está cadastrado '" + idFornededor.ToString() , "ValidarFornededor")
                anexos_falhados.append(idFornededor.ToString())
                
        except Exception as e:
            Utils.LogError("Erro inesperado em cadastrar_subestabelecimento: " + str(e), "apiCadFornecedor")
            return ("{\"status\": \"erro\", \"mensagem\": \"Erro interno ao cadastrar fornecedor: " + str(e) + "\", \"detalhes\": [{\"sql\": \"" + sql.ToString() + "\"}]}")
          
          
####Grid Endereço Fornecedor
        
        pais = "Brazil"
        sigla_pais = "BR"
        
        cep = dados["cep"].ToString()
        estado = dados["estado"].ToString()
        cidade = dados["cidade"].ToString()
        bairro = dados["bairro"].ToString()
        tipo_logradouro = dados["tipo_logradouro"].ToString()
        logradouro = dados["logradouro"].ToString()
        numero = dados["numero"].ToString()
        
        idioma = "Brazilian Portuguese".ToString()
        pagamento = "True"
        compra = "True"
        
        # Processamento do endereço
        
        if cep and estado and cidade and bairro and tipo_logradouro and logradouro and numero and nome_endereco :
            
            os.AdicionaLinhaRegistro("CAD_ENDERECO_FORNECEDOR", ["PAIS", "SIGLA_PAIS", "CEP", "ESTADO", "CIDADE", "BAIRRO", "TIPO_LOGRADOURO", "LOGRADOURO", "NUMERO", "NOME_ENDERECO", "IDIOMA", "COMPRA", "PAGAMENTO"  ], [pais, sigla_pais, cep, estado, cidade, bairro, tipo_logradouro, logradouro, numero, nome_endereco, idioma, compra, pagamento])
            #Utils.LogInformation(custaDep + " - " + valor + " - " + data, "Guias")
        else:
            Utils.LogError("Dados do fornecedor incompleto " , "Erro " + idFornededor.ToString())
            anexos_falhados.append(idFornededor.ToString())
  
##############

####Grid Contatos
        contatos_token = dados["contatosFornecedor"]  # 'dados' já é NJL.JObject
        if contatos_token is None:
            Utils.LogInformation("Campo 'contatosFornecedor' ausente.", "contatos-erro")
        else:
            # Se já for JArray, usa direto; se vier como string/JValue, parseia para JArray
            if isinstance(contatos_token, JArray):
                array_contatos = contatos_token
            else:
                # Pode ser JValue/String; garantimos parse
                array_contatos = JArray.Parse(contatos_token.ToString())
                
            # Validação de campos obrigatórios (mantendo sua função)
            campos_obrigatorios = ["nome", "sobrenome", "email", "codigo_area", "telefone"]
            
            # Itera contatos
            for contato in array_contatos:
                erro_campo = validar_campo_obrigatorio(contato, campos_obrigatorios)
                
                if erro_campo:
                    # Se preferir não abortar tudo, use 'continue' ao invés de 'return'
                    return erro_campo

                # Normalizações
                nome = contato["nome"].ToString().Trim()
                sobrenome = contato["sobrenome"].ToString().Trim()
                email = contato["email"].ToString().Trim().ToLower()
                codigo_area = contato["codigo_area"].ToString().Trim()
                telefone = re.sub(r"\D+", "", contato["telefone"].ToString())

                # Processamento do endereço
                os.AdicionaLinhaRegistro("DIRETORIO_CONTATOS", ["NOME", "SOBRENOME", "EMAIL", "CODIGO_AREA", "TELEFONE"], [nome, sobrenome, email, codigo_area, telefone])
                #Utils.LogInformation(custaDep + " - " + valor + " - " + data, "Guias")
                os.Salva()
            
  
########Dados Bancários
        os["BANCO_NOME"] = dados["banco_nome"].ToString()
        os["AGENCIA_NUMERO"] = dados["agencia_numero"].ToString()
        os["CSC_DIGITO_AGENCIA"] = dados["digito_agencia"].ToString()
        os["CONTA_CORRENTE_NUMERO"] = dados["conta_corrente_numero"].ToString()
        os["OBS3"] = dados["obs"].ToString()




        # Definição da lista de anexos
        anexos = [
            {"nome": "nomeArqCNPJ", "conteudo": "cartaoCNPJ", "tipo": "CARTAOCNPJ"},
            {"nome": "nomeArqContrato", "conteudo": "contratoSocial", "tipo": "CONTRATOSOCIAL"},
            {"nome": "nomeArqDocs", "conteudo": "demaisDocumentos", "tipo": "ANEXO"},
            {"nome": "nomeArqFQ415", "conteudo": "fq415_064", "tipo": "FQ415064"},
            {"nome": "nomeArqProc", "conteudo": "procuracao", "tipo": "PROCURACAO"},
        ]

        anexos_falhados = []

        # Processamento dos anexos
        for anexo in anexos:
            try:
                nome_arquivo = dados[anexo["nome"]].ToString() if anexo["nome"] in dados else None
                conteudo_base64 = dados[anexo["conteudo"]].ToString() if anexo["conteudo"] in dados else None
                tipo_anexo = anexo["tipo"]

                if (not String.IsNullOrEmpty(nome_arquivo) and nome_arquivo != " ") and (not String.IsNullOrEmpty(conteudo_base64) and conteudo_base64.Trim().Length > 0):
                    caminho = anexar_arquivo_base64(nome_arquivo, conteudo_base64)
                    if not processar_anexo(os, caminho, tipo_anexo):
                        anexos_falhados.append(tipo_anexo)

            except Exception as e:
                Utils.LogError("Erro ao processar anexo '" + tipo_anexo + "': " + str(e), "AnexoLoop")
                anexos_falhados.append(tipo_anexo)

        # Salva a OS
        os.AvancaAtividade()
        os.Salva()

        # Monta a resposta
        if len(anexos_falhados) == 0:
            return "{\"status\": \"sucesso\", \"mensagem\": \"Cadastramento processado com sucesso\", \"detalhes\": [{\"numero_os\": \"" + os.Numero.ToString() + "\", \"status\": \"Chamado aberto\"}]}"
        else:
            return "{\"status\": \"sucesso_parcial\", \"mensagem\": \"Cadastramento processado, mas alguns anexos falharam.\", \"detalhes\": [{\"numero_os\": \"" + os.Numero.ToString() + "\", \"anexos_falhados\": " + JsonConvert.SerializeObject(anexos_falhados) + "}]}"
    
    except Exception as e:
        Utils.LogError("Erro inesperado em cadastrar_subestabelecimento: " + str(e), "apiCadFornecedor")
        return ("{\"status\": \"erro\", \"mensagem\": \"Erro interno ao cadastrar fornecedor: " + str(e) + "\", \"detalhes\": [{}]}")
    

        
def buscarOS(numeroOs):
    
    try:
        numeroOs_str = str(numeroOs).strip()
    except Exception as e:
        Utils.LogError("Erro ao converter numeroOs para string: " + str(e), "apiCadFornecedor")
        return "{\"status\": \"erro\", \"mensagem\": \"Parametro numeroOs inválido.\", \"detalhes\": [{}]}"
        
    if not numeroOs_str:
        Utils.LogError("Parametro numeroOs ausente ou em branco", "apiCadFornecedor")
        return "{\"status\": \"erro\", \"mensagem\": \"Parametro numeroOs ausente ou inválido.\", \"detalhes\": [{}]}"

    try:
        numeroOs_int = int(numeroOs_str)
    except:
        Utils.LogError("Parametro numeroOs deve ser inteiro. Valor: " + numeroOs_str, "apiCadFornecedor")
        return "{\"status\": \"erro\", \"mensagem\": \"Parametro numeroOs deve ser um número inteiro.\", \"detalhes\": [{}]}"
        
    try:
        # Verificação inicial do parâmetro
        if numeroOs is None or numeroOs.ToString().Trim() == "":
            Utils.LogError("Parametro numeroOs ausente ou inválido", "apiCadFornecedor")
            return "{\"status\": \"erro\", \"mensagem\": \"Parametro numeroOs ausente ou inválido.\", \"detalhes\": [{}]}"
            
        # Conversão e validação como número inteiro
        try:
            numeroOs_int = int(numeroOs.ToString().Trim())
        except:
            Utils.LogError("Parametro numero Os deve ser um número inteiro válido. Valor recebido: " + numeroOs.ToString(), "apiCadFornecedor")
            return "{\"status\": \"erro\", \"mensagem\": \"Parametro numero Os deve ser um número inteiro.\", \"detalhes\": [{}]}"
            
        # Montagem do SQL seguro (com número convertido e seguro)
        sql = """
        SELECT ocorrencia.id_ocorrencia, ocorrencia.numero, ocorrencia.assunto, ocorrencia.situacao,
               classe_sub_processo.id_classe_sub_processo, ocorrencia.data_hora_sol, cpe_contratos.obs2, 
               cpe_csc.tipo_fornecedor, cpe_csc.motivo_atual_cadas_forn, cp_ordem_servico.favorecido_cobra, 
               ordem_servico.justificativa, pessoa.nome AS cliente, pessoa1.nome AS solicitante, 
               pessoa2.nome AS responsavel, classe_sub_processo.sigla 
        FROM ocorrencia 
        INNER JOIN classe_sub_processo ON classe_sub_processo.id_classe_sub_processo = ocorrencia.id_classe_sub_proc_ini 
        LEFT JOIN cpe_csc ON ocorrencia.id_ocorrencia = cpe_csc.id_ocorrencia 
        LEFT JOIN cp_ordem_servico ON ocorrencia.id_ocorrencia = cp_ordem_servico.id_ocorrencia 
        LEFT JOIN ordem_servico ON ocorrencia.id_ocorrencia = ordem_servico.id_ocorrencia 
        INNER JOIN pessoa ON pessoa.id_pessoa = ocorrencia.id_cliente 
        LEFT JOIN pessoa pessoa1 ON pessoa1.id_pessoa = ocorrencia.id_responsavel 
        LEFT JOIN pessoa pessoa2 ON pessoa2.id_pessoa = cpe_csc.gestor_do_contrato 
        LEFT JOIN pessoa pessoa3 ON pessoa3.id_pessoa = ocorrencia.id_responsavel 
        LEFT JOIN cpe_contratos ON ocorrencia.id_ocorrencia = cpe_contratos.id_ocorrencia 
        WHERE classe_sub_processo.id_classe_sub_processo IN (385) 
        AND ocorrencia.numero = '""" + str(numeroOs_int) + "'"
        
        # Execução da consulta
        result_table = DB.ExecuteDataTable(sql)
        
        # Verifica se houve retorno
        if result_table is None or result_table.Rows.Count == 0:
            Utils.LogInfo("Nenhum registro encontrado para numeroOs=" + str(numeroOs_int), "apiCadFornecedor")
            return "{\"status\": \"sucesso\", \"mensagem\": \"Nenhum registro encontrado.\", \"detalhes\": []}"
            
        # Serialização do resultado para JSON
        json_data = JsonConvert.SerializeObject(result_table)
        
        # Retorno com status OK
        return "{\"status\": \"sucesso\", \"mensagem\": \"Consulta realizada com sucesso.\", \"detalhes\": " + json_data + "}"
        
    except Exception as e:
        # Log de erro completo
        Utils.LogError("Erro ao executar a consulta para numeroOs=" + str(numeroOs) + ": " + str(e), "apiCadFornecedor")
        # Retorno de erro padronizado
        return "{\"status\": \"erro\", \"mensagem\": \"Erro ao executar a consulta.\", \"detalhes\": [{\"exception\": \"" + str(e).replace("\"", "'")
        
        
def reservaDGCO(DGCO):

    dadosRevDGCO = JObject.Parse(DGCO)
    
    if dadosRevDGCO["CNPJ"] is not None:
    
        campos_obrigatorios = ["JURIDICA_FISICA", "CNPJ","RAZAO_SOCIAL_CLIENTE","FORNECEDOR_CLIENTE","OBJETO_CONTRATACAO","DESCRICAO_DETALHADA"]
        
        erro_campo = validar_campo_obrigatorio(dadosRevDGCO, campos_obrigatorios)
        
    elif dadosRevDGCO["CPF"] is not None:
        
            
        campos_obrigatorios = ["JURIDICA_FISICA","CPF","RAZAO_SOCIAL_CLIENTE","FORNECEDOR_CLIENTE","OBJETO_CONTRATACAO","DESCRICAO_DETALHADA"]
        
        erro_campo = validar_campo_obrigatorio(dadosRevDGCO, campos_obrigatorios)
        
    if erro_campo:
        return erro_campo
    #else:
    #    return ("Campos Completos")
        
    
    #login = '***MASCARADO***'
    login = '***MASCARADO***'
    assunto = "Reserva DGCO - Integração Portal Parceiro"
    ordem_servico = OrdemServico.Carrega(20)
    servico = Servico.Carrega("Sigla", "DGCO")
    pessoa = Pessoa.Carrega('UsuarioRede', login)
    pessoa_contratos = Pessoa.Carrega('UsuarioRede', 'fila.csc.-.Contratos')
    
    os = OrdemServico.Nova(ordem_servico, 'SOLICITRESERVDG', 'WEBRESERVDGCO', assunto, servico, pessoa, pessoa_contratos)
    
    os["JURIDICA_FISICA"] = dadosRevDGCO["JURIDICA_FISICA"].ToString()
    os["RAZAO_SOCIAL_CLIENTE"] = dadosRevDGCO["RAZAO_SOCIAL_CLIENTE"].ToString()
    os["COMBOBOX1"] = dadosRevDGCO["FORNECEDOR_CLIENTE"].ToString()
    os["OBJETO_CONTRATACAO"] = dadosRevDGCO["OBJETO_CONTRATACAO"].ToString()
    os.DescricaoDetalhada = dadosRevDGCO["DESCRICAO_DETALHADA"].ToString()
    
        
    if dadosRevDGCO["CNPJ"] is None or "":
        
        os["CSC_CPF"] = dadosRevDGCO["CPF"].ToString()
    else:
        
        os["CNPJ"] = dadosRevDGCO["CNPJ"].ToString()
    
    if dadosRevDGCO["ANEXO_NOME"].ToString() is not None:

        nome_arquivo = "ANEXO_OS_"+os.Numero.ToString()+dadosRevDGCO["ANEXO_NOME"].ToString()
        conteudo_base64 = dadosRevDGCO["ANEXO_CONTEUDO"].ToString()

        if (not String.IsNullOrEmpty(nome_arquivo) and nome_arquivo != " ") and (not String.IsNullOrEmpty(conteudo_base64) and conteudo_base64.Trim().Length > 0):

            caminho = anexar_arquivo_base64(nome_arquivo, conteudo_base64)
            os.AnexaArquivo(caminho,"ANEXO", True)
            
            
    os.AvancaAtividade()    
    os.Salva()
    
    return ("Segue o numero da solicitação: "+os.Numero.ToString())
    #return(nome_arquivo)   
        
#    Busca informações detalhadas de uma Ordem de Serviço (OS) no banco de dados. 
# 
#    Esta função realiza a validação do parâmetro de entrada, executa uma consulta 
#    SQL que integra dados de diversas tabelas relacionadas à OS e retorna o 
#    resultado em formato JSON. 
# 
#    Etapas executadas: 
#    1. Valida se o número da OS foi informado e se é um número inteiro válido. 
#    2. Monta e executa uma consulta SQL com informações da OS e seus relacionamentos 
#       (ocorrência, tipo de processo, dados contratuais, favorecido, justificativas, 
#       e informações de pessoas envolvidas). 
#    3. Retorna um JSON contendo o resultado da consulta ou uma mensagem de "nenhum registro encontrado". 
#    4. Em caso de falha, retorna uma mensagem de erro padronizada com detalhes da exceção. 
#    5. Registra logs de erro e informações no log da aplicação. 
# 
#    Parâmetros: 
#    ---------- 
#    numeroOs : int or string 
#        Número da Ordem de Serviço a ser consultada. 
# 
#    Retorno: 
#    ------- 
#    str (JSON formatado) 
#        Exemplo de retorno de sucesso: 
#        { 
#            "status": "sucesso", 
#            "mensagem": "Consulta realizada com sucesso.", 
#            "detalhes": [ { ... dados da OS ... } ] 
#        } 
# 
#        Exemplo de retorno de erro: 
#        { 
#            "status": "erro", 
#            "mensagem": "Parametro numeroOs ausente ou inválido.", 
#            "detalhes": [{}] 
#        } 
#
