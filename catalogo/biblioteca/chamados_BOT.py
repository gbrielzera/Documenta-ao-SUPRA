# chamados_BOT
# Caminho: Catálogo > Biblioteca de scripts > chamados_BOT
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

import cronograma_dod_alocacao
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.
cronograma_dod_alocacao(NUMERO_OC, FASE, )cronograma_dod_alocacao(NUMERO_OC, FASE, )import clr
import time
from System import *
clr.AddReference("Supravizio.Custom")
from Venki.Supravizio.Processo.Custom import OrdemServico
from Venki.Supravizio.Processo.Custom import Servico
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Recurso.Custom import Tecnico
from System.Text import StringBuilder

 
def novoincidente(assunto, descricao, login, serv):
   s = Servico.Carrega("Sigla", serv)
   tecnico = s.ResponsavelTecnicoId
   os = OrdemServico.Nova(OrdemServico.Carrega(20),'INCISISTE', 'INICIOINCIDE',assunto , Servico.Carrega("Sigla", serv), Pessoa.Carrega("UsuarioRede",login) , Pessoa.Carrega ("Id",tecnico))
   os["TIC_DESCRICAO"] = descricao
   os.AvancaAtividade()
   os.Salva()
   return os.Numero.ToString()

def novochamado(assunto, descricao, justificativa, login):
   os = OrdemServico.Nova(OrdemServico.Carrega(20),'SOLUCTI', 'INICIOTIC',assunto , Servico.Carrega("Sigla", 'ERPPO2'), Pessoa.Carrega("UsuarioRede",login) , Pessoa.Carrega ("UsuarioRede",'fila.gerência.projetos.ti'))
   os["TIC_DESCRICAO"] = descricao
   os["TIC_JUSTIFICATIVA"] = justificativa
   os.AvancaAtividade()
   os.Salva()
   return os.Numero.ToString()

def testePaginaPCCS():
    return "http://santacruz.bbtecno.com.br/Supravizio/Portal/Classico/SIMULACAO_ADESAO.aspx"
    
   
def servico_subprocesso(tipoServico):
    
    qry = " SELECT DISTINCT S.Sigla AS SIGLA_SERVICO, S.Descricao AS DESC_SERVICO FROM Rest_Servico RS INNER JOIN Classe_Sub_Processo CSP ON Rs.Id_Classe_Sub_Processo = Csp.Id_Classe_Sub_Processo INNER JOIN Servico S ON Rs.Id_Servico = S.Id_Servico INNER JOIN Sub_Processo SP ON Sp.Id_Classe_Sub_Processo = Csp.Id_Classe_Sub_Processo INNER JOIN Desenho_Processo DP ON Dp.Id_Desenho_Processo = Sp.Id_Desenho_Processo INNER JOIN Processo PR ON PR.Id_Processo = Dp.Id_Processo INNER JOIN macro_processo mp ON mp.id_macro_processo = pr.id_macro_processo inner join Classe_Servico CS on Cs.Id_Classe_Servico = S.Id_Classe_Servico AND mp.DESCRICAO = 'Tecnologia da Informação Empresarial' WHERE Csp.Sigla = 'INCISISTE' And s.ativo = 'Sim' and Cs.Sigla = '" + tipoServico.ToString() + "' ORDER BY S.Descricao"
    
    servicos = DB.ExecuteDataTable(qry)
    
    xml = StringBuilder()

    if servicos.Rows.Count > 0:
        xml.AppendLine("<DATASET>")
        for row in servicos.Rows:
            xml.AppendLine("<SERVICO>")
            xml.AppendFormat("<ID>{0}</ID>", row['SIGLA_SERVICO'])
            xml.AppendFormat("<DESCRICAO>{0}</DESCRICAO>", row['DESC_SERVICO'])
            xml.AppendLine("</SERVICO>")
        xml.AppendLine("</DATASET>")

    
        return xml.ToString()

        
def tipoServico():
    
    #qry = " SELECT DISTINCT Cs.Sigla, Cs.Descricao FROM Rest_Servico RS INNER JOIN Classe_Sub_Processo CSP ON Rs.Id_Classe_Sub_Processo = Csp.Id_Classe_Sub_Processo INNER JOIN Servico S ON Rs.Id_Servico = S.Id_Servico INNER JOIN Sub_Processo SP ON Sp.Id_Classe_Sub_Processo = Csp.Id_Classe_Sub_Processo INNER JOIN Desenho_Processo DP ON Dp.Id_Desenho_Processo = Sp.Id_Desenho_Processo INNER JOIN Processo PR ON PR.Id_Processo = Dp.Id_Processo INNER JOIN macro_processo mp ON mp.id_macro_processo = pr.id_macro_processo inner join Classe_Servico CS on Cs.Id_Classe_Servico = S.Id_Classe_Servico AND mp.DESCRICAO = 'Tecnologia da Informação Empresarial' WHERE Csp.Sigla = 'INCISISTE' And s.ativo = 'Sim' ORDER BY cS.Descricao"
    qry = "select '1' as SIGLA, 'A' AS DESCRICAO FROM DUAL"
    
    tipoServicos = DB.ExecuteDataTable(qry)
    
    xml = StringBuilder()

    if tipoServicos.Rows.Count > 0:
        xml.AppendLine("<DATASET>")
        for row in tipoServicos.Rows:
            xml.AppendLine("<TIPOSERVICO>")
            xml.AppendFormat("<ID>{0}</ID>", row['SIGLA'])
            xml.AppendFormat("<DESCRICAO>{0}</DESCRICAO>", row['DESCRICAO'])
            xml.AppendLine("</TIPOSERVICO>")
        xml.AppendLine("</DATASET>")

    
        return xml.ToString()
        
def tabela_servico_subprocesso(tipoServico):
    
    qry = " SELECT DISTINCT S.Sigla AS SIGLA_SERVICO, S.Descricao AS DESC_SERVICO FROM Rest_Servico RS INNER JOIN Classe_Sub_Processo CSP ON Rs.Id_Classe_Sub_Processo = Csp.Id_Classe_Sub_Processo INNER JOIN Servico S ON Rs.Id_Servico = S.Id_Servico INNER JOIN Sub_Processo SP ON Sp.Id_Classe_Sub_Processo = Csp.Id_Classe_Sub_Processo INNER JOIN Desenho_Processo DP ON Dp.Id_Desenho_Processo = Sp.Id_Desenho_Processo INNER JOIN Processo PR ON PR.Id_Processo = Dp.Id_Processo INNER JOIN macro_processo mp ON mp.id_macro_processo = pr.id_macro_processo inner join Classe_Servico CS on Cs.Id_Classe_Servico = S.Id_Classe_Servico AND mp.DESCRICAO = 'Tecnologia da Informação Empresarial' WHERE Csp.Sigla = 'INCISISTE' And s.ativo = 'Sim' and Cs.Sigla = '" + tipoServico.ToString() + "' ORDER BY S.Descricao"
    
    servicos = DB.ExecuteDataTable(qry)
    
    return servicos.ToString()
