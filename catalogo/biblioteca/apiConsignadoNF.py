# apiConsignadoNF
# Caminho: Catálogo > Biblioteca de scripts > apiConsignadoNF
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (4 variantes entre os XMLs; esta é a mais recente)

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
            "\"mensagem\": \"Existem campos obrigatórios ausentes, nulos, em branco ou vazios no XML.\", "
            "\"detalhes\": [" + ",".join(campos_invalidos) + "]}"
            "}"
        )
 
    return None
    
def validar_login_e_obter_pessoa(login):
    if login is None or str(login).strip() == "":
        return None, (
            "{"
                "\"status\": \"erro\", "
                "\"mensagem\": \"Parâmetro obrigatório ausente: login do solicitante é requerido.\", "
                "\"detalhes\": [{\"campo\": \"login\"}]"
            "}"
        )
 
    try:
        pessoa = Pessoa.Carrega('UsuarioRede', login)
    except Exception as ex:
        return (
            "{"
                "\"status\": \"erro\", "
                "\"mensagem\": \"Erro ao buscar usuário no Supravizio.\", "
                "\"detalhes\": [{\"erro\": \"" + str(ex).replace("\"", "'") + "\"}]"
            "}"
        )
 
    if pessoa is None or pessoa.Id is None:
        return None, (
            "{"
                "\"status\": \"erro\", "
                "\"mensagem\": \"Usuário não encontrado para o login informado.\", "
                "\"detalhes\": [{\"campo\": \"login\", \"valor\": \"" + str(login) + "\"}]"
            "}"
        )
 
    return pessoa, None

# Função validar campo S/N
def eh_sim(valor):
    return valor is not None and str(valor).strip().upper() == 'S'
    
##################

def obter_valor_anexo(dados, chave_anexo, campo):
    try:
        if "anexos" not in dados or dados["anexos"] is None:
            return ""
 
        anexos = dados["anexos"]
 
        if chave_anexo not in anexos or anexos[chave_anexo] is None:
            return ""
 
        item = anexos[chave_anexo]
 
        if campo not in item or item[campo] is None:
            return ""
 
        return item[campo].ToString().strip()
 
    except Exception as e:
        Utils.LogError("Erro ao obter valor do anexo: " + str(e), "obter_valor_anexo")
        return ""
 
 
def validar_anexos_obrigatorios(dados, anexos_obrigatorios):
    anexos_invalidos = []
 
    if "anexos" not in dados or dados["anexos"] is None:
        return (
            "{\"status\": \"erro\", "
            "\"mensagem\": \"Objeto obrigatório 'anexos' ausente no payload. A OS não será gerada.\", "
            "\"detalhes\": [{\"campo\": \"anexos\", \"motivo\": \"ausente\"}]}"
        )
 
    for anexo in anexos_obrigatorios:
        chave_anexo = anexo["chave"]
        tipo = anexo["tipo"]
 
        nome_arquivo = obter_valor_anexo(dados, chave_anexo, "nomeArquivo")
        conteudo_base64 = obter_valor_anexo(dados, chave_anexo, "conteudo")
 
        if nome_arquivo == "":
            anexos_invalidos.append(
                "{\"tipo\": \"" + tipo + "\", \"campo\": \"anexos." + chave_anexo + ".nomeArquivo\", \"motivo\": \"nome do arquivo ausente ou vazio\"}"
            )
 
        if conteudo_base64 == "":
            anexos_invalidos.append(
                "{\"tipo\": \"" + tipo + "\", \"campo\": \"anexos." + chave_anexo + ".conteudo\", \"motivo\": \"conteúdo base64 ausente ou vazio\"}"
            )
 
    if len(anexos_invalidos) > 0:
        return (
            "{\"status\": \"erro\", "
            "\"mensagem\": \"Existem anexos obrigatórios ausentes, vazios ou sem conteúdo. A OS não será gerada.\", "
            "\"detalhes\": [" + ",".join(anexos_invalidos) + "]}"
        )
 
    return None

####################
    
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
        
#Anexar documento no Chamado        
def processar_anexo(os, caminho, tipo_anexo):
    try:
        os.AnexaArquivo(caminho, tipo_anexo, True)
        return True
    except Exception as e:
        Utils.LogError("Erro ao anexar arquivo: " + e.ToString(), "Anexo")
        return False

#Função PRINCIPAL
def cadastrar_nf_cliente(nf):

    try:
        if not nf:
            return ("{\"status\": \"erro\", \"mensagem\": \"Parâmetros obrigatórios ausentes: dados do da Nota fiscal são requeridos.\", \"detalhes\": []}")
            
        dados = JObject.Parse(nf)
        
        #Validação de campos obrigatórios
        campos_obrigatorios = ["login", "contratoOks", "quantidadeNfs", "gerenciaFaturamento", "negocioProduto", "valorFaturamentoTotal", "valorRebateGlosaMulta", "valorLiquidoFaturar", "repactuacao", "competencia", "dataVencimento", "declaracaoCienciaPenalidade", "primeiroFaturamento"]
        erro_campo = validar_campo_obrigatorio(dados, campos_obrigatorios)
        if erro_campo:
            return erro_campo 
        
        # continua processamento
        Utils.LogInformation("{\"status\": \"sucesso\", \"mensagem\": \"Validação de campos realizada com sucesso.\"}", "apiConsignadoNF")
        
        #Validar anexos obrigatórios
        anexos_obrigatorios = [
            {"chave": "aceiteCliente", "tipo": "ACEITECLIENTE"}
        ]
        
        # Regra: se for primeiro faturamento, exige documento adicional
        if eh_sim(str(dados["primeiroFaturamento"]).strip()):
            anexos_obrigatorios.append({"chave": "documentoAdicional", "tipo": "ARQUIVO"})
         
        erro_anexo = validar_anexos_obrigatorios(dados, anexos_obrigatorios)
        if erro_anexo:
            return erro_anexo
            
        # continua processamento
        Utils.LogInformation("{\"status\": \"sucesso\", \"mensagem\": \"Validação de anexos realizada com sucesso.\"}", "apiConsignadoNF")
        
        if str(dados["declaracaoCienciaPenalidade"]).strip() != 'S':
            Utils.LogInformation("{\"status\": \"erro\", \"mensagem\": \"Emissão de NF bloqueada: declaração de ciência de penalidade não aceita (valor recebido diferente de 'S').\"}", "apiConsignadoNF")
            return ("{\"status\": \"erro\", \"mensagem\": \"Emissão de NF bloqueada: declaração de ciência de penalidade não aceita (valor recebido diferente de 'S').\", \"detalhes\": []}")
            
        
        idPessoa = 0
        login = dados["login"].ToString()
        #login = '***MASCARADO***'
        
        pessoa, erro = validar_login_e_obter_pessoa(login)
        if erro:
            return erro
         
        idPessoa = pessoa.Id
        
        try:
            # Verifica se a ordem de serviço pode ser criada
            assunto = "Cadastro Nota Fiscal Cliente - Integração Portal Consignado"
         
            ordem_servico = OrdemServico.Carrega(20)
            if ordem_servico is None:
                return (
                    "{"
                        "\"status\": \"erro\", "
                        "\"mensagem\": \"Não foi possível carregar o modelo da ordem de serviço.\", "
                        "\"detalhes\": [{\"campo\": \"ordem_servico\", \"valor\": \"20\"}]"
                    "}"
                )
         
            servico = Servico.Carrega("Sigla", "EMISSAONFCLIENTE")
            if servico is None:
                return (
                    "{"
                        "\"status\": \"erro\", "
                        "\"mensagem\": \"Não foi possível carregar o serviço EMISSAONFCLIENTE.\", "
                        "\"detalhes\": [{\"campo\": \"servico\", \"valor\": \"EMISSAONFCLIENTE\"}]"
                    "}"
                )
         
            pessoa_contratos = Pessoa.Carrega("UsuarioRede", "fila.csc.-.Contratos")
            if pessoa_contratos is None:
                return (
                    "{"
                        "\"status\": \"erro\", "
                        "\"mensagem\": \"Não foi possível localizar a fila de contratos no Supravizio.\", "
                        "\"detalhes\": [{\"campo\": \"UsuarioRede\", \"valor\": \"fila.csc.-.Contratos\"}]"
                    "}"
                )
         
            os = OrdemServico.Nova(ordem_servico,"FATCLIEMISNF","INICIOCONSIG",assunto,servico,pessoa,pessoa_contratos)
         
            if os is None:
                return (
                    "{"
                        "\"status\": \"erro\", "
                        "\"mensagem\": \"Não foi possível inicializar a ordem de serviço.\", "
                        "\"detalhes\": []"
                    "}"
                )
         
            # Atribuindo valores aos campos da OS
            os["DGCO_BB"] = str(dados["dgcoBB"]).strip()
            os["OKS_FAT"] = str(dados["contratoOks"]).strip()
            os["NUM_DOCU"] = str(dados["quantidadeNfs"]).strip()
            os["GERENCIAS_FATURAMENTO"] = str(dados["gerenciaFaturamento"]).strip()
            os["COMBOBOX"] = str(dados["negocioProduto"]).strip()
            os["VLFAT_FAT"] = dados["valorFaturamentoTotal"].ToString().replace(".", ",")
            os["VALOR_AUTORIZADO"] = dados["bonus"].ToString().replace(".", ",")
            os["VLREBATE_FAT"] = dados["valorRebateGlosaMulta"].ToString().replace(".", ",")
            os["VALOR FAT LIQUIDO"] = dados["valorLiquidoFaturar"].ToString().replace(".", ",")
            os["SIM_NAO3"] = 'Sim' if eh_sim(str(dados["repactuacao"]).strip()) else 'Não'
            os["MESES_ANO"] = str(dados["competencia"]).strip()
            os["DTVENC_FAT"] = dados["dataVencimento"].ToString("yyyy-MM-dd")
            os["DESTNFSE_FAT"] = str(dados["emailsNotificacao"]).strip()
            os["DEC_AUX_HOM"] = True if eh_sim(str(dados["declaracaoCienciaPenalidade"]).strip()) else False
            os["SIM_NAO2"] = 'Sim' if eh_sim(str(dados["primeiroFaturamento"]).strip()) else 'Não'
            os["DESCRICAO_OBRIG"] = str(dados["descricaoQuestionamento"]).strip()
            os["SIM_NAO1"] = 'Sim' if eh_sim(str(dados["geraPagamentoFornecedor"]).strip()) else 'Não'
            os["SIM_NAO"] = 'Sim' if eh_sim(str(dados["temContrato"]).strip()) else 'Não'
            
        except Exception as e:
            Utils.LogError("Erro inesperado em cadastrar_nf_cliente: " + str(e), "apiConsignadoNF")
            return (
                "{"
                    "\"status\": \"erro\", "
                    "\"mensagem\": \"Erro interno ao cadastrar nota fiscal cliente: " + str(e).replace("\"", "'") + "\", "
                    "\"detalhes\": []"
                "}"
            )
        
        
 
        if eh_sim(str(dados["primeiroFaturamento"]).strip()):
            anexos_obrigatorios.append({"chave": "documentoAdicional", "tipo": "ARQUIVO"})
                    
        # Definição da lista de anexos
        anexos = [
            {"chave": "aceiteCliente", "tipo": "ACEITECLIENTE"},
            {"chave": "documentoAdicional", "tipo": "ARQUIVO"},
            {"chave": "rateioLocalidades", "tipo": "RATEIOLOCALIDADES"},
            {"chave": "outrosDocumentos", "tipo": "ANEXO"},
            {"chave": "parecerNovosNegocios", "tipo": "PARECERNOVOSNEG"},
            {"chave": "deAcordoNi006", "tipo": "DEACORDO"},
        ]
        
        anexos_falhados = []
            
        # Processamento dos anexos
        for anexo in anexos:
            try:
                chave_anexo = anexo["chave"]
                tipo_anexo = anexo["tipo"]
         
                nome_arquivo = obter_valor_anexo(dados, chave_anexo, "nomeArquivo")
                conteudo_base64 = obter_valor_anexo(dados, chave_anexo, "conteudo")
         
                if nome_arquivo != "" and conteudo_base64 != "":
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
        Utils.LogError("Erro inesperado em cadastrar_nf_cliente: " + str(e), "apiConsignadoNF")
        return ("{\"status\": \"erro\", \"mensagem\": \"Erro interno ao cadastrar Nota Fiscal Cliente: " + str(e) + "\", \"detalhes\": [{}]}")
