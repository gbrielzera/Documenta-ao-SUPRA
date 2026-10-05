# apiProjuridArq
# Caminho: Catálogo > Biblioteca de scripts > apiProjuridArq
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

import clr
import time
from System import *
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("Supravizio.Custom")
from Newtonsoft.Json import *
from Newtonsoft.Json.Linq import *
from System.Net.Http import *
from System.Net.Http.Headers import *
from System.Text import *
from Venki.Supravizio.Processo.Custom import OrdemServico
from Venki.Supravizio.Processo.Custom import Servico
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Recurso.Custom import Tecnico
from System.IO import *
 
def pagJudiciais(assuntoGuia, ccMemo, referencia, titulo, processo, reclamante, reclamada, descricao, divisao, dtVenc, pagExcep, guiasJudiciais, arquivoBase64):
    # Validação manual do JSON
    jsonResult = None
    if not guiasJudiciais:
        Utils.LogError("guiasJudiciais está vazio")
        return "Erro: guiasJudiciais está vazio"
    
    try:
        jsonResult = JObject.Parse(guiasJudiciais)
    except Exception as e:
        Utils.LogError("Erro ao processar JSON de guias judiciais: " + str(e))
        return "Erro ao processar JSON: " + str(e)

    # Validação de parâmetros essenciais para criar uma OS
    if not processo or not reclamante or not reclamada:
        Utils.LogError("Dados essenciais do processo estão faltando")
        return "Erro: Dados essenciais do processo estão faltando"

    # Verifica se a ordem de serviço pode ser criada
    login = '***MASCARADO***'
    assunto = "Projurid Solicitação de pagamento judicial"
    ordem_servico = OrdemServico.Carrega(20)
    servico = Servico.Carrega('Sigla', 'SOLPAGJUDAPP')
    pessoa = Pessoa.Carrega('UsuarioRede', login)
    pessoa_contratos = Pessoa.Carrega('UsuarioRede', 'fila.csc.-.Contratos')
    
    if not ordem_servico or not servico or not pessoa or not pessoa_contratos:
        Utils.LogError("Erro ao carregar parâmetros para criação da OS")
        return "Erro: Não foi possível carregar dados para criar a OS"
    
    os = OrdemServico.Nova(ordem_servico, 'APPSOLPAGJUD', 'OrdemServico.Novo()', assunto, servico, pessoa, pessoa_contratos)
    
    # Atribuindo valores aos campos da OS
    os["ASSUNTOMEMORANDO"] = assuntoGuia if assuntoGuia else "Assunto não especificado"
    os["CCMEMORANDO"] = ccMemo
    os["DATA_MEMORANDO"] = referencia
    os["REF_MEMORANDO"] = titulo
    os["PROCESSO_MEMORANDO"] = processo
    os["RECLAMANTE_MEMORANDO"] = reclamante
    os["RECLAMADAS_MEMORANDO"] = reclamada
    os.DescricaoDetalhada = descricao
    os["DIVISAO_JURIDICA"] = divisao
    os["DATA_VENCIMENTO"] = dtVenc
    os["SIM_NAO10"] = 'Não' if pagExcep == 'Nao' else pagExcep

    Utils.LogInformation(os.Numero.ToString(), "OS")
    
    # Valida se existem guias para processar
    if not jsonResult or not jsonResult["guias"]:
        Utils.LogError("Não há guias judiciais para processar")
        return "Erro: Não há guias judiciais para processar"

    # Processamento das guias judiciais
    for linha in jsonResult["guias"]:
        info = linha["custaDep"].ToString() if "custaDep" in linha else None
        valor = linha["valor"].ToString() if "valor" in linha else None
        data = linha["prazo"].ToString() if "prazo" in linha else None

        if info and valor and data:
            custaDep = "Depósito" if info == "Deposito" else info
            os.AdicionaLinhaRegistro("GUIASJUDICIAIS", ["CUSTASDEPOSITO", "VALOR", "PRAZO_FATAL"], [custaDep, valor, data])
            Utils.LogInformation(custaDep + " - " + valor + " - " + data, "Guias")
        else:
            Utils.LogError("Dados incompletos na linha da guia judicial")
            return "Erro: Dados incompletos na linha da guia judicial"

    # Tratamento do arquivo em base64 (se fornecido)
    if arquivoBase64:
        try:
            caminho_arquivo = "\\santacruz1.cobra.com.br\supravizio$/arquivo_recebido.pdf"  # Altere o caminho conforme necessário
            bytes_arquivo = Convert.FromBase64String(arquivoBase64)
            File.WriteAllBytes(caminho_arquivo, bytes_arquivo)
            os.AnexaArquivo(caminho_arquivo, "GUIASPAGAMENTO", True)
            Utils.LogInformation("Arquivo anexado com sucesso: "  + caminho_arquivo , "Arquivo")
        except Exception as e:
            Utils.LogError("Erro ao processar arquivo base64: " + str(e))
            return "Erro ao processar arquivo base64: " + str(e)

    # Tenta avançar a OS e salvar
    if os.Numero:
        os.AvancaAtividade()
        os.Salva()
        return os.Numero.ToString()
    else:
        Utils.LogError("Erro ao avançar ou salvar a OS")
        return "Erro: Não foi possível avançar ou salvar a OS"
