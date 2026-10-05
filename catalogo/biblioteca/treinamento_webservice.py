# treinamento_webservice
# Caminho: Catálogo > Biblioteca de scripts > treinamento_webservice
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

import clr
from System import *
from System.Text import StringBuilder
clr.AddReference("Supravizio.Custom") 
from Venki.Supravizio.Processo.Custom import OrdemServico
from Venki.Supravizio.Processo.Custom import Servico
from Venki.Supravizio.Recurso.Custom import Pessoa

     
def listaOS (chamado):
    xml = StringBuilder()
    try:
        dt = DB.ExecuteDataTable("select O.NUMERO as NUMERO, P.NOME as RESPONSAVEL FROM OCORRENCIA O INNER JOIN PESSOA P ON P.ID_PESSOA = O.ID_RESPONSAVEL INNER JOIN ATIVIDADE A ON A.ID_ATIVIDADE = O.ID_ATIVIDADE WHERE O.NUMERO = '"+chamado.ToString()+"'")
        if dt.Rows.Count > 0 :
            xml.AppendLine("<DADOS>")
            for dr in dt.Rows:
                xml.AppendFormat("<NUMERO>{0}</NUMERO>",dr["NUMERO"])
                xml.AppendFormat("<RESPONSAVEL>{0}</RESPONSAVEL>",dr["RESPONSAVEL"])
            xml.AppendLine("</DADOS>")
        else:
            xml.AppendLine("<DADOS>")
            xml.AppendFormat("<NUMERO>{0}</NUMERO>",0)
            xml.AppendFormat("<RESPONSAVEL>{0}</RESPONSAVEL>","Sem retorno")
            xml.AppendLine("</DADOS>")
    except Exception as e:
        xml.Append("Erro ao executar o webservice")
    return xml.ToString()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#def soma(a,b):
#    try: 
#        resultado = Convert.ToInt32(a) + Convert.ToInt32(b)
#        return resultado.ToString()
#    except Exception as e:
#        Utils.LogInformation("Método soma", "Soma")
#        return e.ToString()
#        
##    int x = 0;
##
##Int32.TryParse(TextBoxD1.Text, out x);
#
#def criarOs(novoassunto):
#    novaOS = OrdemServico.Nova(OrdemServico.Carrega("Numero", 1), "ADZAOTLTRBLHO", "INICIO", "Minhas Compras", Servico.Carrega("Sigla", "HEHIBBRIDO"), Pessoa.Carrega(25493), Pessoa.Carrega(25493))
#    novaOS.Assunto = novoassunto
#    novaOS.Salva()
#    return novaOS.Numero.ToString()
